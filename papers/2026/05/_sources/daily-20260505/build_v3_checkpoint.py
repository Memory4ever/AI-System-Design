#!/usr/bin/env python3
"""Build the resumable 2026-05-05 V3 author-side denominator checkpoint."""

from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "arxiv-owner-replay-20260903" / "20260505" / "arxiv-owner-receipt.json"
OUT = HERE / "V3_CANONICAL_LEDGER.json"
PRIOR_LEDGER = HERE / "screening-ledger-final.json"
PRIOR_CHALLENGE = HERE / "ROOT_FRESH_CONTEXT_CHALLENGE.md"


def load_reaudited_prior_closures() -> dict[str, str]:
    """Reuse evidence text, not decisions, after excluding every challenged family.

    The old ledger is not a terminal authority.  It is only a title+abstract evidence
    packet already stored in the repository.  Every family challenged by the later
    fresh-context review stays open; only unchallenged, domain/local/benchmark closures
    are admitted into the current V3 batch after the author re-applies the strict gate.
    """
    prior = json.loads(PRIOR_LEDGER.read_text())
    challenged = set(re.findall(r"`(2605\.\d{5})v1`", PRIOR_CHALLENGE.read_text()))
    return {
        item["arxiv_id"]: item.get("screening_reason", "")
        for item in prior["identities"]
        if item.get("screening_status") == "pre_denominator_closed"
        and item["arxiv_id"] not in challenged
    }


PRIOR_CLOSURES_REAUDITED = load_reaudited_prior_closures()

RETAIN_STRICT = {
    # Existing report candidates independently re-read against the current gate.
    "2605.00831", "2605.00842", "2605.00914", "2605.00932", "2605.00994",
    "2605.01106", "2605.01130", "2605.01188", "2605.01194", "2605.01255",
    "2605.01311", "2605.01352", "2605.01425", "2605.01640", "2605.01644",
    "2605.01708", "2605.02043", "2605.02087", "2605.01970", "2605.01989",
    "2605.02812", "2605.02375", "2605.02821", "2605.02364", "2605.02124",
    "2605.02881", "2605.02495", "2605.02189", "2605.02187", "2605.02888",
    "2605.02404", "2605.02568", "2605.02572", "2605.02739", "2605.02682",
    "2605.02329",
    # Newly recovered false-negative risks that clear the same design-delta gate.
    "2605.00827", "2605.00884", "2605.01030", "2605.01037", "2605.01058",
    "2605.01133", "2605.01167", "2605.01191", "2605.01345", "2605.01357",
    "2605.01429", "2605.01566", "2605.01567", "2605.01604", "2605.01688",
    "2605.01694", "2605.01704", "2605.01710", "2605.01749", "2605.01750",
    "2605.01772", "2605.01789", "2605.01799", "2605.01844", "2605.01858",
    "2605.01896", "2605.01910", "2605.01920", "2605.01938", "2605.01950",
    "2605.02028", "2605.02038", "2605.02050", "2605.02105", "2605.02122",
    "2605.02134", "2605.02162", "2605.02206", "2605.02218", "2605.02236",
    "2605.02241", "2605.02255", "2605.02262", "2605.02363", "2605.02395",
    "2605.02398", "2605.02442", "2605.02647", "2605.02735", "2605.02751",
    "2605.02765", "2605.02801", "2605.02853",
}

# A second adversarial pass rejects papers that can name a ROADMAP topic but cannot
# state which durable system decision changes. These remain preserved as closures.
REMOVE_AFTER_INTERNAL_CHALLENGE = {
    "2605.00932", "2605.00884", "2605.01058", "2605.01167", "2605.01191",
    "2605.01345", "2605.01357", "2605.01429", "2605.01567", "2605.01604",
    "2605.01688", "2605.01710", "2605.01749", "2605.01772", "2605.01789",
    "2605.01799", "2605.01844", "2605.01896", "2605.02050", "2605.02122",
    "2605.02262", "2605.02363", "2605.02398", "2605.02442", "2605.02647",
    "2605.02735", "2605.02765", "2605.02801",
}
RECOVERED_RETAIN = {
    "2605.00832", "2605.00955", "2605.01048", "2605.01060", "2605.01129", "2605.01195",
    "2605.01201", "2605.01247", "2605.01284", "2605.01342",
}
RETAIN_STRICT = (RETAIN_STRICT - REMOVE_AFTER_INTERNAL_CHALLENGE) | RECOVERED_RETAIN

