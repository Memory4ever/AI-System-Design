#!/usr/bin/env python3
"""Apply the second bounded author repair for the 2026-05-07 V3 Daily.

This script does not edit Books.  It restores only exact-v1-reviewed false
negatives, records the Ch54 Source Family alias, rebuilds the active report,
and emits a root-owned Books writeback queue.  Final semantic acceptance must
still be performed by a non-author reviewer.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parents[1] / "07/README.md"
LEDGER = ROOT / "screening-ledger-v3-author-repair.json"
PACKET = ROOT / "exact-v1-review-packet-v3-author-repair.json"
COVERAGE = ROOT / "coverage-receipt.json"
COMPARISON = ROOT / "books-current-content-comparison.json"
QUEUE_JSON = ROOT / "V3_SECOND_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json"
QUEUE_MD = ROOT / "V3_SECOND_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.md"
CHECKPOINT = ROOT / "V3_SECOND_AUTHOR_REPAIR_20260915.md"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


RECOVERED = {
    "2605.04346": {
        "score": [3, 2, 2], "owner": "TRAIN-PRETRAINING",
        "chapter": "../../../../books/part-04-training-system/28-pretraining.md",
        "claim": "全局反向传播和保存全网 activation 不是唯一训练契约；block-local goodness 可通过协方差统计、边界对齐和可配置梯度 horizon，在内存、跨层协同与准确率之间形成连续取舍。",
        "method": ["§3.1–§3.6", "每个 block 用局部交叉熵且在边界 detach；BiCovG 以跨通道投影和多尺度聚合保留二阶信息，FAL 在隔离块边界做零初始化校正，HGB 用 block size m 控制梯度传播 horizon。"],
        "evaluation": ["§4.1–§4.4；Appendix A–D", "CIFAR-100、Tiny-ImageNet、ImageNet-100 上以 VGG-16 比较严格 layer-local、不同 HGB block size 与 BP；m=4 在作者设置中把峰值显存降低约一半，同时保留更接近 BP 的准确率，并分别消融 covariance、FAL 与 fusion。"],
        "limitations": ["§4.4–§5；实验范围", "证据限 CNN/VGG、监督分类与作者硬件；局部目标依赖标签、readout 和特征统计，未证明可扩展到 Transformer/LLM 预训练、跨设备通信或与 BP 等价。"],
        "decision": "整合",
        "comparison": "Ch28 已解释 BP activation memory 与 checkpoint/recompute，但缺少改变梯度 ownership 的 block-local 训练分支；应补入从全局 BP 到可配置 gradient horizon 的演进，并保留端到端 BP fallback。",
        "writeback": "在 Ch28 activation-memory/optimization 主线中加入受限分支：全局 BP → block-local objective → 可配置 gradient horizon；明确 block boundary、局部 readout/FAL、内存收益、跨层协同损失和 LLM 外推边界。",
    },
    "2605.04413": {
        "score": [3, 2, 3], "owner": "MULTIMODAL-WORLD-MODELS",
        "chapter": "../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md",
        "claim": "非单调具身动力学的 counterfactual identifiability 不要求全局 monotonicity；triangular recursion 下还需 mechanism-wise invertibility 与 context-independent inverse transport，局部可逆本身不足。",
        "method": ["§3；Theorems 1–3；§4", "证明 context-independent inverse transport 等价于 exogenous isomorphism 并导出完整反事实可识别性，同时给出 context-dependent transport 的反例；CausalInverter 用三角可逆层、orientation gate 与 transport-stability regularization 实例化。"],
        "evaluation": ["§5；Appendix C–E", "108 个合成配置、160 个 bridge runs，以及 MuJoCo Door/Push 的 state-based counterfactual 评价；Door 的强非单调区间支持结构偏置，Push 则显示在非单调性较弱时灵活 baseline 仍可更合适。"],
        "limitations": ["Appendix F；§5.4", "只覆盖共享顺序 triangular SCM、mechanism-wise invertibility、低轨迹 state-based 环境；不处理 cyclic SCM、图像 world model、深 latent causal discovery，也不证明真实机器人因果变量完备。"],
        "decision": "整合",
        "comparison": "Ch25 已区分 predictive continuation 与 unrestricted counterfactual contract，也提醒 structured factorization 不等于 causal identification；尚缺非单调 triangular 机制下的充分条件与“局部可逆仍不足”反例。",
        "writeback": "在 Ch25 counterfactual contract 段加入 non-monotone triangular 分支：global monotonicity → mechanism-wise invertibility + context-independent inverse transport；保留 Push 边界、cyclic/latent/vision 未覆盖和 simulator fallback。",
    },
    "2605.04525": {
        "score": [3, 2, 2], "owner": "MULTIMODAL-EMBODIED-VLA",
        "chapter": "../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "claim": "长时域具身规划可把探索性强但迭代慢的 diffusion 放在高层 sparse subgoal，把快速 rectified flow 放在低层 dense trajectory，并由在线 MPC 持续重规划。",
        "method": ["§4.1–§4.4", "先训练 RSSM latent world model，并用 progress contrastive 与 inverse dynamics 形成任务状态；高层 diffusion 生成稀疏 subgoal，经 EBM guidance 与 local manifold projection 修正，低层 rectified flow 生成短轨迹，MPC 重规划后由 inverse dynamics 输出控制。"],
        "evaluation": ["§5；Appendix D–F", "FurnitureBench 仿真与四个真实装配任务、RLBench 18 tasks、OGBench 比较 diffusion/flow 的高低层组合；消融 world model、EBM guidance、projection 和两层生成器，真实任务每项 10 次评价且训练示范有限。"],
        "limitations": ["§6；Appendix F", "依赖带成功/失败标记的 demonstration、RSSM 表示与 inverse dynamics；真实样本和 trial 数有限，未证明开放世界安全、任意 embodiment 迁移或 end-to-end latency SLO。"],
        "decision": "整合",
        "comparison": "Ch26 已有多时间尺度 controller 与 diffusion/flow action head，但尚未把两种生成范式按高层探索/低层实时性分权，也未写清 manifold projection、MPC replan 与 inverse-dynamics handoff。",
        "writeback": "在 Ch26 hierarchical controller 主线中加入 high-level diffusion subgoal → projected latent target → low-level rectified-flow trajectory → MPC/inverse-dynamics handoff；保留数据、表示、延迟和安全 fallback。",
    },
    "2605.04647": {
        "score": [3, 2, 2], "owner": "MULTIMODAL-EMBODIED-VLA",
        "chapter": "../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "claim": "具身 action token 可以先并行 draft、再原位 edit，但 revision 必须和 full-rollout RL credit、mutable action cache invalidation 及最终 controller commit 同时设计。",
        "method": ["§4.1–§4.4；§5", "goal-point posterior 提供行为级候选，masked discrete diffusion 起草 trajectory token，AutoEdit 在同一 token space 直接替换选中位置；完整 draft-and-edit rollout 接收终局 RL reward，并复用 shared-prefix KV、回卷 action cache 后重算 mutable block。"],
        "evaluation": ["§6；Appendix C–F", "NAVSIM 上用 0.7B backbone、0.1B ViT、4 秒/2Hz trajectory 和 SFT→RFT；标准 PDMS、AutoEdit/RL 消融及 NVIDIA Thor 路径支持所披露 operating point。best-of-6 的 94.8 是 oracle，不属于标准在线结果。"],
        "limitations": ["§7", "固定分辨率 BEV token 限制精度，RL reward 是 proxy，未在更高保真 simulator 验证；编辑扰动集中纵向/横向误差，31.8ms 平均延迟不证明尾延迟或安全闭环。"],
        "decision": "整合",
        "comparison": "Ch26 已讨论 action chunk、fast/slow controller 与 warm-start/refinement，但缺少同一离散 action space 的 draft/edit authority、full-rollout credit 以及编辑后 cache rewind/recompute 的一致性边界。",
        "writeback": "在 Ch26 action-token/correction 段加入 draft → selective rewrite → invalidate/recompute mutable action state → reverify/commit；说明 RL credit 必须覆盖完整 rollout，并限定 NAVSIM/Thor/oracle 证据。",
    },
    "2605.04980": {
        "score": [2, 1, 2], "owner": "MODEL-SAMPLING",
        "chapter": "../../../../books/part-02-model/20-sampling.md",
        "claim": "inference-time semantic steering 不必把概念压成单一方向；由 bipolar activations 估计的 soft projection subspace 可保留多维结构，并通过 Boolean composition 形成更丰富但仍需校准的控制 artifact。",
        "method": ["§3–§5", "从正/负概念对的 pooled hidden activations 构造 conceptor soft projection matrix；quota 用作无参数 layer-selection sensor，replacement/interpolation 改写 hidden state，AND/OR/NOT 在子空间几何上组合。"],
        "evaluation": ["§4–§6；Appendix C–F", "Gemma-2-2B/9B、Qwen2.5-3B，三个英文语义维度、五轴设计空间、500 prompts 与两组 Boolean 任务；quota 与 probe separability 在多数设置相关，interpolation 的退化输出少于更激进 replacement/additive 路径。"],
        "limitations": ["§7", "只测三种较小 instruction model、三个英文概念、单层 intervention、有限 contrastive pairs 与自动 classifier；Boolean composition 依赖子空间 overlap，不证明行为正确或生产安全。"],
        "decision": "整合",
        "comparison": "Ch20 已把 hidden-state control vector 绑定 checkpoint、layer、window 与阈值，但默认仍是单方向 artifact；缺少多维 soft-projection、layer quota sensor 和组合操作的替代分支。",
        "writeback": "在 Ch20 trajectory feedback/hidden-state control 后加入 vector → subspace projection 的替代分支；把 quota 限定为 layer sensor，区分 interpolation/replacement 强度、degenerate-output 风险与外部 verifier。",
    },
    "2605.05017": {
        "score": [2, 2, 2], "owner": "PLATFORM-SECURITY",
        "chapter": "../../../../books/part-06-ai-infrastructure/72-security.md",
        "claim": "Embodied privacy 不是 perception 阶段的单点遮蔽，而是从 instruction、sensing、planning 到 interaction 的 lifecycle control signal；privacy level 改变会沿闭环传播为 utility 与可达 action 的变化。",
        "method": ["§3；§4.1", "SPINE 以 stage/function/control/budget 的 tuple 表达隐私标签，在 instruction→perception→planning→interaction 之间传播 policy；导航案例用区域敏感度触发 pixelation、camera depression、edge/cloud placement 或禁止进入。"],
        "evaluation": ["§4.2–§4.3", "Habitat/R2R-CE 的 pixelation sensitivity 与小型 AGV 路径演示只作为受控 probe：SR/SPL 和路线会随遮蔽/区域 policy 改变；作者明确 pixelation K 不是实际 privacy measure。"],
        "limitations": ["§5；§7–§8", "position paper 与概念性案例不提供统一 threat model、形式保证或生产评测；state-based/视觉导航不能覆盖 latent、gradient、memory、旁观者与多机器人泄漏，很多机制仍是 future work。"],
        "decision": "已有覆盖",
        "comparison": "Ch72 已把 privacy 从静态存储扩展到端到端 observable data flow，并按 embodied supply/perception/world-state/planning/action 等 trust boundary 分责；SPINE 提供生命周期实例，但不改变现有 owner、threat-model 或 fail-closed contract。",
    },
    "2605.04470": {
        "score": [3, 2, 2], "owner": "MULTIMODAL-EMBODIED-VLA",
        "chapter": "../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "claim": "具身策略 post-training 可把 dense 但有偏的 counterfactual supervision 当 proxy，再用稀疏但 grounded 的真实 closed-loop event 学 residual correction；两者必须在同一 on-policy visited-state distribution 下对齐。",
        "method": ["§3.1–§3.5", "CRAFT 将真实 closed-loop policy gradient 分解为 proxy 与 residual：group-normalized counterfactual advantages 提供密集信号，interaction-critical rollouts 校正 proxy bias，EMA teacher 的 asymmetric KL 和 dual clipping 约束更新。"],
        "evaluation": ["§4；Appendix B–E", "Bench2Drive 的 hierarchical planning、VLA 与 vocabulary-scoring policies 上比较 closed-loop RL、counterfactual tuning 与组合；component ablation、scaling/stability 和 transfer 支持所测 simulator。作者修改了若干 protocol 细节，主结果不是未经变化的官方 harness。"],
        "limitations": ["§5；Appendix B", "counterfactual proxy 仍依赖 future evaluator，grounded residual 受稀有事件和 simulator realism 限制；EMA 自蒸馏可能保留错误，单一 driving suite 不证明真实道路安全或通用 VLA post-training。"],
        "decision": "整合",
        "comparison": "Ch26 已区分 learned proposal、closed-loop observation 与 safety commit，但缺少 dense biased proxy 与 sparse grounded residual 的同分布组合，以及保留 pretrained behavior 的 teacher boundary。",
        "writeback": "在 Ch26 online post-training 分支加入 counterfactual proxy → grounded residual correction → EMA constraint；强调同一 visited-state distribution、harness revision、proxy bias/rare-event variance 和真实环境 fallback。",
    },
    "2605.05118": {
        "score": [2, 1, 2], "owner": "MULTIMODAL-GENERATIVE-PARADIGMS",
        "chapter": "../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
        "claim": "生成式 drifting 的理论标签必须区分 proposed KL/Wasserstein fixed-point construction 与实际实现的 Sinkhorn-like proxy；后者一般不是任何 distributional loss 的 Wasserstein gradient，也不继承相同收敛性质。",
        "method": ["§2.3；§3；Appendix B–D", "把简化 GMD 写成 Parzen-smoothed KL 的 WGF fixed point，再分析实际 cross-weighted implementation：它的零速度条件可识别 p=q，但一般不存在对应的 WGF functional，并给出 distant non-overlapping modes 的 failure construction。"],
        "evaluation": ["§3.3；§4.3；Appendix D/F", "二维 toy distributions 比较 Sinkhorn proxy、KL/W2 flow，并展示 non-overlapping support 下的 failure；主要证据是命题与反例，不是图像/文本质量、吞吐或生产 benchmark。"],
        "limitations": ["§3.2–§4；Appendix assumptions", "分析依赖 kernel/Parzen 和连续分布假设，未证明 finite neural parameterization、训练稳定性或部署收益；它修正机制解释，不单独建立 GMD 为长期默认生成范式。"],
        "decision": "仅报告",
        "comparison": "Ch24 未采用 GMD/Drifting 作为正文机制；该 note 纠正 emerging family 的理论解释，但在原 family 形成可复用系统路线前，不为一篇 correction 新建孤立正文。",
    },
    "2605.05172": {
        "score": [3, 2, 2], "owner": "MULTIMODAL-EMBODIED-VLA",
        "chapter": "../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "claim": "BC→online RL 不应让新 critic 立即覆盖已有可靠动作；可先从 BC action likelihood/entropy 与少量 rollout 估计冻结价值基线，再由双 Q gate 在 BC 保留与 RL 探索之间逐状态选择。",
        "method": ["§3.1–§3.3；Appendix A", "Q-Estimation 从 BC policy 的 action likelihood、entropy 与少量交互拟合 Q_BC；在线阶段保留冻结 Q_BC，并训练 Q_RL，gate 比较两者对 BC/RL action proposal 的值来收集数据和更新策略。"],
        "evaluation": ["§4；Appendix B–D", "D4RL/robomimic 用 20 rollouts、5 seeds，另有 Franka Panda 真实 pipe assembly、peg insertion 与 kitting；Q-initialization/Q-gating、replay seeding、BC auxiliary loss 和 rollout 数量均做消融。真实结论限 1–2.5h、单 A6000 与所测机器人。"],
        "limitations": ["§5；Appendix C", "需要 BC policy 暴露 action likelihood 与 entropy；soft-optimality、Q estimation 和 critic calibration 可能失准，尚不支持 diffusion/flow policy，Q gate 也不替代 physical safety envelope。"],
        "decision": "整合",
        "comparison": "Ch26 已有 compact RL head 与 human/safety handoff，但缺少 offline BC 可靠动作的独立价值 owner，以及在在线分布偏移下让 BC 与 RL proposal 竞争而非直接覆盖的分支。",
        "writeback": "在 Ch26 online RL 段加入 BC baseline Q state + learnable RL Q state + per-state gate；明确冻结/更新 owner、估计误差、支持的 policy class、robot wear 风险与 safety fallback。",
    },
}


TARGETED_CLOSURES = {
    "2605.04054": "理论 learning dynamics 未给出模型训练接口或可迁移的 state/control owner，保持关闭。",
    "2605.04128": "统一多模态 model report 的增量主要是配方与能力结果；题摘未形成超出现有 Ch23–24 的长期机制，保持关闭。",
    "2605.04590": "rectified-flow segmentation 仍是单任务 output-space 替换，不改变通用生成/具身 contract，保持关闭。",
    "2605.04759": "Neuro-symbolic LM 的摘要主张缺少足以支持新 owner/contract 的可验证机制边界，保持关闭。",
    "2605.04899": "embedding curvature 与棋盘内部状态只形成解释性观察，没有可识别的设计/evaluation contract 变化，保持关闭。",
    "2605.05092": "驾驶舱双流 world model 仍是局部 architecture；此前撤销的通用 world-state 外推不恢复。",
    "2605.05123": "interaction-budget continuous-control policy selection 不提供 LLM/VLA 特有的模型或平台 contract，保持关闭。",
    "2605.05163": "physics-grounded 3D asset generation 是有价值的数据/内容管线，但题摘未赋予环境 transition、policy 或 simulator truth authority；保持关闭。",
}


ledger = json.loads(LEDGER.read_text())
by_id = {x["arxiv_id"]: x for x in ledger["identities"]}
packet = json.loads(PACKET.read_text())
packet_by_id = {x["arxiv_id"]: x for x in packet["items"]}

# The existing Ch54 prose has a title-derived canonical marker.  Preserve that
# canonical ID and explicitly map the active arXiv identity as an alias.
old_marker = "SF-WHEN-KV-MEETS-EMBEDDINGS-DYNAMIC-GPU-MEMORY-ALLOCATION-FOR-ACCELERATING-"
for obj in (by_id["2605.04450"], packet_by_id["2605.04450"]):
    obj["source_family_id"] = old_marker
    obj["source_family_aliases"] = ["SF-2026-ARXIV-2605-04450", "arxiv:2605.04450v1"]
    obj["books_marker_alias"] = old_marker

for arxiv_id, spec in RECOVERED.items():
    source = by_id[arxiv_id]
    source.update({
        "screening_status": "retained",
        "screening_reason": spec["claim"],
        "review_status": "source_review_complete",
        "access_status": "exact_v1_reviewed",
        "integration_disposition": spec["decision"],
        "owner_node": spec["owner"],
        "owner_chapter": spec["chapter"],
        "score_v2": dict(zip(("design_delta", "system_reach", "durability"), spec["score"])) | {"total": sum(spec["score"])},
        "review_ref": f"exact-v1-review-packet-v3-author-repair.json#{arxiv_id}",
        "second_author_repair_scope": "restored after exact-v1 review of the shared false-negative closure stratum",
        "second_bounded_stratum_audit": "recovered_to_candidate",
    })
    if spec["decision"] == "整合":
        source["books_writeback_status"] = "root_writeback_required_before_final_gate"
    else:
        source.pop("books_writeback_status", None)
    packet_by_id[arxiv_id] = {
        "arxiv_id": arxiv_id,
        "source_family_id": source["source_family_id"],
        "title": source["title"],
        "primary_evidence_version": f"arXiv:{arxiv_id}v1",
        "exact_v1_url": f"https://arxiv.org/html/{arxiv_id}v1",
        "owner_evidence_status": source["owner_evidence_status"],
        "first_public_time_derived": source["first_public_time_derived"],
        "owner_evidence": source["owner_evidence"],
        "method": {"locator": spec["method"][0], "evidence": spec["method"][1]},
        "evaluation": {"locator": spec["evaluation"][0], "evidence": spec["evaluation"][1]},
        "limitations": {"locator": spec["limitations"][0], "evidence": spec["limitations"][1]},
        "claim_boundary": spec["claim"],
        "review_result": "source_review_complete",
        "books_disposition": spec["decision"],
        "owner_node": spec["owner"],
        "score_v2": source["score_v2"],
        "books_comparison": spec["comparison"],
        "review_gap": (f"整合（待 root 写回）：{spec['comparison']}" if spec["decision"] == "整合" else f"{spec['decision']}：{spec['comparison']}"),
    }
    if spec["decision"] == "整合":
        packet_by_id[arxiv_id]["books_writeback_status"] = "root_writeback_required_before_final_gate"

for arxiv_id, reason in TARGETED_CLOSURES.items():
    row = by_id[arxiv_id]
    row["second_bounded_stratum_audit"] = "title_and_abstract_rechecked; closure_confirmed"
    row["second_bounded_stratum_decision"] = reason

# Earlier author packets kept V3 scores only in the screening ledger.  The
# rebuilt report consumes the evidence packet directly, so normalize the
# already-reviewed items from that authoritative per-candidate ledger instead
# of inventing or recomputing historical scores here.
for arxiv_id, item in packet_by_id.items():
    item.setdefault("score_v2", by_id[arxiv_id]["score_v2"])

candidate = [x for x in ledger["identities"] if x.get("screening_status") == "retained"]
closed = [x for x in ledger["identities"] if x.get("screening_status") == "pre_denominator_closure"]
withdrawn = [x for x in ledger["identities"] if x.get("screening_status") == "withdrawn_excluded"]
counts = Counter(x["books_disposition"] for x in packet_by_id.values())
complete = sum(x.get("review_result") == "source_review_complete" for x in packet_by_id.values())
disputed = counts["争议"]

ledger.update({
    "candidate_denominator_provisional": len(candidate),
    "denominator_after_exact_v1_scope_recheck": len(candidate),
    "pre_denominator_closures": len(closed),
    "withdrawn_excluded": len(withdrawn),
    "source_review_complete": complete,
    "source_review_disputed": disputed,
    "source_review_pending": 0,
    "books_disposition_summary": {"整合": counts["整合"], "已有覆盖": counts["已有覆盖"], "仅报告": counts["仅报告"], "争议": counts["争议"]},
    "status": "Second author repair complete; root Books writeback and a new non-author semantic review remain pending",
    "second_final_author_repair": {
        "explicit_false_negatives_recovered": ["2605.04346", "2605.04413", "2605.04525", "2605.04647", "2605.04980", "2605.05017"],
        "additional_same_stratum_false_negatives": ["2605.04470", "2605.05118", "2605.05172"],
        "targeted_closures_confirmed": list(TARGETED_CLOSURES),
        "ch54_canonical_family": old_marker,
        "ch54_aliases": ["SF-2026-ARXIV-2605-04450", "arxiv:2605.04450v1"],
        "root_books_writeback_required": sorted(a for a, s in RECOVERED.items() if s["decision"] == "整合"),
        "non_author_review_required": True,
    },
})
write_json(LEDGER, ledger)

packet.update({
    "items": [packet_by_id[k] for k in sorted(packet_by_id)],
    "source_review_complete": complete,
    "disputed": disputed,
    "pending": 0,
    "books_disposition_summary": ledger["books_disposition_summary"],
    "status": "All author-side reviews complete; root Books writeback and a new non-author semantic review remain pending",
    "second_final_author_repair": ledger["second_final_author_repair"],
})
write_json(PACKET, packet)

coverage = json.loads(COVERAGE.read_text())
coverage.update({
    "registered_identities": len(ledger["identities"]),
    "semantic_screened_nonwithdrawn": len(ledger["identities"]) - len(withdrawn),
    "retained": len(candidate),
    "pre_denominator_closed": len(closed),
    "withdrawn_excluded": len(withdrawn),
    "ledger_sha256": hashlib.sha256(LEDGER.read_bytes()).hexdigest(),
    "status": "checked; second bounded false-negative repair complete; final semantic gate remains open",
})
write_json(COVERAGE, coverage)

comparison = json.loads(COMPARISON.read_text())
cmp_by_id = {x.get("arxiv_id"): x for x in comparison["items"]}
for arxiv_id, spec in RECOVERED.items():
    cmp_by_id[arxiv_id] = {
        "source_family_id": by_id[arxiv_id]["source_family_id"],
        "arxiv_id": arxiv_id,
        "owner_node": spec["owner"],
        "owner_path": spec["chapter"].replace("../../../../", ""),
        "adjacent_context_reviewed": True,
        "current_content_comparison": spec["comparison"],
        "disposition": spec["decision"],
        "delta": spec.get("writeback", "No Books change; existing proposition-level coverage is sufficient."),
    }
comparison["items"] = [cmp_by_id[k] for k in sorted(cmp_by_id)]
write_json(COMPARISON, comparison)

queue = []
for arxiv_id, spec in sorted(RECOVERED.items()):
    if spec["decision"] != "整合":
        continue
    queue.append({
        "arxiv_id": arxiv_id,
        "source_family_id": by_id[arxiv_id]["source_family_id"],
        "title": by_id[arxiv_id]["title"],
        "owner_node": spec["owner"],
        "target_path": spec["chapter"].replace("../../../../", ""),
        "exact_v1_url": f"https://arxiv.org/html/{arxiv_id}v1",
        "semantic_delta": spec["writeback"],
        "evidence_boundary": spec["limitations"][1],
        "required_status_after_writeback": "applied_in_books_pending_non_author_gate",
    })
write_json(QUEUE_JSON, {"schema": "v3-second-root-books-writeback-queue", "status": "pending_root_writeback", "items": queue})
QUEUE_MD.write_text("\n".join([
    "# 2026-05-07 第二轮 Root Books 写回队列", "",
    "作者侧只形成命题级队列，没有编辑 Books。root 应按目标章节顺序合并同章增量，避免论文列表式追加；全部写回后仍需新的独立语义终审。", "",
] + [f"## {x['arxiv_id']} — {x['title']}\n\n- Owner：`{x['owner_node']}`\n- Target：`{x['target_path']}`\n- Primary：{x['exact_v1_url']}\n- Semantic delta：{x['semantic_delta']}\n- Evidence boundary：{x['evidence_boundary']}" for x in queue]) + "\n")


def table_row(arxiv_id: str) -> str:
    item = packet_by_id[arxiv_id]
    source = by_id[arxiv_id]
    s = item["score_v2"]
    review = "争议" if item["books_disposition"] == "争议" else ("深入完成" if item["books_disposition"] == "整合" or s["total"] >= 7 else "标准完成")
    books = item["review_gap"]
    if item["books_disposition"] == "整合":
        books = re.sub(r"^整合（待 root 写回）：", "整合：待 root 写回；", books)
        books = re.sub(r"^整合（已落实）：", "整合：已落实；", books)
    elif item["books_disposition"] == "争议":
        books = re.sub(r"^争议：", "暂缓：Disputed；", books)
    if item["books_disposition"] in {"整合", "已有覆盖"}:
        books += f"（`{item['owner_node']}`，[章节]({source['owner_chapter']})）"
    def cell(v: str) -> str:
        return v.replace("|", r"\|").replace("\n", " ")
    return (f"| [{cell(item['title'])}](https://arxiv.org/html/{arxiv_id}v1) | {item['first_public_time_derived']} | "
            f"{cell(item['claim_boundary'])}；**{s['design_delta']} + {s['system_reach']} + {s['durability']} = {s['total']}** | "
            f"{review} | {cell(books)} |")


def evidence_block(arxiv_id: str) -> str:
    item = packet_by_id[arxiv_id]
    return "\n".join([
        f"### [{item['title']}](https://arxiv.org/html/{arxiv_id}v1)", "",
        f"- **Method**（{item['method']['locator']}）：{item['method']['evidence']}",
        f"- **Key evaluation**（{item['evaluation']['locator']}）：{item['evaluation']['evidence']}",
        f"- **Direct limitation**（{item['limitations']['locator']}）：{item['limitations']['evidence']}",
        f"- **采用边界**：{item['claim_boundary']}",
        f"- **审阅/Books**：exact-v1 Source Review 完成；{item['review_gap']}",
    ])


text = REPORT.read_text()
table_start = text.index("| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |")
table_end = text.index("\n\n## 4. 证据与知识整合", table_start)
header = "\n".join(text[table_start:table_end].splitlines()[:2])
text = text[:table_start] + header + "\n" + "\n".join(table_row(x["arxiv_id"]) for x in packet["items"]) + text[table_end:]
evidence_start = text.index("## 4. 证据与知识整合")
evidence_body = text.index("\n", evidence_start) + 1
section5 = text.index("\n## 5. 缺口与下一步", evidence_body)
text = text[:evidence_body] + "\n\n" + "\n\n".join(evidence_block(k) for k in sorted(packet_by_id)) + "\n" + text[section5:]

text = re.sub(r"\*\*检查时间：\*\* .*", "**检查时间：** 2026-09-15T15:30:00+08:00", text, count=1)
text = re.sub(
    r"## 1\. 结论.*?\n## 2\. 来源覆盖",
    f"""## 1. 结论

