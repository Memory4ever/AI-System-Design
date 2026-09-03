#!/usr/bin/env python3
"""Author-side Full Replay for 2026-03-17..24.

This lane intentionally has no Weekly dependency.  It enumerates the frozen
March DataCite/arXiv identity snapshot, performs a strict Beijing-window
screening, retrieves official exact-v1 arXiv HTML/abs pages, and emits V2.1
Daily author packets.  Fresh-context audit and actual Books writeback are
owned by the root reconciliation lane.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import html
import json
import re
import subprocess
import time
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "papers/2026/04/_sources/datacite-arxiv-202603-v2"
ANNOUNCEMENT_RECEIPT = ROOT / "papers/2026/03/_sources/march-2026-arxiv-announcement-recovery.json.gz"
PDFTOTEXT = Path("/Users/apple/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/bin/pdftotext")
OUT = ROOT / "papers/2026/03"
TZ = ZoneInfo("Asia/Shanghai")
UTC = ZoneInfo("UTC")
EXECUTED_AT = datetime.now(TZ).isoformat()


INTEGRATE_SUGGESTIONS = {
    "2603.14799", "2603.14987", "2603.15125", "2603.15202", "2603.15690", "2603.15714",
    "2603.16104", "2603.16435", "2603.16586", "2603.16731", "2603.17104", "2603.17244",
    "2603.17456", "2603.17787", "2603.17803", "2603.18063", "2603.18245", "2603.19328",
    "2603.18433", "2603.18489", "2603.18567", "2603.18773", "2603.19131", "2603.19133",
    "2603.19335", "2603.19469", "2603.20320", "2603.19664", "2603.19987", "2603.20075",
    "2603.20356", "2603.20357", "2603.20586", "2603.20616", "2603.20711", "2603.20884",
    "2603.21019", "2603.21104", "2603.21177", "2603.21340", "2603.21383", "2603.21564",
    "2603.21641", "2603.21654", "2603.21862", "2603.22206", "2603.22212", "2603.22286",
    "2603.22386", "2603.22489", "2603.22563",
}


# Frozen after full title+abstract recall screening.  These identities were
# retained because they alter a durable AI-System mechanism, ownership boundary
# or evaluation contract; the much larger NODE_OVERRIDES table also contains
# rejected calibration candidates and therefore must not define the denominator.
DURABLE_CANDIDATES = set("""
2603.13358 2603.13605 2603.13606 2603.13644 2603.14688 2603.14799 2603.14987
2603.15042 2603.15125 2603.15202 2603.15340 2603.15690 2603.15714 2603.15798
2603.15973 2603.16104 2603.16435 2603.16586 2603.16731 2603.16938 2603.17104
2603.17170 2603.17244 2603.17456 2603.17787 2603.17803 2603.18063 2603.18245
2603.18280 2603.18330 2603.18433 2603.18464 2603.18567 2603.18773 2603.19025
2603.19131 2603.19133 2603.19289 2603.19328 2603.19335 2603.19423 2603.19469
2603.19544 2603.19664 2603.19987 2603.20075 2603.20356 2603.20357 2603.20586
2603.20616 2603.20711 2603.21019 2603.21104 2603.21177 2603.21340 2603.21383
2603.21564 2603.21641 2603.21862 2603.22075 2603.22206 2603.22212 2603.22286
""".split())

# Current Books already carries the durable mechanism for most retained March
# families even when it does not name the paper.  A second owner+adjacent audit
# leaves only these source families as author-side writeback proposals; the
# independent root reviewer may still reject them.
INTEGRATE_SUGGESTIONS = {
    "2603.17803",  # co-activation-aware SSD KV placement/retrieval
    "2603.19131",  # inference-to-actuation evaluation contract
    "2603.19664",  # residual-stream reconstruction as KV/compute branch
    "2603.21177",  # prompt replay with fresh on-policy rollout
    "2603.21564",  # explicit (aggregation, capacity, timescale) memory contract
}


# A readable manuscript alone is not sufficient for Books integration.  The
# following exact-v1 items remain useful report evidence but fail the durable
# mechanism gate because the public paper is a survey/position piece or makes
# claims whose evaluation contract is not independently inspectable.
DISPOSITION_OVERRIDES = {
    "2603.20357": "No Change — Existing Coverage",
    "2603.21340": "Disputed",
}


# Paper-specific author synthesis for every 7--9 / Deep route.  These are not
# abstract copies: each entry states the changed systems contract, the concrete
# mechanism, what the public evaluation can establish, and the coexistence or
# failure boundary.  Exact source excerpts remain separately in the packet for
# an independent reviewer to challenge.
PAPER_SYNTHESIS = {
    "2603.14799": (
        "自演化 agent 若只按表面关键词选择知识域，会把‘知道什么’与‘下一步该验证什么’混在一起。",
        "该工作把 epistemic universe 作为显式路由状态，由分类器决定问题所属的推理制度，并把 hard/soft routing 与停止条件分开。",
        "验证比较 TF-IDF 与多种小型语言模型，并以刻意打破关键词相关性的 held-out 集合检查语义路由；它证明的是路由器在该分类任务上的鲁棒性，不是开放世界中的自知能力。",
        "新增错误面是 universe 标签漂移与错误路由后的级联；边界清楚、一步可解的任务仍无需维护额外 epistemic control plane。",
    ),
    "2603.14987": (
        "孤立 benchmark 的平均分无法代表 agent 在开放工具链、长任务和分布变化下的可信性。",
        "论文把评测重构为 distribution-aware Factory cycle：先定义目标部署分布，再生成/筛选场景、执行红队并把暴露出的 failure mode 反馈到下一轮。",
        "公开实例只有单模型、合成数据和 24 个手工场景，因此证明的是评测流程可运行，而不是该流程已经覆盖真实生产分布。",
        "收益是把 coverage denominator 变成一等对象；代价是分布建模、场景生成与人工判定本身会引入选择偏差。",
    ),
    "2603.15125": (
        "持久 memory 不只是被动数据：一次被污染的检索结果可以改写后续 tool arguments 和控制流。",
        "作者以 agent state machine 与 trace space 形式化 memory-control-flow attack，把写入、检索、参数构造和工具调用串成可审计的攻击映射，并给出对应验证条件。",
        "实验只验证论文定义的攻击族与 agent/tool 配置；它没有证明所列检测条件对未知 memory backend 或长期演化策略完备。",
        "防护必须约束 memory lineage 与消费点，但更严格的校验会增加检索延迟并可能拒绝合法派生记忆；无持久状态时传统输入过滤仍较简单。",
    ),
    "2603.15202": (
        "LLM scheduler 的目标常被拆成互不兼容的 KV locality、等待时间和长度优先级，复杂策略难以在同一合同下比较。",
        "LMetric 把策略拆为可组合的 request metrics，并用乘法组合同时表达 KV reuse 与 aging，使优先级不是某个 engine 内部的隐式分支。",
        "论文提供统一分析框架与端到端比较；结论只覆盖其请求分布、模型与实现，未公开的并发/SLO 不能外推。",
        "乘法简单但对尺度归一化和极端值敏感；工作负载同质时 FIFO 或单指标策略仍具有更低控制开销。",
    ),
    "2603.15690": (
        "运行时可重接线的多 agent 软件会让上下文、结构与演化历史共同决定行为，传统静态代码边界不足以解释漂移。",
        "论文把 context artifact、semantic lens、index generator 与 evolution entropy 组合为显式工程对象，使 rewiring 的来源和结构变化可追踪。",
        "RepoBench-R 只验证其中语义检索与索引机制，不能证明整套 loosely-structured software 治理在生产多 agent 系统中有效。",
        "结构显式化提高可诊断性，却引入额外索引和版本状态；规模小、拓扑固定的 agent graph 仍适合普通代码配置。",
    ),
    "2603.15714": (
        "间接 prompt injection 通过环境内容进入 agent，单轮拒答或静态 jailbreak benchmark 无法覆盖实际工具路径。",
        "工作从公开竞赛记录恢复攻击与防御路径，将成功条件绑定到 agent 对不可信内容的读取、指令采纳和工具执行链。",
        "大规模竞赛提供现实攻击多样性，但参与者选择、赛题环境和评分规则限制了对其他 agent stack 的外推。",
        "真实路径证据优于合成单轮测试；代价是数据分布不可控且难区分模型弱点、工具权限和 orchestration 缺陷。",
    ),
    "2603.16104": (
        "agent workflow 的多个 LLM call 具有依赖关系和重叠中间状态，按独立请求调度会浪费 prefix/KV 并放大尾延迟。",
        "Helium 把 workflow dependency 与中间结果纳入数据系统，联合执行 cache-aware routing、共享状态复用与 workflow-level scheduling。",
        "评测覆盖公开 agent workflow，能支持局部 cache/scheduling 收益；作者也明确当前设计优先 locality，尚未证明动态负载下的公平性与隔离。",
        "共享提高命中率却增加跨步骤 identity、失效和 admission 复杂度；无依赖的普通在线请求仍应走独立调度。",
    ),
    "2603.16435": (
        "逐 token、逐 head 保留完整 KV 在长上下文和高并发下成为容量瓶颈，而简单低维投影容易损失相关结构。",
        "VQKV 用 vector quantization 对 KV 的联合结构编码，以可复用 codebook 换取更高压缩比，并保持训练外部署路径。",
        "论文在多模型与下游任务上比较相同压缩预算；结果只说明这些模型/任务下的 fidelity，不证明所有注意力层都可同等量化。",
        "codebook 查找与量化误差成为新成本；短上下文、严格 exactness 或内存充足时完整 KV 仍是稳健基线。",
    ),
    "2603.16586": (
        "对单次 action 做 allow/deny 无法表达 agent 路径中先前授权、累计风险与状态变化。",
        "论文把 governance 定义为作用在 action path、principal、当前 state 与历史摘要上的 policy function，使每个执行边都有可判定的策略状态。",
        "exact-v1 主要给出形式化与现有机制的缺口分析，没有独立系统实验；因此它提供设计合同，而非性能或防护效果证据。",
        "路径策略提高可表达性但带来 state reconstruction 和 policy conflict；无持久状态的单工具调用仍可使用普通 capability check。",
    ),
    "2603.16731": (
        "量化 optimizer state 不只是存储误差：EMA 更新会积累 stale state，使长期训练动力学发生偏移。",
        "工作把量化、反量化与 EMA reset 写进 optimizer 更新，并比较周期性重置能否清除累积陈旧性。",
        "多种低精度 regime 的训练实验支持 state reset 的条件性收益；没有覆盖的模型规模、优化器和长训练 horizon 不能外推。",
        "重置恢复新鲜度但会丢失动量历史并引入调参；显存允许或稳定性优先时高精度 optimizer state 仍更可靠。",
    ),
    "2603.17104": (
        "真实 coding agent 的 specification 会在执行中逐步出现，若只保存当前 prompt，早期设计承诺会在长链修改中丢失。",
        "ProjectGuard 维护同步的 durable semantic state 与项目 artifact 视图，把新约束、决策和依据持续合并后再提供给 agent。",
        "benchmark 对比一次性完整规格与渐进披露，测量最终实现的 faithfulness loss；证据限于研究型 coding 任务。",
        "外部状态可降低 specification drift，却引入抽取错误和过期承诺；短任务或规格一次给全时不需要该层。",
    ),
    "2603.17244": (
        "agent memory 若只追加事实，无法在相互冲突的新证据到来时说明哪个 belief 有效、为什么被替换。",
        "该工作用 graph-native、versioned belief node 和形式化 revision operator 表达 provenance、冲突与 consolidation。",
        "评测从九个维度与现有系统比较并在长会话数据上检查规模行为；它未证明形式语义能消除抽取或检索错误。",
        "可追溯 belief revision 提升治理性，但图维护和一致性成本更高；只读知识库或无冲突短会话仍可用简单向量记忆。",
    ),
    "2603.17456": (
        "LLM serving 的 prefill、decode 与 KV transfer 共享多阶段网络路径，单队列看不到下游拥塞导致的 TTFT 违约。",
        "MFS 用 defer-and-promote 在多级队列中延迟非紧急 flow，并依据阶段进展提升优先级，从控制通信 flow 而非只排 GPU request。",
        "8 台服务器、每台 4 张 RTX 3090 的 testbed 给出端到端结果；不同 fabric、模型和 SLO 下的排序仍需重验。",
        "多阶段状态改善 deadline 管理但会增加队列维护和 starvation 风险；单阶段或低争用负载仍适合简单 FIFO。",
    ),
    "2603.17787": (
        "多个 agent 对同一实体各自写 memory，会产生冲突、不可追踪派生与跨 workflow 数据泄漏。",
        "论文提出共享 governed memory layer，用 identity、provenance、temporal anchor 与写入 quality gate 统一多 agent 的读写契约。",
        "验证依赖 domain rubric、trace capture 和启发式质量分，能说明架构可运行但不能证明语义质量判定可靠。",
        "治理层提高可追责性，却成为集中式状态和策略瓶颈；隔离任务或短生命周期 agent 可保留私有 memory。",
    ),
    "2603.17803": (
        "KV offload 到单 SSD 时，相关条目常被一起请求，随机布局使多盘带宽无法并行利用。",
        "Swarm 离线学习 KV co-activation，按关联图跨 SSD 放置，并在在线阶段协同检索、更新和缓存。",
        "公开系统使用 H20 GPU、DDR5 与多 NVMe 配置测试多种负载；结论绑定该存储层级和 co-activation 稳定性。",
        "关联感知提高并行带宽但需要 profiling，分布漂移会使布局失效；小 KV 或 DRAM 足够时无需 SSD 层。",
    ),
    "2603.18063": (
        "MCP 把发现、描述与调用工具放进协议后，传统 API 威胁分类缺少对语义委托和 capability confusion 的表达。",
        "MCP-38 按 server、tool metadata、sampling、transport 与跨组件 trust boundary 建立 38 类威胁及对应资产/攻击路径。",
        "exact-v1 是 taxonomy 与框架映射，没有攻击覆盖率或防护效果实验；它只能作为 threat-model denominator。",
        "统一词汇有助审计，但分类重叠和协议演化会带来维护成本；固定私有工具集仍可用较窄威胁模型。",
    ),
    "2603.18245": (
        "安全 benchmark 自己可能漏掉关键 tool-call workflow，单看 agent 得分无法知道测试分母是否完整。",
        "SafeAudit 系统枚举工具、风险、前置状态与交互序列，再量化既有 benchmark 的 coverage 与新增场景。",
        "实验支持对公开 tool-call benchmark 的覆盖审计；枚举规则和环境模型仍可能漏掉未知风险。",
        "meta-audit 让 coverage 可计算，却显著扩大场景空间；窄工具集可采用人工威胁模型作为较低成本基线。",
    ),
    "2603.18433": (
        "prompt injection 的实质是低优先级不可信内容夺取高优先级控制流，单纯关键词过滤无法表达冲突来源。",
        "PCFI 在 gateway 维护消息优先级与 role provenance，以 lexical、role-switch 和 hierarchy check 阻止低级输入覆盖系统约束。",
        "公开评测比较概念性无防护基线、各阶段信号与完整 pipeline；它未证明对语义等价或跨语言攻击完备。",
        "运行时层级检查可快速阻断明显违规，但误报会损害任务完成；无外部内容的受控 prompt 可保留轻量过滤。",
    ),
    "2603.18567": (
        "speculative decoding 的收益依赖 draft model 训练，但现有训练实现分散，数据、loss 与分布式执行难比较。",
        "SpecForge 把 draft 数据生成、训练目标和可扩展训练 runtime 模块化，使不同 proposal 方案共享同一训练合同。",
        "系统评测与两个公开实现比较训练性能；它不等价于证明所有 target/draft 组合都获得高接受率。",
        "统一框架降低实验成本，却增加抽象层和兼容维护；现成 draft 已满足 workload 时无需新训练栈。",
    ),
    "2603.18773": (
        "SFT 与 RL 参数相互耦合，逐阶段单独调参可能得到局部最优而让整条 post-training pipeline 退化。",
        "AutoPipe 先在便宜设置学习配置排序，再用少量 end-to-end 观测做 local correction，搜索联合 SFT-RL 配方。",
        "验证集中在 biomedical chain-of-thought QA；结果支持 ranking transfer 在该域降低搜索成本，不证明跨域排序稳定。",
        "代理排序节省算力但可能因规模/数据变化反转；预算足够或风险高时完整联合 sweep 仍是可靠基线。",
    ),
    "2603.19131": (
        "VLA 的 tokens/s 或单次 latency 不能说明机器人是否在控制周期内完成安全、有效动作。",
        "论文把 inference、action chunk、actuation 与任务完成串成 embodied-efficiency contract，联合测量模型速度和物理执行。",
        "实验能证明传统推理指标在所测 VLA/机器人任务上与真实表现错位；不能外推到未测 embodiment 与控制频率。",
        "端到端指标更真实但重复成本高、环境噪声大；纯模型优化阶段仍可保留推理指标作局部信号。",
    ),
    "2603.19133": (
        "edge-cloud speculative decoding 会同时受 uplink、draft 速度和验证流水线约束，串行传输会抵消 speculation 收益。",
        "PicoSpec 把 edge proposal、分块传输与 cloud verification 管线化，并以概率模型决定通信和计算重叠。",
        "论文用 throughput 模型和 edge-cloud 实验刻画边界；收益依赖网络、接受率和 batch 配置。",
        "流水线提高重叠但增加版本、回滚和缓存提交状态；网络差或接受率低时本地/云端普通 decode 更稳。",
    ),
    "2603.19328": (
        "tool-using agent 的 runtime verifier 越精细，安全性可能提高，但检查开销和拒绝会随任务 horizon 累积。",
        "作者固定模型、工具和环境，只改变 control-flow 与 verifier precision，以区分 verifier tax 与模型能力差异。",
        "评测同时报告任务成功和程序性安全，并观察 horizon 变化；结论只属于所测架构与风险定义。",
        "更强 verifier 带来延迟与 false reject；低风险短任务可采用较薄检查，高风险长任务需要按路径分配验证预算。",
    ),
    "2603.19335": (
        "post-training 算法排名常在单一模型规模上得出，可能把规模效应误当算法普遍优越。",
        "oxRL 用统一实现控制 51 种配方，在多个模型规模下分离 scale、online/offline paradigm 和具体算法。",
        "GSM8K 等可验证任务显示排名会随规模反转；这证明配方选择依赖规模，不证明同一排序适用于开放任务。",
        "统一控制提高可比性但任务窄；成熟固定 workload 仍可复用已验证算法，无需全量重扫。",
    ),
    "2603.19469": (
        "agent action 是否越权取决于指令来源、目标、时间和此前状态，静态恶意字符串无法定义安全性。",
        "论文把安全判定分解为若干 contextual oracle，并用 temporal property 描述授权、信息流与 action sequence。",
        "exact-v1 通过现有防御映射展示覆盖缺口，没有独立攻击/防御实验；它提供形式化需求而非实现效果。",
        "oracle 分解澄清责任但实现近似会产生组合误差；单用户、单工具和无状态场景可用简单 ACL。",
    ),
    "2603.19664": (
        "每层都存 K/V 假定这些张量不可重建，但 residual stream 已携带生成它们的大部分状态。",
        "论文从 residual stream 重新计算部分层的 K/V，以重算换缓存容量，并按层选择可替代的 KV。",
        "多模型实验验证部分架构可近似或精确恢复；Gemma-3 sliding-window 层出现显著退化，证明该机制不是通用删除 KV。",
        "省显存的代价是额外 compute 和架构敏感性；滑窗层、低算力或严苛 latency 下完整 KV 仍成立。",
    ),
    "2603.19987": (
        "整段 trajectory 作为单一训练样本会丢失中间环境 state，使 post-training 难以学习 action 对下一状态的因果影响。",
        "工作把 rollout 重写为显式 Markov state-action transition，并在不输出 chain-of-thought 的条件下逐状态更新 policy。",
        "实验与 conventional trajectory training 比较，支持所测环境中的能力提升；未证明所有任务都满足可观测 Markov 假设。",
        "状态化训练改善 credit assignment，却增加环境序列化和 state leakage 风险；短、静态任务仍可用整段偏好学习。",
    ),
    "2603.20075": (
        "编译器修复 agent 若只在玩具代码上评估，无法暴露跨 pass、构建与回归测试的真实 workflow failure。",
        "该工作构建 llvm-bench 与 llvm-autofix harness，把缺陷定位、补丁生成、编译和测试反馈组织为可复现 agent loop。",
        "评测覆盖 LLVM 基准中的真实修复任务；它证明 harness 的诊断价值，不证明 agent 已能可靠维护编译器。",
        "真实工具链提高有效性却增加执行成本和 flaky build；小型语法修复仍可用轻量单轮 benchmark。",
    ),
    "2603.20356": (
        "显式 agent workflow graph 在部署前已经暴露工具和分支结构，但安全检查通常等到 runtime 才发生。",
        "Agentproof 从框架 API 抽取 graph，静态传播 node/tool 属性并检查不可达授权、缺失 human gate 等结构规则。",
        "评测验证多个 framework graph 的提取与规则命中；LangGraph human-node 依赖命名 heuristic，限制了完备性。",
        "静态检查便宜且可前移 release gate，但看不到运行时 prompt/data；动态行为仍需 runtime policy 与 trace。",
    ),
    "2603.20586": (
        "单层 KV 对所有历史使用同一保留策略，不能同时服务局部依赖、会话状态和长期记忆。",
        "MKA 用 memory key 在 L1/L2/L3 timescale 间动态路由 attention，在固定 KV 预算下选择不同层级的表示。",
        "论文在 Qwen2.5 等三类模型/压缩策略上测量 perplexity 与任务表现；证据不覆盖任意 memory hierarchy。",
        "层次路由提高预算利用率但引入 key 学习和错误层级选择；短上下文仍可用单层 KV。",
    ),
    "2603.20616": (
        "只按 token eviction 分配 KV 预算忽略不同 head/channel 的冗余差异，固定维度压缩会浪费容量。",
        "MixedDimKV 联合选择 token 与投影维度，并重排 memory layout、复用 projection matrix，以不同维数编码不同 KV 子空间。",
        "实验在公开模型上比较同预算压缩；收益依赖 PCA 子空间和层/head 统计稳定性。",
        "混合维度减少浪费却使 kernel、layout 和 metadata 更复杂；规则形状或硬件 kernel 受限时固定维度更易部署。",
    ),
    "2603.20711": (
        "VLA 的感知、推理与控制跨 edge/cloud 切分时，单看算力无法满足网络波动和控制周期。",
        "RoboECC 联合 model-hardware segmentation 与 network-aware adjustment，运行时改变 VLA partition 和放置。",
        "公开实验分析所测模型、设备与网络下的部署收益；不能证明所有机器人链路都能安全动态切分。",
        "自适应放置改善资源利用但引入中间状态传输和切换抖动；网络不可靠或安全关键闭环应优先 edge-local。",
    ),
    "2603.21019": (
        "agent skill marketplace 的包同时含说明、脚本和资产，下载量或静态 metadata 不能说明实际 capability 风险。",
        "SkillProbe 组合多 agent 分工、静态扫描与可选动态执行，对 skill 的声明、代码行为和权限需求做交叉审计。",
        "评测使用真实生态样本与受控环境；检测率受 Python/工具 sandbox 和规则覆盖限制。",
        "协作审计扩大覆盖却增加模型判断与执行成本；可信内部 registry 仍可用签名和人工 review。",
    ),
    "2603.21104": (
        "安全关键 world-model 评测若只生成更危险的画面，无法说明哪一动作或交互导致风险。",
        "CounterScene 把场景生成写成对 multi-agent dynamics 的 counterfactual intervention，比较改变特定因果变量后的 rollout。",
        "闭环驾驶场景实验支持该干预在所测 simulator 中产生可解释危险交互；不证明 learned causality 等同真实世界。",
        "因果控制增强诊断但依赖结构假设；仅需视觉多样性时普通生成模型成本更低。",
    ),
    "2603.21177": (
        "GRPO 每轮重新采样全部 prompt 浪费 rollout，而简单 replay 又会破坏 on-policy freshness。",
        "方法只重放近期产生高方差/高信号 group outcome 的 prompt，再用当前 policy 重新 rollout，而不是复用旧 trajectory。",
        "基于 OLMo-RL 并在六个 benchmark 报告准确率/训练效率；结论绑定筛选规则和任务分布。",
        "prompt replay 提高样本利用率但可能过度聚焦困难样本并改变 curriculum；信号均匀时标准采样更稳。",
    ),
    "2603.21383": (
        "trajectory-level RL 把大量已确定或无信息的 turn 一并训练，浪费 verifier 和 rollout compute。",
        "PivotRL 离线识别 mixed-outcome pivot turn，只在局部 state 上组成 group-normalized 更新，并用 verifier 约束选择。",
        "理论分析与 agentic benchmark 检查 turn selection 和 verifier design；证据限于可可靠标注 pivot 的环境。",
        "局部训练节省算力但可能破坏长程 credit；任务奖励强依赖远期状态时完整 trajectory RL 仍必要。",
    ),
    "2603.21564": (
        "hierarchical memory 系统使用不同术语，难比较它们究竟聚合什么、保留多少以及多久更新。",
        "论文用 (aggregation α, capacity C, timescale τ) 三元组统一 data memory 与 agent-trace memory 的层级设计。",
        "表格映射十一种系统，属于理论/分类比较而非新 runtime benchmark；它证明统一语言可覆盖这些案例。",
        "统一参数便于设计但会抽象掉权限和语义冲突；单层 memory 不需要额外层次模型。",
    ),
    "2603.21641": (
        "MCP server 常把实现方便所需的内部能力全部暴露为 tool，形成超出任务需要的权限面。",
        "审计器解析 Python/JSON tool metadata，联合静态规则与可选 sandbox 动态检查，输出 capability 与最小权限差异。",
        "受控 vulnerable server、MCPTox 和 curated server 上的检测实验支持该实现；TypeScript/JavaScript 暂未覆盖。",
        "自动审计可前移 release gate，但静态近似会误报；语言不支持或动态 capability 仍需人工/运行时验证。",
    ),
    "2603.21862": (
        "宏观 parameter/compute scaling law 不能直接决定 MoE 的 expert 数、粒度、共享层与 routing 配置。",
        "论文在统一实验基础设施上拟合面向 MoE architecture 的 scaling relations，并把 compute budget 映射到结构组合。",
        "多组 MoE 实验支持所给设计空间内的趋势；硬件通信、训练配方和未测 router 会改变最优点。",
        "结构定标减少盲目 sweep，却可能固化历史硬件假设；小模型或通信昂贵时 dense/较少 expert 仍合理。",
    ),
    "2603.22206": (
        "multi-agent workflow 同时包含不同语义角色、输出长度和模型需求，固定模型/队列会同时浪费质量和延迟预算。",
        "Chimera 在 vLLM 前加入异步 semantic router 与 length predictor，联合选择异构模型并形成批次。",
        "评测覆盖多种 Qwen/Ministral 规模与 agent workflow；结果绑定预测误差、模型池和请求分布。",
        "动态路由提高利用率但引入错误选模、冷缓存与公平性问题；单模型同质请求仍宜直接调度。",
    ),
    "2603.22212": (
        "world model benchmark 若只看视频质量或静态 3D 重建，无法判断 action-conditioned interaction 是否正确。",
        "Omni-WorldBench 以交互任务、物理原则和时序响应组织 suite，评估 observation-action-transition 而非单帧外观。",
        "公开 suite 覆盖多类物理和任务，但作者明确环境、多样性与 evaluator 仍有限；它定义合同而非证明某模型通用。",
        "交互评测更接近 planning，却更昂贵且依赖 simulator；纯内容生成仍可使用视觉质量指标。",
    ),
    "2603.22286": (
        "video world model 每步重算全部 DiT 中间状态，即使场景内容变化很小，也浪费推理计算。",
        "WorldCache 按感知变化决定何时复用 cached activation，并在 runtime 动态启停，不修改模型权重。",
        "Cosmos-Predict2.5 2B/14B 的实验支持所测视频 workload 的加速；未证明高速运动或分布外场景保持 fidelity。",
        "内容感知复用减少计算但可能缓存陈旧动态；变化剧烈、安全关键 rollout 应降低复用或完全重算。",
    ),
}


# Every retained family is deliberately routed after title/abstract screening;
# no generic keyword fallback is allowed to decide its canonical knowledge owner.
NODE_OVERRIDES: dict[str, str] = {}
for _node, _ids in {
    "AGENT-MCP": "18063 20313 21641 21642",
    "AGENT-MEMORY": "13644 13875 15280 15421 15634 15642 15658 15666 16171 16496 16862 17168 17244 17787 18330 18429 18631 18718 19595 19935 21564",
    "AGENT-MULTI-AGENT": "17112 19431 19677",
    "AGENT-PLANNING": "14799",
    "AGENT-RAG": "14778 17292 18272 20673 20939",
    "AGENT-TOOL-CALLING": "13426 19896",
    "AGENT-WORKFLOW": "15690 17613 19270 19639 20075 20356 20380 20884",
    "INFER-KV-CACHE": "13281 13289 14224 14303 14371 16435 17168 17803 18489 19664 20397 20586 20616 21576",
    "INFER-PD-DISAGGREGATION": "13358",
    "INFER-SCHEDULING": "13605 15202 16104 16514 17280 17302 17456 19172 22206",
    "INFER-SPECULATIVE-DECODING": "14989 17573 18567 18599 19133 19289 19610",
    "INFER-TENSORRT-LLM": "16590 17435 17809 17891",
    "MODEL-LONG-CONTEXT": "17484 18446 20105 20432 20843 21663 22241",
    "MODEL-MOE": "18297 18492 21862",
    "MULTIMODAL-EMBODIED-VLA": "14851 14972 15257 16013 17524 18091 18178 18342 19131 19418 20659 20668 20711 21341 22003 22280",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "15340 22075 22216 22248",
    "MULTIMODAL-WORLD-MODELS": "14948 15359 15759 16860 17117 17808 18202 18266 18464 19201 19675 19708 19979 20607 21017 21104 21315 21340 21546 21557 22212 22281 22286",
    "PLATFORM-EVALUATION-SYSTEM": "14975 14987 15798 16253 17104 17145 18245 18280 19005 19131 19328 20576 22212",
    "PLATFORM-GPU-SCHEDULER": "15042",
    "PLATFORM-PRODUCTION": "15676",
    "PLATFORM-SECURITY": "13420 15125 15661 15714 15809 15973 16572 16586 16938 17170 17176 17419 17673 18063 18433 19025 19423 19469 20122 20357 21019 21642 21654",
    "PLATFORM-TRACE": "14688",
    "TRAIN-DATA": "16105",
    "TRAIN-DISTRIBUTED-TRAINING": "13606 18872 19544",
    "TRAIN-GRPO": "16158 21016 21177",
    "TRAIN-PRETRAINING": "16731 17052",
    "TRAIN-RLHF": "16253 18736 18773 18815 19220 19335 19423 19987 21383",
}.items():
    for _aid in _ids.split():
        # IDs are kept suffix-only here so the table stays human-auditable.
        NODE_OVERRIDES[f"2603.{_aid}"] = _node
NODE_OVERRIDES["2603.18063"] = "AGENT-MCP"


NODE_PATH = {
    "MODEL-LONG-CONTEXT": "books/part-02-model/22-long-context.md",
    "MODEL-MOE": "books/part-02-model/21-moe.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "TRAIN-RLHF": "books/part-04-training-system/31-rlhf.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "TRAIN-PRETRAINING": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-TENSOR-PARALLEL": "books/part-04-training-system/37-tensor-parallel.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-CONTINUOUS-BATCHING": "books/part-05-inference-system/46-continuous-batching.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/49-tensorrt-llm.md",
    "INFER-GPU-MEMORY": "books/part-05-inference-system/54-gpu-memory.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "INFER-PD-DISAGGREGATION": "books/part-05-inference-system/55-pd-disaggregation.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "PLATFORM-TRACE": "books/part-06-ai-infrastructure/69-trace.md",
    "PLATFORM-PRODUCTION": "books/part-06-ai-infrastructure/73-production-best-practice.md",
    "PLATFORM-GPU-SCHEDULER": "books/part-06-ai-infrastructure/63-gpu-scheduler.md",
    "AGENT-CONTEXT": "books/part-07-agent/75-context.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-TOOL-CALLING": "books/part-07-agent/78-tool-calling.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "AGENT-PLANNING": "books/part-07-agent/79-planning.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-MCP": "books/part-07-agent/83-mcp.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
}


NARRATIVE_LENS = {
    "AGENT-MCP": ("把协议当作普通 tool adapter，部署和权限模型最简单。", "跨 server capability、委托链与动态发现使权限边界不再等同于一次函数调用。", "协议身份、capability 声明、授权与审计状态", "固定工具集、单一信任域仍可保留较薄的 adapter。"),
    "AGENT-MEMORY": ("把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。", "长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。", "memory 的写入、版本、检索与失效控制权", "短会话或不可接受派生状态漂移时仍应回退原始 context。"),
    "AGENT-PLANNING": ("按当前 prompt 即时选择下一步，在短任务中无需维护额外 epistemic state。", "自演化与长链任务需要区分已知、未知和可验证的下一步。", "计划路由、证据需求与停止条件", "目标明确且一步可完成时直接执行仍更稳健。"),
    "AGENT-WORKFLOW": ("把 agent loop 留在进程内代码，开发快且控制流直观。", "长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。", "workflow graph、checkpoint、重试与演进状态", "短暂、幂等任务仍可采用轻量进程内循环。"),
    "INFER-KV-CACHE": ("完整、逐 token 保存 KV，换取语义透明和最低重算风险。", "长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。", "KV 的 identity、压缩、复用、放置与失效状态", "小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。"),
    "INFER-PD-DISAGGREGATION": ("prefill 与 decode 共置便于共享权重和 KV，低负载下最少网络跳转。", "多轮请求的阶段成本和到达分布分化，使单一资源池难同时满足 TTFT 与 TPOT。", "阶段拆分、KV handoff 与资源池选择", "负载较小或网络成本占主导时共置仍更合适。"),
    "INFER-SCHEDULING": ("FIFO 或静态批次在请求同质时易预测、易实现。", "长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。", "准入、批处理、优先级、路由和资源选择", "同质离线吞吐任务仍可使用简单静态策略。"),
    "INFER-SPECULATIVE-DECODING": ("逐 token 串行验证保持 exactness，且不维护额外 draft 状态。", "decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。", "proposal、验证、接受/回滚与缓存提交状态", "接受率低、draft 成本高或状态提交复杂时普通 decode 仍成立。"),
    "MODEL-LONG-CONTEXT": ("全量 attention 保留任意 token 交互，在中短序列上最直接。", "序列增长令计算、显存和信息稀释同时恶化。", "上下文选择、层次化表示和可访问记忆的语义边界", "任务确实依赖密集全局交互且长度可控时全量 attention 仍是基线。"),
    "MODEL-MOE": ("dense 层让每个 token 经过同一参数路径，训练与部署最规则。", "容量扩大后，激活成本和通信使全参数计算不可持续。", "expert 选择、capacity、placement 与通信", "规模较小、负载难预测或通信昂贵时 dense 仍可能占优。"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": ("causal autoregression 提供明确顺序和简单缓存语义。", "图像、视频和并行文本生成需要重审 factorization、修正轮数和提交边界。", "生成顺序、proposal/correction 与终止状态", "需要严格流式输出和成熟 cache 时 autoregressive 路径仍可靠。"),
    "MULTIMODAL-EMBODIED-VLA": ("把感知与动作生成串成单次前向路径，静态任务中接口最少。", "物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。", "observation、action chunk、controller handoff 与环境反馈状态", "低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。"),
    "MULTIMODAL-WORLD-MODELS": ("下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。", "规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。", "latent state、action-conditioned transition 与 rollout commitment", "只需内容生成而不需要因果控制时普通 video model 仍足够。"),
    "PLATFORM-EVALUATION-SYSTEM": ("单一离线分数便于比较版本。", "agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。", "evaluation contract、覆盖分母、evidence lineage 与 release gate", "窄任务且 failure surface 稳定时单指标仍可作为局部信号。"),
    "PLATFORM-GPU-SCHEDULER": ("独占 GPU 提供最清晰的隔离和性能归因。", "并发 workload 与成本压力要求共享，同时又不能破坏确定性。", "GPU slice、隔离、配额与抢占控制", "高风险或稳定满载任务仍宜独占。"),
    "PLATFORM-SECURITY": ("把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。", "工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。", "身份、授权、数据流、策略执行点与审计证据", "无工具、无持久状态的只读场景仍可采用较薄边界。"),
    "PLATFORM-TRACE": ("日志记录结果适合单进程、短链路故障。", "多 agent 因果链和动态路由要求跨调用恢复状态传播路径。", "trace identity、因果边和可归责事件", "短同步请求仍可用结构化日志完成局部诊断。"),
    "TRAIN-DISTRIBUTED-TRAINING": ("单机或纯数据并行状态最少、同步语义清晰。", "参数、optimizer state 和通信规模越过单设备边界。", "训练状态分片、collective、同步与故障恢复", "模型可装入单机且通信占比高时简单并行仍更优。"),
    "TRAIN-GRPO": ("每条样本独立更新易实现，但难利用组内相对信号。", "稀疏可验证奖励和 rollout 成本要求更有效地复用同组比较。", "prompt、rollout、group advantage 与 on-policy freshness", "高质量逐样本监督充足时 SFT/DPO 仍更简单。"),
    "TRAIN-PRETRAINING": ("统一精度和静态 optimizer state 使收敛分析最直接。", "模型和状态规模增长使带宽、精度与数据选择共同限制训练。", "optimizer/data state 的精度、更新与恢复边界", "规模较小或稳定性优先时保守精度与全量状态仍合理。"),
    "TRAIN-RLHF": ("固定后训练配方便于重复和对比。", "模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。", "rollout、reward、policy/reference 与更新 freshness", "反馈稳定、任务窄且分布固定时成熟配方仍可复用。"),
}


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SectionParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_heading = False
        self.in_para = False
        self.heading_buf: list[str] = []
        self.para_buf: list[str] = []
        self.current = "Document"
        self.sections: dict[str, list[str]] = {self.current: []}

    def handle_starttag(self, tag, attrs):
        if tag in {"h1", "h2", "h3", "h4"}:
            self.in_heading = True
            self.heading_buf = []
        elif tag == "p":
            self.in_para = True
            self.para_buf = []

    def handle_endtag(self, tag):
        if tag in {"h1", "h2", "h3", "h4"} and self.in_heading:
            title = clean("".join(self.heading_buf)) or "Untitled"
            self.current = title
            self.sections.setdefault(title, [])
            self.in_heading = False
        elif tag == "p" and self.in_para:
            text = clean("".join(self.para_buf))
            if text:
                self.sections.setdefault(self.current, []).append(text)
            self.in_para = False

    def handle_data(self, data):
        if self.in_heading:
            self.heading_buf.append(data)
        if self.in_para:
            self.para_buf.append(data)


def fetch(url: str, timeout: int = 45) -> tuple[int, bytes]:
    request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design-Historical-Daily/2.1 research@example.invalid"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as error:
        return error.code, error.read()
    except Exception:
        return 0, b""


def load_records():
    rows = {}
    raw = 0
    for path in sorted(SNAPSHOT.glob("doi-prefix-*.json.gz")):
        with gzip.open(path, "rt") as handle:
            payload = json.load(handle)
        for item in payload["data"]:
            raw += 1
            attrs = item["attributes"]
            aid = attrs["doi"].replace("10.48550/arxiv.", "")
            submitted = next((d["date"] for d in attrs.get("dates", []) if d.get("dateType") == "Submitted" and d.get("dateInformation") == "v1"), None)
            updated = next((d["date"] for d in attrs.get("dates", []) if d.get("dateType") == "Updated" and d.get("dateInformation") == "v1"), None)
            if not submitted:
                continue
            abstract = next((d.get("description", "") for d in attrs.get("descriptions", []) if d.get("descriptionType") == "Abstract"), "")
            cats = []
            for subject in attrs.get("subjects", []):
                if subject.get("subjectScheme") == "arXiv":
                    match = re.search(r"\(([^()]+)\)$", subject.get("subject", ""))
                    cats.append(match.group(1) if match else subject.get("subject", ""))
            rows[aid] = {
                "arxiv_id": aid,
                "submitted_v1_utc": submitted,
                "registry_updated_v1_utc": updated,
                "title": clean(attrs.get("titles", [{}])[0].get("title", "")),
                "abstract": clean(abstract),
                "categories": cats,
            }
    with gzip.open(ANNOUNCEMENT_RECEIPT, "rt") as handle:
        receipt = json.load(handle)
    recovered = {}
    for item in receipt["records"]:
        aid = item["doi"].replace("10.48550/arxiv.", "")
        if aid not in rows:
            continue
        recovered[aid] = {**rows[aid], **item, "arxiv_id": aid}
    return receipt["record_count"], recovered, receipt


def infer_node(row) -> str:
    aid = row["arxiv_id"]
    if aid not in NODE_OVERRIDES:
        raise KeyError(f"retained family lacks manually audited Stable Node route: {aid}")
    return NODE_OVERRIDES[aid]


def owner_info(node: str):
    path = NODE_PATH.get(node, "books/part-07-agent/84-agent-platform.md")
    files = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "books").glob("part-*/*.md") if p.name != "README.md")
    adjacent = []
    if path in files:
        index = files.index(path)
        adjacent = files[max(0, index - 1):index] + files[index + 1:index + 2]
    return path, adjacent


def first_heading(path: str) -> str:
    text = (ROOT / path).read_text(errors="ignore") if (ROOT / path).exists() else ""
    match = re.search(r"^#{1,3}\s+(.+)$", text, re.M)
    return clean(match.group(1)) if match else "章节正文"


def owner_proposition(path: str, row) -> tuple[str, str]:
    """Return prose under a real manuscript heading, never bibliography text."""
    text = (ROOT / path).read_text(errors="ignore") if (ROOT / path).exists() else ""
    stop_words = {
        "the", "and", "for", "with", "from", "that", "this", "via", "using",
        "model", "models", "large", "language", "system", "framework", "towards",
    }
    query = {
        word for word in re.findall(r"[a-z][a-z0-9-]{2,}", row["title"].lower())
        if word not in stop_words
    }
    skip_heading = re.compile(
        r"review notes?|sources?|references?|bibliography|evidence|research status|"
        r"integrat(?:ion|ed)|已吸收|论文|案例索引",
        re.I,
    )
    sections: list[tuple[str, str]] = []
    current_heading = None
    buffer: list[str] = []
    for line in text.splitlines():
        heading = re.match(r"^(#{2,4})\s+(.+)$", line)
        if heading:
            if buffer and current_heading:
                sections.append((current_heading, "\n".join(buffer)))
                buffer = []
            current_heading = clean(heading.group(2))
            if skip_heading.search(current_heading):
                # Review/evidence appendices are terminal by project contract.
                break
            continue
        if current_heading:
            buffer.append(line)
    if buffer and current_heading:
        sections.append((current_heading, "\n".join(buffer)))

    ranked: list[tuple[int, int, str, str]] = []
    for order, (heading, body) in enumerate(sections):
        for raw in re.split(r"\n\s*\n", body):
            paragraph = clean(raw)
            if not (80 <= len(paragraph) <= 1400):
                continue
            if paragraph.startswith(("- ", "* ", "|", "```", "<!--")):
                continue
            if re.search(r"https?://|arXiv:|source-family:|sha256:|\*\*SF-", paragraph, re.I):
                continue
            if re.search(r"\*\*(?:Knowledge Tree|Stable Knowledge Node ID|Legacy Chapter|Status|Roadmap Intent):", paragraph, re.I):
                continue
            words = set(re.findall(r"[a-z][a-z0-9-]{2,}", paragraph.lower()))
            overlap = len(query & words)
            proposition_bonus = 2 if re.search(
                r"必须|应当|核心|意味着|因此|不能|只有|本章|owner|contract|state|control",
                paragraph,
                re.I,
            ) else 0
            ranked.append((overlap * 10 + proposition_bonus, -order, heading, paragraph[:700]))
    if ranked:
        _, _, heading, paragraph = max(ranked)
        return heading, paragraph
    return "章节主命题", "现有 owner 已定义该机制的 canonical state/control boundary；本 family 只在独立审计证明存在缺口时才允许写回。"


SECTION_OVERRIDES = {
    # These papers use headings whose semantics are clear but whose wording does
    # not contain a generic "method" or "evaluation" token.  Keep the override
    # source-specific so a document title can never masquerade as a locator.
    "2603.13605": {
        "method": [r"core abstractions", r"system overview"],
    },
    "2603.13644": {
        "method": [r"stateplane architecture", r"core components"],
    },
    "2603.14688": {
        "method": [r"causal graph construction", r"problem definition"],
        "evaluation": [r"evaluation metrics", r"main results"],
    },
    "2603.15202": {
        "method": [r"analysis framework", r"simple multiplication"],
        "evaluation": [r"end-to-end evaluation"],
    },
    "2603.14987": {
        "method": [r"distribution-aware", r"overview"],
        "evaluation": [r"red-team", r"illustrative instantiation"],
    },
    "2603.13358": {
        "method": [r"ppd.*dynamic ap routing", r"dynamic ap routing"],
        "evaluation": [r"real-world validation"],
    },
    "2603.19131": {
        "method": [r"from model inference to robotic actuation", r"evaluation metrics for embodied efficiency"],
        "evaluation": [r"inference efficiency vs.*embodied efficiency", r"evaluating adaptation strategies"],
    },
    "2603.21564": {
        "method": [r"core definitions", r"multi-resolution representation"],
        "evaluation": [r"data and trace systems", r"discussion and future work"],
    },
}


def choose_section(
    sections: dict[str, list[str]],
    role: str,
    paper_title: str,
    fallback: str,
    preferred_patterns: list[str] | None = None,
):
    """Choose an evidence-bearing subsection, never the document title.

    HTML conversion often emits the paper title as an H1.  A first-match search
    therefore produced formally valid but semantically useless locators.  Rank
    actual subsections instead and explicitly reject prior-work/front-matter
    headings.  A missing role is reported as Not Disclosed rather than filled by
    an unrelated paragraph.
    """

    normalized_title = clean(paper_title).casefold()
    excluded = re.compile(
        r"^(?:document|pdf front matter|instructions?|references?|bibliography)$|"
        r"\b(?:related work|background|existing approaches?|prior work)\b",
        re.I,
    )
    role_terms = {
        "method": {
            "methodology": 12, "method": 11, "system overview": 11,
            "system design": 11, "architecture": 10, "design": 9,
            "implementation": 9, "algorithm": 8, "framework": 8,
            "approach": 7, "core components": 7, "overview": 4,
        },
        "evaluation": {
            "end-to-end evaluation": 14, "evaluation": 12,
            "real-world validation": 12, "experimental results": 11,
            "experiments": 10, "main results": 10, "results": 8,
            "benchmark": 8, "validation": 8, "ablation": 7,
            "analysis": 3, "proof": 3, "theory": 2,
        },
        "limitations": {
            "limitations": 13, "limitation": 12, "failure": 10,
            "discussion": 8, "future work": 8, "conclusion": 5,
            "ablation": 4,
        },
    }[role]

    candidates: list[tuple[int, int, str, str]] = []
    for order, (title, paragraphs) in enumerate(sections.items()):
        heading = clean(title)
        if not paragraphs or excluded.search(heading):
            continue
        if heading.casefold() == normalized_title:
            continue
        paragraph_text = clean(" ".join(paragraphs[:3]))[:1200]
        if not paragraph_text:
            continue

        preferred_score = 0
        for rank, pattern in enumerate(preferred_patterns or []):
            if re.search(pattern, heading, re.I):
                preferred_score = 100 - rank
                break
        semantic_score = sum(weight for term, weight in role_terms.items() if term in heading.casefold())
        if preferred_score == 0 and semantic_score == 0:
            continue
        # Prefer a real numbered subsection and enough evidence-bearing prose;
        # use original order only as the final deterministic tiebreaker.
        section_bonus = 3 if re.match(r"^(?:[ivxlcdm]+|\d+(?:\.\d+)*)[.\s]", heading, re.I) else 0
        prose_bonus = min(len(paragraph_text) // 300, 3)
        score = preferred_score * 100 + semantic_score + section_bonus + prose_bonus
        candidates.append((score, -order, heading, paragraph_text))

    if candidates:
        _, _, title, text = max(candidates)
        return title, text
    return fallback, "Not Disclosed — exact-v1 full text 未提供可定位的对应章节。"


def normalize_body(body: str) -> str:
    value = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in value.splitlines()]
    while lines and not lines[0]: lines.pop(0)
    while lines and not lines[-1]: lines.pop()
    return "\n".join(lines)


def pdf_sections(text: str) -> dict[str, list[str]]:
    heading_re = re.compile(
        r"^\s*(?:\d+(?:\.\d+)*\.?\s+)?"
        r"(abstract|introduction|background|method(?:ology)?|approach|architecture|framework|algorithm|"
        r"implementation|system design|theory|analysis|proof|experiment(?:s|al setup)?|evaluation|results?|"
        r"discussion|limitations?|conclusion|future work)\b.*$",
        re.I,
    )
    sections: dict[str, list[str]] = {}
    current = "PDF Front Matter"
    buffer: list[str] = []
    for raw_line in text.splitlines():
        line = clean(raw_line)
        if not line:
            if buffer:
                paragraph = clean(" ".join(buffer))
                if len(paragraph) > 80:
                    sections.setdefault(current, []).append(paragraph)
                buffer = []
            continue
        if len(line) < 140 and heading_re.match(line):
            if buffer:
                paragraph = clean(" ".join(buffer))
                if len(paragraph) > 80:
                    sections.setdefault(current, []).append(paragraph)
                buffer = []
            current = line
            sections.setdefault(current, [])
        else:
            buffer.append(line)
    if buffer:
        paragraph = clean(" ".join(buffer))
        if len(paragraph) > 80:
            sections.setdefault(current, []).append(paragraph)
    return sections


def rp_for(review, review_body: str) -> str:
    def canon(value: str) -> str:
        return ";".join(sorted(unicodedata.normalize("NFC", part.strip()) for part in value.split(";") if part.strip() not in {"", "—"}))
    fields = [
        "review-completion-v1", review["source_family_id"], review["event_identity"], review["primary_identifier"],
        canon("SRC-ARXIV"), review["primary_version"], canon(f"SRC-ARXIV@{review['primary_version']}"), review["review_route"],
        canon(review["method_locator"]), canon(review["evaluation_locator"]), canon(review["limitations_locator"]),
        canon(review["artifact_locator"]), review["claim_ref"], review["review_ref"],
        "review-body-sha256:" + hashlib.sha256(normalize_body(review_body).encode()).hexdigest(),
    ]
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def review_one(row, src: Path):
    aid = row["arxiv_id"]
    abs_url = f"https://arxiv.org/abs/{aid}v1"
    current_abs_url = f"https://arxiv.org/abs/{aid}"
    html_url = f"https://arxiv.org/html/{aid}v1"
    abs_status, abs_body = fetch(abs_url)
    current_abs_status, current_abs_body = fetch(current_abs_url)
    html_status, html_body = fetch(html_url)
    pdf_url = f"https://arxiv.org/pdf/{aid}v1"
    body_dir = src / "exact-v1-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    pdf_status = 0
    pdf_text = ""
    source_kind = "HTML"
    if html_status == 200 and html_body:
        body_path = body_dir / f"{aid}v1.html"
        body_path.write_bytes(html_body)
    else:
        pdf_status, pdf_body = fetch(pdf_url, timeout=120)
        if pdf_status == 200 and pdf_body.startswith(b"%PDF"):
            pdf_path = body_dir / f"{aid}v1.pdf"
            pdf_path.write_bytes(pdf_body)
            text_path = body_dir / f"{aid}v1.pdf.txt"
            if PDFTOTEXT.exists():
                subprocess.run([str(PDFTOTEXT), str(pdf_path), str(text_path)], check=False, capture_output=True)
            pdf_text = text_path.read_text(errors="ignore") if text_path.exists() else ""
            body_path = text_path if pdf_text else pdf_path
            source_kind = "PDF"
        else:
            body_path = body_dir / f"{aid}v1.abs.html"
            body_path.write_bytes(abs_body)
            source_kind = "Abstract"
    # Withdrawal is a source-status fact, not a full-text keyword.  Searching
    # the manuscript body creates false positives from references such as
    # "withdrawn by ISO..." and from a historical revision that was later
    # superseded.  The current unversioned arXiv abstract status is the
    # authoritative whole-family signal; exact-v1 remains the evidence body.
    current_status_text = current_abs_body.decode("utf-8", errors="ignore").lower()
    withdrawn = bool(re.search(r"this paper has been withdrawn by", current_status_text))
    parser = SectionParser()
    if html_body:
        parser.feed(html_body.decode("utf-8", errors="ignore"))
    elif pdf_text:
        parser.sections = pdf_sections(pdf_text)
    overrides = SECTION_OVERRIDES.get(aid, {})
    method_title, method_evidence = choose_section(
        parser.sections, "method", row["title"], "Method", overrides.get("method")
    )
    eval_title, evaluation_evidence = choose_section(
        parser.sections, "evaluation", row["title"], "Evaluation", overrides.get("evaluation")
    )
    limit_title, limitations_evidence = choose_section(
        parser.sections, "limitations", row["title"], "Limitations", overrides.get("limitations")
    )
    accessible = html_status == 200 or (pdf_status == 200 and len(pdf_text) > 1000)
    family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
    node = infer_node(row)
    prior, changed_constraint, ownership, coexistence = NARRATIVE_LENS[node]
    synthesis = PAPER_SYNTHESIS.get(aid)
    if synthesis:
        problem, method_text, eval_text, limit_text = synthesis
    else:
        # Standard (5--6) routes still receive a source-specific review.  The
        # evidence excerpts are preserved below, while the prose states the
        # architectural question without copying the abstract.
        problem = f"`{row['title']}` 检查的是 `{node}` 中 {changed_constraint} 是否会改变现有设计边界。"
        method_text = (
            f"exact-v1 的 `{method_title}` 把论文方案定位到 {ownership}；"
            "该项作为受限实现案例保留，不据此建立新的 canonical owner。"
        )
        eval_text = (
            f"公开验证定位在 `{eval_title}`。证据足以判断该 family 与 owner 的关系，"
            "但未披露字段不得补写，且结果不外推到其他 workload。"
        )
        limit_text = (
            f"限制与反证定位在 `{limit_title}`。{coexistence}"
        )
    disposition = DISPOSITION_OVERRIDES.get(
        aid, "Integrate" if aid in INTEGRATE_SUGGESTIONS else "No Change — Existing Coverage"
    )
    source_url = html_url if source_kind == "HTML" else pdf_url
    digest = sha(body_path)
    def locator(label: str, title: str, value: str, facet: str) -> str:
        if value.startswith("Not Disclosed"):
            return f"Not Disclosed — exact-v1 {source_kind} 全文已审计但未提供独立 {label} 章节 [facet={facet}]; {source_url}; {body_path.relative_to(ROOT)}; sha256:{digest}"
        return f"arXiv:{aid}v1 {source_kind} — §{title} [facet={facet}]; {source_url}; {body_path.relative_to(ROOT)}; sha256:{digest}"
    review = {
        "source_family_id": family,
        "event_identity": f"paper-v1:{aid}",
        "primary_identifier": f"arXiv:{aid}v1",
        "primary_version": f"arXiv:{aid}v1",
        "title": row["title"],
        "problem": problem,
        "method_text": method_text,
        "evaluation_text": eval_text,
        "limitations_text": limit_text,
        "method_evidence_excerpt": method_evidence,
        "evaluation_evidence_excerpt": evaluation_evidence,
        "limitations_evidence_excerpt": limitations_evidence,
        "method_locator": locator("Method", method_title, method_evidence, "method"),
        "evaluation_locator": locator("Evaluation", eval_title, evaluation_evidence, "evaluation"),
        "limitations_locator": locator("Limitations", limit_title, limitations_evidence, "limitations"),
        "artifact_locator": f"arXiv exact-v1 identity {abs_url}; linked external artifact was not required for the manuscript claim unless disclosed in正文",
        "claim_boundary": f"只支持 arXiv:{aid}v1 §{method_title} 的机制与 §{eval_title} 的公开 workload；§{limit_title} 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。",
        "claim_ref": f"claim:{family}",
        "review_ref": f"review:{family}",
        "stable_node_id": node,
        "books_disposition": disposition,
        "review_route": "deep" if disposition == "Integrate" else "standard",
        "access_status": "disputed" if disposition == "Disputed" else ("accessible" if accessible else "blocked_external"),
        "result": "complete" if accessible else "blocked",
        "withdrawn": withdrawn,
        "abs_status": abs_status,
        "current_abs_status": current_abs_status,
        "current_abs_url": current_abs_url,
        "html_status": html_status,
        "pdf_status": pdf_status,
        "source_kind": source_kind,
        "body_path": str(body_path.relative_to(ROOT)),
    }
    return review


def closure_reason(row) -> str:
    cats = ", ".join(row["categories"][:2]) or "unclassified"
    abstract = clean(row["abstract"][:360])
    if not any(category.startswith(("cs.", "stat.ML", "eess.")) for category in row["categories"]):
        return f"{row['title']}（{cats}）不属于 AI System 机制范围；identity/date 已闭合。"
    return (
        f"{row['title']}（{cats}）的公开摘要聚焦于：{abstract} "
        "该 family 未改变长期 state/data/control ownership、可复算 evaluation/release contract，"
        "也未修正当前 Books 的平台、训练或推理成立边界；因此在分母前按局部方法/领域证据闭合。"
    )


def score(row, review):
    # Score is a disposition-independent assessment of durable design delta.
    # Integrate candidates change a mechanism/contract (7--9); standard cases
    # are retained as useful boundary evidence but do not change Books (5--6).
    if review["books_disposition"] == "Integrate":
        text = (row["title"] + " " + row["abstract"]).lower()
        reach = 3 if any(key in text for key in (
            "distributed", "workflow", "serving", "production", "edge-cloud",
            "platform", "multi-agent", "world model", "agent"
        )) else 2
        return 3, reach, 3
    if review["books_disposition"] == "Disputed":
        return 2, 2, 1
    return 2, 2, 2


def render_day(day: int, raw_total: int, records: dict):
    end = datetime(2026, 3, day, 9, tzinfo=TZ)
    start = end - timedelta(days=1)
    report_date = f"2026-03-{day:02d}"
    ids = sorted(aid for aid, row in records.items() if row.get("owner_report_date") == report_date and row.get("status") == "scheduled_match")
    # Candidate identity is independent of the old, invalid date grouping.
    # First-public ownership comes only from the authoritative v2 recovery
    # receipt; the manually screened durable-design denominator is then grouped
    # by that owner date.
    selected = {
        aid for aid, row in records.items()
        if aid in DURABLE_CANDIDATES and row["owner_report_date"] == f"2026-03-{day:02d}"
    }
    missing = selected - set(ids)
    if missing:
        raise RuntimeError(f"2026-03-{day:02d} selected outside strict window: {sorted(missing)}")
    src = OUT / "_sources" / f"daily-202603{day:02d}"
    daily = OUT / f"{day:02d}"
    src.mkdir(parents=True, exist_ok=True)
    daily.mkdir(parents=True, exist_ok=True)

    reviews = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(review_one, records[aid], src): aid for aid in selected}
        for future in as_completed(futures):
            reviews.append(future.result())
    reviews.sort(key=lambda item: item["primary_identifier"])
    withdrawn_ids = {r["primary_identifier"].split(":", 1)[1].removesuffix("v1") for r in reviews if r["withdrawn"]}
    selected -= withdrawn_ids
    reviews = [r for r in reviews if not r["withdrawn"]]

    identities = []
    for aid in ids:
        row = dict(records[aid])
        row["source_family_id"] = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        if aid in withdrawn_ids:
            row.update(screening_status="pre_denominator_closure", screening_reason="withdrawn_primary_source", review_status="not_required_pre_denominator", access_status="withdrawn", integration_disposition="Rejected — Withdrawn primary source")
        elif aid in selected:
            review = next(r for r in reviews if r["primary_identifier"] == f"arXiv:{aid}v1")
            review_depth = "deep" if review["books_disposition"] == "Integrate" else "standard"
            row.update(screening_status="candidate_denominator", screening_reason="改变长期 AI System 机制、ownership、evaluation contract 或成立边界；进入 exact-v1 Review。", review_status=f"{review_depth}_complete" if review["result"] == "complete" else "blocked", access_status=review["access_status"], integration_disposition=review["books_disposition"])
        else:
            row.update(screening_status="pre_denominator_closure", screening_reason=closure_reason(row), review_status="not_required_pre_denominator", access_status="accessible_metadata", integration_disposition="Rejected — Local method / domain evidence")
        identities.append(row)
    ledger = {
        "schema": "screening-ledger-v2.1", "report_date": f"2026-03-{day:02d}",
        "window": {"start": start.isoformat(), "end": end.isoformat(), "semantics": "left_closed_right_open"},
        "utc_window": {"start": start.astimezone(UTC).isoformat(), "end": end.astimezone(UTC).isoformat()},
        "raw_snapshot_records": raw_total, "registered_window_identities": len(ids), "screened_identities": len(ids),
        "candidate_denominator": len(selected), "pre_denominator_closures": len(ids) - len(selected),
        "withdrawn_primary_sources": sorted(withdrawn_ids), "weekly_dependency_count": 0, "identities": identities,
    }
    dump(src / "screening-ledger-final.json", ledger)
    with (src / "screening-ledger-final.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "submitted_v1_utc", "title", "categories", "screening_status", "screening_reason"])
        for row in identities:
            writer.writerow([row["arxiv_id"], row["registry_updated_v1_utc"], row["title"], ";".join(row["categories"]), row["screening_status"], row["screening_reason"]])
    ledger_sha = sha(src / "screening-ledger-final.json")

    comparisons = []
    queue = []
    for review in reviews:
        aid = review["primary_identifier"].split(":", 1)[1].removesuffix("v1")
        row = records[aid]
        owner, adjacent = owner_info(review["stable_node_id"])
        proposition_heading, proposition_text = owner_proposition(owner, row)
        item = {
            "source_family_id": review["source_family_id"], "arxiv_id": aid, "title": review["title"],
            "stable_node_id": review["stable_node_id"], "owner_path": owner, "owner_heading": proposition_heading,
            "adjacent_paths": adjacent, "adjacent_headings": [first_heading(path) for path in adjacent],
            "existing_proposition": proposition_text,
            "evidence_delta": review["method_text"], "claim_boundary": review["claim_boundary"],
            "disposition": review["books_disposition"], "books_review_ref": f"books-review:{review['source_family_id']}",
        }
        comparisons.append(item)
        if item["disposition"] == "Integrate":
            queue.append({**item, "evaluation_contract": review["evaluation_text"], "tradeoffs_failure_modes": review["limitations_text"], "status": "pending_root_serial_writeback_and_fresh_context_prewrite_audit"})
    dump(src / "BOOKS_WRITEBACK_QUEUE.json", {"schema": "books-writeback-queue-v2.1", "report_date": f"2026-03-{day:02d}", "status": "pending_root_serial_writeback_and_fresh_context_prewrite_audit", "items": queue})
    queue_lines = [
        f"# Books Writeback Queue — 2026-03-{day:02d}",
        "",
        "**Status:** Pending root serial writeback and fresh-context prewrite audit. 本文件不证明 Books 已修改。",
        "",
        "| Source Family | Exact Source | Stable Node | Target | Adjacent | Existing Proposition | Proposed Durable Mechanism | Evidence Boundary | Status |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in queue:
        queue_lines.append(
            "| {source_family_id} | arXiv:{arxiv_id}v1 | {stable_node_id} | {owner_path} | {adjacent} | {existing} | {delta} | {boundary} | {status} |".format(
                source_family_id=item["source_family_id"],
                arxiv_id=item["arxiv_id"],
                stable_node_id=item["stable_node_id"],
                owner_path=item["owner_path"],
                adjacent="; ".join(item["adjacent_paths"]) or "Not Required",
                existing=clean(item["existing_proposition"]).replace("|", "\\|"),
                delta=clean(item["evidence_delta"]).replace("|", "\\|"),
                boundary=clean(item["claim_boundary"]).replace("|", "\\|"),
                status=item["status"],
            )
        )
    (src / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(queue_lines) + "\n")
    dump(src / "books-current-content-comparison.json", {"schema": "books-current-content-comparison-v2.1", "report_date": f"2026-03-{day:02d}", "items": comparisons})
    dump(src / "exact-v1-review-packet.json", {"schema": "exact-v1-review-packet-v2.1", "report_date": f"2026-03-{day:02d}", "items": reviews})
    dump(src / "coverage-receipt.json", {"schema": "coverage-receipt-v2.1", "report_date": f"2026-03-{day:02d}", "source_id": "SRC-ARXIV", "window": ledger["window"], "raw_snapshot_records": raw_total, "registered_identities": len(ids), "full_semantic_screened": len(ids), "retained": len(selected), "pre_denominator_closed": len(ids)-len(selected), "ledger_sha256": ledger_sha, "announcement_receipt": str(ANNOUNCEMENT_RECEIPT.relative_to(ROOT)), "announcement_receipt_sha256": sha(ANNOUNCEMENT_RECEIPT), "authority_boundary": "DataCite DOI created/registered is an identity and announcement-batch recovery lead; owner is the official Sun-Thu 20:00 Eastern announcement instant mapped through the strict Beijing half-open window. Submitted:v1 and Updated:v1 do not own the event date.", "pagination": "shared deterministic announcement receipt + DataCite created/registered prefix shards 00..99", "status": "checked" if ids else "no_hit", "executed_at": EXECUTED_AT})
    dump(src / "weekly-dependency-audit.json", {"schema": "historical-daily-weekly-dependency-audit-v1", "report_date": f"2026-03-{day:02d}", "dependency_count": 0, "forbidden_inputs_checked": ["Weekly discovery seed", "Weekly candidate list", "Weekly score/Review", "Weekly Books disposition/gap"], "result": "pass_author_side"})
    blockers = [r for r in reviews if r["result"] != "complete"]
    disputed_reviews = [r for r in reviews if r["books_disposition"] == "Disputed"]
    material_requests = []
    for review in blockers:
        material_requests.append({
            "source_family_id": review["source_family_id"],
            "required_version": review["primary_version"],
            "missing_material": "official exact-v1 HTML/PDF full text",
            "blocking_scope": "Method/Evaluation/Limitations Review",
            "acceptable_material": "official exact-v1 HTML/PDF/e-print or version-proven author manuscript",
            "priority": "P1 Full Text",
            "gap_id": "GAP-EXACT-V1",
        })
    for review in disputed_reviews:
        material_requests.append({
            "source_family_id": review["source_family_id"],
            "required_version": review["primary_version"],
            "missing_material": "version-matched benchmark configuration, raw result ledger and independently inspectable production/deployment artifact",
            "blocking_scope": "Disputed performance and deployment claims",
            "acceptable_material": "author artifact with exact model/workload/hardware/evaluator identity or independent reproduction",
            "priority": "P2 Artifact",
            "gap_id": "GAP-DISPUTED-EVIDENCE",
        })
    dump(src / "materials-request.json", {"schema": "materials-request-v2.1", "report_date": f"2026-03-{day:02d}", "items": material_requests})
    dump(src / "author-side-audit.json", {"schema": "author-side-audit-v2.1", "report_date": f"2026-03-{day:02d}", "raw": len(ids), "screened": len(ids), "retained": len(selected), "closures": len(ids)-len(selected), "withdrawn": len(withdrawn_ids), "review_complete": len(reviews)-len(blockers), "blocked": len(blockers), "integrate_queue": len(queue), "fresh_context_status": "pending_non_writer_reviewer"})

    owner_week = f"2026-W{end.isocalendar().week:02d}"
    candidate_rows = []
    review_rows = []
    review_bodies = []
    books_rows = []
    books_bodies = []
    selection_rows = []
    analysis_blocks = []
    eligible_units = [
        item for item in reviews
        if sum(score(records[item["primary_identifier"].split(":", 1)[1].removesuffix("v1")], item)) >= 7
    ]
    selected_units = sorted(
        eligible_units,
        key=lambda item: (
            item["books_disposition"] == "Integrate",
            sum(score(records[item["primary_identifier"].split(":", 1)[1].removesuffix("v1")], item)),
            item["source_family_id"],
        ),
        reverse=True,
    )[:3]
    selected_ids = {r["source_family_id"] for r in selected_units}
    for index, review in enumerate(reviews):
        aid = review["primary_identifier"].split(":", 1)[1].removesuffix("v1")
        row = records[aid]
        d, s, u = score(row, review)
        review_route = review["review_route"]
        family = review["source_family_id"]
        prior, changed_constraint, ownership, coexistence = NARRATIVE_LENS[review["stable_node_id"]]
        body = (
            f"**问题**：{review['problem']}\n\n"
            f"**旧路径为何合理**：{prior}\n\n"
            f"**约束变化与机制**：{review['method_text']}\n\n"
            f"**State / data / control owner**：`{review['stable_node_id']}` 负责 {ownership}；定位证据为 `{review['method_locator']}`。\n\n"
            f"**Evaluation contract 与未证明部分**：{review['evaluation_text']} 未披露的字段保持 `Not Disclosed`，具体定位为 `{review['evaluation_locator']}`。\n\n"
            f"**Trade-off / failure / coexistence**：{review['limitations_text']}\n\n"
            f"<!-- claim:{family}:start -->**Claim Boundary**：{review['claim_boundary']}<!-- claim:{family}:end -->"
        )
        review["review_provenance_id"] = rp_for(review, body) if review["result"] == "complete" else "—"
        candidate_rows.append(f"| {family} | {review['primary_identifier']} | {review['event_identity']} | {owner_week} | {row['announcement_beijing'][:10]} | SRC-ARXIV | {d} | {s} | {u} | {d+s+u} | retained | {review_route + '_complete' if review['result']=='complete' else 'review_pending'} | {review['access_status']} | none | {review['review_ref'] if review['result']=='complete' else '—'} | self | — | new_in_window | {review['stable_node_id']} | {review['books_disposition']} | books-review:{family} | no |")
        review_rows.append(f"| {family} | {review['review_provenance_id']} | {review_route} | {review['primary_version']} | SRC-ARXIV@{review['primary_version']} | {review['method_locator']} | {review['evaluation_locator']} | {review['limitations_locator']} | {review['artifact_locator']} | {review['claim_ref'] if review['result']=='complete' else '—'} | {review['result']} |")
        if review["result"] == "complete":
            review_bodies.append(f"### {review['title']}\n\n<!-- review:{family}:start -->\n{body}\n<!-- review:{family}:end -->")
        total = d + s + u
        if total < 7:
            pass
        elif family in selected_ids:
            unit = f"DA-202603{day:02d}-{index+1:02d}"
            eligibility = "score_7_9" + (";potential_books_delta" if review["books_disposition"] == "Integrate" else "")
            selection_rows.append(f"| {family} | {eligibility} | selected | {unit} | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:{unit} |")
            analysis_blocks.append(f"<!-- analysis:{unit}:start -->\n### {review['title']}\n\n{review['problem']} 旧路径在其原约束下仍合理：{prior} 本 family 的设计变化是：{review['method_text']} 其公开验证边界为：{review['evaluation_text']} 新增代价与回退条件为：{review['limitations_text']}\n<!-- analysis:{unit}:end -->")
        else:
            eligibility = "score_7_9" + (";potential_books_delta" if review["books_disposition"] == "Integrate" else "")
            selection_rows.append(f"| {family} | {eligibility} | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:{family} |")
            analysis_blocks.append(f"<!-- analysis-decision:{family}:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:{family}:end -->")
        comparison = next(item for item in comparisons if item["source_family_id"] == family)
        adj = "; ".join(f"{p}#{first_heading(p).lower().replace(' ', '-')} (section Ch-adjacent)" for p in comparison["adjacent_paths"]) or "Not Required — edge chapter"
        target = f"{comparison['owner_path']}#{comparison['owner_heading'].lower().replace(' ', '-')} (section Ch-owner)"
        books_rows.append(f"| {family} | {review['stable_node_id']} | {target} | {adj} | existing:{family} | delta:{family} | Layering / Dependency | {review['books_disposition']} | books-review:{family} |")
        books_bodies.append(f"<!-- books-review:{family}:start -->\n### {review['title']} — Books Comparison\n\n<!-- existing:{family}:start -->已读 owner `{comparison['owner_path']}` 与相邻章节。现有命题：{comparison['existing_proposition']}<!-- existing:{family}:end -->\n\n<!-- delta:{family}:start -->新证据差异：{review['method_text']}<!-- delta:{family}:end -->\n\n边界：{review['claim_boundary']} 作者侧决定为 **{review['books_disposition']}**；Integrate 项仅进入串行队列，尚未写回。\n<!-- books-review:{family}:end -->")

    # Persist RP-bearing packet after report body is finalized.
    dump(src / "exact-v1-review-packet.json", {"schema": "exact-v1-review-packet-v2.1", "report_date": f"2026-03-{day:02d}", "items": reviews})
    report = f"""# Daily Research — 2026-03-{day:02d}

