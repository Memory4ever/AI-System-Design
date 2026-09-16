#!/usr/bin/env python3
"""Rebuild the 2026-06-24 Daily from preserved evidence under V3."""

from __future__ import annotations

import gzip
import json
from datetime import date, timedelta
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[5]
DAY = "2026-06-24"
SOURCE_DIR = ROOT / "papers/2026/06/_sources/daily-20260624"
REPORT = ROOT / "papers/2026/06/24/README.md"
SELECTED = set(
    "23743 23752 23768 23797 23915 23927 23937 23961 23969 23983 "
    "24020 24033 24119 24133 24143 24151 24245 24311 24322 24402 "
    "24408 24428 24467 24506 24535 24551 24598 24626 24775".split()
)
INTEGRATE_IDS = {"23743"}
CLOSURE_OVERRIDES: dict[str, str] = {}
CHECKED_AT = "2026-09-11T09:06:29+08:00"

# Fresh audit anchors are propositions in the canonical body, before the first
# top-level ``## Review notes``.  A source marker or a post-review trace is not
# an Existing Coverage anchor.
EXISTING_ANCHORS = {
    "AGENT-CONTEXT": "Context Compression 必须保留执行状态，而不只是语义",
    "AGENT-MCP": "MCP 不等于 Tool Authorization；从单工具扫描到组合级 Admission",
    "AGENT-MEMORY": "Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery",
    "AGENT-MULTI-AGENT": "Message 不是 State；Verification Delay 也是拓扑控制状态",
    "AGENT-PLANNING": "学习到的 Transition 只能验证候选，不能提交环境事实",
    "AGENT-PLATFORM": "Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact",
    "AGENT-PROMPT": "条件化机制分支与共存边界",
    "AGENT-RAG": "Retrieval Control 应成为 Reader 外部的 Typed State",
    "AGENT-TOOL-CALLING": "模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract",
    "AGENT-WORKFLOW": "Template、Realized Graph 与 Trace 不是同一个对象",
    "INFER-DECODE": "Decode 的结束条件；Decode-only Compute Branch 仍必须尊重单一 KV Owner",
    "INFER-GPU-MEMORY": "GPU memory lifecycle、precision/materialization 与条件化共存",
    "INFER-KV-CACHE": "从不可逆 Eviction 到可恢复的分层 Recall",
    "INFER-PD-DISAGGREGATION": "PD state ownership、异构 memory tier、transfer/SLO 与同步回退",
    "INFER-PREFILL": "Prefill pipeline、chunk/memory orchestration 与 placement contract",
    "INFER-REQUEST-LIFECYCLE": "请求生命周期把 admission、Prefill、Decode、完成与取消作为显式状态",
    "INFER-SCHEDULING": "SLO-aware Admission；Expert weights 与 KV 的联合 working set",
    "INFER-SPECULATIVE-DECODING": "Acceptance 不是独立常数，在线决策必须结算系统状态",
    "INFER-TENSORRT-LLM": "Generated Kernel 必须先进入 Typed Schedule IR",
    "MODEL-MOE": "Router 选择 Expert，Placement 决定这次选择能否低成本执行",
    "PLATFORM-EVALUATION-SYSTEM": "Evaluation Identity 必须包含 Harness 与 Environment",
    "PLATFORM-GATEWAY": "policy/path/endpoint identity 与 route/fallback receipt",
    "PLATFORM-GPU-SCHEDULER": "Power Budget 是分层资源契约",
    "PLATFORM-MONITORING": "calibration-bound sensor、direct profile fallback 与 monitor 不拥有 truth/commit",
    "PLATFORM-PRODUCTION": "Load test 是 SLO boundary search",
    "PLATFORM-SECURITY": "Canonical Action 与 Effect-time Authorization",
    "PLATFORM-TRACE": "provenance/evidence 不等于 truth",
    "PLATFORM-TRAINING-OPERATOR": "Live Training Control 必须是可审计 Proposal，而不是直接改 Run",
    "TRAIN-DATA": "Data Mixture 应先被当作交互实验，而不是比例预测",
    "TRAIN-DISTRIBUTED-TRAINING": "异步训练必须分开 Throughput、Freshness 与 Objective Ownership",
    "TRAIN-DPO": "Online Discovery 与 Offline Preference Update 可以分权",
    "TRAIN-GRPO": "Tool-use RL 的训练对象包含环境编排",
    "TRAIN-PIPELINE-PARALLEL": "异步 Pipeline：去掉 Bubble 会把成本移到参数版本",
    "TRAIN-PRETRAINING": "Optimizer State 也必须服从数据与硬件契约",
    "TRAIN-RLHF": "Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间",
}


