# 2026-06-22 Ready to Insert Books V1

Only the source-specific mechanism bodies below may be serialized by root. Insert before `## Review notes`; evidence locators belong inside Review notes.

## `AGENT-CONTEXT` → `books/part-07-agent/75-context.md`

### SF-2026-ARXIV-2606-22528

把 context compaction 识别为治理控制面：安全约束、授权与 provenance 在压缩后必须由 constraint pinning/typed state 继续存在，不能依赖普通 summary 自然保留。

Failure / coexistence boundary: 攻击/防护受具体 compactor 与提示结构限制；pinning 不保证约束本身正确，也不替代 effect-time reference monitor。

Review note: arXiv:2606.22528v1; Method=§3 Compaction-Eviction Attack; §4 Constraint Pinning; Evaluation=§5 Results and Robustness; Limit=§6 Limitations.

## `AGENT-MEMORY` → `books/part-07-agent/77-memory.md`

### SF-2026-ARXIV-2606-22338

把 robot memory 评估从静态问答改为干扰条件下的 construction、retention、retrieval 与 action-use 分离；memory result 必须绑定 interference identity。

Failure / coexistence boundary: 只评一个 released checkpoint/system、单 episode condition，未覆盖多 seed 和真实机器人；不能把 benchmark pass 外推为长期可靠记忆。

Review note: arXiv:2606.22338v1; Method=§3 The Benchmark; §4 Memory Systems; Evaluation=§5 Results; Limit=§6 Limitations.

## `AGENT-WORKFLOW` → `books/part-07-agent/81-workflow.md`

### SF-2026-ARXIV-2606-22485

把 agent reasoning workflow 编译成可重放的 logical trace：tool invocation、synthesized rule 与 derived fact 都成为确定性 program，而非只保存在对话上下文。

Failure / coexistence boundary: 受测金融数据和 Vadalog rules 不证明任意工具或实时数据正确；规则错误可被确定性重放但不会自动被纠正。

Review note: arXiv:2606.22485v1; Method=§4 VADAOrchestra: System Architecture; §4.2 Orchestration Pipeline; §4.3 Logical Trace; Evaluation=§5 Experimental Evaluation; Limit=§6 Conclusion and financial-use-case boundary.

### SF-2026-ARXIV-2606-22704

patch backport workflow 要把 candidate patch、dependency/version、test oracle、semantic verification 与 human escalation 串成可回滚状态机。

Failure / coexistence boundary: benchmark tests 不证明所有语义等价或供应链安全；无法验证时应保留人工 adjudication。

Review note: arXiv:2606.22704v1; Method=§III VeriPort System and Workflow; Evaluation=§V-A Experimental Setup; §V Evaluation; Limit=§V-E Limitations.

## `INFER-PD-DISAGGREGATION` → `books/part-05-inference-system/55-pd-disaggregation.md`

### SF-2026-ARXIV-2606-22541

MoE prefill 不应把 attention、expert dispatch 与 communication 绑成同步 barrier；ASAP 以 PD disaggregation 和 asynchronous expert pipeline 重排控制流，但必须保存请求/segment/expert state identity。

Failure / coexistence boundary: 结论绑定 CANN8.3、PyTorch2.1、特定 MoE/硬件与 workload；异步 stale/misroute 或 SLO slack 耗尽时必须退回同步/隔离路径。

Review note: arXiv:2606.22541v1; Method=§3 ASAP Design; Evaluation=§5 Evaluation; Limit=§6 Discussion and Conclusion.

## `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md`

### SF-2026-ARXIV-2606-22327

把 online LLM scheduling 建模为带几何长度/剩余工作量的 admission 与排队问题；scheduler 以 workload shape 和 SLO slack 决定队列而非只按到达顺序。

Failure / coexistence boundary: 作者 workload、FP16/BF16、QPS 2–128 与队列模型不能外推到其他 engine、KV tier 或多租户优先级；估计失准需要保守 admission fallback。

Review note: arXiv:2606.22327v1; Method=§3 Geometry-Aware Online Scheduling; theoretical bound and system design; Evaluation=§4.1 Evaluation; §4 Experiments; Limit=§5 Discussion and Conclusion.

## `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md`

### SF-2026-ARXIV-2606-23743

video inference optimization 应把 graph transformation、kernel/execution plan、memory schedule 与 serving config 绑定同一可重建 artifact；agent 只能提出/搜索 plan，validator 才能提交。

Failure / coexistence boundary: 收益 instance-specific 于模型、硬件和 serving config，最终 visual quality 仍需人评；不能把单次搜索结果外推通用 engine。

