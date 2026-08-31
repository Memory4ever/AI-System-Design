# 2026-06-28 Ready-to-Insert Books Packet V1

Source denominator daily-v2.1:2026-06-28:20c51e943aacc58d. Insert each owner block once and preserve every independent exact-v1 Review note.

## AGENT-MCP — books/part-07-agent/83-mcp.md

Insert after: ## Tool Catalog 扩大后，Discovery 与 Execution 必须分离

### Owner-merged minimal durable delta

协议连接层要再向下编译成可执行控制状态。每个 protocol 先 lowering 为可回放的有限状态 IR，组合前检查 transition 与 source/type evidence；一次 tool execution 则必须由 grant、handle、policy 与 audit objects 共同标识。Capability 或连接成功只产生 proposal，只有 host-side invariant 与 effect authorization 才能 commit。

### Trade-off、failure、fallback 与 coexistence

Pairwise finite-state composition 与十个 invariant fixtures 不证明任意多协议、生产 runtime 或 proprietary implementation 安全；IR/handle 不完整时隔离协议并回退单工具人工授权。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28690 — primary arXiv:2606.28690v1; exact-v1 URL=https://arxiv.org/html/2606.28690v1; Method=https://arxiv.org/html/2606.28690v1 — §4. The AgentThread Framework; 4.5. Composition Methodology; Evaluation=https://arxiv.org/html/2606.28690v1 — §Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup; Non-proof=https://arxiv.org/html/2606.28690v1 — §6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

## INFER-DECODE — books/part-05-inference-system/44-decode.md

Insert after: ## Decode 的结束条件

### Owner-merged minimal durable delta

Masked-diffusion decode 不必把每一步压成 token-or-mask。Request 可以为每个位置持有连续 x-prediction mixture、异步 progress 与 bounded re-edit state；只有通过 commit rule 的离散 token 才进入 visible frontier。这样 refinement 信息可跨 step 延续，而 cache、step policy 与 commit identity 仍可审计。

### Trade-off、failure、fallback 与 coexistence

连续 mixture 是否被 pretrained MDLM 正确解释只在两组模型/代码任务中验证；它增加 request state、alignment 与 kernel burden，质量或硬件不支持时回退标准 mask/unmask decoder。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-29066 — primary arXiv:2606.29066v1; exact-v1 URL=https://arxiv.org/html/2606.29066v1; Method=https://arxiv.org/html/2606.29066v1 — §Training objective; 4 Training; 4.2 Step-Size Policy Training; Evaluation=https://arxiv.org/html/2606.29066v1 — §5 Experiments; 5.3 Code Generation Evaluation; Setup; Non-proof=https://arxiv.org/html/2606.29066v1 — §7 Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

## MULTIMODAL-EMBODIED-VLA — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

Insert after: ## Safety envelope

### Owner-merged minimal durable delta

物理安全约束可以把昂贵计算移到离线：用 HJ/CBVF 近似学习安全 value 并校准，再把它编译成在线 closed-form DMP modulation。Learned value 只提供 bounded safety sensor，low-level controller 与真实 observation 仍拥有 action commit；coverage 或 calibration 越界即切回保守 controller。

### Trade-off、failure、fallback 与 coexistence

Neural HJ approximation 不是绝对 certificate，依赖已知 signed-distance specification 与离线 coverage；OOD、校准不足或 sensor drift 时停止 modulation 并交回 conservative safety controller。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28995 — primary arXiv:2606.28995v1; exact-v1 URL=https://arxiv.org/html/2606.28995v1; Method=https://arxiv.org/html/2606.28995v1 — §IV Methodology; V-A 3 CBVF Training Details; Evaluation=https://arxiv.org/html/2606.28995v1 — §III Background and Problem Setup; V Experiments; V-A Experimental Setup; Non-proof=https://arxiv.org/html/2606.28995v1 — §VI Conclusion, Limitations and Future Works；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

