# Daily Research — 2026-06-02

**规范：** V3
**窗口：** 2026-06-01T09:00:00+08:00 ～ 2026-06-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T22:00:00+08:00

## 1. 结论

本窗的 V3 候选分母已经从可读 canonical packet 重新冻结：1,449 个去重身份中 110 项 Candidate、1,339 项 pre-denominator Close。旧 51 项前沿经当前门槛重审后保留 44 项、关闭 7 项；1,398 条旧 closure 在全量 title sweep 与边界 abstract 复核后恢复 66 项、维持关闭 1,332 项。旧报告另称 736 raw/28 candidates，但支撑文件均为空，因此不参与当前计数。

本次没有继承旧 `Complete` 或顶部“28/28”声明。旧报告全文已保存在 [`V2_1_EVIDENCE_ARCHIVE.md`](../_sources/daily-20260602/V2_1_EVIDENCE_ARCHIVE.md)，逐项准入、关闭理由与 fresh-context FP/FN 抽检见 [`V3_SCREENING_LEDGER.md`](../_sources/daily-20260602/V3_SCREENING_LEDGER.md)。旧 exact-v1 Method/Evaluation/Limitations 已投影到存续 44 项；新恢复的 66 项也已逐项完成当前 candidate-level evidence。110/110 Candidate 的 Evidence、Books comparison 与正文绑定均已闭合；最终结果为 75 `Existing`、32 `Integrate` 已写入正文、3 `Only report`、0 `Deferred`、0 未决 proposal。

