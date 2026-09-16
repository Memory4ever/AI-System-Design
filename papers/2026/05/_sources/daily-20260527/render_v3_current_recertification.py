#!/usr/bin/env python3
"""Render the current-contract 2026-05-27 author packet.

This intentionally treats the old 633-item created-day report as migration
evidence only.  The owner set is the registered-category projection of the
official 2026-05-27 announcement interval.  Reused title/abstract and exact-v1
records remain traceable to their source artifacts; old completion labels are
not copied.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/27/README.md"
REPLAY = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903"
OWNER_RECEIPT = REPLAY / "20260526/arxiv-owner-receipt.json"
LEGACY_633 = REPLAY / "20260527/arxiv-owner-receipt.json"
DAY25 = ROOT / "papers/2026/05/_sources/daily-20260525"
DAY26 = ROOT / "papers/2026/05/_sources/daily-20260526"
CHECKED_AT = "2026-09-16T18:20:00+08:00"
PUBLIC_TIME = "2026-05-27T08:00:00+08:00"
WINDOW = "[2026-05-26T09:00:00+08:00,2026-05-27T09:00:00+08:00)"
MINIMAX_ID = "minimax:sparse-token-forgetting"
MINIMAX = {
    "arxiv_id": MINIMAX_ID,
    "source_family_id": "SF-2026-MINIMAX-SPARSE-TOKEN-FORGETTING",
    "title": "Why Can't the MiniMax LLM Say \"Ma Jiaqi\"? Internal Investigation of Sparse Token Forgetting",
    "url": "https://www.minimax.io/blog/sparse-token-forgetting",
    "public_owner_time": "2026-05-27T08:00:00+08:00",
    "json_ld_date_published": "2026-05-27T00:00:00Z",
    "owner_node": "TRAIN-SFT",
    "owner_path": "books/part-04-training-system/29-sft.md",
    "adopted_proposition": (
        "SFT 不只监控 task/domain coverage，还要监控 token-as-target coverage 与 pretrain→SFT `lm_head` drift；"
        "全词表重复数据可保底但可能浪费容量或损害会话能力，Korean 反例说明失败时需回退数据清洗、"
        "targeted synthesis、受控 replay 或 CPT。"
    ),
    "method_locator": "Hypothesis 1–2; Exploring Intermediate Metrics",
    "evaluation_locator": "Validation & Repair Experiments",
    "limitations_locator": "Korean non-fix and Other Directions Worth Exploring",
}


# These are the durable mechanisms, boundaries or counterevidence actually
# adopted after rereading the full abstracts.  They deliberately replace
# background/problem-setting sentences recovered from the older packets.
PROPOSITION_OVERRIDES = {
    "2605.24823": "把 Agent Manufacturing 操作化为由 foundation-model agents 承担开放目标解释、长程规划、工具/机器调用及人机协商的生产协调机制，并与封闭协议空间中的传统 multi-agent manufacturing 区分。",
    "2605.24914": "以可学习 prompt segmentation 生成多向量表示，再用 MaxSim 做细粒度匹配；训练目标直接约束在 correctness 前提下增加 cache hit，并以强化学习求解不可微组合优化。",
    "2605.24941": "长期记忆中的成本、耐心或风险偏好即使与当前任务无关，也会通过隐式 steering 与关键词注意力重分配改变 tool arguments；相关性提示和 memory filter 只能缓解，不能消除这种 memory-induced tool drift。",
    "2605.25052": "先构造能暴露真实中间计算的任务并生成 step/CoT 级 ground-truth faithfulness label，再审计现有指标；多数指标接近随机、对长 CoT 退化且跨设置不迁移，因此自动分数不能未经有效性验收就充当 faithfulness 证据。",
    "2605.25077": "用 camera-invariant Normalized World Trajectory 分离对象运动与相机位移，以 Spatial-Pathway LoRA 注入对象控制，并用 trajectory-anchored persistent state 在对象离屏后保留更新位置。",
    "2605.25092": "以 BM25 top-k margin 驱动无需重训的 cascade，逐 query 决定是否运行 dense channel/何种 fusion，并用 time-partitioned index 把增长中的长期记忆检索成本与 corpus size 解耦。",
    "2605.25188": "先保持 agents 独立生成，再把响应解析为候选簇，以 reliability、confidence、parse quality、support pattern 与独立性修正形成 belief distribution；coordinator 只接收 policy 允许的结构化证据而非原始推理串。",
    "2605.25233": "把自然语言任务编译为带显式 I/O contract 与 verifier 的 agent DAG；construction-time gate 定点重生失败 artifact，execution-time gate 再以 local/upstream/structural attribution 选择 retry、局部重放或重分解。",
    "2605.25244": "正确 reasoning trajectory 的 confidence 往往沿程上升、错误轨迹则停滞或下降；CDG voting 把这种轨迹增益作为 answer-selection sensor，但它仍需与模型、任务和采样合同共同校准。",
    "2605.25247": "先建立 LLM inference ecosystem 的 reference architecture，再用 cache-aware discrete-event simulator 联合表示 KV/prefix cache、性能、成本与可持续性，并以真实 traces 校准后用于比较配置。",
    "2605.25252": "在受控 false-positive/false-negative verifier noise 与 rollout 数量下，额外 compute 呈锐减回报且不能消除监督差距；false negative 的损害更快，说明 verifier quality 与训练 compute 不能互换。",
    "2605.25284": "模型在显式判断时常能识别歧义，却在普通 QA 中仍直接作答；检索上下文提高 answerability 的同时进一步降低澄清概率，因此 ambiguity recognition 与 ask/answer 行为必须分开评估。",
    "2605.25313": "用 joint system-environment density-matrix latent 与 unitary predictor 在 blind rollout 中保持表示的不确定性谱；同时证明 action sensitivity 依赖 counterfactual target，而不能由 teacher-forced context capacity 推出。",
    "2605.25375": "以动态 job priority、bandwidth-aware cross-region pathfinder 与按电价分配 GPU 的 allocator 联合控制 geo-distributed pipeline training，避免 HoL blocking 并把 JCT、链路约束和电力成本纳入同一计划。",
    "2605.25389": "把长程 tool attack 建模为带动态 attack memory 的强化学习过程，并用 Attack-Flow GRPO 从 terminal outcome 向中间干预分配 credit；它暴露的是 tool-output trust surface，不授权把攻击策略当通用能力。",
    "2605.25421": "用 latent channel 承载高带宽认知状态、用短文本承载关键可解释信号，并通过单 agent hybrid generation 与多 agent interactive co-training 学习多轮双向混合通信。",
    "2605.25422": "把 token/KV-cache communication medium 与 wireless bandwidth allocation 联合优化；没有一种 medium 在所有 compute/channel regime 都占优，media identity 与资源状态必须共同进入 E2E latency 决策。",
    "2605.25451": "把 multimodal encoder 与 generator 以 dependency-safe nested pipeline 嵌入 LLM pipeline，使二者 activation memory 为 O(1)，同时避免用降低计算利用率来换显存。",
    "2605.25475": "用 learnable indexer 预测 KV importance，同时把被逐出的 token 压入在线更新的 latent memory 并提供 residual readout，从而把 bounded KV residency 与不可逆遗忘分开。",
    "2605.25521": "沿 PQ centroids 而非 subvector dimension 做 SIMD vectorization，并重排 pipeline 提升 cache locality、消除冗余计算，使 CPU index construction 的数据移动与计算粒度共同受控。",
    "2605.25535": "以 session-level storage gate 学习 user-specific retention policy，选择性跳过短暂会话；理想个性化可改善有限预算下的保留，但准确 gating 仍是未解决边界。",
    "2605.25537": "Soft RTC 用部分去噪的 overlap state 与上一 action chunk 构造 action prior，让已提交前缀保持固定、后续 overlap 仍可编辑，从而在不引入昂贵部署 guidance 时降低动作跳变。",
    "2605.25547": "Action-VAE 从 policy proposal 周围生成多个低维 latent action candidates，再以 task-progress outcome predictor 选择动作；verifier 只拥有候选排序权，不能替代 controller commit。",
    "2605.25550": "以异步 pipeline 重叠 diffusion stages 的计算与 handoff，并结合轻量性能预测和 runtime feedback 动态重配各 stage instance ratio，以吸收 workload shift 与 stage imbalance。",
    "2605.25621": "用 multimodal evidence-guided long/short-term memory 在固定预算内压缩流式音视频历史，再由 hidden-state trigger 决定何时主动响应，避免把 silence token 或外部 router 当作唯一时机 owner。",
    "2605.25624": "由 Generator 构造 initial/golden environment state、独立 Discriminator 编写 reward function、orchestrator 迭代执行并以多数票和 rollout 终检，使 task、environment 与 deterministic reward 成为同一可验证 tuple。",
    "2605.25641": "把 factual correction 写成带来源的 nugget，并让生产 RAG 充当 test harness：对触发 query 与 paraphrases 反复 probe、读取失败 trace、修订直到可发现；事实正确性与检索可发现性仍是两个 Gate。",
    "2605.25653": "以 25 个 typed primitives 和 Physical Impact Tier 组成 actuation-boundary zero-trust policy；模型只提议机器人参数，policy 在真实物理 effect 前执行确定性约束。",
    "2605.25655": "把 VLIW-SIMD operator、density-driven graph fusion 与 Prefill-Buffer-Decode bounded-buffer pipeline 组合为硬件感知执行计划，使数据 locality、通信层级和 hybrid parallelism 共同受控。",
    "2605.25674": "以一次全参数 Hessian-vector product 配合 Hutchinson probes 无偏估计每层 Hessian trace；weight sharing 必须先装配 layer Hessian 再二次求导，并用临界 probe 数平衡随机投影与 mini-batch 方差。",
    "2605.25682": "实机 profiling 表明 embedded distributed inference 的瓶颈还包括 CPU-GPU staging；运行时应依据离线 profile 在 local 与 compressed distributed execution 间选择，而不是默认全 tensor exchange。",
    "2605.25707": "用九类可配置的非对抗环境 corruption 分阶段压力测试 computer-use agents，并以 action generator 加独立 onlooker 做 grounding、行为摘要与环境复核；轻微扰动也会造成显著执行退化。",
    "2605.25716": "以 numerically stable feature scrambling 与 token permutation 构造 Scrambled Distributed Attention，把 attention execution 与明文数据位置解耦；该协议仍须对 inversion、collusion 与数值误差单独验收。",
    "2605.25798": "以跨 diffusion step 的 Cached Token Reuse 和复用 attention sparsity mask 的 Softmax Thresholding 形成混合 dense/sparse workload，再用 hash-based bank distribution 在同一 accelerator 数据流中承载稀疏执行。",
    "2605.25820": "用 Visual Redundancy Index 衡量同一步并行提交 tokens 的视觉 grounding 重叠，再让 VRCD 优先提交视觉互补位置；attention overlap 只是 selection sensor，不是语义正确性证明。",
    "2605.25874": "以 video quality、setting/interaction adherence、consistency 与 physics compliance 五轴组成 multi-turn world-model benchmark，并统一 text、6-DoF pose 与 discrete action 接口、用人评校准自动子指标。",
    "2605.25893": "把 diffusion trajectory 中 hidden state 反复贴近 probe decision boundary 的次数定义为 safety hesitation，以此预测轻量 probe failure 并只在阈值越界时路由重 probe。",
    "2605.25966": "factorial evidence 否定 FP16/INT8/INT6 需要不同 warmdown 的假设，却发现 INT4 在约 50M 参数以上出现明确 schedule boundary；bit-width、model size 与 schedule 必须共同组成训练 identity。",
    "2605.25988": "训练期 checker 的输出分布而非 held-out accuracy 决定是否提供可学习梯度：neutral-heavy log-prob scoring 会 signal collapse，过强 checker 又会诱发短答案、避检索与语言坍缩的 reward hacking。",
    "2605.26029": "在可干预 synthetic SCM laboratory 中把 held-out prediction 与 recovered graph/equations 的机制忠实度分开计分；高预测准确率可与低结构恢复并存，premature stopping 需要 consistency verification。",
    "2605.26046": "multi-objective textual-gradient optimization 存在两个可分 failure：联合反馈会稀释 optimization-time task focus，合并单目标优化后的 instructions 又会产生 inference-time interference。",
    "2605.26079": "以 agentic audit 重放 task specification、environment dependency 与 grader logic；发现的问题经专家/上游修复验证后会改变分数和模型排序，因此 benchmark task 本身必须先通过 admission。",
    "2605.26110": "以 plugin registration 将 continual-tuning algorithm state 与 MLLM backbone/runtime 解耦，使新策略无需改写底座即可在同一 scalable pipeline 中复现和公平比较。",
    "2605.26112": "把 context governance、memory、skill routing、orchestration、verification 与 governance 组成可版本化 agent harness，并把 harness-level trajectory、memory hygiene、communication fidelity 与 safe evolution 纳入评价对象。",
    "2605.26114": "把完整 mobile environment state 表示为可配置、fork 和比较的 structured JSON，并以同一 deterministic state judge 同时提供 evaluation verdict 与 dense RL reward，从而支持高并发可验证 rollout。",
}


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def packet_items(day: Path, name: str):
    value = load(day / name)
    return value if isinstance(value, list) else value.get("items", [])


NO_CHANGE_AUDIT = {
    "2605.24823": ("AGENT-PLATFORM", "books/part-07-agent/84-agent-platform.md", "Agent 改变了平台的控制对象"),
    "2605.24892": ("MULTIMODAL-WORLD-MODELS", "books/part-03-multimodal-world-models/25-multimodal-world-models.md", "从单尺度预测到 Abstraction × Timescale Hierarchy"),
    "2605.24930": ("MODEL-LONG-CONTEXT", "books/part-02-model/22-long-context.md", "Selector 可以进入 Forward，但必须显式承担语义责任"),
    "2605.25052": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Scorer 不是绝对真相"),
    "2605.25073": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "生命周期威胁"),
    "2605.25133": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Confidence 最终服务于 Risk–Coverage Decision"),
    "2605.25160": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Benchmark 生成器也会塑造被评估的任务人口"),
    "2605.25188": ("AGENT-MULTI-AGENT", "books/part-07-agent/82-multi-agent.md", "扩展 Agent 数量之前，先测量 Coordination Tax"),
    "2605.25233": ("AGENT-WORKFLOW", "books/part-07-agent/81-workflow.md", "从一次性脚本到平台拥有的可编辑 DAG"),
    "2605.25244": ("MODEL-SAMPLING", "books/part-02-model/20-sampling.md", "Selector 也要先证明“正确性信号可读”"),
    "2605.25247": ("INFER-SCHEDULING", "books/part-05-inference-system/56-inference-scheduling.md", "Task-DAG Simulator 只能校准 Capacity Plan，不能承诺线上 SLO"),
    "2605.25284": ("AGENT-PLANNING", "books/part-07-agent/79-planning.md", "先校准不确定性，再决定行动、询问或探索"),
    "2605.25292": ("PLATFORM-GPU-SCHEDULER", "books/part-06-ai-infrastructure/63-gpu-scheduler.md", "Power Budget 是分层资源契约"),
    "2605.25313": ("MULTIMODAL-WORLD-MODELS", "books/part-03-multimodal-world-models/25-multimodal-world-models.md", "Latent Geometry 不等于 Planning Cost"),
    "2605.25338": ("AGENT-PLATFORM", "books/part-07-agent/84-agent-platform.md", "Harness、Protocol 与 Credit 都是 Platform-owned Artifact"),
    "2605.25376": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Agent 授权必须沿 Delegation Chain 单调收窄"),
    "2605.25389": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "外部化 Attack/Defense Memory 需要 Provenance Gate"),
    "2605.25421": ("AGENT-MULTI-AGENT", "books/part-07-agent/82-multi-agent.md", "Latent Communication 只能压缩 Payload，不能隐藏 Identity"),
    "2605.25521": ("AGENT-RAG", "books/part-07-agent/76-rag.md", "多向量检索的数据面要避免搬运高精度向量"),
    "2605.25535": ("AGENT-MEMORY", "books/part-07-agent/77-memory.md", "个性化更新与事实可靠性是两套策略"),
    "2605.25537": ("MULTIMODAL-EMBODIED-VLA", "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", "Action Chunk 是控制闭环的时间契约"),
    "2605.25547": ("MULTIMODAL-EMBODIED-VLA", "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", "Critical-phase Dreaming 只获得候选排序权"),
    "2605.25624": ("AGENT-PLATFORM", "books/part-07-agent/84-agent-platform.md", "Model 与 data-generating harness 是共同演进的配对 artifact"),
    "2605.25653": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Cyber-physical Safety 要验证持续的 Process Effect"),
    "2605.25655": ("INFER-SCHEDULING", "books/part-05-inference-system/56-inference-scheduling.md", "低带宽拓扑要联合预算 Hops、Bytes 与 Steps"),
    "2605.25682": ("INFER-SCHEDULING", "books/part-05-inference-system/56-inference-scheduling.md", "从逐配置压测到校准后的配置搜索"),
    "2605.25707": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Tool Robustness 要按 Failure Stage 注入"),
    "2605.25798": ("INFER-TENSORRT-LLM", "books/part-05-inference-system/49-tensorrt-llm.md", "Token-level 预算不能由三个独立近似器分别消费"),
    "2605.25874": ("MULTIMODAL-WORLD-MODELS", "books/part-03-multimodal-world-models/25-multimodal-world-models.md", "视觉逼真与三维一致性是两份不同证据"),
    "2605.26079": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "先验证 Benchmark 的 Reference Artifact，再比较 Agent"),
    "2605.26112": ("AGENT-PLATFORM", "books/part-07-agent/84-agent-platform.md", "本章要回答的问题"),
    "2605.26114": ("AGENT-PLATFORM", "books/part-07-agent/84-agent-platform.md", "Model 与 data-generating harness 是共同演进的配对 artifact"),
}


INTEGRATE_REPAIRS = {
    "2605.24914": {
        "owner_node": "INFER-KV-CACHE", "owner_path": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "anchor": "Prefix reuse",
        "delta": "在 exact token-prefix reuse 之外新增 semantic answer-cache 分支：learned segmentation 生成多向量，MaxSim 匹配细粒度意图；hit 只有在版本化 correctness gate 通过后才能复用结果。",
        "tradeoff": "提高语义命中率要付出 segmentation 训练、向量索引、MaxSim 与失效传播成本。", "failure": "prompt 分布或 segmenter 漂移会把表面相似请求错误合并，产生高危 false hit。", "fallback": "置信不足时回退 exact key/prefix match，或完整执行模型并重新校验 cache entry。",
    },
    "2605.24941": {
        "owner_node": "AGENT-TOOL-CALLING", "owner_path": "books/part-07-agent/78-tool-calling.md", "anchor": "模型输出只是 Proposal",
        "delta": "在 tool proposal 前增加 memory-to-field relevance gate：只有与当前 intent、参数 schema 和授权边界相关的 memory 才能影响参数，并保存 memory entry 到 tool field 的 lineage。",
        "tradeoff": "双路径 relevance 检查与对照 proposal 增加延迟，也可能压低有益个性化。", "failure": "关键词重叠和 latent steering 会让无关偏好绕过 prompt/filter 防御。", "fallback": "高风险字段使用 memory-masked proposal、typed default、澄清或人工确认。",
    },
    "2605.25077": {
        "owner_node": "MULTIMODAL-WORLD-MODELS", "owner_path": "books/part-03-multimodal-world-models/25-multimodal-world-models.md", "anchor": "Persistent world state",
        "delta": "把对象轨迹从 camera motion 中因子化为 world-coordinate proposal，并让 renderer/control adapter 与可持久化 object state 分权；离屏后重现必须读取已提交对象位置而非仅续写像素。",
        "tradeoff": "轨迹重投影、专用 adapter 与 state refresh 增加几何校准和版本成本。", "failure": "camera pose 漂移、遮挡或错误对象绑定会把持久状态写错并在长 rollout 中放大。", "fallback": "绑定失败时回退 camera-only navigation、短 horizon reactive generation 或显式 simulator/新观测重置。",
    },
    "2605.25092": {
        "owner_node": "AGENT-MEMORY", "owner_path": "books/part-07-agent/77-memory.md", "anchor": "Memory Read 是受约束检索",
        "delta": "把 BM25/dense/fusion 选择变成逐 query cascade state：先用 sparse margin 决定是否值得运行 dense channel，再让 time-partitioned index 承担增长语料的物理检索。",
        "tradeoff": "router 校准、分区索引与多路 fusion 增加状态、构建和观测成本。", "failure": "query-type 或 workload 漂移会使 skip decision 漏掉 dense 独有证据。", "fallback": "margin/分布越界时强制 dense+RRF，或回退经验证的 BM25/全量检索路径。",
    },
    "2605.25422": {
        "owner_node": "AGENT-MULTI-AGENT", "owner_path": "books/part-07-agent/82-multi-agent.md", "anchor": "Latent Communication 只能压缩 Payload，不能隐藏 Identity",
        "delta": "把 token text 与 KV-cache 视为不同 communication media，并与链路 bandwidth allocation 联合优化；medium decision 必须绑定 sender/receiver model、cache layout、channel state 与 E2E deadline。",
        "tradeoff": "联合求解和 telemetry 提高控制开销，KV 还引入版本耦合与不可解释性。", "failure": "compute/channel regime 变化会让原 medium 变慢或语义不兼容。", "fallback": "身份或预测失配时回退显式 typed text 与保守固定带宽，重新建立可验证 handoff。",
    },
    "2605.25451": {
        "owner_node": "TRAIN-PIPELINE-PARALLEL", "owner_path": "books/part-04-training-system/38-pipeline-parallel.md", "anchor": "Schedule Abstraction 要先证明依赖合法，再比较 Bubble",
        "delta": "为 MLLM training 增加 dependency-safe nested pipeline：encoder/generator 工作嵌入 LLM stage flow，使其 activation lifetime 受界，同时保留参数版本和 micro-batch dependency。",
        "tradeoff": "减少 activation memory 会增加嵌套 readiness、stage balance、边界通信与恢复复杂度。", "failure": "错误依赖或估时会覆盖 activation、形成新 bubble，甚至让 micro-batch 看到不一致参数版本。", "fallback": "校验失败时回退顺序 encoder→LLM→generator 或已验证 GPipe/1F1B schedule。",
    },
    "2605.25475": {
        "owner_node": "INFER-KV-CACHE", "owner_path": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "anchor": "从统一保留到 workload-aware eviction",
        "delta": "把 learned KV-importance index 与 compact online latent memory 分开：前者只提议保留，后者为已逐出 token 提供有损 residual readout，不能冒充 exact KV。",
        "tradeoff": "训练 indexer、更新 latent state 和额外 readout 会消耗计算并扩大 cache identity。", "failure": "importance miss 或 latent collision 会造成不可逆远程召回退化。", "fallback": "高风险/低置信时回退 FullKV、静态保留窗口、offload 或逐出后重算。",
    },
    "2605.25621": {
        "owner_node": "MULTIMODAL-REPRESENTATION", "owner_path": "books/part-03-multimodal-world-models/23-multimodal-representation.md", "anchor": "Streaming Multimodal Identity 不止是 Token Type",
        "delta": "在流式 audio/video identity 上增加固定预算的 evidence long/short memory 与独立 response-trigger state；memory 压缩只保存证据，trigger 只提议何时回复，runtime 保留 commit/cancel 权。",
        "tradeoff": "持续压缩与 hidden-state trigger 增加计算、时序对齐和阈值校准成本。", "failure": "压缩漏证、音视频乱序或 false trigger 会造成过早回答或关键时刻沉默。", "fallback": "越界时回退固定窗口、显式 turn-taking/外部 router 或离线完整上下文。",
    },
    "2605.25641": {
        "owner_node": "AGENT-RAG", "owner_path": "books/part-07-agent/76-rag.md", "anchor": "Retrieval Object 需要 Validity 与 Lifecycle",
        "delta": "把 factual correction 作为版本化 nugget，并用 production RAG 对触发 query 与 paraphrases 做 discoverability probe；rewrite loop 只能优化检索可达性，事实 validity 仍由原始证据 owner 验收。",
        "tradeoff": "反复 probe/rewrite 增加索引构建、模型调用与 lineage 管理成本。", "failure": "对少量 triggering queries 过拟合会改变纠错语义或在其他表述下继续漏检。", "fallback": "回退不可变 correction+原文 provenance、人工 curated entry、hybrid retrieval 与失败时 raw-source dereference。",
    },
    "2605.25674": {
        "owner_node": "PLATFORM-MONITORING", "owner_path": "books/part-06-ai-infrastructure/67-monitoring.md", "anchor": "Model-internal Sensor 必须从 Inference Hot Path 解耦",
        "delta": "把 per-layer Hessian trace 定义为训练健康 sensor：用一次全参数 HVP 和多个 Hutchinson probes 估计各层曲率，weight sharing 必须在二次求导前正确装配。",
        "tradeoff": "HVP、多个 probes 与 mini-batch 重采样增加训练监控开销。", "failure": "probe 方差、batch noise 或错误处理 shared weights 会产生系统偏置并伪造异常。", "fallback": "估计不稳时回退 loss/gradient norm、离线高精度曲率审计、增加 probes 或人工停机判断。",
    },
    "2605.25716": {
        "owner_node": "PLATFORM-SECURITY", "owner_path": "books/part-06-ai-infrastructure/72-security.md", "anchor": "暴露打乱后的 Activation 仍不是 Confidentiality 证明",
        "delta": "将 feature scrambling 与 token permutation 组成 distributed-attention privacy protocol；remote node 只能计算受限中间量，协议 identity 必须包含 permutation、numeric transform、participants 与 inversion audit。",
        "tradeoff": "打乱、通信和重组增加 latency、数值误差与 key/state 生命周期。", "failure": "节点串谋、已知输入、数值不稳定或侧信道可能恢复 plaintext/intermediate state。", "fallback": "威胁模型不满足时回退本地检索、拒绝跨机构执行，或使用经验证的 cryptographic/TEE 分支。",
    },
    "2605.25820": {
        "owner_node": "MULTIMODAL-GENERATIVE-PARADIGMS", "owner_path": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "anchor": "Self-revision：并行位置必须在 Commit 前保持可撤销",
        "delta": "并行 diffusion decoding 的 commit policy 不只按单 token confidence 排序，还要用 visual-grounding overlap 衡量同批位置的互补性；VRI/VRCD 只拥有 selection proposal。",
        "tradeoff": "读取 token-image attention 与组合选择增加 runtime 和调度复杂度。", "failure": "attention overlap 不是因果 grounding，可能漏掉文本依赖或把关键同区域 tokens 错当冗余。", "fallback": "信号失配时回退 confidence top-k、减小并行 K、允许重开或使用顺序 AR/完整迭代。",
    },
    "2605.25966": {
        "owner_node": "TRAIN-PRETRAINING", "owner_path": "books/part-04-training-system/28-pretraining.md", "anchor": "Precision Policy 应沿误差传播路径分区",
        "delta": "把 QAT learning-rate schedule × bit-width × model scale 作为联合实验 identity：FP16/INT8/INT6 的 schedule 差异假设被反证，而 INT4 在约 50M 参数处出现从 noise-dominated 到明确 warmdown preference 的边界。",
        "tradeoff": "定位边界需要大规模 factorial sweep 与 matched seeds。", "failure": "optimizer、数据、训练长度或更大模型变化会使已测 null/boundary 失效。", "fallback": "仅在验证 cells 复用 FP16 schedule；越界时回退 precision-specific local sweep 和保守高精度 recipe。",
    },
    "2605.26029": {
        "owner_node": "PLATFORM-EVALUATION-SYSTEM", "owner_path": "books/part-06-ai-infrastructure/66-evaluation-system.md", "anchor": "Simulator Fidelity：保留真实 Control Plane 仍不足以等同真实硬件",
        "delta": "交互式 causal-discovery evaluation 必须分开 held-out prediction 与 recovered graph/equation fidelity，并记录 observation/intervention policy、实验停止点和 consistency check。",
        "tradeoff": "可干预 SCM environment、机制 scorer 和多轮实验增加 benchmark 成本与 synthetic bias。", "failure": "agent 可通过相关性获得高预测分却未恢复机制，或 premature stop 后给出过度确定答案。", "fallback": "回退简单 prediction baseline，同时保留独立 mechanism audit、强制最小 intervention budget 与人工复核。",
    },
    "2605.26046": {
        "owner_node": "PLATFORM-EVALUATION-SYSTEM", "owner_path": "books/part-06-ai-infrastructure/66-evaluation-system.md", "anchor": "Scorer 不是绝对真相",
        "delta": "把 multi-objective textual-gradient judge optimization 拆成两个 failure owner：联合 critique 的 gradient dilution 与合并单目标 instructions 的 inference interference；criteria、sharing mode 与 prompt revision 必须版本化。",
        "tradeoff": "分解 objective 和重复优化增加 judge calls、搜索预算与集成复杂度。", "failure": "联合反馈失焦，独立优化后的 instructions 又可能在同一 prompt 中互相覆盖。", "fallback": "回退单目标/串行优化、手工 rubric 与 held-out judge calibration，不让自动 prompt update 直接进入 release。",
    },
    "2605.26110": {
        "owner_node": "PLATFORM-TRAINING-OPERATOR", "owner_path": "books/part-06-ai-infrastructure/60-training-operator.md", "anchor": "Operator 与训练并行的边界",
        "delta": "为 continual multimodal tuning 定义 plugin boundary：algorithm state/handler 通过注册接口接入，backbone、distributed runtime 与 job reconciliation 保持平台 owner，并把 plugin/backbone/pipeline revision 组成 run identity。",
        "tradeoff": "稳定接口、兼容矩阵和 adapter tests 增加维护成本，也限制算法任意改写底座。", "failure": "plugin 泄漏 backbone 假设、修改全局状态或依赖未登记 hook 会破坏公平比较与恢复。", "fallback": "接口不够时回退 pinned fork/reference implementation，并用 full integration run 验证后再扩展 operator contract。",
    },
}


def in_owner_interval(arxiv_id: str) -> bool:
    return "2605.24798" <= arxiv_id <= "2605.26115"


receipt = load(OWNER_RECEIPT)
raw = [item for item in receipt["identities"] if in_owner_interval(item["arxiv_id"])]
raw_by_id = {item["arxiv_id"]: item for item in raw}
assert len(raw) == len(raw_by_id) == 691

legacy = load(LEGACY_633)["identities"]
legacy_ids = {item["arxiv_id"] for item in legacy}
assert len(legacy_ids) == 633
assert not (legacy_ids & set(raw_by_id))
assert min(legacy_ids) == "2605.26117" and max(legacy_ids) == "2605.27372"

# The two submitted-window ledgers partition the official owner batch exactly.
screen_rows = {}
source_ledger = {}
for day, label in ((DAY25, "daily-20260525"), (DAY26, "daily-20260526")):
    ledger = load(day / "screening-ledger-independent-final.json")
    for item in ledger["identities"]:
        aid = item["arxiv_id"]
        if aid in raw_by_id:
            assert aid not in screen_rows
            screen_rows[aid] = item
            source_ledger[aid] = label
assert set(screen_rows) == set(raw_by_id)
assert Counter(source_ledger.values()) == {"daily-20260525": 261, "daily-20260526": 430}

retained = sorted(aid for aid, item in screen_rows.items() if item.get("screening_status") == "retained")
closed = sorted(set(raw_by_id) - set(retained))
assert len(retained) == 88 and len(closed) == 603

# Exact-v1 evidence and proposition-level Books comparisons are recoverable
# because identity, exact version and adopted proposition are unchanged.
evidence_by_id = {}
books_by_id = {}
for day in (DAY25, DAY26):
    for item in packet_items(day, "exact-v1-review-packet-independent-final.json"):
        aid = item.get("arxiv_id", "")
        if aid in retained:
            evidence_by_id[aid] = item
    for item in packet_items(day, "books-current-content-comparison-independent-final.json"):
        aid = item.get("arxiv_id", "")
        if aid in retained:
            books_by_id[aid] = item
assert set(evidence_by_id) == set(retained)
assert set(books_by_id) == set(retained)


def first_h2_review_notes(text: str) -> int:
    match = re.search(r"^## Review notes\s*$", text, re.MULTILINE)
    return match.start() if match else len(text)


def section_excerpt(owner_path: str, anchor: str) -> str:
    text = (ROOT / owner_path).read_text()
    text = text[:first_h2_review_notes(text)]
    match = re.search(rf"^#{{2,4}} {re.escape(anchor)}\s*$", text, re.MULTILINE)
    assert match, (owner_path, anchor)
    next_heading = re.search(r"^#{2,4} .+$", text[match.end():], re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading else len(text)
    body = " ".join(
        line.strip() for line in text[match.end():end].splitlines()
        if line.strip() and not line.strip().startswith("<!--")
    )
    assert body and "自检问题" not in anchor and "Review notes" not in anchor, (owner_path, anchor)
    return body[:1200]


def marker_binding(source_family_id: str):
    needle = f"<!-- source-family:{source_family_id} -->"
    matches = []
    for path in (ROOT / "books").rglob("*.md"):
        text = path.read_text()
        count = text.count(needle)
        if count:
            matches.append((path, text, count))
    assert len(matches) == 1, (source_family_id, [(str(p), n) for p, _, n in matches])
    path, text, count = matches[0]
    assert count == 1, (source_family_id, path, count)
    marker_pos = text.index(needle)
    assert marker_pos < first_h2_review_notes(text), (source_family_id, path)
    lines = text.splitlines()
    line_no = text[:marker_pos].count("\n")
    start = line_no
    while start > 0 and not lines[start - 1].startswith("### "):
        start -= 1
    end = line_no + 1
    while end < len(lines) and not lines[end].startswith("### ") and not lines[end].startswith("## "):
        end += 1
    excerpt = " ".join(line.strip() for line in lines[start:end] if line.strip() and not line.strip().startswith("<!--"))
    return str(path.relative_to(ROOT)), excerpt


current_books = []
evidence_items = []
scores = Counter()
for aid in retained:
    row = screen_rows[aid]
    score = row["score_v2"]
    assert score["total"] >= 7
    scores[score["total"]] += 1
    ev = evidence_by_id[aid]
    old_cmp = books_by_id[aid]
    decision = old_cmp["decision"]
    owner_path = old_cmp["owner_path"]
    owner_node = old_cmp["owner_node"]
    marker = None
    marker_excerpt = None
    coverage_anchor = None
    coverage_difference = None
    if decision == "Integrate":
        owner_path, marker_excerpt = marker_binding(row["source_family_id"])
        marker = f"<!-- source-family:{row['source_family_id']} -->"
        decision = "Applied"
        if aid == "2605.25745":
            owner_node = "MODEL-DECODER-ONLY"
    elif aid in NO_CHANGE_AUDIT:
        owner_node, owner_path, coverage_anchor = NO_CHANGE_AUDIT[aid]
        marker_excerpt = section_excerpt(owner_path, coverage_anchor)
        coverage_difference = (
            "该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证："
            + PROPOSITION_OVERRIDES.get(aid, old_cmp.get("new_evidence_delta") or row["screening_reason"])
        )
        decision = "No Change — Existing Coverage"
    else:
        repair = INTEGRATE_REPAIRS[aid]
        owner_node = repair["owner_node"]
        owner_path = repair["owner_path"]
        coverage_anchor = repair["anchor"]
        target_text = (ROOT / owner_path).read_text()
        target_text = target_text[:first_h2_review_notes(target_text)]
        assert re.search(rf"^#{{2,4}} {re.escape(coverage_anchor)}\s*$", target_text, re.MULTILINE), (owner_path, coverage_anchor)
        marker_excerpt = None
        decision = "Integrate"
    method = ev.get("method_locator") or ev.get("method_identity_locators")
    evaluation = ev.get("evaluation_locator") or ev.get("evaluation_locators")
    limitations = ev.get("limitations_locator") or ev.get("limitations_counterevidence_locators")
    claim_boundary = ev.get("claim_boundary") or (
        "只支持 exact-v1 披露的模型、workload、硬件、预算与评价设置；未披露条件为 Not Disclosed，"
        "不能外推为生产或跨分布保证。"
    )
    proposition = PROPOSITION_OVERRIDES.get(aid) or old_cmp.get("new_evidence_delta") or row["screening_reason"]
    comparison = {
        "arxiv_id": aid,
        "source_family_id": row["source_family_id"],
        "owner_node": owner_node,
        "owner_path": owner_path,
        "adjacent_paths": old_cmp.get("adjacent_paths", []),
        "adopted_proposition": proposition,
        "existing_proposition": marker_excerpt,
        "coverage_anchor": coverage_anchor,
        "coverage_difference": coverage_difference,
        "evidence_boundary": claim_boundary,
        "decision": decision,
        "binding_marker": marker,
        "author_check": (
            "Current Books marker is globally unique and before the first main H2 Review notes; semantic final Gate remains fresh-review pending."
            if decision == "Applied"
            else (
                "Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded."
                if decision.startswith("No Change")
                else "Current main body does not carry the adopted delta; root serialized writeback is required."
            )
        ),
    }
    current_books.append(comparison)
    evidence_items.append({
        "arxiv_id": aid,
        "source_family_id": row["source_family_id"],
        "title": row["title"],
        "primary_evidence_version": ev.get("primary_evidence_version", f"arXiv:{aid}v1"),
        "retrieval_route": ev.get("retrieval_route", f"https://arxiv.org/html/{aid}v1"),
        "method_locator": method,
        "evaluation_locator": evaluation,
        "limitations_locator": limitations,
        "claim_boundary": claim_boundary,
        "adopted_proposition": proposition,
        "score": score,
        "review_depth": "deep",
        "completion_result": "complete",
        "owner_node": owner_node,
        "books_decision": decision,
        "evidence_reuse_basis": f"identity/exact-v1/adopted proposition unchanged; recovered from {source_ledger[aid]} and rechecked under current V3",
    })

# MiniMax's official technical page is an independent institutional event. Its
# JSON-LD datePublished, rather than its human-readable date or URL slug, owns
# the event at 2026-05-27 08:00 BJT. The same source family is already bound in
# Ch29, so this is Applied rather than a new root writeback.
minimax_path, minimax_excerpt = marker_binding(MINIMAX["source_family_id"])
assert minimax_path == MINIMAX["owner_path"]
minimax_boundary = (
    "只支持 MiniMax 披露的 M2-series pretrain→SFT 对比、token/language slices、全词表重复数据配方与"
    "对应实验；未披露训练 artifact 和跨模型复现，且 Korean 非修复反例阻止把全词表补数外推为通用方案。"
)
minimax_score = {"design_delta": 3, "system_reach": 2, "durability": 3, "total": 8}
scores[8] += 1
current_books.append({
    "arxiv_id": MINIMAX_ID,
    "source_family_id": MINIMAX["source_family_id"],
    "owner_node": MINIMAX["owner_node"],
    "owner_path": MINIMAX["owner_path"],
    "adjacent_paths": ["books/part-02-model/11-tokenizer.md", "books/part-04-training-system/28-pretraining.md"],
    "adopted_proposition": MINIMAX["adopted_proposition"],
    "existing_proposition": minimax_excerpt,
    "coverage_anchor": "SFT 能否注入知识",
    "coverage_difference": "当前 Ch29 binding 已承担 adopted mechanism、trade-off、Korean counterexample 与 fallback；无需重复写入。",
    "evidence_boundary": minimax_boundary,
    "decision": "Applied",
    "binding_marker": f"<!-- source-family:{MINIMAX['source_family_id']} -->",
    "author_check": "Current Books marker is globally unique and before the first main H2 Review notes; semantic final Gate remains fresh-review pending.",
})
evidence_items.append({
    "arxiv_id": MINIMAX_ID,
    "source_family_id": MINIMAX["source_family_id"],
    "title": MINIMAX["title"],
    "primary_evidence_version": "MiniMax official technical blog; JSON-LD datePublished 2026-05-27T00:00:00Z",
    "retrieval_route": MINIMAX["url"],
    "method_locator": MINIMAX["method_locator"],
    "evaluation_locator": MINIMAX["evaluation_locator"],
    "limitations_locator": MINIMAX["limitations_locator"],
    "claim_boundary": minimax_boundary,
    "adopted_proposition": MINIMAX["adopted_proposition"],
    "score": minimax_score,
    "review_depth": "deep",
    "completion_result": "complete",
    "owner_node": MINIMAX["owner_node"],
    "books_decision": "Applied",
    "evidence_reuse_basis": "official page reread under current V3; prior 05-26 report timestamp is not used as owner evidence",
})

retained_all = retained + [MINIMAX_ID]
assert scores == {7: 22, 8: 57, 9: 10}
book_counts = Counter(item["decision"] for item in current_books)
assert book_counts == {"Applied": 41, "No Change — Existing Coverage": 32, "Integrate": 16}

owner_evidence = {
    "schema": "daily-official-owner-batch-evidence-v3",
    "report_date": "2026-05-27",
    "window": WINDOW,
    "official_schedule": "https://info.arxiv.org/help/availability.html",
    "announcement": {
        "eastern": "2026-05-26T20:00:00-04:00",
        "utc": "2026-05-27T00:00:00Z",
        "asia_shanghai": PUBLIC_TIME,
    },
    "all_category_interval": {
        "preceding_identifier": "2605.24797",
        "first_identifier": "2605.24798",
        "last_identifier": "2605.26116",
        "following_identifier": "2605.26117",
        "sequence_count": 1319,
    },
    "registered_category_projection_count": 691,
    "registered_category_ids": sorted(raw_by_id),
    "institution_events": [{
        "source": "SRC-MINIMAX",
        "id": MINIMAX_ID,
        "title": MINIMAX["title"],
        "public_time_bjt": MINIMAX["public_owner_time"],
        "json_ld_date_published": MINIMAX["json_ld_date_published"],
        "url": MINIMAX["url"],
    }],
    "raw_identity_count": 692,
    "basis": (
        "Neighboring official announcement receipts bound a contiguous all-category sequence. The registered-category projection is recovered from the local 20260526 receipt; its DataCite/OAI date fields are metadata only and do not own this day."
    ),
    "identity_conservation": {
        "current_batch": "692 = 691 official-announcement registered-category identities + 1 MiniMax official technical event",
        "arxiv_recovery": "691 = 261 recovered from daily-20260525 + 430 recovered from daily-20260526",
        "legacy_633_intersection": 0,
        "legacy_633_migration": "all 633 identities are in 2605.26117..2605.27372 and belong to the next official announcement interval, not 2026-05-27",
        "cross_date_correction": "The stale 05-26 report used an unsupported 00:30 BJT owner for the MiniMax page. JSON-LD datePublished owns it at 05-27 08:00 BJT; the 05-26 report must not count the identity a second time.",
    },
    "withdrawn_count": 0,
    "withdrawn_check_boundary": (
        "No owner-batch record carries an official withdrawn/deleted state; all 89 retained exact-v1 bodies/pages are accessible. The 603 closures are not used as positive evidence and remain challengeable by the fresh reviewer."
    ),
}

sources = [
    ("SRC-OPENAI", "official Research index/RSS; adjacent explicit research date 05-20, no window technical event", "checked", "no positive no-hit claim beyond dated index"),
    ("SRC-ANTHROPIC", "official Research index; nearest explicit research date 05-22", "checked", "date-only pages are not promoted without a time inside this window"),
    ("SRC-GOOGLE-AI", "DeepMind Research/Publications; adjacent explicit dates 05-20 and 05-28", "checked", "year-only cards do not prove site-wide no-hit"),
    ("SRC-META-AI", "official Publications entry", "limited", "empty/internal-error behavior; not used for a positive no-hit"),
    ("SRC-QWEN", "official article index; adjacent explicit dates 05-20 and 05-29", "checked", "none"),
    ("SRC-DEEPSEEK", "official Research/News; adjacent explicit dates 04-24 and 06-24", "checked", "none"),
    ("SRC-MOONSHOT", "official Kimi Platform Blog; research/release/RFC slice only", "checked", "no window event found on the dated index"),
    ("SRC-TENCENT-HUNYUAN", "official Research publicList and linked primary artifacts", "checked", "visible dated records outside window"),
    ("SRC-ZAI", "official Research/release index; adjacent explicit dates 05-20 and 06-16", "checked", "none"),
    ("SRC-BYTEDANCE-SEED", "official Research/Public Papers; adjacent explicit dates 05-16 and 05-29", "checked", "none"),
    ("SRC-BAIDU-ERNIE", "official technical Blog; latest explicit pre-window date 05-09", "checked", "none"),
    ("SRC-XIAOMI-MIMO", "official dated paper/blog cards", "limited", "undated cards cannot support a day-level no-hit"),
    ("SRC-MINIMAX", "official Research/Blog JSON-LD datePublished=2026-05-27T00:00:00Z (05-27 08:00 BJT)", "checked", "1 technical research event retained; URL slug/human-readable date not used as owner"),
    ("SRC-ARXIV", "official 05-26 20:00 ET announcement; contiguous sequence projected to registered categories", "checked", "691 arXiv raw = 88 retained + 603 closure"),
]
source_coverage = {
    "schema": "daily-source-coverage-v3",
    "report_date": "2026-05-27",
    "window": WINDOW,
    "checked_at": CHECKED_AT,
    "source_count": 14,
    "institution_source_count": 13,
    "institutional_event_count": 1,
    "sources": [
        {"source_id": sid, "basis": basis, "result": result, "limitation": limitation}
        for sid, basis, result, limitation in sources
    ],
    "ordinary_commits_or_prs_expanded": False,
    "zero_omission_claim": False,
}

outcomes = []
for aid in sorted(raw_by_id):
    recovered = screen_rows[aid]
    if aid in retained:
        cmp = next(item for item in current_books if item["arxiv_id"] == aid)
        reason = (
            "在旧方案仍受原有约束时，材料提出/测得可定位的机制、边界或评价修正："
            + cmp["adopted_proposition"]
            + "；因此需在 exact-v1 边界内重新考虑对应 owner 的选择。"
        )
        status = "retained"
    else:
        reason = recovered.get("screening_reason") or (
            f"{recovered['title']} 的 title+full abstract 只显示任务/应用局部收益，未新增可保留的机制、边界、评价纠错或系统选择变化；若后续公开受控反证或明确系统契约则重开。"
        )
        status = "pre_denominator_closure"
    outcomes.append({
        "arxiv_id": aid,
        "source_family_id": recovered.get("source_family_id", f"SF-2026-ARXIV-{aid.replace('.', '-') }"),
        "title": raw_by_id[aid]["title"],
        "abstract": raw_by_id[aid]["abstract"],
        "categories": raw_by_id[aid].get("categories", []),
        "public_owner_time": PUBLIC_TIME,
        "screening_status": status,
        "screening_reason": reason,
        "reviewed_fields": ["title", "full_abstract", "categories"],
        "recovery_source": source_ledger[aid],
    })

outcomes.append({
    "arxiv_id": MINIMAX_ID,
    "source_family_id": MINIMAX["source_family_id"],
    "title": MINIMAX["title"],
    "abstract": (
        "MiniMax compares pretrain and post-SFT embeddings/lm_head for sparse tokens, identifies target-frequency-driven output-head drift, "
        "and evaluates full-vocabulary repetition data across token and language slices, including a Korean non-fix counterexample."
    ),
    "categories": ["institutional-research-blog", "post-training", "tokenizer"],
    "public_owner_time": MINIMAX["public_owner_time"],
    "screening_status": "retained",
    "screening_reason": (
        "完整技术页给出可定位的 pretrain→SFT 因果诊断、target-frequency/`lm_head` drift 中间量、受控修复实验与"
        "Korean 反例，改变 SFT coverage、回归与 fallback contract；因此通过长期贡献门槛。"
    ),
    "reviewed_fields": ["title", "full_technical_page", "json_ld_datePublished"],
    "recovery_source": "SRC-MINIMAX official Research/Blog",
})

screening = {
    "schema": "daily-screening-outcomes-v3-author-rebuild",
    "report_date": "2026-05-27",
    "window": WINDOW,
    "checked_at": CHECKED_AT,
    "raw_identity_count": 692,
    "retained_count": 89,
    "pre_denominator_closure_count": 603,
    "withdrawn_count": 0,
    "conservation": "692 = 89 retained + 603 pre-denominator closure + 0 withdrawn",
    "normalization": (
        "Old 633/64 and old 698 ledgers do not supply admission. The 691 arXiv owner identities were reprojected through the current title+full-abstract contribution gate; one independently owned MiniMax technical event was added from JSON-LD and full-page review. Prior rows only recover immutable text and exact-v1 locators."
    ),
    "false_positive_negative_challenge": {
        "retained_after_rebuild": 89,
        "reopened_from_stale_projection": 15,
        "demoted_false_positive": ["2605.25310"],
        "closure_count_after_challenge": 603,
    },
    "items": outcomes,
}

evidence = {
    "schema": "daily-evidence-review-v3-author-rebuild",
    "report_date": "2026-05-27",
    "count": 89,
    "deep_complete_count": 89,
    "standard_complete_count": 0,
    "blocked_count": 0,
    "score_distribution": {str(k): v for k, v in sorted(scores.items())},
    "items": evidence_items,
}

books = {
    "schema": "daily-books-comparison-v3-author-rebuild",
    "report_date": "2026-05-27",
    "count": 89,
    "applied_count": 41,
    "no_change_count": 32,
    "pending_integrate_count": 16,
    "items": current_books,
}

evidence_map = {item["arxiv_id"]: item for item in evidence_items}
queue_items = []
for item in current_books:
    if item["decision"] != "Integrate":
        continue
    aid = item["arxiv_id"]
    repair = INTEGRATE_REPAIRS[aid]
    ev = evidence_map[aid]
    queue_items.append({
        "arxiv_id": aid,
        "source_family_id": item["source_family_id"],
        "owner": "root",
        "owner_node": repair["owner_node"],
        "target_path": repair["owner_path"],
        "unique_anchor": repair["anchor"],
        "adopted_proposition": item["adopted_proposition"],
        "proposed_delta": repair["delta"],
        "evidence_boundary": item["evidence_boundary"],
        "trade_off": repair["tradeoff"],
        "failure_mode": repair["failure"],
        "fallback": repair["fallback"],
        "exact_v1_locators": {
            "method": ev["method_locator"],
            "evaluation": ev["evaluation_locator"],
            "limitations": ev["limitations_locator"],
        },
        "status": "pending_root_serialized_writeback",
    })
assert len(queue_items) == 16

queue = {
    "schema": "daily-root-books-writeback-queue-v3",
    "report_date": "2026-05-27",
    "status": "pending_root_serialized_writeback",
    "pending_count": 16,
    "items": queue_items,
    "note": (
        "The author did not edit shared Books. Forty-one current bindings remain applied; thirty-two No Change decisions now cite concrete main-body headings/excerpts, and sixteen failed comparison and require root serialized writeback before fresh review."
    ),
}

materials = {
    "schema": "daily-materials-request-v3",
    "report_date": "2026-05-27",
    "blocked_candidate_count": 0,
    "items": [
        {"source_id": "SRC-META-AI", "missing": "stable dated official publications listing", "effect": "isolated; not used for positive no-hit", "reopen": "official dated listing or page snapshot"},
        {"source_id": "SRC-XIAOMI-MIMO", "missing": "day-level timestamp for undated cards", "effect": "isolated; not used for positive no-hit", "reopen": "official publication timestamp"},
    ],
}

audit = {
    "schema": "daily-author-adversarial-audit-v3",
    "report_date": "2026-05-27",
    "status": "author_repair_complete_pending_root_writeback_and_fresh_non_author",
    "challenges": {
        "owner": "old 633 has zero overlap and migrates to the next announcement interval",
        "coverage": "692 identities = 691 arXiv identities partitioned as 261+430 plus one JSON-LD-owned MiniMax event",
        "false_negative": "14 arXiv mechanism/evaluation/runtime families plus one omitted MiniMax institutional event restored from stale projections",
        "false_positive": "2605.25310 removed because representation decodability alone changes no system contract",
        "evidence": "89 exact-v1/page records have method, evaluation and limitations/counterevidence locators",
        "books": "41 unique current-body markers + 32 No Change with exact main-body heading/excerpt + 16 pending Integrate; 2605.25745 owner corrected to MODEL-DECODER-ONLY",
    },
    "gates": {
        "coverage": "AUTHOR_PASS",
        "candidate_denominator": "AUTHOR_PASS",
        "evidence": "AUTHOR_PASS",
        "books": "PENDING_ROOT_WRITEBACK_THEN_FRESH_SEMANTIC_REVIEW",
        "fresh_non_author": "PENDING",
    },
    "cross_model_review": "skipped in delegated non-interactive author turn; fresh non-author Gate remains mandatory",
}

dump(HERE / "official-owner-batch-evidence-v3.json", owner_evidence)
dump(HERE / "source-coverage-v3.json", source_coverage)
dump(HERE / "screening-outcomes-v3.json", screening)
dump(HERE / "evidence-review-v3.json", evidence)
dump(HERE / "exact-v1-review-packet.json", {"schema": "daily-exact-v1-review-packet-v3", "report_date": "2026-05-27", "items": evidence_items})
dump(HERE / "books-comparison-v3.json", books)
dump(HERE / "books-current-content-comparison.json", books)
dump(HERE / "root-books-writeback-queue-v3.json", queue)
dump(HERE / "materials-request-v3.json", materials)
dump(HERE / "author-adversarial-audit-v3.json", audit)


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def link_to_book(path: str) -> str:
    return "../../../../" + path


report = [
    "# Daily Research — 2026-05-27",
    "",
    "**规范：** V3",
    "",
    "**窗口：** 2026-05-26T09:00:00+08:00 ～ 2026-05-27T09:00:00+08:00",
    "",
    "**状态：** 进行中",
    "",
    "**Books：** 纳入本次",
    "",
    f"**检查时间：** {CHECKED_AT}",
    "",
    "## 1. 结论",
    "",
    "旧 V2.1 的 `633 raw / 64 retained`、DataCite-created owner、评分、Evidence、Books disposition 与 `Complete` 均不继承。05-27 的 arXiv first-public owner 是 2026-05-26 20:00 ET（北京时间 05-27 08:00）的 official announcement batch；全类别连续区间为 `2605.24798..2605.26116`，注册类别投影为 691。MiniMax 技术页的 JSON-LD `datePublished=2026-05-27T00:00:00Z` 另增 1 个独立机构 identity，因此总分母冻结为 **692 = 89 retained + 603 pre-denominator closure + 0 withdrawn**。旧 633 个 arXiv identity 与本集合交集为 0，全部落在下一公告区间。",
    "",
    "89 项均完成 exact-v1/官方技术页深入审阅，Evidence 为 **89 deep + 0 standard + 0 blocked**，评分分布为 `22 score7 + 57 score8 + 10 score9`。本轮逐项清除了摘要背景句式采用命题，并把 48 个旧 No Change 全量重审；MiniMax 事件复用当前唯一 Ch29 binding，Books 投影为 **41 Applied + 32 No Change + 16 pending Integrate**：32 项均记录主 `## Review notes` 前的实际 heading、正文 excerpt 与 exact 差异；16 项没有真实承载，已进入 root 串行 queue。作者没有编辑共享 Books，报告保持 Ongoing。",
    "",
    "## 2. 来源覆盖",
    "",
    "| 来源 | 检查范围与依据 | 结果 | 缺口 |",
    "| --- | --- | --- | --- |",
]
for sid, basis, result, limitation in sources:
    rendered = {"checked": "已检查", "limited": "受阻"}[result]
    report.append(f"| {sid} | {basis} | {rendered} | {limitation} |")
report += [
    "",
    "完整 owner 证据见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260527/official-owner-batch-evidence-v3.json)，14-source 记录见 [`source-coverage-v3.json`](../_sources/daily-20260527/source-coverage-v3.json)，692 条逐项题摘/机构页判定与 family-specific closure 见 [`screening-outcomes-v3.json`](../_sources/daily-20260527/screening-outcomes-v3.json)。Meta 与 MiMo 的入口限制被隔离，不用于正面 no-hit；普通 commit/PR 未扩入 denominator。MiniMax 页在旧 05-26 报告中的 `00:30 BJT` owner 没有 JSON-LD 支持，不能重复计数；该跨日报告元数据由其 owner 另行纠正。",
    "",
    "## 3. 候选与判断",
    "",
    "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |",
    "| --- | --- | --- | --- | --- |",
]
ev_by_id = {item["arxiv_id"]: item for item in evidence_items}
book_by_id = {item["arxiv_id"]: item for item in current_books}
for aid in retained_all:
    ev = ev_by_id[aid]
    bk = book_by_id[aid]
    score = ev["score"]
    contribution = f"{ev['adopted_proposition']}；{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']}"
    if bk["decision"] == "Applied":
        book_text = f"整合：当前正文 binding 已存在 [章节]({link_to_book(bk['owner_path'])})：{bk['owner_node']}"
    elif bk["decision"].startswith("No Change"):
        book_text = f"已有覆盖 [章节]({link_to_book(bk['owner_path'])})：{bk['owner_node']}"
    else:
        book_text = f"整合：待 root 串行写回 [章节]({link_to_book(bk['owner_path'])})：{bk['owner_node']}"
    material_url = MINIMAX["url"] if aid == MINIMAX_ID else f"https://arxiv.org/html/{aid}v1"
    material_time = MINIMAX["public_owner_time"] if aid == MINIMAX_ID else PUBLIC_TIME
    report.append(
        f"| [{aid} {md_escape(ev['title'])}]({material_url}) | {material_time} | {md_escape(contribution)} | 深入完成 | {book_text} |"
    )
report += ["", "## 4. 证据与知识整合", ""]
for aid in retained_all:
    ev = ev_by_id[aid]
    bk = book_by_id[aid]
    report += [
        f"### [{aid} {ev['title']}]({MINIMAX['url'] if aid == MINIMAX_ID else f'https://arxiv.org/html/{aid}v1'})",
        "",
        f"- **采用命题：** {ev['adopted_proposition']}",
        f"- **方法定位：** {ev['method_locator']}",
        f"- **评价定位：** {ev['evaluation_locator']}",
        f"- **限制/反证：** {ev['limitations_locator']}",
        f"- **证据边界：** {ev['claim_boundary']}",
        *([f"- **当前正文承载：** `{bk['coverage_anchor']}` — {bk['existing_proposition']}", f"- **差异判断：** {bk['coverage_difference']}"] if bk["decision"].startswith("No Change") else []),
        f"- **Books：** `{bk['decision']}`；owner 为 `{bk['owner_node']}` / [`{bk['owner_path']}`]({link_to_book(bk['owner_path'])})。{bk['author_check']}",
        "",
    ]
report += [
    "## 5. 缺口与下一步",
    "",
    "Evidence 无 candidate blocker。Meta official Publications 的稳定日期列表与 MiMo 未标日期卡片继续作为来源级隔离项：它们不支持正面 no-hit、候选或 Books 结论；取得官方日期证据时只重开相应来源。当前可执行 Books Gate 是 root 按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260527/root-books-writeback-queue-v3.json) 串行写回 16 项；写回后必须由不同 fresh non-author 独立挑战 692 owner/603 closure、89 项 Evidence/score、32 项 Existing Coverage、41 个既有 binding 与 16 个新 binding。旧 05-26 日报对同一 MiniMax identity 的错误日期归属需由该日报 owner 机械纠正，不能双计。",
    "",
    "## 6. 复核",
    "",
    "- **复核者：** 待不同 fresh non-author reviewer。",
    "- **结论：** 未通过最终 Gate（author repair 已完成；16 项 root Books writeback 与 fresh Gate pending）。",
    "- **作者检查：** Coverage/denominator/Evidence 算术已闭合；41 个 marker 全局唯一并位于首个主 `## Review notes` 前；32 个 No Change 有正文 anchor/excerpt；2605.25745 已按当前正文改归 `MODEL-DECODER-ONLY`。",
    "- **独立性边界：** 本轮作者不自签 Complete，不把 validator 或既有 post-write 收据当作 fresh 语义验收。",
    "",
]
REPORT.write_text("\n".join(report))

checkpoint = f"""# 2026-05-27 V3 author rebuild checkpoint

