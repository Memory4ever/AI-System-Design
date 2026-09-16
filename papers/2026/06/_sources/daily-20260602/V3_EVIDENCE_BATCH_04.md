# 2026-06-02 V3 Evidence Batch 04

本批处理十项当前 V3 存续候选。公开时间使用 2026-06-02 官方 arXiv announcement batch 的北京时间范围；Method、Evaluation 与 non-proof 绑定 exact v1。Books 处置只由当前 owner 正文支持。

## Candidate evidence

### 2606.00832 — Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations

- Primary / exact-v1: <https://arxiv.org/html/2606.00832v1>。
- Method: §2 把跨 session 的 action、preference、decision 与 tool-mediated state 写入 shared memory，检索同时使用 temporal constraint、semantic ranking 和 structured condition；任务要求在 consequential action 前处理 preference update 与 stale history。
- Evaluation: §3–§4 用 161 个 multi-session service tasks、多个 assistant models、固定 user simulator，分别测 DB state、output、tool recall、Pass@k/Pass^K，并定位遗漏 verification/retrieval call 的 failure。
- Non-proof: Limitations 说明用户全由 LLM 模拟、无真人数据；单一 128K memory recipe 与服务场景不能证明真实长期用户状态、隐私治理或生产工具副作用，terminal DB state 也可能漏中间错误。
- Books comparison: `AGENT-MEMORY` 当前正文已分离 recall 与 commitment：历史偏好只是带 provenance 的候选，过期/冲突或有副作用时必须 validation/ask/abstain。Momento 是该 contract 的评测实例，判 `已有覆盖`。

### 2606.00866 — Idleness is Relative: Exploiting Tool-Call Idle Windows for Offloading in Agentic Systems with MORI

- Primary / exact-v1: <https://arxiv.org/html/2606.00866v1>。
- Method: §3–§4 把整个 agentic program 而非单 request 作为 scheduling unit，根据 tool-call gap 的连续 relative idleness 排序；cache manager 动态移动 GPU/CPU tier boundary，并在各 tier 执行 admission，而不是每次调用用二元 idle label 搬迁全部 KV。
- Evaluation: §6 在 single/multi-replica agent workloads 上比较 LRU、binary phase 与 MORI，测 cache residency、transfer、throughput/latency 和 load balancing；实验绑定作者 inference engine 与 memory hierarchy。
- Non-proof: §7 只讨论更多 tier/异构硬件扩展，未证明 remote tier、真实工具 tail、failure recovery 或多租户公平；工具时长预测错、reuse 过早与 PCIe contention 会把迁移带回 critical path。
- Books comparison / final: 差额已写入 `INFER-KV-CACHE` 正文锚点“Agent Idle Window 要按 Program Horizon 决定 Tier，而不是二元搬空”；tier admission、transfer fence 与 no-move/LRU fallback 均可定位。

### 2606.01801 — MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand

- Primary / exact-v1: <https://arxiv.org/html/2606.01801v1>。
- Method: §3 建立 Decide–Retrieve–Adapt–Forge loop：先判定是否需要工具，再检索/参数适配，缺能力时生成 Markdown spec、interface schema 与 Python script 的 executable skill；capacity-constrained pool 决定候选注册/复用。
- Evaluation: §4 与附录在 12 image-text benchmarks、16 baselines、IID/OOD tool split 上比较 accuracy、调用成功、pool evolution、延迟与消融，并分析 forged-tool reuse。
- Non-proof: Limitations 仅覆盖 programmatic image-text operation，不含 audio/video/interactive environment；效率只优化 latency，未结算金钱/context/security，forged tool validation 也不能代表真实权限与供应链安全。
- Books comparison: `AGENT-PLATFORM` 当前正文已有 trajectory/resource→typed Skill candidate、isolated validation、versioned admission、pool evolution、runtime permission/sandbox gate 与 retirement；MetaForge 的具体训练 loop 不改变 owner 边界。判 `已有覆盖`。

### 2606.01813 — Cost-Aware Diffusion Draft Trees for Speculative Decoding