Books trace-to-body 复核发现：17 个旧 `Integrate` 中，`SF-ORDER-AGNOSTIC-CHAIN-RULE` 未通过当前准入，采用链已经删除；其余 16 项均已完成正文绑定或由当前命题级正文明确覆盖。新恢复候选中的 20 项正文 proposal 也均由相应 owner 消费。所有写入都位于顶层 `Review notes` 之前，并保留旧方案、约束变化、状态或控制 owner、trade-off、failure/fallback 与证据边界；独立 post-write 复核未发现 trace 代替正文或 source-specific 列表式追加。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [厂商源再认证](../_sources/daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md#来源结论)：Codex 产品说明缺少长期机制增量，已关闭 | 已检查 | 无 |
| SRC-ANTHROPIC | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-META-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-QWEN | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MOONSHOT | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 同上；“全部”列表本窗无条目 | 已检查 | 无 |
| SRC-ZAI | 同上；Research 列表本窗无条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 同上；技术博客本窗无条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MINIMAX | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-ARXIV | [`canonical-raw-identity-inventory-v2.1.json.gz`](../_sources/daily-20260602/canonical-raw-identity-inventory-v2.1.json.gz) 保存 1,449 条题摘；[`canonical-semantic-screening-checkpoint-v2.1.json.gz`](../_sources/daily-20260602/canonical-semantic-screening-checkpoint-v2.1.json.gz) 保存旧 51/1,398 分层；旧 736/28 空文件不参与当前分母；当前逐项 110/1,339 结果与 FP/FN 抽检见 [`V3_SCREENING_LEDGER.md`](../_sources/daily-20260602/V3_SCREENING_LEDGER.md) | 已检查 | 无 |

对明确范围外、垂直应用或只重复成熟原则的关闭项，不为不影响处置的日期继续追查；当前来源、分母、candidate-level Evidence、Books 与独立复核 Gate 均已闭合。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Emergent Collaborative Deliberation in Multi-Model AI Systems](https://arxiv.org/abs/2606.00005v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | persona×model 分权、claim chain 与 OOS evidence 分离共识和证据；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Deliberative Curation](https://arxiv.org/abs/2606.00007v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | guarded knowledge-artifact lifecycle 与分层复核/争议协议；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Completion at the Boundary](https://arxiv.org/abs/2606.00145v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | Before/Hit/After object 将 completion proposal 与 handoff action 绑定；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW — [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Persona Attack](https://arxiv.org/abs/2606.00150v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | incremental memory injection 使风险跨 turn/implementation 累积；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [DataShield](https://arxiv.org/abs/2606.00160v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | compliance-direction probe 将 benign content 扩为 training-effect admission；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-DATA — [章节](../../../../books/part-04-training-system/27-data.md) |
| [BAGEN](https://arxiv.org/abs/2606.00198v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | prefix replay 校准 remaining-budget interval、feasibility 与 false abort；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-PLANNING — [章节](../../../../books/part-07-agent/79-planning.md) |
| [Quantized Reasoning Models Think They Need to Think Longer, but They Do Not](https://arxiv.org/abs/2606.00206v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | PTQ 引发 intermediate-correct/final-wrong 与 reasoning-token inflation；3+3+3=9 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY — [章节](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [The Deterministic Horizon](https://arxiv.org/abs/2606.00376v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 长链 state tracking 超界后将可形式化 transition 委派给 deterministic tool；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-PLANNING — [章节](../../../../books/part-07-agent/79-planning.md) |
| [SENSE](https://arxiv.org/abs/2606.00021v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 语义检索与 soft gate 改变 speculative verification contract；2+2+2=6 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [ART](https://arxiv.org/abs/2606.00024v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | value-aware accumulated-output stability 在 kernel 内终止 KV traversal；3+2+2=7 | 深入完成 | 整合：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点“Value-aware Termination 只能提前结束读取，不能接管正确性” |
| [Agreement Metrics for LLM-as-Judge Evaluation](https://arxiv.org/abs/2606.00093v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 将 scale、exclusion、abstention、pooling 与 metric 固化为可重构 measurement identity；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Judge Agreement 不是单一数字” |
| [BudgetDraft](https://arxiv.org/abs/2606.00144v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | sparse drafter/full verifier 的多 KV budget 与 acceptance-aware training；2+2+2=6 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [PrivacyPeek](https://arxiv.org/abs/2606.00152v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 隐私 gate 从输出/issue 前移到 tool response 进入 context 的 acquisition 时刻；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Tool Response 在进入 Context 时就要执行 Data-minimization Gate” |
| [Bit-Exact AI Inference Verification](https://arxiv.org/abs/2606.00279v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | software emulator 以数值路径 identity 提供跨硬件 bit-exact replay；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PR2](https://arxiv.org/abs/2606.00395v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | predicted MoE route 同时绑定 rollout behavior 与 training importance estimation；3+3+3=9 | 深入完成 | 整合：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md)；正文锚点“MoE Route Replay 也属于 Behavior-policy Identity” |
| [When Safe Skills Collide](https://arxiv.org/abs/2606.00448v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 安全对象从单 skill 扩为 installed set/capability union，并分离 static candidate 与 runtime issue；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Confused ChatGPT](https://arxiv.org/abs/2606.00485v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 共享 flat context 允许跨 app persistent write 与 confused deputy，要求 per-app isolation/mediator；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“App-local Context Namespace 阻止普通 Writer 获得跨 App Authority” |
| [TAPS](https://arxiv.org/abs/2606.00487v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | prefix reachability 与 target verification latency 联合约束 draft tree；2+2+2=6 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [“I Strongly Suspect This Website Is a Scam”](https://arxiv.org/abs/2606.00497v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | field-level endpoint outcome 揭示 detection–action gap，要求独立 issue gate；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Threshold-Based Exclusive Batching for LLM Inference](https://arxiv.org/abs/2606.00516v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | workload/hardware crossover 驱动 mixed/exclusive phase switch；3+3+2=8 | 深入完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [GNMR](https://arxiv.org/abs/2606.00539v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | operator-normalized risk 与受预算恢复路径形成低精度训练控制面；3+3+2=8 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING — [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [Same Payload, Different Channel](https://arxiv.org/abs/2606.00566v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | matched payload 隔离 channel-conditioned authority asymmetry；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Sandboxed Coding Agents are Competitive Omni-modal Task Solvers](https://arxiv.org/abs/2606.00579v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | sandbox tool transformation 修正 native modality substrate 假设；2+2+2=6 | 标准完成 | 仅报告：现有 tool/workspace contract 足以承载，离线 benchmark 未形成新 owner 机制 |
| [TRACE](https://arxiv.org/abs/2606.00611v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | risk-aware latent evidence 与独立 reader 改变长轨迹 monitor state；3+3+3=9 | 深入完成 | 整合：PLATFORM-MONITORING — [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点“Risk-aware Latent 只能压缩 Evidence，不能压缩 Authority” |
| [MemPro](https://arxiv.org/abs/2606.00619v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 整个 MCR pipeline 成为可执行、可晋升与可回滚的 versioned program；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点“Memory policy 本身也可能成为可学习、可版本化的 procedural asset” |
| [Hidden Thoughts Are Not Secret](https://arxiv.org/abs/2606.00642v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | prompt-based trace exposure 证明 hidden interface 不是 secrecy boundary；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Invitation Trap](https://arxiv.org/abs/2606.00654v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 模型主动诱导未来 trigger，使 attack provenance 跨轮闭环；3+3+2=8 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“模型建议也可能塑造未来 Trigger” |
| [Scaling Behavior of Single LLM-Driven Multi-Agent Systems](https://arxiv.org/abs/2606.00655v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 固定 base LLM 后隔离 agent count 与 coordination tax；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [NeuroLog](https://arxiv.org/abs/2606.00669v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | LLM typed facts、Datalog composition、SMT witness 与 ASan gate 分离推理 ownership；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Paradox of Outcome Optimization](https://arxiv.org/abs/2606.00674v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 因果/信息论边界解释 outcome objective 的 shortcut bias；3+2+2=7 | 深入完成 | 已有覆盖：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [WaveFilter](https://arxiv.org/abs/2606.00724v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | wavelet-guided token filtering 给 diffusion KV 压缩增加多尺度 selector；2+2+2=6 | 标准完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ViBE](https://arxiv.org/abs/2606.00735v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | workload skew 与 measured GPU service rate 联合决定 MoE placement；3+3+3=9 | 深入完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [CoMIC](https://arxiv.org/abs/2606.00756v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | edge-local history 与 cloud-owned cross-agent insight 形成双层 memory ownership；3+3+3=9 | 深入完成 | 整合：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；正文锚点“Edge-local Episode 与 Cloud-derived Guidance 必须分离所有权” |
| [FALAT](https://arxiv.org/abs/2606.00765v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | typed dependency 与 counterfactual repair 区分 first causal error 和传播步骤；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-TRACE — [章节](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety](https://arxiv.org/abs/2606.00801v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | semantic attack archive 将 red-team mode collapse 变成可观测 coverage state；3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Semantic Archive 暴露 Mode Collapse，但不拥有 Release Verdict” |
| [Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems](https://arxiv.org/abs/2606.00804v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | problem-class routing 在 consensus/debate/synthesis/single-agent 间选择控制路径；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs](https://arxiv.org/abs/2606.00813v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | attack archive 跨 release replay，阻止安全结论随版本自动继承；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SkillPager](https://arxiv.org/abs/2606.00822v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | typed skill nodes、dependency completion 与动态 budget 形成 execution-sufficient context；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md) |
| [Momento](https://arxiv.org/abs/2606.00832v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 跨 session history 必须在 consequential action 前重验当前 user state；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md) |
| [MORI](https://arxiv.org/abs/2606.00866v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | program-level relative idleness 决定 KV tier boundary 与 admission；3+3+3=9 | 深入完成 | 整合：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点“Agent Idle Window 要按 Program Horizon 决定 Tier，而不是二元搬空” |
| [MetaForge](https://arxiv.org/abs/2606.01801v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | Decide–Retrieve–Adapt–Forge 将工具候选纳入可版本化 lifecycle；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Cost-Aware Diffusion Draft Trees for Speculative Decoding](https://arxiv.org/abs/2606.01813v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | target verification cost 与 context 驱动每轮 draft-tree budget；3+2+2=7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [CRAB-Bench](https://arxiv.org/abs/2606.01815v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | constraint graph 同时拥有 task generation、多解验收与 disclosure state；3+3+3=9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Constraint Graph 可以连接任务生成与多解验收，但不能替代真实环境” |
| [Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus](https://arxiv.org/abs/2606.01828v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | reliability/divergence/relevance 在预算内选择通信 edge 与 stopping；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Benign Inputs, Harmful Outputs](https://arxiv.org/abs/2606.01837v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | joint cross-modal semantics 可由各自 benign fragments 重组 harmful intent；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Trust-Calibrated Code Review](https://arxiv.org/abs/2606.01969v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | overview/file/snippet 分层暴露 review risk cues；2+2+2=6 | 标准完成 | 仅报告：概念原型与主观 survey 尚未形成可验证 release contract |
| [SafeMCP](https://arxiv.org/abs/2606.01991v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | server-side look-ahead 在 agent 取得工具前限制 power/action set；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MMG2Skill](https://arxiv.org/abs/2606.01993v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | human guide→editable skill→trajectory diagnosis→versioned revision；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Extreme Low-Bit Quantization for Reasoning Models](https://arxiv.org/abs/2606.02011v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | trace inflation/commitment failure 使 per-token speedup 不等于端到端收益；3+3+3=9 | 深入完成 | 整合：INFER-TENSORRT-LLM — [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点“Reasoning Quantization 要验收 Commitment，而不只是 Token Cost” |
| [OpenWebRL](https://arxiv.org/abs/2606.02031v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | live-browser state、trajectory judge 与 online multi-turn RL 形成训练 identity；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [SentGuard](https://arxiv.org/abs/2606.02041v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | sentence-level semantic fence 平衡 streaming intervention 与不完整语义误拒；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Streaming Guard 的最小可解释 Commit Unit 可以是完整 Sentence” |
| [BADGER](https://arxiv.org/abs/2606.02109v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | generative structural parsing 与 deterministic scoring 分离评测 ownership；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AgentRedBench](https://arxiv.org/abs/2606.02240v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | connector/destination/argument mutation 构成 integration-aware red-team subject；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Integration-aware Campaign 必须把 Connector 与 Effect Identity 编进 Case” |
| [When Knowledge Is Not Free](https://arxiv.org/abs/2606.02245v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | evidence access tier、共享预算与 sufficiency/stop 联合进入检索状态；3+3+3=9 | 深入完成 | 整合：AGENT-RAG — [章节](../../../../books/part-07-agent/76-rag.md)；正文锚点“Evidence Access Right、Cost 与 Sufficiency 是联合检索状态” |
| [POIROT](https://arxiv.org/abs/2606.02282v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | peer interrogation 分散诊断但不形成独立 truth；2+2+2=6 | 标准完成 | 仅报告：内部 Agent 共识不能替代 independent verifier |
| [Unified Context Evolution for LLM Agents](https://arxiv.org/abs/2606.02304v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | typed Memory/Strategy/Workflow/Skill units 以 usage evidence 演进；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Do Multimodal Agents Really Benefit from Tool Use?](https://arxiv.org/abs/2606.02357v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | no-tool/call-shell/real-result 反事实区分工具确认、修复与干扰；3+3+3=9 | 深入完成 | 整合：AGENT-TOOL-CALLING — [章节](../../../../books/part-07-agent/78-tool-calling.md)；正文锚点“Tool 出现不等于 Tool 对答案有贡献” |
| [MOC](https://arxiv.org/abs/2606.02359v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | multi-order evidence stream 与 semantic-topological merge 改变消息 state；3+2+3=8 | 深入完成 | 整合：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点“多阶消息需要 Ordered Evidence DAG，而不是压平后的共识摘要” |
| [SPADE-Bench](https://arxiv.org/abs/2606.02380v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | regular/pressure 配对并比较显式 plan 与真实 tool action；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Investigating and Alleviating Harm Amplification in LLM Interactions](https://arxiv.org/abs/2606.02423v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | trajectory-prefix monitor 捕获跨 turn 逐步放大的 harm；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [HLL](https://arxiv.org/abs/2606.02449v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 动态交互 telemetry 与 family-specific rules 验证最终状态；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AgentCL](https://arxiv.org/abs/2606.02461v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | PG/SG 拆开跨任务经验的 plasticity、retention 与 interference；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md) |
| [MCP-Persona](https://arxiv.org/abs/2606.02470v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 真实 MCP trace 派生 stateful simulator 与 checkpoint/execution 双验收；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Monitoring Agentic Systems Before They’re Reliable](https://arxiv.org/abs/2606.02494v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | structural/within-run/cross-run scope 先做成熟度与 FMEA 路由；3+3+3=9 | 深入完成 | 整合：PLATFORM-MONITORING — [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点“Pre-reliability Monitoring 先验证 Wiring，再解释 Quality” |
| [Tracking the Behavioral Trajectories of Adapting Agents](https://arxiv.org/abs/2606.02536v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | versioned skill diff 上的 trait probe 只提供 promotion sensor；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SimSD](https://arxiv.org/abs/2606.02544v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | temporal causal attention 与 RoPE alignment 恢复 dLLM token verification；3+3+2=8 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点“双向 Mask Context 必须先改写成 Temporal-causal Verification Layout” |
| [Lodestar: An Online-Learning LLM Inference Router](https://arxiv.org/abs/2606.00946v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；在线路由在质量、价格与延迟反馈间更新，改变多模型推理控制面；3+3+3=9 | 深入完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Silent Failures in Federated Personalization of Foundation Models](https://arxiv.org/abs/2606.00947v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；client-local 行为不可见改变 foundation-model 评测可观测性；3+3+2=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Federated Personalization 的盲区是可见性合同” |
| [When Parallelism Pays Off: Cohesion-Aware Task Partitioning for Multi-Agent Coding](https://arxiv.org/abs/2606.00953v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；依赖内聚性成为并行 Agent 分工与合并失败的控制条件；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference](https://arxiv.org/abs/2606.01007v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；workload identity 进入 MoE 通信分组与路由协同；3+3+2=8 | 深入完成 | 已有覆盖：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Hybrid Verified Decoding: Learning to Allocate Verification in Speculative Decoding](https://arxiv.org/abs/2606.01019v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；动态分配 speculative verification 改变正确性/吞吐合同；3+3+2=8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [A Finite-Calibration Regime Map for LLM Judge Panels](https://arxiv.org/abs/2606.01034v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；有限 calibration 下 judge panel 的适用区间与报告要求；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Leyline: KV Cache Directives for Agentic Inference](https://arxiv.org/abs/2606.01065v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；Agent 生命周期意图下沉为 KV cache directive；3+3+3=9 | 深入完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Before the Model Learns the Bug:Fuzzing RLVR Verifiers](https://arxiv.org/abs/2606.01066v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；训练前 fuzz verifier reward 漏洞改变 RLVR 发布门禁；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Deep Research as Rubric for Reinforcement Learning](https://arxiv.org/abs/2606.01091v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；evidence-derived atomic rubric 改变 RL reward provenance；3+3+2=8 | 深入完成 | 整合：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md)；正文锚点“Evidence-derived Rubric 是版本化 Reward State” |
| [memorywire: A Vendor-Neutral Wire Format for Agent Memory Operations](https://arxiv.org/abs/2606.01138v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；wire format 明确 memory 读写、版本与互操作 ownership；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md) |
| [SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision](https://arxiv.org/abs/2606.01139v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；失败轨迹接入持久 skill 变更闭环；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Schedule-Level Shared-Prefix Reuse for LLM RL Training](https://arxiv.org/abs/2606.01143v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；schedule-level prefix reuse 改变 rollout/training KV 生命周期；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [When Data Is Scarce: Scaling Sparse Language Models with Repeated Training](https://arxiv.org/abs/2606.01155v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；联合 repetition、sparsity 与 effective parameters 修正 scaling 边界；3+2+3=8 | 深入完成 | 整合：TRAIN-PRETRAINING — [章节](../../../../books/part-04-training-system/28-pretraining.md)；正文锚点“数据受限的 Scaling 必须把 Unique Data 与 Repetition 分账” |
| [Low-Resource Safety Failures Are Action Failures, Not Representation Failures](https://arxiv.org/abs/2606.01196v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；安全退化定位到 action 而非 representation；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation](https://arxiv.org/abs/2606.01212v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；跨检索与生成链的 discourse manipulation 改变 RAG 威胁模型；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories](https://arxiv.org/abs/2606.01311v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；first actionable fault 与 acceptance check 约束可回退 skill 更新；2+3+3=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems](https://arxiv.org/abs/2606.01314v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；skill/tool 联合演进改变能力包状态与验证闭环；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces](https://arxiv.org/abs/2606.01317v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；stateful workspace 的操作安全门禁与 outcome/effect 验收；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability](https://arxiv.org/abs/2606.01365v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；把浪费计算追到 Agent/step 级因果链；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-MONITORING — [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Fail-Closed Lowering of Resident KV Claims onto LLM Serving Runtimes](https://arxiv.org/abs/2606.01387v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；claim identity、materialization 与 fail-closed lowering 构成 KV 合同；3+3+3=9 | 深入完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Differentially Private Datastore Generation for Retrieval-Augmented Inference](https://arxiv.org/abs/2606.01413v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；隐私预算进入检索 datastore 生成边界；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems](https://arxiv.org/abs/2606.01416v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；检测、隔离、恢复与 fallback 构成 orchestration 生命周期；2+3+2=7 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Reliable Post-Retrieval Assembly for Agent Memory: Separating Evidence Extraction from Policy Execution](https://arxiv.org/abs/2606.01435v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；分离 evidence extraction 与 policy execution；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md) |
| [An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models](https://arxiv.org/abs/2606.01462v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；离线评测与生产行为错位修正 release gate；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；多安全信号冲突要求显式 adjudication；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Move the Query, Not the Cache: Characterizing Cross-Instance Latent Attention Redistribution Across GPU Fabrics](https://arxiv.org/abs/2606.01502v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；query 移动与 cache/fabric 代价共同进入跨实例控制；3+3+3=9 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION — [章节](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems](https://arxiv.org/abs/2606.01508v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；Agent control plane 与传统 OS resource boundary 的结构映射；2+3+2=7 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Defenses &amp; Enablers For Skill Injection Attacks on Terminal Based Agents](https://arxiv.org/abs/2606.01567v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；skill 来源、执行权限与注入防护改变终端 Agent 安全边界；2+3+2=7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Don't Let a Few Network Failures Slow the Entire AllReduce](https://arxiv.org/abs/2606.01680v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；degraded-link 在线 collective 调度改变训练控制面；3+3+2=8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点“退化链路仍在线时，Collective 需要 Bandwidth-state Schedule” |
| [Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation](https://arxiv.org/abs/2606.01725v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；workload trace simulation 形成 Agent 容量规划与评测合同；3+3+2=8 | 深入完成 | 整合：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点“Task-DAG Simulator 只能校准 Capacity Plan，不能承诺线上 SLO” |
| [SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving](https://arxiv.org/abs/2606.01751v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；position-aligned segment identity 与 selective correction 改变 KV reuse；3+3+2=8 | 深入完成 | 整合：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点“非 Prefix 复用必须绑定 Position-aligned Segment 与 Correction State” |
| [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；open-ended stream 的 harness routing/evolution 构成部署控制面；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM — [章节](../../../../books/part-07-agent/84-agent-platform.md)；命题锚点“Harness Controller 是版本化策略，不是模型的隐式习惯” |
| [Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving](https://arxiv.org/abs/2606.01839v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；conversation-lifetime placement 与 KV transfer 改变调度粒度；3+3+3=9 | 深入完成 | 整合：INFER-SCHEDULING — [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点“Conversation Placement 用已观察状态替代逐 Turn 预测” |
| [Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction](https://arxiv.org/abs/2606.01850v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；compression release 同时约束 accuracy 与 calibrated uncertainty；2+3+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Compression Release 必须同时验收 Accuracy 与 Calibrated Uncertainty” |
| [Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads](https://arxiv.org/abs/2606.01927v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；scheduling/I/O overlap 与 Amdahl 边界改变并行度选择；3+3+3=9 | 深入完成 | 整合：INFER-REQUEST-LIFECYCLE — [章节](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)；正文锚点“并行扩展必须先移出不可扩展的 Host Critical Path” |
| [Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories](https://arxiv.org/abs/2606.02060v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；outcome 到 first harmful commitment 的 span 追踪改变评测粒度；3+3+3=9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Trajectory Error 需要 Span、Commitment 与 Claim Propagation 三层坐标” |
| [DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding](https://arxiv.org/abs/2606.02091v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；draft capacity 与 target verification 共同决定 diffusion speculation 成本；3+3+2=8 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING — [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点“Draft Capacity 可以借用 Target Feature，但不能借走 Commit Authority” |
| [Faster Synchronous On-Policy RL via Straggler-Aware Group Sizing](https://arxiv.org/abs/2606.02218v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；posterior straggler risk 调整同步 on-policy group size；3+3+2=8 | 深入完成 | 整合：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md)；正文锚点“同步 Group Size 也可以由 Straggler Risk 有界调节” |
| [SeClaw: Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents](https://arxiv.org/abs/2606.02302v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；从安全 spec 生成任务并保留验收边界；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses](https://arxiv.org/abs/2606.02373v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；搜索状态外置到 harness，改变 Agent/environment ownership；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-CONTEXT — [章节](../../../../books/part-07-agent/75-context.md) |
| [Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference](https://arxiv.org/abs/2606.02430v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；layer/operation/token/task propagation chain 改变故障评测；2+3+2=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“数值 Fault 要沿 Layer、Operation、Token 与 Task 观察传播” |
| [On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters](https://arxiv.org/abs/2606.02437v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；million-model deployment 改变 adapter state、存储与 serving ownership；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-MODEL-REGISTRY — [章节](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools](https://arxiv.org/abs/2606.02483v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；proposal/issue/execution 分权揭示 issue-time privacy 边界；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction](https://arxiv.org/abs/2606.02540v1) | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 不重复评分：V2.1 已处理；persistent skill 的 revision、reuse、revoke 与 sandbox 构成生命周期合同；2+3+2=7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点“Harness Backdoor 把单次写入变成跨 Run 控制状态” |

候选分母冻结为 110：44 项旧前沿存续、66 项从旧 closure 恢复；另有 7 项旧前沿降级和 1,332 项旧 closure 维持关闭。66 项恢复候选的七批 current Evidence/Books comparison 最终结果为 44 项已有覆盖、19 项正文整合、3 项仅报告；44 项旧前沿的 exact-v1 证据复用与当前正文重判见 [`V3_PRIOR_CANDIDATE_BOOKS_REJUDGMENT.md`](../_sources/daily-20260602/V3_PRIOR_CANDIDATE_BOOKS_REJUDGMENT.md)，最终结果为 31 项已有覆盖、13 项正文整合。全 110 项合计 75 `Existing`、32 `Integrate`、3 `Only report`、0 `Deferred`，无 exact-v1 access blocker 或未决 proposal。

## 4. 证据与知识整合

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_01.md`](../_sources/daily-20260602/V3_EVIDENCE_BATCH_01.md)。公开时间使用官方 2026-06-02 arXiv announcement batch 的北京时间范围；DataCite `created` 只作注册回执，不冒充首次公开时刻。

### [SENSE](https://arxiv.org/abs/2606.00021v1)

Target hidden-state retrieval 与 semantic soft gate 改变验证语义；当前 speculative-decoding 正文已明确 exact/lossy verification、matched baseline 与 exact fallback，故已有覆盖。

### [ART](https://arxiv.org/abs/2606.00024v1)

Attention kernel 依据 accumulated-output magnitude/direction stability 提前停止 KV block traversal；该增量已归并到 `INFER-KV-CACHE` 正文锚点“Value-aware Termination 只能提前结束读取，不能接管正确性”。

### [Agreement Metrics for LLM-as-Judge Evaluation](https://arxiv.org/abs/2606.00093v1)

Scale、case exclusion、abstention/invalid policy、pooling 与 metric 必须共同进入 agreement measurement identity；该增量已归并到 `PLATFORM-EVALUATION-SYSTEM` 正文锚点“Judge Agreement 不是单一数字”。

### [BudgetDraft](https://arxiv.org/abs/2606.00144v1)

Sparse drafter/full verifier 在多 KV budget 下训练并以 acceptance 对齐；现有 speculative-decoding/KV 正文已拥有 budget、acceptance、verification cost 与 fallback，故已有覆盖。

### [PrivacyPeek](https://arxiv.org/abs/2606.00152v1)

隐私审计需在 tool response 进入 model context 的 acquisition 时刻执行 scope/field admission；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“Tool Response 在进入 Context 时就要执行 Data-minimization Gate”。

### [Bit-Exact AI Inference Verification](https://arxiv.org/abs/2606.00279v1)

Software emulator 复现 arithmetic/reduction/rounding 以跨硬件生成 bit-exact replay evidence；当前 Evaluation 正文已有同名机制、coverage failure 与 tolerance fallback，故已有覆盖。

### [PR2](https://arxiv.org/abs/2606.00395v1)

Predicted route 既是 rollout behavior state，也是 training importance-estimation identity；该合同已写入 `TRAIN-GRPO` 正文“MoE Route Replay 也属于 Behavior-policy Identity”，并保留 route 缺失、expert 不可用和版本失配时的丢弃、重采或 current-policy fallback。

### [When Safe Skills Collide](https://arxiv.org/abs/2606.00448v1)

Installed skill set/capability union 才是 composition risk 对象，static scanner 只是 recall sensor；当前 Security 正文已覆盖跨-skill composition、runtime authority 与 effect boundary，故已有覆盖。

### [Confused ChatGPT](https://arxiv.org/abs/2606.00485v1)

Flat shared context 让一个 app 的 persistent write 影响另一 app 的后续 authority；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“App-local Context Namespace 阻止普通 Writer 获得跨 App Authority”。

### [TAPS](https://arxiv.org/abs/2606.00487v1)

Draft tree selection 必须服从 prefix reachability 并结算 target verification latency；现有 speculative-decoding 正文已覆盖 causal-prefix tree、cost budget 与 sequential fallback，故已有覆盖。

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_02.md`](../_sources/daily-20260602/V3_EVIDENCE_BATCH_02.md)。

### [“I Strongly Suspect This Website Is a Scam”](https://arxiv.org/abs/2606.00497v1)

Field-level endpoint outcome 与 detection–action gap 证明识别风险不等于阻止提交；当前 Security 正文已由独立 issue-time gate 承载，故已有覆盖。

### [Threshold-Based Exclusive Batching for LLM Inference](https://arxiv.org/abs/2606.00516v1)

Mixed/exclusive batching 的优劣由 hardware、model 与 workload crossover 决定；当前 Scheduling 正文已有 workload-dependent phase switch 与 fallback，故已有覆盖。

### [GNMR](https://arxiv.org/abs/2606.00539v1)

低精度训练的 operator-normalized risk、长短窗口信号与 limited recovery budget 已由 Pretraining 正文承载，故已有覆盖。

### [Same Payload, Different Channel](https://arxiv.org/abs/2606.00566v1)

相同 payload 仅因 tool/user channel 不同即产生 authority asymmetry；当前 Security 正文已要求 authenticated provenance、typed boundary 与 effect-time monitor，故已有覆盖。

### [Sandboxed Coding Agents are Competitive Omni-modal Task Solvers](https://arxiv.org/abs/2606.00579v1)

Sandboxed tool transformation 能替代部分 native modality input，但当前证据限于 offline staged tasks，未形成超出现有 tool/workspace contract 的长期机制，故仅报告。

### [TRACE](https://arxiv.org/abs/2606.00611v1)

Risk-aware latent evidence、独立 reader 与 raw-trajectory fallback 已归并到 `PLATFORM-MONITORING` 正文锚点“Risk-aware Latent 只能压缩 Evidence，不能压缩 Authority”。

### [MemPro](https://arxiv.org/abs/2606.00619v1)

重读当前 Memory 正文后改判已有覆盖：“Memory policy 本身也可能成为可学习、可版本化的 procedural asset”已经把 extraction/update procedure、source episodes、held-out validation、versioned skill bank、provenance 与 rollback 连成完整命题；后续 cluster-local tournament 又覆盖独立晋升。MemPro 是该合同的受限实现，不再新增正文。

### [Hidden Thoughts Are Not Secret](https://arxiv.org/abs/2606.00642v1)

Reasoning trace 可被 prompt 重建，说明 hidden interface 不是 secrecy boundary；当前 Security 正文已有同名机制与独立 DLP/authorization fallback，故已有覆盖。

### [The Invitation Trap](https://arxiv.org/abs/2606.00654v1)

模型先诱导用户在后续轮次输入 trigger，使 attack provenance 跨轮闭环；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“模型建议也可能塑造未来 Trigger”。

### [Scaling Behavior of Single LLM-Driven Multi-Agent Systems](https://arxiv.org/abs/2606.00655v1)

固定 base LLM 后，agent count 呈非单调收益并支付 coordination tax；当前 Multi-Agent 正文已拥有同一 budget/fallback contract，故已有覆盖。

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_03.md`](../_sources/daily-20260602/V3_EVIDENCE_BATCH_03.md)。

### [NeuroLog](https://arxiv.org/abs/2606.00669v1)

LLM 只填 typed facts，Datalog/SMT/ASan 分别拥有组合、可行性与 crash truth；当前 Security 已有同一 hypothesis-to-reproduction contract，故已有覆盖。

### [The Paradox of Outcome Optimization](https://arxiv.org/abs/2606.00674v1)

Outcome optimization 的 shortcut bias 与 process verifier 边界已由 GRPO 正文覆盖；论文提供理论与受限 counterfactual evidence，不改变 owner contract。

### [WaveFilter](https://arxiv.org/abs/2606.00724v1)

Wavelet 是 diffusion KV token-utility selector 的局部实现；当前 KV 正文已有 proxy、误差预算、loop drift 与 FullKV fallback，故已有覆盖。

### [ViBE](https://arxiv.org/abs/2606.00735v1)

Expert placement 需要联合 workload skew、measured GPU service rate 与 drift recalibration；当前 Scheduling 正文已有同一状态与静态回退，故已有覆盖。

### [CoMIC](https://arxiv.org/abs/2606.00756v1)

Edge-local episode 与 cloud-derived cross-agent guidance 分属不同 memory owner/revision；该双层异步合同已写入 `AGENT-MEMORY` 正文“Edge-local Episode 与 Cloud-derived Guidance 必须分离所有权”，并明确 dispatch receipt、tenant/expiry 与 local-only fallback。

### [FALAT](https://arxiv.org/abs/2606.00765v1)

Typed dependency 和 counterfactual repair 才能区分 first causal error 与后继传播；当前 Trace 正文已有可证伪因果候选与 multiple-candidate fallback，故已有覆盖。

### [Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety](https://arxiv.org/abs/2606.00801v1)

Semantic archive 把 attack exploration coverage 与 mode collapse 显式化；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“Semantic Archive 暴露 Mode Collapse，但不拥有 Release Verdict”。

### [Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems](https://arxiv.org/abs/2606.00804v1)

Coordination strategy 应按 problem class 与 budget 选择且保留 single-agent fallback；当前 Multi-Agent 正文已有这一长期 contract，故已有覆盖。

### [Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs](https://arxiv.org/abs/2606.00813v1)

安全结果不可随 model generation 自动继承，attack archive 应跨 release replay；当前 Evaluation/Security 已要求 immutable versioned evidence 与重跑 regression，故已有覆盖。

### [SkillPager](https://arxiv.org/abs/2606.00822v1)

Typed semantic node、query selection 与 dependency completion 将长 skill 变成 retrieval plan；当前 Memory/Context 已承载这一机制，故已有覆盖。

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_04.md`](../_sources/daily-20260602/V3_EVIDENCE_BATCH_04.md)。

### [Momento](https://arxiv.org/abs/2606.00832v1)

跨 session history 只是 current user state 的候选，不得直接授权 consequential action；当前 Memory 已有 recall/commitment 分层，故已有覆盖。

### [MORI](https://arxiv.org/abs/2606.00866v1)

Tool-call gap 的 relative idleness 应决定 program-level KV tier boundary；该增量已归并到 `INFER-KV-CACHE` 正文锚点“Agent Idle Window 要按 Program Horizon 决定 Tier，而不是二元搬空”。

### [MetaForge](https://arxiv.org/abs/2606.01801v1)

动态工具生成仍必须经过 typed artifact、isolated validation、versioned admission 与 runtime gate；当前 Agent Platform 已拥有完整 lifecycle，故已有覆盖。

### [Cost-Aware Diffusion Draft Trees for Speculative Decoding](https://arxiv.org/abs/2606.01813v1)

Draft tree 应按 target verification cost、context 与 acceptance 联合选 budget；当前 Speculative Decoding 正文已有同一 contract，故已有覆盖。

### [CRAB-Bench](https://arxiv.org/abs/2606.01815v1)

Constraint graph 同时控制 task generation、多解 materialization 与 user disclosure；该增量已归并到 `PLATFORM-EVALUATION-SYSTEM` 正文锚点“Constraint Graph 可以连接任务生成与多解验收，但不能替代真实环境”。

### [Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus](https://arxiv.org/abs/2606.01828v1)

通信 edge 和 stopping 应由可靠性、divergence、task relevance 与预算决定；当前 Multi-Agent 正文已有条件化 topology 与验证 fallback，故已有覆盖。

### [Benign Inputs, Harmful Outputs](https://arxiv.org/abs/2606.01837v1)

各模态独立 benign 不代表 joint semantics 无害；当前 Security 正文已要求 cross-modal joint-risk admission，故已有覆盖。

### [Trust-Calibrated Code Review](https://arxiv.org/abs/2606.01969v1)

三层 review UI 能改善 attention allocation，但证据仅为 prototype/survey，未验证真实漏审或 release outcome，故仅报告。

### [SafeMCP](https://arxiv.org/abs/2606.01991v1)

Look-ahead world model 只能在 server-side 提议缩小 action set，最终 authority 仍属 deterministic/effect-time gate；当前 Security/MCP 已覆盖，故已有覆盖。

### [MMG2Skill](https://arxiv.org/abs/2606.01993v1)

Human guide 编译、trajectory diagnosis 与 skill revision 必须保留 provenance、validation、admission 和 rollback；当前 Agent Platform 已承载，故已有覆盖。

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_05.md`](../_sources/daily-20260602/V3_EVIDENCE_BATCH_05.md)。

### [Extreme Low-Bit Quantization for Reasoning Models](https://arxiv.org/abs/2606.02011v1)

2-bit trace inflation、commit gap 与 loop/budget exhaustion 要进入 precision release identity；该增量已归并到 `INFER-TENSORRT-LLM` 正文锚点“Reasoning Quantization 要验收 Commitment，而不只是 Token Cost”。

### [OpenWebRL](https://arxiv.org/abs/2606.02031v1)

Live-browser rollout、trajectory judge、invalid-sample filter 与 online RL state 已由 GRPO/Agent Platform 的现有合同承载，故已有覆盖。

### [SentGuard](https://arxiv.org/abs/2606.02041v1)

Sentence boundary 是 streaming safety 的语义 commit fence；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“Streaming Guard 的最小可解释 Commit Unit 可以是完整 Sentence”。

### [BADGER](https://arxiv.org/abs/2606.02109v1)

LLM 只做结构抽取、deterministic scorer 拥有最终判定；当前 Evaluation 已有同一 ownership，故已有覆盖。

### [AgentRedBench](https://arxiv.org/abs/2606.02240v1)

SaaS connector、destination、argument/content mutation 与 fixture state 应构成同一 red-team subject；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“Integration-aware Campaign 必须把 Connector 与 Effect Identity 编进 Case”。

### [When Knowledge Is Not Free](https://arxiv.org/abs/2606.02245v1)

Evidence access right/cost tier、per-query/shared budget 与 sufficiency/stop 已合并进 `AGENT-RAG` 正文“Evidence Access Right、Cost 与 Sufficiency 是联合检索状态”；authorization 与 source authority 先于价格，预算不足时 abstain。

### [POIROT](https://arxiv.org/abs/2606.02282v1)

Peer interrogation 可生成诊断候选，但执行 Agent 的集合不能自证正确或取代独立验收，故仅报告。

### [Unified Context Evolution for LLM Agents](https://arxiv.org/abs/2606.02304v1)

Typed experience unit、usage scoring 与 retirement 已由 Memory/Agent Platform 的 versioned lifecycle 承载，故已有覆盖。

### [Do Multimodal Agents Really Benefit from Tool Use?](https://arxiv.org/abs/2606.02357v1)

Tool trace 不是贡献证据；no-tool/call-shell/real-result intervention 与 confirm/repair/harm/no-effect 归因已写入 `AGENT-TOOL-CALLING` 正文“Tool 出现不等于 Tool 对答案有贡献”。

### [MOC](https://arxiv.org/abs/2606.02359v1)

Multi-order message path、per-hop lineage、consolidation loss 与 raw-message fallback 已写入 `AGENT-MULTI-AGENT` 正文“多阶消息需要 Ordered Evidence DAG，而不是压平后的共识摘要”。

以下八项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_06.md`](../_sources/daily-20260602/V3_EVIDENCE_BATCH_06.md)。

### [SPADE-Bench](https://arxiv.org/abs/2606.02380v1)

显式 plan/self-report 只能解释意图，真实 tool action、environment transition 与 effect receipt 才能支持 deception 判定；当前 Evaluation 已有同一证据顺序，故已有覆盖。

### [Investigating and Alleviating Harm Amplification in LLM Interactions](https://arxiv.org/abs/2606.02423v1)

多轮 harm 要由跨 turn trajectory risk state 与独立 stop/authorization owner 管理；当前 Security 已有这一累计风险合同，故已有覆盖。

### [HLL](https://arxiv.org/abs/2606.02449v1)

CAPTCHA 的动态 interaction rules 是 typed action、state legality、loop 与 completion evidence 的垂直实例；当前 Evaluation 已覆盖，不将绕过能力外推为部署授权。

### [AgentCL](https://arxiv.org/abs/2606.02461v1)

顺序 task stream 必须拆开 acquisition、retention/forgetting、interference 与 transfer；当前 Memory 已有同一 checkpoint contract，故已有覆盖。

### [MCP-Persona](https://arxiv.org/abs/2606.02470v1)

Stateful MCP simulator 必须冻结 initial state、schema、checkpoint、execution outcome 与 real-environment anchor；当前 Evaluation/MCP owner 已承载，故已有覆盖。

### [Monitoring Agentic Systems Before They’re Reliable](https://arxiv.org/abs/2606.02494v1)

结构完整性应先于 task-quality monitor 成为 maturity gate，并用三种 scope、三维信号与 FMEA severity 路由发现；该增量已归并到 `PLATFORM-MONITORING` 正文锚点“Pre-reliability Monitoring 先验证 Wiring，再解释 Quality”。

### [Tracking the Behavioral Trajectories of Adapting Agents](https://arxiv.org/abs/2606.02536v1)

Trait vector 可以筛查 versioned skill diff，但不能替代独立 held-out behavior、quarantine、promotion authority 与 rollback；当前 Security 已有这条供应链边界，故已有覆盖。

### [SimSD](https://arxiv.org/abs/2606.02544v1)

dLLM 的双向 mask context 破坏标准 token-level verification，需以 temporal causal layout 与 RoPE alignment 恢复可验证 prefix；该增量已归并到 `INFER-SPECULATIVE-DECODING` 正文锚点“双向 Mask Context 必须先改写成 Temporal-causal Verification Layout”。

以下八项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_07.md`](../_sources/daily-20260602/V3_EVIDENCE_BATCH_07.md)。其中 `2606.00005v1` 无官方 HTML，使用官方 exact-v1 PDF；其余均使用 exact-v1 HTML。

### [Emergent Collaborative Deliberation in Multi-Model AI Systems](https://arxiv.org/abs/2606.00005v1)

Persona 不创造独立真值，deliberation 必须保存原始 evidence、相关性与 human/independent outcome gate；当前 Multi-Agent 已有这一 contract，故已有覆盖。

### [Deliberative Curation](https://arxiv.org/abs/2606.00007v1)

Knowledge artifact 的 guarded lifecycle、争议/撤回、独立 promotion 与 skill-conditioned reputation 已分别由 Memory、Platform 与 Multi-Agent owner 承载；投票不能自证事实，故已有覆盖。

### [Completion at the Boundary](https://arxiv.org/abs/2606.00145v1)

Completion sensor 只提交 bounded proposal，handoff 仍由 verifier、state revision 与 workflow owner 验收；当前 Workflow 已有相同分权，BPT 是 VLA 局部实现。

### [Persona Attack](https://arxiv.org/abs/2606.00150v1)

多轮 benign-seeming injection 会在 transcript/state memory 中累积风险；当前 Security 已要求跨 iteration trajectory state 与不可由模型自授的 stop/effect gate，故已有覆盖。

### [DataShield](https://arxiv.org/abs/2606.00160v1)

当前 Data 正文已用本篇 exact-v1 写入 checkpoint/layer/projection/threshold 绑定的 training-effect filter，并保留 canary 与 held-out safety regression，故已有覆盖。

### [BAGEN](https://arxiv.org/abs/2606.00198v1)

Remaining budget/feasibility interval 只是需要校准的 controller sensor；当前 Planning/Platform 已要求 hard cap、verification reserve、false-abort outcome 与 terminal receipt，故已有覆盖。

### [Quantized Reasoning Models Think They Need to Think Longer, but They Do Not](https://arxiv.org/abs/2606.00206v1)

当前 GPU Memory 已要求按完成任务的 memory/latency/energy/quality 结算低比特而非压缩比，Decode 也已有 overthinking 的 request-local intervention；marker penalty 不新增 owner contract。

### [The Deterministic Horizon](https://arxiv.org/abs/2606.00376v1)

可形式化状态可交给 deterministic solver，开放 state 仍需 observation、authorization 与 effect receipt；当前 Planning/Tool Calling 已有此边界，论文的强架构上界不作外推。

候选级证据未丢失：[`V2_1_EVIDENCE_ARCHIVE.md`](../_sources/daily-20260602/V2_1_EVIDENCE_ARCHIVE.md) 对 51 个前沿材料保存了标题、精确 v1、Method/Evaluation/Limitations locator、claim boundary、评分与旧 Books comparison。本次抽查 PRISM、Lodestar、Leyline、verifier fuzzing、SparseX、ConServe、compression uncertainty、Albireo、DFlare、SAGC、Ghost Tool Calls 与 SkillHarm，原题摘均直接研究大模型或其基础设施；同时抽查 Metastable Faults、federated-personalization taxonomy、lakehouse agents、Agent OS 等高风险 false-positive，确认仅有通用系统类比、研究议程或垂直应用不能自动保留。

对 1,398 项关闭提案已完成全量 title sweep；边界项进一步读取完整 abstract。旧共享 closure reason 被反例击穿后共恢复 66 项，现已全部闭合 candidate-level Evidence/Books comparison：43 项已有覆盖、20 项正文整合、3 项仅报告、0 项暂缓。`BitsMoE`、`CAST` 等只呈现局部模型/训练方法而没有可迁移系统合同的条目仍关闭。所有 1,332 个维持关闭项已重新落入具名的 embodied/local、incremental、benchmark、theory 或 vertical family，而不是沿用统一模板。

Books 方面，旧 `Integrate` 没有凭 trace 直接闭合：`SF-GHOST-TOOL-ISSUE-PRIVACY` 与 `SF-SKILLHARM-LIFECYCLE` 经正文重读改判 Existing，其余存续项和新恢复的长期增量均已落到唯一 owner 的 Review notes 前正文。`SF-ORDER-AGNOSTIC-CHAIN-RULE` 因当前准入关闭，整条 adoption chain 已删除。旧前沿 44 项的最终正文重判见 [`V3_PRIOR_CANDIDATE_BOOKS_REJUDGMENT.md`](../_sources/daily-20260602/V3_PRIOR_CANDIDATE_BOOKS_REJUDGMENT.md)，全量 post-write 状态见 [`POST_WRITE_AUDIT_SCOPE_V3.md`](../_sources/daily-20260602/POST_WRITE_AUDIT_SCOPE_V3.md)。

## 5. 缺口与下一步

无

本窗口没有剩余 exact-v1 access blocker、Books proposal 或待消费共享写入。`SF-ORDER-AGNOSTIC-CHAIN-RULE` 的撤回采用链和三条错误日期均已修正；后续只有跨日/跨周发现新 identity 或 primary correction 时，才按原 owner 重新打开本报告。

## 6. 复核

复核者：独立 post-write 语义复核

结论：通过

当前题摘分母复核通过：1,449 = 110 Candidate + 1,339 Close；旧前沿 51 = 44 + 7，旧 closure 1,398 = 66 + 1,332。fresh-context FP/FN 抽检没有发现新共享错误 family。110 个 Candidate 的 exact-v1 Evidence、Books comparison 与正文绑定均已闭合且没有已知 access blocker；最终 disposition 为 32 `Integrate`、75 `Existing`、3 `Only report`。32 项 Integrate 均有 Review notes 前正文锚点，未决 proposal 为 0。
