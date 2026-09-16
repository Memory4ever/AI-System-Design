# Daily Research — 2026-07-09

**规范：** V3
**窗口：** 2026-07-08T09:00:00+08:00 ～ 2026-07-09T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T15:30:00+08:00

## 1. 结论

本窗以 arXiv 官方 2026-07-09 新公告批次为 owner 边界，旧报告恢复的 1148 个跨类别去重身份仅作为标题与摘要筛选种子，不继承其 14 项分母。逐项语义复筛后保留 10 个材料家族：它们分别改变了 MoE/KV 联合路由、Agent 过程评测、World Model 状态准入、RL clipping、异构执行计划、KV 归档、长上下文可变状态和 trace 归因等长期系统判断。4 个旧候选因属于 VLA 局部变体、综述或产品级生成方案而在分母前关闭；未见入选 v1 的 withdrawn 标记。

10 项均已回到 exact v1 的机制、实验与限制位置完成相称审阅。旧日报标为“整合”的长期增量已在现有 Books 正文中找到具体承载点，因此本次均判为已有覆盖，不新增书稿写入；本轮纠正了 5 项证据定位和 1 个错误题名，待非作者重新复核后闭合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-ANTHROPIC | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-GOOGLE-AI | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-META-AI | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-QWEN | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-DEEPSEEK | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-MOONSHOT | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-ZAI | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-MINIMAX | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-ARXIV | 官方新公告批次与 availability schedule；1148 个跨类别去重身份完成全标题巡检，含糊或高信号项阅读完整摘要，10 项进入分母 | 已检查 | 无 |

原始身份中的垂直应用、单数据集/局部 benchmark 增量和不改变状态、数据流或控制权的工作均在分母前关闭。代表性关闭项为 Pelican-VLA 0.5、VLA 综述、Infinite Worlds 与 LaMem-VLA；关闭不依赖它们的精确发布日期，亦不支撑技术主张。

## 3. 候选与判断

