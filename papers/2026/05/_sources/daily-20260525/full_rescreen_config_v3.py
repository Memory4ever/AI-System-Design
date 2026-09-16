"""Manual semantic decisions for the 2026-05-25 full closure rescreen.

The sets below are the output of reading every remaining arXiv title and full
abstract.  They are intentionally explicit: no keyword classifier decides
admission, ownership, or Books disposition.  Exact-v1 heading locators are
stored separately in ``full-rescreen-source-heading-index-v3.json``.
"""

from __future__ import annotations

OWNER_GROUPS = {
    "WORLDVIEW-REPRESENTATION": """
        2605.22940 2605.22972 2605.23028 2605.23032 2605.23033 2605.23035
        2605.23039 2605.23087 2605.23156 2605.23393 2605.23395 2605.23410
        2605.23446 2605.23449 2605.23726 2605.23819 2605.23821
    """.split(),
    "MODEL-SELF-ATTENTION": """
        2605.23036 2605.23445 2605.23467 2605.23655 2605.23673 2605.23868
    """.split(),
    "MODEL-DECODER-ONLY": "2605.23024 2605.23702".split(),
    "MODEL-LONG-CONTEXT": "2605.22907".split(),
    "MULTIMODAL-REPRESENTATION": """
        2605.22902 2605.23045 2605.23254 2605.23288 2605.23373 2605.23602
        2605.23634
    """.split(),
    "MULTIMODAL-GENERATIVE-PARADIGMS": """
        2605.22950 2605.22996 2605.23070 2605.23113 2605.23163 2605.23178
        2605.23192 2605.23245 2605.23275 2605.23287 2605.23341 2605.23346
        2605.23451 2605.23508 2605.23672 2605.23861 2605.23878 2605.23888
        2605.23891
    """.split(),
    "MULTIMODAL-WORLD-MODELS": "2605.23089 2605.23345 2605.23699 2605.23845".split(),
    "MULTIMODAL-EMBODIED-VLA": """
        2605.22986 2605.23128 2605.23257 2605.23270 2605.23477 2605.23568
        2605.23717 2605.23733 2605.23762 2605.23847
    """.split(),
    "TRAIN-DATA": "2605.22871 2605.23198 2605.23268 2605.23482 2605.23883".split(),
    "TRAIN-PRETRAINING": "2605.23239 2605.23424 2605.23572 2605.23656".split(),
    "TRAIN-RLHF": "2605.23261 2605.23351 2605.23650".split(),
    "TRAIN-PPO": "2605.23146 2605.23365 2605.23372 2605.23551 2605.23565".split(),
    "TRAIN-GRPO": "2605.23500".split(),
    "TRAIN-DISTRIBUTED-TRAINING": "2605.22898".split(),
    "PLATFORM-GPU-SCHEDULER": "2605.22827".split(),
    "PLATFORM-PRODUCTION": "2605.23312 2605.23560 2605.23630 2605.23707 2605.23832".split(),
    "PLATFORM-SECURITY": """
        2605.23065 2605.23091 2605.23096 2605.23297 2605.23411 2605.23623 2605.23641
        2605.23695 2605.23859 2605.23879
    """.split(),
    "PLATFORM-EVALUATION-SYSTEM": """
        2605.22826 2605.22880 2605.22963 2605.22973 2605.22975 2605.22976
        2605.23017 2605.23069 2605.23108 2605.23116 2605.23141 2605.23176
        2605.23179 2605.23187 2605.23190 2605.23201 2605.23203 2605.23216
        2605.23231 2605.23238 2605.23243 2605.23249 2605.23271 2605.23330
        2605.23420 2605.23426 2605.23472 2605.23563 2605.23598 2605.23618
        2605.23629 2605.23635 2605.23651 2605.23684 2605.23694 2605.23744
        2605.23747 2605.23797 2605.23867 2605.23898
    """.split(),
    "AGENT-RAG": "2605.22829 2605.22878".split(),
    "AGENT-MEMORY": "2605.23043".split(),
    "AGENT-TOOL-CALLING": "2605.22874 2605.23281 2605.23643 2605.23897".split(),
    "AGENT-PLANNING": "2605.22875 2605.22897 2605.23771".split(),
    "AGENT-MULTI-AGENT": "2605.23562 2605.23652 2605.23809 2605.23887".split(),
}

# These mechanisms lack a unique current knowledge owner.  They remain
# candidates for a future structure decision; the daily author does not create
# a chapter or force-fit them into an adjacent owner.
STRUCTURAL = {"2605.22832", "2605.23796"}

# Useful evidence or conceptual framing, but not a stable positive mechanism to
# write into Books in this repair.
REPORT_ONLY = {"2605.23024", "2605.23179", "2605.23330"}

# HTML conversion was absent for three items, but the official exact-v1 PDF was
# accessible and reviewed; therefore no candidate remains access-blocked.
DEFERRED = set()

# Definite false negatives identified by the fresh final reviewer.  This set is
# also used to force deep review even where Books already has the proposition.
CONFIRMED_FALSE_NEGATIVES = {
    "2605.22829", "2605.22902", "2605.23033", "2605.23128", "2605.23163",
    "2605.23271", "2605.23393", "2605.23445", "2605.23482", "2605.23655",
    "2605.23699", "2605.23821", "2605.23868",
}

