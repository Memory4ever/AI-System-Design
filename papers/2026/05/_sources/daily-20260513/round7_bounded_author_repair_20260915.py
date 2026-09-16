#!/usr/bin/env python3
"""Apply the exact bounded Round-7 author repair for 2026-05-13.

This script touches only the active evidence set and Daily for 2026-05-13.
It does not rediscover sources, expand the date window, or edit Books.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "papers/2026/05/_sources/daily-20260513"
REPORT = ROOT / "papers/2026/05/13/README.md"

PRIOR_APPLIED = {
    "2605.10974": 3487,
    "2605.11317": 352,
    "2605.11905": 1036,
    "2605.11931": 814,
    "2605.12201": 3501,
    "2605.12446": 3515,
}

N = {
    "2605.11136": {
        "node": "AGENT-MULTI-AGENT", "path": "books/part-07-agent/82-multi-agent.md",
        "anchor": "Participation Graph 与 Step Orchestration 是联合状态", "score": (3, 2, 3),
        "admission": "Multi-Agent 的 test-time learning 不能简化为 N 个单 Agent memory 更新：individual context、team composition/collaboration structure 与 population knowledge flow 是三个不同状态 owner。",
        "method": "§3.1–§3.5：CODREAM 在 team failure/disagreement 后做非对称经验路由；team operators 在线选择成员与协作结构；population lifecycle 执行 fork、merge、prune 与 seed。",
        "evaluation": "§4.1–§4.4：competition math、code 与 multi-domain reasoning 三条任务流；Qwen3-8B 在单 H100，另用 GPT-4.1-mini；报告 accuracy/pass@1/F1 与分层 ablation。",
        "limits": "Appendix A：只覆盖两个 model family；推理成本约为 single-agent 的 3.6 倍；lifecycle threshold 固定；更长流、credit attribution 和开放 population 未验证。",
        "artifact": "https://github.com/Mercury7353/EvoChamber；未确认与 exact-v1 绑定的 immutable commit。",
        "current": "Ch82 已把 participation graph、message identity 与 orchestration state 分开，但未承载 individual/team/population 三层联合演化、非对称知识转移和 population lifecycle 的状态边界。",
        "delta": "把 multi-agent test-time adaptation 从各 agent 的私有 memory 扩展为三层 versioned state；specialization 依赖非对称 transfer，而 fork/merge/prune/seed 必须由 population controller 提交。",
        "tradeoff": "更强跨 agent 学习换来额外推理、credit attribution、population churn、错误 transfer 与 specialization collapse。",
        "fallback": "短任务、固定团队或 lifecycle evidence 不足时，保留静态 team、局部 memory 和人工/确定性成员管理。",
    },
    "2605.11167": {
        "node": "AGENT-MULTI-AGENT", "path": "books/part-07-agent/82-multi-agent.md",
        "anchor": "Latent Communication 只能压缩 Payload，不能隐藏 Identity", "score": (3, 2, 2),
        "admission": "两个 frozen LM 可在每个 generation step 通过 trainable hidden-state interface 双向通信；这改变的不是消息格式，而是并发 agent 的同步、causal schedule 与 tool-state ownership。",
        "method": "§2.1–§2.4：两个 LM lockstep generation；neural interface 双向变换 hidden state，以 learned suppression gate 注入 residual，并对 tool output 维持因果放置。§3 只训练 interface。",
        "evaluation": "§4：calculator 与 Z3 两个 tool-use domain，比较独立模型、文本交流和 learned interface；§5 分析 gate 与 communication pattern。",
        "limits": "§5.4：双模型推理成本可能近似翻倍；GSM8K 在狭小 capability gap 下由 49.6 降至约 40；训练需要 task-specific causal placement annotation。",
        "artifact": "Not Disclosed：未找到与 exact-v1 绑定的公开 repository 或 immutable commit。",
        "current": "Ch82 已要求 latent handoff 保留 identity、version 和 commitment boundary，但未覆盖两个模型逐 token lockstep、双向 hidden-state coupling、suppression gate 与 tool causality 的联合 contract。",
        "delta": "latent channel 成为同步通信 plane：interface 只拥有 payload transform/gate，两个 frozen LM 各自拥有生成 state，tool runtime 仍拥有 effect commit；causal schedule 必须显式版本化。",
        "tradeoff": "降低文本通信开销但增加双模型 compute、同步阻塞、hidden-state coupling、不可解释通信和负迁移。",
        "fallback": "能力互补或因果标注不足时，回退显式 typed message/handoff、异步协作或单模型 tool loop。",
    },
    "2605.11169": {
        "node": "AGENT-TOOL-CALLING", "path": "books/part-07-agent/78-tool-calling.md",
        "anchor": "执行后行为只能更新下一次 Intent Gate", "score": (3, 2, 3),
        "admission": "在 frozen ReAct reasoner 与 tool execution 之间加入 deployment-time contextual bandit，使 action selection 能由 action-level feedback 在线更新，而不重训 reasoning model。",
        "method": "§4–§5：reasoner hidden state 作为 context；每个 action 保存线性 bandit sufficient statistics；UCB 同时估计 expected reward 与 uncertainty，以 rank-one update 吸收在线反馈。",
        "evaluation": "§6：ToolBench、TaskBench、TaskBench-MM 与 BFCL；Qwen3-4B 和 Mistral-7B fixed；以 reference completion 转换的 tool-multiset F1 比较 fixed selection 与 OLIVIA。",
        "limits": "无独立 Limitations。tool-multiset F1 不证明 effect success、permission safety 或生产 tail；开放 action space、non-stationary/adversarial feedback 和 unsafe exploration 未覆盖。",
        "artifact": "Not Disclosed：未确认公开代码或与 exact-v1 绑定的 immutable artifact。",
        "current": "Ch78 已规定执行结果只能更新下一次 intent proposal，authorizer/effect runtime 保留 commit authority；但未承载 frozen reasoner 之后的 per-action online statistics、UCB exploration 和 deployment-time decision-layer state。",
        "delta": "把 tool proposal policy 拆成可在线学习的 bandit state；feedback 更新 selector 而非 retrospective authorization，UCB uncertainty 只决定探索优先级，不能越过 permission/effect gate。",
        "tradeoff": "适应环境变化但引入冷启动、unsafe exploration、reward poisoning、per-action state 膨胀和 non-stationary regret。",
        "fallback": "高风险 action、反馈不可归因或 action space 快速变化时，回退 frozen policy、allowlist、offline evaluation 和显式审批。",
    },
    "2605.11225": {
        "node": "AGENT-PLANNING", "path": "books/part-07-agent/79-planning.md",
        "anchor": "Replanning 的触发条件", "score": (3, 2, 2),
        "admission": "把完整 trajectory 视为可版本化、可验证的优化状态：执行产生 discrepancy，再用 structured textual gradient 定位并替换 suffix，只有验证后不退化才提交。",
        "method": "§3：PLAN→INSPECT→EVOLVE→VERIFY；inspection 从 execution trace 生成 backward discrepancy/textual gradient，evolution 做 localized trajectory repair，acceptance 保持 incumbent 的 monotonicity。",
        "evaluation": "§4：DeepPlanning 与 GAIA；每个 domain 120 tasks；报告 composite/case metrics、token proxy、迭代收益和 component ablation。",
        "limits": "工具能力限制上界；GAIA basic toolkit 会使部分 refinement 退化为 retry；未直接测量 latency，token 只是 proxy；human-in-the-loop 上界不是 autonomous result。",
        "artifact": "Not Disclosed：未确认与 exact-v1 绑定的公开代码或 immutable commit。",
        "current": "Ch79 已有 observation-triggered replan、局部 replan 后的全约束复核和 completion evidence，但未把 accepted trajectory 作为 incumbent state，也未定义 backward discrepancy、suffix replacement 与 monotonic acceptance。",
        "delta": "replanning 从重新生成变成带版本与接受准则的 trajectory optimization：executor 提供观测，inspector 提出 discrepancy，evolver 只修改局部 suffix，verifier 独占 commit。",
        "tradeoff": "可定位失败并保留已验证 prefix，但增加执行、inspection、版本比较与 verifier 成本；错误 textual gradient 会稳定优化错误方向。",
        "fallback": "工具弱、验证不可靠或迭代预算耗尽时，回退从 checkpoint 全局 replan、保守 retry 或人工接管。",
    },
    "2605.11996": {
        "node": "PLATFORM-SECURITY", "path": "books/part-06-ai-infrastructure/72-security.md",
        "anchor": "Embedding 也是可执行数据供应链的一部分", "score": (3, 3, 3),
        "admission": "KG-derived soft prompt 是独立于可见文本的 graph-conditioned channel；攻击上游 KG representation 可在不改用户文本时改变模型行为，因此 graph→projector→prompt 必须成为供应链信任边界。",
        "method": "§III–§V：定义可修改上游 KG 的 attacker；用 semantic anchoring 维持表面任务相似，再分阶段优化 graph-level representation 与 soft-prompt effect。",
        "evaluation": "§VI：两类 KG-enhanced soft-prompt system、四个 dataset 与多种 backbone/attack/defense setting；报告 attack success、clean utility 与 defense response。",
        "limits": "无独立 Limitations。结论依赖攻击者可接触上游 KG、两个系统族及所测 dataset/backbone；不证明生产 prevalence 或 semantic-anchor detector 能普遍防御。",
        "artifact": "Not Disclosed：未确认与 exact-v1 绑定的公开 repository/commit。",
        "current": "Ch72 已将 embedding、prompt 和 model artifact 纳入供应链，并要求 provenance/identity，但未明确 KG-derived continuous soft prompt 作为旁路 conditioning channel，也未覆盖 graph-space semantic anchoring attack。",
        "delta": "安全 identity 必须绑定 KG snapshot、graph encoder/projector 与 model revision；soft prompt 只是 untrusted conditioning payload，semantic anchor 只能作 sensor，policy/effect gate 保留 authority。",
        "tradeoff": "图知识提升条件化能力却引入不可见 payload、projector drift、poisoned relation propagation 和检测器被规避。",
        "fallback": "provenance 缺失、graph drift 或 detector 不确定时，禁用 soft channel，回退 signed snapshot、文本化可审计 evidence 或隔离模型版本。",
        "handoff": "AGENT-RAG",
    },
    "2605.12477": {
        "node": "PLATFORM-EVALUATION-SYSTEM", "path": "books/part-06-ai-infrastructure/66-evaluation-system.md",
        "anchor": "动态知识系统需要关系型回归，而不只是静态答案分数", "score": (3, 3, 3),
        "admission": "长期 memory 不能只测静态 recall；多实体状态随时间变化时，Deletion、Cascade 与 Absence 分别测试过期事实、依赖传播和无证据拒答。",
        "method": "§3.1 定义 Deletion、Cascade、Absence 三类任务；§3.2 用有时间顺序的多实体 KG 生成 episode/dialog，并保留依赖关系与 expected state。",
        "evaluation": "§4：六个 memory system、三类 paradigm、100 episodes 与约 35k tokens；分别报告 retrieval/final-answer 及 intervention sweep，以区分 stage failure。",
        "limits": "§6：只有两个 handcrafted KG、LLM-generated dialogue、100 episodes、约 35K tokens；多项 ablation 只用小子集且仅英语。",
        "artifact": "https://seokwonjung-jay.github.io/meme-eval/；项目页提供 code/data，但未确认与 exact-v1 绑定的 immutable commit。",
        "current": "Ch66 已指出删除不是沉默、动态关系需回归，并区分 evidence 与 answer；但未形成 multi-entity evolving memory 的 Deletion/Cascade/Absence 三轴合同及 stage-diagnostic intervention。",
        "delta": "评估对象从单条 memory hit 扩展为 versioned entity-relation state；retriever、memory updater 和 answerer 分阶段验收，Cascade/Absence 让依赖传播与无证据拒答成为独立 release gate。",
        "tradeoff": "更能暴露关系错误，却增加 KG/episode 构造、时间真值、干预实验与 evaluator 成本；合成对话可能把生成器偏差写入基准。",
        "fallback": "领域关系或时间真值不可验证时，保留静态 recall 基线但降级声明，并用人工审计/append-only provenance 验收关键变化。",
        "handoff": "AGENT-MEMORY",
    },
}


def load(name: str):
    return json.loads((OUT / name).read_text())


def dump(name: str, value) -> None:
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def row_for(ledger: dict, aid: str) -> dict:
    return next(x for x in ledger["owner_day_screening"] if x["arxiv_id"] == aid)


def review_markdown(row: dict, meta: dict) -> str:
    family = row["source_family_id"]
    a, b, c = meta["score"]
    return "\n".join([
        f"<!-- review:{family}:start -->",
        f"#### {row['title']}", "",
        f"问题、旧基线与准入：{meta['admission']} 旧基线在新增状态、规模或风险约束不存在时仍合理。",
        f"Method / state ownership：{meta['method']} canonical owner=`{meta['node']}`；proposal/sensor 不自动取得 truth 或 commit authority。",
        f"Evaluation contract：{meta['evaluation']} V3={a}+{b}+{c}={a+b+c}。",
        f"Counterevidence / limitations：{meta['limits']}",
        f"Artifact：{meta['artifact']}",
        f"Trade-off / failure：{meta['tradeoff']}",
        f"Fallback / coexistence：{meta['fallback']}", "",
        f"<!-- claim:{family}:start -->exact-v1 只支持上述披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。<!-- claim:{family}:end -->", "",
        "Books Decision=`Integrate — Root write required`；author 只形成命题比较与 root serial queue，不修改共享 Books。",
        f"<!-- review:{family}:end -->",
    ])


def main() -> None:
    ledger = load("v3-active-ledger.json")
    evidence = load("v3-active-evidence.json")
    comparison = load("v3-books-comparison.json")
    queue = load("v3-root-writeback-queue.json")
    audit = load("v3-author-semantic-audit.json")

    # Reconcile the six already written families before opening new work.
    for aid, line in PRIOR_APPLIED.items():
        row = row_for(ledger, aid)
        row["integration_disposition"] = "Integrate — Applied"
        row["round7_state_reconciliation"] = "root binding verified; no pending root write"
        comp = next(x for x in comparison["comparisons"] if x.get("arxiv_id") == aid)
        comp.update({
            "author_decision": "Integrate — Applied",
            "requires_root_write": False,
            "source_binding_line": line,
            "postwrite_review_status": "passed_by_fresh_non_author_round6_reviewer",
        })
        item = next(x for x in queue["items"] if x.get("arxiv_id") == aid)
        item.update({
            "author_status": "applied_and_fresh_review_passed",
            "root_status": "applied_and_fresh_review_passed",
            "source_binding_line": line,
        })

    # Reopen exactly the six false negatives; no other identity is touched.
    new_reviews = []
    new_comparisons = []
    new_queue = []
    for aid, meta in N.items():
        row = row_for(ledger, aid)
        row.update({
            "screening_status": "retained",
            "screening_reason": meta["admission"],
            "review_status": "complete_exact_v1_round7_bounded_repair",
            "access_status": "accessible",
            "integration_disposition": "Integrate — Root write required",
            "withdrawal_status": "exact-v1 HTML accessible; no official withdrawal banner observed at 2026-09-15 review time",
            "stable_node_id": meta["node"],
            "score_v3": {"design_delta": meta["score"][0], "system_reach": meta["score"][1], "durability": meta["score"][2], "total": sum(meta["score"])},
            "active_v3_evidence_ref": f"v3-active-evidence.json#{row['source_family_id']}",
            "round7_bounded_author_repair": "reopened_false_negative_by_fresh_non_author_review",
        })
        family = row["source_family_id"]
        review = {
            "source_family_id": family, "arxiv_id": aid, "title": row["title"],
            "primary_evidence": f"https://arxiv.org/html/{aid}v1",
            "review_depth": "deep", "review_status": "complete_exact_v1_round7_bounded_repair",
            "access_status": "accessible", "reuse_basis": "fresh exact-v1 HTML review; no later revision imported",
            "withdrawal_check": row["withdrawal_status"],
            "semantic_admission_reason": meta["admission"], "method_locator": meta["method"],
            "evaluation_locator": meta["evaluation"], "limitations_locator": meta["limits"],
            "artifact_boundary": meta["artifact"],
            "claim_boundary": "Only exact-v1 disclosed workload, model, evaluator and assumptions are supported; no undisclosed production or cross-domain guarantee.",
            "detailed_review_markdown": review_markdown(row, meta),
        }
        if "handoff" in meta:
            review["related_owner_handoff"] = meta["handoff"]
        new_reviews.append(review)
        comp = {
            "source_family_id": family, "arxiv_id": aid, "title": row["title"],
            "stable_node_id": meta["node"], "owner_path": meta["path"],
            "anchor_heading": meta["anchor"], "anchor_line": None, "source_binding_line": None,
            "current_books_proposition": meta["current"], "new_evidence_delta": meta["delta"],
            "prior_disposition": "Rejected — Below Candidate Denominator",
            "author_decision": "Integrate — Root write required", "requires_root_write": True,
            "author_may_modify_books": False,
        }
        if "handoff" in meta:
            comp["related_owner_handoff"] = meta["handoff"]
        new_comparisons.append(comp)
        item = {
            "source_family_id": family, "arxiv_id": aid, "title": row["title"],
            "stable_node_id": meta["node"], "owner_path": meta["path"],
            "proposed_anchor": meta["anchor"], "semantic_delta": meta["delta"],
            "proposed_spine": "old baseline -> changed constraint -> mechanism/state ownership -> exact-v1 proof/non-proof -> trade-off/failure -> fallback/coexistence",
            "exact_v1_evidence": f"https://arxiv.org/html/{aid}v1",
            "old_baseline": "The simpler static, isolated or full-recompute path remains valid while the new scale/state/risk constraint is absent.",
            "constraint_change": meta["admission"], "mechanism_state_control": meta["delta"],
            "tradeoff_failure": meta["tradeoff"], "fallback_coexistence": meta["fallback"],
            "exact_v1_boundary": "Only exact-v1 disclosed workload/model/evaluator conditions are supported; no undisclosed production guarantee.",
            "method_locator": meta["method"], "evaluation_locator": meta["evaluation"],
            "limitations_locator": meta["limits"], "artifact_boundary": meta["artifact"],
            "author_status": "round7_author_ready_pending_root_serial_write",
            "root_status": "pending_root_serial_write",
        }
        if "handoff" in meta:
            item["related_owner_handoff"] = meta["handoff"]
        new_queue.append(item)

    # Append idempotently and preserve owner-day ordering.
    reopened = set(N)
    evidence["reviews"] = [x for x in evidence["reviews"] if x.get("arxiv_id") not in reopened] + new_reviews
    comparison["comparisons"] = [x for x in comparison["comparisons"] if x.get("arxiv_id") not in reopened] + new_comparisons
    queue["items"] = [x for x in queue["items"] if x.get("arxiv_id") not in reopened] + new_queue
    order = {x["arxiv_id"]: i for i, x in enumerate(ledger["owner_day_screening"])}
    ledger["candidate_ids"] = sorted({*ledger["candidate_ids"], *reopened}, key=lambda x: order[x])
    evidence["reviews"].sort(key=lambda x: order[x["arxiv_id"]])
    comparison["comparisons"].sort(key=lambda x: order[x["arxiv_id"]])
    queue["items"].sort(key=lambda x: order[x["arxiv_id"]])

    retained = sum(x["screening_status"] == "retained" for x in ledger["owner_day_screening"])
    closures = sum(x["screening_status"] == "pre_denominator_closure" for x in ledger["owner_day_screening"])
    ledger["counts"].update(retained_candidates=retained, pre_denominator_closures=closures)
    ledger["arithmetic"] = f"838 = ({retained} retained + {closures} pre-denominator closure + 0 withdrawn) official-owner route + 191 revision/non-owner-route isolation"
    ledger["round7_bounded_author_repair"] = {
        "scope_ids": list(N), "false_negatives_reopened": list(N),
        "owner_receipt_reenumerated": False, "isolation_touched": False,
        "books_edited_by_author": False, "prior_root_bindings_reconciled_applied": list(PRIOR_APPLIED),
        "root_queue_applied_before_new": 77, "root_queue_pending_after_new": 6,
    }
    evidence["candidate_count"] = retained
    evidence["books_writeback_status"] = "77 prior root applications reconciled and fresh-reviewed; 6 round7 root writes pending"
    comparison["comparison_count"] = len(comparison["comparisons"])
    comparison["requires_root_write_count"] = sum(bool(x.get("requires_root_write")) for x in comparison["comparisons"])
    comparison["root_applied_count_pending_fresh_review"] = 77
    comparison["status"] = "round7 bounded author repair complete; 77 prior root writes applied/fresh-reviewed; 6 new root writes pending"
    queue["queue_count"] = len(queue["items"])
    queue["root_applied_count"] = sum("applied" in str(x.get("root_status", "")) for x in queue["items"])
    queue["pending_root_count"] = sum(x.get("root_status") == "pending_root_serial_write" for x in queue["items"])
    queue["root_application_status"] = f"{queue['root_applied_count']} items applied/fresh-reviewed; {queue['pending_root_count']} round7 items pending root serial write"
    queue["status"] = "round7 queue ready; author did not edit shared Books; root serial write then fresh non-author review required"
    audit.update({
        "author_result": "round7_bounded_author_repair_complete_pending_root_and_fresh_non_author_review",
        "false_positive_scope": f"all {retained} retained candidates have identity, score, evidence, owner and disposition; semantic acceptance remains for a different reviewer",
        "required_next_reviewer": "root serial Books synthesis for six round7 items, then a different fresh-context non-author reviewer",
        "round7_scope_ids": list(N), "not_a_completion_signature": True,
    })

    dump("v3-active-ledger.json", ledger)
    dump("v3-active-evidence.json", evidence)
    dump("v3-books-comparison.json", comparison)
    dump("v3-root-writeback-queue.json", queue)
    dump("v3-author-semantic-audit.json", audit)

    # Produce bounded author and root handoff artifacts.
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    author_lines = [
        "# V3 Round 7 Bounded Author Repair — 2026-05-13", "",
        f"- Audit time: {now}", "- Scope: exactly six false negatives; no window/source/838-identity replay",
        "- Books mutation: none", f"- Denominator: {retained} retained + {closures} closure + 191 isolation = 838", "",
        "## Decisions", "",
    ]
    queue_lines = [
        "# V3 Round 7 Root Books Synthesis Queue — 2026-05-13", "",
        "Author evidence repair only; root must serialize these six writes and obtain a new non-author post-write review.", "",
    ]
    for aid, meta in N.items():
        row = row_for(ledger, aid)
        author_lines += [f"## {aid} — {row['title']}", "", meta["admission"], "", f"- V3: {sum(meta['score'])} ({meta['score'][0]}+{meta['score'][1]}+{meta['score'][2]})", f"- Owner: `{meta['node']}` → `{meta['path']}`", f"- Decision: Integrate — Root write required", f"- Evidence: https://arxiv.org/html/{aid}v1", f"- Withdrawal: no official banner observed", ""]
        queue_lines += [f"## {aid} — {row['title']}", "", f"- Owner/anchor: `{meta['node']}` → `{meta['path']}` / {meta['anchor']}", f"- Current proposition: {meta['current']}", f"- Semantic delta: {meta['delta']}", f"- Method: {meta['method']}", f"- Evaluation: {meta['evaluation']}", f"- Limitations: {meta['limits']}", f"- Trade-off/failure: {meta['tradeoff']}", f"- Fallback/coexistence: {meta['fallback']}", f"- Artifact: {meta['artifact']}", ""]
    author_lines += ["## Gate", "", "Author repair is complete but not a completion signature. Daily remains Ongoing pending root writes and a different fresh reviewer.", ""]
    (OUT / "V3_ROUND7_BOUNDED_AUTHOR_REPAIR_20260915.md").write_text("\n".join(author_lines))
    (OUT / "V3_ROUND7_ROOT_BOOKS_SYNTHESIS_QUEUE_20260915.md").write_text("\n".join(queue_lines))

    # Update the human report without regenerating unrelated sections.
    text = REPORT.read_text()
    intro_start = text.index("有界六项返修")
    intro_end = text.index("\n\n## 1. 结论", intro_start)
    text = text[:intro_start] + (
        "Round 6 的 6 项 root 写回已由 fresh non-author reviewer 逐项确认，状态已统一为 Applied。"
        "随后同一 reviewer 在冻结的 closure 中确认 6 个 false negative；本轮仅重开这些 family，未扩日期、来源或 838 个 identity。"
        "六项 exact-v1 均可访问且无官方 withdrawal banner，已完成深度证据审阅与逐命题 Books comparison；Daily 继续保持 Ongoing，等待 root 串行写入及新的独立写后复核。"
    ) + text[intro_end:]
    p1 = text.index("原始身份和窗口范围不变：", text.index("## 1. 结论"))
    p1e = text.index("\n\n", p1)
    text = text[:p1] + (
        f"原始身份和窗口范围不变：838 个 identity 中 647 个 official-owner-day、191 个 revision/non-owner-route isolation。"
        f"冻结分母为 {retained} retained / {closures} pre-denominator closure / 0 withdrawn；{retained} 项均有 V3 score、Evidence Review、Stable Node owner 与 Books comparison。"
        "既有 77 项 root 写回均为 Applied；新增 6 项只进入 root serial queue。"
    ) + text[p1e:]
    text = text.replace("151 retained、496 closure、0 withdrawn、191 isolated", f"{retained} retained、{closures} closure、0 withdrawn、191 isolated")

    # Patch prior six candidate-table states and append the six new rows.
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("|"):
            for aid in PRIOR_APPLIED:
                if f"/{aid}v1" in line:
                    cells = line.split("|")
                    cells[-2] = cells[-2].replace("整合：待 root", "整合：已写入并通过独立写后复核")
                    lines[i] = "|".join(cells)
    section4 = next(i for i, line in enumerate(lines) if line == "## 4. 证据与知识整合")
    table_insert = section4 - 1
    table_rows = []
    for aid, meta in N.items():
        row = row_for(ledger, aid); a,b,c = meta["score"]
        table_rows.append(f"| [{row['title']}](https://arxiv.org/html/{aid}v1) | 2026-05-13T08:00:00+08:00 | {meta['admission']}；{a} + {b} + {c} = {a+b+c} | 深入完成 | 整合：待 root，`{meta['node']}` → [{meta['anchor']}](../../../../{meta['path']}) |")
    lines[table_insert:table_insert] = table_rows
    text = "\n".join(lines) + "\n"

    # Append full reviews/comparisons just before the report's closure section.
    blocks = []
    for aid, meta in N.items():
        row = row_for(ledger, aid)
        blocks += [f"### [{row['title']}](https://arxiv.org/html/{aid}v1)", "", f"**准入：** {meta['admission']}", "", review_markdown(row, meta), "", f"**Books 对读：** `{meta['node']}` → `{meta['path']}` 的“{meta['anchor']}”。{meta['current']} 新证据增量：{meta['delta']} 判定：**Integrate — Root write required**。", ""]
    marker = "## 5. 缺口与下一步"
    text = text.replace(marker, "\n".join(blocks) + "\n" + marker, 1)
    tail_start = text.index("## 5. 缺口与下一步")
    tail_end = text.index("## 6. 复核", tail_start)
    tail = "\n".join([
        "## 5. 缺口与下一步", "",
        f"- 分母已冻结为 {retained} retained + {closures} closure + 191 isolation = 838；不存在未审查的 retained candidate。",
        f"- {retained} 项均完成相应深度 Evidence Review、Stable Node owner 与逐命题 Books comparison。",
        "- Round 6 的 6 项写回连同此前 71 项均已核对为 Applied；当前 queue 的 77 项全部没有 pending root 状态。",
        "- Round 7 新增 6 项等待 root 串行写回；精确 synthesis、证据边界和 fallback 见 v3-root-writeback-queue.json 与 V3_ROUND7_ROOT_BOOKS_SYNTHESIS_QUEUE_20260915.md。",
        "- 无材料 blocker，不需要用户补材料；不得扩窗、扩来源或重扫 838 个 identity。", "",
    ])
    text = text[:tail_start] + tail + text[tail_end:]
    review_start = text.index("## 6. 复核")
    active = text.index("### 活跃证据文件", review_start)
    review_head = "\n".join([
        "## 6. 复核", "", "结论：**未通过 — DAILY 仍为 Ongoing**", "",
        "Round 7 作者返修已完成但不能自签。Coverage、分母、六项 exact-v1 Evidence 与 Books Decision 已闭合；Books Gate 等待 root 串行写入六项后，由未参与本轮写作的 fresh non-author reviewer 检查 binding 唯一性、正文位置、语义完整性与 Review-notes 边界。", "",
        "复核者：待 root writeback 与新的 fresh non-author reviewer", "",
    ])
    text = text[:review_start] + review_head + text[active:]
    text = text.replace("- V3_BOUNDED_SIX_AUTHOR_REPAIR_20260915.md\n", "- V3_BOUNDED_SIX_AUTHOR_REPAIR_20260915.md\n- V3_ROUND7_BOUNDED_AUTHOR_REPAIR_20260915.md\n- V3_ROUND7_ROOT_BOOKS_SYNTHESIS_QUEUE_20260915.md\n")
    text = text.replace("**Review Provenance ID:** daily-20260513-v3-bounded-six-author-repair-20260915", "**Review Provenance ID:** daily-20260513-v3-round7-bounded-author-repair-20260915")
    REPORT.write_text(text)


if __name__ == "__main__":
    main()
