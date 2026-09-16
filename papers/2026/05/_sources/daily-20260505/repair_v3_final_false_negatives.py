#!/usr/bin/env python3
"""Apply the bounded 2026-05-05 false-negative repair.

The independent final review named ten definite false negatives, five boundary
families, one benchmark anti-case and three stale Books locators.  This script
only updates those identities plus derived summaries.  It does not scan a
source, edit Books, or touch another report date.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER_PATH = HERE / "V3_CANONICAL_LEDGER.json"
EVIDENCE_PATH = HERE / "V3_EVIDENCE_REVIEWS.json"
COMPARE_PATH = HERE / "V3_PROPOSITION_BOOKS_COMPARISON.md"
QUEUE_PATH = HERE / "books-writeback-queue.json"
QUEUE_MD_PATH = HERE / "V3_BOOKS_REVIEW_QUEUE.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


OWNER = {
    "MULTIMODAL-REPRESENTATION": (23, "books/part-03-multimodal-world-models/23-multimodal-representation.md"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": (24, "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md"),
    "MULTIMODAL-WORLD-MODELS": (25, "books/part-03-multimodal-world-models/25-multimodal-world-models.md"),
    "MULTIMODAL-EMBODIED-VLA": (26, "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md"),
    "TRAIN-DATA": (27, "books/part-04-training-system/27-data.md"),
    "TRAIN-GRPO": (33, "books/part-04-training-system/33-grpo.md"),
    "INFER-KV-CACHE": (45, "books/part-05-inference-system/45-why-kv-cache-speeds-up.md"),
    "PLATFORM-EVALUATION-SYSTEM": (66, "books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "AGENT-RAG": (76, "books/part-07-agent/76-rag.md"),
    "AGENT-MEMORY": (77, "books/part-07-agent/77-memory.md"),
    "AGENT-TOOL-CALLING": (78, "books/part-07-agent/78-tool-calling.md"),
    "AGENT-PLATFORM": (84, "books/part-07-agent/84-agent-platform.md"),
}


def score(values: tuple[int, int, int], delta: str, reach: str, durability: str) -> dict:
    design_delta, system_reach, durable = values
    return {
        "design_delta": design_delta,
        "system_reach": system_reach,
        "durability": durable,
        "total": sum(values),
        "rationale": {
            "design_delta": delta,
            "system_reach": reach,
            "durability": durability,
        },
    }


TARGETS = {
    "2605.00884": {
        "owner": "MULTIMODAL-EMBODIED-VLA",
        "score": (3, 3, 2),
        "mechanism": "把 VLA 的短 action-token 外环与较慢语义输出拆成双速路径，并把 prefill 主导延迟、控制频率和知识保持训练放进同一部署合同。",
        "method_locators": ["dual-rate operation", "knowledge-preserving fine-tuning", "onboard Jetson AGX Orin deployment"],
        "method": "系统在同一 256M VLA 上区分短 action-token 的快速 guidance mode 与 sentence-level semantic mode；两条路径共享 prefill 成本，训练 mixture 同时包含 reactive flight、aerial semantic 与通用 caption/VQA，以避免动作专化抹掉描述能力。",
        "evaluation_locators": ["Latency Breakdown", "Dual-Rate Performance", "comparison with AnywhereVLA/FutureVLA/ReMem-VLA"],
        "evaluation": "作者在 Jetson AGX Orin 上报告 action branch 50.65 ms（19.74 Hz）、semantic branch 149.90–164.57 ms（6.08–6.67 Hz），并指出该紧凑模型的端到端延迟主要由 multimodal prefill 主导。比较只对作者披露的模型、输入和设备成立。",
        "limitations_locators": ["outer-loop guidance scope", "deployment-condition comparison", "classical flight-control boundary"],
        "limitations": "论文只验证 outer-loop guidance 与周期语义感知；未证明 low-level flight controller、网络抖动、传感器故障、尾延迟或安全 envelope。跨架构 headline rate 也没有统一输入、精度、kernel 与控制任务。",
        "boundary": "证据支持在特定 edge VLA 上把 action 与 semantic cadence 分离，并识别 prefill 为主要成本；不支持把 19.74 Hz 写成通用控制频率，也不授予模型绕过低层控制器的执行权。",
        "books": "no_change",
        "locator": "Fast-Slow VLA：把慢语义状态与快控制拆成有界陈旧的异步闭环",
        "proposition": "慢语义状态与快动作路径必须分别持有 cadence、freshness 和安全回退，低层 controller 仍拥有执行 authority。",
        "comparison": "现有小节已经给出同一双速状态合同、staleness identity、训练部署一致性与保守 controller 回退；LiteVLA-H 增加 Jetson 上 prefill-dominant 的受限测量和双任务训练案例，没有改变该长期命题。",
    },
    "2605.01191": {
        "owner": "MULTIMODAL-EMBODIED-VLA",
        "score": (3, 3, 2),
        "mechanism": "由 active sentinel 持有实时执行状态，只在初始化、新子任务或错误时触发 reasoning/recovery，并把能力边界反馈到持续数据收集。",
        "method_locators": ["Sentinel-VLA architecture", "active status monitoring", "SECL and OC-Adapter"],
        "method": "sentinel 把执行状态划为 Initial、Normal、New-subtask 与 Error；Normal 状态复用动作/思考记忆，其他状态才触发规划、更新或恢复。SECL 根据失败边界收集数据，OC-Adapter 约束持续更新以减轻遗忘。",
        "evaluation_locators": ["real-world manipulation tasks", "status-transition ablation", "continual-learning evaluation"],
        "evaluation": "作者在自动生成的 44 个任务、约 260 万 transition 和有限真实机器人任务上比较状态监控、推理与持续学习组件，并报告相对 PI0 的任务成功率提升；这些结果绑定作者任务、错误注入和训练管线。",
        "limitations_locators": ["selected task/error taxonomy", "open-source future tense", "no production tail/safety evaluation"],
        "limitations": "论文没有证明状态分类覆盖开放世界异常，也没有独立验证 sentinel 的 false-negative、tail latency、传感器失真或物理安全；代码和权重在 v1 中仍以未来开放表述。",
        "boundary": "证据支持把状态监控作为 reasoning 的触发器和数据闭环的传感器；不证明 sentinel 状态是真值，也不允许它直接拥有 actuator commit。",
        "books": "no_change",
        "locator": "从“动作建议”到有状态的安全提交",
        "proposition": "异常监测只触发 plan、update 或 recover，必须绑定 observation revision、deadline 与安全回退，不能越过 action admission。",
        "comparison": "现有小节已经明确正常状态复用、异常状态触发推理/恢复，以及 monitor 只持有 proposal 权；该论文提供一个四状态实现和持续学习案例，但没有改变状态 owner 或提交边界。",
    },
    "2605.01302": {
        "owner": "AGENT-RAG",
        "score": (3, 3, 2),
        "mechanism": "把检索目标从 semantic relevance 改为对错误前提与确认偏误的 counterfactual decision risk，并由 Evidence Critic 产生 robustness score 与 abstention 控制。",
        "method_locators": ["Counterfactual Risk Minimization", "Cognitive Perturbation Protocol", "Evidence Critic"],
        "method": "训练时对 query 注入认知偏误扰动，以文档能否在干预后仍把决策推向正确方向定义效用，再蒸馏轻量 Evidence Critic。在线阶段 critic 对候选证据打 robustness 分，并与风险阈值共同决定采用或拒答。",
        "evaluation_locators": ["decision-making benchmarks", "adversarial query settings", "critic and abstention ablations"],
        "evaluation": "实验比较 dense retriever 与 LLM reranker，在作者构造的 decision/adversarial query benchmark 上报告鲁棒性和 risk-aware abstention 改善；消融支持 perturbation、critic 和 threshold 在该设置中的贡献。",
        "limitations_locators": ["benchmark-bound cognitive perturbations", "learned critic calibration", "threshold transfer not established"],
        "limitations": "偏误类型、counterfactual 构造、正确答案和 critic 共享同一实验合同；结果没有证明新 corpus、领域、语言或真实恶意用户上的校准，固定阈值也不是生产常数。",
        "boundary": "来源支持 relevance 在带偏 query 下可能系统性选择迎合性证据，并支持 counterfactual robustness 作为独立检索信号；不证明 critic score 是事实概率或可替代原始证据核验。",
        "books": "integrate",
        "locator": "Relevance 不等于 Sufficient Context",
        "current": "本章已拆分 relevance、sufficiency、faithfulness，并校准 escalation/abstention，但没有显式处理 query 自身带错误前提时，相关性会主动放大错误这一机制。",
        "delta": "在 relevance 与 sufficiency 之间增加 query-robustness gate：旧 top-k 在 query 前提可信时仍合理；当前提可能错误或带确认偏误时，retriever 应把候选在 counterfactual query perturbation 下能否维持决策支持作为独立信号。Critic 只提出 evidence-risk proposal，原始 source 与 answer gate 仍拥有事实和提交权。该分支以额外扰动数据、critic 校准和更多 abstention 换取对迎合性检索的抵抗；critic 漂移、偏误模板覆盖不足或高风险结论时回退多源原文核验/人工。exact-v1 只证明作者 decision benchmarks 和扰动合同中的结果，不提供跨 corpus 固定阈值。",
    },
    "2605.01345": {
        "owner": "MULTIMODAL-REPRESENTATION",
        "score": (3, 2, 2),
        "mechanism": "把高分辨率视觉推理改写为固定 token 带宽下的顺序 evidence acquisition，controller 在回答前主动选择下一块视觉观测。",
        "method_locators": ["sequential Bayesian optimal experimental design", "coverage-resolution proxy", "FOVEA evidence-oriented probing"],
        "method": "S-BOED 把视野覆盖与局部分辨率的冲突写成序贯实验设计；FOVEA 先用低分辨率全局视图形成假设，再根据 evidence-oriented probe 选择高分辨率 crop，直到预算或停止条件满足。",
        "evaluation_locators": ["high-resolution visual benchmarks", "remote-sensing search tasks", "direct/ReAct baselines"],
        "evaluation": "作者在高分辨率 benchmark，尤其 search-dominated remote-sensing tasks 上比较直接输入和 ReAct-style baseline，报告训练外主动 crop 的一致收益；结果绑定其 VLM、crop budget 与 proxy objective。",
        "limitations_locators": ["ideal-observer approximation", "backbone hallucination", "stochastic latency and adaptive invocation"],
        "limitations": "论文明确讨论 ideal-observer 假设、backbone hallucination、连续空间近似和随机 latency；adaptive invocation 仍属未来工作，未证明 crop policy 能识别所有关键证据或满足实时 SLO。",
        "boundary": "证据支持在固定视觉 token 预算下把 observation acquisition 作为可审计的顺序控制问题；不证明 crop proposal 是充分证据，也不覆盖开放世界视觉安全。",
        "books": "integrate",
        "locator": "固定预算要先分配信息责任，再选择具体 Token",
        "current": "本章已有 query-conditioned 模态/事件预算和 selector，但默认候选 observation 已经存在，没有说明模型可在推理中请求新的高分辨率局部证据。",
        "delta": "把固定视觉输入扩展为 bounded active-observation 分支：全局低分辨率视图先保留 context，acquisition policy 依据当前未决 claim 选择下一 crop，evidence assembler 记录坐标、尺度、采集顺序与 budget，answer gate 决定继续、提交或拒答。旧的一次性均匀采样在低分辨率已足够或 latency 严格时仍更稳；主动采集用细节可见性换额外调用、路径依赖、漏区与尾延迟。Selector 只拥有 observation proposal，不拥有 evidence sufficiency；exact-v1 结果限作者 VLM、crop proxy 和高分辨率 benchmark。",
    },
    "2605.01772": {
        "owner": "MULTIMODAL-EMBODIED-VLA",
        "score": (3, 3, 2),
        "mechanism": "用可随环境状态递归细化、弹出和回退的 subgoal stack 连接高层 anticipation model 与低层 goal-conditioned VLA policy。",
        "method_locators": ["Anticipation Model", "adaptive recursive subgoal generation", "stack-based refine/pop/backtrack execution"],
        "method": "高层 UMM 产生可执行 subgoal，低层 VLA 按当前 observation 执行；stack controller 根据进展弹出已完成目标，在复杂状态中继续细化，在偏离或失败时回退并重建未来 subgoal，而不是冻结固定粒度任务分解。",
        "evaluation_locators": ["simulated long-horizon tasks", "real-world robotic tasks", "subgoal-generation ablations"],
        "evaluation": "作者在模拟与有限真实机器人长程任务中比较固定/自适应 subgoal 路径，并通过消融支持递归 anticipation 对成功率的贡献；结果依赖其任务、value/progress 判断与低层 policy。",
        "limitations_locators": ["bounded task suite", "progress/value-model dependence", "no open-world safety proof"],
        "limitations": "subgoal 是否完成、何时细化和回退由学习式判断控制；论文没有证明开放世界中的 progress calibration、无限递归终止、异常恢复或安全关键物理提交。",
        "boundary": "来源支持将长程计划从固定 trace 演进为可修订 subgoal stack；不证明 anticipation 输出是环境事实，低层 controller 和 fresh observation 仍拥有执行与纠错边界。",
        "books": "integrate",
        "locator": "Full-horizon Multimodal Trace 是 Versioned Proposal",
        "current": "现有小节允许整条 trace 失效后重规划，但缺少局部 subgoal 的递归细化、完成弹出与失败回退状态机。",
        "delta": "在 immutable full-horizon trace 与逐步 reactive policy 之间增加 adaptive subgoal stack：每个 subgoal 绑定 observation revision、parent、完成条件和 validity horizon；高层 planner 只能 push/refine/backtrack proposal，低层 policy 用 fresh observation 执行，controller 验证完成后才 pop。它以局部修订降低整条计划报废成本，却新增 progress detector 误判、递归不终止、stack stale 和高低层语义漂移；动态环境或检测不可信时回退短 horizon reactive planning/全量重规划。exact-v1 只支持作者模拟与有限真实任务，不构成开放世界 safety proof。",
    },
    "2605.01799": {
        "owner": "MULTIMODAL-WORLD-MODELS",
        "score": (2, 2, 2),
        "mechanism": "把单目机器人视频转换为可变视角视频，并以 latent confidence 在 copy、repair 与 inpaint expert 之间路由，作为 embodied 4D 数据引擎。",
        "method_locators": ["3D-aware compositional synthesis", "latent confidence-aware expert modulation", "interaction-aware attention"],
        "method": "系统用跨 embodiment 机械臂与背景合成训练数据，从 source video warp 得到 latent prior，再按置信度把区域路由到复制、修复或补绘 expert，并对交互区域加强 attention。",
        "evaluation_locators": ["visual-generation benchmarks", "simulated robot planning", "real-world robot experiments"],
        "evaluation": "评价包含视觉质量和有限模拟/真实机器人任务；真实实验规模很小，且作者把生成视频作为下游规划/学习数据，不是环境真值。",
        "limitations_locators": ["extreme viewpoints", "fixed-view source", "49-frame generation around two minutes"],
        "limitations": "论文明确存在极端视角、固定源视角和生成速度限制；约 49 帧生成耗时约两分钟，不能用于实时 control，几何一致性也不证明物理 interaction 正确。",
        "boundary": "证据支持 confidence-aware view completion 作为派生数据生成机制；不支持把生成 novel view 当作持久 world state 或可执行 transition。",
        "books": "no_change",
        "locator": "从 RGB Rollout 到 Projective 4D Predictive State",
        "proposition": "多视角生成、几何状态和可执行 transition 是不同责任；派生视图必须保留 source/camera/projection identity 与回退。",
        "comparison": "现有小节已把 projective 4D state 与视觉生成分责，并要求几何/相机/provenance；Embody4D 提供 copy/repair/inpaint 的具体数据引擎，但没有改变 world-state owner 或实时控制边界。",
    },
    "2605.01896": {
        "owner": "MULTIMODAL-REPRESENTATION",
        "score": (2, 2, 2),
        "mechanism": "从 diffusion 中间表示分离 RGB/depth/mask 的模态特征，分别对齐 DINO、Depth 与 segmentation experts，并用 decoupling regularizer 保持互补。",
        "method_locators": ["multi-modal representation alignment loss", "modality-specific decoupling regularization", "expert foundation-model targets"],
        "method": "M2-REPA 不把多个 expert target 混成一个 embedding；它先提取模态专属 feature，再分别匹配对应 foundation model，并用 decoupling objective 减少模态特征坍缩为同一表示。",
        "evaluation_locators": ["RGB/depth/mask joint generation", "visual quality and long-term consistency", "alignment/decoupling ablations"],
        "evaluation": "实验在作者多模态视频生成模型与数据上比较视觉质量、depth/mask 和长时一致性；消融支持 alignment 与 decoupling 的联合贡献。",
        "limitations_locators": ["expert-target dependence", "additional training compute", "generation-benchmark scope"],
        "limitations": "表示质量继承 DINO/depth/segmentation expert 的偏差与覆盖；训练增加多路 target 和 regularization，结果没有证明任意模态/任务或 downstream control 的通用收益。",
        "boundary": "来源支持多目标对齐时先分开 modality-specific representation owner；不证明 expert embedding 是世界真值或联合生成已具有可执行性。",
        "books": "no_change",
        "locator": "对齐不是把向量拉近这么简单",
        "proposition": "语义、时空与行动对齐承担不同目标，多目标 loss 需要保留各自信息责任，不能由单一距离替代。",
        "comparison": "现有小节已明确不同 alignment target 与 reconstruction/semantic/action loss 的冲突；M2-REPA 是 RGB/depth/mask expert 的具体实现，没有改变该多目标分责原则。",
    },
    "2605.01948": {
        "owner": "TRAIN-DATA",
        "score": (2, 2, 2),
        "mechanism": "用手机 6-DoF pose、可替换 ROS 2 bridge 与同步 recorder 把 teleoperation 控制和特定机器人硬件解耦，并直接产出 LeRobot 格式的 VLA 训练记录。",
        "method_locators": ["ARCore 6-DoF controller", "interchangeable ROS 2 bridge nodes", "Universal Recorder"],
        "method": "Phone2Act 由手机产生统一控制 pose，bridge 映射到不同机器人，Universal Recorder 同步多相机 RGB 与机器人状态并序列化为 LeRobot dataset；同步 gate 和 action wrapper 负责时间对齐与 schema 适配。",
        "evaluation_locators": ["130 demonstration episodes", "GR00T-N1.5 fine-tuning", "Dobot CR5 pick-and-place"],
        "evaluation": "作者用 130 条采集 episode 微调 GR00T-N1.5，并在单一真实多阶段 pick-and-place 任务报告 9/10 成功；端到端 latency 主要受机器人系统约束。",
        "limitations_locators": ["single task and robot deployment", "ARCore/calibration dependence", "no safety-tail evaluation"],
        "limitations": "硬件无关只表示 bridge interface 可替换，不证明不同 embodiment 的动作语义、标定误差、同步丢帧和安全边界相同；130 条数据与一个任务不能支持通用 VLA 数据质量。",
        "boundary": "证据支持把采集控制、robot bridge、时间同步和训练记录拆成可版本化接口；不证明低成本 teleoperation 数据自动具有跨机器人可迁移性。",
        "books": "no_change",
        "locator": "从 Physical Teleoperation 到带 Provenance 的 Digital Teleoperation Data",
        "proposition": "teleoperation 派生轨迹必须绑定输入设备、时间同步、robot schema、retarget/bridge 与真实闭环验证。",
        "comparison": "现有小节已规定 teleoperation 到派生 robot trajectory 的 schema、provenance、per-embodiment adaptation 与真实控制验收；Phone2Act 补充手机/ROS2/LeRobot 案例，没有改变数据 owner 或跨 embodiment 边界。",
    },
    "2605.02178": {
        "owner": "TRAIN-GRPO",
        "score": (3, 3, 2),
        "mechanism": "在 token 与 turn 两层跟踪 uncertainty progress，停滞时分别触发 thinking intervention 和 turn resampling，改变多轮 Agent RL 的 rollout admission。",
        "method_locators": ["token-level uncertainty dynamics", "turn-level exploration progress", "intervention and resampling thresholds"],
        "method": "token controller 计算边际 uncertainty change，低于阈值时插入 thinking intervention；turn controller 判断一轮交互是否几乎没有探索进展并动态重采样。两者在优化前改变实际进入训练的 trajectory 分布。",
        "evaluation_locators": ["WebShop", "ALFWorld", "Search QA", "stability and exploration-efficiency ablations"],
        "evaluation": "作者在 WebShop、ALFWorld 和 Search QA 上报告训练稳定性、性能与探索效率改善，并比较 token/turn 组件；结果绑定所用 policy、uncertainty estimator、环境和阈值。",
        "limitations_locators": ["off-policy pipeline staleness", "fixed threshold/configuration", "environment-specific uncertainty calibration"],
        "limitations": "论文讨论 pipeline/off-policy staleness 与固定设置；uncertainty 不等于错误，低变化也可能表示已经收敛或需要长期延迟收益，错误干预会改写 on-policy 分布。",
        "boundary": "来源支持把 exploration progress 作为 rollout control signal；不证明 uncertainty 是 outcome verifier，也不允许 intervention/resampling 的数据在缺少 policy/version identity 时混入更新。",
        "books": "integrate",
        "locator": "Mid-rollout 提前停止只能取消低边际信息轨迹",
        "current": "本章已有 prefix 相似度驱动的取消 proposal，但没有把 token-level 思考干预与 turn-level 重采样分成两种不同控制动作。",
        "delta": "把低边际信息检测扩展成两层 exploration controller：token 层只能提出 bounded thinking intervention，turn 层只能提出 resample/cancel；group builder 保存触发分数、阈值、policy/environment revision 与最终 membership，optimizer 不把缺失 suffix 或重采样重复当独立证据。它用减少空转换取 estimator drift、selection bias、额外 token 和 on-policy staleness；uncertainty 不等于错误，late-reward 或校准不足时回退完整 rollout/静态采样。exact-v1 只支持 WebShop、ALFWorld、Search QA 与作者配置。",
    },
    "2605.02262": {
        "owner": "INFER-KV-CACHE",
        "score": (3, 2, 2),
        "mechanism": "按视觉 token window 与文本 prompt 的相似度分配 KV bit-width，并通过 window 重排把搜索 artifact 编译为可执行 mixed-precision layout/kernel。",
        "method_locators": ["window-level quantization search", "prompt-window similarity", "window reordering and mixed-precision KV computation"],
        "method": "WindowQuant 先在 window 粒度根据视觉窗口与 prompt 相似度搜索 bit-width，再重排同精度 window 以减少 irregular mixed-precision kernel 开销；重排保持 attention 行列对应，量化本身仍是近似。",
        "evaluation_locators": ["LLaVA-OneVision-Qwen2-7B", "EgoSchema and video-language datasets", "memory/latency/quality comparison"],
        "evaluation": "作者在披露 VLM、视频数据、batch 和 GPU 设置下报告平均约 3.17 bits 及 latency/memory 结果，并与 token-granularity 与统一量化比较；性能数字依赖窗口、layout、kernel 和 prompt 分布。",
        "limitations_locators": ["model/dataset/kernel-specific search", "prompt-similarity proxy", "quantization remains approximate"],
        "limitations": "prompt 相似度不是未来 decode query 的充分统计，窗口会混合关键与冗余 token；搜索、重排和 kernel 只在披露模型/硬件验证，未证明跨 prompt、长会话或在线漂移。",
        "boundary": "证据支持把 window-level bit allocation 与物理 layout 联合选择；不证明相似度是通用 KV 重要性，也不把作者平均 bit/latency 作为生产常数。",
        "books": "no_change",
        "locator": "Multimodal KV 选择必须区分 Prefill key 统计与 Decode query 需求",
        "proposition": "多模态 KV 选择必须说明决策时可见的 prompt/prefill 信号、未来 query 风险、量化误差坐标与 fallback。",
        "comparison": "现有小节已把 prompt-conditioned prefill signal 与未来 decode demand 分开，并要求压缩/漂移可检验；WindowQuant 是 window bit-width 与 layout 的具体实现，没有改变其信息边界和回退。",
    },
    "2605.02263": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS",
        "score": (3, 3, 2),
        "mechanism": "用专用 block-end token、block entropy trajectory 与 RL reward 学习动态 reasoning block boundary，替代 diffusion LM 的固定 block size。",
        "method_locators": ["dynamic block-end token", "monotonic entropy descent reward", "GRPO post-training"],
        "method": "b1 把 block boundary 变成生成状态：模型可在推理中输出 block-end token，训练用 entropy 从前一 block 到后一 block 的单调下降作为辅助 reward，并结合任务 reward 通过 GRPO 学习不同任务/步骤的 block size。",
        "evaluation_locators": ["reasoning benchmarks", "fixed-size block baselines", "block-size and reward ablations"],
        "evaluation": "作者在数学/推理 benchmark 和固定最大长度下比较多种固定 block baseline，并做 dynamic token 与 entropy reward 消融；训练硬件和结果只约束该 dLLM 与任务组合。",
        "limitations_locators": ["entropy descent is a proxy", "fixed benchmark/max-length scope", "no universal coherence proof"],
        "limitations": "边际 entropy 下降并不等于推理正确或语义步骤结束，错误但自信的 block 也可能满足 reward；论文未证明不同 dLLM、开放生成或部署并发下的阈值和收益。",
        "boundary": "来源支持把 block boundary 从固定超参数演进为 policy-owned generation state；不证明 entropy trajectory 是 correctness verifier，也不保证动态 block 在所有 workload 更快。",
        "books": "integrate",
        "locator": "Block Diffusion：逐 Token 与全局迭代之间的离散折中",
        "current": "本章已把 block size 视为 workload-dependent trade-off，也讨论 future-stable trajectory，但没有给出 boundary owner、训练信号和错误自信的反例边界。",
        "delta": "在 fixed block 旁增加 learned-boundary 分支：decoder 输出可验证的 block-end proposal，runtime 冻结 boundary/policy revision 后提交；训练可用 entropy trajectory 提供辅助 shaping，但任务 outcome/独立 verifier 仍拥有正确性。动态边界以语义步骤适配换 variable-length scheduling、cache/rollback 复杂度、reward hacking 和错误自信；短输出、静态 shape kernel 或 entropy 未校准时继续使用固定 block。exact-v1 的 reasoning benchmark 只支持该代理信号和后训练机制在作者设置中的结果。",
    },
    "2605.02411": {
        "owner": "AGENT-TOOL-CALLING",
        "score": (3, 2, 2),
        "mechanism": "把 tool shortlist 从初始 query 的一次静态结果变成执行中可修订的 action-space state，通过伪 tool 描述、并行探索和 tool memory 反复检索。",
        "method_locators": ["budgeted test-time retrieval", "serial/parallel pseudo-tool refinement", "Memetic Retrieval and tool memory"],
        "method": "FitText 生成自然语言 pseudo-tool descriptions 作为检索 probe，依据返回工具和执行反馈串行修订或并行探索；memetic 路径对 probe population 做选择、局部改写并缓存已尝试工具，避免重复搜索。",
        "evaluation_locators": ["StableToolBench 16,464 APIs", "current-model comparisons", "40-way concurrency"],
        "evaluation": "作者在 StableToolBench 与 GPT-4.1-mini 等当前模型上比较 static retrieval、single-pass、re-invoke 和 root refinement，并报告 pooled pass-rate 与并发 wall-clock；数值绑定该 catalog、模型、预算和 evaluator。",
        "limitations_locators": ["weak base models amplify noisy probes", "benchmark/catalog scope", "retrieval success is not authorization"],
        "limitations": "论文指出弱 base model 会让 memetic search 放大噪声；伪描述可能漂离真实 intent，tool memory 会过期，StableToolBench pass 也不证明动态版本、权限和副作用安全。",
        "boundary": "来源支持 action-space discovery 在执行中成为可修订状态；不支持由 retrieval score 授权工具，也不证明返回 schema 或 effect 正确。",
        "books": "integrate",
        "locator": "Tool Discovery 与选择",
        "current": "本章已有 authorized catalog retrieval、shortlist 和 schema exposure，但主要是一次性 discovery，没有定义失败后如何修订 probe、并行探索与保存检索 frontier。",
        "delta": "把静态 shortlist 扩展为 bounded revisable discovery state：每次 probe 保存 query/intention revision、返回 tool identities、尝试结果、预算与 parent；parallel branches 只拥有 proposal，retrieval controller 去重/合并 frontier，executor 仍逐项验证 schema、version、authorization 与 effect dependency。它用恢复早期漏检换额外模型调用、探索噪声、过期 tool memory 与 tail latency；catalog 小、接口稳定或风险高时回退静态 allowlist/typed schema。exact-v1 结果只覆盖 StableToolBench、所测模型和预算，不能作为开放生态的安全或性能保证。",
    },
    "2605.02525": {
        "owner": "AGENT-MEMORY",
        "score": (3, 2, 2),
        "mechanism": "以 deterministic resolver 处理稳定语义，只有歧义请求升级到 VLM，并把验证后的偏好按 global/operator/robot scope 提升为跨会话、跨机器人 memory digest。",
        "method_locators": ["six-layer Semantic Autonomy Stack", "seven-step parametric resolver", "five-category scoped semantic memory"],
        "method": "六层架构分离输入解析、确定性 resolution、VLM fallback、memory 与 ROS2 execution；确定性 resolver 先尝试 graph/POI 和规则，歧义才调用 VLM，经过验证的偏好按 scope 写入共享 digest 并供另一机器人读取。",
        "evaluation_locators": ["82 scenario-level decisions", "two differential-drive robots", "33 cross-robot transfer cases"],
        "evaluation": "物理实验覆盖两台 Raspberry Pi 5 机器人、82 个 scenario-level decisions 和 33 次 transfer；88% 指令由确定性路径处理。大幅 latency 比例主要来自微秒级规则与秒级 VLM 的路径差，不是端到端通用加速。",
        "limitations_locators": ["Qwen3.5:4b", "compatible graph/POI identifiers", "two similar robots"],
        "limitations": "作者明确只测一个小模型、相容的 graph/POI IDs 与两台相似机器人；没有证明跨 topology、异构 action schema、长期冲突合并和 unsafe preference 的迁移。",
        "boundary": "证据支持稳定规则 fast path、VLM fallback 与 scoped memory promotion 分责；不证明 memory transfer 自动正确，也不允许共享 digest 绕过 robot-specific capability/safety gate。",
        "books": "no_change",
        "locator": "Stable 与 Transient State 不能共用无条件覆写路径",
        "proposition": "稳定/瞬态、global/operator/robot scope 与事实/偏好必须分别准入、提升和撤销；共享 memory 不能扩大执行权限。",
        "comparison": "现有 Memory 章节已覆盖 scope、promotion、跨主体访问权和 derived digest；该栈提供两机器人规则/VLM 案例，但没有改变 memory ownership 或 capability gate。",
    },
    "2605.02697": {
        "owner": "AGENT-PLATFORM",
        "score": (3, 3, 2),
        "mechanism": "executor 根据 expiry、telemetry freshness、rollback handle、冲突、前置条件、planner-executor risk divergence 与 evidence budget 原子选择 commit、gate 或 reject。",
        "method_locators": ["C0/C1/C2 evidence envelope", "deterministic two-stage policy", "commit/gate/reject semantics"],
        "method": "C0 持有本地 triage，C1 仅在 gated intent 且 deadline/bandwidth 允许时按需取证，C2 留在 online safety path 之外用于事后 provenance；executor 先检查 expiry/freshness/rollback/conflict/risk divergence，再决定直接提交、取证或拒绝。",
        "evaluation_locators": ["3GPP-parameterized energy-saving benchmark", "slice-SLA benchmark", "stale-state fault campaign"],
        "evaluation": "两组无线 supervisory benchmark 比较 decision-identical eager evidence 与 invariant-respecting static threshold；部分结果按构造保持同决策，只隔离 evidence cost，stale fault campaign 验证声明阈值下拒绝行为。",
        "limitations_locators": ["seconds-to-minutes supervisory loop", "trace/benchmark not live network", "domain parameterization"],
        "limitations": "实验不是 live network，控制周期是秒到分钟，安全边界依赖作者规则、3GPP 参数和可用 rollback；结果不能外推到毫秒级控制、未建模冲突或真实 outage。",
        "boundary": "来源支持 executor-side intent admission 的证据分层与 fail-closed 语义；不证明规则覆盖所有风险，也不允许 planner 的风险分数替代授权和实际 effect receipt。",
        "books": "no_change",
        "locator": "Agent Runtime State Machine",
        "proposition": "每次 transition 必须绑定 actor、policy、budget、fresh state、rollback 与 side-effect evidence，执行与审计不能由模型叙述替代。",
        "comparison": "现有平台状态机及安全章节已要求 commit 前验证 scope/freshness/budget、失败时回滚或拒绝，并让 effect owner 产生 receipt；PRGA 的 C0/C1/C2 是无线控制的具体分层，没有改变通用提交权。",
    },
    "2605.02757": {
        "owner": "TRAIN-DATA",
        "score": (2, 2, 2),
        "mechanism": "把模拟 VLA 视频经 segmentation/caption 条件化 transfer 为逼真训练视频，用 diffusion feature reuse 降低生成成本并以 coreset 控制增强分母。",
        "method_locators": ["structured condition extraction", "conditional video transfer", "feature reuse and coreset sampling"],
        "method": "管线从 simulation 提取语义分割与 caption，改写环境描述后条件生成 realistic video，同时保留动作 trajectory；相邻 diffusion timestep 复用 video features，coreset 只选择非冗余 subset 进入昂贵增强。",
        "evaluation_locators": ["RoboTwin 2.0", "LIBERO/LIBERO-Plus", "real robotic platform"],
        "evaluation": "作者在 RDT-1B、pi0、RoboTwin/LIBERO 与一个真实平台上报告任务改善，并用 ablation 比较 transfer、reuse 和 coreset；结果绑定特定 simulator、生成器、模型和任务。",
        "limitations_locators": ["semantic-preservation proxy", "simulator/generator dependence", "selected-task scope"],
        "limitations": "视觉逼真不证明 action-condition 与接触动力学保持，caption/segmentation 错误会进入数据 lineage，coreset 可能删掉罕见安全尾部；未证明跨 embodiment 或开放环境泛化。",
        "boundary": "证据支持把 sim-to-real transfer artifact、feature cache 和 coreset selection 纳入数据版本；不支持将作者百分比外推为通用数据增益或把生成视频当真实 transition。",
        "books": "no_change",
        "locator": "静态 Mixture 到版本化 Data Control Plane",
        "proposition": "派生数据必须绑定 transform/generator、选择分母、cache、action schema 与真实 held-out/closed-loop 验收，稀有 failure tail 不能被中心样本静默删除。",
        "comparison": "现有 Data 章节已覆盖版本化 transform、synthetic trajectory、coreset/medoid 风险、sim-to-real provenance 和真实闭环 admission；该论文提供视频 transfer/reuse 的组合案例，没有改变长期数据合同。",
    },
}


INTEGRATION_INSERTION = {
    "2605.01302": "`Relevance 不等于 Sufficient Context` 内，relevance/sufficiency/faithfulness 三分之后、sufficiency evaluator 之前",
    "2605.01345": "`固定预算要先分配信息责任，再选择具体 Token` 内，层级预算与一次性 selector 之后",
    "2605.01772": "`Full-horizon Multimodal Trace 是 Versioned Proposal` 之后、Action representation 之前",
    "2605.02178": "`Mid-rollout 提前停止只能取消低边际信息轨迹` 之后、Group-relative Gradient 之前",
    "2605.02263": "Block Diffusion 主线内，固定 block size 的成立条件之后、Draft/verify 分支之前",
    "2605.02411": "`Tool Discovery 与选择` 内，catalog shortlist/schema exposure 之后、utility admission 之前",
}


ledger = load(LEDGER_PATH)
evidence = load(EVIDENCE_PATH)
queue = load(QUEUE_PATH)
entries = {item["arxiv_id"]: item for item in ledger["entries"]}
reviews = {item["arxiv_id"]: item for item in evidence["reviews"]}

for arxiv_id, cfg in TARGETS.items():
    entry = entries[arxiv_id]
    chapter, chapter_path = OWNER[cfg["owner"]]
    total = sum(cfg["score"])
    books_decision = (
        "Integrate Proposed — root writeback required; independent review pending"
        if cfg["books"] == "integrate"
        else "No Change — Existing Coverage (author proposition comparison; independent review required)"
    )
    entry.update(
        semantic_decision="semantic_reviewed_retain_frozen",
        decision_reason=(
            f"独立终审 false-negative/boundary 反证后恢复：{cfg['mechanism']} 该变化涉及 `{cfg['owner']}` 的状态、数据、控制或评价选择，"
            "不能在分母前以‘局部方法’关闭。"
        ),
        internal_design_delta_challenge=cfg["boundary"],
        exact_v1_status="review_complete_exact_v1_remote",
        owner=cfg["owner"],
        score_v2={"design_delta": cfg["score"][0], "system_reach": cfg["score"][1], "durability": cfg["score"][2], "total": total},
        books_decision=books_decision,
    )
    record = {
        "arxiv_id": arxiv_id,
        "source_family_id": entry["source_family_id"],
        "title": entry["title"],
        "exact_v1_url": f"https://arxiv.org/html/{arxiv_id}v1",
        "local_exact_v1_html": None,
        "exact_v1_access": "primary exact-v1 HTML reviewed remotely; bounded repair did not create a local mirror",
        "review_status": "deep_complete_author" if total >= 7 else "standard_complete_author",
        "score_v2": score(
            cfg["score"],
            f"题摘与 exact-v1 均显示：{cfg['mechanism']}",
            f"影响 `{cfg['owner']}` 的具体状态/数据/控制或评价合同；按作者 workload 限定 reach。",
            "只计可迁移机制与明确共存边界；单一模型、硬件、领域或 benchmark 数字不外推。",
        ),
        "method_locators": cfg["method_locators"],
        "method_evidence": cfg["method"],
        "evaluation_locators": cfg["evaluation_locators"],
        "evaluation_evidence": cfg["evaluation"],
        "limitations_locators": cfg["limitations_locators"],
        "limitations_evidence": cfg["limitations"],
        "mechanism_claim": cfg["mechanism"],
        "claim_boundary": cfg["boundary"],
        "owner": cfg["owner"],
        "chapter": chapter,
        "chapter_path": chapter_path,
        "books_decision": books_decision,
    }
    if cfg["books"] == "no_change":
        record.update(
            existing_coverage_locator=f"{chapter_path} — `{cfg['locator']}`",
            existing_coverage_proposition=cfg["proposition"],
            existing_coverage_comparison=cfg["comparison"],
            existing_marker_hits=0,
        )
    else:
        record.update(
            existing_coverage_locator=f"{chapter_path} — `{cfg['locator']}`",
            existing_coverage_proposition=cfg["current"],
            existing_coverage_comparison=f"现有覆盖与 exact-v1 对读后仍缺：{cfg['delta']}",
            existing_marker_hits=0,
        )
    reviews[arxiv_id] = record

# Explicit anti-case: keep HalluScan before the denominator after a concrete
# evaluation-owner comparison.  It must not inherit the old generic closure.
hallu = entries["2605.02443"]
hallu.update(
    semantic_decision="pre_denominator_closure_reviewed",
    decision_reason=(
        "显式 Evaluation 反证：HalluScan 的 72 configurations 来自 6 methods × 4 model families × 3 domains，"
        "但实质样本只有每域 8 条（共 24 条）；HalluScore 与专家仅中等相关 r=0.41，ADR 的 2× cost 结论绑定同一 benchmark、"
        "metric 与 routing setup。现有 Ch66 已要求 subject/dataset/scorer/run identity、risk–coverage、校准和独立 evidence；"
        "该来源没有改变通用 evaluation contract，故保持分母前关闭。"
    ),
    internal_design_delta_challenge=(
        "若获得跨数据集/独立人工校准、稳定置信区间或证明 ADR 改变 release-grade evaluator routing contract，应重开；"
        "当前 24-example、benchmark-specific 结果只作 anti-case，不支持生产阈值。"
    ),
    exact_v1_status="reviewed_for_explicit_pre_denominator_closure",
    owner="PLATFORM-EVALUATION-SYSTEM",
    score_v2=None,
    books_decision="Rejected — Existing evaluation contract and insufficient durability",
)

# The final reviewer found three stale locators.  Each now points to a different
# real Ch45 proposition that actually owns the source's mechanism.
LOCATOR_FIXES = {
    "2605.00831": (
        "从统一可靠性到状态敏感的保护预算",
        "KV 离开可靠 HBM 或需要故障接管时，保护预算、checkpoint identity、恢复路径与 failover commit 必须显式化。",
        "GhostServe 的 host-memory erasure-coded shadow checkpoint 是后台保护的具体实现；现有小节已经拥有可靠性分层、恢复/重算与状态身份，故不改变长期命题。",
    ),
    "2605.01910": (
        "稀疏 KV 保留的是派生状态，不只是被抽样的 Token",
        "稀疏 attention 读取的是带 model/position/selection identity 的派生状态，近似选择必须保存误差与 full-context fallback。",
        "Stochastic Sparse Attention 用随机选择换 memory-bound 访问缩减；现有小节已经覆盖稀疏派生状态、选择误差、身份和 FullKV 回退，故不改变长期命题。",
    ),
    "2605.02568": (
        "Structured knowledge 只有进入 physical access plan 才改变 KV 成本",
        "稀疏 logical selection 只有编译成 versioned physical gather/top-k plan，才会改变 HBM traffic；selector 不拥有正确性。",
        "StreamIndex 的 chunked partition-merge top-k 避免物化完整 score tensor，属于 physical access-plan/kernel 实现；现有小节已覆盖 logical/physical 分责、irregular gather 与 dense fallback。",
    ),
}
for arxiv_id, (heading, proposition, comparison) in LOCATOR_FIXES.items():
    review = reviews[arxiv_id]
    review["existing_coverage_locator"] = f"{review['chapter_path']} — `{heading}`"
    review["existing_coverage_proposition"] = proposition
    review["existing_coverage_comparison"] = comparison + " 仍待非作者逐命题复核。"

review_list = sorted(reviews.values(), key=lambda item: item["arxiv_id"])
retained = {item["arxiv_id"] for item in review_list}
for entry in ledger["entries"]:
    if entry["arxiv_id"] not in retained and entry["arxiv_id"] != "2605.02443":
        # Preserve existing specific closure text and status.
        continue

raw_count = ledger["raw_identity_count"]
closure_count = raw_count - len(review_list)
assert len({item["arxiv_id"] for item in ledger["entries"]}) == raw_count
assert len({item["source_family_id"] for item in ledger["entries"]}) == raw_count
assert retained == {item["arxiv_id"] for item in review_list}
assert sum(item["semantic_decision"] == "semantic_reviewed_retain_frozen" for item in ledger["entries"]) == len(review_list)
assert sum(item["semantic_decision"] == "pre_denominator_closure_reviewed" for item in ledger["entries"]) == closure_count

ledger["counts"] = {
    "pre_denominator_closure_reviewed": closure_count,
    "semantic_reviewed_retain_frozen": len(review_list),
}
ledger["candidate_denominator_frozen"] = True
ledger["status"] = "false_negative_author_repair_complete_root_books_writeback_and_independent_review_pending"

deep_count = sum(item["review_status"] == "deep_complete_author" for item in review_list)
standard_count = sum(item["review_status"] == "standard_complete_author" for item in review_list)
blocked_count = sum(item["review_status"] == "blocked_exact_v1_html" for item in review_list)
applied_count = sum(item["books_decision"].startswith("Integrate Applied") for item in review_list)
proposed_count = sum(item["books_decision"].startswith("Integrate Proposed") for item in review_list)
no_change_count = sum(item["books_decision"].startswith("No Change") for item in review_list)
assert deep_count + standard_count + blocked_count == len(review_list)
assert applied_count + proposed_count + no_change_count + blocked_count == len(review_list)

evidence.update(
    status="false_negative_author_repair_complete_root_books_writeback_and_independent_review_pending",
    candidate_count=len(review_list),
    review_complete=len(review_list) - blocked_count,
    deep_complete=deep_count,
    standard_complete=standard_count,
    blocked=blocked_count,
    books_integrate_applied=applied_count,
    books_integrate_proposed=proposed_count,
    books_no_change=no_change_count,
    reviews=review_list,
)

# Preserve applied queue items and add/update only the proposed items from this
# repair.  Complete semantic deltas are ready for root serialization.
queue_items = {item["source_family_id"]: item for item in queue["items"]}
for arxiv_id, cfg in TARGETS.items():
    if cfg["books"] != "integrate":
        continue
    entry = entries[arxiv_id]
    review = reviews[arxiv_id]
    chapter_file = ROOT / review["chapter_path"]
    queue_items[entry["source_family_id"]] = {
        "date": "2026-05-05",
        "source_family_id": entry["source_family_id"],
        "primary_identifier": f"arXiv:{arxiv_id}v1",
        "primary_source": review["exact_v1_url"],
        "stable_node_id": review["owner"],
        "target_chapter_path": review["chapter_path"],
        "current_chapter_sha256": hashlib.sha256(chapter_file.read_bytes()).hexdigest(),
        "current_chapter_locator": INTEGRATION_INSERTION[arxiv_id],
        "current_content_finding": cfg["current"],
        "new_delta_after_compare": cfg["delta"],
        "method_evidence": cfg["method"],
        "evaluation_evidence": cfg["evaluation"],
        "evidence_boundary": cfg["boundary"] + " " + cfg["limitations"],
        "adjacent_handoff": "只在 canonical owner 写完整机制；相邻章节仅更新确有变化的输入/输出 handoff，不复制论文摘要。",
        "required_writeback": "按给定 locator 融入旧方案成立条件 → 约束变化 → 状态/控制机制 → 证据边界 → trade-off/failure/fallback；写后回读相邻段落并新增唯一 source-family marker。",
        "comparison_status": "author_proposition_compare_complete_root_writeback_pending",
        "status": "root_writeback_required",
    }
queue["items"] = sorted(queue_items.values(), key=lambda item: (item["date"], item["source_family_id"]))

# Rebuild the No Change comparison ledger from the evidence array, avoiding
# stale row counts and locators.
no_changes = [item for item in review_list if item["books_decision"].startswith("No Change")]
compare_lines = [
    "# 2026-05-05 V3 Proposition-level Books Comparison",
    "",
    "本表从最终 Evidence Review 数组生成。每一行都比较一个可访问候选与目标章节的现有具体命题；它不是以 owner 名称代替 Books Review。",
    "",
    f"**No Change 数量：** {len(no_changes)}",
    "",
    "| Primary | Source Family | 现有具体命题定位 | 逐命题比较 |",
    "| --- | --- | --- | --- |",
]
for item in no_changes:
    compare_lines.append(
        f"| `{item['arxiv_id']}v1` | `{item['source_family_id']}` | {item['existing_coverage_locator']} | {item['existing_coverage_comparison']} |"
    )
COMPARE_PATH.write_text("\n".join(compare_lines) + "\n")

queue_lines = [
    "# 2026-05-05 V3 Books 写回队列",
    "",
    "本文件是 `books-writeback-queue.json` 的可读投影。作者代理没有直接修改共享 Books；`root_writeback_required` 必须由 root 按日期和目标文件串行写回并重新做语义复核。",
    "",
    "| Source Family | Owner / 目标 | 状态 | 精确插入位置 |",
    "| --- | --- | --- | --- |",
]
for item in queue["items"]:
    queue_lines.append(
        f"| `{item['source_family_id']}` | `{item['stable_node_id']}` / `{item['target_chapter_path']}` | `{item['status']}` | {item['current_chapter_locator']} |"
    )
queue_lines.extend([
    "",
    "## 本轮待写回的完整语义增量",
    "",
])
for item in queue["items"]:
    if item["status"] != "root_writeback_required":
        continue
    queue_lines.extend([
        f"### `{item['source_family_id']}`",
        "",
        item["new_delta_after_compare"],
        "",
        f"**证据边界：** {item['evidence_boundary']}",
        "",
    ])
QUEUE_MD_PATH.write_text("\n".join(queue_lines) + "\n")

dump(LEDGER_PATH, ledger)
dump(EVIDENCE_PATH, evidence)
dump(QUEUE_PATH, queue)

print(
    json.dumps(
        {
            "raw": raw_count,
            "retained": len(review_list),
            "closure": closure_count,
            "deep": deep_count,
            "standard": standard_count,
            "blocked": blocked_count,
            "applied": applied_count,
            "proposed": proposed_count,
            "no_change": no_change_count,
            "writeback_pending": sum(item["status"] == "root_writeback_required" for item in queue["items"]),
        },
        ensure_ascii=False,
    )
)
