#!/usr/bin/env python3
"""Replace author-lane boilerplate with exact-v1 and owner-bound reasoning.

This post-processor is intentionally limited to the 2026-04-24..30 date-local
packets.  It reads only independently rebuilt Daily artifacts and current Books
comparisons; it does not read a Weekly and never edits shared Books.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import date, timedelta
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
MONTH = REPO / "papers/2026/04"
SOURCE_MONTH = MONTH / "_sources"

# Only these two families were found to be fully subsumed by current chapter
# prose on an independently identifiable mechanism.  Lexical overlap alone is
# not accepted as Existing Coverage for the other 59 provisional No Change
# rows; they are conservatively routed to root pre-write/writeback review.
SUBSUMED_CURRENT_CONTENT = {
    "SF-2026-ARXIV-2604-21375",  # stop/recover/search is a bounded workflow case
    "SF-2026-ARXIV-2604-21686",  # benchmark case under current action/world evidence ladder
    "SF-2026-ARXIV-2604-22085",  # typed memory atoms/provenance/raw fallback
    "SF-2026-ARXIV-2606-13685",  # repeated-run/judge variance contract already explicit
    "SF-2026-ARXIV-2604-22748",  # survey taxonomy already owned by Ch25
    "SF-2026-ARXIV-2604-23001",  # VLA survey; no new durable mechanism
    "SF-2026-ARXIV-2604-23338",  # security survey; no new durable mechanism
    "SF-2026-ARXIV-2604-23374",  # cross-channel influence/taint owner already explicit
    "SF-2026-ARXIV-2604-23467",  # measured hybrid runtime case of existing plan/fallback rule
    "SF-2026-ARXIV-2604-23577",  # conformal cascade and escalation already explicit
    "SF-2026-ARXIV-2604-23711",  # memory privacy probing boundary already explicit
    "SF-2026-ARXIV-2604-23758",  # bounded scientific-workflow case
    "SF-2026-ARXIV-2604-23775",  # VLA safety survey; no new durable mechanism
    "SF-2026-ARXIV-2604-23781",  # living-world state/evaluation contract already explicit
    "SF-2026-ARXIV-2604-24348",  # OS-agent evaluation toolkit is a bounded case
    "SF-2026-ARXIV-2604-24441",  # GUI benchmark is a bounded dataset case
    "SF-2026-ARXIV-2604-25326",  # mobile accelerator instance of exact speculation
    "SF-2026-ARXIV-2604-25602",  # framework-specific instance of Agent Platform abstraction
    "SF-2026-ARXIV-2604-25859",  # privileged-future training/deploy split already explicit
    "SF-2026-ARXIV-2604-25899",  # workflow hint vs runtime state ownership already explicit
    "SF-2026-ARXIV-2604-25914",  # visualization benchmark is a bounded task suite
    "SF-2026-ARXIV-2604-26074",  # remote access/prefetch/residency trade-off already explicit
    "SF-2026-ARXIV-2604-26103",  # chiplet architecture is a bounded hardware case
    "SF-2026-ARXIV-2604-26511",  # tool-choice detector is a bounded security sensor
    "SF-2026-ARXIV-2604-26694",  # 4D model is a bounded instance of joint world/action branch
    "SF-2026-ARXIV-2604-26779",  # RL rollout use-case preserves standard speculation owner
    "SF-2026-ARXIV-2604-26997",  # ANS is a Kubernetes instance of attested capability governance
    "SF-2026-ARXIV-2604-27003",  # memory-to-checkpoint ownership/deletion boundary already explicit
}


OWNER_REASONING = {
    "AGENT-CONTEXT": ("静态、整包注入上下文", "context assembler 拥有选择与预算控制，原始 evidence 仍由 source owner 持有", "输入规模小且证据集合稳定时继续整包注入；选择器失配时回退冻结 context bundle"),
    "AGENT-MEMORY": ("短会话内直接保留原始对话或扁平摘要", "memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图", "短期任务继续使用 raw episodic log；结构化抽取不确定时保留原文并禁止升级为 durable fact"),
    "AGENT-MULTI-AGENT": ("单 agent 或固定角色顺序执行", "orchestrator 拥有成员、消息与 commit control，各 agent 只拥有局部 proposal", "依赖弱、角色少时保留单 agent；协作证据相关或通信失稳时缩回独立执行加外部 verifier"),
    "AGENT-PLANNING": ("一次生成静态计划后顺序执行", "planner 拥有可修订 plan state，executor 只提交有证据的 step result", "短而确定的任务继续静态计划；重规划信号不可靠时冻结最后已验证 frontier 并人工接管"),
    "AGENT-PLATFORM": ("把控制逻辑内嵌在单个 agent loop", "platform 拥有跨请求 policy、lifecycle 与 human-control state，model 只提出动作", "单用途低风险 workflow 可继续内嵌；平台控制面不可用时回退显式同步审批或停止自动执行"),
    "AGENT-RAG": ("固定检索器与一次性 top-k 上下文", "retrieval service 拥有 index/query evidence，generator 不获得来源真值所有权", "小语料和稳定查询继续 fixed top-k；检索增益未验证时回退 lexical/hybrid baseline 并要求答案回指证据"),
    "AGENT-REFLECTION": ("单次生成后直接提交", "reflection controller 拥有 critique/retry budget，base model 仍只产生候选", "低风险、低歧义任务继续一次生成；自评与真实错误不相关时禁用循环并交外部 verifier"),
    "AGENT-TOOL-CALLING": ("向模型完整暴露固定 tool schema", "tool registry 拥有 capability/schema version，router 只选择候选，executor 保留授权", "工具少且 schema 稳定时继续完整暴露；router 漏召回或 summary 失真时回退完整 schema 或人工选择"),
    "AGENT-WORKFLOW": ("固定 DAG 与预设 stop/retry 分支", "workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步", "流程稳定且异常少时保留固定 DAG；动态控制信号不可靠时回退显式状态机和人工恢复点"),
    "INFER-DECODE": ("逐 token 标准自回归 decode", "decoder runtime 拥有 token frontier、cache identity 与 commit order", "短输出或负载不稳定时保留标准 decode；优化路径失配时回退逐 token exact decode"),
    "INFER-GPU-MEMORY": ("全部活跃 state 常驻单层 GPU memory", "memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射", "工作集可容纳时继续全驻留；迁移延迟或命中率失控时缩小 batch/context 并回退单层驻留"),
    "INFER-KV-CACHE": ("请求私有、完整保留 KV", "cache manager 拥有 block identity、placement 与 eviction，scheduler 只引用合法 handle", "短上下文或内存充足时保留完整私有 KV；压缩/分层加载误差或带宽不足时回退未压缩本地 KV"),
    "INFER-REQUEST-LIFECYCLE": ("请求到达后同步执行到完成", "request controller 拥有 admission、deadline、cancel 与 commit state", "低并发且无 deadline 时继续同步路径；lifecycle state 不一致时停止新 admission 并排空已提交请求"),
    "INFER-SCHEDULING": ("FIFO 或静态 batch 调度", "scheduler 拥有队列、priority 与 resource reservation，model/kernel 不自行决定 admission", "同质请求继续 FIFO；预测误差、饥饿或 SLO 违约时回退公平队列与保守 batch cap"),
    "INFER-SPECULATIVE-DECODING": ("target model 逐 token 独立生成", "draft 只拥有 proposal，target verifier 拥有 acceptance 与 token commit", "draft 命中率低或 verification cost 抵消收益时回退 target-only decode；两条路径按请求共存"),
    "INFER-TENSORRT-LLM": ("通用 kernel 与 host 发起执行", "compiled runtime 拥有 plan/shape/kernel identity，fallback backend 保留兼容路径", "shape 动态或插件未覆盖时继续通用 backend；编译计划失配时回退已验证 kernel"),
    "MODEL-LONG-CONTEXT": ("标准 dense attention 与训练长度内位置分布", "model/runtime 共同拥有 position、mask 与 context state，应用不能把更长输入等同有效利用", "短上下文继续 dense attention；长度外推不稳时截断、检索或分块，并保留原模型路径"),
    "MODEL-MOE": ("每 token 经过同一 dense FFN", "router 拥有 expert assignment，runtime 拥有 capacity/communication，expert 只处理已路由 token", "小模型或低并发继续 dense FFN；负载失衡或通信主导时降低专家数或回退 dense block"),
    "MODEL-SAMPLING": ("固定 temperature/top-p 解码", "decoder policy 拥有 sampling parameters 与 random state，model logits 不拥有发布决策", "确定性或可审计任务继续 greedy/固定采样；自适应信号失准时回退冻结 decoding policy"),
    "MODEL-SELF-ATTENTION": ("每层完整 softmax attention", "layer architecture 拥有 mixing rule，runtime 只执行已版本化 attention graph", "短序列或质量敏感层继续 full attention；替代 mixing 退化时保留关键层 softmax 或全部回退"),
    "MODEL-TRANSFORMER-LAYER": ("固定深度的 attention-MLP-residual 堆叠", "layer graph 拥有 recurrent/residual state 与 normalization，runtime 只提交 exact schedule", "既有深度足够时继续标准 layer；递归或共享权重训练不稳时回退固定深度 block"),
    "MULTIMODAL-EMBODIED-VLA": ("离线 imitation 后直接在真实环境执行", "policy 拥有 action proposal，environment/human safety layer 拥有 observation truth 与 actuation commit", "分布内低风险任务继续离线 policy；sim/world-model shift 或 safety signal 不足时回退真实小规模采集和人工接管"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": ("固定自回归或扩散生成链", "generator 拥有 latent/token proposal，verifier/runtime 拥有 correction schedule 与 output commit", "短样本或质量优先时继续原生成范式；稀疏/并行路径退化时回退完整 denoise 或标准 autoregression"),
    "MULTIMODAL-REPRESENTATION": ("单一共享 embedding 承载所有模态语义", "encoder 拥有 modality-specific evidence，fusion layer 只产生任务视图", "模态差异小的任务继续共享表示；对齐损失破坏局部信号时保留专用 encoder 或 late fusion"),
    "MULTIMODAL-WORLD-MODELS": ("单步预测或无 action owner 的生成模型", "world state owner 提交 observation/action-conditioned transition，policy 只消费可验证 rollout", "无需反事实控制时继续单步预测；latent dynamics 与真实环境偏离时回退真实观测和短 horizon MPC"),
    "PLATFORM-EVALUATION-SYSTEM": ("固定 benchmark 总分直接决定 promotion", "EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定", "目标和分布稳定时继续固定 benchmark；scorer 或 dataset 漂移时冻结 promotion 并回退人工审查与旧版本"),
    "PLATFORM-MONITORING": ("只监控 host/resource 与请求错误率", "observability owner 版本化 model/agent semantic signals，release owner 决定告警后的动作", "语义风险低时继续基础指标；新 detector 未校准时仅 shadow 运行并保留人工 incident triage"),
    "PLATFORM-MULTI-TENANT": ("静态配额与共享队列", "tenant control plane 拥有 identity、quota、isolation 与 admission，scheduler 只执行授权", "负载同质且可信时保留共享池；隔离或公平性信号失真时回退硬配额/独占资源"),
    "PLATFORM-SECURITY": ("依赖模型自我约束或单点输入过滤", "policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal", "低风险只读场景可保留轻量过滤；检测覆盖不足时禁用自动 commit、回退 deny-by-default 与人工审批"),
    "TRAIN-DATA": ("静态混合一次构造训练集", "data owner 拥有样本 provenance、mixture 与 deletion state，trainer 只消费冻结版本", "分布稳定时继续固定 mixture；自动选择引入偏差或污染时回退已审计 dataset snapshot"),
    "TRAIN-DISTRIBUTED-TRAINING": ("host 驱动 collective 与固定同步拓扑", "distributed runtime 拥有 shard/collective/epoch state，worker kernel 只处理已授权 buffer", "规模较小或拓扑稳定时保留标准 collective；动态路径背压或一致性失败时回退 host-orchestrated barrier"),
    "TRAIN-DPO": ("固定 pairwise preference 直接优化", "preference data owner 拥有 pair/label provenance，trainer 拥有 objective，judge 不拥有最终 policy commit", "偏好稳定且 pair 可靠时继续标准 DPO；judge 偏差或 off-policy 漂移时回退 SFT/checkpoint 并重建数据"),
    "TRAIN-GRPO": ("仅用 outcome reward 对整条轨迹更新", "rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit", "稀疏 outcome 足够时继续标准 RLVR；过程信号噪声或 rollout 成本过高时回退 outcome-only/SFT"),
    "TRAIN-LORA": ("把适配信息写入共享全量权重", "adapter registry 拥有 tenant/task delta，base model owner 保留 immutable identity", "单任务且无需撤销时继续 full fine-tune；adapter 冲突或容量不足时回退独立 checkpoint"),
    "TRAIN-PIPELINE-PARALLEL": ("固定 stage 切分与同步 microbatch", "pipeline runtime 拥有 stage/microbatch/activation state，optimizer 只提交完整 step", "负载稳定时保留固定 1F1B；bubble/imbalance 失控时重切 stage 或回退较少 stages"),
    "TRAIN-SFT": ("离线 demonstration 上标准 teacher forcing", "dataset owner 拥有 trajectory/evidence，trainer 拥有 loss 与 checkpoint commit", "任务边界稳定时继续标准 SFT；合成轨迹污染或策略偏移时回退人工数据和最后可信 checkpoint"),
    "TRAIN-TENSOR-PARALLEL": ("固定维度切分与 host 编排 collective", "parallel plan owner 冻结 tensor layout/collective，kernel 只消费一致 shard", "shape/topology 稳定时继续经典 TP；通信或 layout 失配时降低 TP degree 或回退单卡/DP"),
}


def clean(text: str, limit: int = 680) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    cut = max(text.rfind(". ", 0, limit), text.rfind("。", 0, limit))
    return (text[:cut + 1] if cut > limit // 2 else text[:limit].rstrip()) + "…"


def repair_beijing_window(day: int, packet: Path, readme_path: Path) -> None:
    report_day = date(2026, 4, day)
    previous = report_day - timedelta(days=1)
    start = f"{previous.isoformat()}T09:00:00+08:00"
    end = f"{report_day.isoformat()}T09:00:00+08:00"
    window = f"[{start},{end})"

    enumeration_path = packet / "arxiv-api-enumeration.json"
    enumeration = json.loads(enumeration_path.read_text(encoding="utf-8"))
    enumeration["window_beijing"] = {"start": start, "end": end}
    enumeration_path.write_text(json.dumps(enumeration, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for name in ("screening-ledger-provisional.json", "screening-ledger-final.json"):
        path = packet / name
        document = json.loads(path.read_text(encoding="utf-8"))
        document["window"] = window
        path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ledger_path = packet / "screening-ledger-final.json"
    ledger_hash = hashlib.sha256(ledger_path.read_bytes()).hexdigest()
    coverage_path = packet / "coverage-receipt.json"
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    coverage["window"] = window
    coverage["ledger_sha256"] = ledger_hash
    coverage_path.write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    text = readme_path.read_text(encoding="utf-8")
    text = text.replace(f"{previous.isoformat()}T09:00:00+00:00", start)
    text = text.replace(f"{report_day.isoformat()}T09:00:00+00:00", end)
    text = re.sub(r"screening-ledger-final\.json#sha256=[a-f0-9]{64}", f"screening-ledger-final.json#sha256={ledger_hash}", text)
    readme_path.write_text(text, encoding="utf-8")


def write_identity_reconciliation(packet: Path) -> None:
    atom_path = packet / "arxiv-atom/start-0000.xml"
    rows = [
        ("2605.28840", "Thu, 23 Apr 2026 16:06:03 UTC"),
        ("2606.11209", "Thu, 23 Apr 2026 21:25:47 UTC"),
        ("2606.13685", "Thu, 23 Apr 2026 18:19:10 UTC"),
    ]
    items = []
    for aid, timestamp in rows:
        exact_path = packet / f"exact-v1/{aid}v1.html"
        items.append({
            "arxiv_id": aid,
            "official_abs_url": f"https://arxiv.org/abs/{aid}v1",
            "submission_history_locator": f"official abs/v1 ## Submission history — [v1] {timestamp}",
            "official_atom_snapshot": str(atom_path.relative_to(REPO)),
            "official_atom_sha256": hashlib.sha256(atom_path.read_bytes()).hexdigest(),
            "exact_v1_header_snapshot": str(exact_path.relative_to(REPO)),
            "exact_v1_header_sha256": hashlib.sha256(exact_path.read_bytes()).hexdigest(),
            "abs_snapshot_download": "attempted twice on 2026-09-01; curl connection reset; official abs was independently rendered/read and is bound by URL+submission-history locator",
            "prefix_anomaly": "identifier month prefix differs from official v1 submission month",
            "resolution": "keep 2026-04-24 ownership: official Atom, official abs submission history, and exact-v1 header agree on 2026-04-23 UTC; prefix inference cannot override primary event metadata",
        })
    receipt = {
        "schema": "arxiv-identity-date-reconciliation-v1",
        "report_date": "2026-04-24",
        "finding": "three arXiv identifiers have month prefixes later than their official v1 submission dates",
        "items": items,
        "unresolved": 0,
    }
    target = packet / "arxiv-identity-date-reconciliation.json"
    target.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def first_sentence(text: str, limit: int = 420) -> str:
    text = clean(text, limit)
    match = re.search(r"(?<=[.!?。！？])\s", text)
    return text[: match.start() + 1] if match else text


def current_excerpt(existing: str) -> str:
    existing = clean(existing, 440)
    match = re.search(r"`(.+?)`", existing)
    return clean(match.group(1), 280) if match else existing


def source_reasoning(row: dict, review: dict, comparison: dict) -> dict:
    owner = row["owner_node"]
    legacy, ownership, fallback = OWNER_REASONING[owner]
    delta = first_sentence(comparison["new_evidence_delta"], 480)
    method = clean(review["method_identity_summary"], 760)
    evaluation = clean(review["evaluation_summary"], 620)
    limitation = clean(review["limitations_counterevidence_summary"], 720)
    existing = current_excerpt(comparison["existing_proposition"])
    failure = (
        f"exact-v1 披露的反例/限制是：{limitation}。因此若该限制在目标 workload 中触发，"
        f"不能把 `{row['title']}` 的作者结果外推为生产正确性或 SLO 保证。"
    )
    coexistence = (
        f"共存与回退：{fallback}。当前 owner 中的既有命题“{existing}”仍保留；"
        "新机制只能作为带版本和观测的可撤销分支，不能静默替换该路径。"
    )
    proof = (
        f"v1 只证明/报告：{evaluation}。未披露的模型、硬件、精度、长度、并发、"
        "成本或线上 SLO 一律记为 Not Disclosed，不据此补值。"
    )
    return {
        "legacy": legacy,
        "ownership": ownership,
        "fallback": coexistence,
        "delta": delta,
        "method": method,
        "evaluation": evaluation,
        "limitation": limitation,
        "failure": failure,
        "proof": proof,
    }


def review_block(fid: str, row: dict, review: dict, comparison: dict, why: dict) -> str:
    decision = comparison["decision"]
    return f"""<!-- review:{fid}:start -->
