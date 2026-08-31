# 2026-06-28 Books Integration Queue V1

Denominator daily-v2.1:2026-06-28:20c51e943aacc58d. CLOSED: root wrote 6 Integrate families into 6 owners; 42 No Change and 17 Weekly Only remained unwritten; the 65/65 post-write fresh audit passed.

## AGENT-MCP

- Target: books/part-07-agent/83-mcp.md
- Exact anchor: ## Tool Catalog 扩大后，Discovery 与 Execution 必须分离
- Families: SF-2026-ARXIV-2606-28690
- Missing proposition: Ch83 已把 discovery/capability 与业务授权、effect-time policy、group admission 分开，但尚未把多协议组合和一次 execution 的 grant/handle/policy/audit 对象统一进可检查状态机。
- Owner-merged delta: 协议连接层要再向下编译成可执行控制状态。每个 protocol 先 lowering 为可回放的有限状态 IR，组合前检查 transition 与 source/type evidence；一次 tool execution 则必须由 grant、handle、policy 与 audit objects 共同标识。Capability 或连接成功只产生 proposal，只有 host-side invariant 与 effect authorization 才能 commit。
- Boundary/fallback: Pairwise finite-state composition 与十个 invariant fixtures 不证明任意多协议、生产 runtime 或 proprietary implementation 安全；IR/handle 不完整时隔离协议并回退单工具人工授权。

## INFER-DECODE

- Target: books/part-05-inference-system/44-decode.md
- Exact anchor: ## Decode 的结束条件
- Families: SF-2026-ARXIV-2606-29066
- Missing proposition: Ch44 已把 masked-diffusion refinement、frontier advancement、cache refresh 与 termination 拆成 request-local decode state，但尚未表达可连续携带且可重编辑的 token-mixture state。
- Owner-merged delta: Masked-diffusion decode 不必把每一步压成 token-or-mask。Request 可以为每个位置持有连续 x-prediction mixture、异步 progress 与 bounded re-edit state；只有通过 commit rule 的离散 token 才进入 visible frontier。这样 refinement 信息可跨 step 延续，而 cache、step policy 与 commit identity 仍可审计。
- Boundary/fallback: 连续 mixture 是否被 pretrained MDLM 正确解释只在两组模型/代码任务中验证；它增加 request state、alignment 与 kernel burden，质量或硬件不支持时回退标准 mask/unmask decoder。

## MULTIMODAL-EMBODIED-VLA

- Target: books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md
- Exact anchor: ## Safety envelope
- Families: SF-2026-ARXIV-2606-28995
- Missing proposition: Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。
- Owner-merged delta: 物理安全约束可以把昂贵计算移到离线：用 HJ/CBVF 近似学习安全 value 并校准，再把它编译成在线 closed-form DMP modulation。Learned value 只提供 bounded safety sensor，low-level controller 与真实 observation 仍拥有 action commit；coverage 或 calibration 越界即切回保守 controller。
- Boundary/fallback: Neural HJ approximation 不是绝对 certificate，依赖已知 signed-distance specification 与离线 coverage；OOD、校准不足或 sensor drift 时停止 modulation 并交回 conservative safety controller。

## PLATFORM-EVALUATION-SYSTEM

- Target: books/part-06-ai-infrastructure/66-evaluation-system.md
- Exact anchor: ## Evaluation Run 的平台对象模型
- Families: SF-2026-ARXIV-2606-29038
- Missing proposition: Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。
- Owner-merged delta: 同一个 outcome metric 若在 optimizer、evaluator 与 champion selector 中分别重写，候选即使不变也会发生 selection inversion。Evaluation owner 应发布版本化 callable metric contract，让所有阶段消费同一 extraction/aggregation artifact，并保存 raw trajectory、contract revision 与可重算 verdict。
- Boundary/fallback: 一个 canonical metric 不能修复错误目标或缺失 trajectory；contract migration 也会改变历史可比性。Schema/semantics 不兼容时 Gate 保持 Open，并用旧 revision 对 raw evidence 重算。

## TRAIN-DATA

- Target: books/part-04-training-system/27-data.md
- Exact anchor: ### 从 sample provenance 到训练生命周期 lineage
- Families: SF-2026-ARXIV-2606-28772
- Missing proposition: Ch27 已拥有 sample/transform/label provenance、license、lineage、mixture 与 admission，但尚未要求保留 per-annotator distribution 以阻止 majority label 静默取得价值边界真值。
- Owner-merged delta: 标注聚合不能静默删除价值分歧。Data owner 应保存 per-annotator label、annotator/threshold identity、disagreement 与 aggregation revision；majority 或 soft label 只是可重建的 materialized view。训练可消费聚合结果，但 evaluation 与 policy review 必须能恢复 contested boundary。
- Boundary/fallback: 三位 annotator 和单一 HateXplain/BERT slice 不能区分稳定价值阈值与标注噪声；高分歧时保留多视图或转人工，不把 minority label 自动升级为真值。

## TRAIN-RLHF

- Target: books/part-04-training-system/31-rlhf.md
- Exact anchor: ## Reward hacking 与 Goodhart's Law
- Families: SF-2026-ARXIV-2606-28955
- Missing proposition: Ch31 已解释 reward-model proxy、Goodhart、reference policy 与 reward hacking，但尚未把 equal-budget cloned-policy counterfactual 变成 transition admission gate。
- Owner-merged delta: Reward-hacking 防线可以前移到 transition admission：在修改环境或 replay state 前冻结 current policy 与 return evaluator，对 current/modified policy 做 equal-budget counterfactual forecast；只有 evaluator 接受才提交 transition。模型负责 proposal，独立 evaluator 拥有 gate，原始 true-objective evidence 继续保留。
- Boundary/fallback: Gate 依赖已能把 hacking trajectory 排低的 evaluator、clean seed 与额外 1.8×–4.2× 成本；evaluator misspecification 时它会接受错误 transition，需回退人工/true-objective review。

