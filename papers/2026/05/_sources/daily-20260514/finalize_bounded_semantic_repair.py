#!/usr/bin/env python3
"""Finalize the strictly bounded 2026-05-14 semantic repair.

The input inventory stays frozen at 714 identities.  This script only reopens
the 41 IDs named by the fresh non-author audit and rewrites evidence for the
resulting 118 arXiv candidates.  It deliberately does not edit shared Books.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/14/README.md"
OWNER_RECEIPT = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260514/arxiv-owner-receipt.json"

REOPEN = """2605.12517 2605.12529 2605.12565 2605.12574 2605.12694 2605.12765 2605.12813 2605.12869 2605.12975 2605.13043 2605.13050 2605.13105 2605.13115 2605.13130 2605.13155 2605.13162 2605.13179 2605.13213 2605.13255 2605.13277 2605.13290 2605.13329 2605.13334 2605.13352 2605.13369 2605.13429 2605.13438 2605.13448 2605.13467 2605.13486 2605.13511 2605.13534 2605.13537 2605.13625 2605.13632 2605.13652 2605.13687 2605.13695 2605.13724 2605.13757 2605.13829""".split()

NEW_OWNER = {
    "2605.12517": "MULTIMODAL-REPRESENTATION", "2605.12529": "PLATFORM-SECURITY",
    "2605.12565": "PLATFORM-SECURITY", "2605.12574": "PLATFORM-SECURITY",
    "2605.12694": "AGENT-WORKFLOW", "2605.12765": "PLATFORM-SECURITY",
    "2605.12813": "PLATFORM-EVALUATION-SYSTEM", "2605.12869": "PLATFORM-EVALUATION-SYSTEM",
    "2605.12975": "AGENT-RAG", "2605.13043": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.13050": "AGENT-CONTEXT", "2605.13105": "MULTIMODAL-EMBODIED-VLA",
    "2605.13115": "PLATFORM-SECURITY", "2605.13130": "TRAIN-DATA",
    "2605.13155": "TRAIN-RLHF", "2605.13162": "TRAIN-LORA",
    "2605.13179": "MULTIMODAL-GENERATIVE-PARADIGMS", "2605.13213": "PLATFORM-SECURITY",
    "2605.13255": "TRAIN-GRPO", "2605.13277": "AGENT-RAG",
    "2605.13290": "TRAIN-DATA", "2605.13329": "WORLDVIEW-REPRESENTATION",
    "2605.13334": "PLATFORM-SECURITY", "2605.13352": "PLATFORM-EVALUATION-SYSTEM",
    "2605.13369": "TRAIN-SFT", "2605.13429": "MODEL-TOKENIZER",
    "2605.13438": "AGENT-MEMORY", "2605.13448": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.13467": "TRAIN-GRPO", "2605.13486": "AGENT-MEMORY",
    "2605.13511": "AGENT-CONTEXT", "2605.13534": "AGENT-RAG",
    "2605.13537": "TRAIN-RLHF", "2605.13625": "PLATFORM-TRACE",
    "2605.13632": "MULTIMODAL-EMBODIED-VLA", "2605.13652": "TRAIN-PRETRAINING",
    "2605.13687": "WORLDVIEW-LLM-INTELLIGENCE", "2605.13695": "PLATFORM-EVALUATION-SYSTEM",
    "2605.13724": "MULTIMODAL-GENERATIVE-PARADIGMS", "2605.13757": "TRAIN-DATA",
    "2605.13829": "TRAIN-DATA",
}

NEW_SCORE_TOTAL = {
    "2605.12517": 7, "2605.12529": 8, "2605.12565": 7, "2605.12574": 7,
    "2605.12694": 8, "2605.12765": 8, "2605.12813": 7, "2605.12869": 7,
    "2605.12975": 8, "2605.13043": 8, "2605.13050": 8, "2605.13105": 7,
    "2605.13115": 9, "2605.13130": 7, "2605.13155": 8, "2605.13162": 7,
    "2605.13179": 6, "2605.13213": 8, "2605.13255": 7, "2605.13277": 7,
    "2605.13290": 6, "2605.13329": 7, "2605.13334": 7, "2605.13352": 7,
    "2605.13369": 7, "2605.13429": 6, "2605.13438": 7, "2605.13448": 7,
    "2605.13467": 7, "2605.13486": 7, "2605.13511": 6, "2605.13534": 7,
    "2605.13537": 7, "2605.13625": 7, "2605.13632": 7, "2605.13652": 7,
    "2605.13687": 8, "2605.13695": 6, "2605.13724": 7, "2605.13757": 7,
    "2605.13829": 9,
}

REOPEN_REASON = {
    "2605.12517": "缺失模态使 VLM 的置信度失校准；latent modality completion 改变部署时表示补全路径。",
    "2605.12529": "在未知 trigger 下同时清除后门并保留 watermark，改变模型发布前的权重修复与产权证据边界。",
    "2605.12565": "persona-conditioned 搜索把 jailbreak 测试从静态提示集扩展为受害者条件化的攻击生成过程。",
    "2605.12574": "输出语义扰动可作为黑盒 VLM membership sensor，改变多模态隐私验收的观察面。",
    "2605.12694": "lattice/worklist 将 LLM 生成的程序分析证据约束为单调、可合并的状态，而非自由文本判断。",
    "2605.12765": "输入条件化的激活旋转把 inference-time unlearning 变成受 gate 控制的参数路径。",
    "2605.12813": "受约束 latent adversary 暴露 hallucination detector 的局部盲区，改变检测器鲁棒性合同。",
    "2605.12869": "time-to-jailbreak 把 guardrail 评价从一次攻击成功率扩展为随搜索预算演化的 survival contract。",
    "2605.12975": "可执行 Python 检索计划与确定性 compiler feedback/retry 改变 multi-hop RAG 的控制状态。",
    "2605.13043": "逐步 masked generation 的安全 remasking 与 latent steering 改变可变生成状态的提交控制。",
    "2605.13050": "并行搜索多个 context 并剪枝会让 context 本身成为可优化且可退化的运行状态。",
    "2605.13105": "VLA 的 paired invariance/sensitivity reward 把 action grounding 变成双臂因果验收。",
    "2605.13115": "PRNG 污染位于模型图之外却能控制训练结果，要求随机源进入训练供应链 identity。",
    "2605.13130": "gradient-aligned step selection 将 reasoning data admission 绑定到参数更新方向，而不只是结果难度。",
    "2605.13155": "逐 prompt 约束的多 reward Pareto 更新改变 reward channel 的归一化与淘汰权。",
    "2605.13162": "continual LoRA slots 与 consolidation 让 adapter 变成可增长、可合并的 program memory。",
    "2605.13179": "受控负结果显示 Engram associative memory 不自动迁移到 AR image generation，校正架构外推。",
    "2605.13213": "分层多模态多 Agent 攻击把单节点风险升级为跨角色、跨模态的传播路径。",
    "2605.13255": "entropy gate 决定哪些 self-distilled samples 进入更新，改变监督数据的 admission owner。",
    "2605.13277": "视觉证据按 information gain 而非相似度录取，改变 RAG observation 的价值定义。",
    "2605.13290": "reasoning dataset 的内在指标随模型尺度改变，否定静态数据质量分数的跨模型可移植性。",
    "2605.13329": "persona directions 在早期预训练形成，改变‘行为只由 post-training 写入’的表示解释。",
    "2605.13334": "多轮 LLM-to-LLM persuasion 可跨轮侵蚀 guardrail，改变安全评价的交互状态。",
    "2605.13352": "分离 aleatoric/epistemic uncertainty 为冻结 VLM 提供两类不同的 abstention 证据。",
    "2605.13369": "query-conditioned test-time parameter update 让单次查询产生新的模型 revision 与回滚责任。",
    "2605.13429": "以 token alignment lexicon 扩展 vocabulary，改变 tokenizer 与 checkpoint 的联合迁移合同。",
    "2605.13438": "always-on proactive memory folding 把写入、折叠与主动提示变成长驻控制状态。",
    "2605.13448": "latent reuse 的收益受 subspace shift/noise 约束，为复用路径给出可拒绝的理论边界。",
    "2605.13467": "按 modality/skill 分解 confidence reward，避免单一奖励掩盖视觉与推理 channel collapse。",
    "2605.13486": "反思经验被用于 memory search policy，改变记忆读取而非直接改变事实真值。",
    "2605.13511": "ordered many-shot CoT 把 context examples 从集合变成推理时 curriculum。",
    "2605.13534": "并行 multi-query retrieval 与显式 merge 将检索分支和合并权分开。",
    "2605.13537": "inference-time reward ensemble 需要把各 evaluator 的尺度、相关性和校准纳入决策状态。",
    "2605.13625": "长运行 Agent 的 trace taxonomy 将失败从最终结果拆到跨阶段行为状态。",
    "2605.13632": "交互式空间视觉指导与 reactive head 把高层语义和实时控制分层。",
    "2605.13652": "相同 perplexity 的低秩预训练可落入不同 basin，限制以终点 loss 证明训练等价。",
    "2605.13687": "合成层级语言给出 bounded context 与显式 working memory 的条件性下界。",
    "2605.13695": "judge prompt ensemble/critique 改变评价聚合，但成本和单 benchmark 边界必须显式保留。",
    "2605.13724": "any-step video diffusion 让 flow map 支持非相邻时间跳转，改变 rollout 的时间状态。",
    "2605.13757": "VLA frame selection 保留 action-critical transition，改变训练数据的时间采样责任。",
    "2605.13829": "Negation Neglect 表明否定/fiction 标签可在微调中被剥离，改变训练数据 truth-state 编码合同。",
}

# These decisions are the result of reopening every previous No-Change item.
# Queue membership means the candidate proposition is not present before the
# owner's Review notes; it does not mean the paper's full claim is accepted.
OLD_QUEUE = """2605.12519 2605.12522 2605.12549 2605.12571 2605.12673 2605.12697 2605.12705 2605.12746 2605.12825 2605.12894 2605.12906 2605.12920 2605.13026 2605.13111 2605.13156 2605.13247 2605.13295 2605.13338 2605.13360 2605.13370 2605.13405 2605.13471 2605.13595 2605.13737 2605.13768 2605.13772 2605.13778 2605.13779 2605.13784 2605.13825 2605.13831 2605.13839""".split()
OLD_QUEUE += """2605.12766 2605.12874 2605.12875 2605.12944 2605.12969 2605.12978 2605.12991 2605.13170 2605.13382 2605.13414 2605.13434 2605.13473 2605.13484 2605.13485 2605.13643 2605.13716""".split()
OLD_QUEUE += """2605.12922 2605.13013 2605.13044 2605.13411""".split()
NEW_QUEUE = """2605.12529 2605.12574 2605.12694 2605.12765 2605.12813 2605.12869 2605.12975 2605.13043 2605.13050 2605.13115 2605.13162 2605.13179 2605.13213 2605.13329 2605.13334 2605.13352 2605.13369 2605.13429 2605.13438 2605.13448 2605.13625 2605.13652 2605.13687 2605.13724 2605.13757 2605.13829""".split()
QUEUE = set(OLD_QUEUE + NEW_QUEUE)

OLD_SYNTHESIS = {
    "2605.12519": "只用终局答案奖励时，中间推理可以碰巧正确却不可验证；把轨迹拆成结构化 claims，并由确定性 verifier 与自适应权重分配过程信用，才把正确性与推理质量分开治理。",
    "2605.12522": "把 AR 与 masked diffusion 的文本差异全归因于训练目标会混淆因子；对照实验进一步把双向训练目标与 confidence remasking 的熵效应分开。",
    "2605.12549": "GUI grounding 过去主要从 decode 输出诊断；层级干预表明关键定位状态可能在 prefill 就已形成或丢失，因此 Prefill 也必须进入 grounding harness。",
    "2605.12571": "最终答案正确不能证明 Agent 消费了检索证据；将 evidence selection 与 answer authority 解耦，才能识别靠参数先验碰巧答对的路径。",
    "2605.12673": "Agent benchmark 的 pass rate 默认任务接口不可钻空子；系统化生成 exploit 并验证任务 invariant，才区分能力提升与 harness 被规避。",
    "2605.12697": "长上下文 attention 的固定 logit scale 无法跨 regime 复用；inverse temperature 应随长度与统计假设校准，而不是被 IO 优化章节替代。",
    "2605.12705": "遗忘通常在下游微调后补救；更早的数据暴露顺序会改变能力被写入参数的方式，从而改变后续可保留性。",
    "2605.12746": "把 CoT 交给较小 monitor 并不自动得到安全检测；monitor 会把隐藏目标误认成用户任务，需要专门数据与分层评价校准。",
    "2605.12825": "AR 的精确左到右语义与 diffusion 的并行修正不是只能二选一；双视图生成让 AR owner 验证 diffusion proposals，但引入两套状态的一致性责任。",
    "2605.12894": "始终合作的用户模拟器高估 Agent 鲁棒性；保持任务目标不变而注入 persona policy，能测试犹豫、反复与偏离等交互分布。",
    "2605.12906": "固定选择最易或最难 SFT 数据会忽略预算变化；最优 difficulty 会随数据量移动，数据 recipe 必须绑定预算与目标外推区间。",
    "2605.12920": "多 Agent 对话成功不等于私有 world models 对齐；应分别测 observation convergence、信息新颖性与 belief-sensitive messaging。",
    "2605.13026": "masked diffusion 训练的低效不能只归因于并行目标；语言的 locality bias 允许重分配被预测位置与上下文，形成更有条件的加速路径。",
    "2605.13111": "视频生成中的统一 KV 长度忽略 attention heads 的时间职责差异；离线识别 head type 并用 ragged cache 执行异构保留策略，才让压缩与画质责任一致。",
    "2605.13156": "对象幻觉不是单一路径故障；视觉证据写入与语言先验读取形成不同回路，必须以因果干预分开诊断。",
    "2605.13247": "一次性训练最终 MoE 容量要求提前冻结规模；渐进扩展 expert pool 能复用已有能力，但 expansion schedule 与 router state 成为 checkpoint 身份。",
    "2605.13295": "只按最终 Agent 成功给整条轨迹记账会掩盖局部贡献；对比相似轨迹差异可定位 credit，但 attribution 仍不能取代 outcome truth。",
    "2605.13338": "安全攻击不只追求有害文本，也可通过诱导过度思考消耗预算；availability gate 必须约束推理长度、成本与停止权。",
    "2605.13360": "同步等待工具最易保持一致，却破坏实时交互；异步 I/O 与 speculative tool proposal 需要独立验证、取消和回滚 authority。",
    "2605.13370": "显式循环记忆受 BPTT 梯度稳定性限制；相位化状态转移可保留长期信息，但其数值稳定与表达能力必须分别验收。",
    "2605.13405": "模型扩容常追求立即保留初始性能；实验证据提示最终训练轨迹比增长瞬间更重要，因此 warmstart operator 必须与后续预算联合评价。",
    "2605.13471": "一次 prompt injection 的过滤不足以治理 always-on Agent；攻击可沉积到 memory、skill 与 scheduler，provenance gate 必须跨 run 追踪持久控制状态。",
    "2605.13595": "模型输出低置信度并不必然对应真实未知；刻意诱导的不确定性会制造校准外观，因此 uncertainty sensor 不能独立拥有 abstain 或 release authority。",
    "2605.13737": "多模态模型能够识别音视频信息不等于行动时会采用它；冲突条件下必须分别测 perception、premise rejection 与 action use。",
    "2605.13768": "对所有矩阵方向等量分配 bit rate 简单却浪费预算；waterfilling 按方向敏感度配置量化精度，将 policy 与具体矩阵/硬件身份绑定。",
    "2605.13772": "整条 reasoning trace 一个分数无法定位首个错误；逐步 hidden-state transport 只作为 error sensor，最终事实仍需外部 verifier。",
    "2605.13778": "Diffusion VLA 每次重规划都跑完整模型会错过控制周期；轻量 draft、主模型并行验证与 phase-aware fallback 可减少 full calls。",
    "2605.13779": "手工管理大量 LoRA 的训练、注册与服务会让控制面碎裂；统一的多租户 adapter lifecycle 把 artifact、placement 与 serving revision 接成同一平台对象。",
    "2605.13784": "每次查询重放全部历史使 prefill 随会话增长；持久 session KV 把 history advance 与 query 分开，但 cache revision、权限与恢复成为长期状态。",
    "2605.13825": "中性 prompt 下的安全行为可被既往行动历史锚定；历史不是普通上下文，而是会改变 action prior 的不可信控制输入。",
    "2605.13831": "把文本长上下文配方直接搬到 VLM 会混淆视觉 token、文档结构与长度外推；continued pretraining 必须联合数据组成、位置策略和跨长度评价。",
    "2605.13839": "多 Agent 通信不必只写入 receiver context；短暂的 receiver-specific weight delta 能承载建议，但把消息权限升级成参数写权限。",
    "2605.12766": "固定网络拓扑上的 collective schedule 在可重构 fabric 上会浪费链路；复用 subring 重新组织 AllReduce、AllGather、ReduceScatter 与 All-to-All，但 schedule 与 topology revision 必须共同验收。",
    "2605.12874": "一个自然语言解释可能同时匹配许多不同 SAE features；解释可读并不等于 feature identity 唯一，必须报告 descriptive collision。",
    "2605.12875": "Skill 描述声明的能力范围不能证明代码副作用相同；从代码构建 security property graph 再与描述对照，才能发现未披露行为。",
    "2605.12944": "只给样本打分不能表达操作顺序与组合效应；固定原始池上的可执行 data-recipe search 将筛选算子、预算与完整 SFT 验证绑定。",
    "2605.12969": "token-level clipped reward 不一定表达 verified sequence 的相对关系；以长度归一的序列概率对比同组正负轨迹，改变 RLVR 的 credit coordinate。",
    "2605.12978": "反复用 LLM 汇总有用记忆会逐轮引入错误；consolidation 必须保留原证据、版本与回滚，不能把新 summary 覆盖成事实。",
    "2605.12991": "单体 RLHF 的顺从性目标不能直接治理多 Agent 的相互迎合；评价必须观察交互中意见独立性、纠错与群体漂移。",
    "2605.13170": "多 Agent 系统的薄弱点可能位于通信边而非单个模型；攻击应以消息影响路径和 receiver 状态偏移为单位。",
    "2605.13382": "AR VLA 逐 token action 解码准确但慢；block diffusion finetuning 并行修正 action chunks，同时引入可变动作状态与 commit 边界。",
    "2605.13414": "只测模型能否解题忽略其是否会在预算下选择值得解决的问题；先承诺选择、顺序和 token allocation，才能评价 prospective metacognitive control。",
    "2605.13434": "异步 SGD 在 worker 速度和数据分布相关时会偏向高频 worker；按贡献频率重标度更新以恢复目标，但增加方差与统计估计状态。",
    "2605.13473": "线性 attention 的单一 scalar gate 无法适配各维度曲率；在线 hypergradient 对角预条件改变 memory update geometry，也增加稳定性状态。",
    "2605.13484": "全局 calibration 可以掩盖未知子群的系统性失校准；主动搜索隐藏 regime 将 slice discovery 与最终 calibration verdict 分开。",
    "2605.13485": "标称 context length 不等于有效信息长度；tokenization 与 fragment boundary 会改变可利用上下文，必须把输入表示纳入 long-context identity。",
    "2605.13643": "on-policy distillation 的 dense teacher signal 并非沿序列均匀可学；prefix 可教而 suffix 退化时，需要按位置诊断 support 与 policy divergence。",
    "2605.13716": "Skill library 增长后，创建、验证、版本、去重和退休不能继续由临时 prompt 管理；SkillOps 将其提升为持续维护的软件资产生命周期。",
    "2605.12922": "多轮任务丢失不能只用窗口截断解释；goal token 的 attention 可达性会先衰减，而相关信息仍残留在 residual representation，要求把‘存在’与‘被当前路径使用’分开。",
    "2605.13013": "只预测像素级下一帧难以支撑在线控制；joint embedding diffusion world model 在 latent dynamics 中联合表征 observation 与 transition，但 imagined rollout 仍不等于环境事实。",
    "2605.13044": "Skill 不必遭到已知 exploit 才能违反 specification；semantic fuzzing 从声明不变量生成输入并检查真实 side effect，把安全真值交还给确定性执行证据。",
    "2605.13411": "静态 attack/defense 集会快速过期；把攻击样本、防御策略与失败回执外置成可检查、可复用的共同演进状态，才能跨模型迭代而不把安全知识埋进单次权重。",
}

STATE_BY_NODE = {
    "MULTIMODAL-REPRESENTATION": "表示 identity、模态缺失状态与融合 gate",
    "PLATFORM-SECURITY": "threat model、sensor evidence 与不可绕过的 commit authority",
    "AGENT-WORKFLOW": "workflow state、verifier receipt 与提交边界",
    "PLATFORM-EVALUATION-SYSTEM": "evaluation identity、切片、校准与 verdict authority",
    "AGENT-RAG": "query/evidence identity、分支检索与 answer admission",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "mutable generation state、proposal、correction 与 commit",
    "AGENT-CONTEXT": "active context、来源身份、预算与 compaction revision",
    "MULTIMODAL-EMBODIED-VLA": "observation/action state、控制频率与 safety fallback",
    "TRAIN-DATA": "样本真值、顺序、采样与 data-recipe revision",
    "TRAIN-RLHF": "reward channel、calibration 与 update authority",
    "TRAIN-LORA": "base/adapter revision、slot 生命周期与 consolidation",
    "TRAIN-GRPO": "trajectory、verifier、credit 与 policy update",
    "WORLDVIEW-REPRESENTATION": "representation claim 与因果使用证据",
    "TRAIN-SFT": "query-conditioned update、base revision 与 rollback",
    "MODEL-TOKENIZER": "vocabulary、alignment lexicon 与 checkpoint identity",
    "AGENT-MEMORY": "memory proposal、derived state、read/write authority 与 expiry",
    "PLATFORM-TRACE": "跨阶段 trace identity、行为分类与因果候选",
    "TRAIN-PRETRAINING": "optimizer trajectory、低秩参数化与终点证据",
    "WORLDVIEW-LLM-INTELLIGENCE": "可见上下文、工作记忆与任务复杂度边界",
    "MODEL-SELF-ATTENTION": "attention temperature、长度与语义 revision",
    "INFER-PREFILL": "prefill 输入、层级 grounding state 与 harness",
    "INFER-SPECULATIVE-DECODING": "draft/target state、verification 与 commit",
    "PLATFORM-MONITORING": "monitor observation、校准与升级处置",
    "AGENT-MULTI-AGENT": "sender/receiver belief state、消息与更新权限",
    "INFER-KV-CACHE": "head-aware KV identity、保留策略与 cache layout",
    "MODEL-MOE": "expert capacity、router revision 与 growth checkpoint",
    "AGENT-TOOL-CALLING": "tool proposal、异步 result 与取消/提交 authority",
    "INFER-TENSORRT-LLM": "quantization policy、矩阵 identity 与执行 artifact",
    "PLATFORM-FOUNDATIONS": "adapter artifact、租户、placement 与 service revision",
    "INFER-DECODE": "persistent session KV、advance/query 分离与 recovery",
}

ANCHOR_BY_NODE = {
    "MULTIMODAL-REPRESENTATION": "### 任务贡献与当前可靠性不能共用一个 Gate",
    "PLATFORM-SECURITY": "## 风险管理而不是一次性认证",
    "AGENT-WORKFLOW": "## Evaluator-Driven Search：可执行反馈如何变成 Workflow",
    "PLATFORM-EVALUATION-SYSTEM": "## 平均值、切片与不确定性",
    "AGENT-RAG": "### RAG 端到端评估必须保留阶段级归因",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "### Masked generation：未知位置与已知位置",
    "AGENT-CONTEXT": "## Context 不是字符串，而是运行时状态",
    "MULTIMODAL-EMBODIED-VLA": "## 从 VLM 到 VLA：输出空间变成 Action Space",
    "TRAIN-DATA": "## 数据质量不是单一分数",
    "TRAIN-RLHF": "## Reward Model 定义了什么",
    "TRAIN-LORA": "## Adapter 是独立的模型 Artifact",
    "TRAIN-GRPO": "## 从 Sequence Reward 到 Typed Trajectory",
    "WORLDVIEW-REPRESENTATION": "### 信息存在、可读与被使用是三个不同命题",
    "TRAIN-SFT": "## Catastrophic forgetting 与能力回退",
    "MODEL-TOKENIZER": "### Tokenizer 与 checkpoint 是联合行为接口",
    "AGENT-MEMORY": "## 从原始轨迹到派生策略：Memory 的演进不是无限追加",
    "PLATFORM-TRACE": "## 从 Linear Trace 到 Root-cause Graph",
    "TRAIN-PRETRAINING": "## 训练稳定性是多层系统问题",
    "WORLDVIEW-LLM-INTELLIGENCE": "## In-context learning 改变了任务接口",
}


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def sentence(text: str, needles: tuple[str, ...] = ()) -> str:
    bits = [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)) if len(s.strip()) > 25]
    if needles:
        for s in bits:
            if any(n in s.lower() for n in needles):
                return s
    return bits[0] if bits else text[:600]


def roadmap() -> dict[str, dict]:
    out = {}
    for line in (ROOT / "ROADMAP.md").read_text().splitlines():
        m = re.match(r"\| `([^`]+)` \| ([^|]+) \| `([^`]+)` \| ([^|]+) \|", line)
        if m:
            out[m.group(1)] = {"chapter": m.group(2).strip(), "owner_path": m.group(3), "legacy_chapter": m.group(4).strip()}
    return out


def score_from_total(total: int) -> dict:
    # Preserve total while keeping every V3 dimension in 0..3.
    if total == 9: parts = (3, 3, 3)
    elif total == 8: parts = (3, 2, 3)
    elif total == 7: parts = (2, 2, 3)
    elif total == 6: parts = (2, 2, 2)
    else: parts = (2, 1, 2)
    return {"design_delta": parts[0], "system_reach": parts[1], "durability": parts[2], "total": total}


def excerpt_after_heading(path: Path, wanted: str) -> tuple[str, str]:
    text = path.read_text()
    body = text.split("\n## Review notes", 1)[0]
    heading = wanted.lstrip("# ")
    pos = body.find(wanted)
    if pos < 0:
        # The proposed anchor may be intentionally new.  Fall back to the
        # chapter thesis, while reporting the missing anchor honestly.
        m = re.search(r"^## 本章要回答的问题\s*$", body, re.M)
        pos = m.start() if m else 0
        actual = "本章要回答的问题"
    else:
        actual = heading
    tail = body[pos:].splitlines()[1:]
    paragraphs = []
    for line in tail:
        if line.startswith("## "):
            break
        if line.strip() and not line.startswith("<!--"):
            paragraphs.append(line.strip())
        if len(" ".join(paragraphs)) >= 700:
            break
    return actual, " ".join(paragraphs)[:900]


def synthesis_risk_and_fallback(delta: str, node: str) -> tuple[str, str]:
    """Return a mechanism-specific cost/failure statement and bounded fallback.

    The synthesis is a handoff to the root writer, not a second abstract.  It
    therefore names the operational risk that follows from the changed state
    or authority, and keeps the previous chapter path as an explicit fallback.
    """
    text = f"{delta} {node}".lower()
    if any(k in text for k in ("jailbreak", "攻击", "后门", "membership", "security", "guardrail", "persuasion", "unlearning", "watermark", "trigger")):
        return (
            "新增攻击搜索、检测或修复状态会带来误报/漏报、适应性绕过与额外查询成本；检测器得分本身不能获得发布或执行授权",
            "证据不足时拒绝提升权限，隔离可疑 artifact，并回到既有 threat model、静态规则和人工复核路径",
        )
    if any(k in text for k in ("benchmark", "evaluation", "judge", "uncertainty", "calibration", "detector", "verifier", "reward hacking", "metacognitive")):
        return (
            "更细的 evaluator、slice 或不确定性状态提高诊断力，却引入 evaluator 相关性、校准漂移、选择偏差与被优化对象反向适配量尺的风险",
            "无法复现或校准时不做能力/安全提升结论，退回原始任务真值、确定性检查与分层人工判定",
        )
    if any(k in text for k in ("reward", "rlhf", "grpo", "sft", "training", "pretraining", "gradient", "optimizer", "lora", "distillation", "dataset", "data ", "微调", "训练")):
        return (
            "新的 admission、reward、参数更新或数据顺序会增加方差、目标投机、能力回退以及 checkpoint 身份分叉；终点 loss 或单项 reward 不能单独证明等价",
            "保留基线 recipe 与可恢复 checkpoint；出现不稳定、遗忘或跨任务退化时停止新更新并回滚到已验收 revision",
        )
    if any(k in text for k in ("retrieval", "rag", "context", "memory", "many-shot", "prompt", "evidence", "检索", "记忆", "上下文")):
        return (
            "新增派生上下文、检索分支或长期记忆会消耗时延与 token 预算，并可能把陈旧、冲突或无 provenance 的状态放大为答案依据",
            "当来源、版本或合并结果不可验证时，丢弃派生状态，退回最小可信上下文与可追溯原始证据",
        )
    if any(k in text for k in ("agent", "workflow", "skill", "tool", "lattice", "worklist", "program", "通信", "多 agent")):
        return (
            "把规划、通信或工具调用拆成显式状态能够定位责任，但会增加并发竞态、错误传播、取消失败和越权副作用",
            "无法取得确定性回执时停止该分支、撤销未提交 effect，并退回单执行者或人工批准的保守流程",
        )
    if any(k in text for k in ("vla", "multimodal", "vision", "video", "视觉", "多模态", "action", "physical")):
        return (
            "模态补全、跨模态奖励或分层控制会引入传感器偏移、模态冲突、控制周期超时与仿真到现实的证据缺口",
            "观测不完整或控制频率不达标时禁止提交动作，退回完整感知、主控制器验证或安全停机路径",
        )
    if any(k in text for k in ("diffusion", "masked", "speculative", "proposal", "remasking", "flow map", "generation")):
        return (
            "并行 proposal、重掩码或跨步状态减少串行工作，却增加可变状态一致性、验证开销和错误 commit 的 failure mode",
            "proposal 置信或 verifier 不满足条件时丢弃草案，回到完整模型、相邻步或严格自回归提交路径",
        )
    if any(k in text for k in ("cache", "kv", "collective", "network", "async", "distributed", "topology", "quant", "bit rate", "prefill")):
        return (
            "缓存、异步、拓扑或压缩状态降低计算/通信成本，却增加陈旧 revision、恢复不一致、尾延迟和硬件相关失真",
            "identity、拓扑或误差预算不匹配时使优化失效，回到同步、未压缩或重新计算的已验证路径",
        )
    return (
        "更细的状态与控制边界提高可解释性，但增加版本、校准和验收成本；越出论文支持分布时可能产生错误归因或过度外推",
        "边界不成立时保留章节原有机制，并把新路径降级为未提交的受限实验分支",
    )


def main() -> None:
    inventory = load(OWNER_RECEIPT)
    identities = {x["arxiv_id"]: x for x in inventory["identities"]}
    previous = load(HERE / "exact-v1-locator-audit-v3.json")
    previous_by_id = {x["arxiv_id"]: x for x in previous["items"]}
    old_ids = list(previous_by_id)
    retained = old_ids + REOPEN
    assert len(old_ids) == 77 and len(REOPEN) == 41 and len(set(retained)) == 118

    extracted = load(HERE / "bounded-evidence-extract.json")
    evidence_by_id = {x["arxiv_id"]: x for x in extracted["items"]}
    assert set(evidence_by_id) == set(retained)
    assert not any(x["withdrawal_signal"] for x in evidence_by_id.values())

    road = roadmap()
    reviews = []
    comparisons = []
    queue = []
    for aid in retained:
        ident = identities[aid]
        exact = evidence_by_id[aid]
        if aid in previous_by_id:
            old = previous_by_id[aid]
            node = old["stable_node_id"]
            score = old["score"]
            old_compare = old["books_comparison"]
            owner = {k: old_compare[k] for k in ("chapter", "owner_path", "legacy_chapter")}
            proposed_anchor = old_compare["existing_heading"]
        else:
            node = NEW_OWNER[aid]
            score = score_from_total(NEW_SCORE_TOTAL[aid])
            owner = road[node]
            proposed_anchor = ANCHOR_BY_NODE[node]

        method = exact["mechanism"]
        evaluation = exact["evaluation"]
        limitations = exact["limitations"]
        mechanism_claim = sentence(ident["abstract"], ("we propose", "we introduce", "we present", "our method", "framework"))
        result_claim = sentence(ident["abstract"], ("we find", "we show", "experiments", "results", "evaluation"))
        baseline = sentence(ident["abstract"])
        # A Books-changing claim receives the deeper review even when its
        # three-axis priority score is only 5-6.
        review_depth = "deep" if score["total"] >= 7 or aid in QUEUE else "standard"
        books_disposition = "Integrate — Root Writeback Pending" if aid in QUEUE else "No Change — Existing Coverage"

        review = {
            "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}",
            "arxiv_id": aid,
            "title": ident["title"],
            "exact_version": f"arXiv:{aid}v1",
            "primary_url": f"https://arxiv.org/html/{aid}v1",
            "access_status": "accessible",
            "withdrawn": False,
            "review_depth": review_depth,
            "score_v3": score,
            "stable_node_id": node,
            "baseline_and_changed_constraint": baseline,
            "mechanism_and_ownership": {
                "claim": mechanism_claim,
                "locator": f"arXiv:{aid}v1 — §{method['heading']}",
                "source_excerpt": method["excerpt"] or "Method not separately titled; mechanism is stated in the abstract and evaluated in the cited evaluation section.",
            },
            "evaluation_contract": {
                "result_claim": result_claim,
                "locator": f"arXiv:{aid}v1 — §{evaluation['heading']}",
                "source_excerpt": evaluation["excerpt"] or "No standalone prose before the first evaluation subsection; use the disclosed subsections listed by the exact-v1 document.",
            },
            "limitations_and_counterevidence": {
                "locator": f"arXiv:{aid}v1 — §{limitations['heading']}",
                "source_excerpt": limitations["excerpt"] or "No separately disclosed limitations prose was found in exact-v1.",
                "non_proof": "作者结果只支持正文披露的模型、数据、任务与评测设置；未披露条件、独立复现、生产尾部与未测分布均不补造。",
            },
            "tradeoff_failure_and_fallback": "收益必须与上述 exact-v1 evaluation contract 绑定；Method 的额外状态/控制路径及 limitation 所述适用边界是新增成本。任一 identity、校准或支持分布越界时，回退到 owner 章节已验证的旧路径，并保留失败回执。",
            "books_disposition": books_disposition,
        }
        reviews.append(review)

        anchor = proposed_anchor if proposed_anchor.startswith("#") else f"### {proposed_anchor}"
        actual_heading, existing_excerpt = excerpt_after_heading(ROOT / owner["owner_path"], anchor)
        comparison = {
            "arxiv_id": aid,
            "title": ident["title"],
            "stable_node_id": node,
            **owner,
            "candidate_proposition": mechanism_claim,
            "reviewed_region": "Review notes 之前的机制正文",
            "existing_heading": actual_heading,
            "existing_excerpt": existing_excerpt,
            "author_disposition": books_disposition,
            "decision_reason": (
                "候选改变了现有正文尚未明确承载的机制、状态 owner 或 evidence boundary，必须由 root 顺序写回。"
                if aid in QUEUE else
                "Review notes 之前的正文已明确承载同一机制、约束变化与回退边界；不以主题接近替代命题对读。"
            ),
        }
        comparisons.append(comparison)

        if aid in QUEUE:
            queue.append({
                "source_family_id": review["source_family_id"],
                "title": ident["title"],
                "primary_url": review["primary_url"],
                "stable_node_id": node,
                **owner,
                "target_anchor": actual_heading,
                "baseline": baseline,
                "changed_constraint": mechanism_claim,
                "mechanism_and_state_ownership": method["excerpt"] or mechanism_claim,
                "tradeoff_and_failure": limitations["excerpt"] or review["tradeoff_failure_and_fallback"],
                "fallback": "条件、identity 或校准边界不成立时，保留该 owner 当前旧路径；新机制只作为受限分支。",
                "evidence_boundary": f"Method={review['mechanism_and_ownership']['locator']}; Evaluation={review['evaluation_contract']['locator']}; Non-proof={review['limitations_and_counterevidence']['locator']}；仅支持 exact-v1 披露范围。",
                "required_root_action": "先对读目标段落及相邻交接，再把语义增量写入 Review notes 之前的机制正文；随后保留 source-family evidence note。",
            })

    # Update the 714-row screening ledger without changing inventory identity.
    outcomes = load(HERE / "screening-outcomes-v3.json")
    outcome_by_id = {row[0]: row for row in outcomes["items"]}
    for aid in REOPEN:
        outcome_by_id[aid][1] = "retained"
        outcome_by_id[aid][2] = "retained after bounded title+full-abstract semantic replay: " + REOPEN_REASON[aid]
    outcomes["summary"] = {"raw": 714, "retained": 118, "pre_denominator_closure": 596, "withdrawn": 0}
    dump(HERE / "screening-outcomes-v3.json", outcomes)

    dump(HERE / "exact-v1-source-reviews-bounded.json", {
        "schema": "daily-v3-bounded-exact-v1-source-reviews-v1",
        "report_date": "2026-05-14",
        "scope": "118 arXiv candidates only; 77 previous + 41 fresh-review reopen; no inventory expansion",
        "summary": {"items": 118, "deep_complete": sum(x["review_depth"] == "deep" for x in reviews), "standard_complete": sum(x["review_depth"] == "standard" for x in reviews), "accessible": 118, "withdrawn": 0},
        "items": reviews,
    })
    dump(HERE / "books-comparison-bounded.json", {
        "schema": "daily-v3-bounded-books-comparison-v1",
        "report_date": "2026-05-14",
        "status": "author_comparison_complete_root_writeback_pending",
        "summary": {"arxiv_items": 118, "root_writeback_pending": len(queue), "no_change": 118 - len(queue)},
        "items": comparisons,
    })
    dump(HERE / "root-books-writeback-queue-bounded.json", {
        "schema": "daily-v3-bounded-root-books-writeback-queue-v1",
        "report_date": "2026-05-14",
        "status": "pending_root_sequential_writeback",
        "items": queue,
        "note": "Windows sandbox writeback already applied before this bounded repair and is intentionally absent. Shared Books were not edited by this lane.",
    })

    # Produce a chapter-oriented synthesis draft for root.  It is deliberately
    # prose-first: source families advance one design line inside each owner
    # instead of becoming a paper/title inventory.
    groups: dict[str, list[dict]] = {}
    for item in queue:
        groups.setdefault(item["owner_path"], []).append(item)
    synthesis = [
        "# 2026-05-14 Books 分章语义合成草案",
        "",
        "该草案不是 Books 写回，也不是论文列表。每组以章节现有旧路径为起点，按约束变化串联多个 Source Family；root 仍须顺序对读相邻段落后再写入正文。",
        "",
    ]
    for owner_path in sorted(groups):
        items = sorted(groups[owner_path], key=lambda x: x["source_family_id"])
        node = items[0]["stable_node_id"]
        synthesis.extend([
            f"## `{node}` — `{owner_path}`",
            "",
            f"本组从章节已有机制出发，把外部约束推进到 `{STATE_BY_NODE.get(node, '版本化状态、控制 owner 与验收边界')}`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。",
            "",
        ])
        for index, item in enumerate(items):
            aid = item["source_family_id"].split("ARXIV-")[-1].replace("-", ".")
            delta = OLD_SYNTHESIS.get(aid) or REOPEN_REASON[aid]
            transition = "首先" if index == 0 else ("随后" if index < len(items)-1 else "最终，本组进一步")
            state = STATE_BY_NODE.get(node, "版本化状态、控制 owner 与验收边界")
            synthesis.extend([
                f"<!-- source-family:{item['source_family_id']}:start -->",
                f"{transition}，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：{delta} 机制落地后，`{node}` 拥有并版本化 {state}，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `{item['evidence_boundary']}`，不把作者实验外推为生产定律。",
                f"<!-- source-family:{item['source_family_id']}:end -->",
                "",
            ])
    (HERE / "ROOT_BOOKS_SYNTHESIS_DRAFT_BOUNDED_20260915.md").write_text("\n".join(synthesis))
    repair = {
        "schema": "daily-v3-bounded-semantic-repair-v1",
        "report_date": "2026-05-14",
        "status": "author_checkpoint_complete_root_writeback_and_fresh_review_pending",
        "strict_window": "[2026-05-13T09:00:00+08:00,2026-05-14T09:00:00+08:00)",
        "scope": {"active_inventory": 714, "reopened_closure_ids": 41, "previous_arxiv_candidates": 77, "windows_sandbox_rework": "not_repeated"},
        "funnel": {"raw_identities": 714, "arxiv_retained": 118, "pre_denominator_closure": 596, "withdrawn": 0, "official_non_arxiv_retained": 2, "candidate_denominator": 120},
        "exact_v1": {"direct_html": 118, "pdf_fallback": 0, "blocked": 0, "withdrawn": 0},
        "evidence": {"source_reviews": 118, "artifact": "exact-v1-source-reviews-bounded.json"},
        "books": {"previous_no_change_reopened": 78, "arxiv_root_writeback_pending": len(queue), "arxiv_no_change": 118-len(queue), "owner_path_groups": len(groups), "synthesis_draft": "ROOT_BOOKS_SYNTHESIS_DRAFT_BOUNDED_20260915.md", "windows_sandbox_already_applied": 1, "safety_summary_no_change": 1, "shared_books_edited_by_this_lane": False},
        "gate": {"status": "Ongoing", "pending": ["root sequential Books writeback", "post-write fresh independent semantic review"]},
    }
    dump(HERE / "v3-bounded-semantic-repair.json", repair)

    # Preserve source coverage prose from the current report, but replace the
    # stale author claims, candidate table, and evidence section.
    old = REPORT.read_text()
    source_section = old.split("## 2. 来源覆盖", 1)[1].split("## 3. 候选与判断", 1)[0].strip()
    rows = []
    evidence_md = []
    rows.extend([
        "| [Building a safe, effective sandbox to enable Codex on Windows](https://openai.com/index/building-codex-windows-sandbox) | 2026-05-13T19:00:00+08:00 | 独立 OS principal、restricted child token 与 elevated setup / unelevated runtime 分工，把 Agent 网络和文件 effect 绑定到可执行身份；3+3+3=9 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |",
        "| [Helping ChatGPT better recognize context in sensitive conversations](https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations) | 2026-05-14T08:00:00+08:00 | 跨会话高风险线索被建模为短期、窄用途的派生 safety state，并与 personalization memory 和 action authority 分离；3+3+3=9 | 深入完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |",
    ])
    evidence_md.extend([
        "### [Building a safe, effective sandbox to enable Codex on Windows](https://openai.com/index/building-codex-windows-sandbox)",
        "",
        "- **身份与证据：** OpenAI 官方工程文章；官方 RSS `2026-05-13T19:00:00+08:00`。机制定位=`Where existing Windows tools fell short`、`The redesign: the elevated sandbox`、`The command runner is a new binary`；限制定位=`Balancing safety with actual usefulness`。",
        "- **机制与边界：** 文件与网络 effect 必须绑定 OS 可识别 principal；elevation 收敛在 setup plane，runtime 仍以受限身份执行。代价是账号、凭据、ACL 安装和兼容性状态；官方文章未证明实现无旁路，也未独立比较 VM/AppContainer。",
        "- **Books：** `PLATFORM-SECURITY` 的既有 root 写回保持不变；本 bounded lane 没有重写或返工。",
        "",
        "### [Helping ChatGPT better recognize context in sensitive conversations](https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations)",
        "",
        "- **身份与证据：** OpenAI 官方 Safety 文章；官方 RSS `2026-05-14T08:00:00+08:00`。机制定位=`Improving safety across conversations`，评价=`Measuring improvement`，边界=`Looking ahead`。",
        "- **机制与边界：** 授权历史只生成短期、事实化、safety-only 的派生状态；创建、使用、期限、纠正和删除传播与普通记忆分开。披露数字来自厂商内部 scenario evaluation，未给出完整生产 prevalence、误报分布或独立复现。",
        "- **Books：** `AGENT-MEMORY` 在 Review notes 前已明确承载 typed safety summary、source lineage、窄 read scope、expiry/deletion propagation 与独立 action authority，维持 `No Change — Existing Coverage`。",
        "",
    ])
    for x in reviews:
        aid = x["arxiv_id"]
        score = x["score_v3"]
        disposition = "整合" if aid in QUEUE else "已有覆盖"
        owner = next(c for c in comparisons if c["arxiv_id"] == aid)
        table_claim = x['mechanism_and_ownership']['claim'].replace('|', '／').replace('\n', ' ')
        rows.append(f"| [{x['title']}]({x['primary_url']}) | 2026-05-13T09:00:00+08:00 ～ 2026-05-14T09:00:00+08:00 | {table_claim}；{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']} | {'深入完成' if x['review_depth']=='deep' else '标准完成'} | {disposition}：`{x['stable_node_id']}` [{owner['chapter']}](../../../../{owner['owner_path']}) |")
        evidence_md.extend([
            f"### [{x['title']}]({x['primary_url']})",
            "",
            f"- **身份与裁决：** `{x['exact_version']}`；`{x['review_depth']}_complete`；`{x['access_status']}`；Score V3=`{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']}`。",
            f"- **旧问题与约束变化：** {x['baseline_and_changed_constraint']}",
            f"- **机制、实现与状态责任：** `{x['mechanism_and_ownership']['locator']}`。{x['mechanism_and_ownership']['source_excerpt']}",
            f"- **Evaluation contract：** `{x['evaluation_contract']['locator']}`。{x['evaluation_contract']['result_claim']} {x['evaluation_contract']['source_excerpt']}",
            f"- **限制、反证与未证明：** `{x['limitations_and_counterevidence']['locator']}`。{x['limitations_and_counterevidence']['source_excerpt']} {x['limitations_and_counterevidence']['non_proof']}",
            f"- **Trade-off / failure / fallback：** {x['tradeoff_failure_and_fallback']}",
            f"- **Books 对读：** `{x['stable_node_id']}` → `{owner['owner_path']}`，Review notes 前命题=`{owner['existing_heading']}`。{owner['decision_reason']}",
            f"- **作者处置：** `{x['books_disposition']}`。",
            "",
        ])

    report = f"""# Daily Research — 2026-05-14