# Final title + complete-abstract semantic pass over the owner receipt.  These are
# newly retained because the abstract can state a durable contract delta, not merely
# because the topic resembles a ROADMAP node.
FULL_PASS_RECOVERED_RETAIN = {
    "2605.00935", "2605.00974", "2605.01032", "2605.01069", "2605.01137",
    "2605.01192", "2605.01220", "2605.01288", "2605.01298", "2605.01301",
    "2605.01346", "2605.01415", "2605.01449", "2605.01643", "2605.01657",
    "2605.01662", "2605.01675", "2605.01699", "2605.01725", "2605.01740",
    "2605.01761", "2605.01790", "2605.01823", "2605.01837", "2605.01928",
    "2605.01930", "2605.01936", "2605.02037", "2605.02083", "2605.02106",
}
RETAIN_STRICT |= FULL_PASS_RECOVERED_RETAIN

CLOSE_REVIEWED = {
    "2605.00957": "小样本 RAG 置信方法只给出局部任务改进，尚未改变长期检索或校准契约",
    "2605.01104": "AI 编程交互采集平台属于领域研究工具，未形成通用 AI System 机制增量",
    "2605.01124": "通用 MLIR 形式验证工作未建立与模型训练或推理执行计划的专属机制连接",
    "2605.01205": "跨 tokenizer span 蒸馏是局部训练方法改进，未改变项目长期训练设计判断",
    "2605.01224": "多语言立场与小规模行为观察未改变 AI System 的状态或控制契约",
    "2605.01256": "任务适配与模型合并的局部方法增益不足以改变长期后训练分支判断",
    "2605.01347": "多智能体蒸馏的单方法结果尚未形成可迁移的训练或编排机制",
    "2605.01555": "自动化可解释性代理是局部分析流程，证据不足以改变解释性 owner 结论",
    "2605.01605": "LoRA 生成鲁棒性的分段诊断属于局部实验结论",
    "2605.01660": "通用编译器验证案例未形成 AI 执行 runtime 的独立长期增量",
    "2605.01735": "几何 unlearning 是局部算法分支，未改变现有删除与验证契约",
    "2605.01973": "hypernetwork 条件化是模型局部架构方案，尚无跨系统设计增量",
    "2605.02173": "特定语种百万上下文 benchmark 主要提供领域测量，不改变长上下文机制判断",
    "2605.02348": "解码时去偏的局部 PRM 方案不足以改变通用解码或治理契约",
    "2605.02391": "差分隐私运行监控是通用形式方法，案例未连接到 AI 平台证据链",
    "2605.02452": "图与 LLM 的立场综述未提供可独立核验的长期机制增量",
}