第二次终审的 6 个明确 false negative 已全部恢复并完成 exact-v1 审阅；围绕同一错误关闭理由又定点复核 11 项，额外恢复 2605.04470、2605.05118 与 2605.05172，另外 8 项保留具体关闭理由。当前 active 账面为 **548 = {len(candidate)} 候选 + {len(closed)} 关闭 + {len(withdrawn)} 撤回排除**；候选 Evidence 为 **{complete} 完成、{disputed} 争议、0 待审**，Books 处置为 **{counts['整合']} 整合、{counts['已有覆盖']} 已有覆盖、{counts['仅报告']} 仅报告、{counts['争议']} 争议**。

`2605.04450` 已以 Ch54 现存旧标题 marker `{old_marker}` 作为 canonical family，并在 active ledger/packet 明确登记 `SF-2026-ARXIV-2605-04450` 与 `arxiv:2605.04450v1` alias；没有重复正文。本轮新增 {len(queue)} 项 Books 语义增量只进入[root 写回队列](../_sources/daily-20260507/V3_SECOND_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.md)，作者未编辑 Books。root 写回和新的非作者 fresh-context 终审完成前，日报保持进行中。

arXiv ID/version、DataCite initial-created 与官方 Wednesday 20:00 EDT 共同支持 public-batch-derived **05-07 08:00**；这是批次推导，不是单篇页面直接披露。548 项 route 中 400 为 direct OAI corroboration、148 为 revision reconciliation，后者只有 72 项保存了 later OAI 日期，不能虚构其余均被 revision 覆盖。日期方法见[共享依据](../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md)。撤回 2605.04356 在 active ledger 只留最小排除。