## 当前权威状态

- 日报状态：`Ongoing`；author repair 已完成，Books root writeback 与 fresh non-author Gate pending。
- 严格窗口：`{WINDOW}`，Asia/Shanghai。
- official announcement：`2026-05-26T20:00:00-04:00` = `{PUBLIC_TIME}`。
- denominator：`692 = 89 retained + 603 pre-denominator closure + 0 withdrawn`。
- identity conservation：`692 = 691 arXiv owner identities + 1 MiniMax official technical event`；arXiv 子集 `691 = 261 daily-20260525 recovery + 430 daily-20260526 recovery`，旧 633 与本日交集为 0，全部迁移到下一 announcement interval。MiniMax 由 JSON-LD `datePublished=2026-05-27T00:00:00Z` 定位到 05-27 08:00 BJT；旧 05-26 报告的 `00:30 BJT` 归属不能重复计数。

## Evidence / Books

- Evidence：`89 deep + 0 standard + 0 blocked`；score=`22×7 + 57×8 + 10×9`。
- Books：`41 Applied + 32 No Change + 16 pending Integrate`。
- 41 个当前 marker 全局唯一并位于首个主 `## Review notes` 前；新增 MiniMax identity 使用现存 Ch29 唯一 binding，`2605.25745` 当前唯一 owner 是 `MODEL-DECODER-ONLY` / Ch18，不继承旧 Ch48 routing。
- 32 个 No Change 均有主 `## Review notes` 前的实际 heading、正文 excerpt 与 exact 差异；旧有章节概述、`Review notes` 和自检问题均不再作为 coverage。
- 作者没有编辑共享 Books；`root-books-writeback-queue-v3.json` 精确列出 16 项 target/anchor/delta/evidence boundary/trade-off/failure/fallback 与 exact-v1 locators。

## 当前 Gate

- Coverage Gate：`AUTHOR_PASS`。
- Candidate Denominator Gate：`AUTHOR_PASS`。
- Evidence Gate：`AUTHOR_PASS`。
- Books Gate：`PENDING_ROOT_WRITEBACK_THEN_FRESH_SEMANTIC_REVIEW`。
- Fresh non-author Gate：`PENDING`。

## 精确剩余工作

root 先串行写回 16 项且同步 queue 状态；随后由未参与本轮 author rebuild 和 Books 写回的 fresh reviewer 独立挑战 official owner interval/机构事件、603 条 closure、89 项 exact-v1/score、32 个 No Change、41 个既有 binding 与 16 个新 binding 的采用命题、evidence boundary、trade-off、failure/fallback、owner 与相邻衔接。全部通过后才能把 README 标为 Complete。
"""
(HERE / "AUTHOR_V3_RECERTIFICATION_CHECKPOINT_20260916.md").write_text(checkpoint)

print(json.dumps({
    "raw": 692,
    "retained": 89,
    "closure": 603,
    "withdrawn": 0,
    "deep": 89,
    "standard": 0,
    "books": dict(book_counts),
    "pending_root": 16,
}, ensure_ascii=False))
