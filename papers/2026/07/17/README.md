# Daily Research — 2026-07-17

**规范：** V3
**窗口：** 2026-07-16T09:00:00+08:00 ～ 2026-07-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T17:30:00+08:00

## 1. 结论

本窗口按 first-public owner 得到 506 条 arXiv 原始身份。逐条读取标题与完整摘要后，冻结 12 个候选；旧稿的 77 个候选不作为新分母，其中 65 个旧候选因只提供局部方法/benchmark、垂直应用或没有改变长期系统判断而降回准入前关闭。原始证据保留，但不在正文候选表继续制造重要性错觉。

保留材料集中在可迁移状态、训练/推理执行计划、跨层资源约束、证据与安全边界。每项都已用旧稿保存的 exact-v1 primary evidence 重新核对机制与反证；没有用标题关键字替代语义判断，也没有把能映射 ROADMAP 当作准入理由。独立复核已经把“来源存在”和“正文已承载”分开，并确认本日唯一正文增量已进入目标章节且与相邻论证连续。

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
| SRC-ARXIV | [exact-v1 HTML](https://arxiv.org/)；本窗 506 条 identity 逐条 title + 完整摘要语义筛选；旧稿 exact-v1 Method / Evaluation / Limitations 仅作可核实证据种子 | 已检查 | 无 |

本次排除 AI for Science、纯垂直应用、只改局部任务指标以及没有系统状态/控制/评价契约增量的工作。withdrawn 身份不进入候选；本组没有保留 withdrawn family。

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；7～9 分深入审阅，5～6 分标准审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Polestar: Drift-Aware Cache Calibration and Token Commitment for Efficient Inference of Diffusion LLMs](https://arxiv.org/html/2607.14107v1) | 2026-07-17T08:00:00+08:00 | `INFER-KV-CACHE`；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Stop Means Stop: Measuring and Repairing the Enforcement Gap in Agent-Framework Control Primitives](https://arxiv.org/html/2607.14166v1) | 2026-07-17T08:00:00+08:00 | `AGENT-PLATFORM`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[目标章](../../../../books/part-07-agent/84-agent-platform.md) 已有 completion/cancellation、effect-safe replay 与 state machine 正文 |
| [When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models](https://arxiv.org/html/2607.14169v1) | 2026-07-17T08:00:00+08:00 | `MULTIMODAL-WORLD-MODELS`；2 + 2 + 1 = 5 | 标准完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel](https://arxiv.org/html/2607.14431v1) | 2026-07-17T08:00:00+08:00 | `INFER-KV-CACHE`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 已把 token/model/adapter/position/execution identity 作为复用前提 |
| [Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent](https://arxiv.org/html/2607.14541v1) | 2026-07-17T08:00:00+08:00 | `INFER-TENSORRT-LLM`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 已有正确性 admission、实机测量与 reference fallback |
| [Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems](https://arxiv.org/html/2607.14611v1) | 2026-07-17T08:00:00+08:00 | `AGENT-MEMORY`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[目标章](../../../../books/part-07-agent/77-memory.md) 已有 provenance、poisoning test、选择性删除与写入权威边界 |
| [MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents](https://arxiv.org/html/2607.14651v1) | 2026-07-17T08:00:00+08:00 | `AGENT-MEMORY`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[目标章](../../../../books/part-07-agent/77-memory.md) 已沿写入、检索、派生边与回滚描述污染生命周期 |
| [Reflex: Real-Time VLA Control through Streaming Inference](https://arxiv.org/html/2607.14695v1) | 2026-07-17T08:00:00+08:00 | `MULTIMODAL-EMBODIED-VLA`；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 已有异步流、freshness budget 与同步回退 |
| [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/html/2607.14952v1) | 2026-07-17T08:00:00+08:00 | `TRAIN-DISTRIBUTED-TRAINING`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[目标章](../../../../books/part-04-training-system/36-distributed-training.md) 已有 state lifetime、replay 与 gradient/collective 边界 |
| [Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents](https://arxiv.org/html/2607.15143v1) | 2026-07-17T08:00:00+08:00 | `PLATFORM-SECURITY`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) 已分离不可信文本、artifact identity、安装授权与 effect gate |
| [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/html/2607.15207v1) | 2026-07-17T08:00:00+08:00 | `MULTIMODAL-WORLD-MODELS`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/html/2607.15263v1) | 2026-07-17T08:00:00+08:00 | `PLATFORM-EVALUATION-SYSTEM`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |

## 4. 证据与知识整合

### [Polestar: Drift-Aware Cache Calibration and Token Commitment for Efficient Inference of Diffusion LLMs](https://arxiv.org/html/2607.14107v1)

**机制。** 扩散式语言模型在多轮去噪中既会重复计算近似稳定的中间表示，又必须决定何时提交仍可能变化的 token。Polestar 以 representation drift 同时控制 cache reuse 与 token commit：漂移小的状态可复用，收敛的 token 才提交。

**证据边界。** 作者在所测 diffusion-LM、数学与代码任务上报告 accuracy–throughput Pareto 改善，消融支持 drift signal 的作用；最高数字只属于披露配置。未证明漂移在所有模型、长度和分布下都与语义正确性一致，也未覆盖生产并发、尾延迟与错误提交恢复。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.14107v1#S4 — 4 Polestar Methodology; https://arxiv.org/html/2607.14107v1#S4.SS3 — 4.3 Polestar System Optimization。Evaluation：https://arxiv.org/html/2607.14107v1#S5 — 5 Experimental Evaluations; https://arxiv.org/html/2607.14107v1#A4 — Appendix D Additional Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.14107v1#S5.SS3 — 5.3 Discussions and Ablations; https://arxiv.org/html/2607.14107v1#S6 — 6 Conclusions。

**Trade-off。** 少做去噪计算和更早提交换来吞吐，但新增 drift 统计、阈值校准与过早提交风险；信号不稳时应回退逐轮重算和保守提交。

**Books：已整合。** `INFER-KV-CACHE` 的“压缩、漂移与驱逐都需要可检验的误差预算”已经把迭代生成 cache 的 admission/commit 绑定到中间表示稳定度，并规定漂移越界时回退 FullCache/重算；正文同时保留在线估计、metadata、专用 kernel 与校准漂移的代价。

### [Stop Means Stop: Measuring and Repairing the Enforcement Gap in Agent-Framework Control Primitives](https://arxiv.org/html/2607.14166v1)

**机制。** Approval、cancel、timeout 若只暂停调用分支而不能阻止 sibling、replay 或孤儿任务提交副作用，“拒绝”就不是执行语义。论文将控制点移到 effect commit：副作用以持久身份接受 admission，replay 幂等，取消/超时传播到仍存活执行。

**证据边界。** 差分探针在六个开源框架中复现 approval sibling leak，并检查 replay、cancellation orphan 和 timeout zombie；SOUNDGATE 在该测试合同中阻断已测违规。未证明覆盖任意工具、语言 runtime 或分布式故障，也未证明测试中零拒绝等于生产零误拒绝。

**审阅定位。** Method / identity：https://arxiv.org/pdf/2607.14166v1#page=5 — PDF page 5; https://arxiv.org/pdf/2607.14166v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.14166v1#page=15 — PDF page 15; https://arxiv.org/pdf/2607.14166v1#page=20 — PDF page 20。Limitations / counterevidence：https://arxiv.org/pdf/2607.14166v1#page=25 — PDF page 25; https://arxiv.org/pdf/2607.14166v1#page=30 — PDF page 30。

**Trade-off。** effect-time gate 增强停止语义，却要求统一 effect identity、持久日志和取消传播，并增加延迟/可用性依赖；无法可靠识别副作用时应回退隔离或人工确认。

**Books：已有覆盖。** `AGENT-PLATFORM` 已有 completion/cancellation、Session replay 不重复外部 effect、以及 control/evidence plane 分工；本论文提供的是对既有停止语义缺口的受限测量，不再重复写同一协议。

### [When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models](https://arxiv.org/html/2607.14169v1)

**机制。** 平均 transition accuracy 只衡量常见预测，规划结果却可能由少数 pivotal transition 决定。论文将 planner 搜索分布和实际 play outcome 纳入评价，区分预测正确与足以支持决策。

**证据边界。** 在构造的 code-world 中，模型可通过采样 gate 并在搜索分布上保持很高准确率，却因遗漏低频关键规则而系统性失败；rare-rule instrument 将失败定位到关键转移。未证明所有 world model 同样失败，也未证明 play evaluation 能覆盖开放环境的所有安全状态。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.14169v1#S2 — 2 Setup and Methods; https://arxiv.org/html/2607.14169v1#S1.SS1 — 1.1 The Code World Model paradigm。Evaluation：https://arxiv.org/html/2607.14169v1#S2.SS5 — 2.5 Experimental configuration; https://arxiv.org/html/2607.14169v1#S3.SS3 — 3.3 The rare-rule instrument: verified but wrong at play (headline result)。Limitations / counterevidence：https://arxiv.org/html/2607.14169v1#S5.SS4 — 5.4 Conclusion: translation, not inference; https://arxiv.org/html/2607.14169v1#S6 — 6 Imperfect Information: The Inference Function as a New Failure Surface。

**Trade-off。** 按 planner occupancy 或 play 加权能发现均匀采样漏掉的错误，但增加交互 rollout、ground truth 与搜索策略依赖；预测测试仍适合低成本回归。

**Books：仅报告。**`MULTIMODAL-WORLD-MODELS` 已区分 prediction accuracy 与 action-conditioned adequacy；本材料强化受限反例，不新增独立机制正文。

### [Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel](https://arxiv.org/html/2607.14431v1)

**机制。** 外部知识片段的 KV 即使文本相同，也会因位置编码、chunk 边界和浮点执行历史而不同。论文用 own-position graft，并以输入/输出 hash 将组合绑定到可重放的 chunked reference，使 graft 成为带位置与来源身份的状态导入。

**证据边界。** 作者在 12B、31B 和两个 GPU 目标上验证相对 chunked reference 的 byte-exactness，其中一次为预注册 replay。引擎未公开；不保证相对 monolithic execution 字节一致，也未证明跨架构、并发调度和知识更新时安全组合。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.14431v1#S3 — 3 Methodology; https://arxiv.org/html/2607.14431v1#S4.SS10 — 4.10 Cross-architecture byte-exactness: a pre-registered B200 replay。Evaluation：https://arxiv.org/html/2607.14431v1#S4 — 4 Empirical Results。Limitations / counterevidence：https://arxiv.org/html/2607.14431v1#S5 — 5 Discussion; https://arxiv.org/html/2607.14431v1#S5.SS3 — 5.3 Limitations。

**Trade-off。** 复用片段减少 prefill，却要维护 chunk、位置、模型、精度和执行版本身份；identity 不符时应完整重算。

**Books：已有覆盖。** `INFER-KV-CACHE` 已要求跨请求复用同时匹配 token、model revision、adapter、position 与 execution identity；chunk identity 是这一复用身份的具体实例，论文的 byte-exact reference 继续作为受限证据，不另加平行合同。

### [Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent](https://arxiv.org/html/2607.14541v1)

**机制。** 能编译、单测通过或在少数 shape 上变快，不能证明生成 kernel 可进入生产 execution plan。Atrex-Bench 从生产 trace 抽取 operator/shape，并把模型生成 kernel 与 PyTorch fallback 分开，联合检查 correctness、覆盖与 roofline。

**证据边界。** 六个 coding agent 在 30 个 operator、440 个 shapes 上显示标准 protocol 会因 fallback 与窄 shape 高估能力；最佳 vanilla agent 的几何平均仅达论文 roofline 约一成。该 trace/hardware 不代表未来硬件、训练 kernel 或全部 workload，也未证明长期可维护性。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.14541v1#S3 — 3 Atrex-Bench: Design; https://arxiv.org/html/2607.14541v1#S5.SS2 — 5.2 Architecture and Workflow。Evaluation：https://arxiv.org/html/2607.14541v1#A1 — Appendix A Per-Operator Results; https://arxiv.org/html/2607.14541v1#S2.SS1 — 2.1 LLM Kernel Generation Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.14541v1#S6 — 6 Discussion; https://arxiv.org/html/2607.14541v1#S6.SS1 — 6.1 Limitations。

**Trade-off。** 隐藏分布提高外部有效性，却增加 reference、硬件校准和 nondeterminism 检查成本；高风险算子仍应保留人工/供应商 kernel 回退。

**Books：已有覆盖。** `INFER-TENSORRT-LLM` 已有由真实 interface constraints 生成测试、正确性优先 admission、实机测量和 reference fallback 的完整链；本论文补充 benchmark-to-production gap 的证据，但不改变当前正文命题。

### [Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems](https://arxiv.org/html/2607.14611v1)

**机制。** Memory 会把历史文本重新注入未来 prompt，因此写时普通的记录可在后续检索时重新获得控制权。论文分别测试外部内容诱导写入与预植 payload 跨 session 召回，说明写入信任与读取执行信任必须分离。

**证据边界。** 沙箱实验显示直接诱导 agent 覆写 memory 较难，但已植入 payload 能攻击当前及未来 session。证据限所测 agent、memory 文件和模板；未验证任意 substrate，也未证明分层 policy、净化或 capability gate 的生产效果。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.14611v1#S3 — 3. Methods; https://arxiv.org/html/2607.14611v1#S3.SS1 — 3.1. Threat Model and Scope。Evaluation：https://arxiv.org/html/2607.14611v1#S2.SS2 — 2.2. Benchmarks for Agent Security; https://arxiv.org/html/2607.14611v1#S3.SS3 — 3.3. Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.14611v1#S3.SS1 — 3.1. Threat Model and Scope; https://arxiv.org/html/2607.14611v1#S5 — 5. Discussion。

**Trade-off。** 限制写入会丢失有用经验，只在读取时过滤又可能被组合 payload 绕过；需 provenance、trust tier 和 effect-time authorization，异常条目可撤销。

**Books：已有覆盖。** `AGENT-MEMORY` 已明确 attribution 不是事实权威，写入收据必须绑定 provenance、poisoning test、选择性删除与 held-out evaluation；检索到内容也不获得执行授权。该材料保留为针对 prompt-injection memory 的受限验证。

### [MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents](https://arxiv.org/html/2607.14651v1)

**机制。** 单条 memory 在写入时可无害，却会因联合检索或 trigger activation 在执行阶段变成攻击。MemPoison 横跨 injection channel、substrate 和攻击类型，并追踪恶意影响从写入、检索到 effect 的传播。

**证据边界。** 1227 个手工核验案例、多个开放/闭源模型的实验支持 write-time 防御对组合检索和 trigger 激活存在盲区。未证明 benchmark 覆盖所有 memory 架构或真实攻击分布；影响分解也不是任意 agent 的因果保证。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.14651v1#A2 — Appendix B Experimental Design; https://arxiv.org/html/2607.14651v1#A2.SS7 — B.7 MID implementation details。Evaluation：https://arxiv.org/html/2607.14651v1#A1 — Appendix A Benchmark Details; https://arxiv.org/html/2607.14651v1#A1.SS1 — A.1 Benchmark Construction。Limitations / counterevidence：https://arxiv.org/html/2607.14651v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.14651v1#S3 — 3 Threat Model and Taxonomy。

**Trade-off。** 生命周期检测提高覆盖，却增加 lineage、延迟和误报；严格隔离又会损失跨记忆组合，需 quarantine、撤销和恢复路径。

**Books：已有覆盖。** `AGENT-MEMORY` 已沿 source/derived-edge provenance、retrieval channel、selective deletion 与 rollback 描述污染生命周期；本论文揭示的结构盲点可以由现有链解释，不再重复增加一套 threat taxonomy。

### [Reflex: Real-Time VLA Control through Streaming Inference](https://arxiv.org/html/2607.14695v1)

**机制。** 同步 stop-think-act 把视觉编码、去噪和动作执行串在同一时钟。Reflex 利用 perception encoder 不依赖去噪 timestep 的前提，将视觉编码与动作生成异步流水，并融合算子以降低每 tick 开销。

**证据边界。** 作者在其 VLA、任务与硬件设置中报告更高控制频率和任务表现，消融支持 async pipeline 与 fusion。未证明 timestep-invariance 适用于所有 VLA，也不保证异步 action 的 observation freshness 或真实部署安全。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.14695v1#S2.SS3 — 2.3 Design Goals; https://arxiv.org/html/2607.14695v1#S3 — 3 Method: Streaming VLA Inference。Evaluation：https://arxiv.org/html/2607.14695v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.14695v1#A4 — Appendix D Additional Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.14695v1#S5 — 5 Conclusion。

**Trade-off。** 异步降低等待，却新增 observation/plan/action 版本和 freshness mismatch；过期时要缩短 action chunk、重规划或回退同步控制。

**Books：已有覆盖。** `MULTIMODAL-EMBODIED-VLA` 目标章已有 `semantic-body-binding:SF-2026-ARXIV-2607-14695`，明确异步流、freshness budget 与同步回退。

### [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/html/2607.14952v1)

**机制。** 超长上下文 RL 的瓶颈在 rollout、反向传播和更新阶段同时存活的 activation、KV、optimizer 与样本状态。LongStraw 按 objective/architecture 拆分可驻留、回放和虚拟化的状态，以统一 transaction 连接 response replay 与 distributed gradient execution。

**证据边界。** 论文在固定 GPU 预算下给出超长上下文系统结果，并列出未正确运行的配置，支持 state-lifetime 分解影响 device-fit。未证明 2M+ 上下文普遍提升质量，也未证明所有模型、互联和 RL objective 的回放等价或收敛。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.14952v1#S10.SS9 — 10.9 GRPO Systems; https://arxiv.org/html/2607.14952v1#S3 — 3 Architecture Anatomy and Bottleneck Sources。Evaluation：https://arxiv.org/html/2607.14952v1#S9.SS6 — 9.6 Group Scaling Is a Scheduling Result。Limitations / counterevidence：https://arxiv.org/html/2607.14952v1#S11 — 11 Conclusion; https://arxiv.org/html/2607.14952v1#S12 — 12 Limitations and Validation Roadmap。

**Trade-off。** 虚拟化与 replay 换取 device fit，却增加 host/storage traffic、重算、checkpoint identity 和跨阶段一致性；漂移超界时回退短上下文或同步训练。

**Books：已有覆盖。** `TRAIN-DISTRIBUTED-TRAINING` 已有 LongStraw 的正文机制：固定 GPU 下把 resident state lifetime、host/storage replay、page identity、failure recovery 与 gradient/collective 边界放入同一合同；不再重复。

### [Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents](https://arxiv.org/html/2607.15143v1)

**机制。** Coding agent 把 README/setup 文本转成安装命令，因而文档成为供应链控制入口。论文在代码执行前校验 package name、source、version，把 setup 从可信指令降为 untrusted proposal。

**证据边界。** 十二场景、五类攻击和多个 harness 的对照显示 detection 对 harness 与攻击类别敏感；定向提示只修复点名维度，确定性预安装检查关闭大部分已测路径。未证明能识别恶意但合法签名的包或构建脚本。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.15143v1#A5 — Appendix E System Prompt and Review Prompts; https://arxiv.org/html/2607.15143v1#A9 — Appendix I Pre-Install Hook Architecture。Evaluation：https://arxiv.org/html/2607.15143v1#A3 — Appendix C Experimental Setup; https://arxiv.org/html/2607.15143v1#S4 — 4 Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.15143v1#S10 — 10 Limitations and Future Directions; https://arxiv.org/html/2607.15143v1#S11 — 11 Conclusion。

**Trade-off。** 前置校验降低自动安装风险，却增加 setup friction、签名/镜像依赖和误阻断；无法建立 artifact identity 时应停止自动执行。

**Books：已有覆盖。** `PLATFORM-SECURITY` 已把 untrusted repository content 与执行许可分离，并要求 package namespace/registry、publisher signature、artifact identity 和 effect-time authorization；setup 文档是该威胁链的一个入口，不另建机制。

### [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/html/2607.15207v1)

**机制。** World-Action Model 的未来画面合理，不保证动作与该未来保持因果一致。BadWAM 用小视觉扰动破坏 imagined future 与 executed action 的对齐，把攻击面从感知误差推进到 world/action coupling。

**证据边界。** 作者在所测模型和 closed-loop 任务中观察到任务成功率下降，说明生成质量不能单独充当动作安全证据。未证明所有 WAM 同样脆弱，也未证明扰动在真实传感、物理噪声或不同 controller 下可实现。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.15207v1#S2.SS2 — 2.2 Attacks against Embodied AI Systems; https://arxiv.org/html/2607.15207v1#S4.SS1 — 4.1 Design Motivation。Evaluation：https://arxiv.org/html/2607.15207v1#A1 — Appendix A Details of Experiment Setup; https://arxiv.org/html/2607.15207v1#A1.SS1 — A.1 Full and Subset Evaluation Protocols。Limitations / counterevidence：https://arxiv.org/html/2607.15207v1#S3 — 3 Threat Model; https://arxiv.org/html/2607.15207v1#S5.SS2 — 5.2 BadWAM Reliably Induces Task Failures。

**Trade-off。** 检查 dream/action consistency 可发现图像指标漏掉的风险，但需 counterfactual rollout 和控制 ground truth；最终 commit 仍应由安全 controller 拥有。

**Books：仅报告。**它是 World Model/VLA 的受限安全反例；当前证据不足以形成通用防御机制。

### [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/html/2607.15263v1)

**机制。** 成功率会把昂贵多次重试与低成本稳定成功等同。论文把模型调用、token/行动成本与攻防角色纳入同一评价，比较 cost–success frontier。

**证据边界。** 作者在其攻防任务、模型版本和价格假设下观察到 red/blue agent 不同 scaling regime。未覆盖后续 benchmark 版本；价格与模型会变化，也未证明更高成本带来更高真实安全性或 judge 无偏。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.15263v1#A2 — Appendix B Uncertainty Method; https://arxiv.org/html/2607.15263v1#S3 — 3 Evaluation Design。Evaluation：https://arxiv.org/html/2607.15263v1#S4 — 4 Evaluation Results; https://arxiv.org/html/2607.15263v1#A1 — Appendix A Evaluation Run Dates。Limitations / counterevidence：https://arxiv.org/html/2607.15263v1#S7 — 7 Limitations; https://arxiv.org/html/2607.15263v1#S9 — 9 Conclusion。

**Trade-off。** 成本评价更接近运营选择，却受定价、重试策略和 evaluator 定义影响；固定预算下 success-only 回归仍有价值。

**Books：仅报告。**`PLATFORM-EVALUATION-SYSTEM` 已要求 workload/cost/evaluator contract；该攻防案例不改变现有机制。

## 5. 缺口与下一步

无

无 external Materials Request。全部保留候选均可访问 exact-v1；旧候选降级不会删除原始证据。本日所需 Books 写入和写后语义审计均已完成；若后续出现具体 false positive、false negative 或来源更正，只重开对应 family。

准入闭合账目：raw identities=506；旧候选=77；V3 候选=12；本轮从旧候选降级=65。准入前关闭的共同原因是：局部指标或单任务方法没有持久系统增量、垂直应用/AI for Science 越界、benchmark 未改变 evaluation/deployment contract，或机制已被同日更强材料覆盖。

## 6. 复核

复核者：非作者独立复核（/root/aug11_20，2026-09-10）。

结论：通过

除重新核对本窗、来源适用性、候选身份、exact-v1 定位和各项证据边界外，写后复核确认 `SF-2026-ARXIV-2607-14107` 已进入 `INFER-KV-CACHE` 正文的误差预算主线，而非只停留在 trace 或 Review notes；owner、回退边界与前后段衔接成立。