Review note: arXiv:2606.23743v1; Method=§3 Sol Architecture; §4 Agent-Native Optimization; Evaluation=§5 Experiments; Limit=§6 Limitations and Future Work.

## `MODEL-MOE` → `books/part-02-model/21-moe.md`

### SF-2026-ARXIV-2606-22325

把 MoE collapse 从单一 load-balance 指标提升为 routing dynamics：多种平衡正则最终可进入相似退化吸引域，必须同时观察 expert specialization、token flow 与训练阶段。

Failure / coexistence boundary: 结论受模型规模、数据和 router family 限制；观测到共同吸引域不证明所有 MoE 必然 collapse。

Review note: arXiv:2606.22325v1; Method=§2 Problem Setup; §3 Routing Dynamics and Collapse Analysis; Evaluation=§4 Experiments; §5 Ablations; Limit=§6 Limitations.

## `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`

### SF-2026-ARXIV-2606-22729

action-only diffusion policy 可在 inference 时由 world model 预测 state，再用 temporal-logic robustness 引导采样；guidance 只约束候选，真实 observation 和 controller 保留提交权。

Failure / coexistence boundary: world-model error 会让 temporal formula 对错误 state 成立；短论文/模拟结果不证明真实机器人 safety。

Review note: arXiv:2606.22729v1; Method=§II Method; Evaluation=§III Experiments; Limit=§IV Limitations and Conclusion.

## `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`

### SF-2026-ARXIV-2606-22370

长视频生成不能无限复制完整历史 KV；按 prompt-history 相关性选择可读历史，把 cache budget、selection error 与 continuity 绑定同一运行时状态。

Failure / coexistence boundary: 只覆盖受测长单镜头生成；selection miss 会破坏长期一致性，不能外推到可交互 world state。

Review note: arXiv:2606.22370v1; Method=§3 Method; Evaluation=§4 Experiments; Limit=§5 Conclusion and long-single-shot scope.

## `MULTIMODAL-REPRESENTATION` → `books/part-03-multimodal-world-models/23-multimodal-representation.md`

### SF-2026-ARXIV-2606-22565

多模态 CoT 的收益瓶颈常在视觉 representation 而非文字 reasoning 长度；系统要分开 visual extraction、reasoning token 与最终 task evidence。

Failure / coexistence boundary: benchmark/model slice 不证明所有 modality；reasoning trace 也不等于因果使用的视觉证据。

Review note: arXiv:2606.22565v1; Method=§2 Problem Formulation; §3 Strengths and Pitfalls; §4 Shallow Visual Reflection; Evaluation=§5 Experiments; Limit=§Limitations.

## `MULTIMODAL-WORLD-MODELS` → `books/part-03-multimodal-world-models/25-multimodal-world-models.md`

### SF-2026-ARXIV-2606-22363

把 world-model video 的 physical-consistency evaluation 从 reference video 相似度拆为结构、接触与时序约束；reference-free score 只能作为 detector，不能成为环境真值。

Failure / coexistence boundary: 指标会漏掉严重结构不一致与 non-contact failure，且未验证 OpenVLA 之外泛化；必须保留真实 environment transition adjudication。

Review note: arXiv:2606.22363v1; Method=§2 Methods; Evaluation=§3 Experiments; Limit=Limitation paragraph; §4 Conclusion.

### SF-2026-ARXIV-2606-22488

开放环境 planning 需要把符号 world state 作为可演进、可修订 artifact，并把 observation→symbol update→plan→execution feedback 分开。

Failure / coexistence boundary: symbol extraction 和 transition update 仍可错，environment coverage 受限；不能把 symbolic state 当作真实环境。

Review note: arXiv:2606.22488v1; Method=§3 Method; Evaluation=§4 Experiments; Limit=Appendix A Limitations and Future Discussions.

### SF-2026-ARXIV-2606-22509

在 hierarchical RL 执行动作前，用 world model 想象候选 transition 并以 safety constraint 过滤；world model 只提议风险，真实 controller 和 fallback 持有提交权。

Failure / coexistence boundary: 手工 goal mapping、RTX3060 8GB 实验与模拟环境不能外推真实机器人或视觉泛化；model error 会产生 false-safe。

Review note: arXiv:2606.22509v1; Method=§3 ITES Method; §4 Hierarchical Safety Integration; Evaluation=§5 Experiments; Limit=§6 Limitations and Conclusion.

## `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md`

### SF-2026-ARXIV-2606-22474