- Primary / exact-v1: <https://arxiv.org/html/2606.01813v1>。
- Method: §4 不再固定 draft-tree node budget，而用 offline-profiled target verification cost、context length 与每轮 marginal acceptance 建 surrogate throughput，并利用 unimodality 在线选 budget/tree。
- Evaluation: §5 在 diffusion drafter/target、多个 benchmark/hardware 上比较 expected acceptance、verification time、end-to-end throughput，并验证 cost model、adaptive budget 与参数敏感性。
- Non-proof: 成本曲线和 unimodality 绑定作者模型、kernel、batch/context；离线 profile 漂移或 production batching 改变 verification layout 时不能继承最优 budget，论文也未给通用 tail/SLO 证明。
- Books comparison: `INFER-SPECULATIVE-DECODING` 当前正文已要求 causal-prefix reachability、accepted progress、target verification cost、tree width/depth、batch/context 与 sequential fallback 联合结算。判 `已有覆盖`。

### 2606.01815 — CRAB-Bench: Evaluating LLM Agents under Complex Task Dependencies and Human-aligned User Simulation

- Primary / exact-v1: <https://arxiv.org/html/2606.01815v1>。
- Method: §3–§4 用 constraint graph 生成含跨实体依赖和 structured distractor 的多解任务；RUSE 以 persona、信息披露、合作度等行为维度模拟非理想用户，verifier 同时检查 concrete environment state、factuality、completion 与 efficiency。
- Evaluation: §5 在 trip-booking domain 上比较 frontier agents、cooperative/realistic user，报告 pass@k/Pass^K、约束失败、信息披露和具体状态错误；多解由 graph/materialized state 而非单 reference string 验收。
- Non-proof: Limitations 仅实例化旅行预订，RUSE 仍是 LLM simulator 且只覆盖四类人类行为；未覆盖 coding/生产账户、真实支付或 evaluator common-mode error。
- Books comparison / final: 差额已写入 `PLATFORM-EVALUATION-SYSTEM` 正文锚点“Constraint Graph 可以连接任务生成与多解验收，但不能替代真实环境”；共同 identity、verifier 与 external-validity non-proof 均可定位。

### 2606.01828 — Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus

- Primary / exact-v1: <https://arxiv.org/html/2606.01828v1>。
- Method: §3–§5 每轮以 agent reliability、answer divergence 与 task relevance 为 edge value，在 budget 下选 sparse communication graph，再以动态 trust weight 聚合并在 consensus stabilization 后 early stop。
- Evaluation: §7 在数学、逻辑和事实 QA、不同 agent count/topology 上比较 quality、message/token cost 与收敛，并消融 edge selector、trust aggregation 与 stopping。
- Non-proof: §8–§9 的 reliability/trust 仍由有限任务与模型估计，homogeneous/correlated errors 可让错误共识稳定；QA 没有 tool side effect、异步 delivery、Byzantine identity 或生产 tail。
- Books comparison: `AGENT-MULTI-AGENT` 当前正文已要求 topology 服从任务 constraint/dependency graph、equal-budget Pareto admission、communication edge attribution、coordination tax 与 single-agent/central verifier fallback。判 `已有覆盖`。

### 2606.01837 — Benign Inputs, Harmful Outputs: Cross-Modal Jailbreaking via Distributed Semantic Recomposition

- Primary / exact-v1: <https://arxiv.org/html/2606.01837v1>。
- Method: §3 将 harmful intent 分解为单独看似 benign 的 text/image primitives，利用 multimodal fusion 在推理时重新组合；guardrail failure 因而发生在 joint semantic state 而非单模态 toxicity filter。
- Evaluation: §4 在多个 commercial MLLM pipelines、不同 harmful categories 与 decomposition variants 上比较 attack success/input toxicity，并对 component contribution 做消融。
- Non-proof: 只测论文披露的模型、生成任务与 judge；低输入 toxicity 不等于真实无害，商业 policy/版本会漂移，也未覆盖生产 media pipeline、adaptive defense 或现实伤害率。
- Books comparison: `PLATFORM-SECURITY` 当前正文已要求 run identity 保存 modality sequence/artifact digests，并明确各模态单独无害而 joint composition 形成风险时必须做 cross-modal guardrail/effect gate。判 `已有覆盖`。