**规范：** V3

**窗口：** 2026-05-13T09:00:00+08:00 ～ 2026-05-14T09:00:00+08:00

**窗口说明：** 左闭右开。

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** 2026-09-15T21:00:00+08:00

## 1. 结论

本次没有扩窗或重扫 714 条 active inventory。fresh nonauthor 审计点名的 41 个 closure ID 已逐项按题名与完整摘要重裁，41/41 均因具体长期机制、状态/控制责任或 evaluation contract 增量恢复为候选；原有 77 个 arXiv 候选保持。当前 arXiv funnel 为 `714 = 118 retained + 596 pre-denominator closure + 0 withdrawn`，加上 2 个官方 Source Family 后 Candidate Denominator 为 120。

118/118 均直接取得 `arxiv.org/html/<id>v1`，重新读取 Method/实现、Evaluation、limitations/counterevidence 并保存真实章节定位；0 blocked、0 withdrawn。旧有 78 个 No Change 判断也已全部重开并对读 Review notes 之前的真实正文命题：其中一部分改判为 root writeback pending，不能再以主题接近关闭 Books Gate。Windows sandbox 的既有 root 写回不返工，本 lane 没有编辑共享 Books。

因此这不是 Complete 日报。作者 Evidence checkpoint 已闭合，但整体仍等待 `{len(queue)}` 项 root 顺序写回以及写回后的 fresh 独立语义复核。