公开时间是官方新公告进入本窗的时段，不是作者提交时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [TriRoute](https://arxiv.org/html/2607.06601v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 把 Attention、Expert 与 KV allocation 作为共享预算下的联合路由问题，并暴露 collapse cascade；3 + 3 + 2 = 8 | 深入完成 | 仅报告：MODEL-MOE；缺少可复现 runtime artifact，尚不足以改写通用部署结论 |
| [AgentLens](https://arxiv.org/html/2607.06624v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 将代码 Agent 评测从终局分数扩展为带证据指针的 trajectory review；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Rank-One Corner: How Much Value Equivalence Does a Task Need from a World Model?](https://arxiv.org/html/2607.06640v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 受控实验显示训练目标的维度限制 latent 可安装的 query-closure 方向，而扩大容量不能替代目标覆盖；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Grounding Spatial Relations in Action-Conditioned World Models](https://arxiv.org/html/2607.06925v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 揭示 goal instruction 泄漏会让 dynamics 模型绕过真实 transition learning；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [UP](https://arxiv.org/html/2607.06987v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 将正负 Advantage 的 probability-ratio clipping 拆为不同控制合同；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Voltron](https://arxiv.org/html/2607.07046v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 将异构推理计划从静态映射改为在 token 边界可安全修订的 phase-aware execution plan；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Fractal KV-Cache Archives](https://arxiv.org/html/2607.07144v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 分离 HBM residency 与量化后 symbol stream 的可寻址无损归档；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Sparse Delta Memory](https://arxiv.org/html/2607.07386v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 分离参数拥有的初始状态与请求拥有的在线 delta state；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Single-Rollout Asynchronous Optimization](https://arxiv.org/html/2607.07508v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 用单 rollout critic 与异步样本流重构 RL post-training 的数据和更新节奏；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-PPO，[Ch32](../../../../books/part-04-training-system/32-ppo.md) |
| [STRACE](https://arxiv.org/html/2607.07702v1) | 2026-07-09T08:00:00+08:00 ～ 2026-07-09T09:00:00+08:00 | 用结构先验把 noisy execution trace 转为候选 root-cause attribution；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-TRACE，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |

## 4. 证据与知识整合

### [TriRoute](https://arxiv.org/html/2607.06601v1)

- **拟采用命题：** attention mode、expert set 与 KV bit width 若分别优化，会争抢同一 token/layer 的计算与内存预算；共享控制器可以把三类 provisional choice 放进同一 Lagrangian budget，但可执行 route 仍必须由 runtime kernel 提交。
- **证据定位：** Method 为 §3.1～§3.8（三条路由轴、共享 controller、heterogeneous straight-through relaxation、whitening/balancing/entropy 与成本乘子）；Evaluation 为 §4～§6（最大约 1.3B 的训练、Pareto frontier 与消融）；Limitations 为 §7（ragged kernel、mixed-KV runtime、同步与 tail/fairness 未解决）。
- **证明与未证明：** exact v1 支持“联合预算可减轻跨轴 collapse cascade”这一作者实验结论；不证明该控制状态能在生产引擎中高效执行，也没有公开训练日志、checkpoint 或 event-time runtime artifact。
- **取舍与回退：** 联合控制减少局部最优，却增加跨轴校准、同步、metadata 与不规则 kernel 成本；任何轴的预算或执行布局无法验证时，应回退到分轴路由、固定 KV 精度和已验证的 dense/静态路径。因此仅保留为 `MODEL-MOE` 的实验性分支，不进入 Books 正文。

### [AgentLens](https://arxiv.org/html/2607.06624v1)

- **拟采用命题：** coding-agent 评测必须把最终 repository state、可执行 verifier 与完整 trajectory evidence 分开记录，不能把 outcome、instruction compliance、workflow pitfall、tool use 和 user-facing quality 压成一个无法解释的总分。
- **证据定位：** Method 为 PDF p.3（task/persona run、formal verifier、五类 trajectory review 与 evidence pointer）；Evaluation 为 pp.7、10（32 条 Java trajectory、judge validation、leaderboard/pairwise analysis）；Limitations 为 p.12（Java-only task class、第三方 API/version/latency 与 compact fold）。
- **证明与未证明：** 论文证明同一终局正确性可能掩盖过程失败，且具名证据指针能支持复核；不证明 reviewer 在其他语言、Agent 类型或开放环境中仍可靠，也不证明 judge narrative 等同因果归因。
- **取舍与回退：** 多维轨迹审阅提高可解释性，但增加记录、judge 成本和 evaluator version drift；当过程证据不完整时保留 executable outcome gate，并将过程维度标为不可判定。Ch66 已用 outcome、process evidence、judge identity 与复核边界承载该结论。

### [The Rank-One Corner: How Much Value Equivalence Does a Task Need from a World Model?](https://arxiv.org/html/2607.06640v1)

- **拟采用命题：** world model 要保存的不是 observation 的全部细节，而是下游 query 闭包所需的 predictive coordinates；在论文的受控 DreamerV3 环境中，训练目标的维度限制 latent 安装的 closure rank，单一 scalar value/reward 目标只是 value equivalence 的 rank-one 情形。
- **证据定位：** Method 为 §3（latent-only auxiliary/value head、held-out linear probe 与 leakage check）；Evaluation 为 §4～§5（label-shuffle 因果对照、scalar/full-objective matched comparison 与 1～4 维 objective sweep）、§7（capacity 与 planted-rank calibration）及 §8（Bellman-residual evaluation slice）；理论解释在 §6，适用边界与 limitations 在 §9。
- **证明与未证明：** exact v1 在已知 ground-truth closure 的合成环境中支持“objective dimensionality 决定可安装 rank”的受控结论，并展示 reconstruction 已能恢复 closure 时该规律不再是约束；它不证明自然图像、开放世界或任意非线性 world model 都遵循相同定量规律，也不证明 scalar value 目标在所有控制任务中不足。
- **项目综合（推断）：** 对本项目可采用的长期判断是：扩大 latent capacity 不能补回训练目标没有要求保存的 task-relevant directions，world-model evaluation 也不能只看 reconstruction 或单一 value 指标。该工程结论是从论文证据推导出的设计含义，不是作者直接证明的生产系统合同。
- **取舍与回退：** 扩展目标维度可以提高 query closure 的覆盖，却增加监督构造、目标冲突、probe/calibration 与训练成本；closure 可由 observation reconstruction 直接恢复或任务只依赖单一 scalar 时，旧的重建/单值目标仍成立。Ch25 已以“从重建 Observation 到预测可推进的 Representation”承载该边界。

### [Grounding Spatial Relations in Action-Conditioned World Models](https://arxiv.org/html/2607.06925v1)

- **拟采用命题：** goal 应属于 planner cost，而不应作为 dynamics 的答案通道；若 transition model 同时看到直接命名目标关系的指令，它可能复制 goal semantics 而非学习 action-conditioned state transition。
- **证据定位：** Method 为 §3～§4（compact action-conditioned formulation、goal-conditioned baseline、instruction-leakage intervention）；Evaluation 为 §5.1、§5.4 与 §6（受控空间关系任务、goal-free 对照与 grounding interpretation）；Limitations 为 §7（合成环境、窄关系词表、无物理部署）。
- **证明与未证明：** exact v1 支持该受控设置下的泄漏路径与 goal-free dynamics 改善；不证明真实物理世界的长期因果建模、规划可靠性或安全执行。
- **取舍与回退：** 去除 goal 可减少 shortcut，却可能使有限容量 dynamics 难以聚焦任务相关状态；planner 可保留 goal 并通过显式 cost 选择 rollout，dynamics 则回退到只接收 state/action 的可审计输入。Ch25 已完整承载该边界。

### [UP](https://arxiv.org/html/2607.06987v1)

- **拟采用命题：** 正、负 advantage 不必共享同一 clipping contract：positive branch 可用 stop-gradient self-anchor 保留当前策略 REINFORCE 梯度而不触发陈旧 rollout ratio 的上界，negative branch 仍保留稳定性限制。
- **证据定位：** exact-v1 PDF p.6 的 §4.1、Eq.12～13 给出 stop-gradient self-anchor 及其 REINFORCE-gradient 等价推导，pp.6～7 的 Eq.15～16 给出正负 advantage 的不对称 token/sequence-level 目标；pp.8～12 的 §5 披露 Qwen3 dense、MoE、VLM 上的数学/视觉推理实验和消融，p.12 的 §6 总结结论。v1 没有独立 Limitations 小节。
- **证明与未证明：** exact v1 支持目标的代数形式以及作者披露模型、任务和训练配置下的 accuracy、entropy 与 KL 结果；没有给出一般收敛定理，也未证明无界正向分支在 noisy reward、开放任务或不同 rollout infrastructure 下仍稳定。缺少独立 limitations 不能被日报补写成作者结论。
- **取舍与回退：** 放开正向上界提高探索，却可能放大 noisy positive advantage、KL 漂移和 reward hacking；监控 divergence、KL 与 verifier slice，越界时回退对称 clipping 或更保守的 reference regularization。Ch33 已承载该受限分支。

### [Voltron](https://arxiv.org/html/2607.07046v1)

- **拟采用命题：** edge inference 的 execution plan 不能把 Prefill 与 Decode 当同一 workload；逐层 MP/TP、精度与设备参与度应按 phase 规划，并只能在 token boundary 基于 memory、KV growth 与链路观测提交修订。
- **证据定位：** Method 为 §3（per-layer MP/TP planning 与 task-aware precision）和 §4（Prefill/Decode 分离与 elastic controller）；Evaluation 为 §5～§6（六设备、三集群、模型/任务 suite、trace replay、QoS 与适配消融）；Limitations 为 §7（edge cluster、网络和 workload-specific planner 边界）。
- **证明与未证明：** 作者实验支持 phase-aware plan 在其设备/链路组合内改善 QoS；不证明任意终端、任意网络或不同模型布局的同样收益，亦无可验证的 event-time artifact。
- **取舍与回退：** 在线修订提升适配性，却引入 profile drift、state transfer、预加载和切换原子性；观测不稳定或迁移无法在边界内完成时回退最近的已验证静态计划。Ch49 已覆盖该机制。

### [Fractal KV-Cache Archives](https://arxiv.org/html/2607.07144v1)

- **拟采用命题：** KV 的完整可寻址历史可以与 HBM residency 分离：先把 KV 映射成有损量化 code，再把 code stream 组织成带 anchor 的可随机访问 archive；“lossless archive”只相对 codes 成立。
- **证据定位：** §2 同时给出 contractive iterated-map archive 及其 lossless/linear-time/random-access/append microbenchmark；§3 给出 GPT-2 124M、1024-token、单语料 quantizer setup 与 rate–distortion 实验；§4 给出 stored-vector 上的 suffix retrieval；§5 是 Related Work，§6 才是 Limitations，§7 是 Conclusion。公开仓库无窗口截止前 commit，artifact equivalence 未验证。
- **证明与未证明：** exact v1 证明量化 codes 可被可寻址归档并在作者设置中恢复；不证明恢复原 FP16 KV、长上下文语义等价或 GPU serving 性能。
- **取舍与回退：** archive 降低冷历史存储，却支付量化误差、anchor 空间和随机解码延迟；质量预算或访问延迟越界时回退高精度冷层、热 KV 常驻或从原 token 重算。Ch45 已承载。

### [Sparse Delta Memory](https://arxiv.org/html/2607.07386v1)

- **拟采用命题：** 长期参数基底与请求期间的 mutable memory 应分权：初始 base 保持稳定，product-key sparse read/write 只把请求增量写入显式 N-slot delta table。
- **证据定位：** Method 为 §3（N-slot table、product-key sparse read/write）与 §4（gated delta update）；Evaluation 为 §5～§6 及 Appendix A–E（iso-FLOP scaling、语言/长上下文任务、kernel/memory profile）；Limitations 为 §7 与 Appendix F（HBM residency、巨大物理状态、kernel overhead 与 serving evidence 缺口）。
- **证明与未证明：** 作者结果支持受测 iso-FLOP 设置下扩大可寻址 state；不证明任意长上下文、并发隔离、跨请求持久化或生产 kernel 稳定性，公开仓库也无 event-time 等价 commit。
- **取舍与回退：** 稀疏 delta 扩大容量，却增加 slot collision、路由误差、HBM footprint 与写入一致性；容量/身份无法保证时回退固定 recurrent state、普通 KV 或只读参数基底。Ch22 已明确这三类状态的 owner。

### [Single-Rollout Asynchronous Optimization](https://arxiv.org/html/2607.07508v1)

- **拟采用命题：** 当 group sampling 是训练吞吐瓶颈时，可用 single-rollout critic 与 trust mask 替代组内基线，并把 actor/learner 解耦；但 stale rollout 的 importance correction 与 critic reliability 必须成为显式训练状态。
- **证据定位：** Method 为 §3.1（以 rollout log-probability 为 behavior proxy 的 double-sided token mask）与 §3.2（single rollout、critic 多步更新、frozen-attention value training 和 skip-observation GAE）；Evaluation 为 §4.1～§4.5（Qwen3-30B-A3B 的 math、SWE-Bench Verified、消融、training dynamics 与 simulated online shift）；§5 是 Related Work，§6 是 Conclusion，真正的限制在 Appendix B，Appendix A.2 只是其他 single-rollout baseline 对比。
- **证明与未证明：** exact v1 支持作者任务中 single-rollout SAO 相对所列 baseline 的结果与训练动态；不证明 critic 在开放任务上无偏，也不证明吞吐、任意真实 online shift 或不同模型规模上的同等收益。Appendix B 还明确要求保存 token-level behavior probabilities，并把结论限制在 agentic reasoning/coding、模拟写作偏好和 Qwen3-30B-A3B。
- **取舍与回退：** 单 rollout 降低采样成本，却引入 critic state、异步陈旧性和 trust-mask 误拒；critic 校准或 ratio 超界时回退同步 group baseline、丢弃 stale batch 或降低 actor/learner 间隔。Ch32 已承载该条件分支。

### [STRACE](https://arxiv.org/html/2607.07702v1)

- **拟采用命题：** noisy agent trace 应先规范化为 dependency graph，再用 backward slice 缩小 root-cause candidate；localization 只是待证伪候选，不能直接取得 causal 或 fix ownership。
- **证据定位：** Framework 为 §3：先由实现/接口/日志构建 textual Execution Dependency Graph，再做 failure-pattern mining、representative trace selection、backward slicing 与 prompt heuristic 更新；Evaluation 为 §4（HotpotQA、WebArena、VeruSAGE-Bench，规模/成本、case study 与 ablation）；§5 是 Conclusions，其后的独立 `Limitations` 小节明确要求能看到 codebase/harness artifacts，未覆盖纯黑盒或 trace-only agent。实现可追溯到窗口前 commit `14595633a54079edb5e95287041e2cfd5bd1f1c9`。
- **证明与未证明：** 作者实验支持这套四阶段 pipeline 在三个披露 benchmark 上改善 success rate，并在消融中显示 structural modeling/trace filtering 的贡献；论文把 backward slicing 的输出称为 causal localization，但并未通过 intervention 证明候选节点是失败的充分或必要原因，也不证明对隐藏控制流或纯黑盒 Agent 的泛化。
- **取舍与回退：** dependency graph 减少人工搜索，却会继承 parser 漏边、judge bias 与 trace 缺失；无法建立可靠依赖时回退时间顺序排查，并用 replay/intervention 升级因果证据。Ch69 已覆盖，无需追加。

## 5. 缺口与下一步

无

无材料请求。Books manifest 为“新增写入 0，已有正文覆盖 9，仅报告 1”。

## 6. 复核

复核者：root（非作者独立语义复核）

结论：通过

非作者逐项复核确认：`2607.06640` 已恢复官方题名，论文证据与项目推断分开，Evaluation/Limitations 定位及 Ch25 的 query-closure 正文已纠正；`2607.06987` 使用可审计 PDF 页码，`2607.07144`、`2607.07508`、`2607.07702` 的 Method/Evaluation/Limitations 均与 exact-v1 结构一致。候选分母与 Books 数量未扩大，机械校验与语义 Gate 均闭合。
