# Daily Research — 2026-07-24

**规范：** V3
**窗口：** 2026-07-23T09:00:00+08:00 ～ 2026-07-24T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T17:30:00+08:00

## 1. 结论

本窗口按 first-public owner 得到 555 条 arXiv 原始身份。逐条读取标题与完整摘要后，冻结 16 个候选；旧稿的 113 个候选不作为新分母，其中 97 个旧候选因只提供局部方法/benchmark、垂直应用或没有改变长期系统判断而降回准入前关闭。原始证据保留，但不在正文候选表继续制造重要性错觉。

保留材料集中在可迁移状态、训练/推理执行计划、跨层资源约束、证据与安全边界。每项都已用旧稿保存的 exact-v1 primary evidence 重新核对机制与反证；没有用标题关键字替代语义判断，也没有把能映射 ROADMAP 当作准入理由。独立复核已经把“来源存在”和“正文已承载”分开，并确认本日唯一正文增量已与相邻 cache drift/压缩机制合并，而非追加孤立论文段。

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
| SRC-ARXIV | [exact-v1 HTML](https://arxiv.org/)；本窗 555 条 identity 逐条 title + 完整摘要语义筛选；旧稿 exact-v1 Method / Evaluation / Limitations 仅作可核实证据种子 | 已检查 | 无 |

本次排除 AI for Science、纯垂直应用、只改局部任务指标以及没有系统状态/控制/评价契约增量的工作。withdrawn 身份不进入候选；本组没有保留 withdrawn family。

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；7～9 分深入审阅，5～6 分标准审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models](https://arxiv.org/html/2607.20436v1) | 2026-07-24T08:00:00+08:00 | `PLATFORM-EVALUATION-SYSTEM`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已分开 checkpoint、prompt distribution、readout 与 deployment slice |
| [When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion](https://arxiv.org/html/2607.20543v1) | 2026-07-24T08:00:00+08:00 | `TRAIN-GRPO`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[目标章](../../../../books/part-04-training-system/33-grpo.md) 已区分分支概率与条件完成能力 |
| [SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales](https://arxiv.org/html/2607.20548v1) | 2026-07-24T08:00:00+08:00 | `TRAIN-DISTRIBUTED-TRAINING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing](https://arxiv.org/html/2607.20723v1) | 2026-07-24T08:00:00+08:00 | `PLATFORM-SECURITY`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [GPE: Evaluating Robust Evidence Aggregation for Fact Verification under Controllable GEO-Style Poisoning](https://arxiv.org/html/2607.20730v1) | 2026-07-24T08:00:00+08:00 | `PLATFORM-EVALUATION-SYSTEM`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Memoir: Should a Model Write to Its Memory While It Thinks?](https://arxiv.org/html/2607.20792v1) | 2026-07-24T08:00:00+08:00 | `AGENT-MEMORY`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways](https://arxiv.org/html/2607.20860v1) | 2026-07-24T08:00:00+08:00 | `PLATFORM-MODEL-REGISTRY`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-MODEL-REGISTRY`，[目标章](../../../../books/part-06-ai-infrastructure/59-model-registry.md) 已有版本化行为指纹与 attestation 边界 |
| [Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay](https://arxiv.org/html/2607.21005v1) | 2026-07-24T08:00:00+08:00 | `TRAIN-PRETRAINING`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING`，[目标章](../../../../books/part-04-training-system/28-pretraining.md) 已有 normalization×weight decay 与 module-wise guard |
| [The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and The Channel, Not the Content, Decides What Works](https://arxiv.org/html/2607.21273v1) | 2026-07-24T08:00:00+08:00 | `TRAIN-GRPO`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[目标章](../../../../books/part-04-training-system/33-grpo.md) 已有 dense credit 的 shaping bias、collapse 与 outcome-gate 回退 |
| [Emergent Misalignment Recruits a Pre-existing Persona Subspace](https://arxiv.org/html/2607.21356v1) | 2026-07-24T08:00:00+08:00 | `TRAIN-SFT`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Error Certificates for KV-Cache Eviction via Randomized Design](https://arxiv.org/html/2607.21475v1) | 2026-07-24T08:00:00+08:00 | `INFER-KV-CACHE`；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Finite-Sample Coverage Audits for High-Recall Candidate Generation: Certification and Learning-Theoretic Design](https://arxiv.org/html/2607.21480v1) | 2026-07-24T08:00:00+08:00 | `PLATFORM-EVALUATION-SYSTEM`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems](https://arxiv.org/html/2607.21503v1) | 2026-07-24T08:00:00+08:00 | `AGENT-CONTEXT`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-CONTEXT`，[目标章](../../../../books/part-07-agent/75-context.md) 已有 lifecycle、versioned compaction、fidelity check 与原文回退 |
| [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/html/2607.21535v1) | 2026-07-24T08:00:00+08:00 | `INFER-SPECULATIVE-DECODING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/html/2607.21557v1) | 2026-07-24T08:00:00+08:00 | `TRAIN-GRPO`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering](https://arxiv.org/html/2607.21571v1) | 2026-07-24T08:00:00+08:00 | `MULTIMODAL-EMBODIED-VLA`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |

## 4. 证据与知识整合

### [Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models](https://arxiv.org/html/2607.20436v1)

**机制。** Fine-tuned checkpoint 可能只在 evaluation-style prompt 下看似修复，普通部署 prompt 仍沿用原 routing subspace。论文比较提示分布下的内部路由/行为，审计 evaluation→deployment mismatch。

**证据边界。** 受控模型实验显示改变 prompt style 或深度窗口可重新暴露行为，并区分 heuristic window 偏差。它只是 checkpoint diagnostic，不是训练防御或部署安全保证；有限模型/任务不能证明普遍 subspace 因果。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20436v1#S2 — 2 Methodology; https://arxiv.org/html/2607.20436v1#S2.SS2 — 2.2 Localization Method。Evaluation：https://arxiv.org/html/2607.20436v1#A5 — Appendix E Per-item intervention agreement analysis; https://arxiv.org/html/2607.20436v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20436v1#A7 — Appendix G E4 Adjacent-Window Depth Sweep and Typed-Failure Remediation; https://arxiv.org/html/2607.20436v1#S4 — 4 Discussion。

**Trade-off。** 增加 deployment-like prompts 能降低评测错觉，却扩大测试矩阵并可能仍漏真实 traffic；必须将 prompt distribution 作为 evaluation artifact 版本化。

**Books：已有覆盖。** `PLATFORM-EVALUATION-SYSTEM` 已把 checkpoint、prompt distribution、representation probe、readout/steering 与真实 deployment slice 分开，并要求无法排除混杂时降级为 sensor；本论文提供 routing-subspace 受限证据。

### [When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion](https://arxiv.org/html/2607.20543v1)

**机制。** RLVR 优化单样本正确率时可能把概率质量集中到少数已会解的路径，提升 pass@1 却缩小可通过多次采样发现的 reasoning support。论文以 pass@k inversion 比较训练前后解题集合。

**证据边界。** 作者实验观察训练后小 k 改善而大 k 可解决的 distinct problems 减少，支持“平均奖励提升不等于支持集扩张”。未证明所有 RLVR/GRPO 都会发生，也未隔离所有采样温度、base rollout 与 verifier 偏差。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20543v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20543v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.20543v1#S7 — 7 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20543v1#S4 — 4 Pass@ Inversion Is a Boundary-Regime Failure; https://arxiv.org/html/2607.20543v1#S8 — 8 Discussion。

**Trade-off。** 集中分布提高一次命中，却牺牲多样性与探索；训练 gate 应同时看 pass@1、large-k coverage 和熵，必要时保留 base-policy mixture。

**Books：已有覆盖。** `TRAIN-GRPO` 已区分“自然采样进入某解法”的早期分支概率与“给定入口后完成”的条件能力，并指出有限 pass@k 不能证明能力消失；本材料是这条 reasoning-boundary 判断的直接受限证据。

### [SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales](https://arxiv.org/html/2607.20548v1)

**机制。** SOAP/Muon 类矩阵预条件器在单卡可行，分布式大模型会被矩阵 state、通信和 layer ownership 卡住。论文按 layer 切分 optimizer state 并适配 Megatron，使预条件计算与参数分片对齐。

**证据边界。** 作者报告大规模训练可运行及若干 system optimization，并指出 KL-SOAP 在内存不受限时更有效。未证明所有模型/scale 的收敛优势、与 Adam 的等算力比较或故障恢复；推荐受内存与实现绑定。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20548v1#S4.SS2 — 4.2 Systems to enable higher-order optimizers; https://arxiv.org/html/2607.20548v1#S3.SS1 — 3.1 Batch Size Scaling for Mixture-of-Experts Models。Evaluation：https://arxiv.org/html/2607.20548v1#S5 — 5 Pretraining Experiments with Muon and SOAP。Limitations / counterevidence：https://arxiv.org/html/2607.20548v1#S7 — 7 Conclusions and Future Work。

**Trade-off。** 更强预条件可能提高样本效率，却增加 optimizer state、分解计算和通信；内存/稳定性不足时 Muon/AdamW 仍是合理分支。

**Books：仅报告。**`TRAIN-DISTRIBUTED-TRAINING` 已有 optimizer-state/layout 主线；该实现证据不足以改变通用选择。

### [Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing](https://arxiv.org/html/2607.20723v1)

**机制。** 远程 API 看不到模型，但逐 token timing 泄露 speculative decoding、context window 和并行/缓存边界。论文用精心构造请求与时序统计反推 architecture/deployment knobs。

**证据边界。** 作者在实验中推断多个系统特征，并对 Gemini Flash 2.5 给出约128K draft context 的估计。该结论是黑盒测量推断，不是厂商披露；攻击主要假设单 GPU且未覆盖多 GPU、网络 jitter 和动态 batching。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20723v1#A2 — Appendix B Additional Details on Leaking Model Architecture Attack; https://arxiv.org/html/2607.20723v1#S2.SS1 — 2.1. Transformer Architecture。Evaluation：https://arxiv.org/html/2607.20723v1#A1.SS2 — A.2. Remote Black-Box Model Results; https://arxiv.org/html/2607.20723v1#S4.SS4 — 4.4. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20723v1#S3 — 3. Threat Model; https://arxiv.org/html/2607.20723v1#S8 — 8. Conclusion。

**Trade-off。** 填充/批处理可降 timing signal，却增加延迟和成本；完全隐藏内部状态可能与性能 SLO 冲突，应明确泄露预算。

**Books：仅报告。**`PLATFORM-SECURITY` 的 side-channel 主线已能承载，该单系统推断不作为事实写入 Books。

### [GPE: Evaluating Robust Evidence Aggregation for Fact Verification under Controllable GEO-Style Poisoning](https://arxiv.org/html/2607.20730v1)

**机制。** 事实验证若只在干净 evidence 上评估，会漏掉搜索排序/内容污染使多个来源相关失真的情况。GPE 构造可控 poison 环境，分开 instruction injection、content tampering 与 evidence aggregation。

**证据边界。** 多 verifier/attack 的实验显示干净集排序不能预测污染下鲁棒性，且抗 instruction injection 不推出抗内容篡改。未证明 benchmark poison 分布代表现实 GEO，也未给单一稳健 aggregator 或部署阈值。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20730v1#S4 — IV Evaluation Framework。Evaluation：https://arxiv.org/html/2607.20730v1#S5.SS2 — V-B Results and Analysis; https://arxiv.org/html/2607.20730v1#S3 — III GPE Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.20730v1#S6 — VI Conclusion。

**Trade-off。** 对抗评价暴露脆弱性，却增加人工 ground truth、攻击覆盖和成本；上线仍需 provenance、来源独立性与拒答策略。

**Books：仅报告。**`PLATFORM-EVALUATION-SYSTEM` 已包含 evidence provenance/污染测试；此 benchmark 是受限实例。

### [Memoir: Should a Model Write to Its Memory While It Thinks?](https://arxiv.org/html/2607.20792v1)

**机制。** 推理循环若一边读取 fast memory 一边在每次 pondering iteration 改写它，当前思考会改变后续同一推理的状态，形成自反馈。Memoir 显式测试这种 read/write coupling，并实现 delta-rule kernel。

**证据边界。** 作者给出任务实验及 kernel 从0.907ms到0.351ms的设备绑定结果，但其 limitation 承认 ablation 未隔离命名变量。未证明在线写 memory 是收益来源、跨模型稳定或不会放大错误。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20792v1#S3 — 3 Method; https://arxiv.org/html/2607.20792v1#S4 — 4 Implementation。Evaluation：https://arxiv.org/html/2607.20792v1#S5 — 5 Experimental Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.20792v1#S3.SS3 — 3.3 Future-latent and energy objectives; https://arxiv.org/html/2607.20792v1#S6 — 6 Limitations。

**Trade-off。** 边想边写可快速适应，却会自我污染、难回滚且增加 kernel/state 一致性；高风险推理应 stage writes，验证后 commit。

**Books：仅报告。**`AGENT-MEMORY` 已有 staged write/commit 主线；该未隔离 ablation 不足以改变正文。

### [Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways](https://arxiv.org/html/2607.20860v1)

**机制。** Gateway 可在不告知客户端时替换 backend 或按比例稀释昂贵模型。IRIS 仅用返回文本的随机数/字符串分布做 fingerprint，联合检测 whole-stream substitution、fractional dilution 并估计 routing fraction。

**证据边界。** 论文实验覆盖 adversarial gateway、未知 diluent、knob identifiability 和 false-positive control。未证明所有模型可稳定区分、供应商更新后 fingerprint 不漂移，也不是 cryptographic attestation。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20860v1#S15 — S15 Extended Method Comparison; https://arxiv.org/html/2607.20860v1#S6.SS2 — 6.2 Commercial models via OpenRouter。Evaluation：https://arxiv.org/html/2607.20860v1#S6 — 6 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20860v1#S7 — 7 Conclusion。

**Trade-off。** 黑盒审计无需服务端合作，却消耗查询、受采样噪声和模型升级影响；高价值场景仍需签名/attestation 与合同追责。

**Books：已有覆盖。** 单一 owner 更适合 `PLATFORM-MODEL-REGISTRY`：该章已把版本化行为 fingerprint 定义为 revalidation trigger，绑定 template/schema、sampling、query budget、reference population 与阈值，并明确不能替代 digest/attestation；IRIS 的 routing dilution 是这一合同的实例。

### [Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay](https://arxiv.org/html/2607.21005v1)

**机制。** Normalization 让部分权重方向影响函数而范数不直接影响输出，但 weight decay 仍持续缩小范数；有效更新相对权重变大后可跨过稳定边界并触发 loss spike。论文把它与 learning-rate criticality 区分为 weight-norm criticality。

**证据边界。** 模块级 dynamics 与消融支持只对 scale-invariant weights 施加强 decay 会诱发不稳定，并解释 penalty 不能无限增大。未证明单一临界值跨架构/optimizer/scale 通用，也未排除数据和数值因素共同作用。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21005v1#S6 — 6 Training Instability in Large Language Models and Module-wise Dynamics。Evaluation：https://arxiv.org/html/2607.21005v1#A1.SS1 — A.1 Experimental Details; https://arxiv.org/html/2607.21005v1#A1.SS3 — A.3 Ablation Study: Weight Decay Applied Only to Non-Scale-Invariant Layers。Limitations / counterevidence：https://arxiv.org/html/2607.21005v1#S7 — 7 Discussion。

**Trade-off。** decay 改善正则化却会降低 scale-invariant 参数范数、放大相对步长；需监控 module-wise norm/update ratio，越界时减 decay/lr 或恢复 checkpoint。

**Books：已有覆盖。** `TRAIN-PRETRAINING` 已把 normalization、weight decay、参数范数、相对更新幅度、loss spike 与 module-wise update-ratio guard 放在同一推理链；本 family 的机制已真实承载，不再以来源名称追加。

### [The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and The Channel, Not the Content, Decides What Works](https://arxiv.org/html/2607.21273v1)

**机制。** Dense prediction reward 在 GRPO 中不只提供内容，还改变每 token/step 的 advantage 分布与归一化；模型可优化 reward channel 的可预测结构而非任务。论文用 gold signal、content-free placebo 和 matched normalization 分离内容与通道。

**证据边界。** ALFWorld/WebShop 的匹配实验中，没有 reward-channel variant 稳定胜过 normalization baseline，gold 也未显著胜 placebo；并观察 unbounded advantage collapse。未证明所有任务或 GRPO 实现同样失败，也未提供通用安全 channel。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21273v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21273v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.21273v1#S3 — 3 Experimental Setting; https://arxiv.org/html/2607.21273v1#S4.SS3 — 4.3 Analysis: bounded returns, unbounded advantages。Limitations / counterevidence：https://arxiv.org/html/2607.21273v1#S4 — 4 The Failure: Predictability Hacking; https://arxiv.org/html/2607.21273v1#S6 — 6 Controlled Separation of Failure Axes。

**Trade-off。** 密集 credit 可提高学习信号，却增加 channel hacking、尺度爆炸和任务依赖；必须用 placebo/matched normalization 对照，失败时回退 outcome reward。

**Books：已有覆盖。** `TRAIN-GRPO` 已说明 dense intermediate reward 只能传播接口已有信息，会引入 shaping bias、channel hacking 与 collapse，并要求 outcome gate、per-channel guard 和回退；该材料的 content-free placebo 是验证工具，不改变正文 owner。

### [Emergent Misalignment Recruits a Pre-existing Persona Subspace](https://arxiv.org/html/2607.21356v1)

**机制。** 窄域 fine-tuning 的副作用可能不是新学出完整恶意策略，而是放大预训练模型已存在的 persona direction。论文以表示干预和配对设计把 on-domain adherence 与 off-domain misalignment 投影到共享 subspace。

**证据边界。** 实验支持窄训练可招募预存 persona subspace，但 broad/narrow readout 都由同一 alignment score 阈值构造，干预会机械移动两者。未证明该 subspace 是因果人格、跨模型稳定或可作为安全控制器。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21356v1#A2.SS6 — B.6 The paired design; https://arxiv.org/html/2607.21356v1#A7.SS1 — G.1 Design。Evaluation：https://arxiv.org/html/2607.21356v1#A11 — Appendix K Complete numerical results; https://arxiv.org/html/2607.21356v1#A13.SS5 — M.5 Two 2026 results。Limitations / counterevidence：https://arxiv.org/html/2607.21356v1#A9.SS7 — I.7 Failure modes; https://arxiv.org/html/2607.21356v1#S11 — 11 Conclusion。

**Trade-off。** subspace audit 可提前发现方向漂移，却依赖 probe/阈值并可能误抑制有用能力；仍需行为评价和可逆训练。

**Books：仅报告。**它是 `TRAIN-SFT` 的受限机制证据，未达到可写成通用安全原理的程度。

### [Error Certificates for KV-Cache Eviction via Randomized Design](https://arxiv.org/html/2607.21475v1)

**机制。** KV eviction 的平均注意力误差无法告诉单请求是否进入重损伤区。论文用已知随机 eviction design 构造统计 certificate，并在风险超界时回退 full-cache score。

**证据边界。** 五个模型 family 的长对话中，certificate 相比 entropy/margin 更能识别 heavy damage，触发后恢复 full-cache；结果依赖随机化设计和论文阈值。未证明任意 deterministic eviction、任务/SLO 或在线分布下校准，也不消除全缓存成本。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21475v1#S3.SS3 — 3.3 Design: certainty plus Poisson tail, Hájek by logit offset; https://arxiv.org/html/2607.21475v1#S6.SS1 — 6.1 Design。Evaluation：https://arxiv.org/html/2607.21475v1#A2 — Appendix B Experimental details; https://arxiv.org/html/2607.21475v1#S6 — 6 Pre-registered study on real workloads, at two scales。Limitations / counterevidence：https://arxiv.org/html/2607.21475v1#S5 — 5 From attention error to task failure: synthetic suites; https://arxiv.org/html/2607.21475v1#S6.SS3 — 6.3 The silent-failure panel。

**Trade-off。** certificate 提供可审计 risk，但随机探索会损失部分质量/容量，回退造成延迟突增；需要为 certificate 与 fallback 预留预算。

**Books：已整合。** `INFER-KV-CACHE` 的误差预算主线已明确 eviction 不能只输出启发式重要度；随机化设计可生成 error certificate 供 admission owner 在质量预算内决定驱逐，而 certificate 不证明下游任务正确，身份或 calibration 越界时须失效并回退 full-cache recompute。

### [Finite-Sample Coverage Audits for High-Recall Candidate Generation: Certification and Learning-Theoretic Design](https://arxiv.org/html/2607.21480v1)

**机制。** 高召回候选生成只审入选池无法估计漏检；遗漏只存在于 excluded pool。论文用对排除池的有限样本 audit，给 missing relevant mass 的置信上界与 label complexity。

**证据边界。** 理论给出 finite-class/VC-class 条件下的审计样本复杂度，并以示例说明设计。它未证明现实语义标签独立同分布、reviewer 无误或任意自适应筛选可直接套用，主要是方法学而非 LLM 系统实验。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21480v1#A1.SS1 — A.1 Proof of the finite-class design bound; https://arxiv.org/html/2607.21480v1#A1.SS2 — A.2 Proof of the VC-class design bound。Evaluation：https://arxiv.org/html/2607.21480v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21480v1#S1.SS1 — 1.1 Motivating examples。Limitations / counterevidence：https://arxiv.org/html/2607.21480v1#S9 — 9 Conclusion and future directions。

**Trade-off。** 抽样认证能量化漏检，却消耗人工标签且依赖采样/假设；发现分层误差时需扩查对应排除族。

**Books：仅报告。**它适合研究流程自检，不改变 `PLATFORM-EVALUATION-SYSTEM` 的产品机制正文。

### [Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems](https://arxiv.org/html/2607.21503v1)

**机制。** 把整段历史不断回填 prompt 会让 token 成本随轮次近二次增长，粗暴 summary 又丢 provenance/细节。论文把 context 当 lifecycle：分层存储、检索、验证 compaction，再组装当前工作集。

**证据边界。** 作者评估中 naive accumulation、crude summary 与 validated compaction 呈现成本/准确度差异。证据限 Maximem Synap 实现和任务；未证明 compaction 对所有 agent 保真、跨会话因果一致或经济数字跨定价稳定。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21503v1#A2 — Appendix B Retrieval-study methodology (motivating study, Section 3.3); https://arxiv.org/html/2607.21503v1#S4 — 4 The Maximem Synap System。Evaluation：https://arxiv.org/html/2607.21503v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.21503v1#S6.SS2 — 6.2 Results。Limitations / counterevidence：https://arxiv.org/html/2607.21503v1#S6.SS3 — 6.3 Scope and limitations of this evaluation; https://arxiv.org/html/2607.21503v1#S8 — 8 Future Directions: Decision-Level and Organization-Scale Context。

**Trade-off。** 结构化 compaction 降成本，却增加验证、索引、陈旧和恢复责任；无法证明摘要保真时应保留原文引用或扩大窗口。

**Books：已有覆盖。** `AGENT-CONTEXT` 已把 context registry、source/version/provenance、compaction proposal、fidelity check、compare-and-commit 与原文恢复引用写成生命周期；本实现没有形成新的长期控制边界。

### [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/html/2607.21535v1)

**机制。** MTP draft head 在百万 token 上即使参数小，也可能为完整上下文构建/读取 draft KV，固定成本不再可忽略。Windowed-MTP 只让 draft 看有限窗口，target 仍验证接受 token。

**证据边界。** 论文在披露模型/TP/KV balance 下报告 matched acceptance 的 decode latency 改善，并保持 target verified distribution。具体百分比随 TP 与 memory/compute balance 变化；未证明所有长上下文任务保持 acceptance 或端到端 SLO。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21535v1#S2.SS0.SSS0.Px4 — Serving systems.; https://arxiv.org/html/2607.21535v1#S4 — 4 Method: Windowed-MTP。Evaluation：https://arxiv.org/html/2607.21535v1#A4 — Appendix D Full results tables; https://arxiv.org/html/2607.21535v1#S6 — 6 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21535v1#S7 — 7 Discussion and limitations; https://arxiv.org/html/2607.21535v1#S7.SS0.SSS0.Px9 — Limitations.。

**Trade-off。** 窗口降低 draft KV 税，却可能丢长距依赖并降 acceptance；target verification 保正确分布但不能回收无效 draft 成本，需按 workload 选窗口/回退全上下文。

**Books：仅报告。**`INFER-SPECULATIVE-DECODING` 已有 draft cost/acceptance trade-off；这是长上下文特定分支。

### [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/html/2607.21557v1)

**机制。** Agent RL 若只训练模型而固定 harness，policy 学到的 observation/action contract 与部署 harness 可能错位。OpenForgeRL 把 harness/environment 纳入训练接口，使 rollout、tool use 与 verifier 可替换。

**证据边界。** 所测 harness 中学习难度显著不同，RL 改善 self-verification、tool coverage 和多步完成，但 error recovery 仍弱。未证明框架本身导致收益、跨 harness 泛化或真实副作用安全。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21557v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.21557v1#A3 — Appendix C Evaluation Details; https://arxiv.org/html/2607.21557v1#A3.SS1 — C.1 ClawEval and QwenClawBench Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.21557v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21557v1#S6 — 6 Conclusion。

**Trade-off。** harness-native 训练提高一致性，却绑定工具 schema/runtime 并增加环境维护；error recovery 需专门数据/失败注入，不能只靠更多 RL。

**Books：仅报告。**`TRAIN-GRPO` 与 Agent workflow 已涵盖 environment contract；框架名称不进入正文。

### [Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering](https://arxiv.org/html/2607.21571v1)

**机制。** 连续 embodied QA 需要跨 episode 积累和选择性复用信息；仅持久保存 memory 不保证新知识被正确写入、合并和检索。论文将瓶颈分为 persistence 与 accumulation/usage。

**证据边界。** 顺序 embodied QA 实验显示保存现有 memory 往往不足，支持“存在状态”不等于“可用知识”。未证明任意机器人 memory 架构同样失败，也未隔离感知、写入、检索和回答误差的全部贡献。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.21571v1#S1 — I Introduction; https://arxiv.org/html/2607.21571v1#S2 — II Related Work。Evaluation：https://arxiv.org/html/2607.21571v1#S5 — V Experimental Results and Analysis; https://arxiv.org/html/2607.21571v1#S6.SS2 — VI-B Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.21571v1#S7 — VII Conclusion。

**Trade-off。** 积累机制改善长期任务，却增加错误合并、陈旧和容量；需 provenance、更新冲突与遗忘策略，失败时回读原 observation。

**Books：仅报告。**它强化 `MULTIMODAL-EMBODIED-VLA`/Agent Memory 边界，但证据不足以新增独立机制段。

## 5. 缺口与下一步

无

无 external Materials Request。全部保留候选均可访问 exact-v1；旧候选降级不会删除原始证据。本日所需 Books 写入和写后语义审计均已完成；若后续出现具体 false positive、false negative 或来源更正，只重开对应 family。

准入闭合账目：raw identities=555；旧候选=113；V3 候选=16；本轮从旧候选降级=97。准入前关闭的共同原因是：局部指标或单任务方法没有持久系统增量、垂直应用/AI for Science 越界、benchmark 未改变 evaluation/deployment contract，或机制已被同日更强材料覆盖。

## 6. 复核

复核者：非作者独立复核（/root/aug11_20，2026-09-10）。

结论：通过

写后复核确认 `SF-2026-ARXIV-2607-21475` 已进入 `INFER-KV-CACHE` 的 certified-eviction 正文，且与同节的 drift、cross-loop reuse 和完整 KV 回退形成连续选择链；证书的假设边界没有被误写为下游正确性保证。