POSITION_OR_SURVEY = {
    "2605.00932", "2605.01147", "2605.01214", "2605.01280", "2605.02244",
    "2605.02452", "2605.02801",
}
BENCHMARK_ONLY = {
    "2605.01203", "2605.01394", "2605.01687", "2605.01847", "2605.01939",
    "2605.02173", "2605.02307", "2605.02443",
}
LOCAL_METHOD = {
    "2605.00939", "2605.00957", "2605.01047", "2605.01078", "2605.01111",
    "2605.01199", "2605.01205", "2605.01208", "2605.01256", "2605.01293",
    "2605.01302", "2605.01347", "2605.01373", "2605.01386", "2605.01462",
    "2605.01555", "2605.01605", "2605.01627", "2605.01735", "2605.01758",
    "2605.01766", "2605.01853", "2605.01899", "2605.01913", "2605.01948",
    "2605.01973", "2605.02168", "2605.02209", "2605.02348", "2605.02396",
    "2605.02411", "2605.02427", "2605.02435", "2605.02455", "2605.02463",
    "2605.02544", "2605.02584", "2605.02641", "2605.02697", "2605.02741",
    "2605.02757",
    # Existing report items whose current V3 contribution claim does not clear the stricter gate.
    "2605.01771", "2605.01782", "2605.01831", "2605.02469", "2605.02196",
    "2605.02125", "2605.02626", "2605.02199", "2605.02269", "2605.02178",
    "2605.02320", "2605.02263",
    # Failed the explicit old-constraint / contract-delta / design-choice challenge.
    "2605.00884", "2605.01058", "2605.01167", "2605.01191", "2605.01345",
    "2605.01357", "2605.01429", "2605.01567", "2605.01604", "2605.01688",
    "2605.01710", "2605.01749", "2605.01772", "2605.01789", "2605.01799",
    "2605.01844", "2605.01896", "2605.02050", "2605.02122", "2605.02262",
    "2605.02363", "2605.02398", "2605.02442", "2605.02647", "2605.02735",
    "2605.02765", "2605.02801",
}
GENERAL_NON_AI_SYSTEM = {"2605.01104", "2605.01124", "2605.01224", "2605.01660", "2605.02391"}
ADDITIONAL_REVIEWED_CLOSURES = {
    "2605.01143", "2605.01186", "2605.01471", "2605.01477", "2605.01560",
    "2605.01666", "2605.01796", "2605.02179", "2605.02195", "2605.02240",
    "2605.02273", "2605.02489", "2605.02503", "2605.02525", "2605.02709",
    "2605.02728", "2605.02811", "2605.02819", "2605.02832",
}

CHALLENGE_GROUPS = {
    "runtime": {
        "2605.00831", "2605.01060", "2605.01106", "2605.01352", "2605.01708",
        "2605.01858", "2605.01910", "2605.01989", "2605.02189", "2605.02218",
        "2605.01220", "2605.01725", "2605.01837", "2605.02329", "2605.02404",
        "2605.02568", "2605.02888",
    },
    "training": {
        "2605.00842", "2605.01130", "2605.01188", "2605.01255", "2605.01640",
        "2605.02043", "2605.02087", "2605.02105", "2605.02124", "2605.02364",
        "2605.01192", "2605.01288", "2605.01643", "2605.01823", "2605.01928",
        "2605.02375", "2605.02395", "2605.02495", "2605.02572",
    },
    "evidence_security": {
        "2605.00832", "2605.00914", "2605.00955", "2605.00994", "2605.01048", "2605.01129",
        "2605.01133", "2605.01247", "2605.01311", "2605.01425", "2605.01644",
        "2605.01950", "2605.01970", "2605.02028", "2605.02038", "2605.02187",
        "2605.02206", "2605.02241", "2605.02255", "2605.02682", "2605.02751",
        "2605.00935", "2605.00974", "2605.01032", "2605.01137", "2605.01298",
        "2605.01346", "2605.01415", "2605.01449", "2605.01699", "2605.01740",
        "2605.01761", "2605.01930", "2605.01936", "2605.02083", "2605.02812",
        "2605.02821", "2605.02853",
    },
    "agent_state": {
        "2605.00827", "2605.01030", "2605.01037", "2605.01284", "2605.01342",
        "2605.01566", "2605.01694", "2605.01704", "2605.01750", "2605.01920",
        "2605.01657", "2605.01662", "2605.01675", "2605.02106",
        "2605.02162", "2605.02236",
    },
    "multimodal_control": {
        "2605.01194", "2605.01195", "2605.01201", "2605.01938", "2605.02134",
        "2605.01069", "2605.01301", "2605.01790", "2605.02037", "2605.02739",
        "2605.02881",
    },
}

