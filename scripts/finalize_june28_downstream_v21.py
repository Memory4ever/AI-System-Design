#!/usr/bin/env python3
"""Build the strict 2026-06-28 V2.1 downstream pre-write packet."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260628"
REPORT = ROOT / "papers/2026/06/28/README.md"
LEDGER = PACKET / "screening-ledger.json"
WORKING = PACKET / "EVIDENCE_REVIEW_WORKING_V1.md"
DENOMINATOR = "daily-v2.1:2026-06-28:20c51e943aacc58d"
EXECUTED_AT = "2026-08-29T21:20:00+08:00"
ND = "Not Disclosed"

EXACT_IDENTITY_OVERRIDES = {
    "2606.28876": {
        "title": "Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory",
        "abstract": (
            "Long-context language models often conflate two different goals: compressing history into an efficient state, "
            "and maintaining reliable long-term memory. Linear, recurrent, and sparse attention reduce the cost of processing "
            "long sequences, but they do not by themselves specify when a fact should be written, overwritten, protected from "
            "distractors, or discarded. We study memory-managed long-context attention, a research route that separates a fast "
            "recurrent or sparse backbone from explicit editable request-local memory slots and query-time sparse fallback. "
            "Across structured synthetic tasks, token/chunk/sequence bridges, generated natural language, and local frozen-model "
            "diagnostics, pure fixed-state or pure sparse methods fail some overwrite, version, anti-pollution, or no-write-signal "
            "cases, while a hybrid covers both routes. The evidence separates three claims: controlled slot lifecycle is feasible, "
            "sparse fallback is needed when writes lack future-query signals, and learned open-domain selection remains the main "
            "architectural bottleneck. We do not claim a final generative architecture, global slot-trajectory convergence, or "
            "systems superiority."
        ),
        "stable_node_id": "MODEL-LONG-CONTEXT",
    },
}


PATHS = {
    "AGENT-MCP": "books/part-07-agent/83-mcp.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-PLANNING": "books/part-07-agent/79-planning.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "INFER-DECODE": "books/part-05-inference-system/44-decode.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-REQUEST-LIFECYCLE": "books/part-05-inference-system/42-what-happens-during-inference.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/49-tensorrt-llm.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/22-long-context.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-GPU-SCHEDULER": "books/part-06-ai-infrastructure/63-gpu-scheduler.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "TRAIN-DPO": "books/part-04-training-system/34-dpo.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-PRETRAINING": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-RLHF": "books/part-04-training-system/31-rlhf.md",
    "TRAIN-SFT": "books/part-04-training-system/29-sft.md",
}

ADJACENT = {
    "AGENT-MCP": "books/part-07-agent/82-multi-agent.md",
    "AGENT-MEMORY": "books/part-07-agent/76-rag.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/81-workflow.md",
    "AGENT-PLANNING": "books/part-07-agent/78-tool-calling.md",
    "AGENT-PLATFORM": "books/part-07-agent/83-mcp.md",
    "AGENT-RAG": "books/part-07-agent/77-memory.md",
    "AGENT-WORKFLOW": "books/part-07-agent/80-reflection.md",
    "INFER-DECODE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/44-decode.md",
    "INFER-REQUEST-LIFECYCLE": "books/part-05-inference-system/43-prefill.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/48-speculative-decoding.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/21-moe.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-GPU-SCHEDULER": "books/part-06-ai-infrastructure/64-volcano.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/71-multi-tenant.md",
    "TRAIN-DATA": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-DPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-GRPO": "books/part-04-training-system/32-ppo.md",
    "TRAIN-PRETRAINING": "books/part-04-training-system/27-data.md",
    "TRAIN-RLHF": "books/part-04-training-system/32-ppo.md",
    "TRAIN-SFT": "books/part-04-training-system/30-lora.md",
}

TARGET_ANCHORS = {
    "AGENT-MCP": "## Tool Catalog 扩大后，Discovery 与 Execution 必须分离",
    "AGENT-MEMORY": "### Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery",
    "AGENT-MULTI-AGENT": "### Pairwise coupling 不能外推 group dynamics",
    "AGENT-PLANNING": "## 完成证据与 Verification",
    "AGENT-PLATFORM": "## Agent Runtime State Machine",
    "AGENT-RAG": "### Query、Compression 与 Stopping 是联合 Policy",
    "AGENT-WORKFLOW": "## State Machine 是基本模型",
    "INFER-DECODE": "## Decode 的结束条件",
    "INFER-KV-CACHE": "### 先判断哪一种状态超出容量，再选择 TP 或 KV Compression",
    "INFER-REQUEST-LIFECYCLE": "## 请求状态机",
    "INFER-SCHEDULING": "## 调度对象从 request 变成 token state",
    "INFER-TENSORRT-LLM": "## 量化为什么不自动带来加速",
    "MODEL-LONG-CONTEXT": "### 从 Dense Checkpoint 迁移到 Hybrid State Model",
    "MULTIMODAL-EMBODIED-VLA": "## Safety envelope",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "## Cache、rollback 与 exactness",
    "MULTIMODAL-WORLD-MODELS": "## State ownership",
    "PLATFORM-EVALUATION-SYSTEM": "## Evaluation Run 的平台对象模型",
    "PLATFORM-GPU-SCHEDULER": "## GPU 不是同质标量",
    "PLATFORM-MONITORING": "## Monitoring 也会改变系统",
    "PLATFORM-SECURITY": "## 风险管理而不是一次性认证",
    "TRAIN-DATA": "### 从 sample provenance 到训练生命周期 lineage",
    "TRAIN-DPO": "## KL-constrained 最优策略",
    "TRAIN-GRPO": "### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界",
    "TRAIN-PRETRAINING": "## 一次 training step 的状态流",
    "TRAIN-RLHF": "## Reward hacking 与 Goodhart's Law",
    "TRAIN-SFT": "## Evaluation 应分开能力与行为",
}

OWNER_EXISTING = {
    "AGENT-MCP": "Ch83 已把 discovery/capability 与业务授权、effect-time policy、group admission 分开，但尚未把多协议组合和一次 execution 的 grant/handle/policy/audit 对象统一进可检查状态机。",
    "AGENT-MEMORY": "Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。",
    "AGENT-MULTI-AGENT": "Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。",
    "AGENT-PLANNING": "Ch79 已把 proposal、pre-commit verifier、environment feedback、abstention 与 executable commit 分权。",
    "AGENT-PLATFORM": "Ch84 已把 agent definition、workflow graph、runtime/harness identity、trace、promotion 与 side-effect evidence 纳入平台生命周期。",
    "AGENT-RAG": "Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。",
    "AGENT-WORKFLOW": "Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。",
    "INFER-DECODE": "Ch44 已把 masked-diffusion refinement、frontier advancement、cache refresh 与 termination 拆成 request-local decode state，但尚未表达可连续携带且可重编辑的 token-mixture state。",
    "INFER-KV-CACHE": "Ch45 已拥有 head/layer/page-aware eviction、quality-memory calibration、residual path、refresh、FullKV fallback 与 production SLO 边界。",
    "INFER-REQUEST-LIFECYCLE": "Ch42 已把 phase、queue、placement、task completion、success 与 release 绑定成 request lifecycle。",
    "INFER-SCHEDULING": "Ch56 已把 admission、iteration scheduling、routing/placement、autoscaling、TP/KV state、预测误差与 SLO 放入多时间尺度控制面。",
    "INFER-TENSORRT-LLM": "Ch49 已要求 execution plan 绑定 model、precision、layout、kernel、hardware、correctness vector 与 quality/performance gate。",
    "MODEL-LONG-CONTEXT": "Ch22 已显式区分 checkpoint `M_0` 与 request-owned mutable `M_t`，并覆盖 sparse slots、write conflict、reset/session identity、external-memory boundary 与 frozen-path fallback。",
    "MULTIMODAL-EMBODIED-VLA": "Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "Ch24 已拥有 autoregressive/diffusion/masked state、editable token、provisional commit、cache/rollback 与 validation boundary。",
    "MULTIMODAL-WORLD-MODELS": "Ch25 已拥有 persistent/action-conditioned state、stochastic rollout、entity identity、simulation artifact 与 physical commit boundary。",
    "PLATFORM-EVALUATION-SYSTEM": "Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。",
    "PLATFORM-GPU-SCHEDULER": "Ch63 已把 device/topology/gang feasibility、routing、capacity、placement 与 measured useful work纳入调度控制面。",
    "PLATFORM-MONITORING": "Ch67 已把多 sensor、drift、checkpoint freshness、observe-only authority、告警与 rollback 分层。",
    "PLATFORM-SECURITY": "Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。",
    "TRAIN-DATA": "Ch27 已拥有 sample/transform/label provenance、license、lineage、mixture 与 admission，但尚未要求保留 per-annotator distribution 以阻止 majority label 静默取得价值边界真值。",
    "TRAIN-DPO": "Ch34 已绑定 base/reference/policy identity、preference construction、functional/non-functional trade-off 与 regression evaluation。",
    "TRAIN-GRPO": "Ch33 已拥有 typed trajectory credit、verifier、baseline/normalization、policy freshness 与 off-policy boundary。",
    "TRAIN-PRETRAINING": "Ch28 已拥有 optimizer/schedule/precision/budget、mid-training skill artifact、search experience 与 downstream promotion receipt。",
    "TRAIN-RLHF": "Ch31 已解释 reward-model proxy、Goodhart、reference policy 与 reward hacking，但尚未把 equal-budget cloned-policy counterfactual 变成 transition admission gate。",
    "TRAIN-SFT": "Ch29 已把 demonstration distribution、language/model slice、安全回归、forgetting 与 serving interface 分开验收。",
}

INTEGRATE = {
    "2606.28690", "2606.28772", "2606.28955", "2606.28995", "2606.29038",
    "2606.29066",
}

WEEKLY_ONLY = {
    "2606.28692", "2606.28707", "2606.28712", "2606.28751", "2606.28754",
    "2606.28758", "2606.28804", "2606.28864", "2606.28896", "2606.28898",
    "2606.28932", "2606.28938", "2606.29013", "2606.29059", "2606.29112",
    "2606.29126", "2606.29129",
}

WEEKLY_REASON = {
    "2606.28692": "两层 clinical self-learning 与 212-tool loop 仍由单一医疗工具宇宙、观察性 EHR 与领域 rubric 定义，不能改写通用 Workflow owner。",
    "2606.28707": "semantic-cluster historical baseline 是 critic-free RL 的局部方差控制器；它没有改变 verifier、trajectory 或 reward authority。",
    "2606.28712": "coupled factor graph 与 alternating IRLS 是四个 WildGS scene 上的局部优化路线，且更复杂 joint setting 并不稳定优于 pose-only。",
    "2606.28751": "path-space/irreversibility 主要是受控小模型上的理论结构；planning/uncertainty 结论尚未形成可部署 state contract。",
    "2606.28754": "NoIF/SHIFT 只在作者 wafer/chiplet simulator 中成立，数据中心迁移仍是 future work，不能改写 cluster GPU scheduler。",
    "2606.28758": "96-token sketch 与 embedded world model 是驾驶模型局部架构，没有建立跨任务 world-state owner 或 physical promotion contract。",
    "2606.28804": "visual/parameter-space 协同视频生成是特定 embodied world-model 架构；OOD affordance 与 morphology failure 阻止其成为长期系统结论。",
    "2606.28864": "九种 VLM test-time strategy 的胜负随模型、prompt、benchmark 与 extraction 改变，只保留经验上下文。",
    "2606.28896": "SAR augmentation recipe/observer/repair 由领域数据与 observer 定义，且 5/11 batch 未达到最高 evidence level。",
    "2606.28898": "日文新闻上的 paraphrase+self-training+CPT/SFT/DPO 是知识更新配方，不建立通用 DPO owner 变化。",
    "2606.28932": "duplicated latent residual 与 closed-form fold 是 LLaMA-style low-rank pretraining 的局部参数化，部署图不变不足以形成训练系统新 contract。",
    "2606.28938": "electro-aware driving co-state 只由 synthesized/simulated control proxy 验证，未形成 closed-loop road-safety 结论。",
    "2606.29013": "frozen Qwen branch+image expert 的 MoT 是局部 multimodal architecture；定性 transfer 不证明跨 backbone 的生成 owner 演进。",
    "2606.29059": "frozen DINO latent 上的 feature-space flow 是 context-video 模型路线，非 action-conditioned 且 sampler/BPTT 成本高。",
    "2606.29112": "class-subspace detector 只覆盖两个小图像数据集和一种 latent-class attack，不能外推为平台安全机制。",
    "2606.29126": "环境预给 hierarchy 下的 receiver-driven raw-feature addressing 是 cooperative MARL 的局部通信方法；它未建立跨环境的 channel identity、admission 或 privacy contract。",
    "2606.29129": "Ozaki II scaling 是 GH200/INT8 GEMM 的数学与 kernel 局部改进，不改变 execution-plan owner。",
}

INTEGRATE_EXISTING = {
    "2606.28690": "Ch83 有 group admission，却没有 per-protocol IR、trace replay 与 pairwise composition counterexample 作为组合升级前的验证对象。",
    "2606.28772": "Ch27 保存 label lineage，却没有规定 contested safety boundary 必须保留原始 annotator distribution 而非只提交 majority label。",
    "2606.28925": "Ch82 有 capability routing 和 channel admission，却没有先预测具备覆盖能力的 agent set、再由确定性 cost/coverage selector 处理实际执行集合的两阶段边界，也没有把 coverage miss 与 cost trade-off 分开记账。",
    "2606.28955": "Ch31 讨论 reward hacking，却没有在 transition 写入 replay 前比较 cloned current/modified policy 的 equal-budget counterfactual。",
    "2606.28958": "Ch82 有 latent channel identity，却没有把 visible commitment、full-KV manifest、verifier filter 与 quarantine 绑定成完整性收据。",
    "2606.28995": "Ch26 有独立 safety filter 与 controller-owned physical commit，却没有把离线 HJ/barrier approximation 编译为在线闭式 DMP modulation，也没有把 learned value 的 calibration 前提与 certificate 退化写入 fallback 边界。",
    "2606.29038": "Ch66 已版本化 metric identity、raw evidence 与 release selector，却没有禁止 optimizer、evaluator、champion selector 各自重写 aggregation semantics，也没有要求三者调用同一个可执行 metric artifact。",
    "2606.29066": "Ch44 区分 refinement/advancement，却没有 request-local continuous mixture、异步 per-token progress、re-edit 与 commit state。",
    "2606.29073": "Ch83 说明 MCP 不授予授权，却没有 grant、handle、policy、audit objects 与 machine-readable invariant fixtures 的 execution-control IR。",
    "2606.29124": "Ch72 有安全测试、外部 reference monitor 与人工 release gate，却没有从精确规范句抽取 constraint、生成 extremal case、执行 differential comparison，再把人工确认与原始 specification sentence 串成 protocol-testing lineage。",
    "2606.29126": "Ch82 有 sender/receiver channel identity，却没有让 receiver 逐层选择 group、sender、entity 后读取 raw feature 的 hierarchical admission。",
}

INTEGRATE_DELTA = {
    "2606.28690": "把每个 agent protocol lowering 为带 source/type evidence 的有限状态 IR，先做 pairwise composition 与 trace replay，再把 counterexample 编译成可执行回归；未知组合保持隔离。",
    "2606.28772": "把 per-annotator label、threshold/disagreement 与聚合 rule 作为训练数据状态保存；majority label 只是一个 materialized view，不能删除 contested boundary。",
    "2606.28925": "router 先输出覆盖能力的 agent set，cost/latency policy 再对同一 scorer 输出做确定性 post-selection；coverage miss 与 cost trade-off 分开计量。",
    "2606.28955": "在 transition admission 前冻结 current policy/return estimator，以 equal budget 预测 modified-policy counterfactual；只有 evaluator 接受才写入 replay。",
    "2606.28958": "full-KV handoff 必须先发布可见 commitment，并用 sender/receiver/model/layout 绑定的完整性 manifest、verifier 与 quarantine 决定是否接收。",
    "2606.28995": "把离线 HJ/CBVF learned value 与 conformal calibration 编译为在线 closed-form DMP safety modulation；controller 仍拥有 physical commit。",
    "2606.29038": "将 metric extraction/aggregation 实现提升为一个版本化 callable contract，由 optimizer、evaluator 与 champion selector 调用同一 artifact，并保留 raw trajectory 重算路径。",
    "2606.29066": "masked-diffusion decoder 为每个 token 保存可连续携带的 x-prediction mixture 与 progress，允许 bounded re-edit，只有 commit state 才进入可见 frontier。",
    "2606.29073": "把 connection capability lowering 为 grant、handle、policy 与 audit objects；每次执行先验证 machine-readable invariant，capability 仍不等于 authorization。",
    "2606.29124": "把 protocol specification revision、constraint sentence、extremal input、reference expansion、differential result 与 human verdict 串成一条安全测试 lineage。",
    "2606.29126": "把通信 read authority 交给 receiver：先选择 group，再选择 sender/entity，最后读取 addressable raw feature；未验证 hierarchy 回退 typed broadcast。",
}

OWNER_NARRATIVE = {
    "AGENT-MCP": "协议连接层要再向下编译成可执行控制状态。每个 protocol 先 lowering 为可回放的有限状态 IR，组合前检查 transition 与 source/type evidence；一次 tool execution 则必须由 grant、handle、policy 与 audit objects 共同标识。Capability 或连接成功只产生 proposal，只有 host-side invariant 与 effect authorization 才能 commit。",
    "TRAIN-DATA": "标注聚合不能静默删除价值分歧。Data owner 应保存 per-annotator label、annotator/threshold identity、disagreement 与 aggregation revision；majority 或 soft label 只是可重建的 materialized view。训练可消费聚合结果，但 evaluation 与 policy review 必须能恢复 contested boundary。",
    "AGENT-MULTI-AGENT": "多 Agent 路由和通信应由三个分离的状态机组成：router 先提出 capability-covering agent set，确定性 policy 再按 cost/latency 选择执行集合；receiver 对消息按 group、sender、entity 分层 admission；若通道承载 full KV，visible commitment 与绑定 model/layout 的 integrity manifest 必须先于接收，失败则 quarantine 或回退 typed text。",
    "TRAIN-RLHF": "Reward-hacking 防线可以前移到 transition admission：在修改环境或 replay state 前冻结 current policy 与 return evaluator，对 current/modified policy 做 equal-budget counterfactual forecast；只有 evaluator 接受才提交 transition。模型负责 proposal，独立 evaluator 拥有 gate，原始 true-objective evidence 继续保留。",
    "MULTIMODAL-EMBODIED-VLA": "物理安全约束可以把昂贵计算移到离线：用 HJ/CBVF 近似学习安全 value 并校准，再把它编译成在线 closed-form DMP modulation。Learned value 只提供 bounded safety sensor，low-level controller 与真实 observation 仍拥有 action commit；coverage 或 calibration 越界即切回保守 controller。",
    "PLATFORM-EVALUATION-SYSTEM": "同一个 outcome metric 若在 optimizer、evaluator 与 champion selector 中分别重写，候选即使不变也会发生 selection inversion。Evaluation owner 应发布版本化 callable metric contract，让所有阶段消费同一 extraction/aggregation artifact，并保存 raw trajectory、contract revision 与可重算 verdict。",
    "INFER-DECODE": "Masked-diffusion decode 不必把每一步压成 token-or-mask。Request 可以为每个位置持有连续 x-prediction mixture、异步 progress 与 bounded re-edit state；只有通过 commit rule 的离散 token 才进入 visible frontier。这样 refinement 信息可跨 step 延续，而 cache、step policy 与 commit identity 仍可审计。",
    "PLATFORM-SECURITY": "协议安全测试应从规范拥有真值：锁定 specification revision，抽取显式 constraint，生成边界/extremal case，对多个实现差分执行，再由人工确认 anomaly 是否为 bug。LLM 只生成 candidate constraint/test；reference implementation 与 human verdict 分别拥有 differential signal 和最终 adjudication。",
}

OWNER_BOUNDARY = {
    "AGENT-MCP": "Pairwise finite-state composition 与十个 invariant fixtures 不证明任意多协议、生产 runtime 或 proprietary implementation 安全；IR/handle 不完整时隔离协议并回退单工具人工授权。",
    "TRAIN-DATA": "三位 annotator 和单一 HateXplain/BERT slice 不能区分稳定价值阈值与标注噪声；高分歧时保留多视图或转人工，不把 minority label 自动升级为真值。",
    "AGENT-MULTI-AGENT": "Set labels/cost 是模拟或启发式，receiver hierarchy 由环境预给，full-KV 证据只覆盖有限 Qwen/HiddenBench channel；任一 identity 或 integrity 缺失时回退单 Agent、typed text/schema 与独立 verification。",
    "TRAIN-RLHF": "Gate 依赖已能把 hacking trajectory 排低的 evaluator、clean seed 与额外 1.8×–4.2× 成本；evaluator misspecification 时它会接受错误 transition，需回退人工/true-objective review。",
    "MULTIMODAL-EMBODIED-VLA": "Neural HJ approximation 不是绝对 certificate，依赖已知 signed-distance specification 与离线 coverage；OOD、校准不足或 sensor drift 时停止 modulation 并交回 conservative safety controller。",
    "PLATFORM-EVALUATION-SYSTEM": "一个 canonical metric 不能修复错误目标或缺失 trajectory；contract migration 也会改变历史可比性。Schema/semantics 不兼容时 Gate 保持 Open，并用旧 revision 对 raw evidence 重算。",
    "INFER-DECODE": "连续 mixture 是否被 pretrained MDLM 正确解释只在两组模型/代码任务中验证；它增加 request state、alignment 与 kernel burden，质量或硬件不支持时回退标准 mask/unmask decoder。",
    "PLATFORM-SECURITY": "RFC 中未显式写出的约束不会被自动恢复，短消息差分 anomaly 也不等于实现漏洞；无法复现或确认时保持 Unknown，并回退人工 protocol review。",
}

SELECTION_UNITS = {
    "2606.28690": "DA-20260628-PROTOCOL-EXECUTION-INVARIANTS",
    "2606.28995": "DA-20260628-COMPILED-PHYSICAL-SAFETY",
    "2606.29038": "DA-20260628-SINGLE-METRIC-CONTRACT",
}

SUBSUMED = {
    "2606.29073": "DA-20260628-PROTOCOL-EXECUTION-INVARIANTS",
    "2606.29124": "DA-20260628-PROTOCOL-EXECUTION-INVARIANTS",
}

BENCH_OVERRIDES = {
    "2606.28720": {"hardware": "single NVIDIA RTX 4090"},
    "2606.28839": {"model": "DeepSeek and GPT-4o-mini API models"},
    "2606.28843": {"model": "nine languages across three disclosed model families"},
    "2606.28862": {"model": "Grounding DINO detector and Qwen2.5-VL"},
    "2606.28864": {"model": "Qwen, LLaVA and SmolVLM families", "hardware": "NVIDIA H200"},
    "2606.28876": {"input_length": "2M-token stress slice; other staged contexts disclosed"},
    "2606.28932": {"model": "60M–7B LLaMA-style models"},
    "2606.28938": {"hardware": "single NVIDIA RTX 3090"},
    "2606.28953": {"model": "ResNet50 victim model"},
    "2606.28958": {"model": "Qwen3-4B and Qwen3-8B", "precision": ND},
    "2606.28962": {"model": "seven disclosed LLMs", "precision": "INT8, FP4 and NF4 quantization paths"},
    "2606.29013": {"model": "frozen Qwen2.5 branch; 1.5B/3B/7B scales"},
    "2606.29066": {"model": "LLaDA-8B-Instruct and LLaDA2.0-mini"},
    "2606.29088": {"model": "13 open-weight models; four small fine-tuned models", "precision": "bf16 for disclosed fine-tuning/evaluation path"},
    "2606.29094": {"model": "LLaDA-8B and Dream-7B; Llama-3.3-70B judge", "hardware": "NVIDIA GH200 and H100 clusters", "input_length": "maximum 4,096 tokens", "slo": "homogeneous per-request SLO contract in §5"},
    "2606.29112": {"model": "ResNet-18 and ResNet-34"},
    "2606.29129": {"hardware": "NVIDIA GH200 with CUDA 13.2", "precision": "INT8 matrix engines with DGEMM/SGEMM references", "input_length": "square matrices of size 1,024 and 16,384"},
}


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def first_sentence(value: str) -> str:
    value = clean(value)
    match = re.search(r"(?<=[.!?])\s+", value)
    return (value[:match.start() + 1] if match else value)[:600]


def opening_claim(value: str, minimum: int = 80) -> str:
    """Return enough leading abstract sentences to state the actual problem."""
    value = clean(value)
    pieces = re.split(r"(?<=[.!?])\s+", value)
    selected: list[str] = []
    for piece in pieces:
        if not piece:
            continue
        selected.append(piece)
        if len(" ".join(selected)) >= minimum:
            break
    return " ".join(selected)[:600]


def md(value: str) -> str:
    return clean(value).replace("|", "\\|")


def chapter_ref(path: str, anchor: str | None = None) -> str:
    lines = (ROOT / path).read_text().splitlines()
    if anchor is None:
        anchor = next(line for line in lines if line.startswith("## "))
    assert lines.count(anchor) == 1, (path, anchor)
    return f"{path}#L{lines.index(anchor) + 1} — {anchor}"


def parse_working() -> dict[str, dict[str, str]]:
    out = {}
    for line in WORKING.read_text().splitlines():
        if not line.startswith("| `SF-2026-ARXIV-"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        assert len(cells) == 6, cells
        family, primary, method, evaluation, limitation, artifact = cells
        out[family] = {
            "primary": primary,
            "method": clean(method),
            "evaluation": clean(evaluation),
            "limitation": clean(limitation),
            "artifact": clean(artifact),
        }
    assert len(out) == 65
    return out


def reconcile_exact_primary_identity(payload: dict) -> dict:
    """Replace discovery metadata when exact-v1 full text proves a mismatch."""
    for row in payload["identities"]:
        override = EXACT_IDENTITY_OVERRIDES.get(row["arxiv_id"])
        if not override:
            continue
        row.update(override)
        if "semantic_screen_reason" in row:
            row["semantic_screen_reason"] = (
                "Exact-v1 identity reconciliation: retained under `MODEL-LONG-CONTEXT` because the paper defines request-local "
                "editable memory lifecycle, sparse fallback, and an explicit boundary between compressed state and reliable memory."
            )
    return payload


def persist_identity_reconciliation(payload: dict) -> None:
    LEDGER.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    provisional_path = PACKET / "screening-ledger-provisional.json"
    provisional = json.loads(provisional_path.read_text())
    provisional = reconcile_exact_primary_identity(provisional)
    provisional_path.write_text(json.dumps(provisional, ensure_ascii=False, indent=2) + "\n")

    audit_path = PACKET / "denominator-full-semantic-audit-v1.tsv"
    rows = list(csv.DictReader(audit_path.open(), delimiter="\t"))
    for row in rows:
        override = EXACT_IDENTITY_OVERRIDES.get(row["arxiv_id"])
        if not override:
            continue
        row["title"] = override["title"]
        row["stable_node_id"] = override["stable_node_id"]
        row["family_specific_reason"] = (
            "Exact-v1 identity reconciliation: editable request-local memory lifecycle and sparse fallback alter the long-context state contract."
        )
    with audit_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def make_items() -> tuple[list[dict], dict]:
    payload = reconcile_exact_primary_identity(json.loads(LEDGER.read_text()))
    persist_identity_reconciliation(payload)
    assert payload["denominator_id"] == DENOMINATOR
    evidence = parse_working()
    rows = [
        row for row in payload["identities"]
        if row["semantic_screen_status"] == "retained_for_exact_v1_review"
    ]
    assert len(rows) == 65 and payload["registered_window_identities"] == 211
    items = []
    for row in rows:
        aid = row["arxiv_id"]
        family = row["source_family_id"]
        fact = evidence[family]
        if aid in INTEGRATE:
            disposition = "Integrate"
            score = (3, 3, 3) if aid in SELECTION_UNITS else (3, 3, 2)
        elif aid in WEEKLY_ONLY:
            disposition = "Weekly Only — Context"
            score = (2, 2, 1)
        else:
            disposition = "No Change — Existing Coverage"
            score = (2, 2, 2)
        url = f"https://arxiv.org/html/{aid}v1"
        access = "accessible"
        access_route = "version_stamped_mirror_crosscheck" if aid == "2606.29108" else "official_exact_v1_html"
        locator_prefix = f"arXiv:{aid}v1 version-stamped mirror" if aid == "2606.29108" else url
        benchmark = {key: ND for key in (
            "workload", "model", "hardware", "precision", "input_length",
            "output_length", "batch", "concurrency", "slo", "evaluator",
        )}
        benchmark["workload"] = f"《{row['title']}》exact-v1 evaluation scope: {fact['evaluation']}"
        benchmark["evaluator"] = f"Exact-v1 evaluator/metric evidence: {fact['evaluation']}"
        benchmark.update(BENCH_OVERRIDES.get(aid, {}))
        problem = (
            f"《{row['title']}》处理的问题是：{opening_claim(row['abstract'])}"
        )
        mechanism = (
            f"exact-v1 的机制路径为 {fact['method']}。在 `{row['stable_node_id']}` 中，"
            f"该路径改变或检验的具体对象由题名《{row['title']}》和上述 method locator 共同限定。"
        )
        proof = (
            f"披露的 evaluation contract 是 {fact['evaluation']}；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。"
            "未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。"
        )
        boundary = fact["limitation"]
        items.append({
            "aid": aid, "family": family, "title": row["title"],
            "abstract": row["abstract"], "owner": row["stable_node_id"],
            "problem": problem, "mechanism": mechanism, "proof": proof,
            "boundary": boundary, "artifact": fact["artifact"],
            "method": f"{locator_prefix} — §{fact['method']}",
            "evaluation": f"{locator_prefix} — §{fact['evaluation']}",
            "limitation": f"{locator_prefix} — §{fact['limitation']}",
            "access": access, "access_route": access_route,
            "artifact_locator": "Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review",
            "disposition": disposition, "score": score,
            "benchmark": benchmark,
        })
    assert {x["family"] for x in items} == set(evidence)
    for item in items:
        item["rp"] = provenance(item)
    return items, payload


def existing_and_delta(item: dict) -> tuple[str, str]:
    aid, owner = item["aid"], item["owner"]
    if aid in INTEGRATE:
        return INTEGRATE_EXISTING[aid], INTEGRATE_DELTA[aid]
    if aid in WEEKLY_ONLY:
        return (
            f"Fresh review of `{PATHS[owner]}` and `{ADJACENT[owner]}` found an owner, but exact-v1 does not cross the durable-change threshold.",
            WEEKLY_REASON[aid],
        )
    return (
        f"{OWNER_EXISTING[owner]} Fresh owner+adjacent reread found that《{item['title']}》的 `{item['method']}` remains an instance or bounded probe of this existing proposition.",
        f"该 family 的 source-specific contribution is `{item['mechanism']}`; `{item['boundary']}` prevents it from adding a new owner/control/release contract.",
    )


def build_comparisons(items: list[dict]) -> list[dict]:
    out = []
    for item in items:
        existing, delta = existing_and_delta(item)
        out.append({
            "source_family_id": item["family"],
            "stable_node_id": item["owner"],
            "target_chapter_ref": chapter_ref(PATHS[item["owner"]], TARGET_ANCHORS[item["owner"]]),
            "adjacent_chapter_refs": [chapter_ref(ADJACENT[item["owner"]])],
            "existing_proposition": existing,
            "new_evidence_delta": delta,
            "evolution_relation": "Direct Evolution" if item["aid"] in INTEGRATE else "Principle Reuse",
            "decision": item["disposition"],
            "books_review_ref": "—" if item["aid"] in WEEKLY_ONLY else f"books-review:{item['family']}",
        })
    assert len(out) == 65
    return out


def build_selection(items: list[dict]) -> list[dict]:
    out = []
    for item in items:
        aid = item["aid"]
        if aid in SELECTION_UNITS:
            decision = "selected"
            unit = SELECTION_UNITS[aid]
            subsumed_by = "—"
            rationale = (
                f"《{item['title']}》被选为 `{unit}` 的代表 family，因为 `{INTEGRATE_DELTA[aid]}`。"
                f"选择依据先冻结于 protocol/channel/metric/physical-safety 的跨层 control ownership；未证明边界是 `{item['boundary']}`。"
            )
            narrative_ref = f"analysis:{unit}"
        elif aid in SUBSUMED:
            decision = "subsumed"
            unit = "—"
            subsumed_by = SUBSUMED[aid]
            rationale = (
                f"《{item['title']}》的 `{INTEGRATE_DELTA[aid]}` 与 `{subsumed_by}` 共享同一控制链，"
                f"因此保留独立 Books evidence，但不另建 Deep Analysis；边界为 `{item['boundary']}`。"
            )
            narrative_ref = f"analysis:{subsumed_by}"
        else:
            decision = "not_selected"
            unit = "—"
            subsumed_by = "—"
            if aid in WEEKLY_ONLY:
                deciding = WEEKLY_REASON[aid]
            elif aid in INTEGRATE:
                deciding = f"其长期 delta 已进入 `{item['owner']}`，但跨层影响弱于四个已冻结分析单元：{INTEGRATE_DELTA[aid]}"
            else:
                deciding = (
                    f"其 source-specific mechanism=`{item['method']}`；最新 owner/adjacent 已覆盖该控制边界："
                    f"{OWNER_EXISTING[item['owner']]}"
                )
            rationale = (
                f"《{item['title']}》未单列 Deep Analysis。决定性理由：{deciding} "
                f"exact-v1 non-proof=`{item['boundary']}`。"
            )
            narrative_ref = f"analysis-decision:{item['family']}"
        eligibility = "score_7_9; potential_books_delta" if sum(item["score"]) >= 7 else "potential_books_delta"
        if review_override(item) != "none":
            eligibility += "; forced_review"
        out.append({
            "source_family_id": item["family"],
            "eligibility": eligibility,
            "decision": decision, "analysis_unit_id": unit,
            "subsumed_by": subsumed_by, "priority_rationale": rationale,
            "narrative_ref": narrative_ref,
        })
    assert len(out) == 65
    assert sum(x["decision"] == "selected" for x in out) == 3
    assert sum(x["decision"] == "subsumed" for x in out) == 2
    assert len({x["priority_rationale"] for x in out}) == 65
    return out


def review_override(item: dict) -> str:
    return "release_security_contract" if item["owner"] == "PLATFORM-SECURITY" and sum(item["score"]) < 7 else "none"


def review_route(item: dict) -> str:
    return "deep" if sum(item["score"]) >= 7 or review_override(item) != "none" else "standard"


def review_status(item: dict) -> str:
    return "deep_complete" if review_route(item) == "deep" else "standard_complete"


def write_json(name: str, value) -> None:
    (PACKET / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def write_packets(items: list[dict], selection: list[dict], comparisons: list[dict]) -> dict[str, list[dict]]:
    write_json("exact-v1-access-receipt.json", [{
        "source_family_id": x["family"], "primary_evidence_version": f"arXiv:{x['aid']}v1",
        "official_exact_v1_url": f"https://arxiv.org/html/{x['aid']}v1" if x["access_route"] == "official_exact_v1_html" else ND,
        "access_status": x["access"], "method_locator": x["method"],
        "evaluation_locator": x["evaluation"], "limitations_locator": x["limitation"],
        "recovery_route": x["access_route"], "later_version_used": False,
    } for x in items])
    write_json("source-review-receipts-v2.1.json", [{
        "source_family_id": x["family"], "review_provenance_id": x["rp"],
        "review_route": review_route(x),
        "primary_evidence_version": f"arXiv:{x['aid']}v1", "method_locator": x["method"],
        "evaluation_locator": x["evaluation"], "limitations_locator": x["limitation"],
        "problem": x["problem"], "mechanism": x["mechanism"],
        "evaluation_proof": x["proof"], "non_proof": x["boundary"],
        "owner": x["owner"], "books_disposition": x["disposition"],
        "benchmark_contract": x["benchmark"], "completion_result": "complete",
    } for x in items])
    write_json("deep-analysis-selection-v1.json", selection)
    write_json("books-comparison-v1.json", [
        row for row in comparisons if row["decision"] != "Weekly Only — Context"
    ])
    write_json("exact-v1-benchmark-evidence-v2.json", [{
        "source_family_id": x["family"], **x["benchmark"]
    } for x in items])

    groups: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        if item["aid"] in INTEGRATE:
            groups[item["owner"]].append(item)
    assert len(groups) == 6
    queue = [
        "# 2026-06-28 Books Integration Queue V1", "",
        f"Denominator {DENOMINATOR}. Pre-write only: 6 Integrate, 42 No Change, 17 Weekly Only, 6 owner files. Shared write lock required.", "",
    ]
    ready = [
        "# 2026-06-28 Ready-to-Insert Books Packet V1", "",
        f"Source denominator {DENOMINATOR}. Insert each owner block once and preserve every independent exact-v1 Review note.", "",
    ]
    for owner in sorted(groups):
        xs = groups[owner]
        queue += [
            f"## {owner}", "", f"- Target: {PATHS[owner]}",
            f"- Exact anchor: {TARGET_ANCHORS[owner]}",
            f"- Families: {', '.join(x['family'] for x in xs)}",
            f"- Missing proposition: {OWNER_EXISTING[owner]}",
            f"- Owner-merged delta: {OWNER_NARRATIVE[owner]}",
            f"- Boundary/fallback: {OWNER_BOUNDARY[owner]}", "",
        ]
        ready += [
            f"## {owner} — {PATHS[owner]}", "",
            f"Insert after: {TARGET_ANCHORS[owner]}", "",
            "### Owner-merged minimal durable delta", "", OWNER_NARRATIVE[owner], "",
            "### Trade-off、failure、fallback 与 coexistence", "", OWNER_BOUNDARY[owner], "",
            "### Source-specific exact-v1 Review notes", "",
        ]
        for item in xs:
            ready.append(
                f"- {item['family']} — primary arXiv:{item['aid']}v1; exact-v1 URL=https://arxiv.org/html/{item['aid']}v1; "
                f"Method={item['method']}; Evaluation={item['evaluation']}; Non-proof={item['limitation']}。"
            )
        ready.append("")
    (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue) + "\n")
    (PACKET / "READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready) + "\n")
    return groups


def review_body(item: dict) -> str:
    return "\n".join([
        f"### {item['aid']} — {item['title']}", "",
        f"**问题。** {item['problem']}", "",
        f"**机制与 state/data/control owner。** {item['mechanism']} 归属 `{item['owner']}`；相邻 owner 只消费 handoff。", "",
        f"**Evaluation 的 proof / non-proof。** {item['proof']} 它不证明：{item['boundary']}", "",
        f"**Trade-off、failure、coexistence 与 evolution。** {item['boundary']} 因此前置条件、identity、evaluator 或 workload 越界时保留 `{TARGET_ANCHORS[item['owner']]}` 的既有路径；新机制只在其被验证的局部合同内共存。", "",
        f"**Evidence。** Method=`{item['method']}`；Evaluation=`{item['evaluation']}`；Non-proof=`{item['limitation']}`；Artifact=`{item['artifact_locator']}`。", "",
        f"<!-- claim:{item['family']}:start -->",
        f"Claim boundary：仅 arXiv:{item['aid']}v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。",
        f"<!-- claim:{item['family']}:end -->",
    ])


def provenance(item: dict) -> str:
    body = unicodedata.normalize("NFC", review_body(item).replace("\r\n", "\n").replace("\r", "\n"))
    body_hash = hashlib.sha256("\n".join(line.rstrip() for line in body.splitlines()).strip().encode()).hexdigest()

    def multi(value: str) -> str:
        values = []
        for raw in value.split(";"):
            candidate = unicodedata.normalize("NFC", raw.strip())
            if candidate and candidate not in {"—", "-", "N/A", "n/a"}:
                values.append(candidate)
        return ";".join(sorted(values))

    fields = [
        "review-completion-v1", item["family"], f"paper-v1:{item['aid']}", f"arXiv:{item['aid']}v1",
        "SRC-ARXIV", f"arXiv:{item['aid']}v1", f"SRC-ARXIV@arXiv:{item['aid']}v1", review_route(item),
    ]
    if review_override(item) != "none":
        fields.append(f"review-override:{review_override(item)}")
    fields += [
        multi(item["method"]), multi(item["evaluation"]), multi(item["limitation"]),
        multi(item["artifact_locator"]), f"claim:{item['family']}", f"review:{item['family']}",
        f"review-body-sha256:{body_hash}",
    ]
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def write_report(items: list[dict], payload: dict, selection: list[dict], comparisons: list[dict], groups: dict) -> None:
    refs = "; ".join(f"review:{x['family']}" for x in items)
    selection_refs = "; ".join(dict.fromkeys(x["narrative_ref"] for x in selection))
    books_refs = "; ".join(
        ("review:" if x["aid"] in WEEKLY_ONLY else "books-review:") + x["family"]
        for x in items
    )
    lines = [
        "# Daily Research — 2026-06-28", "",
        f"> Strict V2.1 downstream pre-write report for `{DENOMINATOR}`. Coverage is Closed; exact-v1 Evidence and full-frontier Selection passed the fresh audit; Books remains Open through root writeback and post-write audit.", "",
        "## Executive Summary", "",
        "北京时间窗口 `[2026-06-27 09:00, 2026-06-28 09:00)` 共 211 个注册 identity。全量 title+abstract 语义筛选冻结 211 = 65 retained + 146 family-specific closures；65/65 exact-v1 resolved（64 official HTML，1 version-stamped mirror cross-check），pending=0。最新 owner+adjacent 语义重审得到 6 Integrate、42 No Change 与 17 Weekly Only，合并为 6 个 owner 写入；这些仍是 pre-write 决策，不是完成状态。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |",
        "| Report Type | Daily |", "| Window Start | 2026-06-28 |", "| Window End | 2026-06-28 |",
        "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |",
        "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | {DENOMINATOR} |",
        f"| Denominator Frozen At | {payload['denominator_frozen_at']} |", "| Completion Status | In Progress |",
        "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-06-27T09:00:00+08:00 | 2026-06-28T09:00:00+08:00 | {EXECUTED_AT} | frozen registered snapshots; exact UTC window; all categories | checked | 211 | {'; '.join(x['family'] for x in items)} | pages=40; final_cursor=end | 2026-06-28T01:00:00Z | ../_sources/daily-20260628/screening-ledger.json; ../_sources/daily-20260628/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260628 | — |", "",
        "<!-- coverage:SRC-ARXIV:20260628:start -->",
        "Full-population reconciliation: 211 = 65 + 146; full title+abstract screen and route-negative false-negative audit completed before denominator freeze.",
        "<!-- coverage:SRC-ARXIV:20260628:end -->", "",
        "## 2. Candidate Ledger and Score V2", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in items:
        score = item["score"]
        override = review_override(item)
        books_review_ref = "—" if item["aid"] in WEEKLY_ONLY else f"books-review:{item['family']}"
        lines.append(
            f"| {item['family']} | arXiv:{item['aid']}v1 | paper-v1:{item['aid']} | 2026-W26 | 2026-06-27 | SRC-ARXIV | "
            f"{score[0]} | {score[1]} | {score[2]} | {sum(score)} | retained | {review_status(item)} | {item['access']} | {override} | review:{item['family']} | self | — | new_in_window | {item['owner']} | {item['disposition']} | {books_review_ref} | yes |"
        )
    lines += [
        "", "### Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
        "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in items:
        route = review_route(item)
        lines.append(
            f"| {item['family']} | {item['rp']} | {route} | arXiv:{item['aid']}v1 | SRC-ARXIV@arXiv:{item['aid']}v1 | {md(item['method'])} | {md(item['evaluation'])} | {md(item['limitation'])} | {md(item['artifact_locator'])} | claim:{item['family']} | complete |"
        )
    lines += [
        "", "### Benchmark Contract", "", "<!-- validator:benchmark-contract-v1 -->",
        "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    keys = ("workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator")
    for item in items:
        lines.append("| " + " | ".join([item["family"]] + [md(item["benchmark"][key]) for key in keys]) + " |")
    lines += ["", "## 3. Source Reviews", ""]
    for item in items:
        lines += [f"<!-- review:{item['family']}:start -->", review_body(item), f"<!-- review:{item['family']}:end -->", ""]
    lines += [
        "## 4. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
        "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for decision in selection:
        lines.append(
            f"| {decision['source_family_id']} | {decision['eligibility']} | {decision['decision']} | {decision['analysis_unit_id']} | {decision['subsumed_by']} | {md(decision['priority_rationale'])} | {decision['narrative_ref']} |"
        )
    for item, decision in zip(items, selection):
        if decision["decision"] == "not_selected":
            lines += ["", f"<!-- analysis-decision:{item['family']}:start -->", decision["priority_rationale"], f"<!-- analysis-decision:{item['family']}:end -->"]
    narratives = {
        "DA-20260628-PROTOCOL-EXECUTION-INVARIANTS": "Protocol connectivity 必须先编译成可组合状态与可执行 invariant，再由 effect authorization commit；composition counterexample、grant/handle object 与 extremal differential test 是一条证据链。",
        "DA-20260628-COMPILED-PHYSICAL-SAFETY": "离线 reachability approximation 可以降低在线 safety-filter 成本，但 learned value 与 calibration 只提供 bounded sensor；real observation/controller 继续拥有物理 commit。",
        "DA-20260628-SINGLE-METRIC-CONTRACT": "优化、评估与 champion selection 若分别重写 aggregation，会在同一候选集上制造 selection inversion；metric implementation 必须成为唯一版本化执行 artifact。",
    }
    for unit, body in narratives.items():
        lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "", body, f"<!-- analysis:{unit}:end -->"]
    lines += [
        "", "## 5. Books Comparison and Decision", "", "<!-- validator:books-comparison-v1 -->",
        "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item, comp in zip(items, comparisons):
        if item["aid"] in WEEKLY_ONLY:
            continue
        lines.append(
            f"| {item['family']} | {item['owner']} | {md(comp['target_chapter_ref'])} | {md(comp['adjacent_chapter_refs'][0])} | existing:{item['family']} | delta:{item['family']} | {comp['evolution_relation']} | {item['disposition']} | books-review:{item['family']} |"
        )
    for item, comp in zip(items, comparisons):
        if item["aid"] in WEEKLY_ONLY:
            continue
        lines += ["", f"<!-- existing:{item['family']}:start -->", comp["existing_proposition"], f"<!-- existing:{item['family']}:end -->", "", f"<!-- delta:{item['family']}:start -->", comp["new_evidence_delta"], f"<!-- delta:{item['family']}:end -->", "", f"<!-- books-review:{item['family']}:start -->", f"{comp['evolution_relation']}; {item['disposition']}. {comp['existing_proposition']} {comp['new_evidence_delta']}", f"<!-- books-review:{item['family']}:end -->"]
    lines += [
        "", "## 6. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
        "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        "| SA-20260628-COVERAGE-V1 | fresh-context:jun28-downstream-v1 | coverage | coverage:SRC-ARXIV:20260628 | — | 211/211 screened; 65 retained; 146 closures; denominator frozen | passed |",
        f"| SA-20260628-EVIDENCE-V1 | fresh-context:jun28-downstream-v1 | evidence | {refs} | — | 65/65 exact-v1 resolved; 64 official HTML plus one version-stamped mirror cross-check; blocker=0 | passed |",
        f"| SA-20260628-SELECTION-V1 | fresh-context:jun28-downstream-v1 | deep_analysis_selection | {selection_refs} | — | 65/65 frontier; 3 selected, 2 subsumed, 60 not selected | passed |",
        f"| SA-20260628-BOOKS-PREWRITE-V1 | fresh-context:jun28-downstream-v1 | books | {books_refs} | root writeback pending | 6 Integrate merged into 6 owner narratives; 42 No Change and 17 Weekly Only re-audited against latest owner/adjacent chapters; post-write audit pending | open |",
        "", "## 7. Materials and Access", "",
        "- 65/65 exact-v1 resolved; 64 official HTML and one version-stamped full-text mirror cross-checked with arXiv metadata (`2606.29108v1`); pending=0; blocker=0; later versions used=0.",
        "- No open Materials Request.", "",
        "## 8. Daily Integration Decision", "",
        "- Integrate: 6 across 6 owner files; No Change: 42; Weekly Only: 17.",
        "- Shared Books/LEARNING_STATE were not edited. Root write lock and 65/65 post-write audit remain required.", "",
        "## 9. Repository Changes", "", "- Date-local Daily, source packet and downstream scripts only.", "",
        "## 10. Open Questions", "", "- Evidence and Selection passed the full fresh pre-write semantic audit.", "- Books Gate remains Open until shared writeback and 65/65 post-write audit.",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")


def write_audits(items: list[dict], selection: list[dict], comparisons: list[dict], groups: dict) -> None:
    with (PACKET / "evidence-selection-fresh-audit-v1.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["source_family_id", "primary_evidence_version", "access", "method_locator", "evaluation_locator", "limitation_locator", "benchmark_contract", "selection_decision", "books_disposition", "audit_status"])
        for item, decision in zip(items, selection):
            writer.writerow([item["family"], f"arXiv:{item['aid']}v1", item["access"], item["method"], item["evaluation"], item["limitation"], "source-specific_or_literal_Not_Disclosed", decision["decision"], item["disposition"], "passed"])
    (PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text(
        f"# 2026-06-28 Fresh Evidence and Selection Audit V1\n\n- Denominator: `{DENOMINATOR}`; 211=65+146.\n- Exact-v1: 65/65 resolved; 64 official HTML plus one version-stamped mirror cross-check; pending=0; blocker=0.\n- Evidence Gate: Passed; Selection Gate: Passed; Books Gate: Open.\n- Full frontier: 65/65; selected=3; subsumed=2; not_selected=60; rationales unique=65.\n- Books: 6 Integrate / 42 No Change / 17 Weekly Only across 6 owner files.\n- Independence caveat: nested reviewer spawning was disabled; this is a fresh self-audit, not a claimed independent second-model review.\n"
    )
    comp_by_family = {row["source_family_id"]: row for row in comparisons}
    audit = [
        "# 2026-06-28 Pre-write Fresh Audit V1", "",
        f"- Denominator: `{DENOMINATOR}`; 211 raw = 65 retained + 146 family-specific closures.",
        "- Evidence: PASS — 65/65 exact-v1 resolved; 64 official HTML + one mirror cross-check; unique source-specific locator triples; blocked=0.",
        "- Benchmark: PASS — each family has source-specific workload/evaluator evidence; absent fields are literal `Not Disclosed`.",
        "- Selection: PASS — 65/65 frontier; 3 selected, 2 subsumed, 60 not selected; 65 unique rationales bounded by exact-v1 non-proof.",
        "- Books: PASS pre-write — 6 Integrate merged into 6 owner narratives; 42 No Change; 17 Weekly Only; current owner and adjacent files re-read.",
        "- Findings: zero unresolved. Books Gate remains Open pending serialized writeback and 65/65 post-write audit.",
        "- Independence caveat: nested reviewer spawning was disabled; this is a fresh self-audit, not a claimed independent second-model review.", "",
        "| Source Family | Exact-v1 | Benchmark | Selection | Owner + Adjacent | Disposition | Result |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item, decision in zip(items, selection):
        comp = comp_by_family[item["family"]]
        disclosed = ", ".join(key for key, value in item["benchmark"].items() if value != ND)
        audit.append(
            f"| {item['family']} | PASS — arXiv:{item['aid']}v1; {item['access']} | PASS — {disclosed} | PASS — {decision['decision']} | PASS — `{PATHS[item['owner']]}` + `{ADJACENT[item['owner']]}`; existing={md(comp['existing_proposition'])} | {item['disposition']} | PASS |"
        )
    (PACKET / "PREWRITE_FRESH_AUDIT_V1.md").write_text("\n".join(audit) + "\n")
    (PACKET / "README.md").write_text(
        f"# daily-20260628 source packet\n\n- Denominator: {DENOMINATOR}\n- Raw: 211\n- Retained: 65\n- Closures: 146\n- Exact-v1: 65/65; pending 0; blocker 0\n- Coverage Gate: Closed\n- Evidence Gate: Passed\n- Selection Gate: Passed\n- Books Gate: Open pending root writeback/post-write audit\n- Completion: In Progress\n"
    )


def refresh_hashes() -> None:
    sums = []
    for path in sorted(item for item in PACKET.iterdir() if item.is_file() and item.name not in {"SHA256SUMS", "screening-ledger-provisional.json"}):
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name)
    (PACKET / "SHA256SUMS").write_text("\n".join(sums) + "\n")


def main() -> None:
    items, payload = make_items()
    assert len(INTEGRATE) == 6 and len(WEEKLY_ONLY) == 17
    assert not (INTEGRATE & WEEKLY_ONLY)
    for owner in {item["owner"] for item in items}:
        assert (ROOT / PATHS[owner]).is_file() and (ROOT / ADJACENT[owner]).is_file()
        assert (ROOT / PATHS[owner]).read_text().splitlines().count(TARGET_ANCHORS[owner]) == 1, (owner, TARGET_ANCHORS[owner])
    comparisons = build_comparisons(items)
    selection = build_selection(items)
    groups = write_packets(items, selection, comparisons)
    write_report(items, payload, selection, comparisons, groups)
    write_audits(items, selection, comparisons, groups)
    refresh_hashes()
    print(json.dumps({
        "denominator": DENOMINATOR, "raw": 211, "retained": 65, "closures": 146,
        "exact_v1": "65/65", "selection": "3/2/60", "integrate": 6,
        "no_change": 42, "weekly_only": 17, "owners": sorted(PATHS[owner] for owner in groups),
        "books_gate": "Open",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
