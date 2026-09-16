#!/usr/bin/env python3
"""Apply the bounded author repair requested by the final independent audit.

The transformation is intentionally mechanical: it promotes the eleven
recovered identities, appends their exact-v1 reviews, reconciles current
dispositions, and keeps the Daily Ongoing for a new non-author review.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parents[1] / "07/README.md"
LEDGER = ROOT / "screening-ledger-v3-author-repair.json"
PACKET = ROOT / "exact-v1-review-packet-v3-author-repair.json"
COVERAGE = ROOT / "coverage-receipt.json"


RECOVERED = {
    "2605.04070": {
        "score": [3, 2, 3], "owner": "PLATFORM-EVALUATION-SYSTEM",
        "chapter": "../../../../books/part-06-ai-infrastructure/66-evaluation-system.md",
        "claim": "高风险 human-oversight routing 不能把模型 confidence 当作错误可识别性；应先测 AI 与人的错误重叠、互补区域和人类纠错能力，再决定 route 或 assistance。",
        "method": ["§3.1–§3.4", "在 1,886 个跨知识、事实性、长上下文与欺骗检测样本上比较 confidence hybridization、top-2 assistance 与 subtask delegation；模型 confidence 先经 isotonic calibration，再按固定 calibration/test split 形成路由。"],
        "evaluation": ["§4.1–§4.4；§5", "每项收集 20 个 GPT-5-mini 响应和 3–5 个人类判断；AI 错且人对的互补区域仅 8.9%，confidence routing 相比 AI-only 只增加 0.4pp。top-2 的收益主要来自人采纳正确 AI 候选，而不是识别并推翻 AI 错误。"],
        "limitations": ["§6；Appendix", "任务、模型和 assistance protocol 有限；14 个 tie-breaking 不一致被披露。结果反证所测条件下的 confidence routing，不证明所有模型、人群或领域都缺乏互补性，也不提供生产安全率。"],
        "decision": "已有覆盖",
        "comparison": "Ch66 已明确自报/内部 confidence 只是需按 deployment slice 校准的 sensor，高风险 route/defer 还需外部证据、human adjudication 与 risk-coverage；本结果为该命题提供受限反证，但不改变 owner 或 fallback。",
    },
    "2605.04083": {
        "score": [3, 2, 3], "owner": "PLATFORM-EVALUATION-SYSTEM",
        "chapter": "../../../../books/part-06-ai-infrastructure/66-evaluation-system.md",
        "claim": "Evaluation 必须冻结 criterion、judge procedure 与 aggregation；聚合后 task score 稳定可能掩盖 criterion-level jury dissent，低成本 jury 不能未经 human anchor 就取得同等判定权。",
        "method": ["§3–§4", "把专家要求编码为逐 criterion 的稳定 evaluation contract，并在 model-only Inspect 与 agentic Harbor 中复用；固定 task/reference/criteria/aggregation，只替换五模型 frontier 或 compact jury。"],
        "evaluation": ["§5", "四个 frontier-class solver 上 criterion agreement 为 75.9%–89.6%，compact jury 的 3–2 dissent 明显更高；成本/延迟下降很多，但聚合 task outcome 往往把差异冲淡。"],
        "limitations": ["§6", "agreement 是相对 frontier jury，不是绝对正确率；分歧项没有 human/gold adjudication，只测单一 agent/harness 与有限任务。不能把成本下降外推成 judge 等价。"],
        "decision": "已有覆盖",
        "comparison": "Ch66 已把 per-criterion outcomes、judge/rater identity、aggregation function、disagreement 和 release authority 分权保存；该 source family 强化了 aggregation masking 边界，但未改变现有 contract。",
    },
    "2605.04256": {
        "score": [3, 2, 2], "owner": "AGENT-MCP",
        "chapter": "../../../../books/part-07-agent/83-mcp.md",
        "claim": "异构物理神经基底不能被压平成无状态 tool；control plane 必须暴露 capability、时钟、生命周期、遥测、校准与安全状态，并把 twin state 与真实 substrate execution 分权管理。",
        "method": ["§III–§V", "定义 capability descriptor、timing/lifecycle/telemetry contract，并把 control plane、twin plane 与 substrate-specific data plane 分离；task matcher 只能在当前 readiness、policy 与 twin validity 下提出 backend。"],
        "evaluation": ["§VII–§VIII", "reference prototype 覆盖三类代表性 backend、HTTP externalized path 与 Cortical Labs wetware-facing API；验证 descriptor portability、runtime-aware matching、代表性故障下的 telemetry recovery 与局部 control-path overhead。"],
        "limitations": ["§VIII-D", "证据是 reference architecture 与 prototype-level validation，不是成熟 substrate、跨地域分布式部署或生产安全证明；twin fidelity、物理漂移和 substrate-specific policy 仍需独立验收。"],
        "decision": "整合",
        "comparison": "Ch83 已有唯一正文明确物理 capability 不能被普通 MCP tool schema 压平，并保留 calibration、safety、人工审批与 substrate adapter 边界；本轮恢复账本绑定，不重复写正文。",
    },
    "2605.04450": {
        "title": "One Pool, Two Caches: Adaptive HBM Partitioning for Accelerating Generative Recommender Serving",
        "score": [3, 2, 2], "owner": "INFER-GPU-MEMORY",
        "chapter": "../../../../books/part-05-inference-system/54-gpu-memory.md",
        "claim": "当 embedding hot cache 与 KV cache 竞争同一 HBM 时，静态分池会随 workload regime 变化而失效；memory allocator 与 request router 必须共享同一容量、迁移与 tail-SLO contract。",
        "method": ["§3–§4", "以 online residual policy 调整 EMB/KV 分区，以 burst-aware recovery 限制突发期动作，并让 router 同时考虑 KV residency、embedding locality 与 node load；allocation proposal 不等于迁移已经完成。"],
        "evaluation": ["§5–§6", "三类 production-scale dataset、32-node A100、8K–15K sequences、Steady/Trend/Burst 三类 workload regime 与五次重复运行；P99 与 SLO 数字只属于所披露模型、硬件、分区和路由实现。"],
        "limitations": ["§7", "证据来自生成式推荐的 EMB/KV 双缓存，不证明普通 LLM serving 也存在相同比例或收益；online controller 还引入 H2D refill、policy drift、跨节点路由与 burst recovery failure。"],
        "decision": "整合",
        "comparison": "Ch54 已统一 weights、KV、workspace 与 reserve 的 HBM 预算，但缺少两个独立 cache class 共享 HBM 时 allocator 与 router 的联合控制；需补入动态分池的提交边界、P99 风险和静态回退。",
    },
    "2605.04922": {
        "score": [3, 2, 2], "owner": "AGENT-WORKFLOW",
        "chapter": "../../../../books/part-07-agent/81-workflow.md",
        "claim": "多 Agent 并行修订不能让 role-local 文本直接覆盖共享真值；各角色应在同一 frozen snapshot 上形成 typed patch，固定顺序 materialize 后再由 graph-global commit 判断是否进入最终 artifact。",
        "method": ["§3.2–§3.4；Appendix C–D", "typed idea graph 保存 claim、assumption、risk、evidence need 与它们的关系；role-local action selection、patch materialization、deterministic merge、realized transition 与 graph-global commit 被拆成不同 runtime object。"],
        "evaluation": ["§4；Appendix H", "AI Idea Bench 2025 与 LiveIdeaBench 的 512-group held-out packet、三 seeds 和 controller/frozen-snapshot ablation 支持所测 ideation runtime；顺序更新对照还混有 drop-in controller mismatch。"],
        "limitations": ["§5；Appendix H–I", "结果只评价 proposal quality，不验证科学结论或真实实验；critic 来自 heuristic weak labels，graph schema 固定，benchmark evaluator 和 Qwen3-8B backbone 限制外推。"],
        "decision": "整合",
        "comparison": "Ch81 已有 durable DAG、branch artifact 与 aggregation commit，但缺少同一轮多角色基于 frozen shared state 提案、先验证 patch 再 materialize、最后由 graph-global owner commit 的细粒度状态链；需补入并发可比性和 merge/fallback 边界。",
    },
    "2605.04165": {
        "score": [3, 1, 2], "owner": "PLATFORM-EVALUATION-SYSTEM",
        "chapter": "../../../../books/part-06-ai-infrastructure/66-evaluation-system.md",
        "claim": "生成式 UI 评价应把静态外观与可执行 interaction flow 分开；reference trace 是可诊断 evidence，但 metric、CUA 与 reference coverage 都必须属于 evaluation identity。",
        "method": ["§3.1–§3.3", "从高质量 reference UI 与生成 UI 运行同一验证任务，由 CUA 产生截图轨迹，再以 DTW、eBLEU 与 WMD 比较交互序列；不是只让 MLLM 看最终截图。"],
        "evaluation": ["§4–§4.1", "27 个 reference sites、7 个 generator、每条件 5 次，共 945 个 UI；两位 HCI 专家提供 429 个盲比较。WMD 对人类 Elo 的 Spearman 相关为 0.96，但逐对 agreement 只有 73.0%。"],
        "limitations": ["Limitations: Scope / Implementation / Evaluation", "只覆盖 common one-shot web flows；两个 annotator、一个 CUA，best-of-nine aggregation 依赖 agent 能力。缺少认证/支付等受限流程、迭代式开发、可访问性、安全与完整生产评价。"],
        "decision": "已有覆盖",
        "comparison": "Ch66 已要求以可执行 environment transition、artifact 与 human anchor 评价 agent，不让 judge 取代 outcome；FlowEval 是 UI trace 的受限实例，未改变现有 evaluation owner。",
    },
    "2605.04279": {
        "score": [3, 1, 3], "owner": "MODEL-MULTI-HEAD-ATTENTION",
        "chapter": "../../../../books/part-02-model/15-multi-head-attention.md",
        "claim": "多头 Attention 的总能量可具有梯度流结构，但单头演化仍经共享 token state 和球面投影发生 radial-shadow 耦合；head 正交不等于优化动力学独立。",
        "method": ["§2–§4", "在单位球面 token dynamics 上定义多头 interaction field 与总能量，分解每头输出的切向分量和 radial shadow，并给出 per-head 单调性的充分 Radial Dominance 条件及近似正交鲁棒性。"],
        "evaluation": ["§5–§7", "主要证据是定理：标量/equiangular regime 给出 critical inverse temperature、异质头的 super-additive early clustering rate、ReLU/softmax 线性化时间分离与 entropy production identity；不是生产模型 benchmark。"],
        "limitations": ["§8；assumptions in §3–§7", "许多结论依赖 score symmetry、sphere-normalized dynamics 或 scalar/equiangular regime；未证明训练后真实 Transformer 的所有 heads 满足充分条件，也未给出通用因果功能分工。"],
        "decision": "整合",
        "comparison": "Ch15 当前解释多头的表示子空间、聚合与冗余，但尚未写清共享 token trajectory 使 head optimization 非独立，以及正交仍不能消除 radial-shadow coupling；需由 root 在既有主线中补入受限机制。",
    },
    "2605.04291": {
        "score": [3, 1, 2], "owner": "MULTIMODAL-GENERATIVE-PARADIGMS",
        "chapter": "../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
        "claim": "离散 text diffusion 可把预训练 causal/masked LM 作为能量/条件分布来定义 Glauber transition，并以迭代局部重写换取全局修正；这与均匀 corruption 的从零训练是不同分支。",
        "method": ["§3–§3.1；Appendix A/D", "把单位置条件重采样解释为 mask-infilling，使用共享 causal/masked 权重的 UL2 构造能量与 stationary-distribution proxy，再增加 timestep embedding 并以 score-entropy objective 训练反向 Glauber dynamics。"],
        "evaluation": ["§4.1–§4.4", "在 UL2/T5-Gemma 规模与语言建模、commonsense、Sudoku/Zebra 上比较 diffusion 与 AR；iso-compute 比较把一次 AR pass 加一次 full edit 与两个 AR candidates 对齐。结果依赖作者 evaluator 和有限模型。"],
        "limitations": ["§7", "比既有 discrete diffusion 与 AR 需要更多 model invocations；大模型训练披露为 32×H100 近 6 天。stationary/energy 解释不等于有限步采样已经收敛，也不证明生产 latency 或 streaming 优势。"],
        "decision": "整合",
        "comparison": "Ch24 已覆盖 AR、masked/diffusion、iterative correction 与 commit，但缺少“复用预训练 LM 条件分布作为能量来定义局部 transition”的演进分支；root 应补入该机制并保留更多 NFE、收敛与 streaming fallback。",
    },
    "2605.04569": {
        "score": [3, 2, 2], "owner": "INFER-TENSORRT-LLM",
        "chapter": "../../../../books/part-05-inference-system/49-tensorrt-llm.md",
        "claim": "动态稀疏 Attention 不应只按 token saliency 剪枝；execution plan 可依据 query-specific approximation-risk proxy，在 full attention 与低阶近似路径之间逐块路由并保留 exact fallback。",
        "method": ["§3.2–§3.5", "ISA 先按 saliency 预选 context K/V，再用 query sharpness 作为 approximation error proxy：高风险 query 走 full attention，低风险 query 走 blockwise zeroth-order Taylor sparse attention。"],
        "evaluation": ["§4.1–§4.5；ablation", "LIVEditor-14B 与三类视频编辑 benchmark 上报告 attention-module latency 约降 60%；公开 sensitivity 显示提高 full-path sparsity 会降低质量，作者配置的端到端加速约 1.47×。数字只属于所披露模型/硬件与阈值。"],
        "limitations": ["§4.4–§5", "“near-lossless”是作者 benchmark 结论；query sharpness 不是通用误差证书，阈值、block shape、预选成本与视觉指标均 workload-dependent。unsupported shape 或 proxy 漂移时必须回退 full attention。"],
        "decision": "整合",
        "comparison": "Ch49 已拥有 sparse/approximate kernel 的 execution identity 和 dense fallback，但尚缺 query-level risk routing 把 exact 与 Taylor path 同时纳入 plan；root 应补入该条件分支，不外推视频编辑速度。",
    },
    "2605.04637": {
        "score": [3, 2, 2], "owner": "PLATFORM-EVALUATION-SYSTEM",
        "chapter": "../../../../books/part-06-ai-infrastructure/66-evaluation-system.md",
        "claim": "Coding-agent 平台评价必须区分从零创建与修改既有系统，并沿 requirements、artifact、runtime、operations 与 security 保存分阶段 evidence，避免漂亮 UI 掩盖后端和生产失败。",
        "method": ["§3–§5", "以 ACR/AMR × PM/Engineering/Ops × T4/T5 组织 68 个指标，并按 deterministic、LLM、human、expert judge tiers 组合需求、代码、运行、运维和安全证据。"],
        "evaluation": ["§6–§7", "六个平台、三个领域、18 个 evaluation cells；报告 specification bottleneck、frontend/backend decoupling、production-readiness cliff 与安全/并发失败。AMR 只在 QwikBuild 上执行，结论是描述性样本。"],
        "limitations": ["§8", "作者中两人与 QwikBuild 有关联；平台、prompt、版本、部署环境和 judge 有限，AMR 横向不可比。不能从分数推断所有 vibe-coding 平台或真实长期维护能力。"],
        "decision": "已有覆盖",
        "comparison": "Ch66 已区分 static issue、从零 repository、需求访问、完整 artifact、测试、部署/安全与 environment identity，并要求分阶段 evidence；该 68-metric benchmark 提供实例，但未改变现有主线。",
    },
    "2605.04677": {
        "score": [2, 2, 2], "owner": "AGENT-WORKFLOW",
        "chapter": "../../../../books/part-07-agent/81-workflow.md",
        "claim": "LLM 代码优化应把 runtime profile 当作 target-selection evidence，把候选 edit 当作 proposal；只有通过 build、tests、performance 与静态检查的 artifact 才能进入搜索 population。",
        "method": ["§3.1–§3.5", "用 JFR 构造带 cumulative time/call count 的 component graph，选择热点并冻结邻接 read-only context；MCTS/evolution 生成局部 edits，级联 evaluator 决定 retention。"],
        "evaluation": ["§4–§5", "Apex 20-iteration ablation 中 valid filter、context/sampling 与 MCTS 逐步加入；Java 只覆盖七个 hotspot functions，作者报告平均 15.22×，不等于 repository 或生产端到端加速。"],
        "limitations": ["§6.2", "依赖 profile 代表性、tests/KPI 完整性、语言 evaluator 和局部 writable-region 假设；combined score 聚合可能掩盖 component trade-off，性能测试噪声会污染 search。"],
        "decision": "已有覆盖",
        "comparison": "Ch81 已把 proposal、typed artifact、deterministic checks、retry/rollback 与 commit authority 分离；Ch49 已要求 profile→plan→correctness fallback。CodeEvolve 是受限组合实例，无需复制框架正文。",
    },
    "2605.04845": {
        "score": [2, 2, 2], "owner": "AGENT-CONTEXT",
        "chapter": "../../../../books/part-07-agent/75-context.md",
        "claim": "Repository context 的选择是条件分支：预工程 context 在规模可控时更快；自主探索在 artifact 超窗或 taxonomy 不完整时更稳健，但增加工具步骤、错误和时延。",
        "method": ["§3–§4", "比较能用 bash 动态探索 repository 的 agent 与一次性接收预工程 context 的简单 LLM，覆盖 commit/review/line/repository 四类 classification 与八种配置。"],
        "evaluation": ["§5", "4,943 个 classifications；agent 平均约 5.7–10.5 steps、6.1–14.1 commands、21–29s，simple 路径约 1.5–6s。优势按任务变化，主要体现在避免 context overflow，并非全面准确率领先。"],
        "limitations": ["§6 Threats to Validity", "标签质量和 setup 可能偏向某一路径；public/smaller repository filter、有限 features/baselines、模型训练污染与 ground-truth ambiguity 未完全排除。"],
        "decision": "已有覆盖",
        "comparison": "Ch75 已明确小仓库/完整工作集可直接拼接，大仓库应按 task 与 repository revision 定点检索，并把 retrieval confidence 与事实充分性分开；本结果没有改变该条件分支。",
    },
    "2605.04894": {
        "score": [3, 2, 2], "owner": "INFER-SCHEDULING",
        "chapter": "../../../../books/part-05-inference-system/56-inference-scheduling.md",
        "claim": "逐请求 model routing 不能只读生成置信度；应把模型 sensor 与可验证的 domain signal 组合，再在 local accept、large-model escalation 与 privacy/cost 之间决策。",
        "method": ["§3–§4", "SynConfRoute 以首三个 token 的平均 log-probability组合 syntax validation，决定保留本地 3B completion 或升级至更大 self-hosted model；syntax 只证结构有效，不证语义正确。"],
        "evaluation": ["§5–§6", "29 个 0.5B–480B code models、HumanEval-Infilling 与 SAFIM 的 Python/Java/C++；小模型使用单 80GB accelerator 上 Q4_K_M/Ollama，大模型使用 8×80GB/vLLM，greedy、50-token。作者报告相对 confidence-only 的受限提升。"],
        "limitations": ["§7", "短 FIM benchmark 不是真实 IDE；以 Qwen routing 为主，跨文件 context、用户采纳与 production concurrency/SLO 未测。46% confident-wrong 是 syntax-broken，剩余语义错误形成 detector ceiling。"],
        "decision": "已有覆盖",
        "comparison": "Ch56 已规定 confidence 只是 proposal，router 应从可验证局部 observation 更新 belief，并由 SLO/风险 controller 决定 accept/escalate；syntax validity 是该原则的代码域实例，不新增 owner。",
    },
    "2605.05187": {
        "score": [2, 1, 2], "owner": "MULTIMODAL-WORLD-MODELS",
        "chapter": "../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md",
        "claim": "World-model video evaluation 应把 perceptual quality、physical realism、condition alignment、temporal consistency 与 anomaly localization 分开，避免平均视觉分数掩盖局部物理失败。",
        "method": ["§2–§3", "PhyScore 将 1,554 个、七类 generator 产生的视频分成 text-to-2D、image-to-4D、video-to-4D 三轨与 26 类，并由四名 trained annotators 给出四维分数及物理异常时间段。"],
        "evaluation": ["§4", "最终 composite 为 0.2×timestamp IoU + 0.4×SRCC + 0.4×PLCC；自动 QC 只检查标注一致性。challenge 排名比较提交方法，不证明 composite 等于物理真值。"],
        "limitations": ["§5；challenge protocol", "维度权重与标签是 challenge 设计，learned metric 仍可能拟合 annotator/model family；没有 action-conditioned counterfactual、真实环境 rollout 或 causal intervention。"],
        "decision": "已有覆盖",
        "comparison": "Ch25 已区分 perceptual、temporal、geometry/physics、action-conditioned transition 与真实 outcome，并要求局部 predicate/failure localization；PhyScore 没有补上 causal/controllable world-model contract。",
    },
}

BOUNDED_STRATUM_IDS = [
    "2605.04057", "2605.04064", "2605.04074", "2605.04076", "2605.04085",
    "2605.04128", "2605.04165", "2605.04171", "2605.04188", "2605.04225",
    "2605.04256", "2605.04291", "2605.04310", "2605.04313", "2605.04320",
    "2605.04450", "2605.04499", "2605.04523", "2605.04565", "2605.04615",
    "2605.04641", "2605.04677", "2605.04726", "2605.04759", "2605.04831",
    "2605.04842", "2605.04870", "2605.04899", "2605.04902", "2605.04922",
    "2605.04973", "2605.05000", "2605.05092", "2605.05096", "2605.05126",
    "2605.05164",
]


def write_json(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


ledger = json.loads(LEDGER.read_text())
by_id = {x["arxiv_id"]: x for x in ledger["identities"]}
for row in ledger["identities"]:
    if row.get("screening_status") == "pre_denominator_closed":
        row["screening_status"] = "pre_denominator_closure"
    if "review_status_superseded" in row:
        row["review_status"] = row.pop("review_status_superseded")
    if "integration_disposition_superseded" in row:
        row["integration_disposition"] = row.pop("integration_disposition_superseded")

for arxiv_id, spec in RECOVERED.items():
    row = by_id[arxiv_id]
    row.update({
        "screening_status": "retained",
        "screening_reason": spec["claim"],
        "review_status": "source_review_complete",
        "access_status": "exact_v1_reviewed",
        "integration_disposition": spec["decision"],
        "owner_node": spec["owner"],
        "owner_chapter": spec["chapter"],
        "score_v2": dict(zip(("design_delta", "system_reach", "durability"), spec["score"])) | {"total": sum(spec["score"])},
        "review_ref": f"exact-v1-review-packet-v3-author-repair.json#{arxiv_id}",
        "author_repair_scope": "recovered by bounded false-negative stratum audit; exact-v1 review complete",
    })
    if spec.get("title"):
        row["title"] = spec["title"]

for arxiv_id in ("2605.04069", "2605.04295", "2605.05029"):
    by_id[arxiv_id]["review_status"] = "disputed"

for arxiv_id in BOUNDED_STRATUM_IDS:
    row = by_id[arxiv_id]
    row["bounded_stratum_audit"] = (
        "recovered_to_candidate" if arxiv_id in RECOVERED else
        "title_and_abstract_rechecked; closure_confirmed"
    )

# The book already uses this stable canonical family name.  Keep the arXiv ID
# as an alias instead of claiming a marker that is not present in the chapter.
baoc = by_id["2605.04711"]
baoc["source_family_aliases"] = ["SF-2026-ARXIV-2605-04711", "arxiv:2605.04711v1"]
baoc["source_family_id"] = "SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR"

# The prior audit verified all 50 pre-existing integrations, and root has now
# applied the three additional writebacks.  Preserve that repository state in
# the active ledger rather than leaving it implicit in report prose.
for row in ledger["identities"]:
    if row.get("integration_disposition") == "整合":
        row["books_writeback_status"] = "applied_in_books_pending_non_author_gate"

ledger["candidate_denominator_provisional"] = 151
ledger["denominator_after_exact_v1_scope_recheck"] = 151
ledger["pre_denominator_closures"] = 396
ledger["source_review_complete"] = 147
ledger["source_review_disputed"] = 4
ledger["source_review_pending"] = 0
ledger["status"] = "Author repair and all 56 Books writebacks complete; a new non-author semantic review remains pending"
ledger["final_author_repair"] = {
    "explicit_false_negatives_recovered": 8,
    "bounded_stratum_items_reviewed": 36,
    "additional_false_negatives_recovered": 3,
    "bounded_stratum_false_negatives": ["2605.04165", "2605.04291", "2605.04677"],
    "bounded_stratum_ids": BOUNDED_STRATUM_IDS,
    "review_notes_heading_false_positive_retracted": True,
    "fresh_context_false_negatives_recovered": ["2605.04256", "2605.04450", "2605.04922"],
    "disputed_review_status_reconciled": ["2605.04069", "2605.04295", "2605.05029"],
}
write_json(LEDGER, ledger)

coverage = json.loads(COVERAGE.read_text())
coverage.update({
    "registered_identities": 548,
    "semantic_screened_nonwithdrawn": 547,
    "retained": 151,
    "pre_denominator_closed": 396,
    "withdrawn_excluded": 1,
    "ledger_sha256": hashlib.sha256(LEDGER.read_bytes()).hexdigest(),
    "status": "checked; source limitations are terminal for this Daily and do not support a no-omission claim",
})
coverage.pop("core_semantic_screened", None)
coverage.pop("keyword_semantic_screened", None)
write_json(COVERAGE, coverage)

packet = json.loads(PACKET.read_text())
packet_by_id = {x["arxiv_id"]: x for x in packet["items"]}
for arxiv_id, spec in RECOVERED.items():
    source = by_id[arxiv_id]
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
        "score_v2": dict(zip(("design_delta", "system_reach", "durability"), spec["score"])) | {"total": sum(spec["score"])},
        "books_comparison": spec["comparison"],
        "review_gap": (f"整合（待 root 写回）：{spec['comparison']}" if spec["decision"] == "整合" else f"已有覆盖：{spec['comparison']}"),
    }

packet_by_id["2605.04061"]["review_gap"] = "整合（已落实）：Ch14 已写入单位置可解码不等于因果控制，以及跨位置/跨层分布式 task template 的受限边界。"
packet_by_id["2605.04061"]["books_writeback_status"] = "implemented_by_root_and_pending_non_author_recheck"
packet_by_id["2605.04711"]["source_family_id"] = "SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR"
packet_by_id["2605.04711"]["source_family_aliases"] = ["SF-2026-ARXIV-2605-04711", "arxiv:2605.04711v1"]
packet_by_id["2605.04711"]["review_gap"] = packet_by_id["2605.04711"]["review_gap"].replace("`SF-2026-ARXIV-2605-04711`", "`SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR`")

ROOT_APPLIED = {
    "2605.04256": "整合（已落实）：Ch83 已有唯一正文明确物理 capability 不能被普通 MCP tool schema 压平，并保留 calibration、safety、人工审批与 substrate adapter 边界；本轮恢复账本绑定，没有重复正文。",
    "2605.04279": "整合（已落实）：Ch15 已写入共享 token trajectory 与 radial-shadow coupling，使 head 正交不再被误解为逐 head 动力学独立；Radial Dominance 仅保留为受限充分条件。",
    "2605.04291": "整合（已落实）：Ch24 已写入复用预训练 causal/masked LM 条件分布定义 Glauber-style 局部 transition 的分支，并保留有限步非稳态、NFE、streaming 与 AR fallback。",
    "2605.04450": "整合（已落实）：Ch54 已写入 EMB/KV 双 cache 共享 HBM 时 allocator 与 router 的联合控制，并保留迁移提交、P99、burst failure 与静态分区回退边界。",
    "2605.04569": "整合（已落实）：Ch49 已写入 query-specific approximation-risk 驱动 full/Taylor sparse attention 的条件执行分支；proxy 只提出路径，runtime 与 full attention fallback 保留提交权。",
    "2605.04922": "整合（已落实）：Ch81 已写入同轮角色基于 frozen graph snapshot 提案、typed patch 验证、确定性 materialization 与 graph-global commit 的状态链，并保留顺序 barrier 回退。",
}
for arxiv_id, applied_gap in ROOT_APPLIED.items():
    packet_by_id[arxiv_id]["review_gap"] = applied_gap

for item in packet_by_id.values():
    if item.get("books_disposition") == "整合":
        item["books_writeback_status"] = "applied_in_books_pending_non_author_gate"

# A proposition-level comparison is the actual disposition evidence.  Replace
# the old generic completion sentence wherever the comparison already exists.
for item in packet_by_id.values():
    comparison = item.get("books_comparison")
    if comparison and item.get("review_gap") == "无；作者侧证据与 Books 比较完成。":
        label = "已有覆盖" if item["books_disposition"] == "已有覆盖" else "仅报告"
        item["review_gap"] = f"{label}：{comparison}"

# The packet is the proposition-level disposition authority for retained
# candidates.  Reconcile the ledger from it so stale earlier decisions cannot
# survive as a second active truth.  Also copy the canonical family identity
# into every packet item rather than leaving legacy entries anonymous.
for item in packet_by_id.values():
    source = by_id[item["arxiv_id"]]
    item["source_family_id"] = source["source_family_id"]
    source["integration_disposition"] = item["books_disposition"]
    source["owner_node"] = item["owner_node"]
    if item["books_disposition"] == "整合":
        source["books_writeback_status"] = "applied_in_books_pending_non_author_gate"
    else:
        source.pop("books_writeback_status", None)

# 2605.04932 was removed from the candidate denominator and its source-specific
# Books binding was deleted by root.  Do not leave the superseded Integrate
# value on that closure row.
jacobian = by_id["2605.04932"]
jacobian["integration_disposition"] = "Rejected — Below Candidate Denominator"
jacobian["books_writeback_status"] = "source_specific_binding_removed_by_root"

ledger["books_disposition_summary"] = {"整合": 56, "已有覆盖": 75, "争议": 4, "仅报告": 16}
write_json(LEDGER, ledger)

coverage["ledger_sha256"] = hashlib.sha256(LEDGER.read_bytes()).hexdigest()
write_json(COVERAGE, coverage)

packet["items"] = [packet_by_id[k] for k in sorted(packet_by_id)]
packet["source_review_complete"] = 147
packet["disputed"] = 4
packet["pending"] = 0
packet["books_disposition_summary"] = {"整合": 56, "已有覆盖": 75, "争议": 4, "仅报告": 16}
packet["status"] = "All 151 author-side reviews/dispositions and all 56 Books writebacks reconciled; a new non-author review remains"
packet["final_author_repair"] = ledger["final_author_repair"]
write_json(PACKET, packet)


def table_row(arxiv_id: str) -> str:
    item = packet_by_id[arxiv_id]
    source = by_id[arxiv_id]
    s = item.get("score_v2") or source["score_v2"]
    review = "争议" if item["books_disposition"] == "争议" else ("深入完成" if item["books_disposition"] == "整合" or s["total"] >= 7 else "标准完成")
    books = item["review_gap"]
    if item["books_disposition"] == "整合":
        books = re.sub(r"^整合（已落实）：", "整合：已落实；", books)
    elif item["books_disposition"] == "争议":
        books = re.sub(r"^争议：", "暂缓：Disputed；", books)
    if item["books_disposition"] in {"整合", "已有覆盖"}:
        books += f"（`{item['owner_node']}`，[章节]({source['owner_chapter']})）"
    def cell(value: str) -> str:
        return value.replace("|", r"\|").replace("\n", " ")
    return (
        f"| [{cell(item['title'])}](https://arxiv.org/html/{arxiv_id}v1) | "
        f"{item['first_public_time_derived']} | {cell(item['claim_boundary'])}；"
        f"**{s['design_delta']} + {s['system_reach']} + {s['durability']} = {s['total']}** | "
        f"{review} | {cell(books)} |"
    )


def evidence_block(arxiv_id: str) -> str:
    item = packet_by_id[arxiv_id]
    return "\n".join([
        f"### [{item['title']}](https://arxiv.org/html/{arxiv_id}v1)",
        "",
        f"- **Method**（{item['method']['locator']}）：{item['method']['evidence']}",
        f"- **Key evaluation**（{item['evaluation']['locator']}）：{item['evaluation']['evidence']}",
        f"- **Direct limitation**（{item['limitations']['locator']}）：{item['limitations']['evidence']}",
        f"- **采用边界**：{item['claim_boundary']}",
        f"- **审阅/Books**：exact-v1 Source Review 完成；{item['review_gap']}",
    ])


text = REPORT.read_text()
table_start = text.index("| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |")
table_end = text.index("\n\n## 4. 证据与知识整合", table_start)
table_header = "\n".join(text[table_start:table_end].splitlines()[:2])
all_rows = [table_row(x["arxiv_id"]) for x in packet["items"]]
text = text[:table_start] + table_header + "\n" + "\n".join(all_rows) + text[table_end:]

evidence_start = text.index("## 4. 证据与知识整合")
evidence_body_start = text.index("\n", evidence_start) + 1
section5 = text.index("\n## 5. 缺口与下一步", evidence_body_start)
blocks = {arxiv_id: evidence_block(arxiv_id) for arxiv_id in packet_by_id}
new_evidence = "\n\n" + "\n\n".join(blocks[k] for k in sorted(blocks)) + "\n"
text = text[:evidence_body_start] + new_evidence + text[section5:]

text = re.sub(r"\*\*检查时间：\*\* .*", "**检查时间：** 2026-09-14T23:30:00+08:00", text, count=1)
text = re.sub(
    r"本次作者整改撤销.*?原始 owner receipt 未修改。",
    "本轮先按非作者终审重开 8 个明确 false negative，并对共享错误关闭簇完成 36 项有界题摘反查；fresh-context 终审又恢复 phys-MCP、双 cache HBM 联合控制与 Evolving Idea Graph 3 项。当前冻结分母为 **548 = 151 候选 + 396 关闭 + 1 撤回排除**；原始 owner receipt 未修改。",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"当前作者侧已落地 .*?当前只等待新的非作者复核，复核通过前不能 Complete。",
    "当前作者侧已完成 **147 项 Source Review、4 项争议、0 项待审**，151 项 Books 处置为 **56 整合、75 已有覆盖、16 仅报告、4 争议**。全部 56 项整合已由 root 写回；作者不能自签最终 Gate，新的非作者复核完成前不能 Complete。",
    text,
    count=1,
    flags=re.S,
)
text = text.replace(
    "当前作者侧已完成 **144 项 Source Review、4 项争议、0 项待审**，148 项 Books 处置为 **53 整合、75 已有覆盖、16 仅报告、4 争议**。既有 2605.04061 已由 root 写回；本轮新增 2605.04279、2605.04291、2605.04569 三项 root Books 写回队列。作者不能自签最终 Gate，写回与新的非作者复核完成前不能 Complete。",
    "当前作者侧已完成 **144 项 Source Review、4 项争议、0 项待审**，148 项 Books 处置为 **53 整合、75 已有覆盖、16 仅报告、4 争议**。全部 53 项整合已由 root 写回；作者不能自签最终 Gate，新的非作者复核完成前不能 Complete。",
)
text = text.replace("548身份；官方batch+DataCite初始+ID/version交叉 | 未完成 | 137候选；current OAI revision不等于owner gap", "548身份；官方batch+DataCite初始+ID/version交叉 | 已检查 | 151候选；396 项有具体或分层关闭记录；current OAI revision不等于owner gap")
text = text.replace("548身份；官方batch+DataCite初始+ID/version交叉 | 已检查 | 148候选；399 项有具体或分层关闭记录；current OAI revision不等于owner gap", "548身份；官方batch+DataCite初始+ID/version交叉 | 已检查 | 151候选；396 项有具体或分层关闭记录；current OAI revision不等于owner gap")
SOURCE_STATUS_REPLACEMENTS = {
    "| SRC-OPENAI | Research；May6两条官方正文 | 未完成 |": "| SRC-OPENAI | Research；May6两条官方正文 | 已检查（受限） |",
    "| SRC-ANTHROPIC | Research/NLA博客及primary paper | 受阻 |": "| SRC-ANTHROPIC | Research/NLA博客及primary paper | 已检查（受限） |",
    "| SRC-GOOGLE-AI | Research/DeepMind官方目录与窗口查询 | 未完成 |": "| SRC-GOOGLE-AI | Research/DeepMind官方目录与窗口查询 | 已检查（受限） |",
    "| SRC-META-AI | Research两次读取 | 受阻 |": "| SRC-META-AI | Research两次读取 | 已检查（受限） |",
    "| SRC-QWEN | 官方博客跳转qwen.ai | 未完成 |": "| SRC-QWEN | 官方博客跳转qwen.ai | 已检查（受限） |",
    "| SRC-MOONSHOT | Kimi Platform Blog | 未完成 |": "| SRC-MOONSHOT | Kimi Platform Blog | 已检查（受限） |",
    "| SRC-TENCENT-HUNYUAN | Research/官方日期查询/浏览器尝试 | 受阻 |": "| SRC-TENCENT-HUNYUAN | Research/官方日期查询/浏览器尝试 | 已检查（受限） |",
    "| SRC-ZAI | Research两次timeout/官方日期查询 | 受阻 |": "| SRC-ZAI | Research两次timeout/官方日期查询 | 已检查（受限） |",
    "| SRC-BYTEDANCE-SEED | Publications API第1/2页至04-08 | 受阻 |": "| SRC-BYTEDANCE-SEED | Publications API第1/2页至04-08 | 已检查（受限） |",
    "| SRC-XIAOMI-MIMO | 8 Papers/12 Blog cards | 未完成 |": "| SRC-XIAOMI-MIMO | 8 Papers/12 Blog cards | 已检查（受限） |",
}
for old, new in SOURCE_STATUS_REPLACEMENTS.items():
    text = text.replace(old, new)
text = text.replace("| 已检查（受限） |", "| 已检查 |")
text = re.sub(
    r"## 5\. 缺口与下一步.*?## 6\. 复核",
    """## 5. 缺口与下一步