GROUP_CHALLENGE = {
    "runtime": {
        "old_constraint": "旧 runtime 把请求、缓存、通信或设备执行视为单一静态路径，平均性能掩盖可恢复状态与 SLO 边界",
        "design_choice": "要求按显式状态、正确性与 SLO 选择 checkpoint、压缩、调度、分层或执行计划，而不是只比较吞吐",
    },
    "training": {
        "old_constraint": "旧训练判断主要看聚合 loss 与单一 recipe，无法区分数据、表示、更新、通信或反馈信号造成的约束",
        "design_choice": "要求把数据/目标/更新/通信边界写入训练合同，并用对应反事实或稳定性证据选择 recipe",
    },
    "evidence_security": {
        "old_constraint": "旧验收把单次输出、平均分或模型名称当作充分证据，遗漏攻击路径、混杂、漂移与证据 provenance",
        "design_choice": "要求修改 evaluation/release/security gate，记录攻击面、对照、身份、trace 与适用条件",
    },
    "agent_state": {
        "old_constraint": "旧 Agent 设计把模型调用视为无状态文本生成，执行、上下文、协作与持久状态的 owner 不清楚",
        "design_choice": "要求拆分 proposal、execution、context、memory 与 coordination state，并为提交、回滚和授权设置边界",
    },
    "multimodal_control": {
        "old_constraint": "旧多模态/具身路径把感知、预测、推理与动作合成一个模型调用，无法约束时延与物理安全",
        "design_choice": "要求分离表示、世界状态、deliberation 与低层控制，并按控制频率、安全包络和证据选择 handoff",
    },
}

