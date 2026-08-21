# 第74章 Prompt

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-PROMPT`
**Legacy Chapter:** Ch70
**Status:** Draft

**Roadmap Intent:** Prompt 是 LLM 时代的新接口，也是软程序。

## 本章要回答的问题

Prompt 为什么能在不更新参数的情况下改变模型行为？把它称为“软程序”成立到什么程度？为什么更长、更强硬的 system prompt 不能代替权限、安全和业务校验？

本章的核心判断是：**Prompt 是送入模型条件分布的版本化运行时输入。它可以描述任务、提供示例、约束输出并暴露工具，但执行语义由概率模型、上下文和外部控制面共同决定，因此不是具有确定语义的传统程序。**

## Prompt 改变的是条件，不是参数

Decoder-only 模型在每一步计算：

```text
p(token_t | token_<t, theta)
```

`theta` 是训练后的参数，Prompt 成为 `token_<t` 的一部分。更换 Prompt 会改变条件分布，却没有发生 gradient update。GPT-3 展示的 zero/one/few-shot in-context learning 属于这一层，不应被描述成模型在运行时“学会并永久保存”了新知识。

Prompt 的效果依赖模型、tokenizer、chat template、上下文位置和 decoding settings。脱离这些条件讨论“万能提示词”没有稳定意义。

## 从字符串到结构化接口

真实 Agent prompt 通常由多种来源组装：

```text
system policy and role
+ developer/application instructions
+ user request
+ conversation state
+ retrieved data
+ tool schemas and results
+ output schema
```

这些片段的信任级别不同。User input、网页、文档和 tool result 都是不可信数据；把它们串进同一个文本，不会自动让模型区分“指令”和“引用内容”。

应用应保留 segment source、trust label 和 version，使用 message roles、typed fields、quoting/delimiters 与 constrained output 来减少歧义。结构能降低风险，不能证明模型永不越界。

## Prompt 作为软程序

Prompt 与程序有相似之处：

- 描述目标和约束；
- 提供 examples 作为 demonstrations；
- 定义输入输出 contract；
- 选择可用 tools；
- 改变控制流倾向。

差异更关键：

| 传统程序 | Prompt |
| --- | --- |
| 语义由语言/实现定义 | 语义由模型分布经验性实现 |
| 相同输入通常确定 | sampling、runtime 与模型版本会改变结果 |
| type error 可明确拒绝 | 自然语言约束可能被部分遵循 |
| 权限由执行环境强制 | 文本只能表达意图，不能授予安全权限 |

因此 Prompt 适合表达 task policy，不适合成为唯一 enforcement point。

## Instruction、Example 与 Schema

三类内容作用不同：

**Instruction** 说明要做什么、何时停止和不可做什么。

**Examples** 通过上下文展示输入到输出的模式。示例质量、顺序和覆盖范围都会影响结果，也可能把偶然格式变成模型模仿对象。

**Schema** 缩小可接受输出空间。JSON Schema、grammar 或 enum constrained decoding 能保证部分句法，却不能保证字段事实正确、参数被授权或业务操作安全。

一个稳健接口将三者分离，并在模型外验证：

```text
model output
→ parse
→ schema validation
→ semantic/business validation
→ authorization
→ execution or rejection
```

## Chain of Thought 的边界

Chain-of-Thought demonstrations 在特定模型和任务上可改善多步推理，这是经验结论，不是模型一定暴露真实内部因果过程的证明。

生产系统更应关心可验证 intermediate state：计划节点、tool arguments、retrieved evidence、test result。隐藏或压缩自由文本 reasoning，可以降低泄露、成本和脆弱依赖；不能把一段流畅解释当作正确性证据。

## Prompt Injection 为什么不能仅靠 Prompt 修复

Indirect prompt injection 把恶意指令放入网页、邮件或检索文档。模型收到的 token 同时包含应用指令与攻击内容，而模型并没有传统安全内核来强制 trust hierarchy。

有效防线在模型外：

- 最小化可见 data 和 tools；
- 将 untrusted content 标记并隔离；
- tool call 做 typed validation 与 authorization；
- 高风险 action 要 confirmation；
- 限制 egress、scope、step 与 budget；
- 记录 policy decision 和 side effect。

“忽略所有恶意指令”可以是提示，但不是 security boundary。

## Prompt 生命周期

Prompt 应像配置和代码一样管理：

```text
prompt_id + version
model/tokenizer/chat_template
tool schema versions
evaluation dataset
online cohort
owner and rollout status
```

修改一个词也可能改变行为，因此需要 offline regression、canary、rollback 与 observability。Prompt evaluation 必须覆盖 task success、format、safety、tool choice、latency 和 token cost，而非只比较少量漂亮回答。

### 追加规则容易，可逆地删除规则很难

长期维护的 Prompt、`AGENTS.md` 或 procedural skill 往往从一次次局部失败中追加规则。每次追加都可能
合理，但若只保存“以后不要这样做”，没有保存它防止了什么失败、在什么条件下成立、如何证明已经
失效，后来的维护者就很难安全删除。规则老、触发少或与别处相似，都不等于它已经无用：最昂贵的
不是删掉一行文本，而是重新证明所有相关 constraints 仍被覆盖。

因此 Prompt change 应同时保存 decision rationale 与 falsification condition：

```text
instruction + scope / guard
+ observed failure and evidence
+ expected outcome
+ supersedes / conflicts-with relation
+ validation that permits removal
```

随着规则增长，维护流程也会从 append-only 演进为 typed consolidation：先把 trigger、workflow edge、
tool argument、exception、stop condition 与 output field 抽成 contract，再区分重复、修订、新增和需要
局部重构的 patch。压缩目标不是“最短文本”，而是在保留稀有 guard 和不确定原文的前提下，消除重复
表达；结构检查只能证明抽取出的 contract 没有丢失，不能证明任意自然语言改写在所有模型、task 与
decoding 条件下行为等价，最终仍要经过本章前述 regression 与 canary。

这条路线不会否定短小、人工维护的 Prompt。规则少、owner 明确时，直接 review 更透明；只有长期
自演化、重复 patch 与上下文成本开始成为主要矛盾时，rationale ledger、局部 consolidation 与周期性
全局 repack 才值得引入。2026 年关于 agentic instruction files 与 SkillZip 的两篇预印本分别提供了
“缺少 rationale 会形成保留棘轮”和“typed contract 可保留稀有要求”的受控证据；前者的真实仓库
部分是观察研究，后者的 fidelity guarantee 只覆盖抽取 contract，均为 `Status: Experimental`。

### 从固定 Prompt Score 到 Constraint-residual Feedback

Prompt A/B test 或自动改写常先把 task accuracy、tool cost、handoff、长度、安全和格式压成一个固定 scalar。
当约束少且优先级稳定时，这种方案便宜、容易比较；但部署中的 active constraint 会随 domain 和候选变化：同一
权重可能在 Airline 场景过度调用工具，在 Retail 场景又因过度保守损失成功率。Pareto candidate set 也不会自动
决定哪个点满足必须遵守的 threshold。

若这些要求能够被独立测量，可以把 Prompt search 演进为一个受限反馈回路：

```text
versioned prompt pool + objective + explicit thresholds
→ evaluate objective and each constraint residual
→ residual-conditioned rewrite proposals
→ feasibility-aware candidate retention
→ update per-constraint multipliers
→ offline regression / canary / rollback
```

这里的 multiplier 只改变“下一轮优先修哪个 failure”，不把 Prompt 升级为 hard-policy owner。Schema、authorization、
privacy 和 side-effect safety 仍由模型外 validator 与第 72 章 enforcement 执行。若一个候选在有限 evaluation set 上
满足 threshold，它只是 **empirically feasible**；model、chat template、tool schema、traffic slice 或 judge 改变后都要
重新校准。

这条路线比固定 penalty 更能适应 constraint 轮换，也允许 task model 保持冻结，却新增 candidate-evaluation 成本、
threshold/judge noise、multiplier oscillation、Prompt overfitting 和 constraint gaming。离散 rewrite 也不是可微梯度；
任何 primal-dual 收敛类比都依赖 surrogate smoothness、rewrite alignment、bounded pool/noise 等假设。CAPO/DCAPO 的
作者实验在若干 Agent、assistant 与 privacy tasks 上支持 residual-driven search 的受限价值，但硬件、完整 API cost
与生产 SLO 未披露，不能把“feasible”写成安全证明或跨模型行为等价。

人工 Prompt + deterministic regression 在约束少、风险高或评估数据稀缺时继续成立；固定 scalar 在业务 trade-off
稳定时更简单；Pareto set 在需要人工选择 operating point 时仍有价值。Constraint-aware search 只在 metric owner、
threshold、holdout 与 rollback 都明确时成立，下一阶段压力是处理相互冲突约束、反馈漂移和线上不可逆动作，而不是
让 rewriter 获得更多 authority。

## 本章在知识树中的位置

第 73 章交付 platform identity、policy 与 security。Prompt 是 Agent runtime 的第一个可变输入，但它只是一部分；下一章讨论 Context 如何在有限 token budget 中选择、排序并组装 Prompt、历史、检索结果和工具状态。

## 自检问题

1. Prompt 为什么不会更新模型参数？
2. Prompt 与传统程序最重要的语义差异是什么？
3. Schema constrained output 能保证什么、不能保证什么？
4. 为什么可读 Chain of Thought 不是正确性证明？
5. Prompt injection 的 enforcement boundary 应放在哪里？
6. Prompt version 为什么必须绑定模型和 tool schemas？
7. 一条长期 instruction 要具备哪些 evidence，才能被安全删除或 consolidation？

## 小结

Prompt 是概率模型的运行时接口，可以表达任务和软约束，却不能承担确定执行和权限隔离。下一章把它放入完整 Context assembly，研究有限上下文如何成为 Agent 的工作状态。

## Review notes

本章承接第 18、20 章的条件生成语义与第 72、73 章的安全/发布契约。Prompt engineering 保持在 runtime input 层，不与 SFT 或模型能力本身混写。

Primary-source 入口：

- GPT-3 / in-context learning: https://arxiv.org/abs/2005.14165
- Chain-of-Thought prompting: https://arxiv.org/abs/2201.11903
- BIPIA / indirect prompt injection: https://arxiv.org/abs/2312.14197
- Catastrophic Remembering（Status: Experimental；instruction rationale 与删除边界）:
  https://arxiv.org/abs/2608.11095
- SkillZip（Status: Experimental；typed contract consolidation）:
  https://arxiv.org/abs/2608.11079
- CAPO / DCAPO（Status: Experimental；constraint-residual-driven Prompt search）:
  https://arxiv.org/abs/2608.16068