## 2. 来源覆盖""",
    text, count=1, flags=re.S,
)
text = text.replace("151候选；396 项有具体或分层关闭记录", f"{len(candidate)}候选；{len(closed)} 项有具体或分层关闭记录")
text = re.sub(
    r"## 5\. 缺口与下一步.*?## 6\. 复核",
    f"""## 5. 缺口与下一步

作者侧 Evidence 已闭合：**{complete} 完成、{disputed} 争议、0 待审、0 retained-candidate access blocker**。Books disposition 已逐项闭合为 **{counts['整合']} 整合、{counts['已有覆盖']} 已有覆盖、{counts['仅报告']} 仅报告、{counts['争议']} 争议**；其中历史 {counts['整合'] - len(queue)} 项已落实，新增 {len(queue)} 项等待 root 依据命题级队列写回。

当前没有需要用户补充的 primary material。NLA 与 2605.06548 继续作为跨日隔离终态；四项争议保留精确重开条件。作者侧唯一剩余动作不是继续扩池，而是把新增 Books 队列交 root 合并写回，并由未参与本轮修复的 reviewer 重新检查分母、证据边界、alias 与实际正文。

## 6. 复核""",
    text, count=1, flags=re.S,
)
text = re.sub(
    r"### 作者侧交接（2026-09-14）.*\Z",
    f"""### 第二次作者修复交接（2026-09-15）

分母守恒：**548 = {len(candidate)} retained + {len(closed)} pre-denominator closure + {len(withdrawn)} withdrawn**。Evidence：**{complete} complete + {disputed} disputed + 0 pending**。Books：**{counts['整合']} Integrate + {counts['已有覆盖']} No Change + {counts['仅报告']} Daily Only + {counts['争议']} Disputed**。

指定 6 项与同簇新增 3 项均已完成 exact-v1 Method/Evaluation/limitations、V3 score、唯一 owner 和 Books disposition。Ch54 alias 已贯通，不重复正文。新增 {len(queue)} 项 Integrate 尚未写 Books，见 root queue；因此日报保持进行中。下一步只能由 root 完成写回，再由新的非作者 reviewer 验收；未 stage、commit、push。
""",
    text, count=1, flags=re.S,
)
# Preserve the audit trail without leaving an obsolete intermediate count that
# reads like the active denominator.  The 137/148/151 figures are historical;
# only the second-repair checkpoint below is current.
text = re.sub(
    r"原独立审计的基线为 137 项候选.*?仍须新的非作者 reviewer 验收当前 148 项状态。",
    "原独立审计的 137 项，以及后续 148、151 项，均为已经被本轮修复取代的历史 checkpoint，不再作为当前计数。root 此前写回的 56 项保持不变；本轮新增 7 项只进入写回队列，尚未改动 Books。",
    text,
    count=1,
)
text = re.sub(
    r"本轮运行格式、JSON 唯一性、评分、链接与范围内 diff-check；通过只证明可判定一致性。root 已写回当前账面的全部 56 项 Integrate，但第二次独立语义复核发现新的可执行漏项与 Source Family trace 问题，状态继续保持进行中。未 stage、commit、push。",
    "本轮重新检查格式、JSON 唯一性、评分、alias、链接与范围内 diff；通过只证明可判定一致性。第二次独立语义复核发现的漏项与 Source Family trace 问题已由作者修复，但新增 7 项 Books 写回及新的非作者验收仍未完成，状态继续保持进行中。未 stage、commit、push。",
    text,
    count=1,
)
REPORT.write_text(text)