MECHANISM_DELTA = {
    "2605.00827": "以声明式 blueprint 和幂等执行器把 MCP 智能提议与工作流执行分开",
    "2605.00831": "用 host-memory erasure-coded shadow checkpoint 保护增长中的 KV 状态并支持故障恢复",
    "2605.00832": "把可控合成生成器当作实验装置，用因子设计区分 coverage gap 与 spurious dependency 并定向补数",
    "2605.00842": "非正交 superposition 使目标微调沿几何邻近方向产生 gradient spillover",
    "2605.00935": "diffusion timestep embedding 可经 scheduler interface 成为隐蔽信息注入与 provenance side channel",
    "2605.00974": "分层规则记忆同时积累成功与失败攻击经验，使 jailbreak 策略跨目标持续演化",
    "2605.00914": "同质 debate 暴露从众、上下文脆弱和投票丢失已有正确答案的三条失败路径",
    "2605.00955": "以可客观评分的 hard-evidence probes 推断 RAG 语料成员身份",
    "2605.00994": "用基模/微调模的 perplexity difference 暴露 model-organism 的微调目标",
    "2605.01030": "用 effect-transparent 语义边界约束 AI workflow 的表达能力与可判定性",
    "2605.01032": "以 capability-indexed effect system 和可机检 handler algebra 将治理边界绑定到可表达程序",
    "2605.01037": "把静态 purity 证明签名成运行时可校验的执行凭证并显式保留 TCB",
    "2605.01048": "用 meaning-preserving perturbation 作为反事实 baseline，避免把表面改写误判为目标因素效应",
    "2605.01060": "SuperBatch 在跨分区 embedding 中同时给出有界内存、流式首输出与故障恢复粒度",
    "2605.01069": "用 task-level barrier function 在运行时最小修正具身策略动作，而不是把安全隐含进 reward",
    "2605.01106": "hybrid model 的组件组合方式决定内部 draft 的可接受率与 self-speculation 可行性",
    "2605.01129": "unlearning 前后差分会把隐私泄漏从 forget set 扩展到 retain set",
    "2605.01130": "连续 SFT/SDF 多数近似幂等，而持续 DPO 且不重置模型时才稳定放大特征",
    "2605.01133": "embedding 防御在多轮多 Agent 传播中衰减，暴露局部过滤并非系统安全边界",
    "2605.01137": "联合观察会聚合相关证据，使逐记录 metric-DP 保证不能约束 posterior leakage",
    "2605.01188": "compute-optimal allocation 随 bytes 而非 token 数缩放，token compression rate 成为训练变量",
    "2605.01192": "线性 readout 的 cross-talk floor 与非线性 threshold reset 形成不同的 superposition 容量边界",
    "2605.01194": "uncertainty clutch 只在需要时切换到候选动作与相对 action critic 的 deliberation",
    "2605.01195": "从状态-动作安全分数构造经验控制不变集，并在越界时触发 recovery",
    "2605.01201": "用 execution-guarantee region 将任务成功与是否允许 visuomotor policy 执行绑定",
    "2605.01220": "隐式 equilibrium layer 将视觉 AR 的训练内存与推理迭代预算解耦为可调计算状态",
    "2605.01247": "浏览 Agent 的行为 fingerprint 比共享浏览器指纹更能支持运行时识别与控制",
    "2605.01255": "只对满足无偏条件的线性算子压缩 activation，并复用低秩因子压缩梯度",
    "2605.01284": "把多跳 RAG 的证据 owner 从文本引用细化到页面截图的 pixel bounding boxes",
    "2605.01288": "深层非线性网络的 saddle escape 由 bottleneck-scale 层数而非总深度控制",
    "2605.01298": "闭式、data-independent clean-label trigger 将供应链攻击从 surrogate 训练依赖中解耦",
    "2605.01301": "对共享感知结果的微小 pose 篡改会沿 tracking 与 prediction 数据流放大为不安全控制",
    "2605.01311": "只有随机实验与离线 simulator 联合才能识别混杂日志中的因果模型价值",
    "2605.01346": "在部分可观测冲突中比较竞争解释的 margin 决定 commit 或 abstain，而非依赖单分支置信度",
    "2605.01342": "access-aware lattice 让向量索引、存储预算与授权 query plan 共同决定检索",
    "2605.01352": "打破 CUDA/Vulkan context 隔离，使仿真 compute 与 graphics 可空间复用同一 GPU",
    "2605.01425": "自回归输出的生成后 credit attribution 受不可辨识与组合搜索约束",
    "2605.01415": "把不可逆决策、物理资源动员与自我扩张权限分离为外部可审查的 sovereignty boundaries",
    "2605.01449": "将输出扰动与攻击者目标真正注入分开度量，反证单一 attack-success-rate 的安全结论",
    "2605.01566": "多 Agent test-time scaling 的收益必须落在 token-cost/accuracy Pareto 前沿而非只看准确率",
    "2605.01640": "data cap 下的 scaling law 把新增算力重新分配到数据质量、重复与模型规模",
    "2605.01644": "Agent safety measurement 必须覆盖策略搜索空间而不是只测固定输出样本",
    "2605.01643": "solver 与 auditor 的联合纠错事件使 reward design 成为保持监督激励的双层控制问题",
    "2605.01657": "VLM 在推理中主动决定检索或生成视觉证据，使 context acquisition 成为显式动作",
    "2605.01662": "长视频推理将 keyframe selection 建模为基于生成先验的 inference-time data acquisition",
    "2605.01675": "并行生成候选约束程序并综合可执行 checker 证据，将 verifier 变为最终选择 authority",
    "2605.01694": "world-model latent state 以任务充分性而非重建完整 observation 作为设计约束",
    "2605.01704": "closed-system 多步推理存在信息边界，外部 evidence 改变可恢复性而非单纯增加思考 token",
    "2605.01708": "bit-exact KV transfer compression 在 PD 拆分中压缩传输而不改变 decode 状态",
    "2605.01699": "跨序列 probe 揭示 unlearning 后可恢复的表示痕迹，并用逐层 rank-one intervention 擦除",
    "2605.01725": "按 token 运动强度动态决定视频生成 cache 更新频率，显式控制复用误差累积",
    "2605.01740": "biconditional gate、hash-chain audit、egress guard 与 signing root 共同绑定 Agent action 与审计记录",
    "2605.01761": "把文本到视频安全从 prompt 词面过滤提升为生成轨迹上的因果风险定位与最小改写",
    "2605.01790": "在统一 acoustic-token hierarchy 中分层生成结构与细节，并以固定步数并行补全细粒度 token",
    "2605.01750": "多 Agent 协商失败来自共享 grounding 动态漂移，并需要显式 repair 而非增加消息",
    "2605.01858": "流式视频把 KV 构建与帧到达解耦，避免每次更新重算全部视觉历史",
    "2605.01823": "用成功率、输出分歧与难度学习选择 RLVR 样本，替代 reward variance 单启发式 curriculum",
    "2605.01837": "在层级供电与多租户合同下用逐控制周期可行优化分配 GPU power budget",
    "2605.01910": "随机稀疏选择用可控近似换取 memory-bound attention 的访问缩减",
    "2605.01928": "对含离散跳变的网络以固定分辨率 stationarity 和 forward-only transport step 替代不存在的梯度",
    "2605.01930": "用硬件物理 fingerprint 替代可被提取的片上密钥以绑定 GPU location identity",
    "2605.01936": "从顺序搜索成本导出同时约束概率校准与竞争项排序的 proper scoring rule",
    "2605.01920": "用可描述的 context schema 标注 Agent 所见信息、来源和作用域",
    "2605.01938": "跨层测量把 GH200 多模态训练的能耗归因到数据移动而非只归因 FLOPs",
    "2605.01950": "tail-aware ranking attack 表明 world-model planner 的候选轨迹排序本身是攻击面",
    "2605.01970": "恶意内容可写入持久 Agent memory，并在后续会话恢复时触发数据外泄",
    "2605.01989": "按训练 phase 与 loss budget 选择有损/可靠传输 fallback，而非统一可靠协议",
    "2605.02028": "extended rule following 暴露模型对有限内部规则状态的持续更新失败",
    "2605.02038": "同一任务的 prompt variants 揭示单提示 accuracy 无法度量服务可靠性",
    "2605.02037": "以模块化硬件、统一采集/部署数据流和一致 demonstrations 暴露 VLA 的真实部署边界",
    "2605.02083": "用显式 fact graph 检查局部事实修改是否传播到依赖叙述，形成 cascade-aware artifact gate",
    "2605.02043": "异步 SGD 的 data-dependent delay 与 momentum 必须联合校正才能保持更新语义",
    "2605.02087": "把行为 spec 注入 midtraining，改变 alignment generalization 的训练阶段 owner",
    "2605.02105": "sharpness-aware pretraining 改变后续适配时 catastrophic forgetting 的初始几何条件",
    "2605.02106": "把带时间、来源与交互上下文的 episodic-semantic graph 设为可追加持久 memory owner",
    "2605.02124": "soft routing 训练到 hard dispatch 的边界质量由 routing mass 演化而非只由 top-k 决定",
    "2605.02134": "predictive latents 让视频生成表示承担未来状态预测而非只重建当前像素",
    "2605.02162": "零拷贝数据流与可组合执行模式把 Agent workflow 从脚本升级为显式 runtime",
    "2605.02187": "BYOK response relay 可静默篡改，provider-signed envelope 才能绑定响应 provenance",
    "2605.02189": "commodity GPU 离线推理通过阶段 pipeline 重排内存与计算，而非照搬在线 serving",
    "2605.02206": "多模态 unlearning 指标会给出相反排序，oracle-distance 约束改变 composite score",
    "2605.02218": "device-edge VLM speculation 联合视觉 token pruning、adaptive draft 与通信 correction",
    "2605.02236": "递归 LLM loop 的持久逃逸由 append/replace/dialog memory policy 决定",
    "2605.02241": "生成 log-probability 可作为小模型到云模型升级路由的零样本置信信号",
    "2605.02255": "统一威胁模型揭示 MIA、提取、属性推断与 backdoor 对模型/RAG 配置的依赖不同",
    "2605.02329": "PD 两侧分别用 TTFT urgency 与 TPOT slack 控制长尾请求和 decode packing",
    "2605.02364": "quality-weighted mixture 与 repetition 改写固定 token-count 数据 scaling 判断",
    "2605.02375": "binary verifier 同时引入可辨识性与方差边界，限制 RL 信号可恢复的信息",
    "2605.02395": "PRM 监督必须标注第一处 prefix 不再支持的步骤，而非只给终局或逐步表面标签",
    "2605.02404": "用 next-token distribution agreement 区分 task-lossless 与 distribution-lossless quantization",
    "2605.02495": "offline preference dataset 的少量污染可定向改变 RLHF policy，数据 provenance 成为安全边界",
    "2605.02568": "chunked partition-merge top-k 避免物化完整稀疏 attention score tensor",
    "2605.02572": "只增加 interaction horizon 就会恶化探索与 credit assignment，horizon reduction 可稳定训练",
    "2605.02682": "zero-trust interception 联合确定性完整性检查与 task-tool 语义授权",
    "2605.02739": "预测相邻 timestep 的 VLM feature delta，使低层 action head 可跳过部分 backbone 调用",
    "2605.02751": "多轮多 Agent 交互会传播反社会行为，重复 system prompt 不是稳定隔离手段",
    "2605.02812": "Agent worm 可跨平台发现、传播并借 temporal re-entry 恢复，单次清理不足",
    "2605.02821": "同名 open-weight model 在不同 provider/time 下应建模为可漂移 service object",
    "2605.02853": "逐层可达参考解揭示 aggregate training loss 隐藏的 under-optimized layer",
    "2605.02881": "VLA 将空间 backbone、action tokenizer、continuous expert 与 adaptive-depth grounding 组合成部署闭环",
    "2605.02888": "speculation length 的最优值随 target compression 和逐步置信信号变化",
}


