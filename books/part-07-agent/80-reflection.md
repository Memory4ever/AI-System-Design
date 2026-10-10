# 第80章 Reflection

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-REFLECTION`
**Legacy Chapter:** Ch76
**Status:** Draft

**Roadmap Intent:** 模型如何基于反馈修正自己的中间结果。

## 本章要回答的问题

Reflection 为什么有时能改进结果，有时只会把错误解释得更流畅？它与 verifier、retry、RLHF 和训练更新有何区别？何时应该停止迭代并升级给人？

本章的核心判断是：**Reflection 是 inference-time feedback loop：根据可观察结果生成诊断，再修正 plan、output 或 memory。它不更新模型参数，效果受 feedback independence、verifiability 和 stopping policy 限制。**

## 基本循环

```text
candidate y_0
→ feedback f_0 = evaluate(y_0, evidence)
→ revised y_1 = refine(y_0, f_0)
→ ...
→ accept | stop | escalate
```

Self-Refine 让同一模型产生 feedback 和 revision；Reflexion 将环境反馈总结为语言并写入 episodic memory。
二者是**不修改权重的 verbal test-time adaptation**，不等同于第 31～34 章的参数训练或 policy optimization。
更激进的分支会在 episode 内把 retrospective feedback 编译成 LoRA/weight update；它仍发生在 test time，
但 ownership 已跨入参数状态，不能继续只称为 Reflection：

```text
trajectory + outcome
→ retrospective diagnosis
→ bounded adaptation dataset / objective
→ ephemeral parameter update
→ validation on next attempt
→ commit, reset or rollback
```

这可能把经验从 Context 内化到 policy，却新增 optimizer state、base/adapter identity、catastrophic drift、
contamination 和 rollback。Verbal reflection 在任务短、风险高或不能验证更新时继续成立；参数 adaptation 只有
在 scope、budget、held-out verifier、reset 和 provenance 明确时才可使用。Reflective Test-Time Planning 的
论文提供了这一边界案例，不证明 episode-level LoRA update 普遍优于语言反馈。

## Feedback 来源决定价值

Feedback 可以来自：

| 来源 | 示例 | 独立性 |
| --- | --- | --- |
| Deterministic verifier | compiler、tests、schema、constraint solver | 高 |
| Environment | API result、game state、user correction | 中高 |
| Separate evaluator | judge model、specialized classifier | 取决于模型/数据 |
| Same model self-critique | “检查自己的答案” | 低 |

同一模型可能在 generation 与 critique 中重复同一盲点。External tests 和 environment outcomes 通常比自由文本“再想想”更可操作。

反思也可以只在自评低于阈值时触发，而不是每次都重写：先把原则放入生成条件，再让同一模型逐项打分，任一项未达门限才合并批评并修订。它仍增加逐项 self-evaluation 调用和 token，相对不反思的 base 并不免费；这节省部分无条件修订，却把漏检变成新的停止失效路径；评分者与被评分 policy 相关，微调后仅在回答中提及原则就可能骗过自评门，让本应修订的回答直接停止。原回答、自评分、是否触发及修订后的独立判据应分开保存；一次 revision 还可能引入新违反。[受限 constitution 实验](https://arxiv.org/html/2601.18730v1)的较少 token 同时伴随比对照更高的 violation，不能签发同安全效果下的降本或部署安全证书。无可靠独立反馈时，保留完整规则检查、无自评门的受限修订或升级人工，而不让高 self-score 认证合规。<!-- source-family:SF-2026-ARXIV-2601-18730 -->

即使已有 render observation，revision 信号仍可能被生成 trajectory 内的自我解释束缚。一个分支让 critic 在独立 context 中读取结果与约束、提出修改，再检查重生成是否遵循反馈，只有通过一致性与质量筛选的轨迹才用于蒸馏。[DeepPresenter 的受限对照](https://arxiv.org/html/2602.22839v1)在同一任务集合各采300条训练轨迹，不是冻结完全相同的300条轨迹；teacher 与 critic 同为 Gemini3Pro，独立的是 context 而非模型或训练来源。缺陷统计另在相同300条轨迹上比较，发现更多缺陷不等 true defect recall；GLM 过滤、GPT5内容/style judge 与多样性指标也不授 truth。<!-- source-family:SF-2026-ARXIV-2602-22839 -->

因此 critic 只拥有 revision proposal，最终 rule/render 或 human verifier 保留独立验收职责。1,024采样筛到802条 SFT、128 held-out 的作者协议不代表部署故障率；作者仅披露 approximately80 GPU hours on8 A800 GPUs，不能换算成80墙钟小时或640 GPU hours，也未给全成本/净 SLO。错误反馈可能改坏结果，同源盲点仍存在；缺可靠约束或 revision 遵循验证时，保留原 render、普通 retry 与独立复核，不把蒸馏成功率当永久自我改进保证。

已有 observation 也未必自动成为经验：Agent 可能保留历史，却没有把结果绑定到产生它的 preceding action。一个 in-task 校准分支只给现有观察标注 action–outcome 归属，不加入新环境信息；另一个分支把候选 lesson 与未加 lesson 的后续 action 比较，再筛选是否值得持续保留。前者是表示干预，后者是限定 continuation 下的效果 proposal，二者都不把重复减少当任务成功，也不由打乱 history 后的小幅下降推定内部因果机制。

Persistent lesson 可能写入未经支持的归因、减少重复却使整段 rollout 退步，故应保存 lesson 来源、适用 episode 与直接反侧，允许撤销或回退原 history。[Action Calibration 的受限实验](https://arxiv.org/html/2610.02769v1)用跨 actor 的 next-action judge 选择 lesson，非真实 task-success 标签；额外 reference segment 未在当前恢复状态中执行，不能冒充真实 continuation history，联合调用又改变轨迹 teacher 来源。额外 review 调用、persistent context 和错误更新都应计价，端到端 SLO 未披露；缺可靠 outcome 或效果验证时，保留原观察、局部诊断与真实执行验收，不把 learned calibrator 当成功 authority。<!-- source-family:SF-2026-ARXIV-2610-02769 -->

对已经交付的报告，revision 还多一项不能由“满足新反馈”替代的义务：原来覆盖的内容与引用是否仍然成立。可以把当前目标的 incorporation 与原已满足项的 break 分开测量，逐轮保留上一版的检查项与引用对应关系；format 修改也应接受同样的保留检查。这里 checklist/judge coverage 只是限定评价协议下的覆盖判断，不拥有事实 truth。新目标已经满足，不认证旧目标、citation faithfulness 或 claim groundedness 自动保持。<!-- source-family:SF-2026-ARXIV-2601-13217 -->

[多轮报告修订的受限反侧](https://arxiv.org/html/2601.13217v1)在五种 Deep Research Agents、模拟专家反馈与选定题目中发现：当前反馈的满足可以与旧内容、以前修复目标及引用质量退化同时发生。先把反馈转成编辑计划，或另设 ReAct reviser，仍留下超过10%的平均 break 和引用退化；它们还改变模型、搜索及调用预算，不能据此归因于单一 scaffold。由此推导的设计要求是让 revision proposal 与版本保留验收分权，把必要旧义务的丢失标成未决并保留原版本；它不是作者框架已提供的零破坏保证。额外检查与检索增加费用，缺可靠旧项评价或事实证据时，应采用局部编辑、独立复核或回退旧稿，而非依靠更多轮自检认证报告正确。

Deterministic verifier 的高独立性只覆盖它实际收到的对象。把自然语言推理逐步翻译成逻辑断言时，solver 可以检查给定前提是否蕴含结论，却不能顺带证明翻译忠实、补入的常识为真，或这些前提确实来自原任务而非待证明答案。应保留原文、所选历史前提、额外假设与形式化版本，把 translation/fidelity 审核和 solver result 分账；auto-formalizer 或同模型 judge 仍是可错的提案者，机械有效不等整条自然语言推理可信。

当模型生成并修复自己的测试时，还必须保留**原检验义务**：目标路径、输入条件、独立预期与 helper 版本属于测试提案的身份，compiler 或 sanitizer 通过只说明当前程序/测试可编译或未触发相应运行错误。若 repair 把输入退化到 early return，或修改 assertion 来适配该输入，通过率可能提高而原算法不再被检验；[受限 C 单元测试实验](https://arxiv.org/html/2602.16671v1)实际观察到这条反侧。因此改变 oracle 或目标输入不能默默继承原测试的通过标签，应另核目标路径覆盖与语义断言；这是独立检查的工程要求，不是原框架已实现的正确性保证。逐路径生成、helper 校验、sandbox 与多轮 repair 增加成本，也不能消除不可达路径和不完整 oracle；无法独立确认检验目标时，保留未决结果并回到固定人工测试或人工复核。<!-- source-family:SF-2026-ARXIV-2602-16671 -->

搜索的停止策略还可能改变“verified”的含义。低分步骤可以触发定点重生、回退或保留已核前缀；若有限重试耗尽后为了进展选最高分候选强制前进，或返回未完成路径，应明确交付 unresolved 结果，不能继承逐步通过的标签。[LogicTrack 的受限实验](https://arxiv.org/html/2609.21492v1)同时出现最终正确率与核验率不同方向的变化；形式化、judge 和搜索调用增加成本，离线蒸馏 backtracking 轨迹也不把 solver 证明迁移到无 solver 模型。高风险路径不能强制前进时应停止或升级，普通可容错任务仍可使用有明确未决标记的尽力搜索。<!-- source-family:SF-2026-ARXIV-2609-21492 -->

但反馈带来一次成功，也不代表原诊断已经正确。需要归因时，Reflection 只提出修复假设；保留原执行 prefix、检验修复是否遵循该假设及限定 outcome flip 的证据强度，由 [Trace 的受控重放](../part-06-ai-infrastructure/69-trace.md#从-linear-trace-到-root-cause-graph)接手。这样把“修好任务”和“解释原失败”分开，避免成功重试反过来授权错误归因。

还可以把修复提案细分到发生的时点：同一种行为放在 feedback 或 refinement 阶段，不必产生相同作用。先从轨迹提出候选行为，再分别强调单项与联合项，保留不加提示的对照，才能检查两条建议是互补还是相互干扰。由 judge 标签和结构学习得到的行为 graph 只负责提出这个实验设计；随机划分观测样本后未拒绝均值/方差不变，不等于已获得真实环境干预、排除潜在混杂或识别因果父节点。<!-- source-family:SF-2026-ARXIV-2602-06373 -->

这种分解增加轨迹采样、行为标注与提示对照成本，而且提示可能同时改变多个行为，必须另验是否真遵循了目标指令。[受限时点对照](https://arxiv.org/html/2602.06373v1)在四个模型上的单项与联合效果不同，联合强调两种行为的平均结果反而不及无提示；总体显著性检验也不能证明所有成对差异或唯一作用机制。对当前模型/任务没有可重复收益、行为遵循无法确认时，保留单项受控修复、普通 retry 或独立 verifier，不把观测 hierarchy 提升为普遍自我改进规则。

独立反馈的价值还取决于提出什么问题。若模型只测试当前假设已经预测为真的例子，环境不断返回“成立”仍不足以排除其他规则；多生成正确答案，也不代表更善于发现自己的假设错误。一个条件分支把反思对象移到下一次查询：显式保留当前假设及其补集，或改变例子的一个关键属性，优先选择可能否定当前解释的测试，再用真实环境反馈更新假设。模型拥有查询提议，环境拥有观察结果；“看起来相反”的测试不一定真的能区分假设，反例数量也不是最终成功率。

这条路径增加交互、推理和测试预算；没有可验证反馈、查询会产生不可恢复副作用，或反例主要偏离任务时，应使用静态测试、受限 sandbox 或人工确认。离线训练可以模仿 teacher 的测试查询，甚至保留最终未解出的 episode，而不只蒸馏成功答案；这会继承查询与 judge 偏差，不能自动形成通用证伪能力。`arXiv:2604.02485v1` 的规则发现与有限迁移对照中，任务成功、与当前假设不兼容/兼容的查询比 `I:C` 和 thinking mode 的变化并不总一致；`I:C` 不表示已经成功证伪的比例，部分小模型迁移也未显著。不能把这一查询策略写成正确性保证。<!-- source-family:SF-2026-ARXIV-2604-02485 -->

还有一条发生在**执行前**的反思分支：先判断候选推理—行动对是推进任务、合理探索还是会污染后续状态；只对后者重写成对的理由和动作，再交由真实工具执行。它避免为高熵 tool response 虚构完整环境预测，也比单纯给一句 critique 更直接地改变下一步提案；但专用 judge 只能决定是否建议修订，不能拥有工具权限或最终结果真值。提交的仍是带版本的 action proposal，执行后的 observation 才能确认状态。AEWM 的作者实验覆盖 Search、Terminal、SWE 的受控轨迹及若干 Agent backbone，不能证明此三分类在新环境准确，且增加额外模型调用与错误改写风险；判断器不稳时回退原提案加独立 verifier 或直接停止。<!-- source-family:SF-2026-ARXIV-2609-28416 -->

多约束任务还存在一种有用的不对称：一次发现同时满足所有条件的 candidate 可能很难，
但检查 candidate 是否分别满足每个条件往往更容易。Reflection 因而不应只输出整体
“通过/失败”，而应把 verification 结果转成下一轮的控制信号：

```text
provisional candidate
→ constraint-wise audit
→ verified | unresolved | conflicting | invalidated
→ preserve valid progress
→ target the remaining uncertainty
```

这并不保证 verifier 正确；它只是避免每轮从零搜索，或在已有证据尚未满足所有约束时
过早接受答案。

## Reflection 应输出可执行诊断

### Verification-centric Reflection：先定位 Evidence Gap，再决定重跑什么

Deep Research 的失败可能来自问题构造、证据检索、trajectory synthesis、candidate answer 或 final selection。
只让模型“再想一次”会把这些 failure planes 混在同一段文字里。更可靠的反思对象是 versioned evidence graph：
verifier 输出哪个 claim 缺 source、哪条 path 矛盾、哪个 tool result 不足，再由 workflow 选择局部 repair、
discard-all restart 或停止。

这种结构增加 verifier/tool critical path，也会继承 same-model judge bias；高置信、短链路任务仍可直接 retry。
Marco DeepResearch 的数据构造与 inference loop 提供一个受限实例，但其 call budget、judge 与 mixed baselines
不能外推为通用 deep-research policy。

### 从固定 Reflection Prompt 到 Learned Adaptation Policy

当同一 task 可以从 reset state 重复运行，并能比较 episode outcome 时，可以离线学习一个 meta-policy，把前序
episode evidence 编译成下一 episode 的 actor prompt/state update。Workflow owner 必须持有 environment reset、
episode budget、mutable prompt fields、policy revision 与 rollback；模型文本不能自行宣称 reset 或越过 immutable
safety policy。

Learned reflection 可能减少手工规则，却新增 meta-overfitting、cross-episode leakage、prompt drift 与额外调用成本。
固定规则在 episode 少、reset 不可靠或 safety surface 不可修改时仍成立。Meta-TTL 的作者结果是 Experimental
case，不证明任意 OOD domain 都能通过 test-time reflection 自我改进。

有用 feedback 应定位：

```text
failed criterion
evidence
suspected cause
affected plan/output state
proposed bounded change
confidence
```

“答案不够好，请改进”会导致无方向重写。结构化 diagnostics 让 workflow 决定局部重试、replan 或回滚。

### 从“结果失败”到“最早可修复偏离”

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05980:start -->
### Trajectory Drift Sensor 不能取得成功 Authority

只在 episode 结束后根据 outcome 反思，能保持运行时简单，却无法区分正常长思考与已经进入 overthinking/overacting 的轨迹。若模型可观测，一条受限路径在 trajectory step 上标注 calibrated、overthinking 与 overacting，学习 residual drift axes，并在越界时施加有界 activation steering。Sensor 只建议继续、收缩或停止，外部 verifier、budget 和 effect policy 仍拥有正确性与提交权。

提前干预缩短无效轨迹，也会引入 judge 标签偏差、方向相关而非因果、跨模型失效和白盒依赖。现有证据只覆盖所测 coding agents，不能证明线性可分方向是普遍机制或 steering 天然安全。没有白盒访问、axis calibration 漂移或副作用风险较高时，应回退 observation-based loop guard、hard stop/budget 与外部 verifier。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05980:end -->

最终 outcome 只能说明整条 trajectory 没有满足目标，不能直接说明应该从哪里修。长链路中，后续
步骤可能只是沿着早期错误继续执行；若 Reflection 只重写最后答案，它会保留真正的因果偏离，
若整条轨迹从头再跑，又会丢掉已经验证的工作并重复支付 tool 与 token 成本。

更可操作的 failure audit 应把三个问题分开：

```text
localize earliest evidence-backed critical step
→ attribute a bounded root cause
→ emit a repair directive and affected-state boundary
→ resume, replay or replan under an explicit gate
```

`critical step` 不是“第一个不完美动作”，而是最早有证据支持、并对最终失败具有直接因果意义的
偏离；证据存在容忍区间时，应保留一个 step span，而不是制造虚假的单点精度。Root cause 也不应
只写成模型能力标签，而要落到可改变的 failure class，例如 retrieval coverage、evidence misuse、
constraint violation、premature conclusion 或 environment/tool error。Repair directive 必须引用相关
evidence 和仍然有效的 state，不能只是重新措辞原问题。

多视角 auditor 可以分别从最终约束向后追溯、沿 timeline 向前检查，再由显式 evidence 进行
adjudication；多数票只有在错误近似独立时才增加可信度。离线 frozen trace 还存在硬边界：它不能
恢复未记录的 environment state，单一 primary-cause schema 也会压扁多个共同致因。因此高风险
failure 仍需人工复核，在线 resume 前还要重新验证外部状态和副作用。

SearchAuditor 是这一路线的实验性案例。它的公开结果来自已知失败、可在冻结轨迹中定位的
deep-search runs；端到端 audit 即使在作者最佳配置下也远未成为可靠 oracle。本章吸收
`localize → attribute → repair` 的控制分解，不把论文准确率、错误分布或恢复率外推到其他 Agent、
工具环境和生产流量。

对长时程研究，diagnostics 还应形成 task-scoped improvement state：保留已验证 evidence
及 provenance、未满足约束、冲突、已淘汰 candidate 与下一步 objective，删除重复
observation 和已失效 plan。它比普通摘要更接近状态压缩，因为压缩目标不是“更短”，
而是保留下一次决策所需的事实边界。

AREX 为这种双层 research / audit loop 和 improvement state 提供了一个实验性实现。
论文结果来自作者在 deep-research、reasoning 与 tool-use benchmarks 上的实验，尚无
独立复现；本章只吸收机制边界，不把其模型规模、训练 recipe 或 benchmark gain 外推为
通用 Reflection 收益。

在线纠偏还可以把观察与主执行解耦：observer按固定step间隔消费已记录trajectory，在后台判断已知misbehavior并产生有限DO/DONT；主agent不等它，下一次action之后发现结果ready，才把提醒注入后续上下文。[Wink的原版本接口](https://arxiv.org/html/2602.17037v1)用system-reminder承载提示，改变的是nonblocking诊断的交付时点，不是让observer取得tool、policy或任务成功authority。snapshot与delivery之间主轨迹仍可能推进，因此提醒应绑定所读step与当前state，过期或冲突时重验/丢弃；这是工程防误用边界，不声称原实现已有staleness保证。Meta的15天局部A/B与shadow比较提供在线净效应线索，但triggered轨迹中由LLM judge判“同类行为不再出现且有进展”的recovery，不等全部session的最终正确率；一次trajectory可含多次invocation，不能把其独立比例检验升级为cluster因果保证。时间改善未达所报显著性，taxonomy、同时实验及未披露observer总成本也限制外推。异步延迟或judge资格不稳时，同步loop guard、强verifier与普通retry仍合理；提醒数量减少或主轨迹token下降，不能代替最终任务验收。<!-- source-family:SF-2026-ARXIV-2602-17037 -->

固定主模型参数和 system prompt 时，另一条恢复分支把诊断放在每轮首个 control action 之前：外部模型读取当前对话、用户输入、工具集合和有限 error→plan 映射；返回 No 就沿原控制流程，返回 Yes 才追加一次 `think[恢复计划]`，随后仍由原 policy 采样动作。这与异步提醒不同，会先支付诊断调用并阻塞该轮首次行动；[ReIn 的接口和直接对照](https://arxiv.org/html/2602.17022v1)还显示，建议与已定义的 recovery tool 耦合，无对应工具的道歉策略并不能取得相同恢复效果。因此这是上下文干预位置与工具能力的联合选择，不是外部模型写入内部推理权限、绕过指令层级或更安全的保证。受测 Claude/τ-bench 人口中，ambiguous 成功要求新 internal report 加原目标，而 unsupported 的 human handoff 已在原 prompt 中，baseline 差额不能单归因于思考内容；动态案例也仅覆盖 airline/Sonnet 的有限预算。诊断、用户模拟和恢复行动的总成本、误报与当前状态都要另验；工具不匹配或判断不稳时回到普通澄清、授权升级或同步 verifier，不由 recovery plan 自签任务完成。<!-- source-family:SF-2026-ARXIV-2602-17022 -->

## 反思对象要分开

系统可以修正：

- output：格式、事实、表达；
- tool arguments：参数或目标；
- plan：依赖、顺序、替代路径；
- context：缺 evidence、冲突、压缩损失；
- memory：错误写入、过期事实；
- policy configuration：只能由授权 owner 修改。

模型不能通过 reflection 宣称安全 policy 是阻碍并自行删除。Policy violation 的正确动作通常是 reject/escalate。

## Stopping Policy

无限循环会消耗 token、tool calls 和 wall time，并可能来回振荡。停止条件可包含：

```text
verifier passes
max_iterations
no material delta
same failure repeats
budget/deadline reached
risk threshold exceeded
human decision required
```

Runtime 必须持久化 attempt、feedback 和 decision。只把全部历史重新塞入 Context 会越来越长，还可能强化错误。

当迭代只是把上一轮输出交回固定模型、prompt 与 decoding，且每次独立调用不携带历史或外部反馈时，可以把当前文本视为状态、整个改写接口视为同一个转移 kernel；这比有工具、记忆和环境变化的 Reflection 更窄。固定 greedy 可能很快进入同一字符串或短周期，runtime 因而可以同时记录表面 recurrence 与独立 evidence delta：前者帮助发现重复调用，不能证明当前答案正确，后者也不能由“文字终于稳定”替代。Prompt、decoder 或 schedule 改变后应重新识别这条状态转移，不能静默沿用固定 kernel 的解释。<!-- source-family:SF-2026-ARXIV-2603-11228 -->

受限改写对照中，sampling 延迟 exact recurrence、产生更多不同表面句子，却没有因此证明语义忠实或事实增长；段落整体重复也比单句少。这是固定 checkpoint 下的 inference-time reuse，不是重新训练生成数据的 model collapse。[作者的450首句、每条50轮实验](https://arxiv.org/html/2603.11228v1)只支持这条有限接口边界；更多采样增加调用预算并可能累计偏移，不能作为无限反思或安全早停保证。需要真实改进时仍应回到独立 verifier、外部 observation 和原有预算上限；缺乏新证据时可以保留原文、停止或升级人工，而不是只为摆脱字符串重复提高 temperature。

历史结果还可提供一种较窄的行为 sensor：按同一目标模型过去 recheck 的 confirmatory/non-change 标签检索经验，用当前前缀窗口的 BM25 邻居比例与阈值决定是否抑制本次核验，并用显式 cooldown 限制反复触发。离线标签可以观察后续轨迹，部署 query 却只能使用当时已见前缀；预测“不改结果”不等于当前步骤正确，closure 信号也不能冒充事实已验证或校准置信度。Classifier、label pool、目标模型/mode、窗口、阈值与冷却规则应共同版本化，检索和额外控制调用须计成本。[受限数学对照](https://arxiv.org/html/2602.03485v1)中，统一抑制核验导致质量下降，选择性抑制仍有阈值取舍与激活循环；减少主轨迹 tokens 不是端到端降本或安全早停保证。经验失配、高风险或出现新证据时，应恢复核验、独立 verifier 与原有预算停止条件。<!-- source-family:SF-2026-ARXIV-2602-03485 -->

停止决策还须把“修正错误”与“误改正确答案”分开。设初答正确的比例为 `A`、纠错使错误变正确的条件概率
为 `ECR`、使正确变错误的条件概率为 `EIR`，一次修订在二态近似下的净正确率变化是
`(1-A)·ECR − A·EIR`。当 `A` 已高时，即使模型能修复部分错误，误改成本也可能使默认再答不合算；
因此继续、验证、保留初答或交人工应依据这两个转移及额外调用预算，而不是只看“有错误被修好”。
<!-- source-family:SF-2026-ARXIV-2604-22273 -->

Verify-first 可以先用独立证据缩小需修订的分母，但 verifier 的判断不能由同一个模型的自信陈述充当真值。
这项证据只在 GSM8K 的 500 题与七个受测模型上比较受限的 self-correction 策略；额外验证与模型调用
有成本，方法间调用预算也未严格等同。二态转移是单轮诊断，不直接给多轮稳定策略或开放工具任务的
停止保证；缺可靠 verifier、高误改率或预算紧张时，应保留初答、转入有界人工复核或使用旧固定停止条件。

每一步都调用强 critic 可以更早纠偏，却把成本和 critic 盲点放大到整条 trajectory。一个分层 monitor 可先用
便宜、已校准的 uncertainty proxy 检测 search/reasoning drift，只在残差越界时触发 slow critic 与经验检索：

```text
cheap trajectory sensor
→ calibrated normal relation / threshold
→ selective slow diagnosis
→ bounded repair or memory proposal
```

Token entropy、embedding cluster entropy 等只是 proxy，不是 factual confidence；threshold 会随模型、retriever
和 domain 漂移。未校准或高风险任务仍应直接使用 deterministic verifier/strong review，slow critic 的输出也
必须经过第 77 章的 Memory write gate。分层监控优化的是 critique allocation，不是让 self-reflection 成为 oracle。

一种更主动的分支不只是调用 critic：当局部 token entropy 与窗口波动同时升高时，用同一模型在当前前缀后追加负向反思提示，得到另一组 logits，再作有系数的对比引导；另定期用不同提示对当前状态抽取答案，仅在提示内主答案稳定且提示间一致时提议早停。前者改变下一步生成分布，后者决定是否继续付出生成成本，不能把二者混成“反思发现了真相”。负提示诱导的分布未必代表错误，跨提示一致也可能共同出错，仍需独立任务评价。<!-- source-family:SF-2026-ARXIV-2604-02967 -->

这类干预需访问 logits、维护附加分支并支付周期性 probe 成本；减少主轨迹 token 不等于等比例降低 latency。受限数学/问答与 A100 实验支持其净成本比较，不证明开放工具任务或生产并发收益。错误传播的分支过程模型依赖指定生成与风险假设，比较两个错误概率上界不能证明首个答案总更正确。新证据能纠正旧假设、任务需要探索或 probe 不可靠时，应继续受预算约束的检索与验证，而不是普遍删掉后续推理；无需修正的低风险任务仍可直接回答。

局部 proxy 还有一个结构盲点：当前 action 看起来低风险，不表示它没有继承数步之前的错误 tool result、timeout
或错误假设。把历史只压成 sequence score，又会混淆真正的 continuation、平行尝试与已收到 environment feedback
的分支。监控粒度可以进一步从当前 token/step 演进为 dependency-aware trajectory state：

```text
reasoning / tool / observation nodes
→ temporal, continuation, parallel, feedback and goal-alignment edges
→ local uncertainty + relation-aware propagation
→ trajectory risk estimate
→ selective verifier, replan, abstain or human escalation
```

这种图是从 trace 派生的 telemetry，不是环境真实 causal graph。Rule cues、tool signatures 或 embedding similarity
可能漏掉隐式依赖，也可能把语言相似误判成控制依赖；传播还会放大早期误差并让 graph 随 trajectory 增长。Graph
builder、relation weights、model/harness/tool revisions、threshold 与 calibration slice 因此必须共同版本化。Score 只能
拥有“是否升级检查”的建议权，不能授权工具、副作用或写入长期 Memory。

RUPA 的作者实验在 tau2、Terminal-Bench-2、GAIA 与六个公开模型上支持 relational feature 对 local/linear
uncertainty proxy 的受限补充，并展示了较早失败检测与多样本选择；硬件、额外 latency/cost、并发和 production SLO
未披露，best-F1 threshold 也不是可直接部署的 operating point。短任务、强 executable verifier 或高风险 action
仍应直接验证；只有 dependency signal 经 held-out slice 校准、且 selective review 节省大于 graph cost 时，这条分支
才成立。下一阶段压力是用可执行 intervention 与环境证据校准 edges，而不是继续增加图的复杂度。

压缩后的 improvement state 仍属于当前 run 的 working state，不应仅因它概括了经验就
自动升级为第 77 章的长期 Memory。跨任务写入仍需要 source、scope、confidence、expiry
和 supersession policy。

### 先显式采样 Belief，再决定 Answer、Clarify 或 Abstain

直接从单次 hidden state 判断是否回答，问题清晰且模型校准时成本最低；歧义对话中，单一路径会隐藏竞争解释。Reflection owner 可以先采样 K 个 belief hypothesis，再依据分歧选择回答、澄清或 abstain。收益是把 epistemic branch 变成可检查状态，代价是 K 倍采样和 aggregation bias；样本高度相关、模拟用户或 judge 偏置时，分歧并不代表真实不确定性，应回退规则澄清或人工处理。exact-v1 只支持 BAG 的所测数据、模型和模拟评估，不证明 belief samples 是真实 posterior。<!-- source-family:SF-2026-ARXIV-2605-25831 -->

## Reflection 与 Retry 的区别

Retry 对相同 operation 再执行，适合 transient failure；Reflection 修改 candidate/plan 后再尝试，适合可诊断缺陷。

端到端恢复常把两者混在一起：检测失败、路由重试、提供 critique、重新 grounding 与 candidate selection 是不同 treatment。只有 paired ablation 能把额外收益归因于 rich reflection；若简单 retry 已解释大部分 recovery，就不应把结果记给长 critique。机制分解提高实验成本，却能避免把第二次采样机会误写成自我纠错能力。

第二轮读到草稿时，还应拆开三个可能作用：重新解题的额外采样、空白但符合输出格式的 review scaffold、以及草稿内容本身。对照需匹配模型、题目、调用预算与提示结构，再分别给出无草稿重答、空 scaffold 和真实草稿条件；否则弱模型草稿的“帮助”可能只是重新解题，代码任务的收益也可能来自补齐语法骨架。真实内容甚至可能锚定错误实现，空骨架反而更好；但弱草稿对某些更弱 reviewer 仍有用，不能把单个代码基准外推为“总该丢弃草稿”。这条归因把额外调用与评估成本换成可选择的 retry/review 路径，具体策略仍需按任务、模型能力和外部 verifier 校准。

<!-- source-family:SF-2026-ARXIV-2604-01029 -->

<!-- source-family:SF-2026-ARXIV-2609-12746 -->

若失败来自 authorization deny，重复或改写调用不应绕过 policy。若远端 action outcome ambiguous，应先 reconcile state，而不是让模型“换一种方式再做一次”。

Reflection 的候选来源也应分开：当前执行后的 episodic feedback、外部 bank 中有来源的旧经验，以及**持久权重学到的跨样本诊断 generator**。[ParamMem 的有限分支](https://arxiv.org/html/2602.23320v1#S3)用 LoRA 从问题产生可能错误/子任务，与当前反馈拼接，另一配置再检索成功 trace；它扩展诊断假设，不直接接触当前环境，也不把更高 embedding 多样性当已找到真实错误原因。训练/温度/额外 token 的不匹配限制收益归因，部分任务仍弱于 DoT-bank，HotpotQA 还付出更多 prompt tokens；自生成训练版不等整个流程无监督、无测试或无准备费用。训练、筛选、采样和 verifier 全计费，当前证据须独立验证，错误模式固化、domain shift 或预算不值时回退原始执行反馈、确定性检查与普通 retry，不把参数化 proposal 自动晋升为长期 Memory 事实。<!-- source-family:SF-2026-ARXIV-2602-23320 -->

外部 error bank 也应把“适用”与“违反”分开。将历史失败提出的 indicator 写成 name、error definition 与 trigger condition，先按当前 scenario/action 与 trigger 的相似度检索，再让 rectifier 在 role/input/output 上依据 definition 判断是否需要修改；持续未通过才拒绝转发。这使旧经验消费有一个显式资格接口，而不是把相似案例直接当当前失败真因。[AgentDropoutV2 的受限对照](https://arxiv.org/html/2602.23258v1)中retrieved五项55.25高于random五项50.21，但检索命中、binary flag与teacher诊断都不认证 truth。<!-- source-family:SF-2026-ARXIV-2602-23258 -->

MATH/AQuA已知答案用于离线失败挖掘，code 的 generic indicators 是另一迁移设置；Qwen3-4B/8B非thinking、GPT4.1mini selector与Q4o teacher的权限不混合。更多indicator或第四次reflection反而退步，额外调用未被统一预算控制；剩余消息过少时全局reset也不是可靠 consensus 或安全终止证明。挖掘、检索、rectification与重试全计费，硬件、精度、端到端SLO未披露；bank缺适用项、OOD或反馈失准时，应使用原始执行证据、确定性检查或普通有限retry，不能通过丢消息假装所有错误已被隔离。

## 写入 Memory 的风险

Reflexion 风格系统会保存 linguistic feedback。只有当 feedback 与 task result 绑定、可追溯且适用范围明确时，才应进入 Memory。

一次任务的 workaround 不一定是全局 procedure；错误 critic 可能成为 durable poisoning。Memory write policy 应记录 source、confidence、scope、expiry 和 supersession。

## Evaluation

应比较：

- first-attempt success；
- final success after reflection；
- iterations/cost/latency；
- verifier false accept/reject；
- regression introduced by revision；
- repeated failure classes；
- escalation quality；
- memory transfer to new tasks。

只报告 final success 会隐藏十倍调用成本和失败样本选择偏差。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-11543:start -->
Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-11543:end -->

### Reflection 的停止条件需要 Typed Epistemic State

递归反思如果只问“答案是否更好”，很容易在同一证据上改写措辞而不增加信息。每轮应输出 typed epistemic state：哪些 claim 已有证据、哪些存在冲突、哪一步缺 observation，以及新的 proposal 相对前一轮缩小了多少 order gap。这个 gap 只能作为 local diagnostic；truth 仍由 evidence gate 决定。

停止策略同时受证据增益、预算与最大迭代数约束。gap 不再下降、验证器反复冲突或预算耗尽时，系统应返回当前已证实部分并暴露未知，必要时转人工，而不是无限递归。固定轮数在低风险、成本敏感任务中仍是有效上限；typed state 的价值是让停止原因可解释，而不是保证找到真相。

<!-- source-family:SF-RECURSIVE-STATE-TERMINATION -->

## 本章在知识树中的位置

Planning 产生预期路径，Reflection 消费实际反馈并修正。下一章 Workflow 将两者放入 durable state machine，确保 retries、approvals、timeouts 和 side effects 在进程失败后仍有一致语义。

## 从机制演进到系统设计

Reflection 从生成一段自评文字演进到可治理的 skill/strategy revision 后，candidate lesson、decision history、held-out evaluation、rejected alternative、promotion 与 rollback 必须分离。随机 masking 或新任务 slice可以估计某条 skill 的增量价值，但 verifier 与 policy 不能在同一证据上共同漂移。

持久反思提高跨任务复用，却会引入自证偏差、skill dependency、权限扩散和错误经验固化。held-out 失败、因果贡献不稳定或新任务回退时，应拒绝 promotion、恢复旧 skill 或交还人工；短任务的一次反思仍只是一条候选诊断。

## 自检问题

1. Reflection 为什么不等于参数训练？
2. 同一模型 self-critique 有什么相关性风险？
3. 哪类 feedback 最容易转成可验证修正？
4. Reflection 与 retry 的适用失败类型有何不同？
5. 为什么 policy deny 不应触发“换种方式”绕过？
6. Reflection 写入 Memory 需要哪些限制？
7. Task-scoped improvement state 与普通摘要、长期 Memory 有什么不同？

### Critic Accuracy 不等于 Intervention Value

资源受限时可以把 reflection 拆成 detector、comparator 与 actor：小模型先判断是否值得复核，再比较有限候选，最终 actor 仍负责生成或修订。Tiny advisor 只拥有排序/触发权，不拥有结论；其收益应以端到端错误减少减去额外调用成本衡量。任务简单、分布漂移或 advisor 校准不足时，直接生成与规则 verifier 仍更可靠。<!-- semantic-body-binding:SF-2026-ARXIV-2608-21027 -->

离线 critic 能准确预测轨迹将失败，仍不能推出“现在打断并提醒它”会提高成功率。介入价值应显式分解为 `recovered failures - disrupted successes - intervention cost`：相同的预测器可以在高失败任务中恢复部分轨迹，却在本来会成功的任务中打断有效状态。因而 deployment gate 应先在小型、代表性 pilot 上运行 paired intervene/no-intervene，直接估计净效应，不用 AUROC 替代该因果对照。

这个 gate 会增加 pilot 成本，也受任务 mixture、critic/model identity 与打断方式偏移影响。样本少或任务高风险时，不确定性应导致关闭自动介入、升级强 verifier/人工审批，而不是默认批量打断。作者披露的特定 agent/benchmark 结果不构成其他 workflow 的通用改进幅度。<!-- source-family:SF-2026-ARXIV-2602-03338 -->

比较器的预算分配也会改变 reflection 的收益：先用较便宜的 pointwise 分数建立排序，再把有限 pairwise 复核投给分数接近、尚未比较的候选，可减少把所有候选逐对比较的成本。覆盖阶段让低度数候选先获得比较机会，后续阶段再按 score gap 等不确定性代理安排近邻比较。这里的 gap 不是校准后的正确概率；初始覆盖也不能仅凭每个候选有一条边就声称整个比较图连通，最终选择仍依赖 evaluator 与候选池本身。

比较安排的验收应固定候选池、judge、任务和预算，区分 call 数、token 成本与 wall time。同模型生成并判断会共享盲点，pairwise feedback 不能凭空创造候选池中不存在的正确答案；预算小、分布漂移或判分退化时，保留简单 pointwise、随机比较及独立执行 verifier。[V1 v1 §4、§4.3](https://arxiv.org/html/2603.04304v1)中的固定比较调用预算消融支持选择策略的局部增量，不提供通用成本保证，也不把联合训练后的自判分数当外部正确性。<!-- source-family:SF-2026-ARXIV-2603-04304 -->

## 小结

Reflection 的价值来自 evidence-backed feedback、constraint-wise audit 和有界修正，
而不是让模型无限解释自己。Task-scoped improvement state 保存下一轮所需的有效进展，
但不自动成为长期 Memory。下一章用 Workflow 为这些循环提供持久状态和确定控制。

## Review notes

- `SF-2026-ARXIV-2602-17037` — Daily `2026-02-21`；[Wink exact-v1](https://arxiv.org/html/2602.17037v1) §3.1–3.3/§4.1–4.4/T3–6/§5；2+2+2=6，nonblocking snapshot/delivery两个时点的实际差额深入。只采用异步observer提醒接口，state/staleness为工程边界；Meta-only、triggered recovery与invocation分母、p.073及同时实验/observer成本限制近正文，不授全部任务或控制因果。root必要source/actual owner PRE通过并授窄锁；作者正文/完整邻接及末注已顺读，root非作者实际正文/完整邻接及自身末注POST通过，窄锁释放，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-06373` — Daily 2026-02-10；[ReBeCA exact-v1](https://arxiv.org/html/2602.06373v1) §3–4.2、§5.1–5.2/Table2、Limitations/AppA。2+2+2=6，stage-specific提案/单项与联合反退差额深入；CESR20sample最大cluster、GPT5/人工标签、randomfold ICP未授因果识别，CochranQ omnibus非每pair cause。四Qwen3/bnb4bit、50AIME局部prompting，硬件/temp/outcap未披露，未复现。root必要原源与owner写前通过，实际POST待核。

- `SF-2026-ARXIV-2603-04304`：[exact-v1](https://arxiv.org/html/2603.04304v1) §4–5、§4.3 固定比较预算消融；Daily 2026-03-06。只采用候选选择的比较预算分配，不采 gap 概率解释、图连通保证或自判 RL 的普遍质量提升。作者源/owner/邻接与实际写后检查完成；root 必要源、实际正文及邻接独立写后复核通过，未复现实验。

- `SF-2026-ARXIV-2604-22273`：[exact-v1](https://arxiv.org/html/2604.22273v1) §III–IV；Daily 2026-04-27。只吸收 ECR/EIR 与初始正确率共同决定单次修订净值、verify-first 需独立证据与额外成本的受限 stopping 分支；GSM8K/七模型、调用数不严格匹配及二态非多轮保证保留。作者已完成必要源与 Ch80/Ch84 owner 对读，root 独立 source→owner 及实际正文/邻接写后复核通过；未复现实验。

- Marco DeepResearch（verification-centric repair；Status: Experimental）: https://arxiv.org/abs/2603.28376
- Meta-TTL（learned test-time adaptation policy；Status: Experimental）: https://arxiv.org/abs/2604.00830

本章明确区分 inference-time verbal feedback 与 Part IV 的 RLHF/PPO/GRPO/DPO。论文中的任务级收益不被写成通用保证，成本与 verifier 误差一并保留。

Primary-source 入口：

- Reflexion: https://arxiv.org/abs/2303.11366
- Self-Refine: https://arxiv.org/abs/2303.17651
- ReAct: https://arxiv.org/abs/2210.03629
- AREX, 2026, `Status: Experimental`: https://arxiv.org/abs/2607.21461
- SearchAuditor, 2026, `Status: Experimental`: https://arxiv.org/abs/2608.05212
- RUPA, 2026, `Status: Experimental`: https://arxiv.org/abs/2608.16002
- Deep Search with Hierarchical Meta-Cognitive Monitoring（Status: Experimental）:
  https://arxiv.org/abs/2601.23188
- Reflective Test-Time Planning（reflection-guided parameter adaptation；Status: Experimental）:
  https://arxiv.org/abs/2602.21198

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-08671:start -->
- `SF-2026-ARXIV-2606-08671` — Daily `2026-06-08`；primary `arXiv:2606.08671v1`；Books review `books-review:SF-2026-ARXIV-2606-08671`。

  **已吸收的语义增量：** SkillHone 为 skill revision 保留 decision history、evaluation 与 rejected alternatives，使后续 agent 能解释、回退和继续演化持久技能。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08671:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11543:start -->
- `SF-2026-ARXIV-2606-11543` — Daily `2026-06-11`；primary `arXiv:2606.11543v1`；Books review `books-review:SF-2026-ARXIV-2606-11543`。

  **已吸收的语义增量：** Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11543:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14629:start -->
- `SF-2026-ARXIV-2606-14629` — Daily `2026-06-13`；primary `arXiv:2606.14629v1`；Books review `books-review:SF-2026-ARXIV-2606-14629`。

  **已吸收的语义增量：** Self-improving VLM 的 verifier 更新必须与 policy update 分离，并用 held-out new-task slice 与 rollback gate 防止 verifier在旧任务提升时对新任务回退。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14629:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15390:start -->
- `SF-2026-ARXIV-2606-15390` — Daily `2026-06-14`；primary `arXiv:2606.15390v1`；Books review `books-review:SF-2026-ARXIV-2606-15390`。

  **已吸收的语义增量：** Skill library 应用随机 masking 估计 per-skill causal effect，并对每任务只暴露有正贡献的最小集合。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15390:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16496:start -->
- `SF-2026-ARXIV-2606-16496` — Daily `2026-06-16`；primary `arXiv:2606.16496v1`；Books review `books-review:SF-2026-ARXIV-2606-16496`。

  **已吸收的语义增量：** experience reflection 只有在 candidate lesson、held-out validation 与 promotion 分离时才是可控演进；生成的反思不能直接覆盖运行策略
<!-- daily-books-trace:SF-2026-ARXIV-2606-16496:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16523:start -->
- `SF-2026-ARXIV-2606-16523` — Daily `2026-06-16`；primary `arXiv:2606.16523v1`；Books review `books-review:SF-2026-ARXIV-2606-16523`。

  **已吸收的语义增量：** Agent skill registry 需要 lineage、executable evaluation、dependency/permission metadata 与更新治理，不能把可检索文本集合称为 living skill infrastructure
<!-- daily-books-trace:SF-2026-ARXIV-2606-16523:end -->

- `SF-2026-ARXIV-2602-03485` — Daily `2026-02-05`；[Self-Verification exact-v1](https://arxiv.org/html/2602.03485v1) §3.1–3.3、§4.1–4.2、§5.1–5.4反侧。6分具体gap深入仅采用historical non-change标签→BM25/threshold→selective suppression的控制sensor，离线看后续与部署前缀信息分开；不是correctness/confidence oracle或训练两个policy。Classifier测试标签准确≠答案正确，pool 7:3 prior与τ需校准，full-suppress反退/阈值取舍/loop与3-step cooldown、额外calls均保留，不授万能安全早停。未运行代码或复现；root已实际核§3.1–3.3/§4.1–4.2及§5.1–5.4反侧、具体owner和201行正文/183–220邻接与末注，POST通过；日级Gate待验。

- `SF-2026-ARXIV-2602-17022` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17022v1) §3.1/Algorithm1、§4.1–4.2/4.5–4.6 与A直接限制。2+2+2=6，turn-start hook/assigned recovery tool耦合差额深入；不授safer/bypass hierarchy，新增report与原handoff评价人口、有限动态案例和额外调用费用近正文。root必要source/actual owner PRE通过；作者实际正文/完整邻接已顺读，root非作者实际正文178–192/末注434 POST通过，锁释放。未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-16671` — Daily `2026-02-20`；[SPARC exact-v1](https://arxiv.org/html/2602.16671v1) §3、§4.3.2 与评价/费用反侧。2+1+2=5，具体检验义务差额深入；原路径/input/oracle/helper identity 与 compiler/ASan pass 分权，独立目标核验为工程推导，未称原实现严格 gate。对照调用预算、drop/filter 人口、mutation/人评权限与退化 assertion 反侧保留。root 必要源/实际 owner PRE 通过；root非作者实际正文/完整邻接/自身末注 POST通过，窄锁释放；未运行 artifact 或复现。

- `SF-2026-ARXIV-2602-23320` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23320v1) §3–4/B.2/B.4必要方法/反侧，2+2+2=6；trained diagnostic来源与episodic/bank分责，部分baseline反退/更高费用、监督权限与固化回退近文。fresh非旧作者独核prepared原证与actual owner，root授该窄ownership；作者实际正文/完整邻接顺读，root非作者实际正文、完整邻接及自身末注POST通过，窄锁释放。未核代码/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22839` — Daily `2026-02-28`；exact-v1必要blocks28–54/63–82，2+1+2=5；独立context revision与蒸馏前遵循验证具体差额深入。final_audit非原packet作者必要原源/actual owner PRE通过，当前作者复用未变证据并实际读目标近邻，root授窄锁；正文/完整邻接及自身末注已实际顺读，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放，未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-23258` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23258v1)，2+1+2=5；当前作者非原packet作者必要原源/actual owner具体差额深入，root once准入通过并授窄锁。作者实际正文/完整邻接/自身末注已順读；final_audit非原作者必要原源/actual owner独核通过，root非写入者实际正文/完整邻接/自身末注POST通过，窄锁释放；未核实现/复现，非日级。

- `SF-2026-ARXIV-2601-13217` — Daily `2026-01-22`补查；[exact-v1](https://arxiv.org/html/2601.13217v1) §4.2/5.2/6.1，2+2+2=6，具体owner差额深入。新反馈 incorporation 与旧 coverage/citation 保留分责；judge非truth，模拟反馈、预算变化、reviser仍break与引用退化近正文。root实际必要原源/owner PRE通过并授两段窄锁；作者实际正文/完整邻接顺读，root非写入者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2601-18730` — Daily `2026-01-28`补查；[exact-v1](https://arxiv.org/html/2601.18730v1)必要机制、评价与直接反侧见本日 `supplement-reviews-20261008.md` 与 `supplement-pre-resume-20261008.md`。2+2+2=6，具体owner差额受影响深入；仅采用正文最小接口与相邻失败边界，不授全性能/安全/公平保证。作者与 resume_20260128_audit 必要Source及字面PRE通过，root重授本章一段/自身末注窄锁；作者已顺读完整局部邻接与自身note，resume_20260128_audit实际POST通过，窄锁释放，非DAY。未核artifact或复现。

- `SF-2026-ARXIV-2603-11228` — Daily `2026-03-14`增量；[exact-v1](https://arxiv.org/html/2603.11228v1) §3–6。2+1+2=5，固定改写kernel/recurrence与evidence delta具体差额深入；450首句/50轮、surface非semantic fidelity、无参数更新与prompt schedule边界近正文，不将标准Markov数学作为新理论。root实际必要原源/Ch80完整owner及逐字PRE通过授两段窄锁；mar14_supplement实际写后顺读正文/完整邻接与本人note，root真实新增225/227、完整Stopping205–301及本人末注回源非writer POST通过，窄锁释放。未核artifact/复现，不授日级DAY。
