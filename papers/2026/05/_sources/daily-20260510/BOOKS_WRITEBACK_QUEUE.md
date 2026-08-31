# 2026-05-10 Books Writeback Queue

本文件是 date-local queue；本 author lane **未修改共享 Books**。root 必须按日期串行写回，并由非写作者做 post-write semantic audit。

- Queue count: 29
- Audit status: root serial writeback completed；post-write semantic audit found 29/29 content present but 19 placement violations after the first `## Review notes`；Books Gate remains Open pending relocation and re-audit

## SF-2026-ARXIV-2605-08586
- Primary: `arXiv:2605.08586v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: 实验结论需要把论文数字、实际执行、代码身份与签名收据绑定为不可抵赖的 evidence chain
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08587
- Primary: `arXiv:2605.08587v1`
- Owner: `MODEL-SELF-ATTENTION`
- Delta: 线性注意力的 recurrent state update 应由 online-regression objective 推导步长，而不是只学习无归一化更新系数
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08594
- Primary: `arXiv:2605.08594v1`
- Owner: `PLATFORM-MONITORING`
- Delta: AI accelerator 的 silent-fault sensor 可用代数测试向量保留 PE 行身份；单轮概率定位失败时必须升级到比值型两轮 fallback
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08636
- Primary: `arXiv:2605.08636v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: edge federated fine-tuning 的结论必须同时通过 quality-under-budget、cost-to-target 与 perturbation robustness，不能用 simulation 或 final accuracy 代替真实设备 deployability
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08639
- Primary: `arXiv:2605.08639v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: MoE RL 可把 rollout 已知 routing replay 提升为训练期 placement input，在 inter-batch 重排与 intra-batch replication 间分配控制权
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08647
- Primary: `arXiv:2605.08647v1`
- Owner: `AGENT-MULTI-AGENT`
- Delta: 多 Agent 可靠性必须测量约束跨 hop 生存、错误传播与 converging-DAG synthesis bottleneck，而不只看最终答案
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08678
- Primary: `arXiv:2605.08678v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: 评测 AI 发现新 ML 方法时必须冻结 evaluator 与 training knobs、限制 editable scope、复现强基线并跨 scale 验证，避免把调参或 harness hacking 计为 discovery
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08715
- Primary: `arXiv:2605.08715v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: 长轨迹评测应从 post-hoc attribution 前移到 prefix-only online audit，并把 earliest decisive error 作为可干预状态
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08717
- Primary: `arXiv:2605.08717v1`
- Owner: `AGENT-WORKFLOW`
- Delta: Agent 失败恢复应以运行 telemetry 锚定 diagnosis artifact，经 guidance gate 进入下一次尝试；wrapper 保留执行边界且不能冒充生产 recovery guarantee
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08747
- Primary: `arXiv:2605.08747v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: embodied evaluation 必须把 world completion 与 terminal commitment 分开，避免执行成功、停止失败和无证据承诺被压成同一分数
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08835
- Primary: `arXiv:2605.08835v1`
- Owner: `INFER-CONTINUOUS-BATCHING`
- Delta: diffusion serving 的 continuous batching 要联合控制 UNet throughput、VAE latency、component contention 与 queue feedback
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08838
- Primary: `arXiv:2605.08838v1`
- Owner: `AGENT-RAG`
- Delta: RAG benchmark 生成必须以受控 corpus transformation 构造可验证 answer/evidence pair，并隔离训练污染与 retrieval leakage；高分只有在冻结 corpus 与 verifier 时可解释
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08862
- Primary: `arXiv:2605.08862v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: 同步 RL 的 long-tail bubble 可作为 speculative rollout draft capacity，但必须保留 policy-version verification 与失败回退
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08876
- Primary: `arXiv:2605.08876v1`
- Owner: `PLATFORM-SECURITY`
- Delta: agent availability threat model 必须覆盖 reasoning-level cost amplification，并把 trigger optimization 与 payload optimization 分开
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08908
- Primary: `arXiv:2605.08908v1`
- Owner: `INFER-SCHEDULING`
- Delta: 共享 cache 对 accelerator request 的 admission/bypass 必须联合预测 reuse 与 deadline；core-centric locality predictor 不能拥有 accelerator deadline commit
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08913
- Primary: `arXiv:2605.08913v1`
- Owner: `INFER-DECODE`
- Delta: 端侧 decode latency 不是 context/KV 容量的单调函数；backend execution regimes 与 instrumentation perturbation 必须进入 measurement contract
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08927
- Primary: `arXiv:2605.08927v1`
- Owner: `AGENT-WORKFLOW`
- Delta: coding Agent 生成 compiler optimization 时，proof-producing translation validation 与 credible compilation 是不同 verification contracts；supervision 工时与 compile-time overhead 必须分开比较
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08962
- Primary: `arXiv:2605.08962v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: 多模态训练要把 encoder/LLM 异构并行、sample reshaping 与动态 modality workload 视为共同 runtime control problem
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-09033
- Primary: `arXiv:2605.09033v1`
- Owner: `AGENT-MEMORY`
- Delta: graph memory poisoning 会利用 relation canonicalization、anchor merge 与 retrieval channel；memory write admission 必须验证关系级 provenance
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-09126
- Primary: `arXiv:2605.09126v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: decoupled DiLoCo outer optimizer 应根据 update cosine/staleness gate 衰减，而不是把所有迟到 update 等价接收
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-09168
- Primary: `arXiv:2605.09168v1`
- Owner: `AGENT-TOOL-CALLING`
- Delta: 高风险 action commit 应咨询显式 causal graph，并用 intervention consistency 区分相关性证据与可执行因果依据
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-09204
- Primary: `arXiv:2605.09204v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: depth-parallel backprop 可通过模型原生 bounded interface 把跨 region adjoint transport 压缩为 exact suffix scan，但会牺牲表示自由度
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-09218
- Primary: `arXiv:2605.09218v1`
- Owner: `MULTIMODAL-WORLD-MODELS`
- Delta: 可编辑 3D scene memory 应把 geometry、free space、hypothetical insertion 与外部修正保存为 typed world state，并让 Agent 只通过 composable spatial tools 读写
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-09241
- Primary: `arXiv:2605.09241v1`
- Owner: `MULTIMODAL-WORLD-MODELS`
- Delta: JEPA anti-collapse regularization 应在多个低维 subspace 中约束分布，而非强迫 full ambient representation 服从 isotropic prior
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-10980
- Primary: `arXiv:2605.10980v1`
- Owner: `MULTIMODAL-GENERATIVE-PARADIGMS`
- Delta: diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-10987
- Primary: `arXiv:2605.10987v1`
- Owner: `PLATFORM-SECURITY`
- Delta: 动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-10990
- Primary: `arXiv:2605.10990v1`
- Owner: `AGENT-PLATFORM`
- Delta: skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-11002
- Primary: `arXiv:2605.11002v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: 多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-16360
- Primary: `arXiv:2605.16360v1`
- Owner: `INFER-KV-CACHE`
- Delta: 高精度 KV importance scoring 可异步交给同 family 小模型 proxy，但会增加 prefill 峰值显存并受 intra-family transfer 约束
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.
