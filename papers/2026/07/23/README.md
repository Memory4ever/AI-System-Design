# Daily Research — 2026-07-23

**规范：** V3
**窗口：** 2026-07-22T09:00:00+08:00 ～ 2026-07-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T17:30:00+08:00

## 1. 结论

本窗口按 first-public owner 得到 444 条 arXiv 原始身份。逐条读取标题与完整摘要后，冻结 15 个候选；旧稿的 117 个候选不作为新分母，其中 102 个旧候选因只提供局部方法/benchmark、垂直应用或没有改变长期系统判断而降回准入前关闭。原始证据保留，但不在正文候选表继续制造重要性错觉。

保留材料集中在可迁移状态、训练/推理执行计划、跨层资源约束、证据与安全边界。每项都已用旧稿保存的 exact-v1 primary evidence 重新核对机制与反证；没有用标题关键字替代语义判断，也没有把能映射 ROADMAP 当作准入理由。独立复核已经把“来源存在”和“正文已承载”分开，并确认本日唯一正文增量已进入 GPU Scheduler 的资源耦合主线。

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
| SRC-ARXIV | [exact-v1 HTML](https://arxiv.org/)；本窗 444 条 identity 逐条 title + 完整摘要语义筛选；旧稿 exact-v1 Method / Evaluation / Limitations 仅作可核实证据种子 | 已检查 | 无 |

本次排除 AI for Science、纯垂直应用、只改局部任务指标以及没有系统状态/控制/评价契约增量的工作。withdrawn 身份不进入候选；本组没有保留 withdrawn family。

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；7～9 分深入审阅，5～6 分标准审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads](https://arxiv.org/html/2607.19349v1) | 2026-07-23T08:00:00+08:00 | `INFER-SCHEDULING`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md) 已有联合 workload contract |
| [Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX](https://arxiv.org/html/2607.19353v1) | 2026-07-23T08:00:00+08:00 | `PLATFORM-SECURITY`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [NEXUS: Structured Runtime Safety for Tool-Using LLM Agents](https://arxiv.org/html/2607.19356v1) | 2026-07-23T08:00:00+08:00 | `AGENT-TOOL-CALLING`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`，[目标章](../../../../books/part-07-agent/78-tool-calling.md) 已有 proposal、monitor、authorization 与 effect commit 分权 |
| [Stateful Guardrails for Multi-Turn LLM Systems: A Conversational Risk Accumulation Framework](https://arxiv.org/html/2607.19361v1) | 2026-07-23T08:00:00+08:00 | `PLATFORM-SECURITY`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Rethinking Uncertainty Evaluation in Large Language Models](https://arxiv.org/html/2607.19367v1) | 2026-07-23T08:00:00+08:00 | `PLATFORM-EVALUATION-SYSTEM`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems](https://arxiv.org/html/2607.19430v1) | 2026-07-23T08:00:00+08:00 | `AGENT-MULTI-AGENT`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`，[目标章](../../../../books/part-07-agent/82-multi-agent.md) 已有 Collective Risk 与独立 verifier |
| [ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems](https://arxiv.org/html/2607.19432v1) | 2026-07-23T08:00:00+08:00 | `AGENT-MCP`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Integrity of peer-to-peer distributed LLM inference under malicious nodes](https://arxiv.org/html/2607.19490v1) | 2026-07-23T08:00:00+08:00 | `PLATFORM-SECURITY`；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) 已有 intermediate-state canary 正文 |
| [Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts](https://arxiv.org/html/2607.19539v1) | 2026-07-23T08:00:00+08:00 | `INFER-TENSORRT-LLM`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 已有 tile completion signal 与同步回退 |
| [Do Co-Located AI Training Jobs Synchronize? Load-Dependent Throttling as a Coupling Mechanism for Phase-Locking Behind a Shared Power Cap](https://arxiv.org/html/2607.19638v1) | 2026-07-23T08:00:00+08:00 | `PLATFORM-GPU-SCHEDULER`；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-GPU-SCHEDULER，[目标章](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF](https://arxiv.org/html/2607.19712v1) | 2026-07-23T08:00:00+08:00 | `TRAIN-RLHF`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [DGNA: Dissecting GPU NUMA Architecture through Microbenchmarking and Data Analysis](https://arxiv.org/html/2607.19922v1) | 2026-07-23T08:00:00+08:00 | `INFER-GPU-MEMORY`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/html/2607.19957v1) | 2026-07-23T08:00:00+08:00 | `PLATFORM-SECURITY`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) 已有 position-independent reuse 隔离边界 |
| [SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD](https://arxiv.org/html/2607.20145v1) | 2026-07-23T08:00:00+08:00 | `TRAIN-DISTRIBUTED-TRAINING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：硬件绑定 recipe，不形成新的长期机制 |
| [MoX: Efficient MoE Routing on Direct-Connect Topologies](https://arxiv.org/html/2607.20220v1) | 2026-07-23T08:00:00+08:00 | `MODEL-MOE`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`MODEL-MOE`，[目标章](../../../../books/part-02-model/21-moe.md) 已有 direct-connect multicast/reduction tree 正文 |

## 4. 证据与知识整合

### [FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads](https://arxiv.org/html/2607.19349v1)

**机制。** 真实 LLM serving 的 scheduler 需要知道请求长度、到达间隔、session 与模型分布；只用合成均匀 trace 会优化错误 operating point。FineServe 提供细粒度全球 workload 数据并刻画这些相关性。

**证据边界。** 论文公开数据与采集/统计结果，可用于验证合成 workload 假设。它不证明样本代表所有地区、供应商或未来流量，也不直接证明某调度器更优；隐私处理和采样偏差限制外推。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19349v1#A3.SS1 — C.1. Architecture-Specific Input–Output Token Models; https://arxiv.org/html/2607.19349v1#S3 — 3. Characterizing Architectures and Scales。Evaluation：https://arxiv.org/html/2607.19349v1#S1 — 1. Introduction; https://arxiv.org/html/2607.19349v1#S2 — 2. Preliminary and Motivation。Limitations / counterevidence：https://arxiv.org/html/2607.19349v1#S6 — 6. Conclusion。

**Trade-off。** 真实 trace 提高 workload fidelity，却会过时并受隐私/覆盖限制；应保留参数化 synthetic stress 与持续漂移检测。

**Books：已有覆盖。** `INFER-SCHEDULING` 已把 model/precision、shape range、arrival/length distribution、parallel mapping 与 SLO 作为同一 workload contract，并明确单字段 proxy 不能决定调度；FineServe 作为测量数据集保留，不重复改正文。

### [Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX](https://arxiv.org/html/2607.19353v1)

**机制。** Confidential GPU 把 CPU enclave、GPU protected path 和模型服务串成新执行边界；安全开启后的开销会随模型规模与并发改变饱和点。论文在 H100+Intel TDX 上测量吞吐、延迟和 saturation。

**证据边界。** 两个模型、单一 GPU 配置的结果显示 confidential inference 在负载下仍有可用吞吐，但大模型更早饱和并有 steady penalty。未证明其他 GPU/TEE、网络、attestation 路径或多 GPU scaling。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19353v1#S3.SS4 — 3.4 Load-Generation Methodology; https://arxiv.org/html/2607.19353v1#S3.SS2 — 3.2 Models and Execution Modes。Evaluation：https://arxiv.org/html/2607.19353v1#A1 — Appendix A Full Closed-Loop Results; https://arxiv.org/html/2607.19353v1#S3 — 3 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19353v1#S7 — 7 Limitations and Threats to Validity; https://arxiv.org/html/2607.19353v1#S6 — 6 Discussion。

**Trade-off。** 机密执行保护数据/权重，却增加加密、隔离和容量 headroom；需要按受保护配置重新做容量规划，不能套用普通实例 SLO。

**Books：仅报告。**`PLATFORM-SECURITY` 已有 confidential-compute contract；本材料提供单平台容量案例。

### [NEXUS: Structured Runtime Safety for Tool-Using LLM Agents](https://arxiv.org/html/2607.19356v1)

**机制。** Tool plan 不能二元 allow/block：风险和不确定性不同，需要 allow、block、request confirmation、request revision 四类 effect policy。NEXUS 在 plan 与执行之间运行结构化 monitor，由 side-effect class 和检查结果决定干预。

**证据边界。** 128 个合成实例上报告 F1 0.949、四类干预准确率 0.6406，并优于 rule-only selector。样本小且合成；未证明开放工具、prompt injection 和真实误拒绝成本，也明确不能替代 alignment、内容过滤与事后审计。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19356v1#S4 — 4 The NEXUS Framework; https://arxiv.org/html/2607.19356v1#A1 — Appendix A Runtime Monitoring Algorithm。Evaluation：https://arxiv.org/html/2607.19356v1#A11 — Appendix K Error Analysis; https://arxiv.org/html/2607.19356v1#A14 — Appendix N R-Judge IoT: Trace-Level Failure Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.19356v1#A14 — Appendix N R-Judge IoT: Trace-Level Failure Analysis; https://arxiv.org/html/2607.19356v1#A17 — Appendix Q Deployment Posture and Future Extensions。

**Trade-off。** 细分干预保留更多 utility，却依赖 risk classifier 并增加用户等待；高风险或低置信 proposal 应默认不提交。

**Books：已有覆盖。** `AGENT-TOOL-CALLING` 已把模型输出限定为 proposal，outcome monitor 只提交 observation/violation evidence，policy 与 executor 持有 authorization/effect commit；NEXUS 的四态 intervention 是这条分权链的具体实现。

### [Stateful Guardrails for Multi-Turn LLM Systems: A Conversational Risk Accumulation Framework](https://arxiv.org/html/2607.19361v1)

**机制。** 单轮 guardrail 会漏掉多轮中逐步累积的敏感实体、语义漂移和 compliance increase。CRA 维护 session anchor、信息积累图与 compliance gradient，把风险作为 trajectory state 更新。

**证据边界。** 作者提供无监督融合、CRA-Net DA 与多数据集/人工迁移评价，支持多轮信号能暴露单轮遗漏。未证明三个信号因果、跨域校准或长 session 不漂移；learned score 也不是安全保证。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19361v1#S4 — 4 The CRA Framework; https://arxiv.org/html/2607.19361v1#S5 — 5 Design Consistency Properties。Evaluation：https://arxiv.org/html/2607.19361v1#S9.SS9 — 9.9 Ablation analysis; https://arxiv.org/html/2607.19361v1#S2.SS1 — 2.1 Multi-turn safety evaluation and dialogue state modeling。Limitations / counterevidence：https://arxiv.org/html/2607.19361v1#S12 — 12 Discussion and Limitations; https://arxiv.org/html/2607.19361v1#S13 — 13 Conclusions。

**Trade-off。** 持久风险 state 提高早期检测，却累积误差并引入隐私/存储成本；需要衰减、解释、人工复核和会话重置。

**Books：仅报告。**`PLATFORM-SECURITY` 已有跨轮 risk state 思路；该具体 feature/fusion 尚不足以成为长期唯一机制。

### [Rethinking Uncertainty Evaluation in Large Language Models](https://arxiv.org/html/2607.19367v1)

**机制。** Token 概率、verbal confidence 和 self-consistency 衡量的对象不同，不能被同一个“置信度”解释。论文将 calibration、faithfulness 和 decision utility 分轴评估。

**证据边界。** 跨论文设定的实验显示现有 confidence estimate 不能普遍视为 coherent probability，且 faithfulness 与 calibration 可分离。未证明存在单一替代指标，也未给部署阈值或跨任务稳定校准。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19367v1#S4 — 4 Methodology; https://arxiv.org/html/2607.19367v1#S4.SS2 — 4.2 Confidence Estimation Methods。Evaluation：https://arxiv.org/html/2607.19367v1#A3 — Appendix C Full Benchmark Results; https://arxiv.org/html/2607.19367v1#A2 — Appendix B Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19367v1#A1.SS2 — A.2 Limitations of LLM-Based Semantic Clustering; https://arxiv.org/html/2607.19367v1#S5 — 5 Discussion。

**Trade-off。** 多轴评估更诚实，但增加标注、重复采样与决策成本；使用时必须声明预测事件、base rate、loss 和校准集。

**Books：仅报告。**`PLATFORM-EVALUATION-SYSTEM` 已将置信度绑定 claim/evidence/decision contract；该研究作为受限校准证据。

### [ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems](https://arxiv.org/html/2607.19430v1)

**机制。** 单个 agent 安全不推出多 agent composition 安全，因为消息通道会重编码、聚合或放大攻击。ChannelGuard 在每条 inter-agent channel 放置 pass/compress/block gate，并记录哪层阻断。

**证据边界。** 2100 条 trace、八类攻击、五种防御、三类 backend 的结果显示表面安全可能主要来自云侧过滤；替换 backend 会改变责任。论文早期 Azure client 曾漏报约12%，也说明测量链会制造假安全。未证明 phrase-bank embedding gate 覆盖新攻击或压缩后语义安全。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19430v1#S4 — 4. The ChannelGuard Framework; https://arxiv.org/html/2607.19430v1#A2 — Appendix B The Full Pipeline Algorithm and Three Further Formal Properties。Evaluation：https://arxiv.org/html/2607.19430v1#A6 — Appendix F Gate Ablation; https://arxiv.org/html/2607.19430v1#S5 — 5. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19430v1#S7 — 7. Discussion and Limitations; https://arxiv.org/html/2607.19430v1#A15 — Appendix O Reproducibility Notes on Two Failure Modes。

**Trade-off。** 逐通道 gate 提高可定位性，却增加误阻、语义损失和配置漂移；provider filter 只能作一层，不能替代本地 authorization。

**Books：已有覆盖。** `AGENT-MULTI-AGENT` 的“Collective Risk”已明确单体通过安全评估不推出组合安全，并把 local utility、communication topology、information partition、aggregation rule 与独立 outcome verifier 纳入合同；该 family 提供受限反例，不需再立平行 gate。

### [ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems](https://arxiv.org/html/2607.19432v1)

**机制。** 逐调用检查只看单步，MCP 攻击可把侦察、权限提升和副作用分散到多个合法调用。ChainWatch 以 kill-chain stage 累积序列证据，在跨步状态达到条件时触发检测。

**证据边界。** 五个文献攻击场景展示其能识别逃过 per-call rule 的链条。未证明检测器在真实 MCP 流量、未知链、并发 session 或 adversarial evasion 下的 recall/false-positive，也无生产性能保证。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19432v1#S2.SS1 — II-A MCP Architecture; https://arxiv.org/html/2607.19432v1#S4 — IV ChainWatch Framework。Evaluation：https://arxiv.org/html/2607.19432v1#S3 — III Threat Analysis; https://arxiv.org/html/2607.19432v1#S5 — V Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.19432v1#S3 — III Threat Analysis; https://arxiv.org/html/2607.19432v1#S6 — VI Conclusion。

**Trade-off。** 序列检测补足单步盲区，却保存更多行为状态并可能延迟阻断；高风险单步仍应即时 gate，不能等完整链。

**Books：仅报告。**它是 `AGENT-MCP` 的受限检测分支，尚无足够证据改通用协议章节。

### [Integrity of peer-to-peer distributed LLM inference under malicious nodes](https://arxiv.org/html/2607.19490v1)

**机制。** P2P 分片推理中，任何节点可篡改传给下一节点的 activation，而终端只看到最终文本。论文插入不可区分的 canary，并按节点 activation variation 给篡改定位。

**证据边界。** 408 个预注册配置中检测 AUROC 1.0，恶意 shard 在所有 canary 上排名高于 benign。威胁模型假设攻击每次都篡改且无法识别 canary；未覆盖 selective attacker、串谋、自然 drift 或通信丢包。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19490v1#S3 — 3 Method; https://arxiv.org/html/2607.19490v1#S4.SS4 — 4.4 Experimental design。Evaluation：https://arxiv.org/html/2607.19490v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.19490v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19490v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.19490v1#S3.SS2 — 3.2 Threat model。

**Trade-off。** canary 提供端到端完整性信号，却消耗推理并可能被学习识别；假设失效时需 cryptographic attestation 或可信重算。

**Books：已有覆盖。** `PLATFORM-SECURITY` 已有该 family 的威胁假设与边界条目，不新增。

### [Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts](https://arxiv.org/html/2607.19539v1)

**机制。** MoE 的 dispatch/compute/gather 串行会让第二次 all-to-all 等待整个 expert compute。论文把完成信号降到 tile 粒度，scheduler 在部分 tile 就绪时重叠通信与后续计算。

**证据边界。** 4×A100、三种 MoE、四个 baseline 上报告最高 2.64×端到端、2.74× MoE-layer。未覆盖 backward、大机器和其他 parallelism，adaptive SM partition 仍属未来工作。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19539v1#S3 — 3. System Design; https://arxiv.org/html/2607.19539v1#S2.SS1 — 2.1. Mixture-of-Experts Architectures。Evaluation：https://arxiv.org/html/2607.19539v1#S4 — 4. Experimental Results; https://arxiv.org/html/2607.19539v1#S4.SS1 — 4.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19539v1#S6 — 6. Conclusion。

**Trade-off。** 细粒度 overlap 隐藏通信，却增加 tile dependency、SM 划分和调度开销；小负载/通信轻时粗粒度路径更简单。

**Books：已有覆盖。** 单一 owner 为 `INFER-TENSORRT-LLM`；目标章已经把 tile completion signal、consumer wait、wraparound/late-message 与粗粒度同步回退写入正文。本材料验证 MoE 中的具体 overlap 实现，不再重复。

### [Do Co-Located AI Training Jobs Synchronize? Load-Dependent Throttling as a Coupling Mechanism for Phase-Locking Behind a Shared Power Cap](https://arxiv.org/html/2607.19638v1)

**机制。** 共享 power cap 下两个训练 job 可通过 load-dependent throttling 相互耦合，使原本独立的 compute phases 逐渐 phase-lock。论文用广义 Kuramoto 模型表达这种反馈，并给出可证伪的双作业测量。

**证据边界。** 当前证据主要是机制模型、operator statements 与拟议测量；它排除了 grid frequency/common forcing 的部分解释，但未证明大规模 fleet 的真实发生率、稳定区间或训练质量影响。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19638v1#S3.SS4 — 3.4 Reduction to a generalized Kuramoto system。Evaluation：https://arxiv.org/html/2607.19638v1#S4 — 4 Analysis; https://arxiv.org/html/2607.19638v1#S6 — 6 Numerical study。Limitations / counterevidence：https://arxiv.org/html/2607.19638v1#S7 — 7 Discussion; https://arxiv.org/html/2607.19638v1#S8 — 8 Conclusion。

**Trade-off。** 错峰可降低峰值，却可能被控制反馈重新同步；调度器需观测功率相位并保留 headroom，过度干预会损失利用率。

**Books：已整合。** `PLATFORM-GPU-SCHEDULER` 的“共享 Power Cap 会把独立训练 Job 耦合成相位系统”已说明 co-located jobs 可经 throttling 和 step-duration 反馈形成动态耦合，静态平均功率与一次错峰不足以保证长期稳定；正文保留动态 cap 振荡、吞吐代价与普通 bin packing 的成立边界。

### [How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF](https://arxiv.org/html/2607.19712v1)

**机制。** RLHF pipeline 在所有 rollout 完成评分前不能更新，reward-model inference 因动态长度/recompile 会成为同步 barrier。论文比较 C++ 与 PyTorch runtime，并用重复独立运行分离编译和 steady-state。

**证据边界。** 重复测量支持单次 benchmark 不稳定，论文 shape distribution 中 recompilation 仍是主要未排除变量。未证明其 60-row 分布代表生产 rollout，也未覆盖异步 scoring、模型质量或端到端收敛。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19712v1#S3 — 3 Methodology; https://arxiv.org/html/2607.19712v1#S3.SS4 — 3.4 Statistical Method。Evaluation：https://arxiv.org/html/2607.19712v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.19712v1#S3.SS7 — 3.7 Hardware and Limitations; https://arxiv.org/html/2607.19712v1#S5 — 5 Discussion。

**Trade-off。** 更专用 runtime 可降评分延迟，但增加编译缓存、shape 管理和数值一致性验证；异步评分还会引入 policy staleness。

**Books：仅报告。**它是 `TRAIN-RLHF` 的 runtime 案例，未形成超出现有 pipeline barrier 的新长期结论。

### [DGNA: Dissecting GPU NUMA Architecture through Microbenchmarking and Data Analysis](https://arxiv.org/html/2607.19922v1)

**机制。** GPU 被抽象为统一内存域，但 L2/DRAM latency 可能呈 NUMA 拓扑，错误 placement 会让同一 kernel 的访问成本不同。DGNA 用微基准测延迟并以混合模型分离 cluster，推断隐藏 topology。

**证据边界。** 论文声称无需 vendor-specific 指令即可分别测 L2/DRAM，并给出所测 GPU 的 NUMA 分析。未证明推断等于厂商物理实现、跨代稳定或可直接预测完整模型性能；outlier filtering 也会影响边界。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19922v1#S4 — 4. Methodology; https://arxiv.org/html/2607.19922v1#S4.SS2 — 4.2. NUMA Architecture Topology。Evaluation：https://arxiv.org/html/2607.19922v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.19922v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.19922v1#S6 — 6. Conclusion。

**Trade-off。** 黑盒拓扑测量可指导 placement，却需每硬件重校准且受噪声影响；不能替代官方一致性/故障语义。

**Books：仅报告。**`INFER-GPU-MEMORY` 可把它作为硬件校准工具，但无需新增正文主线。

### [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/html/2607.19957v1)

**机制。** Position-independent KV reuse 弱化了“只有同前缀/同位置才能命中”的隔离边界，攻击者可构造可迁移 cache 状态影响其他请求。HijackKV 将探测、植入和触发组织为攻击链。

**证据边界。** 论文在其 position-independent multi-tenant reuse 设计与模型上展示漏洞。未证明普通 exact-prefix reuse 同样受影响、所有平台暴露相同探测面，或作者 ASR 跨模型/数据泛化。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.19957v1#S4.SS1 — 4.1 Threat Model。Evaluation：https://arxiv.org/html/2607.19957v1#S6 — 6 Experimental Setup; https://arxiv.org/html/2607.19957v1#S7 — 7 Experiment。Limitations / counterevidence：https://arxiv.org/html/2607.19957v1#S8 — 8 Limitations and Discussion; https://arxiv.org/html/2607.19957v1#S4.SS1 — 4.1 Threat Model。

**Trade-off。** 扩大复用提升 hit rate，却使 position/tenant/provenance 不再天然隔离；必须绑定租户和生成身份，无法验证则禁用跨边界复用。

**Books：已有覆盖。** `PLATFORM-SECURITY` 目标章已有 `semantic-body-binding:SF-2026-ARXIV-2607-19957`，明确 position-independent reuse 的隔离缺口与保守边界；原表 `INFER-KV-CACHE` owner 应改为安全 owner。

### [SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD](https://arxiv.org/html/2607.20145v1)

**机制。** 在 Ascend SuperPOD 上对大 MoE 做全参数 post-training，需要将并行、checkpoint、optimizer 和算子适配成一条硬件绑定 pipeline。SLAI T-Rex 汇总这些联调而非提出通用新优化原理。

**证据边界。** 作者报告 34.22% MFU、相对其开源 baseline 2.93×并保持训练稳定。只支持 DeepSeek-V4 family、Ascend 配置和第一阶段 recipe；未证明单项贡献、其他硬件/模型最优或更多数据单调改善。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20145v1#A3 — Appendix C Solver-Verified OR-CPT Data Synthesis: Engine Design and Illustrative Cases; https://arxiv.org/html/2607.20145v1#A3.SS2 — C.2 End-to-end engine architecture。Evaluation：https://arxiv.org/html/2607.20145v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.20145v1#A4 — Appendix D CPT–SFT–Deployment–Evaluation Provenance。Limitations / counterevidence：https://arxiv.org/html/2607.20145v1#S5 — 5 Conclusion, Limitations, and Future Directions。

**Trade-off。** 硬件协同提高利用率，却增加 vendor lock-in、移植和验证成本；无同等支持时需回退通用 runtime。

**Books：仅报告。** SLAI T-Rex 是绑定 Ascend SuperPOD 与特定模型族的 post-training recipe；目标章中的来源边界不等于出现了新的通用正文机制，因此不以“已有来源”冒充 Books 已吸收。

### [MoX: Efficient MoE Routing on Direct-Connect Topologies](https://arxiv.org/html/2607.20220v1)

**机制。** 直接互联拓扑不能像交换网络按瞬时 expert traffic 任意重配置。MoX 离线优化 load-oblivious routing/tree，使 MoE dispatch 在静态 fabric 上可执行而不依赖实时 traffic matrix。

**证据边界。** 论文在其 simulation/proxy 与 topology/workload 假设下报告相对路由改善。未证明 deadlock-free 真实实现、故障行为、硬件时序或相对 switched fabric 的普遍优势。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.20220v1#S2 — 2. Routing Algorithm。Evaluation：https://arxiv.org/html/2607.20220v1#S3 — 3. Evaluation; https://arxiv.org/html/2607.20220v1#S3.SS4 — 3.4. Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.20220v1#S4 — 4. Discussion; https://arxiv.org/html/2607.20220v1#S6 — 6. Conclusion。

**Trade-off。** 静态路由降低控制复杂度，却可能在 traffic skew/drift 时失配；需拥塞检测与保守 fallback。

**Books：已有覆盖。** `MODEL-MOE` 目标章已有 MoX 的 topology/routing 机制和未证明边界；无需追加。

## 5. 缺口与下一步

无

无 external Materials Request。全部保留候选均可访问 exact-v1；旧候选降级不会删除原始证据。本日所需 Books 写入和写后语义审计均已完成；若后续出现具体 false positive、false negative 或来源更正，只重开对应 family。

准入闭合账目：raw identities=444；旧候选=117；V3 候选=15；本轮从旧候选降级=102。准入前关闭的共同原因是：局部指标或单任务方法没有持久系统增量、垂直应用/AI for Science 越界、benchmark 未改变 evaluation/deployment contract，或机制已被同日更强材料覆盖。

## 6. 复核

复核者：非作者独立复核（/root/aug11_20，2026-09-10）。

结论：通过

写后复核确认 `SF-2026-ARXIV-2607-19638` 已进入 `PLATFORM-GPU-SCHEDULER` 正文的 power-cap coupling 主线，而非只出现在 trace；正文明确它只由特定模型、GPU 与 cap 设置下的实验支持，不外推为任意集群固定现象。
