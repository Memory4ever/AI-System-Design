# 2604.25727v1 SkillSynth：既有审阅后的 Ch27/Ch29 唯一 owner 复核

状态：这是同日 [较早单篇审阅](./V3_REOPEN_NOTES.md)的**owner 复核**，不是新增题摘或第二篇。原评分 `2+2+2=6`；由于 Appendix D 图规模印刷反证，原提案为有限 Deep／窄 Disputed，仅隔离该规模宣称。Books 的 Ch27 vs Ch29 唯一 owner 尚待非作者裁定，不申请共享锁、不代表日级 Gate。

## 身份、贡献与原始机制

- [官方 exact-v1](https://arxiv.org/html/2604.25727v1)《Toward Scalable Terminal Task Synthesis via Skill Graphs》，§2–4、Appendix A 的必要段已读。arXiv ID 位于本日官方公告批次联合链内；仍须单篇核是否有更早同家族正式公开，不能以 v1 submitted 字段单独证明首发。
- 数任务数量不能保证 Agent 训练实际到达多样状态。作者以 scenario 为节点、skill 为带前后条件的边，先用 LLM 推断/对齐前后状态，再用状态及技能逆频率采样无重复有向路径，将路径交给任务构造器实例化为 instruction、初始文件系统、容器、tests、oracle；随后分别运行 oracle 和 rubric 检查。这是“覆盖目标→可执行路径提案→任务身份→验收”的机制链，不是仅把 Skill 名单放进 prompt。Eq. (4) 表达固定目标下的经验 `(scenario, skill)` 支持，Algorithm 1 抑制高频节点/边；但 scenario 充分统计和 skill 映射是建模假设，采样覆盖不自动等价于 token-level 学习效用。
- §4 同一构造 harness 与 3,721 个 seed 的 Single-skill、随机 Multi-skill 和图路径比较，Table 4 的 Qwen3-32B 下游 Terminal-Bench 1.0/2.0 是 `25.4/21.3`、`30.8/25.8`、`33.8/29.6`。§4.5 在各策略 1,000 条轨迹经同一 LLM 抽取和 embedding 聚类后，报告状态—技能 pair unique coverage 相对前两者高 31%/19%。这支持在该任务/抽取器/模型配方下 path coherence 比随机技能拼接有效；相同 seed 数不是 matched 训练 token、采样成本或真实难度分布，不能从表单独证明覆盖率是唯一因果变量，也不能把 Hy3 采用叙述计作独立受控收益。

## 反证与分母

- Table 1 的 `3,560/3,721=95.7%` 是 oracle 通过，**双检查均过只有 `3,423/3,721=92.0%`**；另 137 项 oracle 过而 rubric 不过。§4.2 作者把 rubric 不过的任务留作 SFT diversity、从 RL 排除，说明“可执行”不等于 instruction/test 一致或安全 reward。三次 rollout 的 `0/3` 只能说该 Hy3 设置未解，不可自动当能力所需难例；§4.6 失败 taxonomy 先由三位作者各看 20 例，再由 LLM skill 标全量，不是独立人工标注率。
- Appendix D 同一图表给 `82,073` scenario nodes、largest component `118,806 (85.6%)`，component 节点数不可能超过全图节点数。只隔离此图规模／覆盖印刷数字，不能据此说路径采样或 Table 4 必假；需 graph export、统计阶段与节点身份重算来解除争议。较早审阅已记录该反证，这里不重复计一篇。
- Appendix A 的 skill-level loss 等价依赖 deterministic trajectory→skill mapping、scenario 对下一决策充分、skill 自回归及 action 分段连续；论文不验证这些条件在真实终端环境普遍成立。其“覆盖更多可学习 region”不是泛化定理。图连边与 rubric 都由模型判断，可能共享 ontology blind spot；路径长度最多 7，作者将并行 subgraph 留为未来工作。需要保存原 skill/license、scenario/edge generator、图版本、路径、初始 state、verifier 与抽取器身份，才能复核覆盖增量不是生成器分类偏差。

## 实际 owner / 最小 Books 提案

[ROADMAP](../../../../../ROADMAP.md) 的 `TRAIN-DATA` owner 是 [Ch27](../../../../../books/part-04-training-system/27-data.md)。已顺读 Ch27 的 terminal/repository 行 470–485、Coverage Contract 行 548–571：它明确任务、初始环境、轨迹与 verifier 联合身份，也已区分 semantic/feature/dependency coverage 与可执行验收；因此不能把整套 SkillSynth 作为新框架搬进去。但现文尚未把“生成计划覆盖”与“执行轨迹实际覆盖”分账到**状态条件下的技能选择**：同样数量的任务、skills 和 executable checks 仍可能反复到达同一 `(scenario, skill)`，也未说明前后条件相容的路径提案应独立于实际轨迹再验。[Ch29](../../../../../books/part-04-training-system/29-sft.md) 行 526–533 已写 environment-grounded demonstration、teacher 轨迹与独立 outcome Gate，适合消费验收后的 row；任务路径与覆盖策略由 Ch27 数据生产 owner 持有更不重复。较早审阅曾拟 Ch29，须经非作者裁定唯一 owner 后才实写。

若非作者确认该窄缺口与 Ch27 唯一 owner，建议在 Ch27 `### 从样本数量到 Coverage Contract` 的三 coverage 解释段后接两段，不另设章节：

> 对交互式 terminal 数据，任务数量、skill 数量和实际训练轨迹覆盖也不能混为一个指标。任务生成器可把可观察的中间 scenario 与可执行 skill 的前后条件组成版本化图，按低频 `(scenario, skill)` 路径提出新任务；但路径是生成意图，只有在固定环境、scaffold 与抽取器下重放真实轨迹，才能判断 policy 是否确实经历这些状态—技能组合。独立 verifier 仍分别检查执行可达与 instruction/test 一致，不能让生成同一任务的模型自签答案或奖励。
>
这种路径采样能抑制高频技能重复，却以图构建、语义对齐和错误边传播为代价；缺少稳定状态抽象、可执行后置条件或可靠 reset 时，回退静态任务、人工依赖图或既有随机组合，并以 held-out 目标任务验收。现有受限证据只在所测 terminal harness、Qwen3 SFT 和 Terminal-Bench 中表明图路径方案优于同 seed 数的单技能/随机技能组合；`95.7%` 是 oracle 通过而非双验收率，更不证明同训练成本下普遍收益。

不动 Ch84 Skill 注册/发布 owner 或 Ch66 评价 owner；若非作者判断 Ch27 已有命题足以承载该分账，则最终可为具体 Existing，不因方案名自动整合。
