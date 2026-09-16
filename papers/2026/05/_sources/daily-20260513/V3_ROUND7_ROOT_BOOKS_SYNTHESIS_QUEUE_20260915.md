# V3 Round 7 Root Books Synthesis Queue — 2026-05-13

Author evidence repair only; root must serialize these six writes and obtain a new non-author post-write review.

## 2605.11136 — EVOCHAMBER: Test-Time Co-evolution of Multi-Agent System at Individual, Team, and Population Scales

- Owner/anchor: `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md` / Participation Graph 与 Step Orchestration 是联合状态
- Current proposition: Ch82 已把 participation graph、message identity 与 orchestration state 分开，但未承载 individual/team/population 三层联合演化、非对称知识转移和 population lifecycle 的状态边界。
- Semantic delta: 把 multi-agent test-time adaptation 从各 agent 的私有 memory 扩展为三层 versioned state；specialization 依赖非对称 transfer，而 fork/merge/prune/seed 必须由 population controller 提交。
- Method: §3.1–§3.5：CODREAM 在 team failure/disagreement 后做非对称经验路由；team operators 在线选择成员与协作结构；population lifecycle 执行 fork、merge、prune 与 seed。
- Evaluation: §4.1–§4.4：competition math、code 与 multi-domain reasoning 三条任务流；Qwen3-8B 在单 H100，另用 GPT-4.1-mini；报告 accuracy/pass@1/F1 与分层 ablation。
- Limitations: Appendix A：只覆盖两个 model family；推理成本约为 single-agent 的 3.6 倍；lifecycle threshold 固定；更长流、credit attribution 和开放 population 未验证。
- Trade-off/failure: 更强跨 agent 学习换来额外推理、credit attribution、population churn、错误 transfer 与 specialization collapse。
- Fallback/coexistence: 短任务、固定团队或 lifecycle evidence 不足时，保留静态 team、局部 memory 和人工/确定性成员管理。
- Artifact: https://github.com/Mercury7353/EvoChamber；未确认与 exact-v1 绑定的 immutable commit。

## 2605.11167 — The Bicameral Model: Bidirectional Hidden-State Coupling Between Parallel Language Models

- Owner/anchor: `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md` / Latent Communication 只能压缩 Payload，不能隐藏 Identity
- Current proposition: Ch82 已要求 latent handoff 保留 identity、version 和 commitment boundary，但未覆盖两个模型逐 token lockstep、双向 hidden-state coupling、suppression gate 与 tool causality 的联合 contract。
- Semantic delta: latent channel 成为同步通信 plane：interface 只拥有 payload transform/gate，两个 frozen LM 各自拥有生成 state，tool runtime 仍拥有 effect commit；causal schedule 必须显式版本化。
- Method: §2.1–§2.4：两个 LM lockstep generation；neural interface 双向变换 hidden state，以 learned suppression gate 注入 residual，并对 tool output 维持因果放置。§3 只训练 interface。
- Evaluation: §4：calculator 与 Z3 两个 tool-use domain，比较独立模型、文本交流和 learned interface；§5 分析 gate 与 communication pattern。
- Limitations: §5.4：双模型推理成本可能近似翻倍；GSM8K 在狭小 capability gap 下由 49.6 降至约 40；训练需要 task-specific causal placement annotation。
- Trade-off/failure: 降低文本通信开销但增加双模型 compute、同步阻塞、hidden-state coupling、不可解释通信和负迁移。
- Fallback/coexistence: 能力互补或因果标注不足时，回退显式 typed message/handoff、异步协作或单模型 tool loop。
- Artifact: Not Disclosed：未找到与 exact-v1 绑定的公开 repository 或 immutable commit。

## 2605.11169 — OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents

- Owner/anchor: `AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md` / 执行后行为只能更新下一次 Intent Gate
- Current proposition: Ch78 已规定执行结果只能更新下一次 intent proposal，authorizer/effect runtime 保留 commit authority；但未承载 frozen reasoner 之后的 per-action online statistics、UCB exploration 和 deployment-time decision-layer state。
- Semantic delta: 把 tool proposal policy 拆成可在线学习的 bandit state；feedback 更新 selector 而非 retrospective authorization，UCB uncertainty 只决定探索优先级，不能越过 permission/effect gate。
- Method: §4–§5：reasoner hidden state 作为 context；每个 action 保存线性 bandit sufficient statistics；UCB 同时估计 expected reward 与 uncertainty，以 rank-one update 吸收在线反馈。
- Evaluation: §6：ToolBench、TaskBench、TaskBench-MM 与 BFCL；Qwen3-4B 和 Mistral-7B fixed；以 reference completion 转换的 tool-multiset F1 比较 fixed selection 与 OLIVIA。
- Limitations: 无独立 Limitations。tool-multiset F1 不证明 effect success、permission safety 或生产 tail；开放 action space、non-stationary/adversarial feedback 和 unsafe exploration 未覆盖。
- Trade-off/failure: 适应环境变化但引入冷启动、unsafe exploration、reward poisoning、per-action state 膨胀和 non-stationary regret。
- Fallback/coexistence: 高风险 action、反馈不可归因或 action space 快速变化时，回退 frozen policy、allowlist、offline evaluation 和显式审批。
- Artifact: Not Disclosed：未确认公开代码或与 exact-v1 绑定的 immutable artifact。

