# 2026-09-18 Books 串行写入队列

本文件保存本日返修后新增的 Books Decision、精确写入合同与写后核验结果。原有三项共享 Books 修改、定点返修新增的两项，以及本轮重开的两项既有实质绑定均已按日期顺序核对，并已通过 fresh non-author write-after audit。

## 已完成整合

### 2609.18357v1 — Market Signal Injection

- **Owner：** `PLATFORM-SECURITY`，`books/part-06-ai-infrastructure/72-security.md`
- **建议锚点：** `## Prompt Injection 与 Tool Boundary` 中“不可信数据不能取得指令或 effect authority”的主线；放在输入 provenance/canonicalization 与 tool/output commit gate 之间。
- **长期语义增量：** 输入没有显式 instruction、数值也未改变，format、competitor ordering 与 sentiment commentary 仍可改变 LLM agent 的决策。因此防线不能只检测命令式 prompt injection：应先把 untrusted market/context data 规范化为 canonical representation，再以独立 decision boundary 约束输出，并让最终 effect gate 保留 commit authority。
- **证据边界：** 九个 open-weight 与三个 proprietary models 的模拟 Bertrand 市场；matched neutral-text controls 和 rule-based agent 支持 framing account。held-out activation probe 的高 AUC 只证明分布可分，不证明 probe 识别有害决策。canonicalization 消除的是所测 sentiment attacks；anchoring 在 adaptive attacks 下只有部分效果。
- **Trade-off / failure / fallback：** canonicalization 会损失真实语义或排序信号；硬 output projection 会牺牲策略空间且可被适应性攻击绕过。失败时回退到结构化数据 schema、规则约束/人工审批和不可绕过的 effect authorization；不得让 probe 或 prompt constraint 单独放行。

### 2609.18560v1 — The evolution of sex for artificial intelligence

- **Owner：** `TRAIN-DATA`，`books/part-04-training-system/27-data.md`
- **建议锚点：** `### 递归合成语料要先分清 Corpus Recursion 与 Parameter Recursion`；在 synthetic feedback/collapse 后增加“真实样本注入与多父继承不是同一控制量”的分支。
- **长期语义增量：** recursive output training 的退化不仅取决于 real/synthetic ratio；在论文模型中，真实样本的绝对注入量决定 immigration pressure。多父模型也不能只按数量评价：平均父输出可能抵消互补，保留各父最强贡献或合并 specialists 才可能获得收益；merge compatibility 更受冲突 convention/parent disagreement 影响，而非普通参数距离。
- **证据边界：** exact inheritance model、训练的 recurrent/feedforward/VAE generators 与有限 LLM specialist/merge experiments 形成跨层次证据；人口遗传学映射仍是条件模型，不是所有架构、语料和 optimizer 的通用定律。作者结果不提供生产固定 ratio、parent count 或 merge threshold。
- **Trade-off / failure / fallback：** 持续注入真实数据提高 provenance、采集和验证成本；多父组合增加 evaluation 与 lineage 状态；参数平均可造成能力抵消，冲突 convention 可使合并失败。回退为保留经过验证的真实 holdout、独立保留 parent checkpoints、先测 parent disagreement/merge compatibility，失败时不合并而采用 routing/ensemble 或回到最后通过 Gate 的 lineage。

### 2609.18857v1 — Taming the Agentic RAN

- **Owner：** `AGENT-MULTI-AGENT`，`books/part-07-agent/82-multi-agent.md`
- **建议锚点：** `### Coordination State 必须有显式 Owner 与 Commit Transition`，并与 `Coordination Failure` 中的振荡/冲突恢复相邻。
- **长期语义增量：** 两个各自正确的 agent 只要共享控制变量并各自 commit，就可能形成任何单体都不会产生的 recurrent excursion。应把 agents 降为 proposal producers，由唯一 arbiter 持有 commit authority；arbiter 对 shared state 应同时检查 feasibility invariant、per-variable dwell 和 deadband，并记录 proposal、rejection reason 与 committed transition。
- **证据边界：** live OAI/FlexRIC O-RAN testbed 和论文假设下的 convergence proof；共享状态振幅从 8.4 降至 0.4 PRB、cross-slice starvation 从 40–55% 降至 0.3%，但 protected slice 自身 latency compliance 没有改善。结果不证明任意 multi-agent domain 都能用同一参数或得到全指标收益。
- **Trade-off / failure / fallback：** arbitration 牺牲 individual-agent responsiveness；dwell/deadband 过强会迟滞，过弱会振荡；单变量 proposal schema 不能表达耦合动作，且可行点不等于全局最优或公平。无法表达/收敛时回退到 composite proposal/coordinator、serial execution 或人工控制，并保留 last-known-safe shared state。