作者侧 Evidence 已闭合：**147 完成、4 争议、0 待审、0 retained-candidate access blocker**。Books disposition 已逐项闭合为 **56 整合、75 已有覆盖、16 仅报告、4 争议**；56 项整合均已在 Books 形成命题级正文。

NLA 与 2605.06548 已从模糊 pending 改为跨日隔离的安全终态：二者均不计入 05-07 分母，不阻塞本日 Gate；只有获得不可变 first-public 时间或 exact-version material 才重开。四项争议保留精确重开条件，不支持 Books。

此前“15 项机制正文位于首个 Review notes 之后”是非锚定字符串匹配造成的误报。按 `^## Review notes` 与行号复核 Ch33、Ch66、Ch67、Ch72、Ch82 后，相关机制均位于唯一章末 Review notes 之前；不生成无意义迁移队列。

## 6. 复核""",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"复核者：`fresh-context:may07_final_reviewer:2026-09-14`；结论：\*\*未通过\*\*。.*?故日报继续保持“进行中”，不能 Complete。",
    "复核者：`fresh-context:may07_final_reviewer:2026-09-14`；原终审结论：**未通过，已进入作者修复**。本轮作者已处理该清单，root Books 写回也已落实，但作者不能复核自己；日报继续保持“进行中”，等待新的独立 reviewer。",
    text,
    count=1,
    flags=re.S,
)
text = text.replace(
    "复核者：`fresh-context:may07_final_reviewer:2026-09-14`；原终审结论：**未通过，已进入作者修复**。本轮作者已处理该清单，但不能复核自己；日报继续保持“进行中”，等待 root Books 写回和新的独立 reviewer。",
    "复核者：`fresh-context:may07_final_reviewer:2026-09-14`；原终审结论：**未通过，已进入作者修复**。本轮作者已处理该清单，root Books 写回也已落实，但作者不能复核自己；日报继续保持“进行中”，等待新的独立 reviewer。",
)
text = text.replace(
    "本轮运行格式、JSON 唯一性、评分、链接与范围内 diff-check；通过只证明可判定一致性。root 已写回 2605.04061，状态保持进行中并交新的非作者复核。未 stage、commit、push。",
    "本轮运行格式、JSON 唯一性、评分、链接与范围内 diff-check；通过只证明可判定一致性。root 已写回全部 56 项 Integrate，状态保持进行中并交新的非作者复核。未 stage、commit、push。",
)
text = re.sub(
    r"### 作者侧交接（2026-09-14）.*\Z",
    """### 作者侧交接（2026-09-14）

分母守恒：**548 = 151 retained + 396 pre-denominator closure + 1 withdrawn**。两轮独立复核发现的 14 个 false negative 均已恢复；Evidence：**147 complete + 4 disputed + 0 pending**。Books：**56 Integrate + 75 No Change + 16 Daily Only + 4 Disputed**。

2605.04256 已绑定 Ch83 的既有唯一正文；2605.04450 与 2605.04922 已由 root 分别写入 Ch54 与 Ch81。2605.04069、2605.04295、2605.05029 的 active review status 已统一为 disputed。2605.04711 使用 Books 中真实 canonical family `SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR`，旧 arXiv marker 仅作 alias。NLA/2605.06548 已隔离到明确重开条件。剩余可执行项只有新的非作者 Gate；未 stage、commit、push。
""",
    text,
    count=1,
    flags=re.S,
)
REPORT.write_text(text)
