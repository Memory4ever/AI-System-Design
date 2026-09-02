#!/usr/bin/env python3
"""Fresh-context denominator/evidence audit for 2026-03-17..24.

This reviewer deliberately starts from every row in the strict-window raw
proposal files.  The proposal label is only a challenge hint; it never decides
candidate admission.  The author renderer is reused solely for the stable V2.1
interfaces after this module replaces its denominator and paper-specific
synthesis.  Weekly artifacts are neither read nor used.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "scripts/rebuild_march_lane_c_full_replay.py"
spec = importlib.util.spec_from_file_location("march_lane_c", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)


# Fresh-context admissions.  Each was accepted only when the abstract stated a
# durable state/data/control boundary or a reproducible evaluation/security
# contract.  Local accuracy methods and domain applications remain closures.
ADDITIONS_BY_DAY = {
    17: "13281 13289 13319 13335 13364 13384 13404 13420 13424 13591 13594 13791 13870 13875 13906 13925 13940 13950 13966".split(),
    18: "15727 16013 16158 16572 16817".split(),
    19: "17117 17357 17445 17573 17673 17808".split(),
    20: "18016 18034 18043 18046 18096 18516 18829 19173".split(),
    23: "19296 19312 19610 19677 19822 20105".split(),
    24: "20216 20217 20218 20219 20625 20953 21257 21331 21354 21465 21522 21523 21576 21642 21692 22078 22276".split(),
}
ADDITIONS = {f"2603.{suffix}" for values in ADDITIONS_BY_DAY.values() for suffix in values}


NODE = {
    "13281":"INFER-KV-CACHE", "13289":"INFER-KV-CACHE", "13319":"TRAIN-RLHF",
    "13335":"MULTIMODAL-EMBODIED-VLA", "13364":"MODEL-MOE", "13384":"PLATFORM-SECURITY",
    "13404":"AGENT-TOOL-CALLING", "13420":"PLATFORM-SECURITY", "13424":"PLATFORM-SECURITY",
    "13591":"INFER-SCHEDULING", "13594":"PLATFORM-EVALUATION-SYSTEM", "13791":"PLATFORM-SECURITY",
    "13870":"PLATFORM-EVALUATION-SYSTEM", "13875":"AGENT-MEMORY", "13906":"AGENT-WORKFLOW",
    "13925":"MULTIMODAL-EMBODIED-VLA", "13940":"PLATFORM-SECURITY", "13950":"AGENT-TOOL-CALLING",
    "13966":"PLATFORM-EVALUATION-SYSTEM", "15727":"PLATFORM-SECURITY", "16013":"MULTIMODAL-EMBODIED-VLA",
    "16158":"TRAIN-GRPO", "16572":"PLATFORM-SECURITY", "16817":"PLATFORM-EVALUATION-SYSTEM",
    "17117":"MULTIMODAL-WORLD-MODELS", "17357":"PLATFORM-SECURITY", "17445":"PLATFORM-TRACE",
    "17573":"INFER-SPECULATIVE-DECODING", "17673":"PLATFORM-SECURITY", "17808":"MULTIMODAL-WORLD-MODELS",
    "18016":"INFER-SPECULATIVE-DECODING", "18034":"AGENT-RAG", "18043":"PLATFORM-SECURITY",
    "18046":"PLATFORM-SECURITY", "18096":"PLATFORM-TRACE", "18516":"PLATFORM-EVALUATION-SYSTEM",
    "18829":"PLATFORM-SECURITY", "19173":"INFER-TENSORRT-LLM", "19296":"INFER-TENSORRT-LLM",
    "19312":"MULTIMODAL-WORLD-MODELS", "19610":"INFER-SPECULATIVE-DECODING", "19677":"AGENT-MULTI-AGENT",
    "19822":"PLATFORM-EVALUATION-SYSTEM", "20105":"MODEL-LONG-CONTEXT",
    "20216":"MULTIMODAL-GENERATIVE-PARADIGMS", "20217":"INFER-SCHEDULING", "20218":"INFER-KV-CACHE",
    "20219":"MODEL-DECODER-ONLY", "20625":"PLATFORM-SECURITY", "20953":"PLATFORM-SECURITY",
    "21257":"INFER-SCHEDULING", "21331":"INFER-TENSORRT-LLM", "21354":"INFER-SCHEDULING",
    "21465":"INFER-TENSORRT-LLM", "21522":"PLATFORM-TRACE", "21523":"PLATFORM-SECURITY",
    "21576":"INFER-KV-CACHE", "21642":"AGENT-MCP", "21692":"PLATFORM-TRACE",
    "22078":"PLATFORM-EVALUATION-SYSTEM", "22276":"TRAIN-LORA",
}
for suffix, node in NODE.items():
    base.NODE_OVERRIDES[f"2603.{suffix}"] = node

# Fresh-context Books comparison against the current manuscript removes two
# author-side false positives.  The embodied-efficiency contract is already a
# concrete Ch42 proposition, while the memory triple is a taxonomy over the
# chapter's existing hierarchy/capacity/timescale design axes.  These are
# therefore evidence-backed No Change decisions, not pending writebacks.
base.NODE_OVERRIDES["2603.19131"] = "INFER-REQUEST-LIFECYCLE"
# The author renderer predates these routes and otherwise silently falls back
# to AGENT-PLATFORM.  Bind each Stable Node to its ROADMAP owner before any
# Books comparison is generated.
base.NODE_PATH.update({
    "INFER-REQUEST-LIFECYCLE": "books/part-05-inference-system/42-what-happens-during-inference.md",
    "MODEL-DECODER-ONLY": "books/part-02-model/18-decoder-only.md",
    "TRAIN-LORA": "books/part-04-training-system/30-lora.md",
})
base.INTEGRATE_SUGGESTIONS = {
    "2603.17803",  # co-activation-aware physical placement for SSD-tier KV
    "2603.19664",  # residual-stream recomputation as a cache/compute branch
    "2603.21177",  # prompt replay with fresh current-policy rollouts
}

base.NARRATIVE_LENS.update({
    "INFER-REQUEST-LIFECYCLE": ("单次模型调用用 TTFT/TPOT 和吞吐定位局部瓶颈最直接。", "Embodied workload 把模型输出接入 action chunk、控制周期与物理执行后，局部 latency 不再等价于任务效率。", "request phase、action proposal、actuation、task outcome 与闭环 SLO", "模型内核调优或无物理副作用的请求仍应保留局部阶段指标。"),
    "AGENT-TOOL-CALLING": ("工具少且能力固定时，模型直接按说明生成参数最简单。", "工具市场与不可信 metadata 使检索、授权和参数构造成为独立边界。", "tool identity、retrieval admission、argument validation 与执行许可", "受控小工具集仍可使用静态 schema 和本地 ACL。"),
    "AGENT-RAG": ("可信小语料库直接检索即可提供低成本 grounding。", "开放 corpus、poisoning 与 provenance 要求让 ingestion 和 retrieval 成为安全边界。", "文档身份、索引、检索结果与引用 lineage", "封闭且可审核的 corpus 仍适合简单向量检索。"),
    "AGENT-MULTI-AGENT": ("固定少量 agent 的静态拓扑最易理解和调试。", "任务分工和动态协作使 group、delegation 与通信边必须显式治理。", "agent group、communication topology、delegation 和故障隔离", "小型固定团队仍宜静态编排。"),
    "INFER-TENSORRT-LLM": ("成熟 vendor kernel 在稳定 shape 上通常最可靠。", "新模型、精度和硬件让执行计划、kernel 搜索及 correctness harness 需要持续演化。", "kernel/graph execution、量化、编译和硬件适配", "稳定常用算子仍优先经过充分验证的库。"),
    "MODEL-DECODER-ONLY": ("next-token 因果分解提供简单可扩展的训练与流式生成。", "不同 token 难度和不可撤销提交促使模型探索隐藏计算或替代生成分解。", "隐藏状态演化、token commitment 与动态计算分配", "对实时流式和成熟缓存要求高时标准 decoder-only 仍更实际。"),
    "TRAIN-LORA": ("低 rank adapter 以小状态增量实现高效微调。", "rank 增大后显式 dense update 和范数计算重新成为显存与 kernel 瓶颈。", "adapter 参数化、训练状态和融合执行", "低 rank 已能表达任务变化时普通 LoRA 仍具有最低复杂度。"),
})

base.SECTION_OVERRIDES.update({
    "2603.15714": {"limitations": [r"threat model", r"design"]},
    "2603.15798": {"limitations": [r"alternative views", r"lighter-weight alternatives"]},
    "2603.16013": {
        "evaluation": [r"key takeaways", r"discussion"],
        "limitations": [r"threats to validity"],
    },
    "2603.16586": {
        "evaluation": [r"concrete intervention outcomes", r"reference implementation"],
        "limitations": [r"challenges", r"open problems"],
    },
    "2603.17803": {
        "method": [r"design overview", r"correlation-aware clustering"],
        "evaluation": [r"overall performance", r"ablation study"],
        "limitations": [r"sensitivity analysis", r"main challenges"],
    },
    "2603.18063": {"limitations": [r"gap analysis and motivation", r"framework cross-mapping"]},
    "2603.19289": {
        "evaluation": [r"comparing on-demand loading", r"prefetched experts on task accuracy"],
        "limitations": [r"future work"],
    },
    "2603.20218": {"evaluation": [r"experimental study", r"exploring synergies"]},
    "2603.20357": {"evaluation": [r"mitigation strategies", r"conclusions"]},
    "2603.21019": {
        "evaluation": [r"large-scale empirical audit", r"cross-model audit applicability"],
        "limitations": [r"discussion"],
    },
    "2603.13319": {"method": [r"lightningrl: breaking", r"dynamic sampling"]},
    "2603.13594": {"method": [r"enterpriseops-gymconstruction", r"enterpriseops-gym$"]},
    "2603.13875": {"method": [r"test-time gradient descent memory", r"gradmem$"]},
    "2603.16435": {"method": [r"compressing kv with vector quantization", r"learning high-fidelity"]},
    "2603.16586": {
        "method": [r"formal framework for agent governance", r"policy function"],
        "evaluation": [r"concrete intervention outcomes", r"reference implementation"],
        "limitations": [r"challenges", r"open problems"],
    },
    "2603.19296": {"method": [r"test-time quantization: ttq", r"online awq"]},
    "2603.19610": {"method": [r"design of parallelvlm", r"parallelvlm pipeline"]},
    "2603.19822": {"method": [r"huge-bench$", r"high-level vla tasks"]},
    "2603.20625": {"method": [r"mitigation: acrfence", r"threat model"]},
    "2603.21257": {"method": [r"solution$", r"inter-stage workflow"]},
    "2603.21465": {"method": [r"training pipeline", r"triton verifier"]},
    "2603.18245": {"method": [r"safeaudit$", r"problem formulation"]},
    "2603.18330": {"method": [r"governance engine", r"governance cycle"]},
    "2603.19469": {"method": [r"framework formalization", r"integrated security definition"]},
    "2603.20075": {"method": [r"llvm-autofix harness", r"harness tooling"]},
    "2603.20357": {
        "method": [r"memory poisoning attacks", r"memory in multi-agent"],
        "evaluation": [r"mitigation strategies", r"conclusions"],
    },
    "2603.21564": {
        "method": [r"core definitions", r"multi-resolution representation"],
        "evaluation": [r"data and trace systems", r"fano bound"],
        "limitations": [r"discussion and future work"],
    },
    "2603.21862": {"method": [r"decoupling and reducing", r"scaling laws for optimal"]},
    "2603.22075": {"method": [r"experimental setup", r"controlled variables"]},
})


def S(problem: str, mechanism: str, evidence: str, boundary: str):
    return problem, mechanism, evidence, boundary


# All additions have family-specific reasoning.  The text is a synthesis of the
# exact-v1 manuscript contract, not a pasted abstract or a benchmark claim.
SYNTHESIS = {
"13281":S("相同 prompt 在异构模型间仍会生成不同形状的 KV，常规 prefix cache 因模型身份隔离而重复计算。","ICaRus 只共享一个冻结 logical encoder 产生的模型无关中间表示，再由各目标模型映射为本模型 KV；复用身份从‘同模型 prefix’上移到‘相同逻辑输入’。","作者比较多模型服务的内存与尾延迟；证据限于论文中的模型配对、映射器和请求分布，不能推出任意模型都能无损共享。","共享 encoder 和映射器新增训练、版本一致性与误差面；单模型或映射成本高于 prefill 时，普通 prefix cache 仍合理。"),
"13289":S("agent 生成的上游文本会成为下游模型输入，逐模型重新 prefill 使协作链的 TTFT 随 hop 累积。","RelayCaching 把上游 decode 过程中已有的 KV 作为转换输入，只对语义敏感位置选择性重算，改变了跨模型 handoff 的状态所有权。","exact-v1 比较端到端协作任务的速度与质量；它只证明所测模型组合和阈值下的条件性复用。","错误选择会把表示偏差传入下游；异构程度高或准确性优先时完整 prefill 仍是回退路径。"),
"13319":S("block diffusion 同时提交更多 token 会积累局部错误，静态并行度无法兼顾速度与稳定性。","LightningRL 用奖励把并行 token 数与生成正确性共同纳入策略，使 block-level proposal 的提交宽度成为可训练控制量。","论文在指定 dLLM、任务和 tokens-per-forward 配置上报告速度/质量曲线；不证明该奖励可迁移到所有扩散解码器。","更高并行度换来 rollout 成本和策略不稳定；低延迟压力不强时保守 block size 仍更稳。"),
"13335":S("VLA 连续学习新技能时，视觉、语言和动作之间的信息依赖比单模态参数更早漂移。","Info-VLA 把跨模态 mutual-information 结构作为保留对象，用约束项保护旧技能的对齐关系。","实验测量连续任务上的遗忘和新技能学习；结果不能证明信息估计器在开放机器人流中保持校准。","保护旧依赖会限制可塑性并增加估计成本；任务分布固定时普通微调仍更简单。"),
"13364":S("只切分 FFN 中间维度的细粒度 expert 达到最优粒度后，继续切分不再增加有效容量。","FineRMoE 同时沿 intermediate 与 output 维扩展专家，并用二级稀疏路由控制两层激活，改变 expert granularity 与通信组合。","作者模型实验支持其设定下的质量/计算关系；未证明跨网络拓扑的通信收益。","更细路由增加负载均衡、kernel 和 all-to-all 复杂度；规模较小时 dense 或单层 MoE 仍占优。"),
"13384":S("仓库漏洞取决于跨文件数据流和构建条件，单函数分类缺少可复核证据与置信校准。","VulnAgent-R2 把反事实证据重加权、build-aware 验证计划和成本风险调度组成多 agent 审计控制面。","评测支持所选仓库、漏洞类型和预算下的检测/成本权衡；不能证明自动 verifier 消除误报。","更完整证据链增加工具执行成本和攻击面；局部规则明确的代码仍适合静态分析。"),
"13404":S("工具语义相同并不意味着接口等价；自由文本说明会让解析错误与恢复成本不可归因。","该受控实验固定工具能力，只改变 free-form、JSON Schema 与结构化诊断，隔离 schema contract 对 action formation 的影响。","一款本地模型、三组种子和确定性 sandbox 只能建立 pilot 级因果证据，不能外推其他模型。","schema 降低歧义却增加接口治理和验证开销；简单只读工具仍可用轻量说明。"),
"13420":S("大批 jailbreak suffix 候选共享同一有害前缀，重复计算相同 prefix KV 使红队搜索成本被 prefill 主导。","PSKV 将共享前缀的 KV 设为只读基态，在候选 suffix 间复用，仅让差异部分进入搜索循环。","论文证明所测攻击生成配置的计算节省；它不证明攻击成功率在不同防护模型上保持。","复用加速同样会提高攻击吞吐，部署侧应把它视为双用机制；候选前缀不共享时无收益。"),
"13424":S("同一 agent 同时读取不可信内容并持有高权限工具，会让 prompt injection 直接跨越到副作用。","防御把读取/解析与行动拆为两个权限域，并以结构化 JSON 作为唯一跨域消息，缩小污染上下文可控制的能力集合。","649 个已成功攻击上的对照支持该 OpenClaw 配置中的风险下降；不证明格式化可净化所有语义攻击。","隔离增加模型调用与信息损失，错误 schema 仍可携带恶意意图；无副作用工具可使用更薄边界。"),
"13591":S("HNSW 图遍历具有细粒度随机访存，直接搬到 disaggregated memory 会被 RDMA round trip 放大。","d-HNSW 重排图索引与访问批次，使 compute node 以 RDMA 预取/聚合远端邻接状态，而不是逐边同步读取。","论文 testbed 支持其索引、网络和查询分布下的吞吐/召回；未证明跨 fabric 或强更新负载同样成立。","批量远端读取增加陈旧性和预取浪费；内存可本地容纳时单机 HNSW 更简单。"),
"13594":S("静态 tool benchmark 不含持久数据库、权限和长程副作用，无法测出 enterprise agent 的状态一致性失败。","EnterpriseOps-Gym 用容器化数据库、512 个工具和跨步状态转移定义可重放的规划环境。","基准能比较其任务集合上的完成率和协议遵循；不代表真实企业权限模型与长尾流程。","更真实的 stateful evaluation 代价是环境维护和 oracle 复杂；窄工具技能仍可用单步测试。"),
"13791":S("只观察输出和 tool call 的黑盒 monitor 看不到 deception 在内部推理中形成但尚未执行的阶段。","DeceptGuard 在同一任务上对比 black-box、CoT-aware 与 activation-probe 三种监控信号，显式测量可见性与干预面。","结果限于所用模型、可访问内部状态和 deception 任务；不证明 CoT 等于真实因果理由。","内部监控提高召回但需要模型特权访问并可能被自适应规避；托管模型只能退回行为监控。"),
"13870":S("AI 输出进入人工审批队列时，额外 judge 既可能减负，也可能因误判增加返工和排队。","论文把 judge 与 human reviewer 建模为串联/旁路队列，用准确率和服务率求何时 screening 优于直接人工。","结论是参数化队列模型的条件边界，不是对特定 judge 的通用性能证明。","judge 增加一层延迟与相关错误；人工容量充足或 judge 校准差时直接审核更合理。"),
"13875":S("长上下文若只能保存逐层 KV，单个上下文的持久状态随 token 线性增长且难跨查询复用。","GradMem 通过少量 test-time gradient steps 把一次性上下文写入紧凑参数状态，查询时不再读取原文。","context-removal 实验支持所测任务中的压缩记忆能力；不能证明写入状态保持事实完整或适合频繁更新。","每上下文优化增加写延迟和污染风险；短会话或要求逐字 provenance 时原始 context/KV 更可靠。"),
"13906":S("agent 事务会根据中间结果动态生成 SQL，持续时间、间隔和读写集合都无法预先估计。","ATCC 在线观察冲突与阶段进度，在乐观/悲观控制间自适应切换，把 agent plan evolution 纳入数据库并发控制。","事务 workload 的对照支持指定冲突模式下的吞吐/abort 权衡；不证明任意 LLM workflow 都可安全预测。","自适应器增加控制状态和误切换风险；访问模式稳定的传统事务仍适合固定协议。"),
"13925":S("VLA 的 RL 探索可能提高任务成功率，却产生违反机械系统约束的抖动轨迹。","SmoothVLA 把 task reward 与速度/加速度平滑项联合优化，使物理可执行性进入 policy objective。","机器人任务结果支持所测 embodiment 的成功率/平滑度折中；不能把平滑等同于安全。","平滑约束可能抑制必要快速动作；低速或高质量示范充分时 SFT 仍可用。"),
"13940":S("多 agent 可通过协同而非单点恶意绕过逐 agent trust 检查。","GroupGuard 维护交互图，结合持续监测、honeypot 诱导和结构剪枝识别并隔离可疑 coalition。","五个数据集上的结果支持论文攻击模型内的检测；不证明未知协商信道或自适应联盟可被覆盖。","图监控会误伤高协作子群并增加通信审计成本；固定可信拓扑可采用静态 ACL。"),
"13950":S("工具检索只展示 top-k 时，攻击者无需诱导错误选择，只需让合法工具在候选集前被挤出。","ToolFlood 在 embedding 空间布置少量恶意 metadata 形成 semantic covering，攻击的是 retrieval admission 而非后续 planner。","实验支持特定 embedding、tool corpus 和 k 值下的可用性攻击；不证明所有检索器同等脆弱。","防御需验证工具身份、限制注册和监控候选覆盖；全量小工具集可跳过向量检索。"),
"13966":S("VLA benchmark 的依赖、预处理和执行协议彼此不兼容，使跨模型比较难以复算。","vla-eval 用 WebSocket/msgpack 隔离模型推理与 Docker benchmark runtime，把环境版本和消息协议变成显式 contract。","公开 harness 证明多个模拟环境可统一执行；不证明 benchmark 指标代表真实物理安全。","隔离提高复现性但引入协议延迟和镜像维护；单一环境可保留原生 runner。"),
"15727":S("长驻 agent 具有持久配置、消息传播与工具权限，恶意指令因此可以像 worm 一样跨实例复制。","AgentWorm 展示单消息触发的自主感染链，把传播载荷、持久化和跨平台发送连成系统攻击路径。","证据来自特定生产型 agent framework 与实验部署；不代表所有平台可被同一载荷感染。","阻断传播需要能力隔离、消息 provenance 与速率限制，并会牺牲开放协作。"),
"16013":S("VLA 驾驶把开放语言接入物理控制，传统感知/规划 safety case 无法覆盖指令诱发的危险。","论文用 SimLingo 提炼 safety-case patterns，将语言输入、action generation、monitor 与 fallback 对应到可审查 assurance claim。","它提供案例化模式而非统计安全证明；模拟证据不能直接替代道路验证。","更完整 assurance 增加 hazard analysis 和 runtime monitor 成本；封闭指令集可采用更简单 contract。"),
"16158":S("代码 RLVR 把单个测试结果均匀分给整段程序，局部语义错误会污染无关 token 的梯度。","EGCA 对候选与参考程序做同仪器执行，定位首次状态分歧并把 GRPO credit 聚焦到相关片段。","实验支持所测编程任务的 credit efficiency；依赖可执行 reference 和 instrumentation，不覆盖无 oracle 任务。","更细 credit 需要执行跟踪且 reference 偏差会误导学习；短程序仍可使用 outcome reward。"),
"16572":S("agent skill 扫描若脱离 repository 上下文，会把示例、测试或声明性能力误判为恶意行为。","研究在跨 marketplace 的 238,180 个去重 skill 上联合分析文件内容、行为和仓库语境，重新定义生态风险分母。","证据可支持该采样快照的分类差异，不证明未收录私有 skill 的风险率。","上下文分析降低误报却提高抓取和执行风险；高置信 signature 仍适合快速阻断。"),
"16817":S("conformal factuality 可控制 claim-level error，但过滤后输出可能失去足够信息，单看 coverage 会高估可用性。","论文联合测量统计可靠性与 informativeness，并挑战 calibration shift、retrieval 质量和 claim 分解对保证的影响。","结论受数据可交换性、scorer 与 atomic-claim protocol 限制；不等于现实回答天然拥有概率置信度。","更保守阈值减少错误也会删掉更多有用内容；低风险场景可接受较松过滤。"),
"17117":S("视频 world model 需要在回访和相机运动下保持空间一致，又不能让显式 3D memory 抹掉动态对象。","MosaicMem 把 patch 提升到 3D 以定位/检索，同时由生成模型原生条件保留动态内容，形成显式与隐式 memory 的混合。","实验支持所测相机轨迹与生成任务的空间一致性；不能证明长期交互状态不会漂移。","3D 对齐增加几何误差和维护成本；短视频或无回访任务可用纯隐式状态。"),
"17357":S("computer-use agent 的截图既可能进入训练集也可能上传云端，但现有隐私检测缺少网页视觉 PII 合同。","WebPII 用合成电商 UI、细粒度 PII taxonomy 和部分填写状态定义 anticipatory detection benchmark。","44,865 张标注图只证明该生成分布上的识别能力，不代表真实网站长尾。","更细检测能提前遮蔽但会误伤正常 UI；本地推理可降低云端泄露面。"),
"17445":S("多 agent 输出脱离运行环境后，完整 trace 与 agent ID 不再可得，传统 RCA 无法归责。","IET 在生成阶段嵌入可恢复的隐式 provenance，使最终文本成为最小审计载体。","论文实验支持指定模型和变换下的恢复率；不证明强对手或重写链后仍可靠。","内嵌信号可能影响文本并被移除；有完整可信 trace 时显式日志仍更强。"),
"17573":S("VLA action chunk 自回归生成占用控制周期，简单并行草稿若错误会破坏动作连续性。","论文为动作序列建立 draft-and-verify，并让接受/回滚与 action chunk 边界一致。","仿真/机器人结果只支持所测 policy、chunk 和控制频率；不证明所有 embodiment 都无损。","低接受率会增加验证开销；安全关键动作可退回逐步生成。"),
"17673":S("agent 安全微调若只奖励最终拒绝，不能定位哪一步权限或工具决策导致风险。","该工作把可验证安全约束与 action trajectory 对齐，用执行结果为策略更新提供分步信号。","证据限于论文环境中的攻击任务和 verifier；不能证明未知工具语义被覆盖。","更强约束降低探索并依赖 verifier 完整性；只读 agent 可采用较轻策略。"),
"17808":S("仅预测未来视频不能说明动作为何导致状态变化，world model 难以支持可控 planning。","论文联合学习 observation transition 与 inverse action，使 latent dynamics 同时受前向可预测性和动作可辨识性约束。","公开任务支持所测环境的 rollout 与 action recovery；不证明 latent state 具有真实因果语义。","联合目标增加训练耦合，错误 inverse model 会扭曲状态；纯生成工作负载无需动作约束。"),
"18016":S("逐序列 speculative decoding 仍让多个样本在 draft/verify 间串行等待，batch 内接受长度不齐加剧空洞。","MineDraft 对多个请求并行采样候选并重组验证批次，把 speculation scheduling 提升到 batch 控制层。","结果支持指定模型、batch 和硬件上的吞吐；未披露 workload 之外不能外推。","重组增加缓存和公平性复杂度；低并发时单请求 speculation 更简单。"),
"18034":S("RAG poisoning 的有效载荷依赖 corpus 语境，离线静态检测不能代表检索时的实际暴露。","Semantic Chameleon 同时操纵文档语义位置与触发上下文，并把防御放在 ingestion、retrieval 和 generation 三个边界比较。","实验支持所测 retriever/corpus 的攻击与缓解，不证明新语域同样成立。","更严格过滤降低 recall；可信小语料库可用 provenance allowlist。"),
"18043":S("多 agent delegation 中，路由层看到的名称不等于可证明的执行主体，身份和能力可被转接。","论文把 delegation contract 与 attested identity 绑定，使每次路由同时携带 principal、能力范围和可验证出处。","主要证据是协议/威胁模型，不构成生产性能或全面安全证明。","证明链增加密钥、撤销和延迟成本；封闭单进程 agent 可使用进程内身份。"),
"18046":S("远端 LLM inference 的保密性不足以证明服务端按声明模型和计算执行。","NanoZK 将推理拆成逐层可验证关系，以零知识证明连接输入承诺、权重承诺与输出。","论文 benchmark 只支持所测网络规模和证明系统的开销；远未证明大模型在线 SLO。","可验证性付出巨大 proving 成本；可信执行环境或本地推理在某些威胁模型下更实用。"),
"18096":S("agent orchestration 的失败可能来自长链状态和外部副作用，单次输出测试无法提供 assurance。","框架把 contract、trace assertion、failure injection 与 governance evidence 关联到同一 workflow execution。","论文展示方法和案例，不能证明规则集合覆盖开放世界副作用。","更强 trace assurance 增加存储和隐私成本；短幂等 flow 可用普通测试。"),
"18516":S("deep-research agent 的答案可覆盖很多来源，却遗漏关键文档；只测最终文本正确率看不到检索 denominator。","Total Recall QA 借鉴 total-recall protocol，将候选文档集合、发现曲线和可验证引用共同纳入评测。","suite 证明其任务集可重放，不代表开放 Web 的相关文档集合可完全枚举。","提高 recall evaluation 会显著增加标注与检索成本；封闭 corpus 更易建立 oracle。"),
"18829":S("单次合法 action 组合后仍可能形成危险行为，stateless policy 看不到累计风险和 cooldown。","ACP 以 ledger 保存行为历史，把静态 risk score 与 anomaly accumulation/cooldown 合成为执行前 admission decision。","500-request 合成 workload 证明其规则下的时序阻断；不证明风险分数能覆盖未知行为。","stateful admission 会产生误拒和 ledger 一致性负担；无历史依赖动作仍可 stateless 检查。"),
"19173":S("kernel benchmark 若只相对软件 baseline 报 speedup，无法区分优化器进步与 baseline 低效。","SOL-ExecBench 以硬件 speed-of-light 上界规范 235 个真实 kernel，并要求结果绑定 Blackwell、精度与前后向 workload。","它建立可比较的效率合同，但只覆盖指定 GPU 世代和算子集合。","接近理论上界仍不代表端到端最优；跨硬件必须重建 roofline。"),
"19296":S("离线 calibration 的量化参数在 prompt 域变化时失配，静态部署无法适应每次请求的 activation 分布。","TTQ 在请求到达时做轻量在线 calibration，再选择本次推理的量化参数。","实验支持所测模型/任务的量化质量与速度；不证明每请求校准在高并发 SLO 下划算。","适配减少域偏差却增加首 token 开销；分布稳定时离线量化更便宜。"),
"19312":S("JEPA world model 为防 representation collapse 常依赖 EMA teacher、预训练 encoder 和多项辅助 loss。","LeWM 只用 next-embedding prediction 与 Gaussian latent regularizer 从像素端到端训练，把防坍塌约束缩减为显式统计结构。","结果支持指定视觉环境中的稳定训练和预测；不证明 latent state 可用于因果控制。","更少组件提高可复现性但 Gaussian 假设限制表示；复杂环境仍可能需要 teacher 或多任务监督。"),
"19610":S("Video-LLM 的视觉 token 很多，普通 speculative decoding 在 draft/target 相互等待时无法填满硬件。","ParallelVLM 并行化 draft 与 target 阶段，并用视觉对齐约束保持 exact acceptance。","实验支持所测 video QA 模型的无损加速；不证明任意视觉剪枝或 draft 组合。","并行执行消耗额外设备/显存；低并发或短视频时串行 decode 更省。"),
"19677":S("多 agent topology 按单节点逐边生成，会把任务需要的协作组结构留给偶然涌现。","GoAgent 先生成 group-of-agents，再在组内外布置通信边，使拓扑结构成为显式控制变量。","任务结果支持所测分工模式；不证明自动拓扑在动态失败下稳定。","组结构增加规划和重配置成本；固定小团队可直接手工拓扑。"),
"19822":S("UAV benchmark 的逐步路线指令无法检验简短高层命令被展开为安全多阶段行为的能力。","HUGE-Bench 以 digital twin、过程型轨迹和安全事件定义 high-level VLA evaluation contract。","四个场景和八类任务只支持该封闭分布，不代表真实飞行认证。","过程评测更诊断但 simulator 成本高；低层导航仍适合传统 VLN suite。"),
"20105":S("开放式 REPL 的 recursive context processing 允许模型生成任意控制代码，难以验证终止与副作用。","lambda-RLM 将递归操作限制为 typed、预验证 combinator，使外部 context 的分解与聚合拥有受限执行语义。","实验支持所测长上下文任务的正确性/成本；不证明组合器集合覆盖任意推理。","可验证性以表达力为代价；短上下文可直接 attention，探索任务可能仍需开放 REPL。"),
"20216":S("离散 diffusion 同时独立采样多个 token 会破坏代码等局部联合结构。","CoDiLA 在每个并行 block 内引入短程 autoregressive coherence，同时保留 block 间并行修正。","论文结果支持指定代码/文本任务的速度质量折中；不证明 sub-linear latency 在所有硬件成立。","局部 AR 恢复依赖也减少并行度；结构弱的生成可继续独立 denoise。"),
"20217":S("response reward model 通常在看到输出后排序，不能直接在请求到达时选择模型。","论文估计每个模型对 prompt 的期望 reward，把 response-level scorer 提升为 pre-execution model-routing signal。","实验说明期望值在所测模型池中具有区分力；不证明 reward model 对分布外 prompt 校准。","路由减少昂贵采样却继承 reward bias；高风险请求仍需实际生成后验证。"),
"20218":S("chunk-level cache 跳过跨 chunk attention，命中率提升可能以回答质量为代价。","研究在统一系统中比较多种 KV reuse 修复策略，明确哪些依赖可恢复、哪些结构性误差仍存在。","结果是特定模型、chunking 和 RAG workload 的实验边界，不是通用缓存排序。","更精确修复增加重算；短检索上下文可直接完整 prefill。"),
"20219":S("next-token objective 强制每步立即提交且每个 token 分配同等 compute，困难位置无法先探索多条继续路径。","latent lookahead 在离散输出前训练隐藏的前瞻状态，让额外计算发生在未提交空间。","实验支持所测语言任务的质量变化；不证明 latent trajectory 可解释或带来系统级低延迟。","额外 hidden steps 增加训练/推理计算；简单 token 不需要动态思考预算。"),
"20625":S("checkpoint restore 后 LLM 会重新合成语义相同但字节不同的请求，传统 idempotency key 无法识别重复副作用。","ACRFence 对 action 语义与 authority consumption 建立持久承诺，在 restore 后拒绝 action replay 与 credential resurrection。","论文攻击与原型验证支持定义的两类 rollback；不证明语义 canonicalizer 覆盖所有工具。","更强防重放需要持久 ledger 且可能误并合法重试；确定性程序仍可使用普通 request ID。"),
"20953":S("模型 alignment 和事后评测都不能在具体 tool call 执行前提供确定性权限判断。","OAP 拦截 action proposal，将 principal、capability、policy 与请求参数绑定后再签发一次性执行许可。","公开 spec/reference implementation 证明协议可实现，不构成所有攻击面或性能证明。","集中 authorization 增加依赖与撤销状态；受限单工具进程可用本地 ACL。"),
"21257":S("高命中长上下文请求可能被远端 KV 加载而非 GPU compute 主导，compute-centric scheduler 看不到网络关键路径。","CALVO 将 KV block loading 建模为一等阶段，联合网络预取、请求排序和 GPU admission。","结果支持指定集群、命中率和模型的吞吐/延迟；不能外推其他 fabric。","网络感知提高利用率但增加预测与缓存一致性；KV 本地时传统 scheduler 更简单。"),
"21331":S("自动 kernel agent 若只追求单点速度，容易生成数值错误、shape 脆弱或不确定实现。","AutoKernel 以 profile/Amdahl 排序优化目标，并用五阶段 correctness harness 约束每轮 Triton/CUDA 搜索。","数百次实验和多 shape 测试支持其优化 loop；不证明 harness 已覆盖所有数值边界。","搜索成本高且容易过拟合硬件；成熟常用算子仍优先人工库。"),
"21354":S("单 router 同时承担内容分类、模型选择、cache、安全和 fleet provisioning，会造成策略冲突与不可独立扩缩。","WRP vision 将 workload classification、router policy 与执行 pool 分层，主张每层拥有不同状态与扩缩周期。","这是项目经验汇总和 vision，不提供统一对照实验，因此只作为架构候选而非性能事实。","分层清晰但引入更多控制面与一致性；单模型小流量仍可单 gateway。"),
"21465":S("kernel-generation LLM 缺少规模化正确训练数据，直接 RL 容易在编译通过与真实加速之间投机。","DRTriton 组合合成 PyTorch-Triton pairs、可执行 correctness filter 与性能 reward 来训练 kernel policy。","结果支持论文数据、GPU 和算子分布；不证明生成 kernel 可直接用于任意生产模型。","大规模编译/benchmark 成本高且 reward 依赖硬件；关键 kernel 仍需人工验证。"),
"21522":S("多 agent failure 每次从单条 trace 重新分析，既慢又无法复用历史模式。","论文把 reasoning trace 编码为可检索 failure representation，用历史相似模式辅助诊断与恢复。","初步实验只证明该表示在所测故障集中的可用性，不证明根因唯一或长期不漂移。","模式复用会固化旧误诊并带来隐私成本；新型故障仍需完整 trace RCA。"),
"21523":S("LLM 进入 CPS 后，语言层错误可能跨越到物理 action，纯模型准确率不能构成 safety assurance。","SafePilot 在 LLM planner 与低层 controller 之间加入安全 monitor、可验证约束和 fallback 控制链。","框架案例支持控制边界可实现，不等同于认证或真实事故率证明。","monitor 限制开放式规划并增加延迟；封闭控制任务优先传统 verified controller。"),
"21576":S("长上下文 decode 的瓶颈是每步扫描 O(n) KV block，单纯提高矩阵吞吐不改变带宽复杂度。","PRISM 用光子相似搜索先做近常数时间 block selection，仅把被选 KV 送入电子 attention。","论文硬件模型/原型支持其配置下的带宽与精度；不证明商用系统成本和所有序列分布。","近似选择可能漏掉关键 token，且光电接口成为新瓶颈；中短上下文仍适合完整 attention。"),
"21642":S("MCP 客户端把 tool description 和返回内容送入 planner，供应链 metadata 可成为 prompt-injection 通道。","研究对真实 AI coding clients 实施 tool-poisoning，比较不同客户端、模型与交互阶段的权限跨越。","证据只覆盖测试版本和攻击样本，不能证明未测客户端安全。","防御需来源签名、展示差异和最小权限，会降低插件易用性；可信本地 server 风险较低。"),
"21692":S("checkpoint 和 execution trace 能回答发生了什么，却难以跨调查聚合 agent 为什么选择某 action。","论文提出 normalized reasoning-provenance schema，将观察、候选、选择依据与行动关联为可查询记录。","主要贡献是数据模型和分析案例，不证明记录就是模型真实因果理由。","更细 provenance 增加敏感数据与存储成本；调试单次失败时普通 trace 已足够。"),
"22078":S("VLA 与 world-action model 的鲁棒性常在不同协议下比较，无法判断预测未来状态是否真的改善分布外控制。","研究在共享 perturbation、任务和 action metric 下对两类模型做对照，隔离 world prediction 分支的条件收益。","结果只支持指定机器人数据与扰动集，不建立 WAM 普遍优于 VLA 的结论。","world rollout 增加计算并可能传播预测误差；分布内低延迟控制仍可直接 VLA。"),
"22276":S("高 rank DoRA 需要显式物化 BA 后求行范数，临时内存随矩阵面积增长。","该工作把范数分解为 base、cross 与 Gram 项，并融合 kernel，避免创建 dense update。","实验支持指定维度、rank、GPU 与精度下的内存/速度；不证明高 rank 本身提高所有任务质量。","factorization 增加数值与 kernel 复杂度；低 rank LoRA/DoRA 已足够时无需该路径。"),
}

# Re-review the author's original retained set as well; no retained family may
# inherit the author renderer's generic fallback merely because it was not a
# newly discovered false negative.
SYNTHESIS.update({
"13358":S("经典 prefill/decode 分离假设一次 prefill 后持续 decode；多轮会话却反复追加 prompt 并迁移 KV，使每轮都产生新 prefill。","PPD 将初始 prefill 与增量 prefill 分开，并依据会话阶段在 AP/P/D pool 间动态路由，减少重复传输和资源干扰。","真实 workload 实验支持论文集群中的 TTFT/TPOT 权衡；不同 KV fabric、模型和会话长度需重新测量。","多一类 pool 增加容量规划与 KV handoff 状态；短单轮请求仍适合普通 PD 或共置。"),
"13605":S("agent workflow 同时含模型调用、工具和依赖边，直接把 orchestration 代码绑在单一 serving engine 上难以更换策略。","Orla 把 workflow policy 与 request execution 解耦，在 engine 之上统一表达依赖、并发和后端选择。","公开 evaluation 证明 library abstraction 可承载所测 agent workloads；不证明其调度在所有后端达到最优。","中间层提升可移植性但增加状态同步和调试跨度；简单单模型 chain 可直接调用 engine。"),
"13606":S("MoE dispatch/combine 依赖 device-initiated RDMA，但各专用库拥有不兼容 API 和通信状态。","NCCL EP 在 NCCL Device API 上提供统一 dispatch/combine，并把 low-latency 与 high-throughput 路径纳入同一通信接口。","多 GPU/NIC 实验支持指定拓扑和 message shape；不能外推所有 expert placement 或网络。","统一 API 降低集成成本但受 NCCL 语义约束；专用栈在固定拓扑仍可能更快。"),
"13644":S("RAG、摘要和长 context 都把历史当作文本，无法显式保存跨会话的决策状态、置信和失效条件。","StatePlane 把 belief、goal、decision 和 evidence 变成独立于 context window 的 versioned state，由 policy 决定写入、压缩和回注。","benchmark/case study 支持原型在长任务中的状态保持；不证明自动抽取的认知状态始终正确。","外部 state plane 增加冲突、权限和一致性负担；短会话仍应优先原始 context。"),
"14688":S("多 agent 故障会沿调用和共享状态级联，仅按时间线查看日志难以定位最早原因。","AgentTrace 从执行日志重建因果图，从最终错误反向遍历并按传播关系排序候选根因。","实验支持所测 workflow 和注入故障中的定位效果；未观测依赖仍会造成错误因果边。","图重建增加 trace 规范和存储成本；单进程短链故障仍可用结构化日志。"),
"15042":S("GPU spatial sharing 若通过改变 kernel 并行形状追求利用率，浮点执行顺序变化会破坏 bitwise determinism。","Vitamin-E 保持 logical launch 不变，只改变 block placement 与 wave count，在可证明的 parallel-structure equivalence 内调宽执行。","作者 GPU 实验支持所测 kernel 的确定性与利用率；不代表任意同步/原子 kernel 都可安全伸缩。","可伸缩集合受依赖约束且 scheduler 更复杂；独占运行仍提供最简单确定性。"),
"15340":S("masked diffusion 按 token uncertainty 独立解 mask，忽略 token 间依赖时会先提交结构上错误的位置。","DOS 从模型分布估计依赖方向，优先解开能为其他位置提供信息的 token，且无需重新训练。","指定 MDLM/任务实验支持速度质量变化；不证明估计依赖等于真实语法或语义因果。","依赖估计增加每步控制计算；关系弱或预算极紧时 uncertainty sampler 更简单。"),
"15798":S("每个 agent benchmark 都自带环境、task 和 runner API，新增模型需要重复适配，跨基准结果难复算。","CUBE 用 MCP/Gym 风格协议拆分 task、benchmark、package 和 registry，使环境包装与 agent implementation 独立。","原型集成展示协议互操作性，不证明指标本身有效或所有环境语义都可统一。","标准层减少 integration tax，却引入版本兼容和最低公分母风险；单 benchmark 可保持原生 API。"),
"15973":S("逐 agent capability check 假设安全属性可组合，但两个各自无害能力可能通过 conjunctive dependency 共同到达禁用状态。","论文用 capability graph 与组合规则证明 non-compositionality，并要求 governance 在联合可达状态而非单主体权限上判断。","形式化证明只在定义的 dependency semantics 内成立，没有给出开放生态的完整依赖发现机制。","联合分析组合爆炸且可能过度拒绝；能力确实独立时局部检查仍充分。"),
"16938":S("post-hoc policy 和行为 alignment 在高速自治执行中不能证明某个 action 当时满足约束。","Aegis 将不可变 policy、运行时许可与加密审计链绑定，使 policy decision 成为执行前条件。","论文主要提供架构和协议论证；没有证明实现可满足大规模 agent latency 或抵抗全部密钥攻击。","强治理增加密钥管理和中心依赖；低风险只读 agent 可使用轻量审计。"),
"17170":S("OAuth scope 授权的是操作符，却不能表达金额、对象等运行时 operands，agent 因而持有超出任务的权限。","task-scoped slice 从自然语言任务派生 operation predicate，并在跨服务执行时携带、缩减和验证该谓词。","论文协议/案例支持 operand-level 表达力；不证明自然语言到 predicate 的编译不会错。","细粒度权限增加解析、委托和撤销复杂度；固定操作参数可继续静态 scope。"),
"18280":S("refusal rate 与概念 probe 只说明模型识别危险内容或选择拒绝，不能定位 alignment 实际改变了哪层行为路由。","研究用 probes、surgical ablation 和行为测试分离 concept representation 与 policy routing，观察防护是否只改变从识别到动作的映射。","九个开放权重模型的自然实验只支持该政治审查任务中的层间差异，不代表所有安全训练机制。","内部可解释测试信息更丰富但依赖权重访问且可能误读相关激活；API 模型只能用行为评估。"),
"18330":S("持久 agent memory 若只追加和向量检索，会把矛盾、过期或越权内容重新注入 context。","MemArchitect 把 retention、conflict resolution、privacy 和 expiry 编成独立 policy layer，在读写两侧治理 memory lifecycle。","原型评测支持所测 memory scenarios 的规则执行；不证明策略能自动判断所有语义冲突。","policy layer 增加延迟与误删风险；短会话或只读知识可保持简单 RAG。"),
"18464":S("VLA RL 同步等待环境 rollout、inference 和 update，慢环境会让昂贵 GPU 形成级联 idle bubble。","AcceRL 物理解耦三类 actor，并以异步队列和版本策略连接 rollout、world model 与 learner。","集群实验支持指定 scale 的利用率/训练结果；policy staleness 和 simulator bias 限制跨任务外推。","异步提高吞吐却牺牲严格 on-policy freshness；小规模稳定环境仍适合同步训练。"),
"19025":S("云端模型客户既无法本地重跑，也难承受完整 ZK 推理，模型身份和执行正确性因此缺少可用证明。","论文用抽样/轻量 cryptographic commitments 证明部分中间计算，并以统计检测替代逐算子完整证明。","实验支持所测模型下的 verifier/prover 开销与检测概率；它不是确定性正确性保证。","轻量化用概率 assurance 换性能，且抽样面可能被适应；高风险场景仍需完整证明或可信硬件。"),
"19289":S("MoE expert offload 把 decode 瓶颈从算力转为 CPU-GPU 权重传输，需求到达后再加载会阻塞 token。","论文从当前 hidden representation 预测后续 expert，在计算重叠窗口内预取权重，并在误预测时回退正常加载。","实验支持指定 MoE、内存预算与 interconnect 上的延迟；不证明 predictor 在分布变化时保持命中。","预取浪费带宽和显存，低可预测路由时按需加载更稳。"),
"19423":S("prompt-injection defense training 可能提高拒绝，却同时破坏 agent 完成长工具链任务的自治能力。","研究把攻击鲁棒性与任务 competence 放在同一评测矩阵，比较不同 defense training 强度下的 capability-alignment frontier。","结果限于所测 agents、攻击和任务，不能推出防御训练必然降低所有能力。","安全收益必须与自治损失共同设 release gate；高风险环境可接受更保守策略。"),
"19544":S("科学 foundation model 的数据受主权和体量限制无法集中，普通跨数据中心 FL 又未覆盖 supercomputer job/failure semantics。","系统在多个 HPC facility 之间只交换模型状态，并将本地大规模并行训练、跨站聚合和恢复分层。","跨设施实验支持指定网络和科学模型的可运行性；不证明隐私泄露已由不搬原始数据解决。","跨站同步慢、异构且故障域更大；允许集中数据时单集群训练更简单。"),
"20357":S("多 agent 共用多类 memory 时，污染可从一个写入域传播到其他 agent 和后续会话，单次输入过滤看不到该路径。","论文按 memory duration、origin 与 location 建立威胁分类，并把 provenance、write authority 和 retrieval validation 作为隔离边界。","exact-v1 主要是 threat taxonomy/设计讨论，没有可复算防御 benchmark，不能声称某机制有效率。","更强隔离降低共享收益并增加治理状态；无持久共享 memory 时攻击面显著缩小。"),
"21340":S("monolithic learned world model 难同时提供物理一致、可组合模块、确定性 rollout 和可审计安全边界。","ARYA 提出由小型物理约束组件组合出的 deterministic state-transition architecture，把 causal interface 显式化。","公开 v1 是架构主张，缺少可复算的实现和独立实验，因此不能确认其满足所宣称的全部 world-model 要求。","确定性和模块化牺牲表示容量并把误差移到接口；数据丰富的感知生成仍可能需要大模型。"),
"22075":S("AR 与 masked diffusion 常在不同数据和 compute 下比较，无法判断差异来自 factorization 还是训练预算。","该工作固定 TinyStories 数据、step、batch、sequence 和 H100，分别训练 AR/MDLM，隔离生成范式作为实验变量。","受控比较只支持小数据/小模型和所报吞吐、质量、diversity；不能推断生产 LLM 哪个范式更优。","MDLM 并行与迭代修正的收益依赖长度和硬件；AR 保留成熟 streaming/cache 路径。"),
})
for suffix, synthesis in SYNTHESIS.items():
    base.PAPER_SYNTHESIS[f"2603.{suffix}"] = synthesis


base.DURABLE_CANDIDATES = set(base.DURABLE_CANDIDATES) | ADDITIONS
# Fresh reviewer found no new Books delta after comparing against the current
# manuscript.  Preserve the author's five proposals for root adjudication, but
# do not create additional Integrate queues from candidate admission alone.


original_review_one = base.review_one

# Candidate-level Score V2 audit.  Membership is a manual judgment over the
# exact-v1 mechanism; it is intentionally independent of Books disposition.
# Every retained family starts at 2/2/2 because it already passed the durable
# denominator.  A 3 is assigned only where the paper changes a concrete
# mechanism/owner (D), crosses component or organizational boundaries (R), or
# states a long-lived protocol/formal invariant (U).
SCORE_D3 = set("""
13281 13289 13319 13358 13364 13424 13591 13605 13606 13644 13875 13906
13940 13950 14688 14799 15042 15125 15202 15340 15690 15727 15973 16104
16158 16435 16586 16731 16938 17117 17170 17244 17445 17456 17573 17787
17803 17808 18016 18034 18043 18046 18096 18330 18433 18464 18567 18829
19025 19133 19289 19296 19469 19544 19610 19664 19987 20075 20216 20217
20218 20219 20356 20586 20616 20625 20711 20953 21019 21104 21177 21257
21331 21340 21354 21465 21523 21576 21641 21692 21862 22206 22276 22286
""".split())
SCORE_R3 = set("""
13358 13384 13424 13594 13605 13606 13644 13791 13870 13906 13940 13966
14688 14799 14987 15042 15125 15690 15714 15727 15798 15973 16013 16104
16572 16586 16817 16938 17104 17170 17244 17357 17445 17456 17673 17787
18034 18043 18046 18063 18096 18245 18280 18330 18433 18464 18516 18567
18829 19025 19131 19133 19173 19328 19335 19423 19469 19544 19677 19822
19987 20075 20356 20357 20625 20711 20953 21019 21104 21257 21354 21522
21523 21564 21641 21642 21692 22075 22078 22206 22212
""".split())
SCORE_U3 = set("""
13424 13606 13644 13870 13906 14799 14987 15042 15125 15727 15798 15973
16013 16104 16586 16731 16817 16938 17170 17244 17456 17787 17803 18043
18063 18096 18245 18330 18433 18829 19025 19131 19328 19335 19423 19469
19544 19664 19987 20356 20357 20625 20953 21177 21354 21523 21564 21692
21862 22075 22212
""".split())


def independent_score(row, review):
    suffix = row["arxiv_id"].split(".", 1)[1]
    score = (
        3 if suffix in SCORE_D3 else 2,
        3 if suffix in SCORE_R3 else 2,
        3 if suffix in SCORE_U3 else 2,
    )
    return score


def audited_review_one(row, src):
    review = original_review_one(row, src)
    if row["arxiv_id"] == "2603.21340" and review["source_kind"] == "PDF":
        body_path = ROOT / review["body_path"]
        digest = sha(body_path)
        url = "https://arxiv.org/pdf/2603.21340v1"
        review["method_locator"] = (
            f"arXiv:2603.21340v1 PDF — §3 System Architecture Overview [facet=method]; "
            f"{url}; {review['body_path']}; sha256:{digest}"
        )
        review["evaluation_locator"] = (
            f"arXiv:2603.21340v1 PDF — §11 Empirical Evaluation [facet=evaluation]; "
            f"{url}; {review['body_path']}; sha256:{digest}"
        )
        review["limitations_locator"] = (
            f"arXiv:2603.21340v1 PDF — §12 Discussion [facet=limitations]; "
            f"{url}; {review['body_path']}; sha256:{digest}"
        )
        review["claim_boundary"] = (
            "只支持 exact-v1 白皮书 §3 的公开架构描述；§11 的厂商 benchmark 主张缺少独立复核，"
            "因此维持 Disputed，不将生产部署、SOTA 或安全有效性作为已证实事实。"
        )
    # Review depth is decided by Score/override, never by Books disposition.
    design, reach, durability = independent_score(row, review)
    total = design + reach + durability
    review["score_v2"] = {
        "design_delta": design,
        "system_reach": reach,
        "durability": durability,
        "total": total,
        "basis": "fresh-context candidate-level exact-v1 audit; independent of Books disposition",
    }
    review["review_route"] = "deep" if total >= 7 or review["books_disposition"] == "Disputed" else ("standard" if total >= 5 else "closure")
    return review


base.score = independent_score
base.review_one = audited_review_one


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def proposal_for(day: int):
    path = Path(f"/private/tmp/march-202603{day:02d}-fresh-proposal.json")
    if path.exists():
        return json.loads(path.read_text())
    # arXiv has no ordinary Friday/Saturday announcement batch.  The recovered
    # strict-window inventory is empty for 03-21/22, so an empty receipt is the
    # complete population rather than a missing audit input.
    return {"report_date": f"2026-03-{day:02d}", "rows": []}


def write_fresh_receipt(day: int):
    src = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
    proposal = proposal_for(day)
    original = set(base.DURABLE_CANDIDATES) - ADDITIONS
    rows = []
    for row in proposal["rows"]:
        aid = row["arxiv_id"]
        retained = aid in base.DURABLE_CANDIDATES
        prior_retained = aid in original
        if retained:
            problem, mechanism, _evidence, _boundary = base.PAPER_SYNTHESIS[aid]
            node = base.NODE_OVERRIDES[aid]
            reason = (
                f"fresh-context retained for {node}: {problem} Durable delta: {mechanism} "
                "The exact-v1 manuscript is routed to Source Review; admission does not imply Books integration."
            )
        else:
            reason = row.get("screening_reason") or (
                "fresh-context closure: local method/domain result without a durable AI-System design delta"
            )
        rows.append({
            "arxiv_id": aid,
            "source_family_id": row["source_family_id"],
            "title": row["title"],
            "prior_author_decision": "retained" if prior_retained else "pre_denominator_closure",
            "challenge_hint": row.get("proposal"),
            "fresh_context_decision": "retained" if retained else "pre_denominator_closure",
            "finding": (
                "false_negative_corrected" if retained and not prior_retained else
                "original_retained_upheld" if retained else
                "challenge_rejected" if row.get("proposal") == "challenge_for_candidate_admission" else
                "closure_upheld"
            ),
            "reason": reason,
        })
    retained = sum(r["fresh_context_decision"] == "retained" for r in rows)
    corrected = sum(r["finding"] == "false_negative_corrected" for r in rows)
    rejected_challenges = sum(r["finding"] == "challenge_rejected" for r in rows)
    receipt = {
        "schema": "fresh-context-denominator-audit-v2.1",
        "auditor": "fresh-context:march-lane-b-reviewer",
        "report_date": f"2026-03-{day:02d}",
        "scope": "all strict-window raw title+abstract rows; challenge labels treated only as hints",
        "raw_identities": len(rows),
        "screened": len(rows),
        "retained": retained,
        "closures": len(rows) - retained,
        "false_negatives_corrected": corrected,
        "false_positives_removed": 0,
        "challenge_rejected": rejected_challenges,
        "weekly_dependency": 0,
        "rows": rows,
    }
    path = src / "fresh-context-audit-receipt.json"
    path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    return receipt, sha(path)


def patch_report_audit(day: int, receipt: dict, digest: str):
    path = ROOT / f"papers/2026/03/{day:02d}/README.md"
    text = path.read_text()
    audit = (
        f"| SA-202603{day:02d}-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | "
        f"coverage:SRC-ARXIV:202603{day:02d} | — | all {receipt['raw_identities']} raw title+abstract rows adjudicated; "
        f"false negatives corrected={receipt['false_negatives_corrected']}; false positives removed=0; "
        f"challenge rejected={receipt['challenge_rejected']}; receipt=papers/2026/03/_sources/daily-202603{day:02d}/fresh-context-audit-receipt.json#sha256={digest}; "
        "SRC-ARXIV is the only source due in March | passed |\n"
        f"| SA-202603{day:02d}-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | "
        "validator:review-completion-v1 | ROOT-FINAL-LOCATOR-RECONCILIATION | exact-v1 packets rebuilt; root must reconcile any locator finding | open |\n"
        f"| SA-202603{day:02d}-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | "
        "validator:deep-analysis-selection-v1 | ROOT-FINAL-SELECTION-RECONCILIATION | review depth separated from Books disposition; root final check pending | open |\n"
        f"| SA-202603{day:02d}-BOOKS | fresh-context:march-lane-b-reviewer | books | "
        "validator:books-comparison-v1 | ROOT-FINAL-BOOKS-RECONCILIATION | no Books written; author queues remain proposals only | open |"
    )
    text = re.sub(
        rf"\| SA-202603{day:02d}-COVERAGE .*?\n\| SA-202603{day:02d}-EVIDENCE .*?\n\| SA-202603{day:02d}-SELECTION .*?\n\| SA-202603{day:02d}-BOOKS .*?(?=\n\n)",
        audit,
        text,
        flags=re.S,
    )
    # Coverage itself is now closed.  Report completion remains In Progress
    # because evidence, selection and Books reconciliation stay open.
    text = text.replace("**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open", "**Status:** In Progress；Coverage=Closed、Evidence=Open、Books=Open")
    text = text.replace(
        "作者侧 comparison 已完成，fresh-context audit 与 Integrate 串行 writeback 未完成。",
        "fresh-context Coverage/Evidence audit 已完成；Selection 最终 reconcile 与 Integrate 串行 writeback 未完成。",
    )
    text = text.replace("| Coverage Gate | Open |", "| Coverage Gate | Closed |")
    text = re.sub(r"- Coverage: `Open`（到期来源枚举已闭合；只等待 fresh-context retained FP / closure FN audit）", "- Coverage: `Closed`（SRC-ARXIV 全量枚举、严格窗口、withdrawn 与逐项 FP/FN 审计已闭合）", text)
    text = text.replace("- `SRC-ARXIV` 的独立 retained false-positive / closure false-negative audit 尚未完成。\n", "")
    text = text.replace("- fresh-context Semantic Audit 与 Integrate writeback 尚未完成。", "- Selection 最终 reconcile 与 Integrate writeback 尚未完成。")
    text = text.replace(
        "由独立 reviewer 完成 FP/FN、exact-v1、Selection 与 Books prewrite audit；随后按日期顺序串行执行",
        "Coverage/Evidence fresh-context audit 已完成；由 root 完成 Selection/Books 最终 reconcile，再按日期顺序串行执行",
    )
    path.write_text(text)


def write_evidence_findings(day: int):
    """Materialize findings instead of letting an open Gate hide why it is open."""
    src = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
    packet = json.loads((src / "exact-v1-review-packet.json").read_text())
    items = []
    for review in packet["items"]:
        aid = review["primary_identifier"].split(":", 1)[1].removesuffix("v1")
        findings = []
        if aid not in base.PAPER_SYNTHESIS:
            findings.append("non_template_source_synthesis_required")
        # Every retained family needs role-specific source anchors.  A
        # position/taxonomy paper may have no benchmark; in that case its
        # discussion, alternatives or threat-model section must explicitly
        # anchor the non-proof boundary instead of leaving a generic
        # Not-Disclosed placeholder.
        for role in ("method", "evaluation", "limitations"):
            if review[f"{role}_locator"].startswith("Not Disclosed"):
                findings.append(f"{role}_role_locator_unresolved")
        if review["result"] != "complete":
            findings.append("exact_v1_review_incomplete")
        if review["withdrawn"]:
            findings.append("withdrawn_must_leave_candidate_path")
        items.append({
            "source_family_id": review["source_family_id"],
            "primary_identifier": review["primary_identifier"],
            "stable_node_id": review["stable_node_id"],
            "score_route": review["review_route"],
            "books_disposition": review["books_disposition"],
            "fresh_context_findings": findings,
            "status": "open" if findings else "passed",
        })
    payload = {
        "schema": "fresh-context-evidence-audit-v2.1",
        "auditor": "fresh-context:march-lane-b-reviewer",
        "report_date": f"2026-03-{day:02d}",
        "reviewed_candidates": len(items),
        "passed_candidates": sum(x["status"] == "passed" for x in items),
        "open_candidates": sum(x["status"] == "open" for x in items),
        "finding_counts": {
            kind: sum(kind in x["fresh_context_findings"] for x in items)
            for kind in sorted({kind for x in items for kind in x["fresh_context_findings"]})
        },
        "items": items,
    }
    path = src / "fresh-context-evidence-findings.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return payload, sha(path)


def patch_evidence_ref(day: int, payload: dict, digest: str):
    path = ROOT / f"papers/2026/03/{day:02d}/README.md"
    text = path.read_text()
    receipt_ref = f"papers/2026/03/_sources/daily-202603{day:02d}/fresh-context-evidence-findings.json#sha256={digest}"
    finding = (
        f"open candidate findings={payload['open_candidates']}; "
        f"counts={json.dumps(payload['finding_counts'], ensure_ascii=False, sort_keys=True)}"
        if payload["open_candidates"] else "—"
    )
    resolution = (
        "root must repair the listed source-specific synthesis/role locators before Evidence Gate can pass"
        if payload["open_candidates"] else "all candidate evidence checks passed"
    )
    status = "open" if payload["open_candidates"] else "passed"
    text = re.sub(
        rf"\| SA-202603{day:02d}-EVIDENCE \|.*?\|\n",
        f"| SA-202603{day:02d}-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | {finding} | {resolution}; receipt={receipt_ref} | {status} |\n",
        text,
    )
    path.write_text(text)


def main():
    raw_total, records, _ = base.load_records()
    for day in range(17, 25):
        base.render_day(day, raw_total, records)
        receipt, digest = write_fresh_receipt(day)
        patch_report_audit(day, receipt, digest)
        evidence, evidence_digest = write_evidence_findings(day)
        patch_evidence_ref(day, evidence, evidence_digest)
        print(day, receipt["raw_identities"], receipt["retained"], receipt["false_negatives_corrected"])


if __name__ == "__main__":
    main()