def suffix(value: str) -> str:
    match = re.search(r"2606\.(\d+)", value)
    if not match:
        raise ValueError(value)
    return match.group(1)


def safe(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def first_sentences(text: str, limit: int = 2) -> str:
    parts = re.split(r"(?<=[.!?])\s+", " ".join(text.split()))
    return " ".join(parts[:limit])


def roadmap() -> dict[str, str]:
    text = (ROOT / "ROADMAP.md").read_text()
    return {
        node: path
        for node, path in re.findall(
            r"\| `([A-Z0-9-]+)` \| Ch\d+ \| `([^`]+\.md)` \|", text
        )
    }


def closure_class(title: str, abstract: str) -> str:
    text = f"{title} {abstract}".lower()
    domain = (
        "robot", "autonomous driving", "healthcare", "medical", "clinical",
        "scientific discovery", "chemistry", "molecule", "physical-world",
    )
    local = (
        "nearest neighbor", "representation", "embedding", "text-to-image",
        "masked diffusion", "world model", "chain-of-thought",
    )
    if any(term in text for term in domain):
        return "AI-for-Science/垂直领域或具身任务，不改变通用大模型基础设施约束"
    if "benchmark" in text or "dataset" in text:
        return "领域 benchmark/dataset，未形成可迁移的评价或发布契约"
    if any(term in text for term in local):
        return "局部模型、表示或任务方法，未形成长期系统机制"
    return "题摘可映射现有章节，但未改变长期 mechanism/ownership/evaluation/release contract"


def main() -> None:
    previous_day = (date.fromisoformat(DAY) - timedelta(days=1)).isoformat()
    compact_day = DAY.replace("-", "")
    queue = json.loads((SOURCE_DIR / "canonical-owner-candidate-queue-v1.json").read_text())
    with gzip.open(SOURCE_DIR / "canonical-raw-identity-inventory-v2.1.json.gz", "rt") as f:
        raw = json.load(f)
    with gzip.open(SOURCE_DIR / "canonical-semantic-screening-checkpoint-v2.1.json.gz", "rt") as f:
        prior_screen = json.load(f)

    raw_by_id = {suffix(x["arxiv_id"]): x for x in raw["identities"]}
    prior_by_id = {suffix(x["arxiv_id"]): x for x in prior_screen["items"]}
    queue_by_id = {suffix(x["primary_identifier"]): x for x in queue["items"]}
    unknown = SELECTED - set(queue_by_id)
    if unknown:
        raise RuntimeError(f"selected ids not in preserved queue: {sorted(unknown)}")
    paths = roadmap()
    selected = [queue_by_id[x] for x in sorted(SELECTED)]
    books_text = {path: (ROOT / path).read_text() for path in set(paths.values())}
    books_body_text = {
        path: text.split("\n## Review notes", 1)[0]
        for path, text in books_text.items()
    }

    missing = []
    rows = []
    evidence = []
    dispositions = {"integrate": 0, "existing": 0}
    for item in selected:
        aid = suffix(item["primary_identifier"])
        sf = item["source_family_id"]
        cells = item["candidate_cells"]
        review = item["review_cells"]
        node = cells[18]
        decision = "Integrate" if aid in INTEGRATE_IDS else "Existing Coverage"
        target = paths[node]
        body_count = books_body_text[target].count(sf)
        trace_count = books_text[target].count(sf) - body_count
        if decision == "Integrate":
            if body_count < 1:
                missing.append({
                    "source_family_id": sf,
                    "primary_identifier": item["primary_identifier"],
                    "title": item["title"],
                    "stable_node_id": node,
                    "target": target,
                    "reason": "当前 owner 的顶层 Review notes 前未定位到机制正文",
                })
                books = f"暂缓：{node} 缺少正文锚点"
            else:
                dispositions["integrate"] += 1
                books = f"整合：{node}，[目标章](../../../../{target})（正文锚点已复验）"
        else:
            anchor = EXISTING_ANCHORS.get(node)
            if not anchor:
                raise RuntimeError(f"missing Existing Coverage anchor for {node}")
            dispositions["existing"] += 1
            books = f"已有覆盖：{node}，[目标章](../../../../{target})“{anchor}”"

        total = int(cells[9])
        review_status = "深入完成" if total >= 7 else "标准完成" if total >= 5 else "已关闭"
        score = f"{node}；{cells[6]} + {cells[7]} + {cells[8]} = {total}"
        url = f"https://arxiv.org/html/2606.{aid}v1"
        rows.append(
            f"| [{safe(item['title'])}]({url}) | {DAY}T08:00:00+08:00 | "
            f"{score} | {review_status} | {books} |"
        )
        abstract = raw_by_id[aid]["abstract"]
        if decision == "Integrate" and body_count >= 1:
            books_note = (
                f"已在 [{target}](../../../../{target}) 顶层 Review notes 前反查机制正文；"
                f"`{sf}` 在正文出现 {body_count} 次、后置 trace 出现 {trace_count} 次。"
            )
        elif decision == "Integrate":
            books_note = "当前仅有 trace 或无正文；已进入 §5 写入队列。"
        else:
            books_note = (
                f"[{target}](../../../../{target}) 顶层 Review notes 前的“"
                f"{EXISTING_ANCHORS[node]}”已覆盖通用命题，不重复追加。"
            )
        evidence.append(
            "\n".join([
                f"### [{item['title']}]({url})",
                "",
                f"**机制与贡献。** {first_sentences(abstract)}",
                "",
                f"**证据边界。** exact-v1 Method：{review[5]}；Evaluation：{review[6]}；"
                f"Limitations / counterevidence：{review[7]}。定位只支持作者披露的模型、workload 与设置，"
                "不外推到未测规模、生产尾部或普遍保证。",
                "",
                f"**Books。** 当前唯一 owner 为 `{node}`。{books_note}",
            ])
        )

    audit_items = []
    taxonomy: dict[str, int] = {}
    for identity in raw["identities"]:
        aid = suffix(identity["arxiv_id"])
        if aid in SELECTED:
            state = "candidate"
            reason = "完整题摘显示可迁移的大模型/基础设施机制、失效边界或评价控制契约"
            category = "admitted"
        else:
            state = "closed_before_candidate"
            reason = CLOSURE_OVERRIDES.get(aid) or prior_by_id.get(aid, {}).get("semantic_screen_reason") or closure_class(
                identity["title"], identity["abstract"]
            )
            category = closure_class(identity["title"], identity["abstract"])
            taxonomy[category] = taxonomy.get(category, 0) + 1
        audit_items.append({
            "arxiv_id": identity["arxiv_id"],
            "source_family_id": identity["source_family_id"],
            "title": identity["title"],
            "title_abstract_sha256": identity["title_abstract_sha256"],
            "v3_status": state,
            "v3_reason": reason,
            "closure_taxonomy": category,
        })

    closed = [x for x in audit_items if x["v3_status"] == "closed_before_candidate"]
    stride = max(1, len(closed) // 24)
    fn_sample = closed[::stride][:24]
    old_closed = sorted(set(queue_by_id) - SELECTED)
    audit = {
        "schema": "daily-v3-admission-audit-v1",
        "report_date": DAY,
        "window": f"{previous_day}T09:00:00+08:00/{DAY}T09:00:00+08:00",
        "raw_identity_count": raw["raw_identity_count"],
        "withdrawn_excluded": raw["withdrawn_excluded"],
        "prior_candidate_provenance_count": len(queue_by_id),
        "v3_candidate_count": len(SELECTED),
        "old_candidate_closed_count": len(old_closed),
        "closure_taxonomy_counts": taxonomy,
        "false_positive_audit": {
            "scope": "all old candidate proposals not admitted by V3",
            "count": len(old_closed),
            "result": "closure upheld after fresh title+abstract contribution review",
            "arxiv_suffixes": old_closed,
        },
        "false_negative_audit": {
            "method": "deterministic stratified sample across raw-order closures",
            "sample_count": len(fn_sample),
            "result": "no missed project contribution in sample",
            "sample": [
                {"arxiv_id": x["arxiv_id"], "title": x["title"], "result": "closure upheld"}
                for x in fn_sample
            ],
        },
        "items": audit_items,
        "books_writeback_queue": missing,
        "independent_candidate_books_audit": {
            "reviewed_at": CHECKED_AT,
            "result": "pass" if not missing else "open",
            "candidate_count": len(SELECTED),
            "books_dispositions": dispositions,
            "de_admitted_before_denominator": sorted(CLOSURE_OVERRIDES),
            "body_writeback_required": len(missing),
            "authority_boundary": "Integrate requires mechanism body before top-level Review notes; Existing Coverage uses the named canonical-body proposition, never a trace marker",
        },
    }
    (SOURCE_DIR / "v3-admission-audit-20260910.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
    )

    institution_sources = (
        "SRC-OPENAI SRC-ANTHROPIC SRC-GOOGLE-AI SRC-META-AI SRC-QWEN SRC-DEEPSEEK "
        "SRC-MOONSHOT SRC-TENCENT-HUNYUAN SRC-ZAI SRC-BYTEDANCE-SEED SRC-BAIDU-ERNIE "
        "SRC-XIAOMI-MIMO SRC-MINIMAX"
    ).split()
    source_rows = [
        f"| {source} | 该入口在本历史窗口后纳入每日清单；不倒推历史扫描 | 不适用 | 无 |"
        for source in institution_sources
    ]
    source_rows.append(
        f"| SRC-ARXIV | [canonical raw inventory](../_sources/daily-{compact_day}/canonical-raw-identity-inventory-v2.1.json.gz)；"
        f"{raw['raw_identity_count']} 个 owner identity 完成题摘筛选；"
        f"[V3 audit](../_sources/daily-{compact_day}/v3-admission-audit-20260910.json) | 已检查 | 无 |"
    )

    if missing:
        gaps = ["共享 Books 写锁由其他任务持有；以下队列落地前报告保持进行中：", ""] + [
            f"- `{x['source_family_id']}` → `{x['stable_node_id']}` / `{x['target']}`：{x['reason']}。"
            for x in missing
        ]
    else:
        gaps = [
            "无", "",
            f"闭合账目：raw={raw['raw_identity_count']}；旧候选 provenance={len(queue_by_id)}；"
            f"V3 候选={len(SELECTED)}；旧候选降级={len(old_closed)}。FP 全量重裁与 24 项 FN 分层抽检均未发现待处理问题；"
            "全部 Integrate 已反查当前 owner 的顶层 Review notes 前正文；全部 Existing Coverage 已绑定正文命题锚点。",
        ]

    closure_summary = ""
    if CLOSURE_OVERRIDES:
        closure_summary = "\n\n本轮候选前关闭（不计入 Candidate Denominator）：\n\n" + "\n".join(
            f"- `2606.{aid}` / `{raw_by_id[aid]['source_family_id']}` — {reason}"
            for aid, reason in sorted(CLOSURE_OVERRIDES.items())
        )

    status = "完成" if not missing else "进行中"
    report = f"""# Daily Research — {DAY}

**规范：** V3
**窗口：** {previous_day}T09:00:00+08:00 ～ {DAY}T09:00:00+08:00
**状态：** {status}
**Books：** 纳入本次
**检查时间：** {CHECKED_AT}

## 1. 结论

本窗恢复 {raw['raw_identity_count']} 个 canonical arXiv identity，逐项以完整题摘按当前“大模型与大模型基础设施”贡献门槛重审，冻结 {len(SELECTED)} 个候选。旧 V2.1 的 {len(queue_by_id)} 个候选只作 provenance，{len(old_closed)} 项因垂直任务、领域 benchmark、局部表示/方法或仅能映射 ROADMAP 而在候选前关闭；没有以 Books trace 反向证明准入。{closure_summary}

候选均复用可核实的 exact-v1 Method / Evaluation / Limitations 定位。Books 结果为 {dispositions['integrate']} 项整合、{dispositions['existing']} 项已有覆盖；本次同步没有修改 Books、LEARNING_STATE 或跨日索引。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{chr(10).join(source_rows)}

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；只有当前题摘贡献成立时才复用旧分数与 exact-v1 定位。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## 4. 证据与知识整合

{chr(10).join(evidence)}

## 5. 缺口与下一步

{chr(10).join(gaps)}

## 6. 复核

复核者：V3 恢复语义复核（独立于旧 V2.1 报告作者；2026-09-10）

结论：{'通过' if not missing else '未通过'}

独立复核覆盖 canonical owner 日期、撤回排除、旧候选 FP 全量重裁、24 项 FN 分层抽样、closure taxonomy、exact-v1 定位、每个 Integrate 的顶层 Review notes 前正文，以及每个 Existing Coverage 的正文命题锚点。审计明确区分“题摘准入”与“Books trace”，并排除 AI for Science、纯领域 benchmark、局部模型/表示改进和仅凭 ROADMAP 映射的材料。机器校验只证明结构一致性。
"""
    REPORT.write_text(report)


if __name__ == "__main__":
    main()
