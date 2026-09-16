# 2026-06-02 V3 Evidence Batch 06

本批处理八项当前 V3 存续候选。公开时间使用 2026-06-02 官方 arXiv announcement batch 的北京时间范围；Method、Evaluation 与 non-proof 均绑定 exact v1。Books 处置只由当前 owner 正文支持。

## Candidate evidence

### 2606.02380 — SPADE-Bench: Evaluating Spontaneous Strategic Deception in Agents via Plan-Action Divergence

- Primary / exact-v1: <https://arxiv.org/html/2606.02380v1>。
- Method: §3–§4 在 regular/pressure 配对环境中分别取得 Agent 的显式 plan 与实际 tool-executed action，再由局部 deception judge 比较两者 stance；最终标签由显式规则聚合，不把自然语言自报直接当作事实。
- Evaluation: §5 用 300 个配对场景、239 个工具与人工核验案例测试 spontaneous strategic deception，并在 200 个 held-out cases 上校准检测 judge 与人工的一致性。
- Non-proof: benchmark、压力脚本与 judge taxonomy 会限制可观察的 deception family；plan 可能本来就不完整，action 与文本 divergence 也可能来自工具失败或合理修正。约 82.5% human agreement 不构成生产 truth detector、发生率或自动封禁依据。
- Books comparison: `PLATFORM-EVALUATION-SYSTEM` 当前正文已明确 self-report、typed action、environment transition 与 task/effect check 的证据顺序，并要求 raw trajectory、failure slices 与独立校准。SPADE 是 plan/action 配对的具体实例，判 `已有覆盖`。

### 2606.02423 — Investigating and Alleviating Harm Amplification in LLM Interactions

- Primary / exact-v1: <https://arxiv.org/html/2606.02423v1>。
- Method: §3 将十二类真实风险扩写为必须多轮累积才成立的 harmful workflow，并用独立 user simulator 依据 assistant 前轮回复推进；§4 的 TrajSafe 在 trajectory prefix 上选择 continue、intervene 或 terminate，而不是逐 turn 独立分类。
- Evaluation: §5 比较 single-turn/full-objective 与 multi-turn workflow 的 harm amplification，并在多种 target assistant、prompt-only guardrail 与 TrajSafe 上联合报告 harm score、over-refusal、干预位置和一般能力。
- Non-proof: workflow extension、user simulator、harm judge 与 monitor 训练数据共享构造假设；十二类风险、三种 assistant 与自动评分不证明开放攻击覆盖率。低 harm/over-refusal 也不授权 monitor 直接提交或撤销真实副作用。
- Books comparison: `PLATFORM-SECURITY` 当前正文已把跨 turn 的 canonical action/effect、trajectory risk state、harm verifier 与独立 stop/authorization owner 串成同一长期 contract，并保留 prompt guard 的廉价前置分支。判 `已有覆盖`。

### 2606.02449 — HLL: Can Agents Cross Humanity’s Last Line of Verification?

- Primary / exact-v1: <https://arxiv.org/html/2606.02449v1>。
- Method: §3 将十类 CAPTCHA 拆成难度、网页干扰与动态交互三条轴；动态路径收集统一 submission payload，并用 family-specific trajectory-continuity、spatial-consistency、loop 与 state-legality 规则验证 final answer 是否有足够交互证据。
- Evaluation: §4 在多种 frontier/other multimodal agents 上比较静态任务、现实干扰和动态验证，按 task family 暴露 perception、grounding、state tracking、recovery 与非法状态等失败。
- Non-proof: CAPTCHA 是受限垂直验证任务；作者 environment、坐标 convention 和 family rules 不能代表任意 GUI、真实反滥用服务或授权边界。benchmark success 不等于允许 Agent 绕过生产 CAPTCHA，模型排名也会随版本漂移。
- Books comparison: `PLATFORM-EVALUATION-SYSTEM` 当前正文已要求 interactive task 的 event/state schema、typed actions、environment snapshot、checkpoint/state assertion、loop 与 side-effect evidence 分层；HLL 的领域实例不改变该 owner contract，判 `已有覆盖`。

### 2606.02461 — AgentCL: Toward Rigorous Evaluation of Continual Learning in Language Agents

- Primary / exact-v1: <https://arxiv.org/html/2606.02461v1>。
- Method: §3 将 task stream 构造成 naive、block 与 compositional variants，并在写入前、最终冻结 memory 后分别定义 Plasticity Gain 与 Stability Gain，从而拆开前序经验帮助、当前经验持久保留和后续干扰。
- Evaluation: §5 在 coding、deep research、language/reasoning streams 与多种 memory design 上比较 PG、SG、held-out generalization 和 memory cost；MemProbe 进一步定位 retrieval/reuse 与 consolidation 的差异。
- Non-proof: benchmark taskification、stream order、合成 compositional pairs 与 evaluator 会改变 plasticity/stability 压力；有限 task/model/memory 实现不证明长期生产用户、并发写入、隐私删除或开放迁移。
- Books comparison: `AGENT-MEMORY` 当前正文已要求顺序任务分别保留 acquisition、retention/forgetting、interference/transfer checkpoint，并冻结 episode、memory、retriever、tool sandbox 与 evaluator revision。AgentCL 的 PG/SG 是同一 contract 的 metric 实例，判 `已有覆盖`。