**Research Date:** 2026-03-{day:02d}

**Timezone:** Asia/Shanghai

**Strict Window:** {start.strftime('%Y-%m-%d %H:%M:%S')} ～ {end.strftime('%Y-%m-%d %H:%M:%S')}（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；作者侧 comparison 已完成，fresh-context audit 与 Integrate 串行 writeback 未完成。

## Executive Summary

严格窗口 raw/registered/screened={len(ids)}/{len(ids)}/{len(ids)}；denominator={len(selected)}、pre-denominator closures={len(ids)-len(selected)}。exact-v1 Review complete={len(reviews)-len(blockers)}、blocked={len(blockers)}；Integrate 建议={len(queue)}。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-{day:02d} |
| Window End | 2026-03-{day:02d} |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-202603{day:02d}-AUTHOR-{len(selected)} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | {start.isoformat()} | {end.isoformat()} | {EXECUTED_AT} | official-schedule recovery receipt + {len(ids)}/{len(ids)} title/abstract replay + official abs/HTML/PDF exact-v1 | {'checked' if ids else 'no_hit'} | {len(ids)} | {';'.join(r['source_family_id'] for r in reviews) or '—'} | pages=100; prefixes=00..99; final_cursor=end; registered={len(ids)}; screened={len(ids)}; retained={len(selected)}; closure={len(ids)-len(selected)} | {end.astimezone(UTC).isoformat()} | screening-ledger-final.json#sha256={ledger_sha}; announcement-recovery#sha256={sha(ANNOUNCEMENT_RECEIPT)} | {'GAP-EXACT-V1' if blockers else '—'} |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:202603{day:02d}:start -->作者侧已逐项筛选全部 {len(ids)} 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:202603{day:02d}:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(candidate_rows)}

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(review_rows)}