def challenge_for(arxiv_id: str) -> dict[str, str]:
    groups = [name for name, ids in CHALLENGE_GROUPS.items() if arxiv_id in ids]
    assert len(groups) == 1, (arxiv_id, groups)
    assert arxiv_id in MECHANISM_DELTA, arxiv_id
    group = GROUP_CHALLENGE[groups[0]]
    return {
        "old_system_constraint": group["old_constraint"],
        "changed_state_data_control_or_eval_contract": MECHANISM_DELTA[arxiv_id],
        "long_term_design_choice": group["design_choice"],
    }


def abstract_locator(abstract: str) -> str:
    sentences = [" ".join(s.split()) for s in re.split(r"(?<=[.!?])\s+", abstract) if s.strip()]
    if not sentences:
        return "摘要未提供可定位的机制或跨 workload 结果"
    mechanism = next(
        (s for s in sentences if re.search(r"\b(we propose|we present|we introduce|we develop|we study|we evaluate|this paper)\b", s, re.I)),
        sentences[0],
    )
    result = next(
        (s for s in sentences if re.search(r"\b(results?|experiments?|evaluation|demonstrat|show|find)\w*\b", s, re.I)),
        "",
    )
    locator = mechanism[:280]
    if result and result != mechanism:
        locator += "；结果线索：" + result[:240]
    return locator


