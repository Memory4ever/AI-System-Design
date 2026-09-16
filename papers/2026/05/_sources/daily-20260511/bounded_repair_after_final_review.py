#!/usr/bin/env python3
"""Apply only the bounded 2026-05-11 author repair requested by the final audit."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/11/README.md"
LEDGER = SOURCE_DIR / "V3_SCREENING_LEDGER_20260914.json"
EVIDENCE = SOURCE_DIR / "V3_EVIDENCE_REVIEWS_20260914.json"
QUEUE = SOURCE_DIR / "V3_BOOKS_WRITEBACK_QUEUE_20260914.json"
COMPARISON = SOURCE_DIR / "V3_BOUNDED_REPAIR_BOOKS_COMPARISON_20260915.json"
SYNTHESIS = SOURCE_DIR / "V3_BOUNDED_REPAIR_ROOT_QUEUE_20260915.md"
CHECKPOINT = SOURCE_DIR / "V3_BOUNDED_REPAIR_AUTHOR_CHECKPOINT_20260915.md"

CHECKED_AT = "2026-09-15T20:30:00+08:00"
PUBLIC_EVENT = "2026-05-11T08:00:00+08:00 scheduled arXiv announcement"

OWNER_PATHS = {
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "PLATFORM-TRACE": "books/part-06-ai-infrastructure/69-trace.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
}


def spec(score, owner, disposition, claim, mechanism, boundary, comparison, locators, artifact):
    return {
        "score": score,
        "owner": owner,
        "disposition": disposition,
        "claim": claim,
        "mechanism": mechanism,
        "boundary": boundary,
        "comparison": comparison,
        "locators": locators,
        "artifact": artifact,
    }


REOPEN = {
    "2605.06731": spec(
        (3, 3, 3), "AGENT-MEMORY", "No Change — Existing Coverage",
        "持久 Agent state 的安全边界不止是读取可信度，还包括每次 writeback 的授权漂移审计与可选择回滚。",
        "ULSPB 将日常多轮交互造成的 authorization drift、tool-use escalation 与 unchecked autonomy 计入 Harm Score；StateGuard 在执行后的 state-file writeback 边界检查 diff，并只回滚危险编辑。作者以 OpenClaw、四个 backbone、350 个设置及真实交互种子评估。",
        "证据限 OpenClaw、构造交互模式与安全优先阈值；高 false positive 会拒绝有益个性化，未知或适应性攻击仍可能绕过审计。低风险、短期且不持久的状态可保留轻量写入路径。",
        "Ch77 正文已把 poisoning 拆成 write→persistence→recall→adoption→external consequence，并要求 write admission、授权 mutation lineage、stable/transient state、选择性 repair 与 rollback；StateGuard 是该既有命题的受限实现，不新增长期 owner。",
        ("§2.1–2.3；§3.1–3.3；§5.1", "§4.1–4.3；§5.2；Appendix C/J", "Appendix A；§6；实验与 threat-model scope"),
        "public artifact disclosed: https://github.com/XiaoyuXU1/ULSPB ; adopted claim does not assume unreleased implementation details",
    ),
    "2605.06761": spec(
        (3, 3, 3), "AGENT-WORKFLOW", "No Change — Existing Coverage",
        "Web Agent 训练环境应把可复放的页面状态、交互 transition 与生成环境 identity 分开保存，离线成功不能直接授予 live-Web promotion。",
        "Weblica 用 HTTP-level caching 捕获并回放稳定视觉状态，同时保持交互行为；另一分支由 LLM 依据真实网站与核心导航技能合成环境，再用于 SFT/RL。作者在 held-out Weblica 与多个 Web navigation benchmark 上比较规模与 test-time compute。",
        "缓存只代表事件时 snapshot，无法覆盖页面更新、权限、动态后端和真实工具失败；合成环境还有 sim-to-real gap。离线环境适合训练和回归，live shadow/canary 仍拥有上线权。",
        "Ch81 正文的 Offline World 已明确 versioned corpus、search/visit actions、trajectory lineage、rejection filtering、SFT/RL 与 live canary，并指出 snapshot 不证明 freshness、动态页面、权限或 tool failure；Weblica 不改变该长期合同。",
        ("§3.1–3.3；§4.1–4.2", "§5.1–5.4；Appendix A/C/D", "§6 Limitations"),
        "no dedicated implementation artifact disclosed in exact-v1 for the adopted mechanism",
    ),
    "2605.06812": spec(
        (3, 2, 2), "PLATFORM-TRACE", "No Change — Existing Coverage",
        "Agent 审计图必须同时表达静态 capability base 与动态 semantic state，并保留二者之间的数据、控制与权限传播路径。",
        "Agent-BOM 用层级有向属性图表示 model/tool/long-term-memory 等静态能力，以及 goal/reasoning/action 等运行态，通过 semantic edge 与 security attribute 支持入口定位、前后向路径追踪和属性裁决；论文声称在 OpenClaw plugin 中覆盖四类代表性攻击链。",
        "exact-v1 仅为短篇扩展正文，没有独立实验协议、消融、limitations 或公开 artifact；代表性案例不证明图完整、归因因果或生产 adjudication 正确。无法建立完整事件 lineage 时应回退原始 trace 与人工审计。",
        "Ch69 已要求 immutable event trace 为 authority、dependency/root-cause/claim graph 为派生视图，并保存 data/control dependency、agent/tool identity、commit boundary 与 repair authority；Agent-BOM 的静态/动态分层是该命题的具体 schema。",
        ("exact-v1 主文 References 前第 1–3 段", "exact-v1 主文 References 前第 2–3 段的代表性 attack-scenario 描述", "exact-v1 无独立 limitations/evaluation protocol；边界由短篇主文披露范围给出"),
        "not disclosed in exact-v1; the paper states an OpenClaw plugin but provides no separate artifact locator",
    ),
    "2605.06898": spec(
        (3, 3, 3), "AGENT-PLATFORM", "No Change — Existing Coverage",
        "模型可以提出甚至生成 orchestration program，但 effect isolation、执行边界与最终 commit authority 仍必须留在 harness/runtime。",
        "SPE 让一次 model completion 同时成为上下文和 orchestrator program；Spell 以 Lisp 的 code-as-data、自编辑与重新求值实现，并把 outer evaluator 保持纯、effectful expression 放入只执行一次的 inner eval，以避免编辑程序时重放副作用。作者在 TerminalBench 1.1 与 SWE-bench Lite 子集上测试未专训模型。",
        "多数模型仍会生成 invalid program 或致命错误，实验只展示有限 orchestration；模型生成程序扩大了代码注入、资源和副作用风险。静态 workflow 对高风险、可复现任务仍更稳妥。",
        "Ch81 已规定 generated code workflow 必须经过 sandbox、typed interface 与 effect verifier；Ch84 又显式把 execution structure 与 orchestration owner(host/model) 纳入平台 identity。SPE 改变 proposal 位置，但未改变现有提交权边界。",
        ("§2；§3；Appendix A/B", "§4；TerminalBench 1.1 与 SWE-bench Lite 子集", "§6 Discussion；§4 的 invalid/fatal-program 结果与未训练范围"),
        "public implementation disclosed: https://github.com/lukejoconnor/spell",
    ),
    "2605.06919": spec(
        (3, 3, 3), "AGENT-RAG", "Integrate",
        "RAG 不能把检索文本表达的 certainty 直接当 evidence authority；source certainty、模型 prior 与最终 answer confidence 必须分开校准。",
        "论文定义 context-certainty obedience，并用 prior-answer reminder、certainty recalibration、context simplification 与最后 synthesis 组成约三次 forward 的交互策略，使模型在不确定上下文后重新暴露 prior，再按声明 certainty 调整回答。",
        "实验限 ClashEval 短答、八个开放权重模型且需要输出概率；表达 certainty 可能错误或被攻击，部分正确 context、长文本和 API/reasoning model 未覆盖。权威来源与 claim verifier 仍优先，策略失配时回退逐 claim 引用、冲突展示与 abstain。",
        "Ch76 已保存 source authority、freshness、provenance 与 sufficiency，却没有明确拆开“来源自报 certainty”“模型闭卷 prior”“回答采用强度”三种状态；该分离应进入 RAG answer gate。",
        ("§2.1–2.3；§3.1–3.4", "§4；§5.1–5.6；Appendix D", "Appendix E Limitations"),
        "no implementation repository disclosed in exact-v1; evaluated model licenses are not method artifacts",
    ),
    "2605.06978": spec(
        (3, 2, 3), "AGENT-MEMORY", "No Change — Existing Coverage",
        "大型 skill library 的检索对象应保留 entry、依赖、guard 与 verifier role，而不是把一组相关文本直接拼成上下文。",
        "GoSkills 从 typed skill graph 选择 anchor，沿 group graph 扩展 support，再压缩为有限 atomic payload，并以 Start/Support/Check/Avoid 固定字段呈现；下游 agent、skill payload 与环境不变。作者在 SkillsBench 与 ALFWorld 上对比可见需求覆盖、reward 与 runtime。",
        "role schema 依赖高质量 skill metadata 与可见需求，隐藏约束和缺失能力不会被结构化上下文修复；图漂移、错误边和压缩会删掉必要信息。无法证明 dependency closure 时回退完整 skill 或人工依赖。",
        "Ch77 已要求 section-level procedural graph 保存 intent、I/O、precondition、guard、verifier、source pointer 和 dependency closure，并已有 typed skill graph 的 merge/split/retire 与 workflow validation；四种 role 是现有命题的呈现实例。",
        ("§3.1–3.2；Appendix B/D", "§4–§5；Appendix E/F", "§6 Limitations；Appendix H"),
        "related public specification disclosed: https://github.com/agentskills/agentskills ; no GoSkills implementation artifact adopted",
    ),
    "2605.06992": spec(
        (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "Agent safety 的跨任务泛化必须独立于任务执行能力评估，不能用同任务安全率或平均成功率替代。",
        "论文用 LQ/H-infinity controller 构造安全映射复杂度分析，并在模拟 quadcopter 与 Llama-3.2 CRM 中比较 safe/unsafe teacher imitation，观察安全策略的跨任务映射更复杂、迁移更差。",
        "理论依赖线性控制、Lipschitz surrogate 与理想样本假设；实验限 imitation、模拟任务与受测 CRM，不证明所有 safety objective 都更难，也不授予因果机制。低风险同分布回归仍可保留较小 acceptance card。",
        "Ch66 已明确把统计可靠性、unseen-semantic generalization、mechanistic consistency 与 cross-task transfer 分成 claim-specific acceptance card，且任何单项不能独占发布权；该论文直接支持既有 cross-task 安全切片。",
        ("§2；§3.1–3.4", "§4.1–4.3；Appendix F", "§5 Limitations"),
        "public artifact disclosed: https://github.com/Tomerslortau/agentic-safety-generalization",
    ),
    "2605.07660": spec(
        (3, 2, 3), "TRAIN-GRPO", "No Change — Existing Coverage",
        "Token-level RL credit 具有可观测异质性，但 entropy 只能作为 eligibility/weighting sensor，不能替代 verifier 或因果 credit。",
        "作者按 attention entropy 区分低熵 anchor 与高熵 explorer，分析 gradient alignment/variance，并以从低熵到高熵的动态 soft weighting 调节训练；主实验为 Qwen3-8B+VeRL/DAPO，另含有限模型迁移检查。",
        "结果依赖受控 Qwen 配置、固定中层与 group-level 相关性；entropy 不证明 token 因果贡献，explorer-only 也不稳定。漂移或 verifier 不可靠时回退 uniform credit、process verifier 或 critic。",
        "Ch33 已有 Selective eligibility trace：低熵 token mask 只筛选 credit，明确 entropy 与因果不一致，并要求 verifier authority、mask/trajectory/update identity 和 uniform/process-verifier/critic fallback；动态 soft weighting不改变该长期结论。",
        ("§2–§5；Appendix B/D/K", "§3–§5；Appendix F/G/J/K", "§7 Limitations"),
        "no public implementation artifact disclosed in exact-v1",
    ),
    "2605.07686": spec(
        (3, 3, 3), "INFER-SCHEDULING", "Integrate",
        "Reasoning trace 与 final answer 共用输出上限时会发生结构性 budget coupling；调度与评估必须分别记录 reasoning budget、answer reserve 与截断浪费。",
        "论文把可见 CoT 与 answer 的共享上限写成 |Z|+|A|≤b，以 chain-length distribution 分解 truncation waste；split-budget generation 为推理和回答保留独立预算，再用 non-thinking extraction pass 从 trace 生成答案。",
        "证据限 Qwen3、DeepSeek-R1-Distill、数学/BBH 与固定输出限制；额外 extraction 增加 prefill、调用和选择偏差，task crossover 必须实测。短答案、无可见 CoT 或严格低延迟时仍可共用简单预算。",
        "Ch56 已让 scheduler 持有 reasoning budget、stopping 与 marginal value，却未明确 final-answer reserve 及共享 max-output 导致的 truncation coupling；该状态应进入 request admission 和 evaluation identity。",
        ("§4.1–4.5；§5.1–5.3", "§3；§6；Appendix B–V", "§7；任务/模型/budget crossover scope"),
        "no dedicated public artifact disclosed in exact-v1",
    ),
    "2605.07701": spec(
        (3, 2, 2), "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "Diffusion language model 的 CFG scale 可以从固定超参数演进为读取当前 diffusion state 的逐步控制策略。",
        "作者把每步 guidance scale 作为离散 action，以 diffusion state 为 observation、task reward 为终局信号，用 PPO 学习 task-与阶段相关的 guidance trajectory，并与固定/启发式 scale 比较。",
        "实验只有三个受控 NLP 任务和特定 discrete diffusion model；learned policy 会随 task、reward、sampler 与 state encoding 漂移，terminal reward 也不证明逐步控制因果正确。失配时回退固定 CFG 或保守启发式 schedule。",
        "Ch24 已把 source/coupling/schedule、conditional guidance 并行和 prior guidance 纳入 identity，但未表达 CFG strength 本身由 trajectory-conditioned policy 逐步拥有；该机制补足生成控制 owner。",
        ("§3.1–3.3；§4.1–4.3", "§5.1–5.4；Appendix B/C", "§6 Limitations"),
        "no public implementation artifact disclosed in exact-v1",
    ),
    "2605.07769": spec(
        (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
        "Coding Agent 的 evaluation set 必须包含正确行为为 no-op 的负动作样本，并把 reproduce、act、abstain 与 partial-fix 分开计分。",
        "FixedBench 从 SWE-bench Verified 构造 200 个已修复任务，期望 empty patch，并在五个模型、四种 harness 上测不当修改；reproduce-before-patch 提示降低 action bias，却在 partial-fix 场景引入过度 abstention。",
        "证据限 Python、热门仓库、所测 harness 与 patch 定义；no-op benchmark 不代表真实 issue triage，提示策略也会漏修部分修复。应以 paired action/no-action/partial-fix slices 与真实 regression outcome验收。",
        "Ch66 有通用 abstention 和 outcome contract，但尚未要求将 no-op 成功、stale issue 与 partial-fix 对照纳入 Coding Agent evaluation identity；缺少这一 slice 会把无必要 patch 错计为积极行为。",
        ("§2.1–2.5", "§3.1–3.3；Appendix C/D", "§5 Limitations"),
        "no dedicated public benchmark/code artifact disclosed in exact-v1",
    ),
    "2605.07806": spec(
        (2, 2, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "单一 verbalized confidence 不是充分 failure sensor；不同 self-assessment 维度必须按任务切片校准，并只作为选择性决策输入。",
        "论文同时采集 confidence 与 effort、understanding、ability、pleasantness、esteem、goal 等 appraisal，比较 12 个模型、38 个任务中的 failure discrimination、calibration 与 pre/post-task abstention；effort/ability 在部分任务更有效。",
        "这些信号是功能性 self-report，不是 self-awareness 或 truth；任务多为可验证 benchmark，开放任务、人类基线和分布外校准有限。信号失配时回退外部 evidence、executable verifier 或人工。",
        "Ch66 已把 black-box consistency、token probability、reflexive judge 与 claim-level score 视为观察不同误差面的 sensors，要求按 deployment slice 校准，并把 abstain/human escalation 交给风险策略；新增 appraisal 维度是已有多传感器原则的实例。",
        ("§2；Appendix C–H", "§3.1–3.3；§4；Appendix I–N", "Appendix A.1 Limitations"),
        "no public implementation artifact disclosed in exact-v1",
    ),
    "2605.07937": spec(
        (3, 3, 3), "AGENT-WORKFLOW", "Integrate",
        "Clarification 不只是 ask/assume 二选一；缺失信息类型与已执行轨迹的不可逆程度共同决定提问时点。",
        "论文在 goal/input/constraint/context 四类缺失信息上，于轨迹 10/30/50/70/90% 强制注入 clarification，并用三套长程 Agent benchmark、84 variants、6,000+ runs 和 300 个自然会话估计 timing demand curve。",
        "forced injection 关闭自然询问且只测 demand side，样本、模型和 benchmark 有 floor/crossover；早问会增加打断和无必要澄清，晚问会浪费已提交工作。policy 不确定或 effect 不可逆时回退执行前硬门禁与人工确认。",
        "Ch81 已把 clarification 写成每轮 admission gate，却未让缺失信息类型、trajectory commitment 和 rollback cost 进入 timing state；该增量应补在 ask/assume 之前。",
        ("§3；§4.1–4.5", "§5.1–5.4；Appendix A", "§6 Limitations；Appendix A.7"),
        "code/data promised but no exact public artifact locator disclosed in exact-v1",
    ),
    "2605.07986": spec(
        (2, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "Evaluation identity 必须从抽象 capability 名称落到具体用户、预期 outcome、正负影响、风险和 KPI 的运行场景。",
        "论文以 SME Use Case Worksheet 收集 sector/user/outcome/impact/KPI，再用 LLM 扩展和三阶段人工审阅形成 107 个金融服务场景，并以 rubric 检查 scenario quality 与 operational grounding。",
        "示例限美国金融服务，LLM 扩展与人工 review 不证明场景完备、代表性或 KPI 因果有效；它是 scenario-construction 方法而非模型表现证据。缺少 domain SME 或可测 outcome 时应保留探索性评估。",
        "Ch66 已要求 EvalSpec 冻结 workload/query distribution、intended decision、stage receipts、risk/critical slices、cost/SLO 与 artifact identity，并把 deployment outcome 与 self-report/probe 分开；该 worksheet 是现有 operational-grounding 命题的领域实例。",
        ("§3；§4.1", "§5.2 的 process demonstration 与 validation rubric", "§5.3 Limitations"),
        "no software/data artifact required or disclosed for the adopted methodological claim",
    ),
}


LOCATOR_FIXES = {
    "2605.06733": ("§3.1–3.2 problem/theory；§4.1–4.3 GLoRA algorithm", "§5.1–5.5；Appendix B/C", "§3.2 discussion；§6；experiment scope；无独立 Limitations 标题"),
    "2605.07568": ("§3.1–3.3；§4.1；§5.1；§6.1", "§4.2–4.3；§5.2–5.4；§6.2–6.3；Appendix B/C/E", "§7；实验范围；无独立 Limitations 标题"),
    "2605.07881": ("§3.1–3.7；§4.1–4.5", "§5.1–5.7；§5.9", "§5.8；§5.10；§7"),
}


QUEUE_PAYLOADS = {
    "2605.06919": {
        "insertion_point": "Ch76 的 evidence authority / answer gate 主线中，在 source authority 与最终 confidence 决策之间。",
        "final_prose": "检索排序和来源权威都正确时，最简单的回答器仍可能把文本中‘可能、据称、90%’一律吸收为事实；反过来，低 certainty context 也可能压掉模型原本稳定的先验。RAG answer gate 因而应把三类状态分开：来源表达的 certainty 只是带 provenance 的 claim metadata，模型 prior 只是候选解释，最终 answer confidence 必须由 authority、freshness、corroboration、contradiction 与任务风险共同校准。一个受限交互分支可先要求模型显式给出 prior，再简化复杂 context、重标 certainty 并合成答案；它不能把自报概率升级为真值。该路径以额外 forward、prompt coupling 和概率访问换更细的证据服从，遇到来源自报失真、长上下文、部分正确证据或校准漂移时，应回退逐 claim 引用、冲突展示、外部 verifier 或 abstain。 [受限证据：arXiv:2605.06919v1]",
    },
    "2605.07686": {
        "insertion_point": "Ch56 ‘Reasoning Budget 必须进入调度与评估身份’中，紧接固定预算与按边际收益分配之后。",
        "final_prose": "即使 reasoning budget 已版本化，若它与 final answer 共用同一个 max-output 上限，延长可见 CoT 仍会挤占答案空间：轨迹可能推理正确，却在结论写完前被截断。Scheduler 应分别保存 reasoning allowance、answer reserve、stop/extract policy 与 truncation receipt；split-budget 分支先在有界 reasoning 通道生成 trace，再以独立非思考 extraction pass 产出答案。它用第二次 prefill/forward、选择偏差和更复杂的请求状态换较少 crowd-out，不证明更长推理单调增益。任务很短、无需可见 CoT、trace 本身就是交付物或 tail-SLO 紧张时，共用简单预算仍成立；task crossover 未校准时必须同时保留 no-thinking 与 coupled baseline。 [受限证据：arXiv:2605.07686v1]",
    },
    "2605.07701": {
        "insertion_point": "Ch24 Conditional Guidance 主线中，在固定 CFG 与 prior-guidance 分支之间。",
        "final_prose": "固定 classifier-free guidance scale 在任务和各去噪阶段的控制需求近似稳定时最容易复现；离散文本 diffusion 中，过强 guidance 会牺牲流畅与多样性，过弱又无法满足任务约束，而且最优强度会随 provisional state 改变。可把每一步 scale 视为有界 action，让 policy 读取当前 diffusion state 并在 task-level reward 下学习 guidance trajectory；sampler 仍拥有 token revision 与 commit。该分支用额外策略训练、状态编码和 reward coupling 换 task/step 自适应，也新增 policy drift、terminal-reward shortcut 与不可解释早期锁定。任务、sampler 或 reward revision 改变而未重新校准时，应回退固定 CFG 或保守 heuristic schedule。 [受限证据：arXiv:2605.07701v1]",
    },
    "2605.07769": {
        "insertion_point": "Ch66 Agent evaluation 的 outcome/abstention contract 中，加入 no-op 与 partial-fix 对照切片。",
        "final_prose": "只用‘给 issue 产出 patch’的任务评估 Coding Agent，会把行动本身训练成隐含成功条件；真实队列还包含已修复的 stale issue，此时正确结果是复现后保持 no-op。EvalSpec 应把 needs-action、already-fixed 与 partially-fixed 组成配对切片，分别记录 reproduction evidence、empty/non-empty patch、test outcome、abstention reason 和 technical-debt side effect。这样可以暴露 action bias，却也会引入另一端的过度拒绝：reproduce-before-patch 规则可能把部分修复误判为无需行动。样本身份或仓库 revision 不确定时，应先重建环境并返回 Unknown；不能用 no-op 分数替代真实修复能力，也不能把任何 patch 当积极性证明。 [受限证据：arXiv:2605.07769v1]",
    },
    "2605.07937": {
        "insertion_point": "Ch81 ‘Clarification 与 Workflow-level Speculation 都是有损 Admission’开头，在 ask/assume gate 定义之后。",
        "final_prose": "Clarification gate 还需要时间维度：缺的是 goal 时，早期假设会重写整条 workflow；缺的是某个后续 input 时，等待到相关步骤前可能仍可恢复。Runtime 应把 missing-information type、completed actions、rollback cost、irreversible effects 与 remaining budget 写入同一 admission state，在信息价值跌破继续执行代价前选择 ask，而不是只用一个全程固定阈值。它用更频繁的状态估计和用户中断换减少级联返工，也可能因过早提问造成 friction、因错误 demand curve 过度等待。高风险不可逆动作仍必须执行前硬确认；低风险可撤销步骤可继续采用 assume/proceed，并在 checkpoint 回滚。 [受限证据：arXiv:2605.07937v1]",
    },
}


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def disposition_label(item, queue_status):
    disposition = item["books_disposition"]
    owner = item["owner"]
    path = item["owner_path"]
    rel = "../../../../" + path
    if disposition == "Integrate":
        status = queue_status.get(item["arxiv_id"], "")
        suffix = "等待 root 串行写回" if status == "pending_root_serialized_books_writeback" else "已存在 Books 正文，前次终审通过"
        return f"整合：`{owner}`，[{Path(path).name}]({rel})；{suffix}"
    if disposition == "No Change — Existing Coverage":
        return f"已有覆盖：`{owner}`，[{Path(path).name}]({rel})"
    return f"仅报告：`{owner}`；不改变长期知识"


def main():
    ledger = load(LEDGER)
    evidence_doc = load(EVIDENCE)
    queue_doc = load(QUEUE)
    ledger_by_id = {x["arxiv_id"]: x for x in ledger["entries"]}
    evidence_by_id = {x["arxiv_id"]: x for x in evidence_doc["items"]}
    queue_by_id = {x["arxiv_id"]: x for x in queue_doc["items"]}

    for aid, data in REOPEN.items():
        entry = ledger_by_id[aid]
        entry["v3_status"] = "retained"
        entry["withdrawal_signal"] = "none_in_exact_v1_checked_2026-09-15"
        entry["reason"] = (
            "按 fresh non-author 终审的精确有界清单重开。完整题摘已明确触发 contribution gate："
            + data["claim"] + "；不得在候选分母前关闭。"
        )
        score = data["score"]
        evidence_by_id[aid] = {
            "arxiv_id": aid,
            "source_family_id": entry["source_family_id"],
            "title": entry["title"],
            "primary": f"https://arxiv.org/html/{aid}v1",
            "public_event": PUBLIC_EVENT,
            "review_depth": "deep",
            "access_status": "accessible_exact_v1",
            "withdrawal_status": "not_withdrawn_in_exact_v1_checked_2026-09-15",
            "score": {
                "design_delta": score[0], "system_reach": score[1],
                "durability": score[2], "total": sum(score),
            },
            "adopted_claim": data["claim"],
            "mechanism_and_evaluation": data["mechanism"],
            "non_proof_tradeoff_and_fallback": data["boundary"],
            "owner": data["owner"],
            "owner_path": OWNER_PATHS[data["owner"]],
            "books_disposition": data["disposition"],
            "books_comparison": data["comparison"],
            "evidence_locators": {
                "method": data["locators"][0],
                "evaluation": data["locators"][1],
                "limitations_and_non_proof": data["locators"][2],
            },
            "artifact_status": data["artifact"],
            "reviewed_at": CHECKED_AT,
        }

    # The explicit control stays closed, with a family-specific reason.
    control = ledger_by_id["2605.07726"]
    control["v3_status"] = "pre_denominator_closed"
    control["reason"] = (
        "有界重审后维持 closure：该文组合 TP/PP/sharded-DP 并在 SuperMUC-NG Phase 2 上调参，"
        "披露的是特定 Intel GPU/HPC 软件栈的 recipe、throughput 与 scaling operating point；没有提出独立于"
        "现有 Distributed Training owner 的新状态、控制权、correctness 或 evaluation contract。"
    )

    for aid, locators in LOCATOR_FIXES.items():
        evidence_by_id[aid]["evidence_locators"] = {
            "method": locators[0],
            "evaluation": locators[1],
            "limitations_and_non_proof": locators[2],
        }
        evidence_by_id[aid]["reviewed_at"] = CHECKED_AT

    # The non-author review that produced this bounded repair explicitly passed
    # all fifteen pre-existing body integrations. Remove the stale per-item
    # "pending independent review" wording before appending new root work.
    for queued in queue_by_id.values():
        queued["write_status"] = "applied_root_serialized_books_writeback_verified_previous_fresh_review"

    for aid, payload in QUEUE_PAYLOADS.items():
        item = evidence_by_id[aid]
        queue_by_id[aid] = {
            "source_family_id": item["source_family_id"],
            "arxiv_id": aid,
            "owner": item["owner"],
            "target_path": item["owner_path"],
            "insertion_point": payload["insertion_point"],
            "final_prose": payload["final_prose"],
            "tradeoff_and_fallback": item["non_proof_tradeoff_and_fallback"],
            "evidence_boundary": (
                f"{item['primary']}；Method={item['evidence_locators']['method']}；"
                f"Evaluation={item['evidence_locators']['evaluation']}；"
                f"non-proof={item['evidence_locators']['limitations_and_non_proof']}；"
                f"Artifact={item['artifact_status']}。"
            ),
            "write_status": "pending_root_serialized_books_writeback",
        }

    items = [evidence_by_id[k] for k in sorted(evidence_by_id)]
    queue_items = [queue_by_id[k] for k in sorted(queue_by_id)]
    assert len(items) == 60
    assert all(x["access_status"].startswith("accessible_exact_v1") for x in items)
    assert all(sum(x["score"][k] for k in ("design_delta", "system_reach", "durability")) == x["score"]["total"] for x in items)
    direct_retained = sum(x["receipt_route"] == "official_arxiv_oai_direct" and x["v3_status"] in {"retained", "retained_candidate"} for x in ledger["entries"])
    direct_closed = sum(x["receipt_route"] == "official_arxiv_oai_direct" and x["v3_status"] == "pre_denominator_closed" for x in ledger["entries"])
    revision_closed = sum(x["receipt_route"] != "official_arxiv_oai_direct" for x in ledger["entries"])
    assert (direct_retained, direct_closed, revision_closed) == (60, 575, 191)
    dispositions = Counter(x["books_disposition"] for x in items)
    assert dispositions == Counter({"Integrate": 20, "No Change — Existing Coverage": 38, "Weekly Only — Context": 2})
    pending = [x for x in queue_items if x["write_status"] == "pending_root_serialized_books_writeback"]
    assert {x["arxiv_id"] for x in pending} == set(QUEUE_PAYLOADS)

    ledger["schema"] = "ai-system-design.v3-screening-ledger.bounded-final-audit-repair"
    ledger["summary"].update({
        "retained_candidates": 60,
        "pre_denominator_closed_direct": 575,
        "evidence_accessible_exact_v1": 60,
        "false_negatives_restored": 31,
        "books_integrate": 20,
        "books_applied": 15,
        "books_pending_root": 5,
    })
    ledger["bounded_repair_after_final_review"] = {
        "review_basis": "V3_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_REPAIR_20260915.md",
        "reopened": sorted(REOPEN),
        "control_kept_closed": ["2605.07726"],
        "locator_fixes": sorted(LOCATOR_FIXES),
        "result": "14 retained and deep-reviewed; 5 Integrate queued, 9 No Change with proposition-level comparison",
        "checked_at": CHECKED_AT,
        "completion_authority": "root writeback plus a new non-author fresh-context reviewer",
    }

    dump(LEDGER, ledger)
    dump(EVIDENCE, {
        "schema": "ai-system-design.v3-evidence-review.bounded-final-audit-repair",
        "report_date": "2026-05-11",
        "reviewed_at": CHECKED_AT,
        "items": items,
    })
    dump(QUEUE, {
        "schema": "ai-system-design.v3-books-writeback-queue.root-serialized",
        "report_date": "2026-05-11",
        "status": "15_applied_5_pending_root_writeback_then_fresh_review",
        "items": queue_items,
    })
    dump(COMPARISON, {
        "schema": "ai-system-design.v3-bounded-books-comparison",
        "report_date": "2026-05-11",
        "reviewed_at": CHECKED_AT,
        "scope": sorted(REOPEN),
        "items": [
            {
                "arxiv_id": aid,
                "source_family_id": evidence_by_id[aid]["source_family_id"],
                "owner": evidence_by_id[aid]["owner"],
                "owner_path": evidence_by_id[aid]["owner_path"],
                "disposition": evidence_by_id[aid]["books_disposition"],
                "adopted_claim": evidence_by_id[aid]["adopted_claim"],
                "proposition_level_comparison": evidence_by_id[aid]["books_comparison"],
            }
            for aid in sorted(REOPEN)
        ],
    })

    queue_status = {x["arxiv_id"]: x["write_status"] for x in queue_items}
    source_rows = [
        ("SRC-OPENAI", "Research 历史入口；动态列表无法稳定分页回到本窗", "受阻", "隔离：不支持全站零遗漏；取得 2026-05-10/11 官方归档时只重开该入口"),
        ("SRC-ANTHROPIC", "Research 历史列表；相邻公开事件 05-08 与 05-14", "已检查", "未见已列事件落窗；不扩张为全站证明"),
        ("SRC-GOOGLE-AI", "DeepMind/Google Research 本窗定点检查", "受阻", "历史列表缺日级稳定停止点；隔离"),
        ("SRC-META-AI", "Meta/FAIR publications 本窗定点检查", "受阻", "动态目录缺日级稳定分页；隔离"),
        ("SRC-QWEN", "Qwen 官方历史入口本窗定点检查", "受阻", "旧入口不能稳定回溯；隔离"),
        ("SRC-DEEPSEEK", "News/Research；相邻事件 04-24 与 05-14", "已检查", "未见本窗事件"),
        ("SRC-MOONSHOT", "Kimi Blog 与官方仓库本窗定点检查", "受阻", "无稳定历史日级发现页；隔离"),
        ("SRC-TENCENT-HUNYUAN", "Research‘全部’列表；相邻条目 04-30 与 05-21", "已检查", "未见本窗事件"),
        ("SRC-ZAI", "智谱 Research；相邻条目 04-29 与 05-20", "已检查", "未见本窗事件"),
        ("SRC-BYTEDANCE-SEED", "Seed Research/Publication 与 arXiv identity 交叉检查", "已检查", "目录回填日不替代首次公开"),
        ("SRC-BAIDU-ERNIE", "ERNIE Blog；相邻事件 05-09 08:00+08", "已检查", "早于本窗，不重复"),
        ("SRC-XIAOMI-MIMO", "MiMo Papers 与 Blog 历史入口", "受阻", "Papers 可排除；Blog 卡片缺可复查历史时刻；隔离"),
        ("SRC-MINIMAX", "Research/Blog；相邻事件 03-18 与 05-26", "已检查", "未见本窗事件"),
        ("SRC-ARXIV", "官方 2026-05-11 08:00+08 announcement；635 direct + 191 ordinary revision identities 完成题名/完整摘要筛选；60 candidate exact-v1 Evidence Review", "已检查", "无 exact-v1 material blocker；191 ordinary revisions 无 important-revision signal"),
    ]
    report = [
        "# Daily Research — 2026-05-11", "",
        "**规范：** V3", "**窗口：** 2026-05-10T09:00:00+08:00 ～ 2026-05-11T09:00:00+08:00",
        "**状态：** 进行中", "**Books：** 纳入本次", f"**检查时间：** {CHECKED_AT}", "",
        "## 1. 结论", "",
        "本轮严格响应 fresh non-author 终审的精确有界清单：没有扩窗、扩来源或重扫全量。826 个 identity 仍由 635 个 arXiv official-announcement direct 与 191 个 ordinary revision 构成；14 个指定项完成题名、完整摘要、exact-v1、撤稿、方法、评价、限制、artifact 和 owner 对照后进入候选，`2605.07726` 以 family-specific 理由维持 closure。当前 direct 算术为 635 = 60 candidate + 575 pre-denominator closure。", "",
        "60 个候选均有 exact-v1 Evidence Review；Books 判断为 20 Integrate、38 No Change、2 Weekly Only。原有 15 个 Integrate 的 Books 正文已由前次 fresh review 通过；新增 5 个 Integrate 只进入 root 写回队列，本轮没有编辑 Books。报告保持进行中，只有 root 写回完成并由新的非作者 reviewer 验证后才能 Complete。", "",
        "## 2. 来源覆盖", "",
        "本轮沿用已经冻结的来源与窗口，只返修终审点名项目；下列 coverage 不构成新的来源重放。", "",
        "| 来源 | 检查范围与依据 | 结果 | 缺口 |", "| --- | --- | --- | --- |",
    ]
    report.extend(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in source_rows)
    report += ["", "## 3. 候选与判断", "", "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |"]
    for item in items:
        score = item["score"]
        report.append(
            f"| [{item['title']}]({item['primary']}) | 2026-05-11T08:00:00+08:00 | {item['adopted_claim']}；"
            f"{score['design_delta']} + {score['system_reach']} + {score['durability']} = {score['total']} | "
            f"{'深入完成' if item['review_depth'] == 'deep' else '标准完成'} | {disposition_label(item, queue_status)} |"
        )
    report += ["", "## 4. 证据与知识整合", "",
               "以下结论均绑定 exact-v1。详细筛选理由见 [screening ledger](../_sources/daily-20260511/V3_SCREENING_LEDGER_20260914.json)，逐项证据见 [Evidence reviews](../_sources/daily-20260511/V3_EVIDENCE_REVIEWS_20260914.json)，本轮命题级对照见 [bounded comparison](../_sources/daily-20260511/V3_BOUNDED_REPAIR_BOOKS_COMPARISON_20260915.json)。", ""]
    for item in items:
        loc = item["evidence_locators"]
        report += [
            f"### [{item['title']}]({item['primary']})", "",
            f"**采用命题：** {item['adopted_claim']}", "",
            f"**机制与评价：** {item['mechanism_and_evaluation']}", "",
            f"**证据位置：** Method：{loc['method']}；Evaluation：{loc['evaluation']}；Limitations / non-proof：{loc['limitations_and_non_proof']}。Artifact：{item['artifact_status']}。", "",
            f"**未证明、代价与回退：** {item['non_proof_tradeoff_and_fallback']}", "",
            f"**Books 比较：** {item['books_comparison']}", "",
            f"**最终处置：** {disposition_label(item, queue_status)}。", "",
        ]
    report += [
        "## 5. 缺口与下一步", "",
        "本次有界返修没有 exact-version primary material blocker，也没有新增用户材料请求。", "",
        "下一步严格只有两项：", "",
        "1. root 按日期与目标文件冲突顺序写入 `2605.06919`、`2605.07686`、`2605.07701`、`2605.07769`、`2605.07937` 五个 queue item；本作者不编辑 Books。",
        "2. 写回后由未参与本轮返修的新 reviewer 做 fresh-context 终审，复核 60/575 算术、14 个恢复项、3 个 locator 修正、20 项 Books disposition 与实际正文。", "",
        "## 6. 复核", "",
        "**复核者：** 等待新的非作者 reviewer（本次作者不能自签）", "",
        "**结论：** 未通过 Complete Gate（有界作者返修完成；等待 5 项 root 写回与 fresh review）", "",
        "本轮机器校验只证明 JSON、评分、分母算术、唯一 owner、链接字段与 Markdown 结构一致；它不能替代 Books 写回或独立语义审阅。", "",
        "**Repository Changes：** 更新本 Daily、V3 screening ledger、Evidence reviews 与 root queue；新增本轮 comparison、root synthesis 和 author checkpoint。未编辑 Books，未 stage、commit 或 push。", "",
    ]
    REPORT.write_text("\n".join(report))

    SYNTHESIS.write_text("\n".join([
        "# 2026-05-11 有界返修：root Books 写回清单", "",
        "本文件只汇总新增五项；权威 prose、位置与 evidence boundary 位于 `V3_BOOKS_WRITEBACK_QUEUE_20260914.json`。", "",
        *[f"- `{aid}` → `{evidence_by_id[aid]['owner']}` / `{evidence_by_id[aid]['owner_path']}`：{QUEUE_PAYLOADS[aid]['insertion_point']}" for aid in sorted(QUEUE_PAYLOADS)], "",
        "作者侧未编辑 Books。root 写回后仍需新的非作者 fresh-context reviewer；当前 Daily 必须保持 Ongoing。", "",
    ]))
    CHECKPOINT.write_text("\n".join([
        "# 2026-05-11 有界作者返修 checkpoint", "",
        f"- checked at: {CHECKED_AT}",
        "- scope: 12 definite false negatives + 2 bounded re-reviews + 3 locator fixes；未扩窗/扩源/全量重扫",
        "- exact-v1 / withdrawal: 17/17 已核对；无材料 blocker；无 withdrawn signal",
        "- retained: 60（返修前 46；新增 14）",
        "- direct closures: 575（返修前 589）；2605.07726 维持 closure",
        "- disposition: 20 Integrate / 38 No Change / 2 Weekly Only",
        "- Books: 15 已存在且前次终审通过 / 5 pending root；本作者未编辑 Books",
        "- locator fixes: 2605.06733 / 2605.07568 / 2605.07881",
        "- state: Ongoing；等待 root 写回与新的非作者 fresh review", "",
    ]))


if __name__ == "__main__":
    main()