## 已由 root 串行整合并通过独立复核

### 2609.18270v1 — BENCHCOMPASS

- **Owner：** `PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`
- **建议锚点：** 评价条件与证据 identity 主线；放在“可访问上下文不等于模型会使用它”及 perturbation/control 讨论附近。
- **长期语义增量：** 同一模型应在 closed、open 与 attacked-open 三个条件下对照。closed 失败可指向 parametric knowledge 缺口；open 仍失败说明 context-use gap/interference；answer-preserving attacked-open 失败则暴露 harness/格式脆弱性。每个 evidence pack 要绑定来源定位、适用问题和扰动 provenance，不能只记录总分。
- **证据边界：** 306 个专家最终接纳的 payment-domain 案例；结果不覆盖 retrieval、tool use、multi-agent 或任意领域。repair hypotheses 只是诊断映射，不是已验证的因果修复；judge sensitivity 与 domain coverage 仍限制外推。
- **Trade-off / failure / fallback：** 三条件评价增加 evidence 构建、专家接纳和 perturbation 验证成本；若攻击改变答案语义，归因会失真。回退为保留 closed/open baseline、人工核验扰动等价性，并将无法区分的失败标记为 Unknown，而不是强行归因。

### 2609.18649v1 — DyMT-ESB

- **Owner：** `PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`
- **建议锚点：** 多轮/状态化评价主线；位于 single-turn case contract 向 workflow/trajectory evaluation 的演进段。
- **长期语义增量：** 多轮评价不能预先冻结所有 user turns，因为真实的下一轮输入依赖模型上一轮响应。evaluation identity 应携带 conversation history、turn frontier、user-generation policy、judge version 和停止条件；同时报告首次出现、持续、消退与重新出现的 failure，而不是只给固定轮数终值。
- **证据边界：** 240 个 seed stereotypes、六类偏差、六个模型、5/10-turn 对照与 human judge validation。用户由模型合成，generator/judge 主要依赖 GPT-4o-mini；不能外推真实用户发生率、所有模型或所有风险类型。
- **Trade-off / failure / fallback：** 动态对话提高生态有效性，但降低跨 run 可比性并引入 generator/judge confounding；长对话也提高成本。回退为同时保留 deterministic replay、固定-turn baseline 和人工抽检，对不稳定分支报告分布与停止原因，不压缩成单一 score。

## 定点返修确认已有实质绑定，不重复写入

### 2609.18622v1 — How Many Labels Does Model Choice Need?

- **Owner：** `PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`
- **现有绑定：** `<!-- source-family:SF-2026-ARXIV-2609-18622 -->`；正文位于 `### 模型选择需要与目标指标绑定的标注证书`，唯一且在章末 `Review notes` 之前。
- **长期语义增量：** prediction agreement 不能统一决定模型选择的标注预算；selection objective 改变时，同一 disagreement support 对 accuracy 与 AUGRC 的证书闭合能力可能完全不同。应按 metric、tolerance 与不可区分候选集维护证书，并在证书闭合时停止采样。
- **证据边界：** exact-v1 的固定 pool/candidate predictions/ranks、binary 或共享 multiclass predictions、`K<=8` 与 108 个 panel comparisons；disagreement labels 在所测 panel 中闭合全部 accuracy choice，却没有闭合 AUGRC choice。该结果不覆盖 retraining、transfer、distribution shift 或任意模型库，也不提供通用标签比例。
- **Trade-off / failure / fallback：** metric-specific acquisition 和 certificate 增加评估实现与审计成本，严格 exact choice 仍可能需要标注大部分 pool。目标、slice 或模型版本变化时证书失效；回退为扩大标注、保留多个不可区分候选，或明确 abstain，不能用 agreement 代替真值。