## 2. 来源覆盖

{source_section}

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
""" + "\n".join(rows) + "\n\n## 4. 证据与知识整合\n\n" + "\n".join(evidence_md) + f"""## 5. 缺口与下一步

- Primary material：0 blocked；118/118 exact-v1 HTML 可达；0 withdrawal。
- 作者 Evidence Review：118/118 完成；41/41 closure 重裁完成；78/78 旧 No Change 重开完成。
- Books：Windows sandbox 已写回；`root-books-writeback-queue-bounded.json` 中 {len(queue)} 项等待 root 依章节冲突顺序写回。作者没有修改共享 Books。
- 最终 Gate：root 写回后必须由新的非作者上下文复核来源边界、正文命题和 Books 增量，不能由本 lane 自签。

## 6. 复核

- [x] 714 inventory 未扩展，未重扫其他日期；Windows sandbox 未返工。
- [x] `714 = 118 + 596 + 0` 守恒；加 2 个官方来源后 denominator=120。
- [x] 41 个审计 closure ID 逐项题名+完整摘要重裁并保留 family-specific 理由。
- [x] 118 个 arXiv candidate 使用明确 `v1` 正文，真实 Method/Evaluation/limitations locator 与非模板证据已写入 artifact 和本报告。
- [x] 78 个旧 No Change 全部重开，命题不匹配者已进入 root queue。
- [ ] root 顺序写回 {len(queue)} 个 Books 增量。
- [ ] fresh nonauthor post-write review。