## 2605.11225 — PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement

- Owner/anchor: `AGENT-PLANNING` → `books/part-07-agent/79-planning.md` / Replanning 的触发条件
- Current proposition: Ch79 已有 observation-triggered replan、局部 replan 后的全约束复核和 completion evidence，但未把 accepted trajectory 作为 incumbent state，也未定义 backward discrepancy、suffix replacement 与 monotonic acceptance。
- Semantic delta: replanning 从重新生成变成带版本与接受准则的 trajectory optimization：executor 提供观测，inspector 提出 discrepancy，evolver 只修改局部 suffix，verifier 独占 commit。
- Method: §3：PLAN→INSPECT→EVOLVE→VERIFY；inspection 从 execution trace 生成 backward discrepancy/textual gradient，evolution 做 localized trajectory repair，acceptance 保持 incumbent 的 monotonicity。
- Evaluation: §4：DeepPlanning 与 GAIA；每个 domain 120 tasks；报告 composite/case metrics、token proxy、迭代收益和 component ablation。
- Limitations: 工具能力限制上界；GAIA basic toolkit 会使部分 refinement 退化为 retry；未直接测量 latency，token 只是 proxy；human-in-the-loop 上界不是 autonomous result。
- Trade-off/failure: 可定位失败并保留已验证 prefix，但增加执行、inspection、版本比较与 verifier 成本；错误 textual gradient 会稳定优化错误方向。
- Fallback/coexistence: 工具弱、验证不可靠或迭代预算耗尽时，回退从 checkpoint 全局 replan、保守 retry 或人工接管。
- Artifact: Not Disclosed：未确认与 exact-v1 绑定的公开代码或 immutable commit。

## 2605.11996 — BadSKP: Backdoor Attacks on Knowledge Graph-Enhanced LLMs with Soft Prompts

- Owner/anchor: `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` / Embedding 也是可执行数据供应链的一部分
- Current proposition: Ch72 已将 embedding、prompt 和 model artifact 纳入供应链，并要求 provenance/identity，但未明确 KG-derived continuous soft prompt 作为旁路 conditioning channel，也未覆盖 graph-space semantic anchoring attack。
- Semantic delta: 安全 identity 必须绑定 KG snapshot、graph encoder/projector 与 model revision；soft prompt 只是 untrusted conditioning payload，semantic anchor 只能作 sensor，policy/effect gate 保留 authority。
- Method: §III–§V：定义可修改上游 KG 的 attacker；用 semantic anchoring 维持表面任务相似，再分阶段优化 graph-level representation 与 soft-prompt effect。
- Evaluation: §VI：两类 KG-enhanced soft-prompt system、四个 dataset 与多种 backbone/attack/defense setting；报告 attack success、clean utility 与 defense response。
- Limitations: 无独立 Limitations。结论依赖攻击者可接触上游 KG、两个系统族及所测 dataset/backbone；不证明生产 prevalence 或 semantic-anchor detector 能普遍防御。
- Trade-off/failure: 图知识提升条件化能力却引入不可见 payload、projector drift、poisoned relation propagation 和检测器被规避。
- Fallback/coexistence: provenance 缺失、graph drift 或 detector 不确定时，禁用 soft channel，回退 signed snapshot、文本化可审计 evidence 或隔离模型版本。
- Artifact: Not Disclosed：未确认与 exact-v1 绑定的公开 repository/commit。

## 2605.12477 — MEME: Multi-entity &amp; Evolving Memory Evaluation

- Owner/anchor: `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` / 动态知识系统需要关系型回归，而不只是静态答案分数
- Current proposition: Ch66 已指出删除不是沉默、动态关系需回归，并区分 evidence 与 answer；但未形成 multi-entity evolving memory 的 Deletion/Cascade/Absence 三轴合同及 stage-diagnostic intervention。
- Semantic delta: 评估对象从单条 memory hit 扩展为 versioned entity-relation state；retriever、memory updater 和 answerer 分阶段验收，Cascade/Absence 让依赖传播与无证据拒答成为独立 release gate。
- Method: §3.1 定义 Deletion、Cascade、Absence 三类任务；§3.2 用有时间顺序的多实体 KG 生成 episode/dialog，并保留依赖关系与 expected state。
- Evaluation: §4：六个 memory system、三类 paradigm、100 episodes 与约 35k tokens；分别报告 retrieval/final-answer 及 intervention sweep，以区分 stage failure。
- Limitations: §6：只有两个 handcrafted KG、LLM-generated dialogue、100 episodes、约 35K tokens；多项 ablation 只用小子集且仅英语。
- Trade-off/failure: 更能暴露关系错误，却增加 KG/episode 构造、时间真值、干预实验与 evaluator 成本；合成对话可能把生成器偏差写入基准。
- Fallback/coexistence: 领域关系或时间真值不可验证时，保留静态 recall 基线但降级声明，并用人工审计/append-only provenance 验收关键变化。
- Artifact: https://seokwonjung-jay.github.io/meme-eval/；项目页提供 code/data，但未确认与 exact-v1 绑定的 immutable commit。