### 2609.17904v1 — Timely Activation of Safety Filters via One-Step Reachability Expansion

- **Owner：** `MULTIMODAL-EMBODIED-VLA`，`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`
- **现有绑定：** `<!-- source-family:SF-2026-ARXIV-2609-17904 -->`；正文位于 `### 离散控制周期要为 Safety Filter 预留一步可达域`，唯一且在章末 `Review notes` 之前。
- **长期语义增量：** continuous-time HJ filter 的安全不变性不能直接外推 sampled control。最坏情况一步可达域可能在下个控制更新前跨入 unsafe BRT，因此 filter 应按 reachability、采样周期、扰动与 actuator delay 提前扩张触发边界。
- **证据边界：** exact-v1 的理想命题依赖准确动力学与设定假设；Dubins-car 仿真每个采样周期 100 次、完美状态且精确模型，扩张 filter 的 safe outcomes 仍为 67–86/100。论文明确说明没有完全消除 continuous-discrete mismatch，且未验证真实机器人、高维动力学或未知扰动。
- **Trade-off / failure / fallback：** 扩张会增加误触发、保守轨迹和模型误差敏感性；过小无法覆盖周期内跃迁，过大则侵蚀可行动作空间。失配、周期抖动或扩张失败时，应降低控制周期、启用硬件急停/低层约束，或停止高层 policy。

## 已有正文覆盖，不写 Books

| Source Family | Owner | 已有具体命题 | 本次不追加的原因 |
| --- | --- | --- | --- |
| `arxiv:2609.17989v1` | `AGENT-PROMPT` / Ch74 | prompt 输入必须携带 role、authority、scope 与 provenance；模型生成的角色服从不能替代外部 policy/evidence 验证 | principal assignment 导致 sponsorship bias 是该命题的受限实验实例，没有新增独立状态机制或控制面 owner |
| `arxiv:2609.18440v1` | `PLATFORM-EVALUATION-SYSTEM` / Ch66 | 相关/可解码/曲线相似不能取得 causal claim；复现必须分离 observable、site、intervention 与 mechanism | 论文复现 Figure 形状却未恢复 newline-resident mechanism，正好落入已有证据边界，无需重复案例 |
| `arxiv:2609.18516v1` | `MULTIMODAL-REPRESENTATION` / Ch23 | modality-specific encoder 到 shared token space 需要显式 alignment/compression contract；continuous/discrete token identity 与 distillation 边界要分别验收 | ACIF/DTW 与单层 KD 是该主线的一个 speech operating point，没有改变 canonical representation owner |
| `arxiv:2609.18306v1` | `AGENT-MULTI-AGENT` / Ch82 | belief state、message effects、herding、correlated error 与最终行动应分别观测 | biased minority 对 numeric opinion 与 rhetoric 的不同影响是该既有边界的受限实验实例 |
| `arxiv:2609.18520v1` | `AGENT-MULTI-AGENT` / Ch82 | role、authority、local state、message 与 commit owner 必须显式分离；physical execution 向 Ch26 handoff | AeroWeaver 的 UAV harness 是现有 coordination/embodiment 分层的实现案例，没有新增 canonical owner |
| `arxiv:2609.18860v1` | `PLATFORM-EVALUATION-SYSTEM` / Ch66 | probe decodability、causal intervention、native routing 与 behavior/effect evidence 是不同证据等级 | sparse probe、knockout、patching 与 recovery 实验落入既有证据层级，不需重复案例 |

## 写后验收

七项均已完成正文写入或既有实质绑定核对；fresh non-author reviewer 已核验：

1. 正文锚点真实存在，新增段落位于旧方案边界、约束变化与下一步压力的连贯推理链中；
2. 机制 owner 唯一，没有把论文名称或数值当正文主语；
3. evidence boundary、trade-off、failure mode 与 fallback 均可在正文定位；
4. Daily、Source Review 与 Books 的命题一致；
5. 实际 Books 内容而非本队列声明已完成 fresh-context 复核；`2609.18622v1` 与 `2609.17904v1` 的 marker 各自在全书唯一，正文位于章末 `Review notes` 之前。