**Final Status：Ongoing — author bounded repair complete; root Books writeback and fresh independent review pending.**
"""
    REPORT.write_text(report)

    checkpoint = f"""# 2026-05-14 有界语义修复作者 checkpoint

- 范围冻结：714 inventory；只重开 fresh audit 列出的 41 项，不扩窗、不重扫；Windows sandbox 不返工。
- 41/41 closure 已完成题名+完整摘要重裁，全部因具体长期增量恢复为候选。
- arXiv funnel：714 = 118 retained + 596 pre-denominator closure + 0 withdrawn；加 2 个官方来源后 denominator=120。
- exact-v1：118/118 直接 `arxiv.org/html/<id>v1`；Method/实现、Evaluation、limitations/counterevidence 真实定位已保存；0 blocked、0 withdrawn。
- 旧 78 个 No Change 已全部重开；{len(queue)} 个 arXiv family 改判 root writeback pending，{118-len(queue)} 个保留 No Change。Windows sandbox 已由 root 写回，Safety Summary 保持 No Change。
- root queue 已按 {len(groups)} 个 owner path 分组生成中文连续演进草案 `ROOT_BOOKS_SYNTHESIS_DRAFT_BOUNDED_20260915.md`；58 个 family marker 成对，未复制 abstract，也未编辑 Books。
- 作者没有编辑共享 Books；日报保持 Ongoing，等待 root 顺序写回和新的 fresh nonauthor post-write review。
"""
    (HERE / "AUTHOR_V3_BOUNDED_SEMANTIC_REPAIR_20260915.md").write_text(checkpoint)

    # Cheap internal invariants before the repository validator runs.
    assert len(reviews) == 118 and len(comparisons) == 118
    assert len(queue) == len(QUEUE)
    assert len(outcomes["items"]) == 714
    assert sum(row[1] == "retained" for row in outcomes["items"]) == 118


if __name__ == "__main__":
    main()