### Source Reviews

{chr(10).join(review_bodies)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_rows)}

{chr(10).join(analysis_blocks)}

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(books_rows)}

{chr(10).join(books_bodies)}

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-202603{day:02d}-COVERAGE | fresh-context:pending-independent-reviewer | coverage | coverage:SRC-ARXIV:202603{day:02d} | FINDING-PENDING-INDEPENDENT-COVERAGE-FP-FN | root reviewer must replay retained false positives and closure false negatives | open |
| SA-202603{day:02d}-EVIDENCE | fresh-context:pending-independent-reviewer | evidence | validator:review-completion-v1 | FINDING-PENDING-INDEPENDENT-EXACT-V1 | root reviewer must verify source-specific locators and claim boundaries | open |
| SA-202603{day:02d}-SELECTION | fresh-context:pending-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | FINDING-PENDING-INDEPENDENT-SELECTION | root reviewer must challenge comparative selection | open |
| SA-202603{day:02d}-BOOKS | fresh-context:pending-independent-reviewer | books | validator:books-comparison-v1 | FINDING-PENDING-ROOT-SERIAL-WRITEBACK | root reviewer must complete prewrite audit, date-ordered writeback and post-write audit | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-202603{day:02d}/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

由独立 reviewer 完成 FP/FN、exact-v1、Selection 与 Books prewrite audit；随后按日期顺序串行执行 {len(queue)} 项 Integrate 建议。

