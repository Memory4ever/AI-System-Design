# Daily Research — 2026-07-31

**规范：** V3
**窗口：** 2026-07-30T09:00:00+08:00 ～ 2026-07-31T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T15:11:09+08:00

## 1. 结论

本窗 arXiv 官方 owner inventory 含 599 个去重身份。旧 V2.1 报告完成了逐项题摘筛选与 84 个 exact-v1 审阅，但把大量“能映射章节”的局部方法也列入候选，准入与评分均偏宽。作者侧原先保留 26 个材料家族、将 58 项转回逐项 pre-denominator closure。独立复核对降级项做 false-negative 抽检后，恢复 7 个明确改变 evaluation、KV、GPU admission 或 Agent control contract 的材料家族；当前分母为 33，pre-denominator closure 为 51。原始题摘、排除理由和旧审阅仍保存在本日 _sources 与 Git 历史中，不因报告压缩而删除证据。

保留项集中在五条真正改变长期设计判断的路线：跨硬件 kernel/Agent evaluation 不能只报成功率；Agent 权限、记忆和多 Agent credit 必须落到可验证状态；MLA、低比特、动态宽度、KV identity 与 PD transfer 都把近似执行的正确性边界显式化；多模态训练、VLA 与 World Model 需要区分表示、可控 transition 和物理反馈；反思与上下文注入的价值必须在等预算、跨 agent 的受控实验中验证。24 项长期增量已进入对应 Books 的机制正文，9 项由现有论证承载而无需重复追加。

原 26 项的证据与 Books 对读已完成独立抽检；新恢复的 7 项中，3 项由现有正文命题承载，4 项已经由共享文件 owner 写入并完成非作者 post-write 复核。Books trace 的日期 owner 也已统一修正到北京时间窗口所属的 2026-07-31。终审发现的 KernelGenBench 与 Flow-Matching Uncertainty 正文缺口已并入各自既有 canonical 机制段，没有另建重复论证；本报告现已闭环。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-ANTHROPIC | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-GOOGLE-AI | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-META-AI | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-QWEN | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-DEEPSEEK | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-MOONSHOT | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-ZAI | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-MINIMAX | 当前每日清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-ARXIV | 官方分类列表、v1 history 与 availability schedule；599 个跨分类去重身份，题摘筛选记录见 _sources/daily-20260731/ | 已检查 | 无 |

本窗没有实际触发需要另行扫描的按需来源。arXiv 日期按官方首次公告归属；技术结论只使用 exact v1，不把 DataCite 等身份元数据当作机制证据。

## 3. 候选与判断