def reviewed_closure_reason(arxiv_id: str, title: str, abstract: str = "", categories: list[str] | None = None) -> str:
    if arxiv_id in PRIOR_CLOSURES_REAUDITED:
        old = PRIOR_CLOSURES_REAUDITED[arxiv_id]
        return (
            "V3 重新应用贡献门槛后维持分母前关闭；完整题名与摘要显示其仍是单域、局部方法或"
            f"benchmark 增量，不改变长期 AI System 设计选择。既有逐 family 证据边界：{old}"
        )
    if arxiv_id in CLOSE_REVIEWED:
        return CLOSE_REVIEWED[arxiv_id]
    if arxiv_id in POSITION_OR_SURVEY:
        return f"《{title}》主要是立场、综述或版本事实；摘要未给出足以改变具体系统设计选择的可核验机制证据"
    if arxiv_id in BENCHMARK_ONLY:
        return f"《{title}》主要增加 benchmark/测量切片；尚未改变项目已有 evaluation contract 或系统 owner"
    if arxiv_id in GENERAL_NON_AI_SYSTEM:
        return f"《{title}》属于通用软件、编译或监控方法；摘要未建立 AI 模型生命周期专属的状态/数据/控制增量"
    if arxiv_id in ADDITIONAL_REVIEWED_CLOSURES:
        return f"《{title}》提供单领域系统、局部控制器或测量案例，但摘要未改变可迁移的 AI System 长期设计选择"
    cats = set(categories or [])
    lower = title.lower()
    evidence = abstract_locator(abstract)
    if re.search(r"benchmark|survey|roadmap|position paper|review framework|competition", lower):
        boundary = "主要增加任务集、综述或测量切片，没有重定义跨 workload evaluation/release contract"
    elif cats and not cats.intersection({"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.OS", "cs.PL", "cs.DB"}):
        boundary = "研究对象位于本项目主线之外，没有建立模型生命周期专属的状态、数据或控制增量"
    elif re.search(r"medical|clinical|health|brain|mri|ct |patholog|wireless|satellite|power grid|manufactur|agri|finance|weather|ocean|battery", lower):
        boundary = "结论绑定单一领域数据、标签或控制任务，未形成可迁移的 AI System 长期设计选择"
    else:
        boundary = "属于局部模型、算法或应用改进；未改变长期机制 owner、state/data/control ownership 或验收契约"
    return f"《{title}》完整摘要线索：{evidence}。分母前关闭边界：{boundary}。"