### 2606.01969 — Trust-Calibrated Code Review: A Participatory Design Study of Review Workflows for LLM-Generated Multi-File Changes

- Primary / exact-v1: <https://arxiv.org/html/2606.01969v1>。
- Method: §4–§10 通过 participatory double-diamond process 提出 overview→file→snippet 的三层 review UI，以及 chunk、risk-per-line/file、judge、walk-through、zoom 与 security cage 等 attention cues；产物是高保真 semi-interactive prototype。
- Evaluation: 17 位 practitioner 参与发现、7 位参与设计，43 位 survey respondent 对三层 workflow 做主观可用性/预期 effort 评价；没有真实 repository review accuracy 或 defect-escape experiment。
- Non-proof: Threats 明示小样本、自选择、概念/原型而非生产工具；risk/judge signal 未校准，参与者“预期减少工作量”不证明实际节省或更少漏审。
- Books comparison: 分层展示可帮助 human review，但当前证据没有建立新的可验证 runtime/release contract；已有 Workspace/Platform 正文已要求 diff、依赖图、测试、human gate 与不可由 model confidence 接管验收。判 `仅报告`。

### 2606.01991 — SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning

- Primary / exact-v1: <https://arxiv.org/html/2606.01991v1>。
- Method: §3–§4 将可用 action set 视为 power state，由 server-side world model 在工具返回给 agent 前做 look-ahead，先过滤会扩大危险可达性的 tool，再以 immediate intervention 作为 fail-safe；训练用 environment grounding 与 dual verifiable rewards。
- Evaluation: §5 在 PowerSeeking Bench 与模拟 MCP environment 上比较 reactive guardrail、tool filtering 和 full SafeMCP，并测 utility/safety、ablation、judge consistency 与 cross-domain slice。
- Non-proof: Limitations 依赖可建模的 environment dynamics 和本地数据，跨域 prior 尚未证明；所有执行均为 synthetic sandbox/mock layer，world model 与 LLM evaluator 不能拥有真实 production authorization。
- Books comparison: `PLATFORM-SECURITY` 与 `AGENT-MCP` 当前正文已要求 capability/tool-set admission、least authority、action/effect-time reference monitor、state transition 与 fail-closed fallback；look-ahead 只能作为 proposal sensor。判 `已有覆盖`。

### 2606.01993 — MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?

- Primary / exact-v1: <https://arxiv.org/html/2606.01993v1>。
- Method: §3–§4 将 human multimodal guide 编译为 editable skill，再用 agent-visible execution trajectory 与 analyzer 诊断修订 skill file；success signal 校准后 early stop，raw guide 与 revision history保留。
- Evaluation: §5 与附录在 GUI、open-world game、card play 上比较 raw guide、constructed/revised skill、不同 revision horizon 与 analyzer stopping，并报告 step/call/token cost。
- Non-proof: Limitations 假设上游已给正确 guide，不处理发现、来源可信度或过期；固定模型/预算和 sandbox task 不证明生产 action 安全，高成本多模态 revision 也会受 API/rate limit 约束。
- Books comparison: `AGENT-PLATFORM` 当前正文已要求 raw trajectory/guide→typed skill candidate→isolated execution validation→versioned admission→supersession/retirement，并把 authoring/promotion 与 runtime gate 分开。判 `已有覆盖`。

## Batch result

- Evidence closed: 10 / 10。
- Books: 7 `已有覆盖`，2 `整合已写入`，1 `仅报告`，0 `整合 proposal`，0 `暂缓`。
- Proposal queue: 空。2606.00866、2606.01815 均已完成正文绑定。
- 写入后按当前 owner 正文复核；未发现重复合并或 trace 代替正文。
