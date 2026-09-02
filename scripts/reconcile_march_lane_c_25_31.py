#!/usr/bin/env python3
"""Reconcile the independent 2026-03-25..31 fresh-context audit.

This script replaces the author denominator with the reviewer-adjudicated
denominator, rebuilds exact-v1 Source Reviews and Books comparisons, and keeps
all real Books writes root-owned.  It never reads Weekly artifacts.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import rebuild_march_lane_d_full_replay as lane


ROOT = Path(__file__).resolve().parents[1]

ADDITIONS_BY_DAY = {
    25: "22367 22563 22855 22928 23055 23064 23292 23414 23483".split(),
    26: "23516 23801 24564 24582".split(),
    27: "24676 25111 25120 25289 25342".split(),
    28: [],
    29: [],
    30: "25969 26131 26221 26469".split(),
    31: "27299 27905 28005 28063 28166 28168 28342 28345 28507 28590 28622 28650".split(),
}

NODE = {
    "22367": "AGENT-WORKFLOW", "22563": "TRAIN-RLHF",
    "22855": "INFER-TENSORRT-LLM", "22928": "PLATFORM-SECURITY",
    "23055": "PLATFORM-EVALUATION-SYSTEM", "23064": "PLATFORM-SECURITY",
    "23292": "PLATFORM-EVALUATION-SYSTEM", "23414": "TRAIN-DISTRIBUTED-TRAINING",
    "23483": "INFER-SPECULATIVE-DECODING", "23516": "MODEL-LONG-CONTEXT",
    "23801": "PLATFORM-SECURITY", "24564": "AGENT-MEMORY",
    "24582": "PLATFORM-EVALUATION-SYSTEM", "24676": "AGENT-MULTI-AGENT",
    "25111": "PLATFORM-SECURITY", "25120": "TRAIN-DISTRIBUTED-TRAINING",
    "25289": "TRAIN-DISTRIBUTED-TRAINING", "25342": "PLATFORM-EVALUATION-SYSTEM",
    "25969": "PLATFORM-PRODUCTION", "26131": "INFER-GPU-MEMORY",
    "26221": "PLATFORM-SECURITY", "26469": "PLATFORM-EVALUATION-SYSTEM",
    "27299": "PLATFORM-FOUNDATIONS", "27905": "AGENT-PLATFORM",
    "28005": "PLATFORM-EVALUATION-SYSTEM", "28063": "PLATFORM-EVALUATION-SYSTEM",
    "28166": "PLATFORM-SECURITY", "28168": "TRAIN-DISTRIBUTED-TRAINING",
    "28342": "INFER-TENSORRT-LLM", "28345": "PLATFORM-SECURITY",
    "28507": "WORLDVIEW-SCALING-LAW", "28590": "PLATFORM-EVALUATION-SYSTEM",
    "28622": "INFER-SCHEDULING", "28650": "PLATFORM-SECURITY",
}


def s(problem: str, mechanism: str, evidence: str, boundary: str):
    return problem, mechanism, evidence, boundary


SYNTHESIS = {
"22367": s("把检索原文持续塞回上下文会让 token 成本和可生成陈述面随数据集增长。", "RES 把意图解析、确定性检索聚合和叙述生成拆开；Executor 只向 Synthesizer 交付固定尺寸统计摘要，使 raw record 不进入生成状态。", "Crossref-backed ScholarSearch 的 100 次运行支持所测数据规模下的 O(1) token 输入；它不证明固定摘要足以回答任意开放问题。", "固定摘要压低成本与数据幻觉面，却牺牲逐条证据可见性；需要引用原文或开放探索时 RAG 仍必要。"),
"22563": s("在整条 RLHF pipeline 上统一施加 DP 会把隐私噪声扩散到策略优化并浪费已公开的训练信号。", "该方案只在敏感偏好进入 reward learning 时建立 DP 边界，再让 policy 从私有 reward model 学习；隐私 owner 从最终策略更新前移到奖励数据接口。", "理论 upper/lower bound 与 HH-RLHF/Gemma-2B-IT 实验支持特定预算下的额外误差项；不证明 reward model 输出不会泄漏未建模属性。", "解耦降低 policy 侧噪声，却把风险集中到 reward model 版本、访问与再利用；无敏感偏好时普通 RLHF 更简单。"),
"22855": s("edge 视觉推理中 dense CLIP window alignment 会同时受算力、存储流量和实时 deadline 约束。", "TorR 用 HDC associative reasoner、query cache、bit-delta update 与 load-gated bypass，在控制器中按负载选择 full/delta/bypass path。", "28nm synthesis 与 cycle-accurate simulation 支持论文配置的能耗、延迟和 AP 折中；不是流片结果，也不能外推其他传感器与工艺。", "缓存和多路径换取实时性，却新增阈值漂移、复用错误与专用硬件成本；负载低或精度优先时 dense path 仍成立。"),
"22928": s("LLM 一旦接入 RAG、工具和多 agent，攻击不再停留在输入文本，而会沿知识、权限和协作边传播。", "SoK 把 prompt、knowledge base、tool/plugin 与 cross-agent 组合成显式 trust-boundary taxonomy，并将 unsafe action 与 privilege escalation 纳入系统评估。", "证据是 2023–2025 研究与标准的系统化归纳，可支持威胁模型和控制清单；不能证明任一 defense 在生产中达到固定有效率。", "统一 taxonomy 提高完整性却可能随新协议过时；封闭、只读单 agent 可使用更窄威胁模型。"),
"23055": s("同一数据先筛模型再估计 KPI 分布会产生 post-selection bias，普通 confidence interval 不再覆盖声明对象。", "PS-DME 用 e-value 在任意 data-dependent pre-selection 后控制 distributional KPI 的 false coverage rate，而不是只报告一个目标阈值。", "理论条件、synthetic、text-to-SQL 和 telecom 实验支持所述 coverage/sample-efficiency；不保证任意 evaluator 或分布漂移下仍校准。", "复用数据提高效率但依赖统计假设与更复杂审计；样本充足时独立 holdout 仍更容易解释。"),
"23064": s("heartbeat background execution 与前台会话共用 memory 时，不可信后台内容可在用户不可见的情况下变成后续行为状态。", "论文形式化 Exposure→Memory→Behavior 链，并区分短期 session 污染、长期写入和跨会话影响，要求 background identity、provenance 与 write authority 分离。", "MissClaw 控制实验支持特定社交线索与 memory policy 下的污染率；不代表所有 Claw 实现或自然流量具有相同比例。", "隔离 background memory 降低静默污染，却减少跨渠道连续性并增加审批；可信本地定时任务仍可共享有限状态。"),
"23292": s("公开 benchmark 会被训练暴露、反复调参与隐藏 harness 差异共同侵蚀，单看 leaderboard 无法区分能力与适配。", "Olympiad contract 在评测前密封题目、冻结 submission、统一执行 harness，结束后再公开题目和代码，分离测量期保密与事后可审计。", "这是 evaluation design proposal 而非新模型实验；可支持 release contract，不能证明密封本身消除组织泄漏或 evaluator 偏差。", "sealed exam 提高独立性却降低即时透明度并增加保密运营；诊断性公开集仍适合日常开发。"),
"23414": s("长 rollout 使 RL learner 等待最慢 trajectory，统一大 batch 会形成严重同步 bubble。", "SortedRL 在线按输出长度重排 rollout，允许短组先更新，并用 stateful controller、rollout buffer 与 cache 约束 off-policy 程度。", "LLaMA-3.1-8B/Qwen-2.5-32B 的指定任务支持 bubble 与训练结果折中；不证明长度排序对所有 reward 或策略漂移稳定。", "异步重排提高利用率却改变数据时序和 freshness；短、同质 rollout 仍适合同步 batch。"),
"23483": s("agentic vision 的感知、推理和工具循环串行累积，单纯加速每个模型调用不能消除 agentic depth。", "SpecEyes 让轻量无工具模型预测 trajectory，以 answer-separability gate 决定提前提交，并用异构并行 funnel 覆盖大模型串行执行。", "V* Bench、HR-Bench、POPE 支持所测模型/并发下的速度质量；self-verification gate 不是通用 correctness proof。", "错误 speculation 会跳过必要工具并放大置信误校准；高风险或难验证任务仍应执行完整链。"),
"23516": s("full attention、固定 memory state 与外部 RAG 分别受二次成本、不可编辑或端到端失配约束。", "MSA 组合 scalable sparse attention、document-wise RoPE、KV compression、Memory Parallel 与 Memory Interleaving，把超长 memory 作为可训练且可分布的模型状态。", "论文报告 16K→100M、2×A800 等指定配置的质量/容量；不能把作者 benchmark 外推为通用 lifetime memory。", "线性扩展换来稀疏索引、并行通信和文档身份治理；证据需逐字引用时外部 RAG 仍更可审计。"),
"23801": s("agent protocol 各自声明安全属性时，跨 MCP/A2A 等共享基础设施的组合破坏不会被单协议检查发现。", "AgentRFC 定义六层 protocol stack 与 11 个 TLA+ invariant，并把规范抽成 typed IR、model-check counterexample 后回放到 live SDK。", "形式模型与代表性实现可证明定义内的 non-conformance/组合反例；不能证明规范外环境或未知实现安全。", "conformance pipeline 提高可复算性，却增加规范抽取、状态爆炸和 replay 维护；简单单协议仍可用较窄测试。"),
"24564": s("agent memory 若跨主体交易，普通文本或向量记录无法证明来源、计算投入与执行环境兼容。", "clawgang 将 memory 与可验证 computation provenance 绑定，meowtrade 再把认证 artifact 的 listing、transfer 与 governance 分层。", "exact-v1 主要是架构与经济机制主张，缺少独立大规模安全/价值实验；只能支持 provenance contract，不支持市场价值结论。", "可验证 lineage 增加签名、环境 identity、撤销和隐私成本；单用户私有 memory 无需市场层。"),
"24582": s("agent workflow 的 state 看似常见，不代表 state-action transition 有足够样本支持自动执行。", "该框架用 Markov visitation measure 区分 state blind mass 与 state-action blind mass，并把 entropy escalation gate 映射为预期人工 oversight cost。", "BPI 2019 log 的 held-out simulation 支持所定义 blind-mass/成本关系；日志策略不是真实 autonomous agent，不能证明 deployment reliability。", "细化 state 提高风险可见性却扩大稀疏空间和人工负担；确定性流程仍可用显式规则。"),
"24676": s("多 agent 达成 consensus 可能来自随机对称破缺和 memetic drift，而非更强集体推理。", "论文把 population size、interaction 与初始微小偏置纳入 scaling analysis，区分稳定集体信号与 lottery-like convergence。", "命名/协作实验支持所测模型与拓扑下的 drift 规律；不能外推所有任务或把共识等同正确。", "增加 agent 可提高探索也会放大协调偏差；高度耦合或缺少独立证据时单 agent/固定审议更稳。"),
"25111": s("self-evolving agent 若能改写自身策略或代码，仅用结果测试无法证明每次变化仍满足安全约束。", "SEVerA 把候选演化、形式化 specification、verified synthesis 与 acceptance gate 连成闭环，使修改必须携带可检查 proof obligation。", "公开任务验证支持论文形式系统覆盖的性质；不能证明自然语言 specification 完整，也不覆盖 verifier bug。", "证明门槛限制搜索空间并增加 solver 成本；低风险、可快速 rollback 的变化可用测试加审计。"),
"25120": s("多模态训练的 data loader、通信、memory 与算子瓶颈会随模态配比改变，固定 pipeline 参数难以保持效率。", "DFLOP 从运行 profile 学习数据驱动的 pipeline 配置，在阶段间联合调节 batch、并行与资源分配。", "实验支持指定模型、集群和 modality workload 的吞吐改进；不证明 learned policy 跨硬件或数据分布稳定。", "动态优化减少手工调参，却新增 profiling 开销、控制振荡和复现难度；稳定 workload 仍宜冻结配置。"),
"25289": s("cross-silo federated learning 中 participant dropout/straggler 不只降低吞吐，还会系统性改变每轮数据代表性和最终模型质量。", "论文把 failure pattern、参与集合与聚合结果关联，要求 runtime 同时跟踪 availability state 与 statistical contribution，而非只重试通信。", "实验能支持所测数据异质性和故障率下的质量变化；不能外推任意聚合器或现实组织行为。", "failure-aware selection 提高鲁棒性却可能长期排除弱节点并引入公平偏差；稳定全参与环境仍可使用标准 FedAvg。"),
"25342": s("deep-research agent 只按最终答案打分，无法定位意图分解、证据覆盖和推理结构在哪一步失真。", "该工作用 categorical structure 表达 intent→subclaim→evidence→conclusion 的可达/一致关系，把 process evidence 与 outcome 分开验证。", "所给任务和 evaluator 支持结构指标的诊断价值；LLM judge 与类别映射不等于事实真值。", "结构化评估提高可解释性但增加标注与 schema bias；短事实查询仍可直接核对答案。"),
"25969": s("现代 accelerator 的 hardware 与 firmware 并行演进，单侧仿真无法捕获 timing、register 和 recovery protocol 的跨层不一致。", "FireBridge 用 cycle-accurate hardware model 与真实 firmware 在同一 co-verification loop 中交换事件与状态，形成可重放接口契约。", "作者案例支持指定 accelerator block 的 bug detection 与 cycle fidelity；不能外推完整芯片、工艺或生产可靠性。", "联合验证提高覆盖却增加模型同步和仿真成本；接口稳定的小模块仍可分层测试。"),
"26131": s("CXL memory expansion 增加容量却受 link bandwidth 限制，透明搬运原始 cache line 会让远端访问吞吐先耗尽。", "IBEX 在扩展内存路径内压缩数据并协调 metadata、decode 与 consistency，使 bandwidth/latency 成为可控 memory-tier policy。", "架构模拟或原型支持指定压缩率、workload 与 CXL 配置；不能证明所有模型 tensor 都可压缩且无尾延迟。", "压缩节省带宽却增加 compute、metadata 和不可压缩回退；HBM/DRAM 足够时本地状态仍最简单。"),
"26221": s("开放 agent runtime 的 plan、tool result、memory 与 delegated authority 都是动态且概率性的，传统固定控制流威胁模型不够。", "该 SoK 用六维 taxonomy 汇总攻击、benchmark、defense、audit 与 operational governance，并把 capability revocation、persistent-memory integrity 纳入 secure-by-construction doctrine。", "50 篇研究的系统化归纳支持缺口与设计清单；不能证明推荐控制已经在生产验证。", "更完整 doctrine 增加运行时治理成本；封闭、无持久状态 agent 可采用较窄边界。"),
"26469": s("distributed inference 研究依赖 ad-hoc testbed，难在同一代码下复现异构 device/network 与假想拓扑。", "UNIFERENCE 用按 communication primitive 同步的 discrete-event logical process 保持因果顺序，并复用 PyTorch Distributed 代码从 simulation 切到 deployment。", "多 backend/hardware 对比支持论文场景的 runtime fidelity；98.6% 不能外推未建模 contention、failure 或 kernel。", "仿真提高探索速度却依赖设备模型校准；最终 release 仍需真实集群验证。"),
"27299": s("gateway、agent workflow、Kubernetes 与协议边界分别维护策略，会让同一阈值和权限在层间漂移。", "Semantic Router DSL 用非图灵完备 declarative source 编译 priority decision tree、orchestration node、NetworkPolicy/Sandbox 和 MCP/A2A gate，并保留结构化 audit trace。", "论文可支持语言约束与生成 artifact 的一致性主张；不能证明所有目标 runtime 语义等价或 production scale。", "统一编译减少 drift，却放大 compiler bug blast radius并限制表达力；局部复杂策略仍需专用控制器。"),
"27905": s("post-hoc validator 只能在完整输出后拒绝，static constrained decoding 又难处理运行时 contract 漂移。", "ATLAS-RTC 在每个 token 监控 contract drift，并用 bias、mask 与 rollback 闭环干预，把生成状态的 commit 权交给 runtime controller。", "structured generation/tool-calling 实验支持指定 failure-heavy workload 的 success/latency；不证明轻量信号能识别语义正确性。", "逐 token 控制提高合规却增加监控开销和错误 rollback；语法固定时普通 constrained decoding 更简单。"),
"28005": s("atomic claim decomposition 常与更长、更细 rubric 一起变化，观察到的收益无法归因于 decomposition 本身。", "研究冻结输入与 prompt richness，只改变 self-decomposing atomic 与 holistic judge，并跨 prompt variant 做 paired/bootstrap 比较。", "三个 QA benchmark、四类模型支持该单 prompt 设定的条件结论；不覆盖多阶段 atomic pipeline 或非 QA。", "atomic 提高可定位性却会累积拆分误差和成本；完整性敏感任务中 rich holistic judge 可能更稳。"),
"28063": s("有限 evaluator 只覆盖部分质量维度时，优化器会系统性把资源移向可测维度，reward hacking 不是偶发实现 bug。", "论文在多维质量、有限评测和资源约束下推导 distortion index，并分析 agent tool 增长使 coverage 组合性下降。", "主要证据是给定公理下的理论结果与部分分析；不能证明现实系统完全满足假设或数值阈值。", "扩大评测覆盖能减轻但不能消除盲区，并使成本快速增长；限制工具与权限仍是有效结构性手段。"),
"28166": s("预编码 toy tool 无法暴露真实 SDK 的 privilege scope、副作用和 prompt-injection 路径。", "GrantBox 把真实工具接入隔离 sandbox，记录 agent 获得、请求和实际使用的 privilege，按 attack trace 评估越权。", "公开场景支持所测 agent 在复杂 injection 下的高攻击成功率；不能外推所有工具或把 sandbox 当生产隔离证明。", "真实工具提高生态效度却增加运行风险、凭证管理和复现成本；单元 conformance 仍适合早期检查。"),
"28168": s("OCS GPU cluster 的 circuit path 会产生 routing polarization，传统以 spine 为中心的拓扑优化可能把不均衡下沉到 leaf link。", "leaf-centric 设计约束同一 leaf 流量在 spine 间均衡，并给出避免 polarization 的充分条件与多项式算法。", "理论与大规模 simulation 支持所建流量/拓扑模型的吞吐和求解成本；未证明真实 OCS 重配置与故障下同样成立。", "快速均衡牺牲全局最优空间并依赖流量估计；规模小或拓扑静态时 MIP/固定布线仍可用。"),
"28342": s("one-shot kernel generation 难同时保持 correctness 与性能，单一 incumbent 也容易在局部最优中坍缩。", "Kernel-Smith 维护可执行 candidate population，以 compile/correctness/speed feedback 进化，并将高增益正确 revision 转成 step-centric SFT/RL 信号。", "KernelBench、NVIDIA Triton 与 MetaX MACA 结果支持所测 backend 的搜索/训练闭环；vendor/author benchmark 不代表任意生产 kernel。", "evolution 提高搜索覆盖却消耗大量编译执行预算并可能过拟合 harness；成熟常用 kernel 仍优先人工库。"),
"28345": s("LLM call 把程序值穿过不透明自然语言变换，传统 taint summary 在 NL/PL 边界断裂。", "PRISM 用 placeholder→output reachability 和信息保留×输出模态的有限 taxonomy，为 LLM call 生成可组合 dataflow predicate。", "8,119 对样本、annotator agreement 与 taint evaluation 支持 taxonomy coverage；soundness 只相对标签成立，不代表 LLM 变换可完全预测。", "taxonomy 恢复静态分析却引入分类误差和保守传播；不含动态 prompt 的普通函数仍用精确 summary。"),
"28507": s("只依赖更多算力延续 scaling，会忽略效率改进必须重复发生才能抵消硬件、数据与成本约束。", "论文把能力扩展分解为 compute growth 与连续 efficiency doubling，要求 scaling forecast 显式记录算法/系统效率来源而非单一 FLOP。", "历史估计与情景分析只能支持所用指标和时间段的趋势；不能保证未来 doubling 速度或因果来源。", "效率视角改善规划却高度依赖基准口径与选择偏差；同代固定系统比较仍可用纯 compute 曲线。"),
"28590": s("CoT 文本可能与最终决策因子脱钩，把可读推理直接当 oversight signal 会产生伪安全感。", "MonitorBench 用显式 decision-critical factor、19 类任务与 stress prompt 测量被监控模型、monitor 模型和任务的条件性交互。", "1,514 例实验支持 monitorability 是条件属性且可被压低；不证明隐藏推理或真实因果链被恢复。", "更强 stress test 提高风险发现，却不能把低 monitorability 修复为可验证行为；高风险动作仍需外部 effect receipt。"),
"28622": s("edge distributed inference 的 best-effort peer route 不区分节点失效、性能波动与恶意行为，单个 peer 可使链路失败。", "G-TRAC 用 trust-floor pruning 加 risk-bounded shortest path，并由稳定 anchor 保存 reputation、边缘后台同步轻量状态。", "异构 testbed 支持指定规模/故障与分区下的 completion；trust score 来源与攻击适应性限制外推。", "trust-aware route 提高韧性却引入中心 anchor、陈旧 reputation 与误隔离；可信小集群仍可用普通最短路。"),
"28650": s("若每轮 self-modification 都只靠有重叠分布的 classifier gate，要求累计风险可和与无限效用可能相互冲突。", "论文给出 classifier TPR 与风险预算的上界，并以 Lipschitz-ball verifier 说明可验证结构如何逃离统计分类限制。", "定理只在明确公理与分布条件内成立；GPT-2/LoRA 实验是受限验证，不证明大规模 agent 自改安全。", "形式 verifier 可把局部风险压低，却限制允许修改集合并依赖 bound 正确；不可验证开放修改必须设有限预算和人工 gate。"),
}


KEEP_INTEGRATE = {f"2603.{x}" for x in "22300 22339 22751 22774 23049 23149 23806 24595 24775 25702 26498 26728 26993 27116 27138 27624 27819 28101 28239".split()}


def main() -> None:
    selected = {day: list(ids) for day, ids in lane.SELECTED.items()}
    for day, suffixes in ADDITIONS_BY_DAY.items():
        selected[day] = sorted(set(selected[day]) | {f"2603.{suffix}" for suffix in suffixes})
    lane.SELECTED = selected
    lane.INTEGRATE = KEEP_INTEGRATE
    lane.PAPER_SYNTHESIS.update({f"2603.{suffix}": value for suffix, value in SYNTHESIS.items()})

    # Rebuild GROUPS without duplicate routes, then bind additions and the five
    # author-owner corrections found by the independent audit.
    correction = {
        "22774": "INFER-SCHEDULING", "22858": "MODEL-LONG-CONTEXT",
        "23049": "INFER-KV-CACHE", "26074": "PLATFORM-SECURITY",
        "28101": "TRAIN-DISTRIBUTED-TRAINING", **NODE,
    }
    for node, suffixes in list(lane.GROUPS.items()):
        lane.GROUPS[node] = " ".join(s for s in suffixes.split() if s not in correction)
    for suffix, node in correction.items():
        lane.GROUPS[node] = (lane.GROUPS.get(node, "") + " " + suffix).strip()

    protected_section_overrides = {
        "2603.22367": {
            "method": [r"^III\. THE RES ARCHITECTURE$"],
            "evaluation": [r"^VI\. EVALUATION$"],
            "limitations": [r"^D\. Limitations$"],
        },
        "2603.23801": {"limitations": [r"^Bounded model checking\.$", r"^Specification fidelity\.$"]},
        "2603.24564": {
            "method": [r"^2 ClawGang", r"^2\.1 Proving"],
            "evaluation": [r"^4 Illustrative Use Cases$"],
        },
        "2603.24582": {"method": [r"^4\.1 Blind-spot mass over states and actions$"]},
        "2603.27299": {"evaluation": [r"^A\.3 Generated: LangGraph Decision Node", r"^A\.4 Generated: Kubernetes Artifacts$"]},
        "2603.28507": {
            "method": [r"^4 A Time-Indexed Efficiency-Doubling Extension$", r"^3 Logical Compute"],
            "evaluation": [r"^5 The Operational Meaning of Diminishing Returns$"],
        },
        "2603.28650": {"method": [r"^4\.2 Construction: Lipschitz Ball Verifier$", r"^3\.1 Hölder"]},
    }

    class ProtectedSectionOverrides(dict):
        def update(self, other=(), /, **kwargs):
            super().update(other, **kwargs)
            super().update(protected_section_overrides)

    lane.base.SECTION_OVERRIDES = ProtectedSectionOverrides(lane.base.SECTION_OVERRIDES)
    lane.base.SECTION_OVERRIDES.update(protected_section_overrides)

    # The only exact-v1 without arXiv HTML uses Roman-numeral PDF headings;
    # lane D's generic PDF parser recognizes Arabic headings, so provide the
    # actual PDF sections rather than downgrading them to Document/title.
    original_local_sections = lane.local_sections
    def local_sections(path: Path):
        if path.name == "2603.22367v1.pdf.txt":
            text = path.read_text(errors="ignore")
            headings = list(re.finditer(r"(?m)^((?:[IVXLCDM]+|[A-Z])\.)\s+([^\n]+)$", text))
            sections = {"Abstract": [lane.base.clean(text[:headings[0].start()])]}
            for index, match in enumerate(headings):
                end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
                sections[lane.base.clean(match.group(0))] = [lane.base.clean(text[match.end():end])]
            return sections
        return original_local_sections(path)
    lane.local_sections = local_sections

    lane.main()


if __name__ == "__main__":
    main()