把 factual verification 从所有 claim 同成本复核改为 claim-risk/uncertainty 驱动的资源分配；阈值、coverage 与 verification latency 必须联合验收。

Failure / coexistence boundary: March-2022 Wikipedia、FactScore 和 T4/256-token 生成条件限定结论；uncertainty score 未校准时不能拥有 release authority。

Review note: arXiv:2606.22474v1; Method=§3 FACTOR Method; Evaluation=§4 Experiments; Limit=§5 Limitations and Conclusion.

### SF-2026-ARXIV-2606-22633

把 verbal confidence 与内部冲突分开：模型可高置信输出但隐藏 state 对相反命题均有支持，evaluation 需要独立测 conflict geometry 和 resolution behavior。

Failure / coexistence boundary: representation probe 是诊断，不证明因果使用；不能直接成为 release gate。

Review note: arXiv:2606.22633v1; Method=§2 Method; Evaluation=§3 Experiments and Results; Limit=§Limitations.

### SF-2026-ARXIV-2606-22719

forecast benchmark 必须按 decision-time 可获得输入冻结，并以 walk-forward 防止 later-data leakage；nowcast revision 也要成为 dataset version。

Failure / coexistence boundary: 样本小、统计功效不足且金融 domain 特定；结果不能证明生产 alpha，只证明 leakage-aware protocol。

Review note: arXiv:2606.22719v1; Method=§3 Method; Evaluation=§4 Results; Limit=§5 Discussion — Limitations.

### SF-2026-ARXIV-2606-22737

stateful Agent evaluation 可由确定性 environment transition、predicate 与 event log 计算 GroundEval，而不是让 LLM judge 重新解释完整轨迹。

Failure / coexistence boundary: context mode 可观测性更弱，确定性 evaluator 也只覆盖已编码 predicate；未编码目标不会自动出现。

Review note: arXiv:2606.22737v1; Method=§3 GroundEval Framework; Evaluation=§5 Evaluation; Limit=§10 Limitations.

## `PLATFORM-GATEWAY` → `books/part-06-ai-infrastructure/62-gateway.md`

### SF-2026-ARXIV-2606-22560

第三方 LLM gateway 不能仅返回 provider name；每次路径选择要生成 evidence-bound provenance，绑定 policy、provider endpoint、fallback、请求版本与可验证 receipt。

Failure / coexistence boundary: 只覆盖受测 gateway/provider；receipt 证明公开路径与策略执行，不证明 provider 内部模型或隐藏处理。

Review note: arXiv:2606.22560v1; Method=§3 Provenance Model; §4 Gateway-Path Binding; §5 Implementation; Evaluation=§7 Evaluation; Limit=§9 Limitations and Conclusion.

## `PLATFORM-MODEL-REGISTRY` → `books/part-06-ai-infrastructure/59-model-registry.md`

### SF-2026-ARXIV-2606-22593

registry 的 release authority 不是 package presence；必须测量谁能发布、撤回、覆盖 metadata，以及 registry mediator 是否保留身份和审计链。

Failure / coexistence boundary: 公开 registry metadata 只能观察可见 authority，不证明离线凭据、组织流程或未披露 compromise。

Review note: arXiv:2606.22593v1; Method=§3 Authority Model and Measurement; §3.4 Evaluation; Evaluation=§4 Results; Limit=§5 Limitations and Discussion.

## `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md`

### SF-2026-ARXIV-2606-22311

把 privacy claim 从运行时猜测改成组件不可组装的结构性质：只有当暴露组件在既定组合规则下仍无法计算敏感谓词，系统才可声称 non-assembly；硬件隔离、阈值与允许组合必须进入证明身份。

Failure / coexistence boundary: 这是 computational、predicate-specific 保证，不是 information-theoretic secrecy；组合规则、birthmark threshold 或硬件信任根变化都会使证明失效。

Review note: arXiv:2606.22311v1; Method=§3 Architecture; §4 Formal Properties; Birthmark Standard; Evaluation=§6 Evaluation and Case Analysis; Appendix A; Limit=§7.3 Limitations; §8 Conclusion.

### SF-2026-ARXIV-2606-22413

把 AI 代码从一次生成/测试升级为 requirement→Java→formal model→多 verifier→结构化修复的闭环；LLM 只起草，proof tool 持有证据提交权。

Failure / coexistence boundary: 只证明 extraction-tractable Java profile 与三 case；formal model faithful extraction、spec completeness 和 verifier trust base 仍是边界。