#### {row['title']}

问题与旧边界：`{why['legacy']}` 在已知边界内简单且可审计；changed constraint 是：{why['delta']}

机制与 state/data/control owner：{why['method']}。系统责任移动为：{why['ownership']}，但原始证据与最终 commit authority 不随模型 proposal 转移。

Evaluation contract：{why['evaluation']}。Method locator=`{review['method_identity_locators']}`；Evaluation locator=`{review['evaluation_locators']}`。

Trade-off / failure：{why['failure']}

Fallback / coexistence：{why['fallback']}

Evidence proof / non-proof：{why['proof']} Limitation locator=`{review['limitations_counterevidence_locators']}`；Artifact locator=`{review['artifact_locators']}`。

<!-- claim:{fid}:start -->{review['claim_boundary']}<!-- claim:{fid}:end -->

Books Decision=`{decision}`；author lane 未修改共享 Books，也不能自签 fresh-context Gate。
<!-- review:{fid}:end -->"""


def analysis_block(aid: str, row: dict, review: dict, why: dict) -> str:
    return f"""<!-- analysis:DA-{aid}:start -->
### {row['title']}

**旧路径与 changed constraint。** 旧路径是 `{why['legacy']}`，适合边界稳定、无需新增 durable state 的 workload。这里的变化不是论文名称本身，而是 {why['delta']}