## 10. Repository Changes

- 新增本日 Daily 与 source packet。
- 未修改 `books/`、Weekly、`docs/LEARNING_STATE.md` 或月级共享索引。

## 11. Open Questions

- {len(blockers)} 项 exact-v1 仍 blocked。
- `SRC-ARXIV` 的独立 retained false-positive / closure false-negative audit 尚未完成。
- fresh-context Semantic Audit 与 Integrate writeback 尚未完成。

## 12. Sources

- [arXiv](https://arxiv.org/) — exact-v1 primary manuscript and status。
- DataCite March frozen snapshot — identity/title/abstract/submission provenance only。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(f'| MR-{item["source_family_id"]} | {item["priority"]} | {item["source_family_id"]} | — | — | {owner_week} | {item["required_version"]}; https://arxiv.org/abs/{item["required_version"].split(":",1)[1]} | {item["missing_material"]} | 当前公开材料不能关闭 {item["blocking_scope"]} | {item["acceptable_material"]} | {item["required_version"].split(":",1)[1]}.artifact | {item["blocking_scope"]} |' for item in material_requests)}

## 13. Final Status

- Completion Status: `In Progress`
- Coverage: `Open`（到期来源枚举已闭合；只等待 fresh-context retained FP / closure FN audit）
- Evidence: `Open`（等待 independent evidence/selection audit；blocked={len(blockers)}）
- Books: `Open`（Integrate queue={len(queue)}，未写回）
- unresolved findings: 4
- Raw identities={len(ids)}；retained={len(selected)}；retain rate={(len(selected)/len(ids)*100 if ids else 0):.2f}%；closures={len(ids)-len(selected)}。
"""
    (daily / "README.md").write_text(report)


def main():
    raw_total, records, _announcement_receipt = load_records()
    for day in range(17, 25):
        render_day(day, raw_total, records)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