Review note: arXiv:2606.22413v1; Method=§3 Approach; §3.1 Top-Down Code Synthesis; §3.2 Extraction and Verification Phases; §3.3 Closed-Loop Refinement; Evaluation=§4 Feasibility Demonstration; §4.2 Setup; §4.5 RQ3; §4.7 RQ5; Limit=§5.4 Generalisability; §5.5 Trust Boundary; §5.6 Threats to Validity.

### SF-2026-ARXIV-2606-22504

把 agent authority 从 task-wide tool visibility 改为 resource/effect/phase scoped capability：grant 生成 epoch-bound handle，trusted closure 后从下一 planner interface 移除，并在 effect 前拒绝 stale replay。

Failure / coexistence boundary: 依赖 mediated tools、sound typed catalog 与 linearizable effect-time recheck；不覆盖 bypass shell/network、compromised host 或所有工具生态。

Review note: arXiv:2606.22504v1; Method=§3 Problem and Threat Model; §4 Model of Capabilities and Interfaces; §5 Portico as a Reference Monitor; Evaluation=§6 Experimental Questions and Setup; §7 Results; Limit=§8 Discussion: Revocation Scope and External Validity.

### SF-2026-ARXIV-2606-22659

prompt-injection detector 的 calibration 要按 attack severity 与 shift slice，而不是 pooled ECE；frozen threshold 必须显示 confident false-negative risk。

Failure / coexistence boundary: pooled calibration 会隐藏严重攻击 false negative；512-token detector 与受测数据/4-bit targets 不能外推所有 tool agent。

Review note: arXiv:2606.22659v1; Method=§3 Method; Evaluation=§4 Results; Limit=§5 Discussion and Bounded Scope.

## `PLATFORM-TRACE` → `books/part-06-ai-infrastructure/69-trace.md`

### SF-2026-ARXIV-2606-22698

black-box agent forensics 需要固定 probe transcript、system-prompt/topic 条件与 attribution threshold，把模型/配置 fingerprint 当 evidence 而非身份真值。

Failure / coexistence boundary: synthetic transcript 与 threshold/config scope 限制外推；provider 更新、sampling 和 prompt drift 会使 fingerprint 失效。

Review note: arXiv:2606.22698v1; Method=§3 Approach; Evaluation=§4 Experiments; §4.3 Evaluation; Limit=§7 Limitations.

## `TRAIN-GRPO` → `books/part-04-training-system/33-grpo.md`

### SF-2026-ARXIV-2606-22570

LLM reasoning RL 的 update quality 取决于 rollout freshness、update count 与 policy drift；同一 reward 下不能把更多 optimizer steps 当成免费收益。

Failure / coexistence boundary: 单模型/任务与固定 1e-6 LR 不证明通用最优 update ratio；更少 drift 以额外 rollout 成本为代价。

Review note: arXiv:2606.22570v1; Method=§3 Analysis of Update Factors; §4 Algorithm; Evaluation=§5 Experiments; Limit=Appendix N Limitations.

### SF-2026-ARXIV-2606-22716

效率 RL 不应奖励所有短答案；correct-only adaptive reward 先冻结 correctness，再在正确轨迹中调节效率 credit，避免把错误的短输出当优化方向。

Failure / coexistence boundary: 单 scale/数据与 reward verifier 限制结论；correct-only gate 会牺牲错误样本中的潜在学习信号。

Review note: arXiv:2606.22716v1; Method=§3 Method and Reward Formalism; Evaluation=§3.3 Experimental Setup; §4 Results; Limit=§Limitations.

## `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md`

### SF-2026-ARXIV-2606-22600

on-policy distillation 的 token position 并非等权：teacher/student prefix compatibility 与序列位置共同影响 gradient；修正 bias 必须声明 density proxy 和残余 mismatch。

Failure / coexistence boundary: prefix compatibility 只是 density correction proxy；4B scale、数据与 DPO 小 10× LR/少 40× rows 构成 confound。

Review note: arXiv:2606.22600v1; Method=§3 Position-Bias Analysis; §4 Proposed Correction; Evaluation=§5 Experiments; Appendix C Protocol; Limit=Appendix E Limitations.

### SF-2026-ARXIV-2606-23740

offline reasoning training 的方法差异要同时看 weight-space trajectory、data/step/LR matching 与功能结果；几何分离若训练预算不匹配不能归因于 objective。

Failure / coexistence boundary: 单 seed/domain/checkpoint，且 DPO 用 10× smaller LR 与 40× fewer rows，构成强 confound；不能形成 objective superiority 结论。

Review note: arXiv:2606.23740v1; Method=§2 Experimental Setup; Evaluation=§3 Results; Limit=§4 Discussion; Limitations.

