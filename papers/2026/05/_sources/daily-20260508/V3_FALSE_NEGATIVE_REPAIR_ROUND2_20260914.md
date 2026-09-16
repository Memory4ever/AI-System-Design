# 2026-05-08 V3 post-write false-negative 作者侧修复

## 结论

非作者 post-write audit 指出的 4 项均为 true false negative；作者侧已完成 exact-v1、owner、withdrawal、Score V2、Evidence Review、唯一 Stable Node 与 proposition-level Books Decision。随后只在同一批 `513` 个 canonical closure 中，围绕同一类 generic rejection rationale 做有界语义反查，又确认 5 项 false negative。没有扩大来源，也没有把旧 `screening-ledger-final.json` 中不属于本窗 canonical 619 family 的条目移入本日报。

修复后机械账本为：

```text
619 raw unique Source Families
= 106 retained and evidence-reviewed
+ 513 pre-denominator closures
```

9 项均可访问、未见 arXiv withdrawal 标记，并按 May official announcement cadence 归属 `2026-05-08T08:00:00+08:00`。其中 5 项需要 root 写回 Books，4 项由现有正文的具体命题完整承载。作者修复不能自签独立 Gate；报告继续为 `Ongoing`。

## Owner、版本与撤稿检查

| Source Family | exact-v1 header | owner window | Withdrawal | 处理 |
| --- | --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-05250` | v1, 2026-05-05 | 2026-05-08 08:00 official batch | 未见 | 重开；另有 05-06 stale duplicate，交 root 对账 |
| `SF-2026-ARXIV-2605-05501` | v1, 2026-05-06 | 同上 | 未见 | 重开 |
| `SF-2026-ARXIV-2605-05678` | v1, 2026-05-07 | 同上 | 未见 | 同类 closure 反查重开 |
| `SF-2026-ARXIV-2605-05715` | v1, 2026-05-07 | 同上 | 未见 | 重开 |
| `SF-2026-ARXIV-2605-05750` | v1, 2026-05-07 | 同上 | 未见 | 同类 closure 反查重开 |
| `SF-2026-ARXIV-2605-06036` | v1, 2026-05-07 | 同上 | 未见 | 重开 |
| `SF-2026-ARXIV-2605-06078` | v1, 2026-05-07 | 同上 | 未见 | 同类 closure 反查重开 |
| `SF-2026-ARXIV-2605-06200` | v1, 2026-05-07 | 同上 | 未见 | 同类 closure 反查重开 |
| `SF-2026-ARXIV-2605-06308` | v1, 2026-05-07 | 同上 | 未见 | 同类 closure 反查重开 |

`2605.05250` 在 05-06 旧 screening ledger 中也被写成 closure；本项目当前 owner 使用 scheduled announcement batch 而不是 submitted timestamp，因此不能在两天重复拥有同一 family。本 lane 不修改 05-06，精确 reconciliation 已写入 root queue。

## 逐项 Evidence Review

### `SF-2026-ARXIV-2605-05250` — Decision-aware User Simulation Agent

- **Problem / changed constraint:** 流畅且始终合作的 LLM simulator 会忽略 choice overload、犹豫和退出，系统性高估 conversational agent 的 acceptance。
- **Mechanism / ownership:** Hesitator 将候选选择与是否承诺分开。选择阶段先做 non-compensatory filtering，再做 weighted utility；commit 阶段以 assortment size、complexity、task difficulty、preference uncertainty 组成 overload state，并映射为 acceptance probability；response model 只负责语言化 action。
- **Evaluation:** Amazon Reviews 2023 的 Electronics 与 Video Games；每配置 40 sessions、最多 20 turns；backbone 为 `gpt-oss-20b`，比较 3 个 simulator baseline。
- **Proof / non-proof:** 只证明上述两类商品、静态 persona 和 consumer-psychology meta-analysis 校准下的行为差异；不证明其他 Agent workload、动态偏好或生产用户同分布。
- **Trade-off / fallback:** 增加可解释的 behavioral state，却引入领域校准和心理学参数迁移风险；缺少目标用户数据时保留简单 simulator，并把 cross-simulator ranking reversal 作为 measurement uncertainty。
- **Score / owner:** `2+2+2=6`；因修复 false negative 执行 Deep Review；`PLATFORM-EVALUATION-SYSTEM`，对读 `AGENT-PLATFORM`。
- **Books Decision:** `No Change — Existing Coverage`。Ch66 已明确要求 simulator 拆分 behavioral realism 与 tester reliability，并校准 decision fidelity、disengagement / walking-away；本篇补强证据，不新增命题。
- **Primary:** https://arxiv.org/html/2605.05250v1

### `SF-2026-ARXIV-2605-05501` — SOCpilot

- **Problem / changed constraint:** action 名称合法不代表 action sequence 满足 mandatory ordering、approval 和 policy；把政策塞进 prompt 不能赋予模型 compliance authority。
- **Mechanism / ownership:** 模型只生成 typed plan proposal；catalog filter 先去掉未知 action，deterministic verifier 再对 incident package、action catalog 与 policy rules 执行 pre-execution 检查。Verifier 只证明 syntax/policy compliance，不判断 action 是否语义上适合事件。
- **Evaluation:** 200 个匿名 production SOC incidents、两家模型 provider、配对 analyst baseline；public corpus action mapping `1147/1147`。论文分别测 insert/order/defer/approval，不能把 466 个被移除的 approval-gated actions 外推为所有 policy check 的统一效果。
- **Proof / non-proof:** 证据属于 plan compliance，不覆盖真实工具执行、serving security、环境效果或攻击后的 runtime containment。
- **Trade-off / fallback:** 外置 verifier 增加 deterministic coverage 与审计性，也依赖 catalog/rule completeness；无法表达语义风险时必须升级人工/领域审批。
- **Score / owner:** `3+2+3=8`；Deep Review；`PLATFORM-SECURITY`，对读 `AGENT-WORKFLOW`。
- **Books Decision:** `No Change — Existing Coverage`。Ch72 已把模型输出定义为 untrusted proposal，并由 deterministic tool policy 拥有 allow/deny/approval authority。
- **Primary:** https://arxiv.org/html/2605.05501v1

### `SF-2026-ARXIV-2605-05678` — Chain of Risk

- **Problem / changed constraint:** final answer 安全不能代表 reasoning trajectory 安全；unsafe reasoning→safe-looking answer 与 safe-looking reasoning→unsafe answer 都会逃逸单点检查。
- **Mechanism / ownership:** 以同一 20-principle rubric 分别测 reasoning 与 answer，形成 unsafe/leak/escape taxonomy；白盒分支按 principle 构造 safe/unsafe centroid direction 并作 conditional steering。Evaluation owner 拥有 stage-wise measurement；steering 只是受限 actuator。
- **Evaluation:** 15 个 open/API reasoning models，每模型约 41K prompts，另有 HeldOut2K/OOD2K；三种可 steering open models 上报告 unsafe-count reduction，并用 BBH/GSM8K/MMLU 检查 capability retention。
- **Proof / non-proof:** visible reasoning 可能不忠实于内部 computation；steering 需要 white-box/semi-white-box access，单层 nearest-centroid gate 未覆盖 multilingual、multimodal、tool-use 或生产 Agent。
- **Trade-off / fallback:** stage-wise inspection 增加数据暴露、存储和 evaluator 成本；不可见 CoT 时仍须依赖 output inspection、least privilege、sandbox、typed authorization 与 outcome receipt。
- **Score / owner:** `3+2+3=8`；Deep Review；`PLATFORM-SECURITY`，对读 `PLATFORM-EVALUATION-SYSTEM`。
- **Books Decision:** `No Change — Existing Coverage`。Ch72 已区分 CoT monitor、output inspection 与 action/outcome authority；Ch66 已要求输入、trace、输出分别验收。
- **Primary:** https://arxiv.org/html/2605.05678v1

### `SF-2026-ARXIV-2605-05715` — Decodable but Not Corrected

- **Problem / changed constraint:** hidden-state failure signal 线性可解码，不代表沿同一方向 steering 能纠错。
- **Mechanism / ownership:** 论文测试 29 个 fixed linear steering configuration，覆盖 contrastive、probe-guided、multi-layer、rank-k 与 dynamic gating；同一 probe 另用于 selective abstention。Sensor、intervention 与 release decision 必须分权。
- **Evaluation:** Llama-3.1-8B-Instruct 的 12,000 traces、三类 failure regime；full test `n=1,273`。fixed steering 近零收益，shared steering `-12.1pp`，erasure `-3.6pp`；Qwen2.5-7B 与 MMLU-STEM 给出相同 null direction。probe AUROC `0.610`，60% coverage 时 accuracy `72.3%`（+5.5pp）；self-consistency AUROC `0.804` 但约 10× cost。非线性 adapter `+2.8pp` 同时有 `8.2%` damage。
- **Proof / non-proof:** 仅覆盖两个 7–8B model、以 MedQA 为主；Qwen 没有 erasure，对 intervention family 也非穷尽。不能把 fixed-linear negative result 外推为所有 steering 不可行。
- **Trade-off / fallback:** probe 可降低 coverage 换 accuracy，却需要目标模型/任务校准；无法证明 causal correction 时只允许 abstain/escalate，不能让 probe 直接拥有 actuation authority。
- **Score / owner:** `3+2+3=8`；Deep Review；`PLATFORM-EVALUATION-SYSTEM`。
- **Books Decision:** `Integrate — Queued`。Ch66 已有“sensor 不是 truth”，但缺少“decodability 不是 intervention efficacy”的明确负面证据与 fallback。
- **Primary:** https://arxiv.org/html/2605.05715v1

### `SF-2026-ARXIV-2605-05750` — RVPO

- **Problem / changed constraint:** 多目标 reward 的算术均值允许一个高分目标补偿安全、格式等低分硬约束，平均 reward 会隐藏 bottleneck failure。
- **Mechanism / ownership:** 用 LogSumExp/SoftMin 形成 inter-reward variance penalty，把 aggregation 从 maximize sum 推向 risk-sensitive consistency；risk coefficient `k` 与 curriculum schedule 属于训练控制面。
- **Evaluation:** HealthBench / GPQA-Diamond 的 rubric reward 与 tool-calling rule reward；Qwen2.5 3B/7B/14B；group size 分别 16/4。作者结果依赖 reward normalization、judge 与训练 schedule。
- **Proof / non-proof:** 最佳静态 `k=5` 会在后期 collapse，aggressive start 也会归零；最差 criterion 可能只是 noisy reward channel 而非真实 policy weakness。不能把 SoftMin 当作声明优先级或安全约束的充分表达。
- **Trade-off / fallback:** 提升 bottleneck adherence，代价是对 reward dimensionality、group size、objective conflict 与 noise 更敏感；reward 不可靠或约束需要 hard guarantee 时回退分项指标与 deterministic gate。
- **Score / owner:** `3+2+2=7`；Deep Review；`TRAIN-RLHF`，对读 `TRAIN-GRPO`。
- **Books Decision:** `Integrate — Queued`。
- **Primary:** https://arxiv.org/html/2605.05750v1

### `SF-2026-ARXIV-2605-06036` — SelectiveRM

- **Problem / changed constraint:** preference data 包含异质噪声；strict mass conservation 会强迫 reward model 为 outlier 分配匹配质量并过拟合错误偏好。
- **Mechanism / ownership:** Joint Consistency Discrepancy 对齐 feature/prediction 与 preference；partial optimal transport 通过 mass quota 排除与 semantic consistency 冲突的样本。Data/RM owner 决定 admission，policy optimizer 只消费版本化 reward artifact。
- **Evaluation:** HelpSteer、UltraFeedback、PKU-SafeRLHF；Qwen2.5/LLaMA2 7B–72B；下游 GRPO safety 使用 HarmBench/FFT/DAN，并以 DeepSeek-V3 作 judge。
- **Proof / non-proof:** 理论上界只针对被选择子集，依赖 clean samples 具有更高 semantic-preference consistency 的假设；系统性或 adversarial noise 可破坏此前提。作者 benchmark 不能证明真实 annotation pipeline 的噪声可识别。
- **Trade-off / fallback:** 可拒绝 noisy mass，却引入 `O(N²)` cost matrix、mass quota、embedding identity 与 online scaling 成本；假设/校准失败时保留原始 preference、人工 dispute 和简单 robust loss。
- **Score / owner:** `2+2+2=6`；false-negative 修复执行 Deep Review；`TRAIN-RLHF`，对读 `TRAIN-DATA`。
- **Books Decision:** `Integrate — Queued`。
- **Primary:** https://arxiv.org/html/2605.06036v1

### `SF-2026-ARXIV-2605-06078` — BEACON

- **Problem / changed constraint:** long-horizon Agent 的 terminal reward 会把正确前缀、已完成 subgoal 与终局失败一并置零，造成 credit misattribution 与 successful-sample waste。
- **Mechanism / ownership:** 环境 milestone detector 冻结 segment boundary；segment 内 temporal shaping 与 dual-scale advantage 将局部 progress 与 global outcome 分开。Milestone identity 由 environment/harness 持有，不能由同一 policy 事后改写。
- **Evaluation:** ALFWorld、WebShop、ScienceWorld；discrete action/text interaction；group size 8、最多 15/30 steps、每 checkpoint 128 samples；与 GRPO/GiGPO 使用相同主要训练配置。
- **Proof / non-proof:** milestone 依赖 domain pattern/page transition/explicit subgoal；粒度过稀退化成 terminal reward，过密会增加噪声。未覆盖 continuous control、multi-Agent 或无可验证 state transition 的任务。
- **Trade-off / fallback:** 提升 credit density和样本利用率，代价是 milestone engineering、reward shaping bias 与环境版本耦合；无法证明 milestone 时回退 terminal/critic/verifier 分支。
- **Score / owner:** `3+2+2=7`；Deep Review；`TRAIN-GRPO`。
- **Books Decision:** `Integrate — Queued`。
- **Primary:** https://arxiv.org/html/2605.06078v1

### `SF-2026-ARXIV-2605-06200` — A2TGPO

- **Problem / changed constraint:** pooled normalization 混合不同 turn position 的 context distribution；累积项数随深度变化又使 advantage scale 漂移，固定 clipping 不能区分 turn informativeness。
- **Mechanism / ownership:** 在 `(prompt, turn-index)` group 内标准化 information gain，以累计项数平方根重标定 discounted advantage，并在 turn boundary 用 stop-gradient IG 调节 clip range。Group builder 持有 membership，optimizer 只消费冻结的 turn-level credit。
- **Evaluation:** 7 个 single/multi-hop QA benchmark、Qwen3-4B/8B 与 Qwen2.5-7B；Wikipedia local retriever；8×H20；VeRL；报告约 `+2.9%` step-time net overhead，但 IG forward 单项约 `+164s`。
- **Proof / non-proof:** 需要 ground-truth answer，直接适用限于 verifiable outcome；同 turn index 的 state similarity 随深度下降，不能把 position 等同于真实 state equivalence。未覆盖更长 tool suite 或生产异步 trajectory。
- **Trade-off / fallback:** 无外部 PRM 即可细化 credit，但增加每 turn target likelihood forward 与小 group variance；group size≤1 时退回 outcome reward。
- **Score / owner:** `3+2+2=7`；Deep Review；`TRAIN-GRPO`。
- **Books Decision:** `Integrate — Queued`。
- **Primary:** https://arxiv.org/html/2605.06200v1

### `SF-2026-ARXIV-2605-06308` — Black-box trajectory confidence

- **Problem / changed constraint:** self-consistency 只测 sample agreement，单一 verbal confidence 也不能覆盖“正确候选从未被提出”；black-box confidence 必须拆分 signal ownership。
- **Mechanism / ownership:** `Coverage` 表示 judge-mediated candidate reachability，`Geometry` 表示 embedding trajectory 对 answer anchor 的收敛，`Verbalization` 是条件性的 self-report channel；fusion 与阈值必须按 deployment setting 校准。
- **Evaluation:** MedQA-USMLE、GPQA Diamond、MMLU-Pro；Gemini 3.1 Pro / Claude Sonnet 4.6；matched setting 中 `K=4` fusion 对 `SC@8` 为 6/6 Pareto improvement，另做 fixed-pick 与 E5 embedder control。
- **Proof / non-proof:** Coverage 受 LLM judge 解释影响；Verbalization 只在 6/18 open-ended settings 提供额外 signal；3 个英文 benchmark/3 个 reasoner 不代表跨语言/模态；within-trace score 无法恢复没进入 candidate set 的真值。
- **Trade-off / fallback:** 以 K 次 rollout 与一次 embedding 换较低 sampling cost，但仍需 slice calibration、external evidence 与 abstention；judge/embedder drift 时回退可执行 verifier 或人工。
- **Score / owner:** `3+2+2=7`；Deep Review；`PLATFORM-EVALUATION-SYSTEM`。
- **Books Decision:** `No Change — Existing Coverage`。Ch66 已把 coverage、black-box consistency、trajectory/internal signal、verbal confidence 作为异质 sensor，并要求校准、risk–coverage 与 abstention。
- **Primary:** https://arxiv.org/html/2605.06308v1

## 同类 closure 有界反查

本轮没有用关键词命中直接下结论。先从 canonical 513 closures 中按四类错误理由构造风险层，再逐项读 title+abstract；只有明确改变长期 state/data/control owner 或 evaluation/training contract 才重开。

| 风险层 | 反查的代表项 | 结论 |
| --- | --- | --- |
| simulator / stage-wise evaluation | `05678`, `05741`, `05777`, `06308` | 重开 `05678`、`06308`；`05741` 的 cognitive-effort probe 与 `05777` 的 proxy uncertainty 仍依赖特定 proxy/training recipe，未给可升级为系统 authority 的校准或跨 workload contract |
| steering / probe / runtime control | `05892`, `05980`, `06342` | 保持 closure；均为受限 activation-steering implementation，未改变 canonical owner，且不能从 AUC/benchmark 直接升级为 intervention authority |
| preference / reward aggregation | `05750`, `06036`, `06070` | 重开 `05750`、`06036`；`06070` 仍是 text-to-image 的局部 offline reward recipe |
| long-horizon credit / verifier | `05893`, `06078`, `06200`, `06660` | 重开 `06078`、`06200`；`05893` 是局部 unsupervised verifier，`06660` 是数学题生成的三方 self-play 实例，均未改变现有跨 workload owner |

另外，旧 screening ledger 中的 `05686`、`06225`、`06241` 不在本日报 canonical 619 raw set，不能借本次 closure 修复移入 05-08。若其他 owner date 尚未收录，需由 root 按 first-public/official-batch identity 定点 reconciliation，而不是在本日报补记。

## Books writeback 与 Gate

- 精确写回队列：`BOOKS_WRITEBACK_QUEUE_FALSE_NEGATIVES_ROUND2.md`。
- 本 lane 未修改 Books。
- 05-06 duplicate reconciliation 与三个非本窗 family 的 owner 检查均交 root，不改变本窗 `619` raw。
- 作者交接时账本满足 `619 = 106 + 513`，`Review Pending = 0`，当时存在 `5 Integrate — Queued`，因此作者不能签 Completion Gate。

## 后续状态

Root 已按队列完成 5 项 Books 写回，并把当前 V3 活动账本同步为 `49 Applied + 57 No Change`。本文件上方逐项 `Queued` 是作者交接时的历史状态，不是当前状态；最终 Gate 仍等待未参与修复与写回的新 reviewer。
