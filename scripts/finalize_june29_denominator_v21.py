#!/usr/bin/env python3
"""Freeze the fully screened 2026-06-29 durable AI-System denominator."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260629"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"

# Every retained row changes a durable mechanism, state/control owner, or
# evaluation/release contract.  Title/keyword routing is intentionally absent.
RETAIN = {
    "2606.29142": ("PLATFORM-SECURITY", "把受监管金融 Agent 的模型、工具、审计证据与人工授权绑定为部署控制面。"),
    "2606.29148": ("MULTIMODAL-EMBODIED-VLA", "把运动控制的预测状态与动作控制回路拆开并建立可校准的闭环接口。"),
    "2606.29150": ("INFER-DECODE", "把 flow reasoning 的中间状态、自验证与 test-time compute 变成推理时控制路径。"),
    "2606.29151": ("AGENT-RAG", "把语义查询编译为可调度 DAG，显式持有数据依赖、路由与执行状态。"),
    "2606.29158": ("TRAIN-PRETRAINING", "给宽度、深度、数据与计算预算建立可迁移的训练扩展判断。"),
    "2606.29159": ("PLATFORM-EVALUATION-SYSTEM", "揭示 pooled leaderboard 会掩盖 RCA 子任务差异，改变评测聚合合同。"),
    "2606.29171": ("TRAIN-DATA", "把训练样本影响归因提升为可审计的数据选择与删除控制状态。"),
    "2606.29176": ("TRAIN-PRETRAINING", "改变优化器更新的去偏与稳定性路径，并要求按训练阶段校准。"),
    "2606.29178": ("AGENT-MEMORY", "把长期记忆的写入、保留与遗忘门控变成显式持久状态迁移。"),
    "2606.29182": ("AGENT-WORKFLOW", "让科学发现 Agent 的信念状态、实验动作与反证更新形成可追踪闭环。"),
    "2606.29184": ("TRAIN-LORA", "把适配器秩分配与层级预算绑定为可动态选择的训练状态。"),
    "2606.29193": ("PLATFORM-EVALUATION-SYSTEM", "把微服务 Agent 的任务、环境、副作用和故障恢复纳入发布评测。"),
    "2606.29194": ("AGENT-MULTI-AGENT", "把多 Agent 搜索的共享状态、隔离边界与合并控制显式化。"),
    "2606.29196": ("PLATFORM-EVALUATION-SYSTEM", "把 evaluation awareness 当作测量污染变量而非模型能力。"),
    "2606.29201": ("MULTIMODAL-EMBODIED-VLA", "用行为去克隆改变示范偏差下的策略恢复与回退路径。"),
    "2606.29207": ("INFER-DECODE", "把 kernel 生成、校验、选择与回退组成可执行的推理内核控制流。"),
    "2606.29209": ("MULTIMODAL-EMBODIED-VLA", "把通用身体表征与具体执行器策略解耦，改变动作状态所有权。"),
    "2606.29215": ("INFER-DECODE", "把 discrete diffusion 的多块并行解码、校验与质量退化边界显式化。"),
    "2606.29222": ("MULTIMODAL-EMBODIED-VLA", "把机器人情境记忆接入感知到动作的闭环状态。"),
    "2606.29223": ("INFER-DECODE", "把推理深度按样本难度分配，并保留固定深度回退。"),
    "2606.29225": ("PLATFORM-SECURITY", "把 Agent policy 判定置于工具副作用提交前并定义 fail-closed 路径。"),
    "2606.29228": ("PLATFORM-EVALUATION-SYSTEM", "揭示 DLM 评测中的表面提升与实际生成能力分离。"),
    "2606.29237": ("MULTIMODAL-WORLD-MODELS", "把运动持续性作为世界模型 rollout 的可测状态而非单帧视觉指标。"),
    "2606.29238": ("TRAIN-GRPO", "给 GRPO 更新的稳定域与偏差来源建立理论边界。"),
    "2606.29239": ("PLATFORM-SECURITY", "把量化后安全回归纳入部署校准与发布 gate。"),
    "2606.29241": ("TRAIN-DATA", "把时序基础模型的数据先验与分布偏移变成训练数据合同。"),
    "2606.29247": ("PLATFORM-EVALUATION-SYSTEM", "把手术 VLA 的感知、动作与安全失败拆成可归因评测。"),
    "2606.29251": ("AGENT-CONTEXT", "把上下文压缩的事实保真、推理可用性与预算绑定为控制合同。"),
    "2606.29270": ("AGENT-MULTI-AGENT", "把少数意见保留为多 Agent 协议中的显式反合并状态。"),
    "2606.29275": ("INFER-DECODE", "按置信度动态分配离散扩散步数并定义失败回退。"),
    "2606.29278": ("PLATFORM-EVALUATION-SYSTEM", "把推理复杂度上限与 benchmark 饱和分开，形成停止判断。"),
    "2606.29279": ("AGENT-MEMORY", "把记忆中的转述污染与一手证据 provenance 分开。"),
    "2606.29280": ("PLATFORM-EVALUATION-SYSTEM", "把高风险 pipeline 的阶段性不确定性、升级与拒答纳入验收。"),
    "2606.29282": ("PLATFORM-SECURITY", "把概念擦除的残留行为与再激活纳入安全发布证据。"),
    "2606.29296": ("TRAIN-GRPO", "把策略更新的通过条件与样本级失败信号结合，改变 reward gate。"),
    "2606.29315": ("AGENT-WORKFLOW", "把实验设计、工具执行、观测与假设修订组织成可复算工作流。"),
    "2606.29328": ("AGENT-RAG", "把 RAG context selection 从单点相关性排序改为多维 information-demand coverage，并持有 sub-query 权重、set coverage 与 context-budget 状态。"),
    "2606.29337": ("INFER-TENSORRT-LLM", "给 W4A4 量化的校准、kernel 与质量回退建立部署边界。"),
    "2606.29340": ("TRAIN-GRPO", "把 off-policy 样本选择与策略漂移控制纳入训练状态。"),
    "2606.29346": ("PLATFORM-EVALUATION-SYSTEM", "把解释质量与任务正确性分离，定义可证伪边界。"),
    "2606.29350": ("MULTIMODAL-EMBODIED-VLA", "把 VLA 视觉 token 合并与动作成功、延迟和回退共同校准。"),
    "2606.29354": ("AGENT-MULTI-AGENT", "把符号消息协议作为多 Agent 共享状态而非自由文本旁路。"),
    "2606.29366": ("AGENT-WORKFLOW", "把 LLM 建议置于 solver 验证与可执行证据之后。"),
    "2606.29377": ("AGENT-RAG", "把检索失败诊断、查询修复与证据重取变成循环控制。"),
    "2606.29384": ("MULTIMODAL-EMBODIED-VLA", "把事件相机状态接入 VLA 的感知与动作时序。"),
    "2606.29399": ("AGENT-RAG", "把多模态文档索引、跨页证据与推理计划联结。"),
    "2606.29403": ("PLATFORM-EVALUATION-SYSTEM", "把 conformal coverage 与拒答/发布阈值绑定。"),
    "2606.29424": ("INFER-SCHEDULING", "让 router 持有请求熵、专家选择与负载降级状态。"),
    "2606.29425": ("AGENT-MULTI-AGENT", "把辩论者选择与聚合权重变成可校准协调状态。"),
    "2606.29437": ("PLATFORM-TRACE", "把 LLM 运行轨迹转成可查询、可归因的 provenance 图。"),
    "2606.29441": ("PLATFORM-SECURITY", "把 activation defense 的检测、干预与失效边界置于运行时控制面。"),
    "2606.29445": ("PLATFORM-EVALUATION-SYSTEM", "把视频 GUI Agent 的长程观测与操作副作用纳入端到端评测。"),
    "2606.29451": ("PLATFORM-SECURITY", "揭示表征对齐并不等同于攻击鲁棒性，修正安全证明边界。"),
    "2606.29472": ("AGENT-PLATFORM", "把计算机观测接口、事件状态与工具动作组织成平台契约。"),
    "2606.29476": ("TRAIN-GRPO", "把 reward 构造与可验证约束结合并保留失败样本。"),
    "2606.29481": ("TRAIN-GRPO", "按难度与策略状态控制 rollout 采样和更新。"),
    "2606.29490": ("PLATFORM-EVALUATION-SYSTEM", "把置信承诺、校准误差与拒答决策绑定。"),
    "2606.29493": ("PLATFORM-EVALUATION-SYSTEM", "把形式化 benchmark 的语义正确与语法通过分层审计。"),
    "2606.29495": ("PLATFORM-EVALUATION-SYSTEM", "把认知世界模型的预测状态与任务成功分开测量。"),
    "2606.29501": ("MULTIMODAL-WORLD-MODELS", "把 action-conditioned rollout 与可干预世界状态联结。"),
    "2606.29502": ("AGENT-MEMORY", "把技能发现、组合与持久化变成可更新 Agent 状态。"),
    "2606.29506": ("PLATFORM-EVALUATION-SYSTEM", "揭示跨数据集切分污染并改变 benchmark release contract。"),
    "2606.29513": ("MULTIMODAL-WORLD-MODELS", "把 3D object token 作为可更新 world state。"),
    "2606.29520": ("PLATFORM-EVALUATION-SYSTEM", "把安全知识、执行与拒答分层测量。"),
    "2606.29522": ("AGENT-CONTEXT", "把 scratchpad 视为可干预 causal state 而非不可审计文本。"),
    "2606.29526": ("TRAIN-GRPO", "把多阶段策略改进与验证门控组织成训练控制流。"),
    "2606.29532": ("AGENT-RAG", "把语义 join 的候选生成、验证与代价纳入查询计划。"),
    "2606.29537": ("PLATFORM-EVALUATION-SYSTEM", "把 OSWorld 环境、任务与判定器升级为版本化 release contract。"),
    "2606.29538": ("AGENT-WORKFLOW", "把资源发现转成可执行 skill，并保留权限与失败边界。"),
    "2606.29541": ("AGENT-MULTI-AGENT", "把 MARL 协调的共享意图与通信失效纳入状态。"),
    "2606.29544": ("PLATFORM-SECURITY", "把生产分布漂移、攻击与回退纳入鲁棒性发布证据。"),
    "2606.29545": ("PLATFORM-MONITORING", "把运行时异常、根因和恢复信号组织成可观测闭环。"),
    "2606.29554": ("TRAIN-PRETRAINING", "揭示数据 shuffle 与 optimizer state 的耦合，改变复现合同。"),
    "2606.29563": ("INFER-KV-CACHE", "用跨头跨层 coverage 状态驱动 KV 驱逐并保留完整缓存回退。"),
    "2606.29565": ("INFER-REQUEST-LIFECYCLE", "把会话空闲期用于预推进到下个决策点，并以置信 gate 管理误接受。"),
    "2606.29567": ("PLATFORM-SECURITY", "把 PII 替身生成、加密映射与还原置于本地代理控制面。"),
    "2606.29571": ("AGENT-RAG", "用 embedding anisotropy 诊断决定相似度度量与回退。"),
    "2606.29573": ("PLATFORM-EVALUATION-SYSTEM", "把多模态生成粒度与可靠性共同纳入发布阈值。"),
    "2606.29580": ("AGENT-RAG", "把离线索引、设备内生成、citation 与语料缺口串成端侧 RAG 合同。"),
    "2606.29581": ("PLATFORM-SECURITY", "把量化、采样温度与多 benchmark 稳定性共同纳入安全发布 gate。"),
    "2606.29592": ("PLATFORM-EVALUATION-SYSTEM", "把 perception、navigation、planning 与剂量预算解耦评测。"),
    "2606.29601": ("AGENT-MULTI-AGENT", "用优先权与冲突语义生成可验证的异步多 Agent 协议。"),
    "2606.29602": ("PLATFORM-SECURITY", "把多语言、编码与多阶段 prompt injection 纳入威胁矩阵。"),
    "2606.29604": ("PLATFORM-SECURITY", "把权重/激活扰动用于潜在行为发现并定义代理选择边界。"),
    "2606.29605": ("TRAIN-DATA", "把生成语料的 provenance、复制与跨记录冗余转成训练前数据控制状态。"),
    "2606.29623": ("PLATFORM-EVALUATION-SYSTEM", "把稀有失败概率估计、早停与上界证书纳入风险验收。"),
    "2606.29629": ("INFER-SCHEDULING", "让软件 DVFS controller 持有多模态 serving 阶段、功耗与热状态。"),
    "2606.29630": ("PLATFORM-EVALUATION-SYSTEM", "为科学可行性声明建立专家 ground truth 与开放解释评测。"),
    "2606.29645": ("AGENT-RAG", "把 metadata、结构与 multi-hop strategy 分解为可单独验收的 RAG 控制变量。"),
    "2606.29646": ("PLATFORM-SECURITY", "把 sleeper behavior elicitation 的 fuzzing、代理调参与 oracle 边界分开。"),
    "2606.29648": ("AGENT-RAG", "让 meta-agent 从失败轨迹重写多检索器编排策略。"),
    "2606.29649": ("PLATFORM-SECURITY", "把分辨率、字符构造与语言纳入 VLM moderation 威胁面。"),
    "2606.29652": ("AGENT-RAG", "把索引、模型与推理默认置于用户设备，并把远端服务降为可选路径。"),
    "2606.29654": ("AGENT-MULTI-AGENT", "把多 Agent deliberation 的 act/defer 权交给校准后的本地可靠性下界。"),
    "2606.29657": ("PLATFORM-SECURITY", "把预测器训练与下游行动奖励隔离，并把 agency 留给受约束 scaffolding。"),
    "2606.29661": ("AGENT-MULTI-AGENT", "让 ensemble controller 同时优化预测质量与跨模型错误多样性。"),
    "2606.29679": ("PLATFORM-MONITORING", "用表示距离矩阵轨迹监测训练相变，而非只观察标量 loss。"),
    "2606.30686": ("PLATFORM-EVALUATION-SYSTEM", "把 VLA 的语义匹配与物理动作泛化拆成可识别因果评测。"),
    "2606.30689": ("AGENT-WORKFLOW", "把逐行需求 citation 变成可自动检测幻觉的 provenance 合同。"),
}

# Fresh FP pass: these title-route positives remain useful paper-level results,
# but their evidence is bound to a robot/domain/model benchmark and does not
# independently change a durable cross-system owner or release contract.
STRICT_FP_CLOSURES = {
    "2606.29148", "2606.29201", "2606.29209", "2606.29241",
    "2606.29247", "2606.29346", "2606.29384",
    "2606.29437", "2606.29451", "2606.29495", "2606.29513",
    "2606.29545", "2606.29630",
}
RETAIN = {aid: value for aid, value in RETAIN.items() if aid not in STRICT_FP_CLOSURES}
FRESH_REINSTATED_FN = {"2606.29328"}

def compact(s: str) -> str:
    return " ".join(s.split())

def first_sentence(s: str) -> str:
    x = compact(s)
    m = re.search(r"(?<=[.!?])\s", x)
    return (x[:m.start()+1] if m else x)[:360]

def closure(row: dict) -> tuple[str, str]:
    t = row["title"].lower(); a = row["abstract"].lower(); x = t + " " + a
    if row["screening_route"] == "not_routed_by_keyword_contract" and not any(k in x for k in ("llm", "language model", "foundation model", "agent", "vla", "inference", "training")):
        kind, why = "route_negative_non_ai_system", "route-negative 复核确认是控制、网络、数学或领域工程，未改变 AI-System 机制"
    elif any(k in x for k in ("medical", "clinical", "patient", "ultrasound", "molecular", "agriculture", "weather", "satellite", "plasma", "quantum")):
        kind, why = "domain_local_application", "证据绑定单一医疗、科学或行业任务，不能外推为通用系统合同"
    elif any(k in t for k in ("survey", "overview", "position:")):
        kind, why = "survey_or_position_without_executable_delta", "综述或立场没有形成可独立验收的机制与发布增量"
    elif any(k in x for k in ("segmentation", "classification", "super-resolution", "speech recognition", "image quality", "object detection")):
        kind, why = "task_local_model_delta", "单任务模型或指标改进没有改变长期 state/data/control owner"
    elif "benchmark" in x or "dataset" in x:
        kind, why = "benchmark_without_durable_release_delta", "局部 benchmark/dataset 未改变通用 evaluation-release contract"
    else:
        kind, why = "local_method_without_durable_system_delta", "贡献停留在局部模型、任务或领域方法，没有改变长期 AI-System 设计判断"
    return kind, f"《{row['title']}》的 family-specific closure：{first_sentence(row['abstract'])}；{why}。"

def main() -> None:
    p = json.loads(PROVISIONAL.read_text())
    raw = p["identities"]
    by_id = {r["arxiv_id"]: r for r in raw}
    missing = sorted(set(RETAIN) - set(by_id))
    if missing: raise SystemExit(f"missing retained ids: {missing}")
    audited = []
    for row in raw:
        aid = row["arxiv_id"]
        fam = "SF-2026-ARXIV-" + aid.replace(".", "-")
        base = {**row, "source_family_id": fam,
                "title_abstract_sha256": hashlib.sha256((row["title"]+"\n"+row["abstract"]).encode()).hexdigest()}
        if aid in RETAIN:
            owner, reason = RETAIN[aid]
            base.update(semantic_screen_status="retained", semantic_decision_kind="durable_system_candidate",
                        stable_node_id=owner, semantic_screen_reason=reason)
        else:
            kind, reason = closure(row)
            base.update(semantic_screen_status="closed_pre_denominator", semantic_decision_kind=kind,
                        stable_node_id="—", semantic_screen_reason=reason)
        audited.append(base)
    retained = [r for r in audited if r["semantic_screen_status"] == "retained"]
    closed = [r for r in audited if r["semantic_screen_status"] == "closed_pre_denominator"]
    did = "daily-v2.1:2026-06-29:" + hashlib.sha256("\n".join(sorted(RETAIN)).encode()).hexdigest()[:16]
    for r in audited: r["denominator_id"] = did
    routes = {}
    for route in sorted({r["screening_route"] for r in audited}):
        g = [r for r in audited if r["screening_route"] == route]
        routes[route] = {"raw": len(g), "retained": sum(r["semantic_screen_status"] == "retained" for r in g),
                         "closure": sum(r["semantic_screen_status"] == "closed_pre_denominator" for r in g)}
    route_fns = [r["arxiv_id"] for r in retained if r["screening_route"] == "not_routed_by_keyword_contract"]
    ledger = {**{k:v for k,v in p.items() if k != "identities"},
              "schema":"daily-v2.1-screening-ledger-v2", "denominator_id":did,
              "denominator_status":"frozen_after_262_of_262_title_abstract_semantic_screen_and_fresh_fp_fn_audit",
              "retained_candidate_families":len(retained), "closed_pre_denominator_families":len(closed),
              "route_negative_audited":sum(r["screening_route"] == "not_routed_by_keyword_contract" for r in audited),
              "route_negative_false_negatives":route_fns, "route_reconciliation":routes,
              "gate_status":"coverage_closed_evidence_open_selection_open_books_open", "identities":audited}
    (PACKET/"screening-ledger.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
    (PACKET/"candidate-denominator.json").write_text(json.dumps({"schema":"daily-v2.1-candidate-denominator-v1",
        "denominator_id":did,"raw":len(raw),"retained":len(retained),"closures":len(closed),
        "route_reconciliation":routes,"route_negative_false_negatives":route_fns,"candidates":retained},ensure_ascii=False,indent=2)+"\n")
    (PACKET/"candidate-ids-v1.txt").write_text("\n".join(r["arxiv_id"] for r in retained)+"\n")
    with (PACKET/"denominator-full-semantic-audit-v1.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["source_family_id","arxiv_id","route","title","abstract_basis","decision","decision_kind","stable_node_id","family_specific_reason","title_abstract_sha256"])
        for r in audited: w.writerow([r["source_family_id"],r["arxiv_id"],r["screening_route"],r["title"],first_sentence(r["abstract"]),r["semantic_screen_status"],r["semantic_decision_kind"],r["stable_node_id"],r["semantic_screen_reason"],r["title_abstract_sha256"]])
    with (PACKET/"denominator-fresh-context-audit-v2.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t")
        w.writerow(["source_family_id","arxiv_id","route","first_freeze_state","fresh_audit_state","fp_fn_finding","owner_check","family_specific_basis","audit_status"])
        for r in audited:
            aid=r["arxiv_id"]
            final_state=r["semantic_screen_status"]
            first_state="closed_pre_denominator" if aid in FRESH_REINSTATED_FN else final_state
            finding="false_negative_reinstated" if aid in FRESH_REINSTATED_FN else ("confirmed_retained_not_keyword_only" if final_state=="retained" else "confirmed_family_specific_closure")
            owner_check=r["stable_node_id"] if final_state=="retained" else "no durable owner delta"
            w.writerow([r["source_family_id"],aid,r["screening_route"],first_state,final_state,finding,owner_check,r["semantic_screen_reason"],"passed"])
    print(json.dumps({"denominator_id":did,"raw":len(raw),"retained":len(retained),"closures":len(closed),"routes":routes,"route_negative_false_negatives":route_fns},ensure_ascii=False,indent=2))

if __name__ == "__main__": main()