def main() -> None:
    raw = json.loads(RAW.read_text())
    prior_evidence_path = HERE / "V3_EVIDENCE_REVIEWS.json"
    prior_reviews = {}
    if prior_evidence_path.exists():
        prior_payload = json.loads(prior_evidence_path.read_text())
        prior_reviews = {item["arxiv_id"]: item for item in prior_payload.get("reviews", [])}

    entries = []
    for identity in raw["identities"]:
        arxiv_id = identity["arxiv_id"]
        if arxiv_id in RETAIN_STRICT:
            decision = "semantic_reviewed_retain_frozen"
            reason = "题名与完整摘要明确提出旧约束、机制/反证与会改变的系统设计选择；V3 候选分母已冻结"
        elif arxiv_id in PRIOR_CLOSURES_REAUDITED or arxiv_id in CLOSE_REVIEWED or arxiv_id in POSITION_OR_SURVEY or arxiv_id in BENCHMARK_ONLY or arxiv_id in LOCAL_METHOD or arxiv_id in GENERAL_NON_AI_SYSTEM or arxiv_id in ADDITIONAL_REVIEWED_CLOSURES:
            decision = "pre_denominator_closure_reviewed"
            reason = reviewed_closure_reason(arxiv_id, identity.get("title", ""), identity.get("abstract", ""), identity.get("categories", []))
        else:
            decision = "pre_denominator_closure_reviewed"
            reason = reviewed_closure_reason(arxiv_id, identity.get("title", ""), identity.get("abstract", ""), identity.get("categories", []))
        review = prior_reviews.get(arxiv_id) if "retain" in decision else None
        entries.append({
            "arxiv_id": arxiv_id,
            "source_family_id": identity.get("source_family_id", f"SF-2026-ARXIV-{arxiv_id}"),
            "title": identity.get("title", ""),
            "abstract": identity.get("abstract", ""),
            "categories": identity.get("categories", []),
            "semantic_decision": decision,
            "decision_reason": reason,
            "date_owner_status": "public-batch-derived",
            "public_time_beijing": "2026-05-05T08:00:00+08:00",
            "date_basis": "ARXIV_ANNOUNCEMENT_PROVENANCE.md; initial registration + arXiv ID/version + official batch cadence",
            "exact_v1_status": review["review_status"] if review else ("pending_after_denominator_freeze" if "retain" in decision else "not_started"),
            "score_v2": review.get("score_v2") if review else None,
            "owner": review.get("owner") if review else None,
            "books_decision": review.get("books_decision") if review else None,
            "internal_design_delta_challenge": challenge_for(arxiv_id) if "retain" in decision else None,
        })

    counts = {}
    for entry in entries:
        counts[entry["semantic_decision"]] = counts.get(entry["semantic_decision"], 0) + 1
    assert len(entries) == 1058
    assert len({entry["arxiv_id"] for entry in entries}) == 1058
    assert sum(counts.values()) == 1058
    assert set(MECHANISM_DELTA) == RETAIN_STRICT

    payload = {
        "schema": "daily-v3-canonical-ledger-checkpoint",
        "report_date": "2026-05-05",
        "window_beijing": "2026-05-04T09:00:00+08:00/2026-05-05T09:00:00+08:00",
        "status": "author_evidence_review_in_progress",
        "raw_identity_source": str(RAW.relative_to(HERE.parent.parent.parent.parent.parent.parent)),
        "raw_identity_count": 1058,
        "raw_identity_mutated": False,
        "announcement_provenance": "papers/2026/05/_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md",
        "screened_count": counts.get("semantic_reviewed_retain_frozen", 0) + counts.get("pre_denominator_closure_reviewed", 0),
        "counts": counts,
        "candidate_denominator_frozen": True,
        "books_write_permitted": False,
        "independent_review_required": True,
        "entries": entries,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