公开时间表示官方公告落入本窗的可证范围，不是作者提交时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Multi-Head Attention Residuals](https://arxiv.org/html/2607.27230v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将单一 residual stream 扩展为跨深度可学习路由，显式交换表达力、跨层状态和执行成本；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER，[Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [KernelGenBench](https://arxiv.org/html/2607.27231v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 把 kernel 生成评价从单源单卡成功率扩为多算子、多芯片、成本与移植失败合同；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Asymmetric Collapse in Model Merging](https://arxiv.org/html/2607.27240v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 受控展示安全 task-vector 尺度不平衡会让合并结果从识别坍缩为泛化拒答；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Do Context Files Help Coding Agents?](https://arxiv.org/html/2607.27250v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 用跨两个 agent 的真实仓库消融限制“更多持久 context 必然更好”的主张；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [FAVA](https://arxiv.org/html/2607.27267v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将静态 tool permission 演进为携带证据、随 runtime state 变化的授权图；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Beyond KV Reconstruction](https://arxiv.org/html/2607.27269v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 证明 standalone generation 的 MLA 重构误差可能在 speculative acceptance 上被放大，draft 必须按目标函数验证；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [LayerRAG-Bench](https://arxiv.org/html/2607.27353v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 把 RAG 可靠性拆为 evidence、tool contract、authorization 与 session state，避免总分掩盖层级故障；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Explorative Modeling](https://arxiv.org/html/2607.27372v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 把多模态分布的多解压力从生成过程移到训练匹配过程，形成与 AR/diffusion 不同的分支；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Subtract, Transport, or Replay?](https://arxiv.org/html/2607.27539v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将语言模型记忆删除拆成参数减法、表示运输和训练重放，并要求可审计删除证据；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MEMORY / PLATFORM-SECURITY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [GyRot](https://arxiv.org/html/2607.27694v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 揭示全局 rotation 与局部 group scale 的错位，要求量化算法与硬件数据通路共同设计；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [ChronoMem](https://arxiv.org/html/2607.27773v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将 forward-only agent memory 改为版本化、可检查、可语义回滚的状态历史；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [RedFlow](https://arxiv.org/html/2607.27782v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将 VLA flow-matching 的失败信号重定向为 action-level correction，而非仅重采样视觉轨迹；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [MemTxn](https://arxiv.org/html/2607.27834v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 为 source-supported memory update 建立提交边界与完整状态恢复，避免部分写入污染长期记忆；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [The Geometry of Flow-Matching Uncertainty](https://arxiv.org/html/2607.27933v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 提出 VLA flow geometry 的局部不确定性 sensor，并把它限定为 failure detection 而非事实保证；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Safeguards Based on Copyable Context Cannot Provide Reliable Safety](https://arxiv.org/html/2607.27951v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 说明可复制进 prompt/context 的安全规则不能成为不可绕过 authority，必须下沉到外部 enforcement；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MARS-RA](https://arxiv.org/html/2607.27967v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 用多模态比较与 rank aggregation 分配 embodied multi-agent credit，暴露 judge correlation 与归因边界；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [SemPIC](https://arxiv.org/html/2607.28069v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将 cache identity 从固定绝对位置提升为可学习的语义位置不变表示，并保留边界 conditioning 失配；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-VLLM，[Ch50](../../../../books/part-05-inference-system/50-vllm.md) |
| [SmartGen](https://arxiv.org/html/2607.28150v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 在生成负载中选择性迁移 KV，将 PD 解耦的收益与 transfer volume、reuse 和 fallback 绑定；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-PD-DISAGGREGATION，[Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Correcting What You Cannot See](https://arxiv.org/html/2607.28336v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将多模态 on-policy distillation 的失败拆为 perception 与 reasoning，使用 disagreement 约束 credit；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [How Benchmarks Mis-Score Computer-Use Agents](https://arxiv.org/html/2607.28367v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 把 CUA 评分链拆为 task、trajectory observation、oracle 与 reporting，修正单一成功率的权威边界；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [QQWorld](https://arxiv.org/html/2607.28415v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 用 quantile matching 修复 latent world-model tail gradient 消失，并显式付出跨 batch 估计成本；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [WIDE](https://arxiv.org/html/2607.28418v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将静态结构剪枝演进为 token-level 动态宽度选择，并要求 kernel 真正消费 routing decision；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Stage-Replay Divergence Follows the KV Cache](https://arxiv.org/html/2607.28495v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 用双向 cache transplant 表明相同 token prefix 不代表相同执行状态，重放 identity 必须包含 KV 与 precision；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Sample More, Reflect Less](https://arxiv.org/html/2607.28576v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 在等 token 预算下比较 self-refine、Reflexion 与独立采样，限制“增加反思轮次必然更好”的主张；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [OSReward](https://arxiv.org/html/2607.28609v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将 CUA reward-model 评价绑定完整 trajectory、跨平台状态与分层 failure taxonomy；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PhiZero](https://arxiv.org/html/2607.28624v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 用离散 physical language 显式表示 world-state transition，区分视频生成与可操作动态；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [BMOA](https://arxiv.org/html/2607.27270v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将 compiler 数值偏差从单一 pass/fail 拆为 baseline、mechanism 与 outcome 三层可审计归因；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Back from the Future](https://arxiv.org/html/2607.27600v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 用基于现有 KV 的 counter-causal pass 估计 token 冗余，显式引入 refresh work 与近似误差；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ClawTrack](https://arxiv.org/html/2607.28037v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 把 Agent outcome 与 process evidence 分开，避免 lucky success 掩盖轨迹缺陷；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / PLATFORM-TRACE，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Queue-Theoretic Admission Control for Multi-Tenant GPU Clusters](https://arxiv.org/html/2607.28223v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将 pending workload 分成可报价与不可行集合，并把等待界与多资源 packing、稳定性假设绑定；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-GPU-SCHEDULER，[Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [One Human, N Agents](https://arxiv.org/html/2607.28317v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 证明相关且失准的 self-confidence 可能使有限人工审计劣于随机抽查，改变 fleet oversight 策略；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Why Are GUI Agents Correct but Late?](https://arxiv.org/html/2607.28399v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 将 Decode 从平均延迟问题提升为 transient action 的 decision-time critical path，并以预编译 policy tree 移出在线生成；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-DECODE，[Ch44](../../../../books/part-05-inference-system/44-decode.md) |
| [Rethinking Inference-Time Scaling in Local Computer-Use Agents](https://arxiv.org/html/2607.28573v1) | 2026-07-31T08:00:00+08:00 ～ 2026-07-31T09:00:00+08:00 | 区分 context、horizon、decomposition 与 parallel sampling 的成本和 failure migration，限制“更多 test-time compute 必然更好”；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |

## 4. 证据与知识整合

### [Multi-Head Attention Residuals](https://arxiv.org/html/2607.27230v1)

Exact v1 的方法与 ablation 支持把历史深度状态作为 learned routing 的候选输入；收益随所测规模增长，但没有证明跨模型与分布式执行的普适收益。Ch17 已明确保存额外 activation、顺序依赖和跨 stage 通信代价。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27230v1#S2 — 2 Method: Multi-Head Attention Residuals。Evaluation：https://arxiv.org/html/2607.27230v1#S3 — 3 Experiments; https://arxiv.org/html/2607.27230v1#S4 — 4 Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.27230v1#S5 — 5 Conclusion。
- **取舍与回退：** 跨层路由扩大可访问深度状态，却增加 activation 存活期、顺序依赖和 pipeline 通信；模型或并行布局不支持时保留标准 residual stream。

### [KernelGenBench](https://arxiv.org/html/2607.27231v1)

Exact v1 同时报告 operator source、目标芯片、correctness、生成方式和 token cost，跨平台退化说明单卡成功率不可外推。Ch66 的 Kernel Benchmark 机制正文已承载这一 evaluation identity。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27231v1#A1 — Appendix A Prompt Design; https://arxiv.org/html/2607.27231v1#S3.SS3 — 3.3 Evaluation Framework。Evaluation：https://arxiv.org/html/2607.27231v1#A9 — Appendix I Fast p Evaluation and Cost Results; https://arxiv.org/html/2607.27231v1#S4 — 4 Experiments and Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.27231v1#A11 — Appendix K Platform-Specific Failure Patterns; https://arxiv.org/html/2607.27231v1#S2.SS2 — 2.2 Limitations of Existing Benchmarks。
- **取舍与回退：** 跨算子、跨芯片评价提高外部有效性，却增加 reference kernel、硬件校准和生成预算；未通过 correctness/target-chip gate 时回退供应商或人工 kernel。

### [Asymmetric Collapse in Model Merging](https://arxiv.org/html/2607.27240v1)

受控 Gemma-3-1B-IT case 支持 task-vector magnitude imbalance 会偏向 refusal update；单一模型和两项安全目标不足以证明一般合并规律。Ch72 已要求对每项行为能力独立做 pre/post-merge regression。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27240v1#A2.SS0.SSS0.Px1 — Method; https://arxiv.org/html/2607.27240v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.27240v1#S3 — 3 Experimentation and Results; https://arxiv.org/html/2607.27240v1#S2.SS0.SSS0.Px3 — Merge configuration and evaluation.。Limitations / counterevidence：https://arxiv.org/html/2607.27240v1#S4 — 4 Limitations and Future Work; https://arxiv.org/html/2607.27240v1#S5 — 5 Conclusion。
- **取舍与回退：** 按 task-vector 尺度校正可降低 refusal 偏置，却可能牺牲另一安全能力；合并前后逐能力回归未通过时撤销 merge，保留独立模型或原 checkpoint。

### [Do Context Files Help Coding Agents?](https://arxiv.org/html/2607.27250v1)

两个 agent、17 个任务和 288 次运行没有给出 context injection 的稳定 correctness 增益，且论文明确不是充分功效的等价性证明。Ch75 已把 context 当作需按任务、agent、冲突和 token cost 验证的输入，不需新增普遍结论。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27250v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.27250v1#A1 — Appendix A Experimental Harness Details; https://arxiv.org/html/2607.27250v1#A2 — Appendix B Per-Task Results。Limitations / counterevidence：https://arxiv.org/html/2607.27250v1#S5 — 5 Discussion; https://arxiv.org/html/2607.27250v1#S6 — 6 Conclusion。
- **取舍与回退：** 持久 context 可能提供任务知识，也会带来 token 成本、冲突和 agent-specific regression；未在匹配任务与 agent 上显示净增益时不注入或回退最小上下文。

### [FAVA](https://arxiv.org/html/2607.27267v1)

Permission-carrying graph 在所测 trace-conditioned 场景中拦截动态违规，但 DCR 不能覆盖未建模状态、身份或外部副作用。Ch72 的机制正文已将授权前移到 effect commit。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27267v1#Sx3 — FAVA Method; https://arxiv.org/html/2607.27267v1#Sx3.SSx6 — Security Assumptions and System Scope。Evaluation：https://arxiv.org/html/2607.27267v1#Sx5 — Experiments; https://arxiv.org/html/2607.27267v1#Sx5.SSx1 — RQ1: Main Permission-Compliance Result。Limitations / counterevidence：https://arxiv.org/html/2607.27267v1#Sx5.SSx5 — RQ5: Failure Analysis; https://arxiv.org/html/2607.27267v1#Sx6 — Discussion。
- **取舍与回退：** 动态权限图能表达运行时证据，却新增图版本、状态覆盖和误拒绝；状态或 principal 无法绑定时回退最小静态权限、隔离执行和人工批准。

### [Beyond KV Reconstruction](https://arxiv.org/html/2607.27269v1)

192 个披露配置显示，MLA 转换后的 reconstruction quality 与 speculative acceptance 不是同一目标。Ch48 的机制正文已要求 draft 按目标模型行为而非局部 cache 误差验收。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27269v1#Sx4 — Method。Evaluation：https://arxiv.org/html/2607.27269v1#Sx6 — Results and Analysis; https://arxiv.org/html/2607.27269v1#Sx5 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27269v1#Sx7 — Discussion; https://arxiv.org/html/2607.27269v1#Sx8 — Limitations。
- **取舍与回退：** 以 acceptance 校准 MLA draft 能减少 verifier waste，却要求 target-aligned 测量并可能失去重构率优势；agreement 不达标时回退原 draft 或完整 target decode。

### [LayerRAG-Bench](https://arxiv.org/html/2607.27353v1)

九类 fault scenario 将 evidence、tool、authorization 与 session state 分离，证明层级 credit 不能由最终回答分数替代；合成 corpus 仍限制外推。Ch66 已承载该分层合同。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27353v1#S2 — 2 Benchmark and Methods; https://arxiv.org/html/2607.27353v1#S2.SS1 — 2.1 Benchmark design and threat model。Evaluation：https://arxiv.org/html/2607.27353v1#A1 — Appendix A Additional Live-Matrix Results; https://arxiv.org/html/2607.27353v1#S2 — 2 Benchmark and Methods。Limitations / counterevidence：https://arxiv.org/html/2607.27353v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.27353v1#S2.SS1 — 2.1 Benchmark design and threat model。
- **取舍与回退：** 分层故障注入提高归因能力，却增加合成场景与 layer oracle 的维护成本；无法建立层级 ground truth 时保留端到端失败并转人工诊断。

### [Explorative Modeling](https://arxiv.org/html/2607.27372v1)

该分支在训练时探索多个 generation-data matching 并选择匹配，改变的是多解分布的 factorization，而非简单增加采样。Ch24 已保留其训练成本、selection bias 和有限任务边界。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27372v1#A3 — Appendix C Approach Details; https://arxiv.org/html/2607.27372v1#A5.SS3 — E.3 Explorative Modeling Based Methods。Evaluation：https://arxiv.org/html/2607.27372v1#S4 — 4 Experimentation and Results; https://arxiv.org/html/2607.27372v1#A1 — Appendix A Additional Experimentation。Limitations / counterevidence：https://arxiv.org/html/2607.27372v1#S7 — 7 Limitations and Conclusion; https://arxiv.org/html/2607.27372v1#S5 — 5 Discussion。
- **取舍与回退：** 训练期探索多种 matching 能覆盖多解分布，却增加候选生成、选择偏差和训练成本；选择器不稳时回退固定 factorization 或显式多样性基线。

### [Subtract, Transport, or Replay?](https://arxiv.org/html/2607.27539v1)

论文比较多类可审计删除路径，支持把参数影响、行为拒答与可恢复知识分开；它不证明某一删除方法在开放模型上普遍成立。Ch72/77 已有该 separation 与 provenance 责任。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27539v1#S3.SS5 — 3.5 Recovering the redesigned memory; https://arxiv.org/html/2607.27539v1#S3.SS6 — 3.6 The exact decrement, audited at the model output。Evaluation：https://arxiv.org/html/2607.27539v1#A1 — Appendix A Experimental details; https://arxiv.org/html/2607.27539v1#A2 — Appendix B Full 1B utility results。Limitations / counterevidence：https://arxiv.org/html/2607.27539v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.27539v1#S8 — 8 Discussion: deletion is a property of representation。
- **取舍与回退：** 可审计删除把参数影响与行为拒答分开，却增加 provenance、重放成本和残留验证；无法证明影响移除时回退隔离 checkpoint、重训或停止删除声明。

### [GyRot](https://arxiv.org/html/2607.27694v1)

Exact v1 将 rotation 与 fine-grained group scaling 的 mismatch 落到硬件数据通路；作者结果只属于披露模型与 accelerator。Ch49 的机制正文已把 granularity、layout 和 dense fallback 绑定。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27694v1#S5 — V GyRot Microarchitecture; https://arxiv.org/html/2607.27694v1#S3.SS1 — III-A Model Accuracy Perspective。Evaluation：https://arxiv.org/html/2607.27694v1#S6 — VI Evaluation; https://arxiv.org/html/2607.27694v1#S6.SS1 — VI-A Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27694v1#S7 — VII Conclusion。
- **取舍与回退：** rotation 与 group scale 联合设计提高低比特可用性，却绑定 layout 与 accelerator 数据通路；目标硬件不支持或误差超界时回退既有量化粒度或 dense kernel。

### [ChronoMem](https://arxiv.org/html/2607.27773v1)

版本选择和 semantic rollback benchmark 支持长期记忆需要历史状态与回滚语义；线性历史不证明并发分支一致性。Ch77 的机制正文已承载这一边界。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27773v1#S3 — 3. System Design of ChronoMem: The Natural Language “Undo” Button of Agent Memory; https://arxiv.org/html/2607.27773v1#S3.SS2 — 3.2. Architecture Overview。Evaluation：https://arxiv.org/html/2607.27773v1#S2.SS3 — 2.3. Memory Retrieval and Evaluation; https://arxiv.org/html/2607.27773v1#S4 — 4. Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27773v1#S6 — 6. Conclusion; https://arxiv.org/html/2607.27773v1#Sx1 — Limitations。
- **取舍与回退：** 版本化记忆支持语义回滚，却增加历史存储、冲突和分支一致性问题；无法确定正确 revision 时回退源记录重建并暂停自动合并。

### [RedFlow](https://arxiv.org/html/2607.27782v1)

方法将 flow-matching VLA 的失败重定向为 action-level correction；收益限于作者控制任务，不等于现实物理安全。Ch26 已把 correction 放在 controller 与 environment feedback 之间。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27782v1#S3 — 3 Methodology; https://arxiv.org/html/2607.27782v1#A3 — Appendix C Simulation Implementation Details。Evaluation：https://arxiv.org/html/2607.27782v1#S4 — 4 Experiment; https://arxiv.org/html/2607.27782v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27782v1#A6 — Appendix F Limitations; https://arxiv.org/html/2607.27782v1#S5 — 5 Conclusion。
- **取舍与回退：** action-level correction 可减少整段重采样，却依赖失败定位和控制时延；sensor 未校准或安全 envelope 被突破时回退外部 controller、重新规划或人工接管。

### [MemTxn](https://arxiv.org/html/2607.27834v1)

该工作把 source-supported update 与完整状态恢复组织成 transaction boundary，针对的是部分写入和污染，而非一般数据库 ACID 证明。Ch77 的机制正文已保存 candidate、commit 与 rollback 分离。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27834v1#Sx3 — Method; https://arxiv.org/html/2607.27834v1#Sx3.SSx2 — System model and trust boundary。Evaluation：https://arxiv.org/html/2607.27834v1#Sx4 — Experiments; https://arxiv.org/html/2607.27834v1#Sx4.SSx1 — Evaluation Overview。Limitations / counterevidence：https://arxiv.org/html/2607.27834v1#Sx5 — Discussion and Limitations; https://arxiv.org/html/2607.27834v1#Sx6 — Conclusion。
- **取舍与回退：** 事务式 memory update 避免部分写入，却增加日志、验证和恢复成本；source support 或原子提交无法证明时丢弃 candidate update 并恢复上一版本。

### [The Geometry of Flow-Matching Uncertainty](https://arxiv.org/html/2607.27933v1)

Flow geometry 可作所测 VLA 的 failure sensor，但不是 correctness probability 或跨模型校准值。Ch26 已把它限制在 safety monitor，并保留外部观察和人工接管。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27933v1#S4.SS2 — 4.2 Method; https://arxiv.org/html/2607.27933v1#A5 — Appendix E Toy Model Implementation Details。Evaluation：https://arxiv.org/html/2607.27933v1#A6 — Appendix F Failure-Detection Experimental Details; https://arxiv.org/html/2607.27933v1#A7 — Appendix G Ablation Study on Failure Detection。Limitations / counterevidence：https://arxiv.org/html/2607.27933v1#A1.SS1 — A.1 How Works as a Failure Score?; https://arxiv.org/html/2607.27933v1#A6 — Appendix F Failure-Detection Experimental Details。
- **取舍与回退：** flow geometry 提供低成本风险信号，却存在跨模型校准漂移且不是 correctness probability；信号不可靠时只能触发减速或重规划，并由外部观察或人工决定 action commit。

### [Safeguards Based on Copyable Context Cannot Provide Reliable Safety](https://arxiv.org/html/2607.27951v1)

论文的核心反证是：可被模型读写的 safeguard 不能成为不可绕过 authority。Ch72 已通过模型外 authorization、policy revision 和 effect-time enforcement 完整承载，不重复追加。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27951v1#S3.SS7 — 3.7 Design Implications。Evaluation：https://arxiv.org/html/2607.27951v1#S3 — 3 Main Result。Limitations / counterevidence：https://arxiv.org/html/2607.27951v1#S5 — 5 Limitations; https://arxiv.org/html/2607.27951v1#S6 — 6 Conclusion。
- **取舍与回退：** 模型外 safeguard 提高不可绕过性，却增加独立 policy/effect gate 的延迟与运维成本；外部 authority 不可用时应 fail closed，而不是把规则复制回 prompt 充当保证。

### [MARS-RA](https://arxiv.org/html/2607.27967v1)

多模态比较和 rank aggregation 提供局部 credit signal，同时引入 judge correlation 和 attribution error。Ch82 的机制正文已要求保存 evaluator identity 与独立 verifier 回退。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27967v1#S5 — 5 Method。Evaluation：https://arxiv.org/html/2607.27967v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.27967v1#A4 — Appendix D Experiments on Overcooked and Pistonball。Limitations / counterevidence：https://arxiv.org/html/2607.27967v1#S10 — 10 Limitations; https://arxiv.org/html/2607.27967v1#S9 — 9 Conclusion。
- **取舍与回退：** rank aggregation 能合并多模态局部判断，却放大相关 judge bias 与 credit error；相关性或分歧超界时保留逐 evaluator 结果并回退独立 verifier 或人工。

### [SemPIC](https://arxiv.org/html/2607.28069v1)

Position-independent cache 通过学习语义表示减弱位置耦合，但 boundary conditioning 仍会留下误差。Ch50 已把它作为可验证 reuse 分支，而非无条件通用 cache。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28069v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28069v1#S2 — 2 Background: Position-Independent Caching。Evaluation：https://arxiv.org/html/2607.28069v1#A4 — Appendix D Evaluation Details; https://arxiv.org/html/2607.28069v1#S4 — 4 Motivating Analysis: Boundary Conditioning Leaves an Interior Gap。Limitations / counterevidence：https://arxiv.org/html/2607.28069v1#S7 — 7 Conclusion。
- **取舍与回退：** 位置不变表示提高 cache reuse，却可能丢失 boundary conditioning 与执行身份；compatibility probe 失败时回退位置绑定 KV 或完整 prefill。

### [SmartGen](https://arxiv.org/html/2607.28150v1)

Selective KV transfer 只有在复用收益超过传输与协调成本时成立。Ch55 的机制正文已把 transfer volume、命中、SLO 与 dense recompute fallback 放入同一决策。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28150v1#S4 — 4 The SmartGen Design; https://arxiv.org/html/2607.28150v1#S6.SS1 — 6.1 LLM Inference Systems。Evaluation：https://arxiv.org/html/2607.28150v1#S3 — 3 Analysis of KV Cache Transfer; https://arxiv.org/html/2607.28150v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.28150v1#S4.SS4 — 4.4 Discussions; https://arxiv.org/html/2607.28150v1#S7 — 7 Conclusion。
- **取舍与回退：** 选择性传输减少网络与 prefill work，却增加命中预测、传输协调和 stale-state 风险；收益不覆盖 transfer cost 或 SLO 越界时回退本地重算。

### [Correcting What You Cannot See](https://arxiv.org/html/2607.28336v1)

Teacher-student disagreement 与 downstream failure 共同识别可修正 perception error；2B matched ablation 支持组件贡献但不能外推规模规律。Ch29 已保留 verifier bias 与 perception/reasoning credit separation。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28336v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28336v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.28336v1#S4 — 4 Experiments; https://arxiv.org/html/2607.28336v1#S4.SS1 — 4.1 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.28336v1#S4.SS5 — 4.5 Limitations and Threats to Validity; https://arxiv.org/html/2607.28336v1#S5 — 5 Conclusion。
- **取舍与回退：** 按 perception/reasoning 分配纠正信号能减少错误 credit，却依赖 disagreement 与 downstream verifier；verifier 偏置或错误不可观测时回退未分解蒸馏和人工标注。

### [How Benchmarks Mis-Score Computer-Use Agents](https://arxiv.org/html/2607.28367v1)

论文展示 task、trajectory observation、oracle 与 aggregate reporting 可分别制造误判。Ch66 的机制正文已把 score provenance 与 failure taxonomy 写入 EvalSpec。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28367v1#S2 — 2 Evaluation Reliability Framework; https://arxiv.org/html/2607.28367v1#S5 — 5 Designing Reliable Benchmarks。Evaluation：https://arxiv.org/html/2607.28367v1#A1 — Appendix A Benchmark Details; https://arxiv.org/html/2607.28367v1#A3.SS3 — C.3 Dynamic Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.28367v1#A2 — Appendix B Failure-Taxonomy Details; https://arxiv.org/html/2607.28367v1#A3 — Appendix C Future-Direction Details。
- **取舍与回退：** 保存完整评分链提高误判定位，却增加 trajectory、oracle 与版本数据的存储和复核成本；任一环缺失时只报告受限分数，不据此发布通用能力结论。

### [QQWorld](https://arxiv.org/html/2607.28415v1)

Quantile matching 针对 EP objective 的 tail-gradient 衰减，cross-batch 估计则增加状态和分布假设。Ch25 已把它定位为 latent regularization，而非物理因果正确性证明。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28415v1#S3 — 3 Method; https://arxiv.org/html/2607.28415v1#S2.SS1 — 2.1 Latent World Models for Planning。Evaluation：https://arxiv.org/html/2607.28415v1#S4 — 4 Experiments; https://arxiv.org/html/2607.28415v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.28415v1#S5 — 5 Conclusion。
- **取舍与回退：** quantile matching 保留 tail pressure，却引入跨 batch 统计状态和分布稳定假设；估计漂移时回退原 objective、扩大样本或停止把 latent score 当环境正确性。

### [WIDE](https://arxiv.org/html/2607.28418v1)

Token-level dynamic width 只有被实际 attention/GEMM kernel 消费才可能获得端到端收益；训练和 gather/scatter 成本不能忽略。Ch49 的机制正文已保留 dense path 与部署边界。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28418v1#S3 — 3 WIDE: Preliminary, Training, and Inference Design; https://arxiv.org/html/2607.28418v1#A1 — Appendix A The Cost for Naive Gather-Scatter Implementations。Evaluation：https://arxiv.org/html/2607.28418v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.28418v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.28418v1#S5 — 5 Conclusion。
- **取舍与回退：** 动态宽度减少部分 token 计算，却增加 routing、gather/scatter 和专用 kernel 成本；端到端收益或质量 gate 不成立时回退静态宽度 dense path。

### [Stage-Replay Divergence Follows the KV Cache](https://arxiv.org/html/2607.28495v1)

固定 token、role 与 mask 后的双向 cache transplant 支持 KV 是所测分歧的充分 carrier，precision 调节其表达。Ch45 已将 replay identity 扩为 token 加 cache-construction state。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28495v1#S3.SS1 — 3.1 Token, role, mask, and replay-boundary contract; https://arxiv.org/html/2607.28495v1#S3.SS2 — 3.2 Models and evaluation set。Evaluation：https://arxiv.org/html/2607.28495v1#S3.SS6 — 3.6 Experiment 4: bidirectional KV-cache transplantation; https://arxiv.org/html/2607.28495v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.28495v1#S6 — 6 Limitations and Threats to Validity; https://arxiv.org/html/2607.28495v1#S7 — 7 Conclusion。
- **取舍与回退：** 把 cache-construction state 纳入 replay identity 提高可复现性，却减少可复用命中并扩大 metadata；身份不完全匹配时回退 fresh prefill。

### [Sample More, Reflect Less](https://arxiv.org/html/2607.28576v1)

等 token 预算下，所测 1.5B–7B 模型的重复采样优于 Self-Refine/Reflexion；这不覆盖带新环境反馈或持久 memory 的反思。Ch80 已把 independent exploration 设为基线并要求新增 observation。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28576v1#S4.SS3 — 4.3 Methods compared; https://arxiv.org/html/2607.28576v1#S5.SS1 — 5.1 Does any method beat the sampling baseline at equal cost?。Evaluation：https://arxiv.org/html/2607.28576v1#A1.SS4 — A.4 A failure that would have biased the results; https://arxiv.org/html/2607.28576v1#S4 — 4 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.28576v1#A1.SS4 — A.4 A failure that would have biased the results; https://arxiv.org/html/2607.28576v1#S4.SS7 — 4.7 Threats to validity。
- **取舍与回退：** 独立采样提高探索覆盖，却增加 selector/verifier 成本且可能重复同类错误；新 observation 或环境反馈可用时仍保留反思分支，否则以等预算 sampling 为基线。

### [OSReward](https://arxiv.org/html/2607.28609v1)

Benchmark 将 CUA reward 判断绑定跨平台 trajectory 与分层 failure，公开 artifact 支持复核但不认证任意真实桌面任务。Ch66 已吸收 trajectory completeness 与 evaluator scope。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28609v1#A3.SS1 — C.1. Evaluated Models; https://arxiv.org/html/2607.28609v1#S6 — 6. OS-Shepherd: An Open Reward Model。Evaluation：https://arxiv.org/html/2607.28609v1#A5 — Appendix E Additional Results and Analysis; https://arxiv.org/html/2607.28609v1#A3 — Appendix C Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.28609v1#A2.SS3 — B.3. Failure-Type Taxonomy; https://arxiv.org/html/2607.28609v1#S8 — 8. Conclusion。
- **取舍与回退：** 跨平台完整 trajectory 评价提高 reward 可解释性，却增加采集、对齐和 evaluator 维护成本；轨迹不完整或平台状态不可比时不发布统一分数。

### [PhiZero](https://arxiv.org/html/2607.28624v1)

离散 physical language 显式表达 world-state transition，区别于把动力学隐含在 pixel predictor；结果仍主要是生成与模拟证据。Ch25 已保留 controllability 与真实环境验证的边界。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28624v1#S3 — 3 Method; https://arxiv.org/html/2607.28624v1#A3.SS1 — C.1 Controllable and Interactive World Model。Evaluation：https://arxiv.org/html/2607.28624v1#A2 — 附录 B Additional Evaluation Details; https://arxiv.org/html/2607.28624v1#A2.SS1 — B.1 Physical Video Generation Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.28624v1#A5 — 附录 E Limitations and Future Work; https://arxiv.org/html/2607.28624v1#S5 — 5 Conclusions。
- **取舍与回退：** 离散 physical language 增强 transition 可解释性，却带来符号化误差和模拟器依赖；真实环境验证不足时保留 pixel/latent predictor 与外部 controller，不授予物理保证。

### [BMOA](https://arxiv.org/html/2607.27270v1)

论文把数值 mismatch 拆成 comparison baseline、证据支持的 compiler mechanism 与 reference-qualified outcome。其 ARM64、Clang 和有限 kernel 矩阵只证明“偏差不自动等于应用精度损失”，不构成任意编译器的正确性证明；长期增量是让 compiler/runtime evaluation 保存 baseline、tolerance、mechanism evidence 与 outcome owner。Ch66 现已把三者连接为同一个 EvalSpec，并要求越出验证矩阵时回退 reference implementation。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27270v1#S3 — 3. Method; https://arxiv.org/html/2607.27270v1#S4 — 4. Experimental Design。Evaluation：https://arxiv.org/html/2607.27270v1#S4 — 4. Experimental Design; https://arxiv.org/html/2607.27270v1#S5 — 5. Results。Limitations / counterevidence：https://arxiv.org/html/2607.27270v1#S6 — 6. Discussion and Limitations; https://arxiv.org/html/2607.27270v1#S8 — 8. Conclusion。
- **取舍与回退：** 分层记录 baseline、compiler mechanism 与 outcome 避免把数值差异直接当失败，却提高 reference/tolerance 维护成本；越出验证矩阵时回退 reference implementation。

### [Back from the Future](https://arxiv.org/html/2607.27600v1)

论文用已缓存状态上的 counter-causal pass 估计哪些旧 token 可由后继上下文预测，再据此 eviction。它减少 KV resident set，却增加周期性反向 mask 计算、refresh policy 和单层近似误差；Ch45 已有“eviction signal 只是 proposal、质量预算与 dense fallback 仍拥有提交权”的完整命题，判已有覆盖。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.27600v1#S3.SS2 — 3.2 Algorithm Summary。Evaluation：https://arxiv.org/html/2607.27600v1#A1 — Appendix A Benchmark Prompts; https://arxiv.org/html/2607.27600v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27600v1#S5 — 5 Conclusion and Discussion。
- **取舍与回退：** counter-causal eviction 减少 KV resident set，却增加反向 mask、refresh 与近似误差；质量预算或 refresh 成本失控时回退原 eviction signal 或 dense KV。

### [ClawTrack](https://arxiv.org/html/2607.28037v1)

论文同时保存 Task Score 与逐 turn Process Score，所测 320 个任务支持 outcome-only evaluator 会把 lucky pass 与可靠过程混在一起；LLM grader、mock service 和 rubric coverage 仍限制外推。Ch66 已将 trajectory narrative、typed action、environment transition 与 completion evidence 分层，Ch69 拥有 trace，因此不重复写入。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28037v1#A4.SS1 — D.1. Process Grader System Prompt; https://arxiv.org/html/2607.28037v1#A4.SS2 — D.2. Outcome Grader System Prompt。Evaluation：https://arxiv.org/html/2607.28037v1#A4 — Appendix D Evaluation Prompts; https://arxiv.org/html/2607.28037v1#A5 — Appendix E Extended Results。Limitations / counterevidence：https://arxiv.org/html/2607.28037v1#A1 — Appendix A Limitations and Broader Impacts; https://arxiv.org/html/2607.28037v1#S5 — 5. Conclusion。
- **取舍与回退：** 过程评分能区分 lucky success，却依赖 grader、rubric 与完整轨迹并增加评审成本；过程证据不足时保留 outcome-only 指标的受限含义并人工复核。

### [Queue-Theoretic Admission Control for Multi-Tenant GPU Clusters](https://arxiv.org/html/2607.28223v1)

论文将多资源 pending queue 分成稳定条件下可给等待界的 quotable workloads 与必须重配置的 unfeasible workloads，并以 vector packing 得到 effective server count。M/G/k、stochastic domination 与到达分布假设不等于生产 SLA；Ch63 现已将“没有可证稳定性时调度器不得给有限等待承诺”写入 admission 主线，并要求假设漂移时撤销 bound、回退实测 percentile。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28223v1#S2.SS1 — 2.1. GPU Cluster Admission Architecture; https://arxiv.org/html/2607.28223v1#S3.SS1 — 3.1. System Definition。Evaluation：https://arxiv.org/html/2607.28223v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.28223v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.28223v1#S7 — 7. Limitations; https://arxiv.org/html/2607.28223v1#S8 — 8. Discussion and Open Problems。
- **取舍与回退：** 可报价等待界提升 admission 可解释性，却依赖到达分布、稳定性和多资源 packing 假设；假设漂移时撤销 bound，回退实测 percentile 与保守拒绝。

### [One Human, N Agents](https://arxiv.org/html/2607.28317v1)

论文表明当 Agent self-confidence 失准且错误相关时，confidence-ranked audit 存在劣于随机抽检的翻转区间。有限模型样本与 Gaussian-copula 假设不证明通用阈值；Ch82 现已把校准、相关性、随机 baseline 与人工 audit budget 放入同一 fleet oversight contract，并在相关性不可辨识时降低自动提交权限。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28317v1#S12 — 12 H2 in the synthetic model; robustness to the copula choice; https://arxiv.org/html/2607.28317v1#S3 — 3 Model。Evaluation：https://arxiv.org/html/2607.28317v1#S1 — 1 Introduction; https://arxiv.org/html/2607.28317v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.28317v1#S14 — 14 Confidence parse failures and imputation; https://arxiv.org/html/2607.28317v1#S15 — 15 Limitation support values。
- **取舍与回退：** 置信度排序可集中人工预算，却会在失准和相关错误下劣于随机抽查；相关性不可辨识时混入随机基线并降低自动提交权限。

### [Why Are GUI Agents Correct but Late?](https://arxiv.org/html/2607.28399v1)

论文把 transient GUI action 的失败定位到 decision-time critical path：空闲期生成带 guard、deadline 与预授权 action 的 bounded policy tree，事件发生后只做轻量 branch match。它以预计算、tree invalidation、误路由与授权范围换取更短在线路径，且只适用于候选 action 可预枚举的事件；Ch44 现已将其写成事件关键路径前移的条件分支，并保留 reactive decode 作为开放 action space 或 guard 失效时的共存路径。

**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28399v1#S16 — 16 Method details moved from the main text; https://arxiv.org/html/2607.28399v1#S11 — 11 Per-model serving provenance。Evaluation：https://arxiv.org/html/2607.28399v1#S18 — 18 Additional results detail; https://arxiv.org/html/2607.28399v1#S4 — 4 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.28399v1#S19 — 19 Full limitations register; https://arxiv.org/html/2607.28399v1#S6 — 6 Discussion。
- **取舍与回退：** 预编译 policy tree 缩短瞬时 GUI 决策，却增加树失效、误路由和预授权风险；action 不可枚举或 guard 失效时回退 reactive decode 或人工接管。

### [Rethinking Inference-Time Scaling in Local Computer-Use Agents](https://arxiv.org/html/2607.28573v1)

论文在所测本地模型与 OSWorld 中区分 context、horizon、structural decomposition 与 parallel sampling，观察到额外 compute 会饱和或迁移 failure，而非稳定提升成功率。该证据不提供跨设备最优预算；Ch84 已要求按状态信息增益、模型能力、成本与 failure type 选择 test-time compute，判已有覆盖。


**Evidence Review 细节。**
- **证据定位：** Method / identity：https://arxiv.org/html/2607.28573v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.28573v1#S3.SS4 — 3.4 Experimental Setup; https://arxiv.org/html/2607.28573v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.28573v1#S5 — 5 Discussion; https://arxiv.org/html/2607.28573v1#S6 — 6 Conclusion。
- **取舍与回退：** 增加 test-time compute 可能改善特定失败，也会饱和并迁移故障、提高本地成本；没有新信息或验证收益时回退较短 horizon 或更小并行度。

### 近似执行的正确性边界

[Beyond KV Reconstruction](https://arxiv.org/html/2607.27269v1) 的 192 个 model-converter-backend-method-task 配置表明：把 MHA/GQA 压缩为 MLA 时，standalone quality 可接受并不保证 draft-target agreement；low-rank 与 RoPE 处理误差会直接降低 acceptance。Ch48 已据此把 draft 优化目标从“重构 KV”收窄为“保留目标模型的条件分布与 verifier 接受行为”，未把四组模型上的结果外推成所有 MLA 转换结论。

[GyRot](https://arxiv.org/html/2607.27694v1) 与 [WIDE](https://arxiv.org/html/2607.28418v1) 共同说明：算法稀疏或低比特只有被真实 layout、group scale、gather/scatter 与 kernel 数据通路消费时才产生系统收益。Ch49 已将 rotation/group quantization 的 granularity mismatch 和 token-wise width routing 纳入 execution-plan contract；作者硬件与模型结果只证明所测 operating point，dense/静态路径仍是兼容与低复杂度回退。

[Stage-Replay Divergence](https://arxiv.org/html/2607.28495v1) 固定 token、role、mask 与 prefix，再交换 retained/fresh KV，发现 continuation 跟随 cache state；precision 只调节差异表达。Ch45 已据此把 replay identity 扩展到 KV construction、precision 与 runtime state。证据限于披露的 Qwen2.5-derived system，不证明所有 fresh prefill 都改变最终任务结果。

[SemPIC](https://arxiv.org/html/2607.28069v1) 与 [SmartGen](https://arxiv.org/html/2607.28150v1) 分别探索 position-independent cache 与 selective KV transfer。它们的共同收益是减少重算或跨节点移动，代价是更强 cache identity、transfer policy 与质量 fallback；Ch50/55 已保留边界 conditioning、reuse hit、transfer volume 和 dense recompute 回退，不把实验吞吐数字作为跨平台保证。

### Agent 的 authority、memory 与 evidence

[FAVA](https://arxiv.org/html/2607.27267v1) 在有限 trace-conditioned 场景中用 permission graph 和 evidence-backed authorization 拦截动态违规；90.5% DCR 不是生产安全证明。Ch72 已把授权从 tool name 提升为 principal、resource、purpose、data flow、runtime state 与 evidence 的提交条件，并保留误拒绝、coverage gap 和外部 policy fallback。

[ChronoMem](https://arxiv.org/html/2607.27773v1) 与 [MemTxn](https://arxiv.org/html/2607.27834v1) 把 agent memory 从 forward-only 文本集合演进为 versioned state：前者处理语义 rollback，后者处理 source-supported update 的原子提交与恢复。Ch77 已将 provenance、revision、commit、rollback 与 candidate memory 隔离成唯一 owner；线性历史和特定 benchmark 不证明开放环境中的并发或跨分支一致性。

[MARS-RA](https://arxiv.org/html/2607.27967v1) 用多模态 comparison 做 embodied multi-agent credit assignment。Ch82 已吸收“聚合分数不能隐去 evaluator identity、相关错误与局部贡献”的边界；模型 judge 仍不是环境真值，相关性过高时回退独立 verifier 或人工。

[Safeguards Based on Copyable Context](https://arxiv.org/html/2607.27951v1) 支持一个更基础的边界：模型能读取的 prompt、policy text 或 memory 也能被复制、覆盖或重新解释，因而不能同时充当不可绕过 authority。该命题已经由 Ch72 的外部 authorization、effect-time policy 与 trust-domain 隔离完整承载，无需重复追加。

### Evaluation 必须验证完整系统，而非漂亮总分

[KernelGenBench](https://arxiv.org/html/2607.27231v1) 的跨算子和跨芯片结果显示，单平台成功率会隐藏移植崩塌与 token 成本；作者的 15B-token 规模也不能证明真实生产 ROI。Ch66 已把 operator source、hardware、compiler/runtime、correctness oracle、speedup、generation budget 与失败类型绑定为同一 EvalSpec。

[LayerRAG-Bench](https://arxiv.org/html/2607.27353v1) 把 evidence、tool、authorization 与 session-state 故障分别注入；合成 policy corpus 不能代表企业生产分布，却足以说明一个最终答案分数不能定位控制平面故障。Ch66 已吸收 layer-specific credit，不把某一层修复记作端到端可靠性。

[How Benchmarks Mis-Score Computer-Use Agents](https://arxiv.org/html/2607.28367v1) 与 [OSReward](https://arxiv.org/html/2607.28609v1) 分别审计 task/trajectory/oracle/reporting pipeline 与跨平台 trajectory reward。Ch66 已要求保存观察缺口、有效替代路径、failure taxonomy 与 evaluator revision；它们只支持所测 benchmark 与 reward model，不认证任意 CUA。

[Do Context Files Help Coding Agents?](https://arxiv.org/html/2607.27250v1) 在 17 个任务、两个 agent、288 次运行中没有测得 context-injection 的稳定 correctness 增益，并指出 informative difficulty band 随 agent 变化。这个结果不是“上下文文件无用”的等价性证明；Ch75 已把 context 价值写成信息收益、冲突、token cost 与任务/agent 条件下的可测假设，因此判已有覆盖。

[Sample More, Reflect Less](https://arxiv.org/html/2607.28576v1) 在披露模型与任务上发现等预算重复采样优于 self-refine/Reflexion。Ch80 已要求把反思与独立探索在相同 token、attempt、selector 和 verifier 下比较；当反馈不含新 observation 时，采样仍是合理基线。结果不覆盖更大模型、持久 memory 或真实环境反馈。

### 表示、训练与物理闭环

[Multi-Head Attention Residuals](https://arxiv.org/html/2607.27230v1) 允许子层对历史深度状态做 learned routing，扩大信息路径却增加 activation/state 与跨 stage 通信。Ch17 已在“Residual Stream 从单一累加状态走向 Depth-wise Routing”中完整承载这一 alternative branch，标准 residual 在实现成熟、带宽敏感或浅层场景仍成立。

[Explorative Modeling](https://arxiv.org/html/2607.27372v1) 把多模态匹配的多解选择放入训练循环；Ch24 已将其作为 AR、diffusion 之外的 factorization 分支，保留多候选训练成本、mode selection bias 与有限任务证据。

[Correcting What You Cannot See](https://arxiv.org/html/2607.28336v1) 用 teacher-student disagreement 与 downstream failure 区分 perception correction；matched 2B ablation 支持方法内组件贡献，不证明跨模型通用。Ch29 已将 perception/reasoning credit separation 与 verifier bias 纳入多模态蒸馏边界。

[QQWorld](https://arxiv.org/html/2607.28415v1) 观察 EP objective 对 tail sample 的修正梯度快速衰减，以投影 quantile matching 保留 tail pressure；cross-batch 估计换来额外状态与分布假设。Ch25 已把 latent regularization 写入 imagined rollout 的可信度边界，而不是把更高任务分数解释为真实世界因果正确。

[PhiZero](https://arxiv.org/html/2607.28624v1)、[RedFlow](https://arxiv.org/html/2607.27782v1) 与 [Flow-Matching Uncertainty](https://arxiv.org/html/2607.27933v1) 分别处理显式 transition language、动作级修正和失败 sensor。Ch25/26 已形成“预测 observation → action-conditioned transition → controller → environment feedback → correction”的连续路线；视频质量、flow geometry 或模拟成功都不能替代真实环境安全证据。

[Subtract, Transport, or Replay?](https://arxiv.org/html/2607.27539v1) 与 [Asymmetric Collapse](https://arxiv.org/html/2607.27240v1) 提供两类受限反证：删除不能以拒答替代，模型合并也不能假设不同行为向量会对称保留。Ch72/77 已分别拥有参数擦除与行为抑制的分离、以及安全能力的独立 regression slice，单一小模型或任务对不能升级为普遍规律。
## 5. 缺口与下一步

无

独立复核已修正 7 个 false negative，当前算术为 `599 raw = 33 candidates + 566 非候选`；84 项旧 exact-v1 审阅可进一步写成 `33 当前候选 + 51 当前 pre-denominator closure`。33 项的 Evidence、Stable Node 与 Books disposition 均已闭合；当前没有 exact-v1 访问阻塞或待执行 Books 工作，材料请求为无。

## 6. 复核

复核者：非作者独立智能体 `/root/aug21_31`
结论：通过

非作者 post-write 复核确认窗口、599 raw 身份、84 份既有 exact-v1 证据、33 项准入、V2 算术、Stable Node 与链接结构，并逐项核对 24 个整合 disposition 的真实机制正文。BMOA、GPU admission、fleet oversight 与 GUI decision critical path 的新增正文，以及其余既有整合正文均已通过；KernelGenBench 已合并进 Ch66 的 canonical Kernel Benchmark 合同，Flow-Matching Uncertainty 已合并进 Ch26 的 canonical Trajectory Geometry sensor，均保留未证明内容、代价、失败和回退边界。五项错误 Books trace 日期已修正；当前不存在只靠 marker、Review note、重复段落或错误日期宣称吸收的情况。

本轮全月 Gate audit 进一步为 33 项候选逐项恢复 exact-v1 的 Method、Evaluation 与 Limitations 定位，并补写与各自机制对应的代价和可执行回退；未扩展候选，也未以通用模板替代单篇证据判断。