## PLATFORM-EVALUATION-SYSTEM — books/part-06-ai-infrastructure/66-evaluation-system.md

Insert after: ## Evaluation Run 的平台对象模型

### Owner-merged minimal durable delta

同一个 outcome metric 若在 optimizer、evaluator 与 champion selector 中分别重写，候选即使不变也会发生 selection inversion。Evaluation owner 应发布版本化 callable metric contract，让所有阶段消费同一 extraction/aggregation artifact，并保存 raw trajectory、contract revision 与可重算 verdict。

### Trade-off、failure、fallback 与 coexistence

一个 canonical metric 不能修复错误目标或缺失 trajectory；contract migration 也会改变历史可比性。Schema/semantics 不兼容时 Gate 保持 Open，并用旧 revision 对 raw evidence 重算。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-29038 — primary arXiv:2606.29038v1; exact-v1 URL=https://arxiv.org/html/2606.29038v1; Method=https://arxiv.org/html/2606.29038v1 — §2 Pipeline Architecture and Metric Aggregation Divergence; 2.4 Positioning: Pipeline Architecture as Unregistered Degrees of Freedom; Evaluation=https://arxiv.org/html/2606.29038v1 — §3.2 Controlled Aggregation Experiment (EA-2); Appendix A Experiment Parameters; Non-proof=https://arxiv.org/html/2606.29038v1 — §Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy; 6 Discussion; 7 Limitations and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

## TRAIN-DATA — books/part-04-training-system/27-data.md

Insert after: ### 从 sample provenance 到训练生命周期 lineage

### Owner-merged minimal durable delta

标注聚合不能静默删除价值分歧。Data owner 应保存 per-annotator label、annotator/threshold identity、disagreement 与 aggregation revision；majority 或 soft label 只是可重建的 materialized view。训练可消费聚合结果，但 evaluation 与 policy review 必须能恢复 contested boundary。

### Trade-off、failure、fallback 与 coexistence

三位 annotator 和单一 HateXplain/BERT slice 不能区分稳定价值阈值与标注噪声；高分歧时保留多视图或转人工，不把 minority label 自动升级为真值。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28772 — primary arXiv:2606.28772v1; exact-v1 URL=https://arxiv.org/html/2606.28772v1; Method=https://arxiv.org/html/2606.28772v1 — §3 Methods; Evaluation=https://arxiv.org/html/2606.28772v1 — §3.3 Statistical Analysis; 4 Results; Non-proof=https://arxiv.org/html/2606.28772v1 — §Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain; 4.1 Disagreement Concentrates at the Value Boundary; 4.5 Boundary Disagreement Is Not Driven by Annotation Error；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

## TRAIN-RLHF — books/part-04-training-system/31-rlhf.md

Insert after: ## Reward hacking 与 Goodhart's Law

### Owner-merged minimal durable delta

Reward-hacking 防线可以前移到 transition admission：在修改环境或 replay state 前冻结 current policy 与 return evaluator，对 current/modified policy 做 equal-budget counterfactual forecast；只有 evaluator 接受才提交 transition。模型负责 proposal，独立 evaluator 拥有 gate，原始 true-objective evidence 继续保留。

### Trade-off、failure、fallback 与 coexistence

Gate 依赖已能把 hacking trajectory 排低的 evaluator、clean seed 与额外 1.8×–4.2× 成本；evaluator misspecification 时它会接受错误 transition，需回退人工/true-objective review。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28955 — primary arXiv:2606.28955v1; exact-v1 URL=https://arxiv.org/html/2606.28955v1; Method=https://arxiv.org/html/2606.28955v1 — §3 Method; Pretraining.; Pretraining budget.; Evaluation=https://arxiv.org/html/2606.28955v1 — §Theoretical analysis.; 4 Experiments; 4.2 Main results; Non-proof=https://arxiv.org/html/2606.28955v1 — §5 Limitations and Future Work; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