# Only these five exact-v1 propositions are not already carried by the current
# owner body.  They form the serialized root queue; this file never writes Books.
INTEGRATIONS = {
    "2605.23128": {
        "anchor": "after `### VLA policy`; before `### Action-facing Representation 也是 Gradient Authority Boundary`",
        "delta": "新增 closed-loop VLA equilibrium branch：把 action decoder 写成 task-conditioned fixed-point field，并把 residual threshold、iteration cap、warm start 与 latency budget 纳入 runtime state；停止深度必须按行为成功率而非 residual 单独验收。",
        "boundary": "RoboTwin/LIBERO 与作者模型只说明 matched-compute 下的局部可行性；两项 threshold scan 不给全局收敛或最优阈值，EqM objective、stopping rule 与 warm start 的增益仍有混杂。迭代不收敛、行为回归或时延超界时回退固定步数 flow/action decoder。",
    },
    "2605.23482": {
        "anchor": "after `### 从样本数量到 Coverage Contract：Curriculum 必须同时管理内容、能力与环境`; before `### 从 Trajectory Count 到 Primitive × Transition Coverage`",
        "delta": "新增 multimodal dataset-distillation branch：在 joint image-text embedding geometry 中匹配真实与合成分布，并把 expert revision、synthetic-set identity、modality balance 与 downstream evaluator 共同写入 distilled-data contract。",
        "boundary": "结果绑定作者的 embedding geometry、数据集、IPC/trajectory baselines 与 expert pool；joint-space 距离可能遗漏细粒度 modality evidence，规模增大还受 expert-training cost 支配。几何失配或 downstream slice 回归时回退原始数据 mixture、单模态校验与可重放 trajectory matching。",
    },
    "2605.23562": {
        "anchor": "after `### Pairwise coupling 不能外推 group dynamics`; before `#### Review notes`",
        "delta": "新增 MARL reward-shaping admission：dense shaping reward 只有在固定 opponent policy 下保持每个 agent 的 conditional best-response set 时，才能声称保留 equilibrium；reward learner、policy learner 与 exploration schedule 必须分责。",
        "boundary": "理论保证依赖固定对手条件，实验只覆盖部分可观测 multi-agent pathfinding；有限探索与耦合 policy-reward dynamics 会形成 oscillatory reward hacking。检测到循环协调或 best-response 漂移时增加探索、冻结 shaping model，或回退原始 sparse reward。",
    },
    "2605.23565": {
        "anchor": "before `## PPO 没有解决 Reward correctness`; after `## 关键诊断指标`",
        "delta": "新增 sequential-RL goal-generalization contract：OOD goal 由完整训练顺序与早期 salient features 共同决定，checkpoint 不能只记录最终 reward；把 task order、feature exposure 与 latent-policy-gradient probe 纳入训练历史审计。",
        "boundary": "100 余条训练流水线和 250 余个合成 OOD 环境只支持作者特征化环境；latent policy gradients 是低维预测模型，不是真实 policy 的因果证书。probe 失配或真实任务无可定义 feature basis 时回退直接 OOD rollout、counterfactual retraining 与人工 goal audit。",
    },
    "2605.23883": {
        "anchor": "after `### Supervision Granularity 应跟随可验证的状态边界`; before `### Data Mixture 可以随模型状态更新，但 Proposal 不能冒充最优配方`",
        "delta": "新增 fine-grained visual-supervision diagnostic：把可验证几何 primitive overlay 到真实图像，在不增加 sample count 的条件下区分 perception supervision 缺口与架构/分辨率瓶颈；overlay recipe 与真实语义 slice 必须共同版本化。",
        "boundary": "收益绑定作者的 geometric overlays、MLLM、instruction-tuning recipe 与 11 个 benchmark；任务饱和、视觉 clutter 与合成 primitive 偏差会削弱迁移，不能证明所有空间错误都来自数据。迁移或通用能力回归时回退原始 mixture、独立 synthetic set 与真实图像人工标注。",
    },
}


def owner_by_id() -> dict[str, str | None]:
    """Return a total, duplicate-free owner assignment for restored items."""
    result: dict[str, str | None] = {}
    for owner, ids in OWNER_GROUPS.items():
        for arxiv_id in ids:
            if arxiv_id in result:
                raise AssertionError((arxiv_id, result[arxiv_id], owner))
            result[arxiv_id] = owner
    for arxiv_id in STRUCTURAL:
        if arxiv_id in result:
            raise AssertionError((arxiv_id, result[arxiv_id], "Structural Candidate"))
        result[arxiv_id] = None
    return result


OWNER_BY_ID = owner_by_id()
RESTORE_IDS = set(OWNER_BY_ID)
assert len(RESTORE_IDS) == 157, len(RESTORE_IDS)
assert CONFIRMED_FALSE_NEGATIVES <= RESTORE_IDS
assert set(INTEGRATIONS) <= RESTORE_IDS
assert REPORT_ONLY <= RESTORE_IDS
assert DEFERRED <= RESTORE_IDS
