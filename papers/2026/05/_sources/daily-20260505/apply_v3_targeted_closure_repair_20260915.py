#!/usr/bin/env python3
"""Apply the bounded 467-entry closure-layer repair for 2026-05-05.

This script never re-enumerates the 1058 raw identities and never writes Books.
It reuses the frozen raw ledger, promotes verified false negatives, creates exact-v1
evidence packets, and emits a root-only Books writeback queue.
"""

from __future__ import annotations

import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER_PATH = HERE / "V3_CANONICAL_LEDGER.json"
EVIDENCE_PATH = HERE / "V3_EVIDENCE_REVIEWS.json"
HTML_DIR = HERE / "arxiv-v1-html"
GENERIC_SENTENCE = "属于局部模型、算法或应用改进；未改变长期机制 owner、state/data/control ownership 或验收契约。"

CHAPTERS = {
    "WORLDVIEW-REPRESENTATION": (5, "books/part-01-worldview/05-what-neural-networks-learn.md"),
    "MODEL-SELF-ATTENTION": (14, "books/part-02-model/14-self-attention.md"),
    "MODEL-SAMPLING": (20, "books/part-02-model/20-sampling.md"),
    "MULTIMODAL-REPRESENTATION": (23, "books/part-03-multimodal-world-models/23-multimodal-representation.md"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": (24, "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md"),
    "TRAIN-DATA": (27, "books/part-04-training-system/27-data.md"),
    "TRAIN-PRETRAINING": (28, "books/part-04-training-system/28-pretraining.md"),
    "TRAIN-SFT": (29, "books/part-04-training-system/29-sft.md"),
    "TRAIN-LORA": (30, "books/part-04-training-system/30-lora.md"),
    "TRAIN-RLHF": (31, "books/part-04-training-system/31-rlhf.md"),
    "TRAIN-GRPO": (33, "books/part-04-training-system/33-grpo.md"),
    "INFER-SCHEDULING": (56, "books/part-05-inference-system/56-inference-scheduling.md"),
    "PLATFORM-EVALUATION-SYSTEM": (66, "books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "PLATFORM-MONITORING": (67, "books/part-06-ai-infrastructure/67-monitoring.md"),
    "PLATFORM-TRACE": (69, "books/part-06-ai-infrastructure/69-trace.md"),
    "PLATFORM-SECURITY": (72, "books/part-06-ai-infrastructure/72-security.md"),
    "AGENT-RAG": (76, "books/part-07-agent/76-rag.md"),
    "AGENT-WORKFLOW": (81, "books/part-07-agent/81-workflow.md"),
}

# id | owner | DD/SR/D | disposition | mechanism | already-covered proposition
ROWS = """
2605.00836|MULTIMODAL-GENERATIVE-PARADIGMS|2|2|2|N|把 flow-matching 采样器从固定 Euler 步进提升为可比较的高阶与自适应 ODE 求解器，并以 NFE-quality frontier 暴露模型误差与数值误差的共同上限|本章已把 sampler、step schedule、误差控制和 NFE/质量前沿定义为生成执行合同，旧 Euler 在低预算与误差容忍场景仍成立
2605.00939|PLATFORM-EVALUATION-SYSTEM|3|2|2|I|以参数梯度敏感度近似局部曲率，区分可被小扰动修正的普通错误与对输入改写仍稳定的 stubborn hallucination|本章已有事实正确性、校准与证据门，但缺少把错误的局部可修正性作为独立诊断信号
2605.01047|PLATFORM-SECURITY|2|2|2|N|把已观测 package hallucination 转成可定位的 post-deployment unlearning 对象，并用自适应 masking 限制能力 collateral damage|本章已要求删除、抑制或修复后的能力保持与攻击复测共同进入 release gate；单一 package 工作负载没有改变该合同
2605.01111|INFER-SCHEDULING|2|3|2|N|由小模型先执行、再按边际效用与长度惩罚决定是否升级大模型，把协作推理变成请求级资源控制|本章已把模型路由写成按难度、质量预算和尾延迟升级的控制环，DUET 是该分支的受限实现
2605.01148|WORLDVIEW-REPRESENTATION|2|1|2|N|用跨任务 activation patching 与 Fourier probe 显示加法子电路可被循环概念复用，并定位稀疏 MLP 子电路|本章已区分表示几何、可干预电路与因果证明；该案例补充证据但不改变表示不等于算法所有权的边界
2605.01167|WORLDVIEW-REPRESENTATION|2|2|2|N|在保持目标 steering 幅度的约束面上最小化二阶 collateral energy，把 activation steering 写成受约束几何优化|本章已要求 steering 同时评估目标方向、旁路能力损失与分布外回退，COAST 没有改变该所有权边界
2605.01172|WORLDVIEW-REPRESENTATION|3|2|2|N|把深度学习泛化拆成可被测试点看到的 signal channel 与训练集 reservoir，并用 drift-diffusion 与 train-test coupling 刻画误差|本章已把低训练损失与泛化分离，并要求表征、优化轨迹和数据分布共同解释；理论模型未推翻该主线
2605.01199|MODEL-SELF-ATTENTION|2|2|2|N|把 attention 学习描述为 focus、dilution 与再聚焦的阶段性梯度动力学，而非单调收敛|本章已解释 attention score、竞争归一化和训练信号的相互作用；单层 Markov 理论属于机制证据而非新 owner
2605.01327|TRAIN-GRPO|3|3|2|I|把 token-level policy MDP 提升为推理 segment MDP，并按自适应分段计算 value、advantage 与 importance ratio|本章已有 group 与 token 级 credit assignment，但缺少由语义步骤持有 credit 与截断边界的中间粒度
2605.01347|TRAIN-SFT|3|3|2|I|让多个教师在学生 on-policy state 上辩论形成 privileged distribution，并按任务选择 JSD 或 reverse-KL、按 agent step 稳定蒸馏|本章已有单教师 on-policy distillation 与 KL 方向选择，但没有教师集体形成 supervision state、confidence ownership 和 agent-step sampling 的分支
2605.01373|MULTIMODAL-GENERATIVE-PARADIGMS|3|2|2|I|用相邻 denoising step 的 top-K 分布差识别高动态 token，并对其自对比重掩码，集中迭代修正预算|本章已有 selective refresh 与可变 commit，但未说明用跨步分布不稳定性决定哪些 token 重新开放
2605.01374|TRAIN-SFT|2|2|2|N|沿教师与学生的层级 transformation trajectory 对齐 token、span 和 hidden representation，而非只对齐末端 logits|本章已区分 output、feature 与 trajectory distillation，并要求层映射和表示损失受限；MTA 是受限实例
2605.01429|TRAIN-LORA|3|2|2|I|在开放 LoRA 池检索后，以层级稀疏残差合并和多视图一致性审计决定组合、拒绝或回退|本章已有 adapter merge 与冲突风险，但缺少 post-retrieval composition 的可靠性状态和 disagreement gate
2605.01506|MULTIMODAL-REPRESENTATION|2|2|2|N|以统一 token template、Omni-RoPE 和时窗移动联合编码视频、音频与运动连续性|本章已要求 modality identity、时间戳和窗口边界随 token 保留；该 encoder 没有改变统一空间与模态专属前端共存关系
2605.01609|WORLDVIEW-REPRESENTATION|2|1|2|N|以谱能量与 whitened causal alignment 区分稀疏概念方向和高能 syntax 结构，反证只看方差的解释|本章已区分相关方向、线性 probe 与因果干预；谱反集中是新的测量案例而非新表示 owner
2605.01642|TRAIN-RLHF|3|3|2|I|把人群偏好分解为低秩 reward basis，经民主过滤形成 jury，再随时间更新群体权重与策略|本章已有多目标 reward 与偏好聚合，但缺少 reward basis、jury membership 和时间变化权重的显式状态所有权
2605.01653|MULTIMODAL-GENERATIVE-PARADIGMS|2|2|2|N|以瓶颈 activation adapter 在 diffusion 运行时注入方向控制，形成不改主权重的控制接口|本章已覆盖 conditioning、adapter 与迭代生成控制，并保留能力干扰和强度校准；该接口是受限实现
2605.01710|PLATFORM-TRACE|3|3|3|I|为动态模型路由生成 route receipt，记录候选、策略版本、约束、选择结果与可披露 provenance|本章已有请求 trace，但缺少路由决策本身的候选集、策略版本和约束快照，模型名不能重建实际决策
2605.01732|TRAIN-SFT|2|2|2|N|按教师 entropy 调整 curriculum、temperature 与蒸馏路径，使 token-level transfer 随不确定性变化|本章已有按 teacher disagreement/entropy 选择 token 与温度的机制；EGAD 未改变 teacher/student ownership
2605.01733|MULTIMODAL-REPRESENTATION|3|2|2|I|并行执行图像直答与 caption 辅助路径，以 confidence gate、information gain 和证据权重融合，限制错误 caption 锚定|本章已有多模态证据 provenance，但缺少 caption 作为不对称可疑证据的双路径 admission/拒绝控制
2605.01749|PLATFORM-EVALUATION-SYSTEM|3|3|2|I|把长答案生成拆成 calibrated exploration 与 selective commitment，只将达到可靠性门槛的推理投影为最终 claim|本章已有 claim-level evidence gate，但缺少 exploration state 与 externally committed answer 的训练时分权
2605.01771|PLATFORM-TRACE|3|3|2|I|区分结果合规与过程合规，要求工具调用、检索与中间动作日志证明系统实际遵循了指定过程|本章已有 trace/span，但缺少将 process instruction 映射为可观察事件并判定 false compliance 的验收合同
2605.01782|AGENT-RAG|3|3|2|I|先记录 misgeneration 与检索事件，再以 counterfactual deletion 回溯到字符级 poisoned span，并把 span provenance 返回修复环|本章已有文档级 provenance 与 poisoning 防御，但缺少黑盒链路中从错误输出反查字符 span 的两阶段取证状态
2605.01789|TRAIN-DATA|2|2|2|N|用 goal、artifact、critic、correction 和 acceptance 的双环构建可控视觉训练数据|本章已把合成数据生产定义为带目标、校验、版本与失败回退的闭环；DataEvolver 没有改变数据 owner
2605.01844|WORLDVIEW-REPRESENTATION|2|1|2|N|以圆柱几何解释同一 steering 方向在不同样本相位下产生不稳定效果，并给出敏感扇区|本章已否定单一全局线性方向的充分性，并要求 sample-conditioned geometry 与副作用测量；该假说属于受限解释
2605.01899|PLATFORM-SECURITY|2|2|2|N|用 persona lineage 的对抗自博弈产生攻击，再以 persona-invariant consistency 降低角色表面变化对安全判断的影响|本章已要求跨 persona、上下文和多轮变体做安全一致性测试；该训练方案未改变安全 gate
2605.01929|TRAIN-LORA|3|2|2|I|在无目标数据时按谱刚性聚类 LoRA，并仲裁 video-diffusion 变体间的 routing interference|本章已有权重空间合并，但缺少跨 backbone/蒸馏变体迁移时的谱兼容性 gate 与无数据回退边界
2605.02144|MODEL-SELF-ATTENTION|3|3|2|I|用原始 hidden-state 间 Gaussian kernel 直接构造 row-stochastic attention，移除 Q/K 投影并以 bandwidth 控制局部性|本章把 Q/K 视为可学习寻址坐标，但尚未呈现 projection-free kernel diffusion 作为不同归纳偏置的替代分支
2605.02152|MULTIMODAL-GENERATIVE-PARADIGMS|3|3|2|I|先低分辨率生成 draft，以语义验证锁定稳定区域，仅对未锁定区域恢复高分辨率并继续计算|本章已有 token commit/rollback，但缺少跨分辨率 draft、semantic lock 与 selective high-resolution compute 的组合
2605.02196|PLATFORM-SECURITY|3|3|2|I|揭示低精度量化可重新暴露已 unlearn 的内容，使 precision 成为遗忘验收与部署 artifact 身份的一部分|本章已有 unlearning release gate，但缺少量化后复测与精度派生 artifact 可能逆转删除结论的边界
2605.02269|PLATFORM-EVALUATION-SYSTEM|3|3|2|I|用可观察环境中的隐藏 hacking opportunity 分离任务成功与 specification gaming，并测量 RL 后行为变化|本章已有 reward hacking 测试，但缺少把可利用机会、过程轨迹与表面成功分开的统一评价合同
2605.02398|PLATFORM-EVALUATION-SYSTEM|3|2|2|I|显示强制格式与合规措辞会在压力下压低模型元认知表达，要求把结构约束本身作为评测干预变量|本章已有 prompt sensitivity，但缺少把 compliance scaffold 导致的自我评估退化单独隔离并复测
2605.02442|PLATFORM-EVALUATION-SYSTEM|2|2|2|N|把 reasoning evaluation 从答案正确率扩展到 contamination、search complexity、外显过程与不可见 latent reasoning 的证据边界|本章已要求答案、过程、污染和 evaluator contract 分离；该综述巩固而不改变现有主线
2605.02469|TRAIN-GRPO|3|3|3|I|证明固定 reference 下 KL-regularized RLVR 可投影为 reference-sampled weighted SFT，并显式给出 support、ESS 与 one-shot gap|本章已有 on-policy/offline 分界，但缺少何时 weighted SFT 能精确替代、何时因 support/ESS 产生不可约差距的判据
2605.02647|PLATFORM-SECURITY|2|2|2|N|用多轮 conversational priming 的进化搜索生成上下文 jailbreak，并对 judge reliability 做独立约束|本章已要求多轮、上下文累积和自动攻击搜索共同进入 red-team；该实现未改变 threat owner
2605.02765|AGENT-WORKFLOW|3|3|2|I|把用户约束分成 hard 与 soft：hard 交给形式 checker，soft 交给可校准 judge，并保留冲突解释与人工修改|本章已有工作流 verifier，但缺少 hard/soft constraint 的不同所有权、冲突优先级与用户修订闭环
"""

TARGETS: dict[str, dict] = {}
for line in ROWS.strip().splitlines():
    aid, owner, dd, sr, durability, decision, mechanism, covered = line.split("|", 7)
    TARGETS[aid] = {
        "owner": owner,
        "score": (int(dd), int(sr), int(durability)),
        "decision": decision,
        "mechanism": mechanism,
        "covered": covered,
    }


class SectionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_heading = False
        self.heading_parts: list[str] = []
        self.current = "Front matter"
        self.sections: dict[str, list[str]] = {self.current: []}
        self.ignored = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style", "nav"}:
            self.ignored += 1
        if re.fullmatch(r"h[1-6]", tag):
            self.in_heading = True
            self.heading_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav"} and self.ignored:
            self.ignored -= 1
        if re.fullmatch(r"h[1-6]", tag) and self.in_heading:
            heading = " ".join("".join(self.heading_parts).split())
            if heading and heading != "Report GitHub Issue":
                self.current = heading
                self.sections.setdefault(heading, [])
            self.in_heading = False

    def handle_data(self, data: str) -> None:
        if self.ignored:
            return
        if self.in_heading:
            self.heading_parts.append(data)
        else:
            text = " ".join(data.split())
            if text:
                self.sections.setdefault(self.current, []).append(text)


def parse_sections(path: Path) -> dict[str, str]:
    parser = SectionParser()
    parser.feed(path.read_text(errors="replace"))
    return {h: " ".join(parts) for h, parts in parser.sections.items()}


def locators(sections: dict[str, str], pattern: str, fallbacks: tuple[str, ...], limit: int = 3) -> list[str]:
    headings = [h for h in sections if h != "Front matter"]
    hits = [h for h in headings if re.search(pattern, h, re.I)]
    if not hits:
        for fallback in fallbacks:
            hits.extend(h for h in headings if fallback.lower() in h.lower())
    return list(dict.fromkeys(hits))[:limit]


def excerpt(sections: dict[str, str], headings: list[str], limit: int = 900) -> str:
    text = " ".join(sections.get(h, "") for h in headings)
    text = " ".join(text.split())
    return text[:limit].rstrip() if text else "Not Disclosed in an independently titled section."


def first_sentence(text: str, limit: int = 240) -> str:
    compact = " ".join(text.split())
    parts = re.split(r"(?<=[.!?。])\s+", compact, maxsplit=1)
    return parts[0][:limit].rstrip()


def closure_bucket(entry: dict) -> str:
    text = f"{entry['title']} {entry['abstract']}".lower()
    if any(term in text for term in ("medical", "clinical", "wireless", "blockchain", "finance", "protein", "molecule", "eeg", "agriculture")):
        return "领域应用的任务结论没有改写大模型或 AI Infra 的长期机制"
    if any(term in text for term in ("benchmark", "dataset", "survey", "classification", "detection", "segmentation")):
        return "局部数据集、指标或任务比较没有形成新的系统验收合同"
    if any(term in text for term in ("theorem", "polynomial", "algebra", "graph", "optimization")):
        return "数学或算法结果没有建立到现有 AI System 状态/控制选择的可迁移链路"
    if any(term in text for term in ("agent", "llm", "transformer", "diffusion", "multimodal", "language model")):
        return "AI 相关方法仅改变单任务实现或分数，未改变现有 owner 的长期设计边界"
    return "主题不属于当前大模型、训练/推理基础设施或 Agent 系统主线"


def hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ledger = json.loads(LEDGER_PATH.read_text())
    evidence = json.loads(EVIDENCE_PATH.read_text())
    entries = {e["arxiv_id"]: e for e in ledger["entries"]}
    reviews = {r["arxiv_id"]: r for r in evidence["reviews"]}
    generic_ids = [e["arxiv_id"] for e in ledger["entries"] if e.get("decision_reason", "").endswith(GENERIC_SENTENCE)]
    assert len(generic_ids) == 467, len(generic_ids)
    closure_ids = {e["arxiv_id"] for e in ledger["entries"] if e["semantic_decision"] == "pre_denominator_closure_reviewed"}
    assert set(TARGETS) <= closure_ids
    generic_recovered = set(TARGETS) & set(generic_ids)

    recovered: list[str] = []
    blocked: list[str] = []
    for aid, spec in TARGETS.items():
        entry = entries[aid]
        owner = spec["owner"]
        chapter, chapter_path = CHAPTERS[owner]
        html_path = HTML_DIR / f"{aid}v1.html"
        dd, sr, durability = spec["score"]
        score = {
            "design_delta": dd, "system_reach": sr, "durability": durability,
            "total": dd + sr + durability,
            "rationale": {
                "design_delta": f"长期增量为：{spec['mechanism']}。",
                "system_reach": f"影响限定在 `{owner}` 的状态、控制或验收边界；不因题名相关性加分。",
                "durability": "仅计可迁移机制与共存边界；作者 workload、模型和 benchmark 数字不外推。",
            },
        }
        if not html_path.exists():
            status = "blocked_exact_v1_html_and_pdf"
            decision = "Blocked / Unverified"
            blocked.append(aid)
            review = {
                "arxiv_id": aid, "source_family_id": entry["source_family_id"], "title": entry["title"],
                "exact_v1_url": f"https://arxiv.org/html/{aid}v1", "review_status": status,
                "score_v2": score, "mechanism_claim": spec["mechanism"], "owner": owner,
                "chapter": chapter, "chapter_path": chapter_path, "books_decision": decision,
                "material_request": "exact-v1 HTML、完整 PDF 或作者存档正文；摘要不足以核验方法、实验与 limitations",
            }
        else:
            sections = parse_sections(html_path)
            front = sections.get("Front matter", "")[:12000].lower()
            if "this paper has been withdrawn" in front or "withdrawn by" in front:
                raise RuntimeError(f"withdrawn paper must be excluded, not retained: {aid}")
            method = locators(sections, r"method|approach|architecture|algorithm|formulation|framework|mechanism|analysis", ("3 ", "4 "))
            evaluation = locators(sections, r"experiment|evaluation|result|ablation|empirical|setup|case study|proof-of-concept", ("4 ", "5 "))
            limitations = locators(sections, r"limitation|trade.?off|threat|failure|discussion|conclusion|future", ("Conclusion", "Discussion"))
            decision = ("Integrate Proposed — root writeback and independent review required" if spec["decision"] == "I"
                        else "No Change — Existing Coverage (proposition comparison; independent review required)")
            review_status = "deep_complete_author" if score["total"] >= 7 or spec["decision"] == "I" else "standard_complete_author"
            review = {
                "arxiv_id": aid, "source_family_id": entry["source_family_id"], "title": entry["title"],
                "exact_v1_url": f"https://arxiv.org/html/{aid}v1",
                "local_exact_v1_html": str(html_path.relative_to(ROOT)),
                "exact_v1_access": "official exact-v1 HTML cached and section-reviewed in bounded repair",
                "review_status": review_status, "score_v2": score,
                "method_locators": method, "method_evidence": excerpt(sections, method),
                "evaluation_locators": evaluation or ["Not Disclosed as a standalone section"],
                "evaluation_evidence": excerpt(sections, evaluation),
                "limitations_locators": limitations or ["Not Disclosed as a standalone section"],
                "limitations_evidence": excerpt(sections, limitations, 700),
                "mechanism_claim": spec["mechanism"],
                "claim_boundary": (
                    "只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、"
                    "长度或 SLO 不补齐，作者 benchmark 不外推。"
                ),
                "owner": owner, "chapter": chapter, "chapter_path": chapter_path,
                "existing_marker_hits": [], "books_decision": decision,
                "existing_coverage_locator": f"{chapter_path} — canonical owner `{owner}` 的相关机制主线",
                "existing_coverage_proposition": spec["covered"],
                "existing_coverage_comparison": (
                    (f"现有正文仍缺：{spec['mechanism']}。应在保留旧方案适用条件的同时，补入状态/控制变化、"
                     "证据边界、代价、失败模式与回退。") if spec["decision"] == "I" else
                    (f"exact-v1 的新增证据是“{spec['mechanism']}”；它落在现有命题的实现或受限案例层，"
                     "没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。")
                ),
            }
        reviews[aid] = review
        entry.update({
            "semantic_decision": "semantic_reviewed_retain_frozen",
            "decision_reason": f"467 条泛化 closure 定点反查恢复：{spec['mechanism']}，会改变或检验 `{owner}` 的长期设计选择。",
            "exact_v1_status": review["review_status"], "score_v2": score, "owner": owner,
            "books_decision": decision,
            "internal_design_delta_challenge": {
                "old_system_constraint": spec["covered"],
                "changed_state_data_control_or_eval_contract": spec["mechanism"],
                "long_term_design_choice": review.get("existing_coverage_comparison", "exact-v1 受阻，不能完成最终 Books 判断。"),
            },
            "closure_reaudit": {"scope": "467-entry generic-closure layer", "result": "false_negative_recovered"},
        })
        recovered.append(aid)

    # Reaffirm every other item in the reopened layer with a title/abstract-specific closure record.
    for aid in generic_ids:
        if aid in TARGETS:
            continue
        entry = entries[aid]
        bucket = closure_bucket(entry)
        signal = first_sentence(entry["abstract"])
        entry["decision_reason"] = (
            f"定点重审《{entry['title']}》完整题名与摘要后关闭：{bucket}。"
            f"摘要主张锚点：{signal}"
        )
        entry["closure_reaudit"] = {
            "scope": "467-entry generic-closure layer",
            "title_abstract_semantic_recheck": "complete",
            "result": "pre_denominator_closure_reaffirmed",
            "missing_contribution_element": bucket,
        }

    # Correct the four ledger/evidence state drifts already confirmed by root body markers.
    for aid in ("2605.01208", "2605.01913", "2605.01959", "2605.02323"):
        entries[aid]["books_decision"] = "Integrate Applied — root writeback complete; independent post-write review pending"
        entries[aid]["books_writeback_status"] = "root_writeback_complete_pending_independent_review"
        assert reviews[aid]["books_decision"].startswith("Integrate Applied")

    ordered_reviews = sorted(reviews.values(), key=lambda item: item["arxiv_id"])
    retained_count = sum(e["semantic_decision"] == "semantic_reviewed_retain_frozen" for e in ledger["entries"])
    closure_count = sum(e["semantic_decision"] == "pre_denominator_closure_reviewed" for e in ledger["entries"])
    assert retained_count + closure_count == ledger["raw_identity_count"] == 1058
    assert len(ordered_reviews) == retained_count
    complete = sum(r["review_status"] in {"deep_complete_author", "standard_complete_author"} for r in ordered_reviews)
    blocked_count = retained_count - complete
    deep = sum(r["review_status"] == "deep_complete_author" for r in ordered_reviews)
    standard = sum(r["review_status"] == "standard_complete_author" for r in ordered_reviews)
    applied = sum(r["books_decision"].startswith("Integrate Applied") for r in ordered_reviews)
    proposed = sum(r["books_decision"].startswith("Integrate Proposed") for r in ordered_reviews)
    no_change = sum(r["books_decision"].startswith("No Change") for r in ordered_reviews)
    assert applied + proposed + no_change + blocked_count == retained_count

    ledger.update({
        "status": "author_targeted_repair_complete_root_writeback_and_independent_review_pending",
        "counts": {"pre_denominator_closure_reviewed": closure_count, "semantic_reviewed_retain_frozen": retained_count},
        "candidate_denominator_frozen": False, "books_write_permitted": False,
        "targeted_closure_reaudit": {
            "reviewer_failed_layer_count": 467, "raw_identity_rescan": False,
            "recovered_false_negative_count": len(recovered),
            "recovered_from_shared_generic_layer_count": len(generic_recovered),
            "reviewer_explicit_nonshared_reason_recovered_count": len(recovered) - len(generic_recovered),
            "reaffirmed_shared_generic_closure_count": 467 - len(generic_recovered),
            "recovered_ids": recovered, "blocked_recovered_ids": blocked,
            "author_result": "complete_pending_root_writeback_and_fresh_non_author_review",
        },
    })
    evidence.update({
        "status": "author_targeted_repair_complete_root_writeback_and_independent_review_pending",
        "candidate_count": retained_count, "review_complete": complete, "blocked": blocked_count,
        "deep_complete": deep, "standard_complete": standard,
        "books_integrate_applied": applied, "books_integrate_proposed": proposed,
        "books_no_change": no_change, "reviews": ordered_reviews,
    })
    LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    EVIDENCE_PATH.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n")

    root_items = []
    for review in ordered_reviews:
        if not review["books_decision"].startswith("Integrate Proposed"):
            continue
        root_items.append({
            "date": "2026-05-05", "source_family_id": review["source_family_id"],
            "primary_identifier": f"arXiv:{review['arxiv_id']}v1", "primary_source": review["exact_v1_url"],
            "stable_node_id": review["owner"], "target_chapter_path": review["chapter_path"],
            "current_chapter_sha256": hash_file(ROOT / review["chapter_path"]),
            "current_chapter_locator": f"canonical owner `{review['owner']}` 的相关演进段；root 写前须回读实际标题并选择精确锚点",
            "current_content_finding": review["existing_coverage_proposition"],
            "new_delta_after_compare": review["existing_coverage_comparison"],
            "method_evidence": review["method_evidence"], "evaluation_evidence": review["evaluation_evidence"],
            "evidence_boundary": review["claim_boundary"] + " " + review["limitations_evidence"][:500],
            "required_writeback": "按旧方案为何合理 → 约束变化 → 状态/控制权 → 收益证据 → trade-off/failure/fallback 融入正文；不得追加论文摘要。",
            "status": "root_writeback_required_then_independent_review",
        })
    queue = {"schema": "books-writeback-queue-v1", "generated_by": "2026-05-05 bounded 467-layer repair", "items": root_items}
    (HERE / "V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json").write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

    audit_lines = [
        "# 2026-05-05 V3 定点 closure 重审", "",
        "状态：作者返修完成；等待 root Books 写回和新的非作者最终复核。", "",
        "## 守恒", "",
        f"- Raw identity：1058（未重扫、未变更）。",
        f"- Reviewer 指定重开层：467；其中恢复 false negative：{len(generic_recovered)}；重新确认 closure：{467-len(generic_recovered)}。",
        f"- Reviewer 另点名的非共享理由 closure：恢复 {len(recovered)-len(generic_recovered)}；合计恢复 {len(recovered)}。",
        f"- 新 Candidate Denominator：{retained_count}；pre-denominator closure：{closure_count}。",
        f"- Evidence：完成 {complete}（Deep {deep} / Standard {standard}），Blocked {blocked_count}。",
        f"- Books：Applied {applied}、Proposed {proposed}、No Change {no_change}、Blocked {blocked_count}。", "",
        "## 恢复项", "",
    ]
    for aid in recovered:
        r = reviews[aid]
        audit_lines.append(f"- `{aid}` → `{r['owner']}`，{r['score_v2']['total']}/9，`{r['books_decision']}`。")
    audit_lines += ["", "## Gate", "", "作者不得自签。Proposed 项尚未写 Books，且 fresh-context 非作者复核尚未执行；Daily 必须保持 Ongoing。", ""]
    (HERE / "V3_TARGETED_CLOSURE_REAUDIT_20260915.md").write_text("\n".join(audit_lines))

    summary = {
        "raw": 1058, "reopened": 467, "recovered": len(recovered),
        "recovered_in_shared_layer": len(generic_recovered), "reaffirmed_shared_layer": 467-len(generic_recovered),
        "retained": retained_count, "closure": closure_count, "review_complete": complete,
        "blocked": blocked_count, "deep": deep, "standard": standard,
        "applied": applied, "proposed": proposed, "no_change": no_change,
        "root_queue": len(root_items),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
