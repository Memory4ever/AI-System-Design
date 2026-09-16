# Daily Research — 2026-07-22

**规范：** V3
**窗口：** 2026-07-21T09:00:00+08:00 ～ 2026-07-22T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T17:30:00+08:00

## 1. 结论

本窗口按 first-public owner 得到 495 条 arXiv 原始身份。逐条读取标题与完整摘要后，冻结 13 个候选；旧稿的 96 个候选不作为新分母，其中 83 个旧候选因只提供局部方法/benchmark、垂直应用或没有改变长期系统判断而降回准入前关闭。原始证据保留，但不在正文候选表继续制造重要性错觉。

保留材料集中在可迁移状态、训练/推理执行计划、跨层资源约束、证据与安全边界。每项都已用旧稿保存的 exact-v1 primary evidence 重新核对机制与反证；没有用标题关键字替代语义判断，也没有把能映射 ROADMAP 当作准入理由。独立复核已经把“来源存在”和“正文已承载”分开，并确认两项相邻材料已合并进入同一 control-plane owner，而不是在 Books 中形成重复分支。

## 2. 来源覆盖

当前登记的机构日源在 2026-09-07 才纳入合同；按历史生效边界不倒推本窗口。表中仍逐项列出，避免把‘不适用’误读为已扫描。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ANTHROPIC | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-GOOGLE-AI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-META-AI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-QWEN | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-DEEPSEEK | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-MOONSHOT | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ZAI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-MINIMAX | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ARXIV | [exact-v1 HTML](https://arxiv.org/)；本窗 495 条 identity 逐条 title + 完整摘要语义筛选；旧稿 exact-v1 Method / Evaluation / Limitations 仅作可核实证据种子 | 已检查 | 无 |

本次排除 AI for Science、纯垂直应用、只改局部任务指标以及没有系统状态/控制/评价契约增量的工作。withdrawn 身份不进入候选；本组没有保留 withdrawn family。

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；7～9 分深入审阅，5～6 分标准审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Beyond Accuracy and Cost: Latency-Aware LLM Query Routing for Dynamic Workloads](https://arxiv.org/html/2607.18253v1) | 2026-07-22T08:00:00+08:00 | `INFER-SCHEDULING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Interactive Training 2: Auditable Control Plane for Live Model Training](https://arxiv.org/html/2607.18314v1) | 2026-07-22T08:00:00+08:00 | `PLATFORM-TRAINING-OPERATOR`；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-TRAINING-OPERATOR，[目标章](../../../../books/part-06-ai-infrastructure/60-training-operator.md) |
| [Decode-Time Grammars: Constrained LLM Generation over a Refinement Order of Grammar Fragments](https://arxiv.org/html/2607.18357v1) | 2026-07-22T08:00:00+08:00 | `MODEL-SAMPLING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report](https://arxiv.org/html/2607.18367v1) | 2026-07-22T08:00:00+08:00 | `MULTIMODAL-WORLD-MODELS`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving](https://arxiv.org/html/2607.18631v1) | 2026-07-22T08:00:00+08:00 | `INFER-SCHEDULING`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md) 已有 realizability→probe→ranking 正文 |
| [DWM: Separating World Effects from Actions in Latent World Models](https://arxiv.org/html/2607.18715v1) | 2026-07-22T08:00:00+08:00 | `MULTIMODAL-WORLD-MODELS`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning](https://arxiv.org/html/2607.18722v1) | 2026-07-22T08:00:00+08:00 | `TRAIN-GRPO`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[目标章](../../../../books/part-04-training-system/33-grpo.md) 已有 sample-level staleness 与 asymmetric clip 正文 |
| [AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents](https://arxiv.org/html/2607.18754v1) | 2026-07-22T08:00:00+08:00 | `PLATFORM-TRACE`；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-TRACE`，[目标章](../../../../books/part-06-ai-infrastructure/69-trace.md) 已有 Detect/Attribute/Recover/Rerun 与低绝对归因率边界 |
| [InstantInfer: Enabling Fast LLM Cold Start with Communicating Finite Automata](https://arxiv.org/html/2607.18957v1) | 2026-07-22T08:00:00+08:00 | `PLATFORM-MODEL-REGISTRY`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/html/2607.19058v1) | 2026-07-22T08:00:00+08:00 | `TRAIN-PRETRAINING`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING`，[目标章](../../../../books/part-04-training-system/28-pretraining.md) 已按参数角色分配 optimizer state |
| [ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation](https://arxiv.org/html/2607.19182v1) | 2026-07-22T08:00:00+08:00 | `PLATFORM-TRAINING-OPERATOR`；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-TRAINING-OPERATOR，[目标章](../../../../books/part-06-ai-infrastructure/60-training-operator.md) |
| [Keeping the Cache Warm Pays: Keepalive Economics for Agentic Workloads](https://arxiv.org/html/2607.19214v1) | 2026-07-22T08:00:00+08:00 | `PLATFORM-COST`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [HACO: Hedged Agent Computing for Reliable LLM Systems](https://arxiv.org/html/2607.19215v1) | 2026-07-22T08:00:00+08:00 | `AGENT-PLATFORM`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |

## 4. 证据与知识整合

### [Beyond Accuracy and Cost: Latency-Aware LLM Query Routing for Dynamic Workloads](https://arxiv.org/html/2607.18253v1)

**机制。** 静态 routing 以平均 accuracy/cost 选模型，动态负载下会忽略队列造成的尾延迟。论文把模型质量/成本与实时 queue state、deadline 一起纳入每请求决策。

**证据边界。** 作者在其 workload 与模型池中报告 latency-aware routing 改善 deadline/效用。未证明流量漂移、供应商限流、状态估计误差或生产 tail SLO 下稳定，也不能把 evaluator score 当真实用户价值。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18253v1#S2 — 2 Background on LLM serving frameworks; https://arxiv.org/html/2607.18253v1#S4.SS1 — 4.1 Serving Framework Simulation (SFS) for latency estimation。Evaluation：https://arxiv.org/html/2607.18253v1#A7 — Appendix G Additional Experimental Results; https://arxiv.org/html/2607.18253v1#A4 — Appendix D Response Evaluation using LLM-as-a-judge。Limitations / counterevidence：https://arxiv.org/html/2607.18253v1#S1 — 1 Introduction; https://arxiv.org/html/2607.18253v1#S2 — 2 Background on LLM serving frameworks。

**Trade-off。** 利用队列状态可降低排队，却会把决策绑定瞬时噪声并引入切换；信号不可靠时需保守路由和容量隔离。

**Books：仅报告。**`INFER-SCHEDULING` 已有 SLO-aware routing 主线；这是受限算法分支。

### [Interactive Training 2: Auditable Control Plane for Live Model Training](https://arxiv.org/html/2607.18314v1)

**机制。** Live training 中 agent/人类若直接改 optimizer、数据或 checkpoint，控制请求与真实执行会失配。Interactive Training 2 将动作变成类型化、权限化 command，经 validation、human gate、execution 与 immutable record 形成可审计 control plane。

**证据边界。** 五个 NLP/RL workflow 展示 request 到 recorded result 的闭环，支持该接口可表达已测训练控制。未证明 agent action 安全/最优，也未覆盖大规模故障、并发冲突和回滚一致性。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18314v1#S2 — 2 System at a Glance; https://arxiv.org/html/2607.18314v1#S3 — 3 Control-Plane Design。Evaluation：https://arxiv.org/html/2607.18314v1#S5.SS2 — 5.2 From Request to Recorded Result。Limitations / counterevidence：https://arxiv.org/html/2607.18314v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.18314v1#Sx1 — Limitations。

**Trade-off。** 可审计控制提高可恢复性，却增加权限、延迟和操作状态机；紧急或不支持动作应退回人工运维和 checkpoint recovery。

**Books：已整合。** `PLATFORM-TRAINING-OPERATOR` 的 “Live Training Control 必须是可审计 Proposal” 已把训练变更建模为绑定 run revision、前置状态、影响范围、授权、dry-run 与 rollback point 的 proposal，再由确定性 controller 提交；聊天或模型不能直接修改 runtime。

### [Decode-Time Grammars: Constrained LLM Generation over a Refinement Order of Grammar Fragments](https://arxiv.org/html/2607.18357v1)

**机制。** 生成时 grammar 若一次性固定，会在上下文逐渐收窄时过宽或过窄。论文将 grammar fragment 按 environment-indexed refinement 排序，decode mask 随已知上下文单调细化，并证明特定 fragment 的 support soundness。

**证据边界。** 形式结果证明 No-Ghost soundness 与 refinement 保持 support-set guarantee，实验只验证论文实现范围。它未证明 mask 可表达语义、权限或所有跨字段约束，也不保证模型在合法 support 内生成正确程序。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18357v1#S5 — 5. Implementation and Scope。Evaluation：https://arxiv.org/html/2607.18357v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18357v1#S3.SS1 — 3.1. The failure: negative transfer, not ignorance; https://arxiv.org/html/2607.18357v1#S5.SS4 — 5.4. Limitations。

**Trade-off。** 更强 grammar 降低语法违规，却增加 parser state、mask compute 与拒绝风险；不可 mask 的性质仍需执行前验证/沙箱。

**Books：仅报告。**`MODEL-SAMPLING` 已区分 constrained decoding 与语义正确性；该 refinement formalization 暂不需独立正文。

### [AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report](https://arxiv.org/html/2607.18367v1)

**机制。** 长时交互 world model 需同时保存视觉先验、动作条件和跨段记忆；逐段独立生成会丢 persistent state。AlayaWorld 用双向预训练建立视频先验，再以 autoregressive 控制/记忆模块递推长时状态。

**证据边界。** iWorld-Bench 上作者报告长时生成表现领先，并给 24fps、540p/720p 系统结果。未证明视频指标等于 action-conditioned causal fidelity、planning utility 或真实环境稳定性，也未给开放世界安全保证。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18367v1#S3.SS2 — 3.2 Bidirectional Model Pre-Training – Establishing the General Video Prior; https://arxiv.org/html/2607.18367v1#S3.SS3 — 3.3 Autoregressive Model Training – Control and Memory Integration。Evaluation：https://arxiv.org/html/2607.18367v1#S4 — 4 Results; https://arxiv.org/html/2607.18367v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18367v1#S5 — 5 Conclusion。

**Trade-off。** 持久记忆改善连贯性，却累积误差并增加计算/状态恢复；长 rollout 漂移时需重锚真实 observation。

**Books：仅报告。**它为 `MULTIMODAL-WORLD-MODELS` 提供受限实现，不足以改变“生成连贯不等于可控 world state”的主结论。

### [Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving](https://arxiv.org/html/2607.18631v1)

**机制。** MoE plan search 有两个空间：cost model 能评分的 plan 与 toolchain 真能编译/运行的 plan。论文先做 realizability admission，再用双保真 cost model 排序，避免把不可构建方案当最优。

**证据边界。** 2×RTX4090 与 8×H800 的四个 phase/hardware cell 中有一格未过作者 0.98 gate；预注册 artifact 固定预测再运行。它未证明跨硬件/编译器泛化，artifact URL 未公开，且不保证模型误差下生产最优。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18631v1#S3 — III Design; https://arxiv.org/html/2607.18631v1#S3.SS2 — III-B Dual-fidelity cost model。Evaluation：https://arxiv.org/html/2607.18631v1#S5 — V Evaluation; https://arxiv.org/html/2607.18631v1#S5.SS5 — V-E RQ5: Ablation and discriminative power。Limitations / counterevidence：https://arxiv.org/html/2607.18631v1#S6.SS4 — VI-D Limitations and threats to validity; https://arxiv.org/html/2607.18631v1#S6 — VI Discussion。

**Trade-off。** realizability filter 降低无效搜索，却可能错杀可修复 plan并增加 compiler probes；失败时回退已知可构建配置。

**Books：已有覆盖。** 该 family 已在 `INFER-SCHEDULING` [目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md) 作为 exact-v1 分支承载，包含硬件、未过 gate 与 artifact 边界；原表 `MODEL-MOE` owner 不准确。

### [DWM: Separating World Effects from Actions in Latent World Models](https://arxiv.org/html/2607.18715v1)

**机制。** 普通 latent transition 把 action-driven 变化与环境自身演化压入同一 target，容易让 policy control 与不可控 dynamics 混淆。DWM 在 supervision 层分解 world effect 和 action effect，再组合预测下一 latent。

**证据边界。** 作者在 flat 与刻意增强混淆的 W-variants 上报告 planning success 平均绝对提升 13.1%。未证明分解变量对应真实因果因素、跨环境可识别，或视觉/机器人 world model 获得同样收益。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18715v1#S4 — 4 DWM: World/Action Disentanglement for Latent World Models。Evaluation：https://arxiv.org/html/2607.18715v1#S5.SS1 — 5.1 Benchmarks and Experimental Setup; https://arxiv.org/html/2607.18715v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18715v1#S6 — 6 Conclusion。

**Trade-off。** 分解提升可控性诊断，却需要额外监督/假设并可能误分耦合因素；分解无依据时联合 transition 仍更稳健。

**Books：仅报告。**它支持 `MULTIMODAL-WORLD-MODELS` 的受限 supervision 分支，不足以确立通用因果分解。

### [Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning](https://arxiv.org/html/2607.18722v1)

**机制。** 异步 RL 中 rollout policy 与当前 learner 相差不同，统一 PPO clip 把所有样本当同等新鲜。SAT 用 detached sampled log-ratio 估计 staleness，只收缩高 mismatch 样本与不利方向的 clip endpoint。

**证据边界。** Qwen3-30B-A3B 数学 RL、30,712 prompts、4096 responses/iteration、544 iterations 和 lag 1/8 的结果支持所测 async regime 稳定性。未证明其他 reward/model/lag 或理论 monotonic improvement，artifact 也未证明为 SAT 实现。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18722v1#A5 — Appendix E How Does Each Stability Approach Work in Async RL?。Evaluation：https://arxiv.org/html/2607.18722v1#A6 — Appendix F Experimental Details; https://arxiv.org/html/2607.18722v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.18722v1#S6 — 6 Limitations and Open Questions; https://arxiv.org/html/2607.18722v1#S7 — 7 Conclusion。

**Trade-off。** 按样本收缩减少 stale update 破坏，却可能过度丢弃长尾经验并依赖 proxy；极端 drift 时仍应丢弃/同步刷新 rollout。

**Books：已有覆盖。** `TRAIN-GRPO` 目标章已有 SAT 的 exact-v1 机制与具体 evaluation boundary，无需重复。

### [AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents](https://arxiv.org/html/2607.18754v1)

**机制。** Agent failure 若只保留最终失败标签，无法定位哪个 agent/step 首次破坏状态，也无法验证恢复。AgentDebugX 组织 Detect→Attribute→Recover→Rerun，并允许从残差失败扩展 taxonomy。

**证据边界。** Who-and-When benchmark 上，DeepDebug 在两种开放模型取得最佳 strict agent+step attribution，最高 28.8%，仍显示绝对准确率有限。未证明 judge 可靠、taxonomy 完备或真实生产恢复有效。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18754v1#A1 — Appendix A System and Prompt Details; https://arxiv.org/html/2607.18754v1#S3 — 3 System Overview。Evaluation：https://arxiv.org/html/2607.18754v1#A3 — Appendix C Evaluation Protocol; https://arxiv.org/html/2607.18754v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18754v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.18754v1#S3.SS4 — 3.4 Extensible Failure Taxonomy。

**Trade-off。** 闭环调试提高可追溯性，却增加 trace、judge 和 rerun 成本；归因不确定时必须保留人工审查而非自动修复。

**Books：已有覆盖。** `PLATFORM-TRACE` 目标章已承载该 family 的 Detect/Attribute/Recover/Rerun 与 taxonomy 不完备边界。

### [InstantInfer: Enabling Fast LLM Cold Start with Communicating Finite Automata](https://arxiv.org/html/2607.18957v1)

**机制。** 冷启动由下载、反序列化、内存映射和 runtime 初始化组成；串行组件各自优化仍留下跨组件空隙。InstantInfer 用 communicating finite automata 表达状态依赖，重构组件程序以安全重叠。

**证据边界。** 论文在多 GPU/workload/scale 上报告最高 7.2× cold-start 加速。未证明任意 runtime 的 automata model 完备，也未披露生产 burst、失败恢复、artifact integrity 和 steady-state 影响。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18957v1#S3.SS1 — 3.1. System Model; https://arxiv.org/html/2607.18957v1#S3.SS2 — 3.2. Programming Framework and Runtime。Evaluation：https://arxiv.org/html/2607.18957v1#A3 — Appendix C Additional Burst Cold-Start Results; https://arxiv.org/html/2607.18957v1#S2.SS2 — 2.2. Problem Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.18957v1#S9 — 9. Conclusion。

**Trade-off。** 跨组件 overlap 降启动时间，却增加状态机、buffer lifetime 和错误传播；依赖不满足时必须退回顺序加载。

**Books：仅报告。**`PLATFORM-MODEL-REGISTRY`/Serving 已有 staged loading；CFA 是实现分支，证据不足以改长期主线。

### [Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/html/2607.19058v1)

**机制。** MoE 只有少量 experts 每步活跃，但 Adam moments 通常为所有参数常驻高精度，state 比 weights 更占内存。论文按 expert 活跃/重要性把 optimizer state 分层放置或降低精度，把 state residence 与每步更新需求对齐。

**证据边界。** 6.78B total/440M active、128 experts、约81.9M tokens，主要 H200 且含 H100/MI300X follow-up 的结果支持论文配置；下游接近 chance，不能作能力证据。未证明大规模 wall-clock、长期收敛或任意 MoE routing 下收益。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19058v1#S3.SS0.SSS0.Px4 — Memory model.; https://arxiv.org/html/2607.19058v1#S4.SS0.SSS0.Px1 — Model.。Evaluation：https://arxiv.org/html/2607.19058v1#A4 — Appendix D Zero-shot evaluation detail; https://arxiv.org/html/2607.19058v1#S4 — 4 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.19058v1#S6 — 6 Limitations; https://arxiv.org/html/2607.19058v1#S7 — 7 Conclusion。

**Trade-off。** tiering 降 HBM，却增加 transfer、量化误差和 stale moments；训练不稳时应提升精度/驻留或回退标准 AdamW。

**Books：已有覆盖。** 该 family 已在 `TRAIN-PRETRAINING` [目标章](../../../../books/part-04-training-system/28-pretraining.md) 以 SkewAdam/Tiered Optimizer State 承载；原 `TRAIN-DISTRIBUTED-TRAINING` owner 不准确。

### [ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation](https://arxiv.org/html/2607.19182v1)

**机制。** 让 LLM 直接执行 Kubernetes remediation 会把诊断猜测变成集群副作用。ARBITER 将 agent proposal 置于 telemetry-derived SLO、typed action、policy guard、dry-run/approval 与 reconciliation loop 内。

**证据边界。** 论文发布 controller、replay corpus、harness 和 safety tests，并在其故障场景中评估恢复。未证明开放世界根因诊断、任意 CRD/集群安全或生产 tail behavior。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19182v1#S2.SS3 — II-C Why OpenTelemetry Changes the Design Space; https://arxiv.org/html/2607.19182v1#S4 — IV ARBITER Control Architecture。Evaluation：https://arxiv.org/html/2607.19182v1#S8 — VIII Evaluation Results; https://arxiv.org/html/2607.19182v1#S7 — VII Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.19182v1#S11 — XI Conclusion。

**Trade-off。** guard 降低误操作，却增加策略维护、恢复延迟和 false negative；证据不足时应只建议或人工批准。

**Books：已整合。** 单一 owner 为 `PLATFORM-TRAINING-OPERATOR`；该章已与 Interactive Training 2 合并表达 Agent proposal、policy/SLO admission、operator effect commit 与实际 workload-state 验收的分权边界，并在无法证明 effect 或 rollback 时回退人工处理。

### [Keeping the Cache Warm Pays: Keepalive Economics for Agentic Workloads](https://arxiv.org/html/2607.19214v1)

**机制。** Agent 在 tool/approval 间隔后续接相同前缀，但 provider cache 可能已逐出，导致再次支付全 prefill。论文用客户端定时 replay prefix 的 keepalive 维持 residency。

**证据边界。** 在四家 provider、论文时间点计价与间隔下，keepalive 可跨原本逐出的 gap 保温，post-pause 成本最高降 12.5×。未证明 provider 内部 residency、未来计价、多人共享公平或持续 keepalive 对容量/SLO 的系统影响。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19214v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.19214v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19214v1#S6 — 6 Discussion: rational adoption, and the provider response it forces; https://arxiv.org/html/2607.19214v1#S7 — 7 Threats to validity。

**Trade-off。** 个体客户端节省重算，却占用 provider cache、增加无业务 token 和公地竞争；应由定价/配额约束，而非默认无限保温。

**Books：仅报告。**它揭示 `PLATFORM-COST` 的外部性，但当前供应商行为和价格短期性强，不写长期机制正文。

### [HACO: Hedged Agent Computing for Reliable LLM Systems](https://arxiv.org/html/2607.19215v1)

**机制。** 固定 agent→model 绑定假设 runtime 稳定；模型延迟/质量变化时，冗余执行要么不够要么成本过高。HACO 按 role、模型与环境动态决定是否发 hedged invocation，并在足够结果后取消其余。

**证据边界。** 作者在多个 benchmark 与注入 degradation 下报告优于固定/全并行的质量、token 和 latency。未证明 degradation detector、取消传播、共享 tool side effect 或生产 tail risk。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19215v1#A4 — Appendix D Algorithms and Baselines; https://arxiv.org/html/2607.19215v1#A4.SS1 — D.1 HACO Algorithm。Evaluation：https://arxiv.org/html/2607.19215v1#S4.SS2 — 4.2 Experimental Results; https://arxiv.org/html/2607.19215v1#A3 — Appendix C Experimental Setup Details。Limitations / counterevidence：https://arxiv.org/html/2607.19215v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.19215v1#S5 — 5 Conclusion。

**Trade-off。** hedging 降尾部失败但增加重复成本与副作用竞争；只适合幂等/可取消阶段，非幂等工具需 single commit。

**Books：仅报告。**`AGENT-PLATFORM` 已有 bounded redundancy/commit 原则；HACO 是受限策略实例。

## 5. 缺口与下一步

无

无 external Materials Request。全部保留候选均可访问 exact-v1；旧候选降级不会删除原始证据。本日所需 Books 写入和写后语义审计均已完成；若后续出现具体 false positive、false negative 或来源更正，只重开对应 family。

准入闭合账目：raw identities=495；旧候选=96；V3 候选=13；本轮从旧候选降级=83。准入前关闭的共同原因是：局部指标或单任务方法没有持久系统增量、垂直应用/AI for Science 越界、benchmark 未改变 evaluation/deployment contract，或机制已被同日更强材料覆盖。

## 6. 复核

复核者：非作者独立复核（/root/aug11_20，2026-09-10）。

结论：通过

写后复核确认 `SF-2026-ARXIV-2607-18314` 与 `SF-2026-ARXIV-2607-19182` 已共同进入 `PLATFORM-TRAINING-OPERATOR` 的 live-control 正文：proposal、authorization/admission、controller commit 与 effect verification 分权清晰，并保留静态 spec、暂停及人工回退；两项来源没有被写成自治运维的通用安全保证。