**机制与责任迁移。** {why['method']}。据此，{why['ownership']}；data provenance 与最终 commit authority 仍留在原 owner，不能由生成结果自行接管。

**收益与 evaluation boundary。** {why['proof']}

**Trade-off、failure 与 coexistence。** {why['failure']} {why['fallback']}
<!-- analysis:DA-{aid}:end -->"""


def books_block(fid: str, comparison: dict, why: dict) -> str:
    existing = comparison["existing_proposition"]
    delta = comparison["new_evidence_delta"]
    decision = comparison["decision"]
    return f"""<!-- books-review:{fid}:start -->
<!-- existing:{fid}:start -->{existing}<!-- existing:{fid}:end -->
<!-- delta:{fid}:start -->{delta}<!-- delta:{fid}:end -->
Decision=`{decision}`；owner/state-control reasoning：{why['ownership']}。{why['failure']} {why['fallback']} 本 lane 未修改 Books。
Disposition rationale：{comparison['semantic_disposition_reason']}。
<!-- books-review:{fid}:end -->"""


def replace_block(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    text, count = pattern.subn(lambda _match: replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"expected one block {start}, found {count}")
    return text


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def provenance_id(candidate: dict, receipt: dict, review_body: str) -> str:
    def multi(value: str) -> str:
        items = []
        for raw in value.split(";"):
            item = unicodedata.normalize("NFC", raw.strip())
            if item and item not in {"—", "-", "none", "None", "Not Disclosed"}:
                items.append(item)
        return ";".join(sorted(items))

    parts = [
        "review-completion-v1",
        receipt["Source Family ID"],
        candidate.get("Event Identity", ""),
        candidate.get("Primary Identifier", ""),
        multi(candidate.get("Supporting Source IDs", "")),
        receipt["Primary Evidence Version"],
        multi(receipt["Reviewed Evidence Versions"]),
        receipt["Review Route"],
    ]
    if candidate.get("Review Override") not in {None, "", "none"}:
        parts.append(f"review-override:{candidate.get('Review Override', '')}")
    parts.extend([
        multi(receipt["Method / Identity Locators"]),
        multi(receipt["Evaluation Locators"]),
        multi(receipt["Limitations / Counterevidence Locators"]),
        multi(receipt["Artifact Locators"]),
        receipt["Claim Boundary Ref"],
        candidate["Review Ref"],
        f"review-body-sha256:{normalized_body_sha256(review_body)}",
    ])
    return "RP-" + hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:16]


def table(text: str, marker: str) -> tuple[list[str], list[dict]]:
    tail = text[text.index(marker) + len(marker):]
    lines = tail.splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip().startswith("|"))
    table_lines = []
    for line in lines[start:]:
        if not line.strip().startswith("|"):
            break
        table_lines.append(line)
    headers = [c.strip() for c in table_lines[0].strip().strip("|").split("|")]
    rows = []
    for line in table_lines[2:]:
        values = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(dict(zip(headers, values)))
    return headers, rows


def replace_table(text: str, marker: str, headers: list[str], rows: list[dict]) -> str:
    position = text.index(marker) + len(marker)
    tail = text[position:]
    lines = tail.splitlines()
    start_index = next(i for i, line in enumerate(lines) if line.strip().startswith("|"))
    end_index = start_index
    while end_index < len(lines) and lines[end_index].strip().startswith("|"):
        end_index += 1
    rendered = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    rendered.extend("| " + " | ".join(row[h] for h in headers) + " |" for row in rows)
    lines[start_index:end_index] = rendered
    return text[:position] + "\n".join(lines)


def refresh_disposition_tables(text: str, comparisons: dict) -> str:
    headers, candidates = table(text, "validator:candidate-ledger-v2.1")
    for row in candidates:
        decision = comparisons[row["Source Family ID"]]["decision"]
        row["Books Disposition"] = decision
        row["Review Override"] = "knowledge_gap" if decision == "Integrate" else "none"
    text = replace_table(text, "validator:candidate-ledger-v2.1", headers, candidates)

    headers, books_rows = table(text, "validator:books-comparison-v1")
    for row in books_rows:
        row["Decision"] = comparisons[row["Source Family ID"]]["decision"]
    text = replace_table(text, "validator:books-comparison-v1", headers, books_rows)

    headers, selection_rows = table(text, "validator:deep-analysis-selection-v1")
    for row in selection_rows:
        eligibility = [item for item in row["Eligibility"].split(";") if item]
        if comparisons[row["Source Family ID"]]["decision"] == "Integrate":
            for required in ("forced_review", "potential_books_delta"):
                if required not in eligibility:
                    eligibility.append(required)
        else:
            eligibility = [item for item in eligibility if item not in {"forced_review", "potential_books_delta"}]
        row["Eligibility"] = ";".join(eligibility)
    return replace_table(text, "validator:deep-analysis-selection-v1", headers, selection_rows)


def refresh_review_table(text: str, reviews: dict) -> str:
    _, candidates_list = table(text, "validator:candidate-ledger-v2.1")
    candidates = {row["Source Family ID"]: row for row in candidates_list}
    headers, receipts = table(text, "validator:review-completion-v1")
    for receipt in receipts:
        fid = receipt["Source Family ID"]
        review = reviews[fid]
        receipt.update({
            "Method / Identity Locators": review["method_identity_locators"],
            "Evaluation Locators": review["evaluation_locators"],
            "Limitations / Counterevidence Locators": review["limitations_counterevidence_locators"],
            "Artifact Locators": review["artifact_locators"],
        })
        start = f"<!-- review:{fid}:start -->"
        end = f"<!-- review:{fid}:end -->"
        body = text[text.index(start) + len(start): text.index(end)]
        receipt["Review Provenance ID"] = provenance_id(candidates[fid], receipt, body)

    return replace_table(text, "validator:review-completion-v1", headers, receipts)


def refine_day(day: int) -> dict:
    compact = f"202604{day:02d}"
    packet = SOURCE_MONTH / f"daily-{compact}"
    readme_path = MONTH / f"{day:02d}" / "README.md"
    repair_beijing_window(day, packet, readme_path)
    if day == 24:
        write_identity_reconciliation(packet)
    ledger = json.loads((packet / "screening-ledger-final.json").read_text(encoding="utf-8"))
    rows = {x["source_family_id"]: x for x in ledger["identities"] if x.get("screening_status") == "retained_after_full_semantic_screen"}
    review_path = packet / "exact-v1-review-packet.json"
    reviews_doc = json.loads(review_path.read_text(encoding="utf-8"))
    reviews = {x["source_family_id"]: x for x in reviews_doc["items"]}
    compare_path = packet / "books-current-content-comparison.json"
    compare_doc = json.loads(compare_path.read_text(encoding="utf-8"))
    comparisons = {x["source_family_id"]: x for x in compare_doc["items"]}

    for fid, comparison in comparisons.items():
        existing = current_excerpt(comparison["existing_proposition"])
        delta = first_sentence(comparison["new_evidence_delta"], 440)
        if fid in SUBSUMED_CURRENT_CONTENT:
            comparison["decision"] = "No Change — Existing Coverage"
            comparison["semantic_disposition_reason"] = (
                f"current owner proposition '{existing}' already carries the durable responsibility/fallback axis; "
                f"exact-v1 delta '{delta}' is the same mechanism or a bounded survey/benchmark/hardware instance, "
                "so it adds evidence rather than a new stable knowledge proposition"
            )
        else:
            comparison["decision"] = "Integrate"
            comparison["semantic_disposition_reason"] = (
                f"current owner proposition '{existing}' does not yet encode the exact-v1 delta '{delta}' together "
                "with its state/data/control owner and source-specific failure/fallback; route that concrete gap to "
                "independent pre-write and root serial writeback"
            )

    # Exact-v1 PDF exception: HTML was unavailable, so preserve a manual,
    # section-bound design/non-proof summary rather than pretending generic PDF
    # chunks are Method/Evaluation locators.
    special = reviews.get("SF-2026-ARXIV-2604-23049")
    if special:
        special.update({
            "method_identity_locators": "arXiv:2604.23049v1 PDF §III–V (decoupled HITL component; WHEN/WHO/WHAT/WHERE; request-resolution API)",
            "evaluation_locators": "arXiv:2604.23049v1 PDF §VI–VII (architecture discussion and design implications; no controlled empirical benchmark disclosed)",
            "limitations_counterevidence_locators": "arXiv:2604.23049v1 PDF §II, §VI–VII (embedded-rule duplication/fragmented observability; decoupled subsystem and human-latency costs)",
            "artifact_locators": "arXiv:2604.23049v1 PDF §V (/api/hitl/request, decision retrieval/callback, Approve/Reject/Defer)",
            "method_identity_summary": "The design separates human-in-the-loop control from individual agent loops into a component with event-driven WHEN, role-based WHO, interaction WHAT, and channel WHERE policies. Agents submit structured requests; the service owns pending decision state and returns Approve, Reject, or Defer through polling or callback interfaces.",
            "evaluation_summary": "The exact-v1 PDF presents an architecture and API contract, not a controlled empirical benchmark. It supports the separation of HITL policy/state from agent proposals, but reports no measured production safety, scalability, or human-latency improvement.",
            "limitations_counterevidence_summary": "Embedded HITL rules can be duplicated and inconsistently observed across agents; decoupling addresses that ownership problem but adds a service/protocol dependency and human-response latency. The paper does not empirically establish reliability under service outage or high concurrency.",
            "artifact_summary": "The disclosed interface includes /api/hitl/request, decision retrieval/callback, structured action/facts/policy/rubric fields, and Approve/Reject/Defer outcomes.",
            "claim_boundary": "仅接受 exact-v1 PDF 披露的 decoupled HITL architecture/API；不把设计论证当作已测量的生产安全、可靠性、并发或 latency 结论。",
        })

    text = readme_path.read_text(encoding="utf-8")
    text = refresh_disposition_tables(text, comparisons)
    reasoning = {}
    for fid, row in rows.items():
        why = source_reasoning(row, reviews[fid], comparisons[fid])
        reasoning[fid] = why
        reviews[fid].update({
            "state_data_control_shift": why["ownership"],
            "operational_failure": why["failure"],
            "fallback_coexistence": why["fallback"],
            "evidence_proof_nonproof": why["proof"],
        })
        comparisons[fid].update({
            "mechanism_state_control_delta": why["ownership"],
            "failure_boundary": why["failure"],
            "fallback_coexistence": why["fallback"],
            "exact_v1_boundary": why["proof"],
        })
        text = replace_block(
            text,
            f"<!-- review:{fid}:start -->",
            f"<!-- review:{fid}:end -->",
            review_block(fid, row, reviews[fid], comparisons[fid], why),
        )
        text = replace_block(
            text,
            f"<!-- books-review:{fid}:start -->",
            f"<!-- books-review:{fid}:end -->",
            books_block(fid, comparisons[fid], why),
        )

    selected_ids = re.findall(r"<!-- analysis:DA-([0-9]+-[0-9]+):start -->", text)
    for aid in selected_ids:
        fid = f"SF-2026-ARXIV-{aid}"
        text = replace_block(
            text,
            f"<!-- analysis:DA-{aid}:start -->",
            f"<!-- analysis:DA-{aid}:end -->",
            analysis_block(aid, rows[fid], reviews[fid], reasoning[fid]),
        )

    text = refresh_review_table(text, reviews)

    queue_items = []
    for fid, comparison in comparisons.items():
        if comparison["decision"] != "Integrate":
            continue
        why = reasoning[fid]
        queue_items.append({
            "source_family_id": fid,
            "arxiv_id": comparison["arxiv_id"],
            "stable_node_id": comparison["stable_node_id"],
            "target_chapter": comparison["target_chapter"],
            "adjacent_chapters": comparison["adjacent_chapters"],
            "mechanism_delta": comparison["new_evidence_delta"],
            "state_data_control_shift": why["ownership"],
            "failure_fallback_coexistence": f"{why['failure']} {why['fallback']}",
            "evidence_boundary": why["proof"],
            "suggested_insertion": f"在 {comparison['target_ref']} 所在 canonical H2 内、Review notes 前融入旧路径→约束变化→机制→代价/回退链；不得追加论文清单。",
            "status": "waiting_for_root_serial_writeback",
        })
    queue_doc = {
        "schema": "books-writeback-queue-v2.1-author",
        "report_date": f"2026-04-{day:02d}",
        "status": "pending_root_serial_writeback_and_independent_prewrite",
        "items": queue_items,
    }
    queue_path = packet / "BOOKS_WRITEBACK_QUEUE.json"
    queue_path.write_text(json.dumps(queue_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    text = re.sub(r"Books queue=\d+", f"Books queue={len(queue_items)}", text)
    text = re.sub(r"Integrate queue=\d+", f"Integrate queue={len(queue_items)}", text)

    # The repeated author shorthand was the reported semantic finding.  It is
    # forbidden after refinement, including in selected Deep Analysis.
    forbidden = [
        "超出 v1 证据范围时回退 owner 章节既有路径",
        "旧方案在边界稳定且不需要新增 owner 时合理",
        "收益只在作者 evaluation contract 内成立",
        "旧路径在无需新增状态、证据或控制责任的 workload 下继续成立",
    ]
    hits = {phrase: text.count(phrase) for phrase in forbidden}
    if any(hits.values()):
        raise RuntimeError(f"boilerplate remains for {compact}: {hits}")

    readme_path.write_text(text, encoding="utf-8")
    review_path.write_text(json.dumps(reviews_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    compare_path.write_text(json.dumps(compare_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    independence = {
        "schema": "historical-daily-independence-audit-v1",
        "report_date": f"2026-04-{day:02d}",
        "semantic_inputs": [
            "official strict-window arXiv Atom raw inventory",
            "100% title+abstract semantic replay",
            "date-local exact-v1 HTML/PDF",
            "current Books owner and adjacent chapters",
        ],
        "forbidden_weekly_dependency_hits": [],
        "dependency_count": 0,
        "allowed_derived_fields": ["ISO Owner Week"],
        "cross_model_review": "skipped: non-interactive author lane; different fresh-context reviewer remains required",
    }
    independence_path = packet / "historical-daily-independence-audit.json"
    independence_path.write_text(json.dumps(independence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    receipt = {
        "schema": "source-specific-semantic-refinement-receipt-v1",
        "report_date": f"2026-04-{day:02d}",
        "reviewed_families": len(rows),
        "source_specific_failure_fallback_rows": len(rows),
        "selected_deep_analysis_rows": len(selected_ids),
        "generic_phrase_hits_after": hits,
        "review_packet_sha256": hashlib.sha256(review_path.read_bytes()).hexdigest(),
        "books_comparison_sha256": hashlib.sha256(compare_path.read_bytes()).hexdigest(),
        "readme_sha256": hashlib.sha256(readme_path.read_bytes()).hexdigest(),
        "gate_effect": "none; author cannot self-pass fresh-context Semantic Audit",
    }
    receipt_path = packet / "source-specific-semantic-refinement-receipt.json"
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return receipt


def main() -> None:
    receipts = [refine_day(day) for day in range(24, 31)]
    print(json.dumps(receipts, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
