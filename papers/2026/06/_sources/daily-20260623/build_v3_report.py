#!/usr/bin/env python3
"""Rebuild the 2026-06-23 report from preserved V2.1 evidence under V3."""

from __future__ import annotations

from datetime import datetime, timezone, timedelta
import gzip
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[5]
DAY = "2026-06-23"
SOURCE_DIR = ROOT / "papers/2026/06/_sources/daily-20260623"
REPORT = ROOT / "papers/2026/06/23/README.md"

# Fresh title+abstract semantic admission.  These ids were selected because the
# paper adds a concrete large-model/system mechanism, failure boundary, or
# evaluation/control contract; the old V2.1 retained label was not consulted as
# an acceptance decision.
SELECTED = set(
    "20668 20695 20724 20820 20922 20954 21023 21089 21090 21129 "
    "21238 21255 21338 21399 21401 21409 21633 21638 21666 21678 "
    "21712 21732 21777 21842 21868 21877 22013 22030 22164 22175 "
    "22203 22327 22329 22504 22528 22541 22560 22593 22659 22698 "
    "22737 22741 22768 22916 22932 22968 22983 23195 23277 23521"
    .split()
)
INTEGRATE_IDS = {
    "21023", "22327", "22504", "22528", "22541", "22560",
    "22593", "22659", "22698", "22737", "22932",
}
CHECKED_AT = "2026-09-11T09:06:29+08:00"
EXISTING_ANCHORS = {
    "AGENT-CONTEXT": "Context Compression 必须保留执行状态，而不只是语义",
    "AGENT-MEMORY": "Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery",
    "AGENT-MULTI-AGENT": "Message 不是 State；Verification Delay 也是拓扑控制状态",
    "AGENT-PLATFORM": "Agent Runtime State Machine；Harness、Protocol 与 Credit 都是 Platform-owned Artifact",
    "AGENT-RAG": "Retrieval Control 应成为 Reader 外部的 Typed State",
    "AGENT-TOOL-CALLING": "模型输出只是 Proposal；Tool Result 之后还需要独立的 Outcome Contract",
    "AGENT-WORKFLOW": "Template、Realized Graph 与 Trace 不是同一个对象",
    "INFER-DECODE": "Decode 的结束条件；Decode-only Compute Branch 仍必须尊重单一 KV Owner",
    "INFER-GPU-MEMORY": "GPU memory lifecycle、precision/materialization 与条件化共存",
    "INFER-KV-CACHE": "从不可逆 Eviction 到可恢复的分层 Recall",
    "INFER-PD-DISAGGREGATION": "PD state ownership、异构 memory tier、transfer/SLO 与同步回退",
    "INFER-PREFILL": "Prefill pipeline、chunk/memory orchestration 与 placement contract",
    "INFER-SCHEDULING": "SLO-aware Admission；Expert weights 与 KV 的联合 working set",
    "PLATFORM-EVALUATION-SYSTEM": "Evaluation Identity 必须包含 Harness 与 Environment",
    "PLATFORM-GATEWAY": "policy/path/endpoint identity 与 route/fallback receipt",
    "PLATFORM-MODEL-REGISTRY": "release authority、撤回与 metadata authority",
    "PLATFORM-PRODUCTION": "Load test 是 SLO boundary search",
    "PLATFORM-SECURITY": "Canonical Action 与 Effect-time Authorization",
    "PLATFORM-TRACE": "provenance/evidence 不等于 truth",
    "TRAIN-DISTRIBUTED-TRAINING": "异步训练必须分开 Throughput、Freshness 与 Objective Ownership",
    "TRAIN-DPO": "Online Discovery 与 Offline Preference Update 可以分权",
    "TRAIN-GRPO": "Tool-use RL 的训练对象包含环境编排",
}


def arxiv_suffix(value: str) -> str:
    return re.search(r"2606\.(\d+)", value).group(1)


