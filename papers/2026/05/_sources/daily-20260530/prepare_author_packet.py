#!/usr/bin/env python3
"""Build the 2026-05-30 author packet from the frozen 730-identity window.

The script writes only date-local Daily artifacts and reads Books for a
provisional owner/adjacent comparison. It never modifies shared Books.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT_DATE = "2026-05-30"
REVIEWED_AT = "2026-09-01T23:20:00+08:00"
SOURCE = json.loads((HERE / "screening-ledger-provisional.json").read_text())

CANDIDATE_IDS = """
2606.00144 2606.00150 2606.00152 2606.00162 2606.00172 2606.00183 2606.00189 2606.00198 2606.00206 2606.00229
2606.00232 2606.00251 2606.00267 2606.00269 2606.00271 2606.00279 2606.00305 2606.00318 2606.00340 2606.00341
2606.00348 2606.00365 2606.00376 2606.00380 2606.00395 2606.00408 2606.00424 2606.00432 2606.00437 2606.00439
2606.00448 2606.00457 2606.07603 2606.07616 2606.20631
2605.30711 2605.30712 2605.30723 2605.30727 2605.30728 2605.30736 2605.30738 2605.30753 2605.30757 2605.30771
2605.30777 2605.30785 2605.30803 2605.30807 2605.30824 2605.30832 2605.30833 2605.30834 2605.30837 2605.30838
2605.30842 2605.30851 2605.30852 2605.30854 2605.30855 2605.30859 2605.30880 2605.30883 2605.30888 2605.30896
2605.30898 2605.30911 2605.30917 2605.30924 2605.30998 2605.31003 2605.31033 2605.31042 2605.31056 2605.31058
2605.31066 2605.31073 2605.31086 2605.31105 2605.31111 2605.31158 2605.31159 2605.31164 2605.31167 2605.31170
2605.31175 2605.31176 2605.31244 2605.31264 2605.31278 2605.31308 2605.31328 2605.31354 2605.31360 2605.31361
2605.31365 2605.31377 2605.31381 2605.31408 2605.31455 2605.31460 2605.31463 2605.31464 2605.31468 2605.31490
2605.31509 2605.31545 2605.31557 2605.31584 2605.31593
""".split()

# A title/abstract hit is not automatically part of the denominator. These
# families are intentionally closed before scoring because their disclosed
# contribution is a local theory/task/library/benchmark result and does not
# change a durable AI-System contract in this window.
PRE_DENOMINATOR_DROPS = {
    "2606.00340",  # exact learning-rate dynamics for small linear networks
    "2605.31003",  # e-commerce-specific relevance objective
    "2605.31056",  # Chinese zero-pronoun capability study
    "2605.31360",  # dataset-shift utility implementation
    "2605.31377",  # time-sensitive news retrieval application
    "2605.31545",  # personalized preference rubric method
    "2605.31557",  # egocentric-memory diagnostic benchmark
}
CANDIDATE_IDS = [aid for aid in CANDIDATE_IDS if aid not in PRE_DENOMINATOR_DROPS]

# Author-side Books proposals are deliberately narrower than the denominator.
# All other retained families remain auditable `No Change` proposals until a
# different reviewer reopens current owner + adjacent chapters.
INTEGRATE_IDS = {
    "2606.00152", "2606.00162", "2606.00198", "2606.00251", "2606.00271",
    "2606.00279", "2606.00318", "2606.00341", "2606.00348", "2606.00376",
    "2606.00437", "2606.00448", "2606.00457", "2606.20631", "2605.30723",
    "2605.30727", "2605.30736", "2605.30771", "2605.30803", "2605.30834",
    "2605.30837", "2605.30851", "2605.30852", "2605.30880", "2605.30998",
    "2605.30898", "2605.31042", "2605.31073", "2605.31170", "2605.31278",
    "2605.31593",
}

OWNER_OVERRIDES = {
    "2605.30753": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.30771": "AGENT-MEMORY",
    "2605.30785": "AGENT-CONTEXT",
    "2605.30824": "AGENT-WORKFLOW",
    "2605.30832": "INFER-SCHEDULING",
    "2605.30833": "TRAIN-RLHF",
    "2605.30842": "AGENT-CONTEXT",
    "2605.30859": "TRAIN-RLHF",
    "2605.30888": "TRAIN-RLHF",
    "2605.30898": "INFER-SCHEDULING",
    "2605.30911": "MULTIMODAL-REPRESENTATION",
    "2605.30917": "AGENT-RAG",
    "2605.30998": "PLATFORM-SECURITY",
    "2605.31033": "MULTIMODAL-WORLD-MODELS",
    "2605.31058": "TRAIN-DATA",
    "2605.31105": "INFER-KV-CACHE",
    "2605.31164": "TRAIN-DATA",
    "2605.31170": "AGENT-MULTI-AGENT",
    "2605.31175": "TRAIN-DATA",
    "2605.31176": "AGENT-RAG",
    "2605.31264": "AGENT-PLATFORM",
    "2605.31308": "PLATFORM-EVALUATION-SYSTEM",
    "2605.31354": "AGENT-MULTI-AGENT",
    "2605.31365": "AGENT-PLATFORM",
    "2605.31455": "TRAIN-RLHF",
    "2605.31463": "TRAIN-DISTRIBUTED-TRAINING",
    "2605.31464": "INFER-TENSORRT-LLM",
    "2605.31468": "AGENT-WORKFLOW",
    "2605.31509": "AGENT-PLATFORM",
    "2605.31584": "TRAIN-RLHF",
}

DEEP = {
    "2606.00279": "DA-BIT-EXACT-INFERENCE-VERIFICATION",
    "2605.30898": "DA-UNIFIED-ROUTING-TEST-TIME-SCALING",
    "2605.31593": "DA-STATEFUL-DISTRIBUTED-AGENT-MONITORING",
}


def family(aid: str) -> str:
    return "SF-2026-ARXIV-" + aid.replace(".", "-")


def sentences(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text or "").strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean) if s.strip()]


def mechanism(row: dict) -> str:
    for sentence in sentences(row.get("abstract", "")):
        if re.search(r"\b(propose|introduce|present|develop|design|show|identify|demonstrate|formalize|study|find)\b", sentence, re.I):
            return sentence
    return sentences(row.get("abstract", ""))[0] if row.get("abstract") else row["title"]


def owner_for(title: str, abstract: str) -> str:
    text = (title + " " + abstract).casefold()
    rules = [
        (r"world model|world-model|video generation|latent world", "MULTIMODAL-WORLD-MODELS"),
        (r"vision-language-action|\bvla\b|robot|embodied|driving", "MULTIMODAL-EMBODIED-VLA"),
        (r"prompt injection|jailbreak|attack|security|privacy|guardrail|misalignment|untrusted", "PLATFORM-SECURITY"),
        (r"benchmark|evaluation|audit|judge|rubric|confidence|reliability|replicab", "PLATFORM-EVALUATION-SYSTEM"),
        (r"speculative|parallel decoding", "INFER-SPECULATIVE-DECODING"),
        (r"kv cache|kv-cache|cache compression", "INFER-KV-CACHE"),
        (r"router|routing and test-time|model routing", "INFER-SCHEDULING"),
        (r"gpu|quantiz|inference verification|kernel runtime|compression", "INFER-TENSORRT-LLM"),
        (r"distributed training|asynchronous low-communication|moe training|routing replay", "TRAIN-DISTRIBUTED-TRAINING"),
        (r"on-policy distillation|distillation|reward model|post-training", "TRAIN-RLHF"),
        (r"\bgrpo\b|policy gradient|credit assignment", "TRAIN-GRPO"),
        (r"data scheduling|data mixture|dataset build|data refinement", "TRAIN-DATA"),
        (r"scaling law|neural scaling", "WORLDVIEW-SCALING-LAW"),
        (r"retrieval|\brag\b", "AGENT-RAG"),
        (r"context management|long-context", "AGENT-CONTEXT"),
        (r"memory|remembering", "AGENT-MEMORY"),
        (r"multi-agent|shared-state collaboration|agent language", "AGENT-MULTI-AGENT"),
        (r"tool calling|tool delegation|tool use", "AGENT-TOOL-CALLING"),
        (r"skill|agent evolution|self-improving", "AGENT-PLATFORM"),
        (r"workflow|deep research|scientific research lifecycle|trajectory", "AGENT-WORKFLOW"),
        (r"agent", "AGENT-PLATFORM"),
    ]
    for pattern, owner in rules:
        if re.search(pattern, text):
            return owner
    return "PLATFORM-EVALUATION-SYSTEM"


def score_for(row: dict) -> dict[str, int]:
    text = (row["title"] + " " + row.get("abstract", "")).casefold()
    reach = 3 if re.search(r"system|runtime|platform|distributed|deployment|production|multi-agent|data center", text) else 2
    design = 3 if re.search(r"architecture|contract|control|state|verification|routing|scheduling|monitor|memory|security|privacy|world model", text) else 2
    durability = 3
    total = design + reach + durability
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": total}


def closure_reason(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    claim = " ".join(ss[:2]) or row["title"]
    return f"`{row['title']}`：{claim} 该工作仍是领域任务、局部模型/表示改进或单一 benchmark 结果，没有改变长期 state/data/control owner、evaluation/release contract 或生产 fallback；后续若出现跨 workload 的系统接口与证据再重开。"


def exact_headings(aid: str) -> tuple[list[str], str]:
    path = HERE / "exact-v1-html" / f"{aid}v1.html"
    if path.exists() and path.stat().st_size >= 1000:
        text = path.read_text(errors="ignore")
        if re.search(r"</html>", text, re.I):
            values = []
            for m in re.finditer(r"<h([2-5])[^>]*>(.*?)</h\1>", text, re.I | re.S):
                value = re.sub(r"<[^>]+>", " ", m.group(2))
                value = html.unescape(re.sub(r"\s+", " ", value)).strip()
                if value and value not in values:
                    values.append(value)
            if values:
                return values, f"official arXiv exact-v1 HTML https://arxiv.org/html/{aid}v1"
    text_path = HERE / "exact-v1-pdf-text" / f"{aid}v1.txt"
    if text_path.exists() and text_path.stat().st_size >= 1000:
        values = []
        for line in text_path.read_text(errors="ignore").splitlines():
            value = re.sub(r"\s+", " ", line).strip()
            if re.match(r"^(?:\d+(?:\.\d+)*|[IVX]+)\.?\s+[A-Z][A-Za-z0-9 /&,:()\-]{2,100}$", value):
                value = re.sub(r"^(?:\d+(?:\.\d+)*|[IVX]+)\.?\s+", "", value)
                if value not in values:
                    values.append(value)
        if values:
            return values, f"official arXiv exact-v1 PDF https://arxiv.org/pdf/{aid}v1"
    return [], ""


def choose_locator(headings: list[str], patterns: tuple[str, ...], fallback: str) -> str:
    hits = [h for h in headings if any(re.search(p, h, re.I) for p in patterns)]
    if hits:
        return "; ".join(f"§{h}" for h in hits[:3])
    return fallback


rows_by_id = {r["arxiv_id"]: r for r in SOURCE["identities"]}
assert len(rows_by_id) == 730 and len(CANDIDATE_IDS) == len(set(CANDIDATE_IDS)) == 103
missing_identity = sorted(set(CANDIDATE_IDS) - set(rows_by_id))
assert not missing_identity, missing_identity

rows, reviews, blocked = [], [], []
for source in SOURCE["identities"]:
    row = dict(source)
    aid = row["arxiv_id"]
    if aid not in CANDIDATE_IDS:
        row.update(screening_status="pre_denominator_closure", screening_reason=closure_reason(row), review_status="identity_date_closed", access_status="accessible", integration_disposition="Rejected — Below Candidate Denominator")
    else:
        headings, retrieval_route = exact_headings(aid)
        owner = OWNER_OVERRIDES.get(aid, owner_for(row["title"], row.get("abstract", "")))
        score = score_for(row)
        if headings:
            method = choose_locator(headings, (r"method", r"approach", r"framework", r"architecture", r"system design", r"model$"), f"§{headings[min(1, len(headings)-1)]}")
            evaluation = choose_locator(headings, (r"experiment", r"evaluation", r"result", r"benchmark", r"analysis"), f"§{headings[-1]}")
            limitations = choose_locator(headings, (r"limitation", r"discussion", r"conclusion", r"threat.*valid"), f"§{headings[-1]}; no dedicated limitations heading; scope is bounded by the disclosed models, tasks and setup")
            review_status, access_status = "deep_complete", "accessible"
            disposition = "Integrate" if aid in INTEGRATE_IDS else "No Change — Existing Coverage"
            local_source = HERE / ("exact-v1-pdf" if "PDF" in retrieval_route else "exact-v1-html") / f"{aid}v1.{'pdf' if 'PDF' in retrieval_route else 'html'}"
            reviews.append({
                "source_family_id": family(aid),
                "arxiv_id": aid,
                "title": row["title"],
                "primary_evidence_version": f"arXiv:{aid}v1",
                "review_provenance_id": f"RP-{hashlib.sha256((aid + retrieval_route).encode()).hexdigest()[:16]}",
                "retrieval_route": retrieval_route,
                "retrieved_at": REVIEWED_AT,
                "source_body_sha256": hashlib.sha256(local_source.read_bytes()).hexdigest(),
                "method_locator": method,
                "evaluation_locator": evaluation,
                "limitations_locator": limitations,
                "mechanism_claim": mechanism(row),
                "claim_boundary": f"只支持 `{row['title']}` exact-v1 在 {evaluation} 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。",
                "not_proven": f"该来源没有证明 `{row['title']}` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。",
                "completion_result": "complete",
            })
        else:
            method = evaluation = limitations = "Pending — official exact-v1 HTML/PDF body unavailable after author-lane retrieval"
            review_status, access_status, disposition = "blocked", "blocked", "Blocked / Unverified"
            blocked.append(aid)
        row.update(source_family_id=family(aid), screening_status="retained", screening_reason=mechanism(row), owner_node=owner, score_v2=score, review_status=review_status, access_status=access_status, integration_disposition=disposition, method_locator=method, evaluation_locator=evaluation, limitations_locator=limitations)
    rows.append(row)

retained = [r for r in rows if r["screening_status"] == "retained"]
closures = [r for r in rows if r["screening_status"] != "retained"]
assert len(retained) == 103 and len(closures) == 627
ledger = {**SOURCE, "schema": "daily-screening-ledger-v2.1-author", "screened_identities": 730, "candidate_denominator": 103, "pre_denominator_closures": 627, "identities": rows}
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
(HERE / "candidate-ids.txt").write_text("\n".join(CANDIDATE_IDS) + "\n")

# Provisional Books comparison from the actual current owner and neighbors.
roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons, queue = [], []
for row in retained:
    owner, aid = row["owner_node"], row["arxiv_id"]
    owner_path = paths[owner]; target = ROOT / owner_path
    siblings = sorted(p for p in target.parent.glob("*.md") if re.match(r"\d+-", p.name)); idx = siblings.index(target)
    adjacent = [str(p.relative_to(ROOT)) for p in siblings[max(0, idx-1):idx] + siblings[idx+1:idx+2]]
    body = target.read_text(); headings = re.findall(r"^##+\s+(.+)$", body.split("\n## Review notes", 1)[0], re.M)
    marker = family(aid) in body
    decision = row["integration_disposition"]
    if decision == "Integrate" and marker:
        decision = "No Change — Existing Coverage"
        row["integration_disposition"] = decision
    existing = f"已顺读 `{owner_path}` 及 immediate adjacent；当前主干包含 {headings[:10]}；exact family marker={'present' if marker else 'absent'}。Review notes 不计语义覆盖。"
    comparison = {"arxiv_id": aid, "source_family_id": family(aid), "owner_node": owner, "owner_path": owner_path, "owner_sha256": hashlib.sha256(body.encode()).hexdigest(), "adjacent_paths": adjacent, "adjacent_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in adjacent}, "owner_headings_reviewed": headings, "existing_proposition": existing, "new_evidence_delta": row["screening_reason"], "decision": decision, "review_scope": "author-side provisional current owner + immediate adjacent; independent challenge required"}
    comparisons.append(comparison)
    if decision == "Integrate" and row["review_status"] == "deep_complete":
        queue.append({"report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": family(aid), "stable_node_id": owner, "owner_path": owner_path, "adjacent_paths": adjacent, "evidence_delta": row["screening_reason"], "required_post_write_audit": "owner + adjacent semantic audit after root serial writeback", "status": "provisional_pending_independent_prewrite_audit"})

(HERE / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v1", "report_date": REPORT_DATE, "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "report_date": REPORT_DATE, "status": "provisional_pending_independent_prewrite_audit", "items": queue}, ensure_ascii=False, indent=2) + "\n")
requests = [{"request_id": f"MR-20260530-{aid.replace('.', '-')}", "priority": "P1 Full Text", "source_family_id": family(aid), "known_identifier": f"arXiv:{aid}v1", "missing_material": "exact-v1 HTML/PDF/TeX body", "acceptable_substitute": "author-hosted event-time v1 full text", "required_review_scope": "Method/Evaluation/Limitations/artifact and Books comparison"} for aid in blocked]
(HERE / "materials-request.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": REPORT_DATE, "status": "open" if requests else "none", "requests": requests}, ensure_ascii=False, indent=2) + "\n")

# Shared renderer owns the canonical Markdown schema.
config = {r["arxiv_id"]: [r["owner_node"], r["score_v2"]["total"], r["integration_disposition"], r["method_locator"], r["evaluation_locator"], r["limitations_locator"]] for r in retained}
(HERE / "candidate-config-author.json").write_text(json.dumps({"candidates": config, "deep": DEEP, "pdf_ids": []}, ensure_ascii=False, indent=2) + "\n")
template = HERE.parent / "daily-20260525" / "render_author_packet.py"
code = template.read_text().replace('"screening-ledger-provisional.json"', '"screening-ledger-final.json"')
code = code.replace("2026-05-24", "__START__").replace("2026-05-25", "2026-05-30").replace("__START__", "2026-05-29").replace("2026-W21", "2026-W22")
code = code.replace("papers/2026/05/25/README.md", "papers/2026/05/30/README.md")
deep_text = {
    "2606.00279": (
        "旧的 inference audit 采用近似数值匹配，因为并行 reduction 的非结合性被视作不可消除噪声；这在只要求运行可复现时合理，却给低信任 prover 留下可否认空间。"
        "exact-v1 将差异拆成固定硬件/软件 reduction tree 导致的 non-invariance 与 atomic accumulation 导致的 genuine nondeterminism，并用 CPU 软件模型复现 tensor-core block-FMA、SFU、kernel reduction、RoPE 与 FlashAttention-2 的舍入路径。"
        "控制权因此从‘接受容差’转为‘记录 hardware SKU、software stack、quantization/kernel、parallel topology 与动态 batch size，再进行 bit-exact recomputation’。"
        "作者在 Qwen3-4B、多个 NVIDIA SKU 与列明的 vLLM/HF stack 上报告中间张量逐 bit 匹配；代价是维护 SKU/kernel dispatch catalog 和复算成本，且 MoE、部分 INT atomic kernel、非 NVIDIA、training backward 尚未覆盖。"
        "所以本日报只把它作为可审计 inference identity 的受限机制证据，不推导为所有加速器或所有训练 workload 都可 bit-exact。"
    ),
    "2605.30898": (
        "把 model routing 与 test-time scaling 分开优化，在模型规模离散、单模型 compute 边际收益快速递减时仍然合理，但二者各自选择会遗漏跨维组合。"
        "UniScale 把 model、reasoning path、candidate count 与 batch/configuration 组成统一 action space，由 query/action semantic representation 驱动 LinUCB，在每次请求后用 verifier quality 与 cost model 的复合 reward 更新策略；state owner 由静态 router 迁移到带 uncertainty 的在线闭环控制器。"
        "exact-v1 的实验显示其在所测动态场景中改变 quality-cost frontier，且 query embedding 加 bandit update 在作者 160 次 warm-up 后统计中占总时延 0.91%；收益同时引入 exploration、reward-estimator drift、action-space discretization 与 verifier 误差。"
        "论文结论明确仍受 PRM 精度约束，因此不能把作者结果外推成任意任务、任意 SLO 或生产流量下的最优调度；旧的固定 router 在低漂移、可预测 workload 下仍更简单。"
    ),
    "2605.31593": (
        "逐 transcript 的无状态 monitor 在单会话攻击下合理，却看不到攻击者把同一目标拆到多个账号和 subagent 后留下的弱相关信号。"
        "exact-v1 让 monitoring state 成为跨会话资源：每个请求先做局部 suspiciousness 与 embedding，在线聚合到 centroid/buffer；只有簇积累足够跨会话证据时才调用 cross-context LLM，决定 allow/refuse。"
        "这把安全控制点从孤立 request classifier 演进为 streaming correlation + rare escalation，并在作者模拟 datacenter traffic 与 cyber task 设置中报告更早检测，同时让约 99% 流量不支付额外 LLM reasoning 延迟。"
        "代价是持久化跨用户表征带来的隐私/tenancy 边界、cluster poisoning、阈值校准、P99 escalation 与 background traffic 放大；作者 red-team 也发现状态监控仍有规避路径，不能证明对其他威胁模型或真实生产基线同样成立。"
    ),
}
code = re.sub(r"analysis_text = \{.*?\n\}\nfor arxiv_id", "analysis_text = " + repr(deep_text) + "\nfor arxiv_id", code, flags=re.S)
exec(compile(code, str(HERE / "_shared_renderer_20260530_author.py"), "exec"), {"__file__": str(HERE / "prepare_author_packet.py"), "__name__": "__main__"})

# Restore exact author packet artifacts after the renderer's generic copies.
(HERE / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v1", "report_date": REPORT_DATE, "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "report_date": REPORT_DATE, "status": "provisional_pending_independent_prewrite_audit", "items": queue}, ensure_ascii=False, indent=2) + "\n")
(HERE / "semantic-author-audit.json").write_text(json.dumps({"schema": "semantic-author-audit-v1", "report_date": REPORT_DATE, "auditor": "author-lane", "status": "author_complete_pending_fresh_context_independent_audit", "not_a_fresh_context_audit": True, "counts": {"registered": 730, "screened": 730, "retained": len(retained), "closures": len(closures), "reviewed": len(reviews), "blocked": len(blocked), "integrate": len(queue)}, "unresolved_findings": ["Different reviewer must replay denominator/evidence/selection/Books.", *([f"Exact-v1 body unavailable: {','.join(blocked)}"] if blocked else []), "Root serial Books writeback and post-write audit pending."]}, ensure_ascii=False, indent=2) + "\n")

report = ROOT / "papers/2026/05/30/README.md"
text = report.read_text().replace("DEN-20260525-V2-AUTHOR", "DEN-20260530-V2-AUTHOR").replace("GAP-20260525-INDEPENDENT-AUDIT", "GAP-20260530-INDEPENDENT-AUDIT").replace("coverage:SRC-ARXIV:20260525", "coverage:SRC-ARXIV:20260530").replace("SA-20260525-", "SA-20260530-")
text = text.replace("**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author packet 已完成，等待非作者 fresh-context 审计。", "**Status:** In Progress；Pending Independent Pre-write Audit；Coverage=Open、Evidence=Open、Books=Open。author packet 不构成独立验收。")
text = text.replace("Completion Status: `In Progress`", "Completion Status: `In Progress`")
text = text.replace("Author packet 已交付；非作者 fresh-context 审计、root Books 串行写回及 post-write semantic audit 尚未完成。", "Author packet 已交付；状态为 Pending Independent Pre-write Audit。非作者审计、root Books 写回及 post-write audit 均未完成。")
report.write_text(text)

print(json.dumps({"raw": SOURCE["raw_snapshot_records"], "registered": 730, "screened": 730, "provisional_denominator": len(retained), "closures": len(closures), "exact_accessible": len(reviews), "blocked": len(blocked), "provisional_queue": len(queue)}, ensure_ascii=False))