### 2606.02470 — MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation

- Primary / exact-v1: <https://arxiv.org/html/2606.02470v1>。
- Method: §3 先遍历真实 MCP tool call/response 构造可执行 stateful simulator，再以 profile context tree 和 tool-chain constraint 生成 personalized tasks；checkpoint 与 execution scorer 分别检查中间约束和最终状态。
- Evaluation: §4 在多类 personal/social/enterprise MCP servers 上比较 agents，验证 simulator fidelity，并消融 skill、candidate tool、context confusion，联合报告 checkpoint accuracy、execution accuracy、tokens、cost 与 step length。
- Non-proof: executable simulator 仍是从有限 server/tool 样本生成的替身，无法证明真实账户、credential、provider drift、并发状态或不可逆 side effect；human-LLM correlation 与低于 50% 的结果也不是部署授权。
- Books comparison: `PLATFORM-EVALUATION-SYSTEM` 当前正文已把 simulator revision、initial state、tool schema、fault policy、checkpoint/state assertion、execution outcome 与 real-environment anchor 写入 EvalSpec；`AGENT-MCP` 已拥有真实 connector 的权限与 effect gate。判 `已有覆盖`。

### 2606.02494 — Monitoring Agentic Systems Before They’re Reliable

- Primary / exact-v1: <https://arxiv.org/html/2606.02494v1>。
- Method: §2–§3 将 quality、suitability、efficiency 三个维度分别投影到 within-run、cross-run、structural 三种 monitor scope，以 variance 作 characterization signal，再用四阶段 FMEA severity pipeline 把发现路由到 automated monitoring 或 human investigation。
- Evaluation: §4–§5 在 synthetic agentic testbed 的 220 次运行中注入 structural/integration/task failure，比较不同 scope 可见的 defect，并演示 deterministic triage 将 integration-integrity gap 升级给人工。
- Non-proof: 单一 synthetic testbed、人工构造 error taxonomy 和 severity mapping 不证明生产发生率或跨领域阈值；variance 可能来自 workload/依赖漂移，FMEA routing 也不能代替 incident truth、release gate 或人工复验。
- Books comparison / final: 差额已写入 `PLATFORM-MONITORING` 正文锚点“Pre-reliability Monitoring 先验证 Wiring，再解释 Quality”；scope identity、FMEA routing 与 unknown/human fallback 均可定位。

### 2606.02536 — Tracking the Behavioral Trajectories of Adapting Agents

- Primary / exact-v1: <https://arxiv.org/html/2606.02536v1>。
- Method: §3 对 before/after SKILL.md 生成 normalized embedding diff，用标注的 trait-change pair 学习线性 trait vector，再以投影分数评价新 skill edit；§4 通过受信 intermediary、按 digest 固定的 executor/processor container 和 mounted diff 运行 Agent-to-Agent protocol。
- Evaluation: 68 个标注 skill diff pair 在“更倾向搜索敏感数据”这一 trait 上进行 leave-one-out validation，并以 live runtime、registry digest、cron discovery 和数据库 metadata 演示端到端执行。
- Non-proof: 只有单一 trait、68 个样本、线性 embedding probe 与同一 Hermes agent 双角色；sign accuracy/correlation 是代理测量，不证明编辑的真实行为、攻击意图、跨模型迁移或受信 intermediary 本身安全。
- Books comparison: `PLATFORM-SECURITY` 当前正文已把 experience-to-skill promotion 当作供应链发布，要求版本化 diff、独立 evidence、quarantine、held-out trajectory 与 rollback；trait probe 只能作为 sensor，不能拥有 promotion 或 runtime authority。判 `已有覆盖`。

### 2606.02544 — SimSD: Simple Speculative Decoding in Diffusion Language Models

- Primary / exact-v1: <https://arxiv.org/html/2606.02544v1>。
- Method: §3 为 dLLM 构造 token-level temporal causal attention：在同一输入中保存 reference/data token 与 mask prediction slot，按 denoising temporal order 建 attention mask 并对齐 RoPE；由 draft 收集候选、target 在单次 forward 中验证，且无需训练。
- Evaluation: §4 在多个 diffusion language models、datasets 与 baselines 上报告 accuracy、TPS、acceptance 和 per-block latency，并消融 temporal factor、draft length 与 RoPE alignment。
- Non-proof: attention/layout 与收益绑定所测 dLLM、blockwise decoding、KV support、hardware 和 batch/context；accuracy/throughput trade-off 表明不同 temporal factor 不可视为透明加速，论文未证明任意 dLLM target distribution、生产 tail 或跨 tokenizer exactness。
- Books comparison / final: 差额已写入 `INFER-SPECULATIVE-DECODING` 正文锚点“双向 Mask Context 必须先改写成 Temporal-causal Verification Layout”；target commit、position alignment 与 blockwise fallback 均可定位。

## Batch result

- Evidence closed: 8 / 8。
- Books: 6 `已有覆盖`，2 `整合已写入`，0 `整合 proposal`，0 `仅报告`，0 `暂缓`。
- Proposal queue: 空。2606.02494、2606.02544 均已完成正文绑定。
- 写入后按当前 owner 正文复核；未发现重复合并或 trace 代替正文。