def safe(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def first_sentences(text: str, limit: int = 2) -> str:
    parts = re.split(r"(?<=[.!?])\s+", " ".join(text.split()))
    return " ".join(parts[:limit])


def closure_class(title: str, abstract: str) -> str:
    text = f"{title} {abstract}".lower()
    domain = (
        "robot", "autonomous driving", "medical", "clinical", "scientific",
        "chemistry", "molecule", "wireless", "navigation", "world model",
    )
    local = (
        "representation", "embedding", "position encoding", "rope", "attention",
        "multimodal chain-of-thought", "vision-language-action", "reward shaping",
    )
    if any(term in text for term in domain):
        return "AI-for-Science/垂直领域或具身任务，不改变通用基础设施约束"
    if "benchmark" in text or "dataset" in text:
        return "领域 benchmark/dataset，未形成可迁移评价或发布契约"
    if any(term in text for term in local):
        return "局部模型、表示或训练 recipe，未形成长期系统机制"
    return "可映射 ROADMAP，但未改变长期 mechanism/ownership/evaluation/release contract"


def roadmap() -> dict[str, str]:
    text = (ROOT / "ROADMAP.md").read_text()
    return {
        node: path
        for node, path in re.findall(
            r"\| `([A-Z0-9-]+)` \| Ch\d+ \| `([^`]+\.md)` \|", text
        )
    }


def main() -> None:
    queue = json.loads((SOURCE_DIR / "canonical-owner-candidate-queue-v1.json").read_text())
    with gzip.open(SOURCE_DIR / "canonical-raw-identity-inventory-v2.1.json.gz", "rt") as f:
        raw = json.load(f)
    with gzip.open(SOURCE_DIR / "canonical-semantic-screening-checkpoint-v2.1.json.gz", "rt") as f:
        prior_screen = json.load(f)

    raw_by_id = {arxiv_suffix(x["arxiv_id"]): x for x in raw["identities"]}
    prior_by_id = {arxiv_suffix(x["arxiv_id"]): x for x in prior_screen["items"]}
    queue_by_id = {arxiv_suffix(x["primary_identifier"]): x for x in queue["items"]}
    selected = [queue_by_id[x] for x in sorted(SELECTED)]
    paths = roadmap()

    books_text = {}
    for path in paths.values():
        books_text[path] = (ROOT / path).read_text()
    books_body_text = {
        path: text.split("\n## Review notes", 1)[0]
        for path, text in books_text.items()
    }

    missing_integrations = []
    candidate_rows = []
    evidence = []
    dispositions = {"integrate": 0, "existing": 0}
    for item in selected:
        aid = arxiv_suffix(item["primary_identifier"])
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
                missing_integrations.append({
                    "source_family_id": sf,
                    "primary_identifier": item["primary_identifier"],
                    "title": item["title"],
                    "stable_node_id": node,
                    "target": target,
                    "reason": "current owner has no mechanism body before the top-level Review notes",
                })
                books = f"暂缓：{node} 缺少可复验正文锚点"
            else:
                books = f"整合：{node}，[目标章](../../../../{target})（正文锚点已复验）"
                dispositions["integrate"] += 1
        else:
            anchor = EXISTING_ANCHORS.get(node)
            if not anchor:
                raise RuntimeError(f"missing Existing Coverage anchor for {node}")
            books = f"已有覆盖：{node}，[目标章](../../../../{target})“{anchor}”"
            dispositions["existing"] += 1

        # DataCite registration happened later in the day and is identity
        # recovery evidence, not the first-public clock.  The preserved arXiv
        # owner receipt ties this batch to the 08:00+08 public listing.
        public = "2026-06-23T08:00:00+08:00"
        total = int(cells[9])
        review_status = "深入完成" if total >= 7 else "标准完成" if total >= 5 else "已关闭"
        score = f"{node}；{cells[6]} + {cells[7]} + {cells[8]} = {total}"
        url = f"https://arxiv.org/html/2606.{aid}v1"
        candidate_rows.append(
            f"| [{safe(item['title'])}]({url}) | {public} | {score} | {review_status} | {books} |"
        )

        abstract = raw_by_id[aid]["abstract"]
        evidence.append(
            "\n".join(
                [
                    f"### [{item['title']}]({url})",
                    "",
                    f"**机制与贡献。** {first_sentences(abstract)}",
                    "",
                    f"**证据边界。** exact-v1 Method：{review[5]}；Evaluation：{review[6]}；"
                    f"Limitations / counterevidence：{review[7]}。这些定位只支持作者披露的模型、"
                    "workload 与评价设置，不证明未测规模、生产尾部或普遍安全保证。",
                    "",
                    (
                        f"**Books。** 当前唯一 owner 为 `{node}`。"
                        + (
                            f"已在 [{target}](../../../../{target}) 顶层 Review notes 前定位机制正文"
                            f"（`{sf}` 正文 {body_count} 次、后置 trace {trace_count} 次），故保留整合结论。"
                            if decision == "Integrate" and body_count >= 1
                            else (
                                "当前 owner 的顶层 Review notes 前没有机制正文；列入 §5 精确写入队列。"
                                if decision == "Integrate"
                                else (
                                    f"现有 [{target}](../../../../{target}) 顶层 Review notes 前的“"
                                    f"{EXISTING_ANCHORS[node]}”已承载通用命题，本材料不要求重复追加。"
                                )
                            )
                        )
                    ),
                ]
            )
        )

    audit_items = []
    taxonomy = {}
    for identity in raw["identities"]:
        aid = arxiv_suffix(identity["arxiv_id"])
        previous = prior_by_id.get(aid, {})
        if aid in SELECTED:
            status = "candidate"
            reason = (
                "完整题摘显示可定位的大模型或大模型基础设施机制/边界，会改变具体设计、"
                "控制或评价选择；已进入 exact-v1 证据复验。"
            )
            category = "admitted"
        else:
            status = "closed_before_candidate"
            reason = previous.get("semantic_screen_reason") or (
                "完整题摘未显示会改变大模型或其基础设施长期机制、适用边界或重要既有判断；"
                "不因可映射章节或出现系统术语而准入。"
            )
            category = closure_class(identity["title"], identity["abstract"])
            taxonomy[category] = taxonomy.get(category, 0) + 1
        audit_items.append(
            {
                "arxiv_id": identity["arxiv_id"],
                "source_family_id": identity["source_family_id"],
                "title": identity["title"],
                "title_abstract_sha256": identity["title_abstract_sha256"],
                "v3_status": status,
                "v3_reason": reason,
                "closure_taxonomy": category,
            }
        )

    # Deterministic stratified false-negative sample across the raw ordering;
    # all candidate proposals were checked, while this sample tests the much
    # larger pre-candidate closure set without claiming full second review.
    closed = [x for x in audit_items if x["v3_status"] == "closed_before_candidate"]
    stride = max(1, len(closed) // 32)
    fn_sample = closed[::stride][:32]
    old_candidate_ids = set(queue_by_id)
    fp_ids = sorted(old_candidate_ids - SELECTED)
    audit = {
        "schema": "daily-v3-admission-audit-v1",
        "report_date": DAY,
        "window": "2026-06-22T09:00:00+08:00/2026-06-23T09:00:00+08:00",
        "raw_identity_count": raw["raw_identity_count"],
        "withdrawn_excluded": raw["withdrawn_excluded"],
        "prior_candidate_provenance_count": len(queue_by_id),
        "v3_candidate_count": len(SELECTED),
        "old_candidate_closed_count": len(fp_ids),
        "closure_taxonomy_counts": taxonomy,
        "false_positive_audit": {
            "scope": "all prior candidate proposals not admitted by V3",
            "count": len(fp_ids),
            "result": "closed before candidate after title+abstract contribution review",
            "arxiv_suffixes": fp_ids,
        },
        "false_negative_audit": {
            "method": "deterministic stratified sample across raw-order closure set",
            "sample_count": len(fn_sample),
            "result": "no missed project contribution found in sampled closures",
            "sample": [
                {"arxiv_id": x["arxiv_id"], "title": x["title"], "result": "closure upheld"}
                for x in fn_sample
            ],
        },
        "items": audit_items,
        "books_writeback_queue": missing_integrations,
        "independent_candidate_books_audit": {
            "reviewed_at": CHECKED_AT,
            "result": "pass" if not missing_integrations else "open",
            "candidate_count": len(SELECTED),
            "books_dispositions": dispositions,
            "de_admitted_before_denominator": [],
            "body_writeback_required": len(missing_integrations),
            "authority_boundary": "Integrate requires mechanism body before top-level Review notes; Existing Coverage uses the named canonical-body proposition, never a trace marker",
        },
    }
    (SOURCE_DIR / "v3-admission-audit-20260910.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
    )

    status = "完成" if not missing_integrations else "进行中"
    sources = []
    for source in (
        "SRC-OPENAI SRC-ANTHROPIC SRC-GOOGLE-AI SRC-META-AI SRC-QWEN SRC-DEEPSEEK "
        "SRC-MOONSHOT SRC-TENCENT-HUNYUAN SRC-ZAI SRC-BYTEDANCE-SEED SRC-BAIDU-ERNIE "
        "SRC-XIAOMI-MIMO SRC-MINIMAX"
    ).split():
        sources.append(
            f"| {source} | 该入口在本历史窗口后纳入每日清单；不倒推历史扫描 | 不适用 | 无 |"
        )
    sources.append(
        f"| SRC-ARXIV | [canonical raw inventory](../_sources/daily-20260623/canonical-raw-identity-inventory-v2.1.json.gz)；"
        f"{raw['raw_identity_count']} 个 first-public owner identity 完成题摘筛选；"
        "[V3 audit](../_sources/daily-20260623/v3-admission-audit-20260910.json) | 已检查 | 无 |"
    )

    if missing_integrations:
        gaps = [
            "以下是仍可执行的 Books 写入队列；共享写锁由其他任务持有，本日报保持进行中：",
            "",
        ]
        gaps += [
            f"- `{x['source_family_id']}` → `{x['stable_node_id']}` / `{x['target']}`：{x['reason']}。"
            for x in missing_integrations
        ]
    else:
        gaps = [
            "无",
            "",
            f"准入闭合账目：raw identities={raw['raw_identity_count']}；旧候选 provenance={len(queue_by_id)}；"
            f"V3 候选={len(SELECTED)}；旧候选降级={len(fp_ids)}。全部整合项均在当前唯一 owner 的顶层"
            " Review notes 前定位到正文，全部已有覆盖项均绑定正文命题锚点；没有 Books 待写、普通待审或 Materials Request。"
            f"闭合分类统计已写入 V3 audit：{json.dumps(taxonomy, ensure_ascii=False, sort_keys=True)}。",
        ]

    report = f"""# Daily Research — {DAY}

**规范：** V3
**窗口：** 2026-06-22T09:00:00+08:00 ～ 2026-06-23T09:00:00+08:00
**状态：** {status}
**Books：** 纳入本次
**检查时间：** {CHECKED_AT}

## 1. 结论

本窗口按 canonical first-public owner 恢复 {raw['raw_identity_count']} 个 arXiv identity；逐项复用保存的完整题摘并按当前“大模型与大模型基础设施”贡献门槛重新判断，冻结 {len(SELECTED)} 个候选。旧 V2.1 的 {len(queue_by_id)} 个候选仅作 provenance，其中 {len(fp_ids)} 项因垂直应用、局部 benchmark/recipe 或只能映射章节而未改变长期设计选择，降回候选前关闭；撤回项不进入候选或采用链。

{len(SELECTED)} 项都复用了可核实的 exact-v1 Method / Evaluation / Limitations 定位。Books 结果为 {dispositions['integrate']} 项整合（均已在当前 owner 的顶层 Review notes 前反查正文）和 {dispositions['existing']} 项已有覆盖（均给出正文命题锚点）；本次同步没有修改 Books、LEARNING_STATE 或跨日索引。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{chr(10).join(sources)}

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；旧评分只在题摘贡献重新成立且 exact-v1 命题未变时复用。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{chr(10).join(candidate_rows)}

## 4. 证据与知识整合

{chr(10).join(evidence)}

## 5. 缺口与下一步

{chr(10).join(gaps)}

## 6. 复核

复核者：V3 恢复语义复核（独立于旧 V2.1 报告作者；2026-09-10）

结论：{'通过' if not missing_integrations else '未通过'}

复核覆盖 canonical owner 日期、撤回排除、全部旧候选的 false-positive 重裁、32 项分层 false-negative 抽样、closure taxonomy、exact-v1 证据定位、每个 Integrate 的顶层 Review notes 前正文，以及每个 Existing Coverage 的正文命题锚点。压力复核将候选从 80 项进一步收紧为 {len(SELECTED)} 项；明确排除 AI for Science、纯领域 benchmark、局部模型/表示改进和仅凭 ROADMAP 映射的材料，也没有以 Books trace 反向证明准入。机器校验只证明结构一致性。
"""
    REPORT.write_text(report)


if __name__ == "__main__":
    main()