CHECKPOINT.write_text(f"""# 2026-05-07 V3 第二次作者修复 checkpoint

**状态：** 作者侧修复完成；日报保持进行中

## 本轮结果

- 分母：`548 = {len(candidate)} retained + {len(closed)} closure + {len(withdrawn)} withdrawn`。
- Evidence：`{complete} complete + {disputed} disputed + 0 pending`。
- Books disposition：`{counts['整合']} Integrate + {counts['已有覆盖']} No Change + {counts['仅报告']} Daily Only + {counts['争议']} Disputed`。
- 指定恢复：{', '.join(ledger['second_final_author_repair']['explicit_false_negatives_recovered'])}。
- 同簇新增恢复：{', '.join(ledger['second_final_author_repair']['additional_same_stratum_false_negatives'])}。
- Ch54 canonical：`{old_marker}`；aliases：`SF-2026-ARXIV-2605-04450`、`arxiv:2605.04450v1`。
- root Books queue：{len(queue)} 项，见 `{QUEUE_MD.name}`。

## 仍未闭合

作者没有编辑 Books，也不能自签 fresh-context Gate。root 必须先合并写回队列，再由未参与本轮修复的 reviewer 核验 active ledger、packet、README、alias、实际正文与关闭抽样。此 checkpoint 不是 Complete 声明。
""")
