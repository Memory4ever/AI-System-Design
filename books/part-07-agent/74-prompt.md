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

自动把 policy specification 编成 Prompt 与测试时，测试 oracle 也进入待验 artifact：可见失败能驱动改写，却可能让生成器只满足当前断言；hidden cases 与行为 mutation 应在候选冻结后另行检查。Mutation 必须确实改变目标行为，未激活或被排除的项不能混入 mutation score，编译失败的 run 也不能从成功率与预算中消失。[有限编译实验](https://arxiv.org/html/2603.08806v1#S5)中的测试通过与高分只覆盖所选 specification、mock tool 和成功编译人口，不授部署安全。发现 hidden failure 后可把它提升为 regression，但下一轮须更新独立 held-out，保存 spec/test/prompt/model/tool revision 与失败账。生成、验证、mutation 和重复调用均付费；测试相互冲突、oracle 不可信或预算耗尽时保留人工审阅、原 Prompt 与 canary/rollback，不由测试生成器同时宣布规则正确和外部 effect 可提交。<!-- source-family:SF-2026-ARXIV-2603-08806 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-13449:start -->
Repository instruction 文件进一步把 Prompt 变成工程控制面：它可能按目录层级被发现、继承、覆盖或根本没有进入某次 Agent 调用。因而不能用“仓库里存在规则”和最终 PR 是否成功之间的相关性直接证明规则有效。诊断至少要依次区分规则是否存在、runtime 是否读取、是否进入有效 Context、模型是否遵守，以及遵守后是否改变 terminal outcome；任一前置环节失败，都不应归因成模型拒绝服从。

这套可观测链会增加 instrumentation、matched run 与隐私成本，也不能证明自然语言规则具有确定语义。短任务或单一 Prompt 仍可直接做端到端回归；只有多层 instruction、目录继承或跨 Agent harness 出现时，才值得保留逐层 receipt，并把它与 model、harness、repository revision 和 evaluation contract 一起版本化。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-13449:end -->

<!-- source-family:SF-2026-ARXIV-2605-27784 -->

当多个 system、project、user 与 tool instruction 同时出现时，仅靠文本顺序和人工 review 解析 precedence，在规则少且冲突罕见时足够；规则增长后，同一组局部合理约束可能不存在共同可满足解，或只在某些输入上冲突。可执行的 prompt specification 可以先把候选约束编译成逻辑谓词，用 SAT/SMT 类检查发现 collision，生成最小 witness，并把选择的 resolution profile 绑定到部署版本。

形式检查拥有的是“抽取后约束是否一致”，不是自然语言意图真值。抽取错误、开放世界知识与概率行为仍需 regression、canary 和人工判断；过度形式化也会抬高维护成本。短 prompt 仍可直接审阅，只有多层 policy、重复继承与高代价冲突出现时，才值得用 executable spec 提前暴露不一致，并让 witness 成为可复现测试，而不是把求解器当作模型行为保证。

### 自动 Prompt 优化还要区分设计信号与采样噪声

反复测试候选 system prompt 时，reward 的波动同时来自 Prompt 对成功概率的真实改变和冻结 response model 的随机生成。若任务只返回二元正确性，同一 Prompt 的多次 response 可估计后一个噪声项；候选间总 variance 减去这项估计，才近似反映可优化的 Prompt 差异。将许多异质任务直接平均，可能互相抵消不同任务对 Prompt 的偏好，增加数据却削弱优化信号；这不是“少数据总更好”，也不等于 reward variance 越大越可学习。

一条受限分支先用足够重复采样估计这两类 variance，再选真实候选差异较大的小任务子集优化 prompt generator，并在未参与选择的任务上验收。额外采样、穷举子集和选择偏差都要计入预算；单题可过拟合，低噪声而容易的样本也会使 signal/noise 比值不稳定。[作者数学实验](https://arxiv.org/html/2604.08801v1)中小子集优于全量训练，但更同质的 instruction-following 任务仍以全量更好，跨模型迁移也只在受测 Qwen 家族内成立。任务偏好一致、数据少或二元反馈假设不成立时，人工 Prompt、全量 regression 与固定候选比较继续合理；选择器拥有的是实验预算，不是外部真值和安全权限。<!-- source-family:SF-2026-ARXIV-2604-08801 -->

固定一条改写规则在请求同质、预算紧或缺少可信反馈时最简单；不同问题的指代、句式与约束却可能需要不同处理，统一展开或简化还可能丢失关键语义。可把保持原意的几种改写作为有限arm，用本次query的语言特征选择arm，再根据可核验答案反馈更新选择器；更新的是外部选择policy，不是模型参数，更不是发现了幻觉的唯一内部机制。Original query、feature/rubric、arm prompt、selector state与reward身份都应随版本保存。<!-- source-family:SF-2026-ARXIV-2602-20332 -->

[有限QA实验](https://arxiv.org/html/2602.20332v1#S4)的收益来自“原题能答对、语义扰动后部分答错”的筛选人口，reference answer参与judge与词面reward；不能外推到无标签自然请求，也不能把canonical原题不改写更优解释成已证明训练污染。特征标注、改写、回答、judge和探索均有成本，proxy偏置或语义保持失败时回退原请求与固定基线；反馈不可独立核验时只冻结离线选出的policy，不能靠自己的答案继续认证自己的改写。

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

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

身份信息还需按任务语义分责，而不是一律删除或一律个性化。年龄、性别等显式线索有时是问题不可缺的条件，有时只是改变生成倾向的无关输入；一个受限分支先定位这些片段，再以“移除后是否丢失解题信息”的反事实问题提出 relevance 判断，仅对被判为无关的片段做 neutralization，生成语义核心答案。若需要面向不同读者调整表达，再在核心之后做 style-only 改写并核查内容保持，核查失败回退核心。这个顺序把任务必要信息与呈现偏好分开，却不赋予判断器删除事实的权限：相关性与内容保持都只是可能出错的模型 proposal，不确定时保留原条件或先澄清。<!-- source-family:SF-2026-ARXIV-2601-09141 -->

定位、反事实判定、改写和核查增加模型调用与维护成本；隐式身份线索也可能来自语境而非可识别词片段。有限英文任务与三个模型的实验中，作者既观察到关键身份误删、无关身份误留，也有任务准确率退步；500 条单任务人工核查的高一致率不构成公平或安全保证。身份仍可由 probe 读出，更不能据此认定生成偏差只来自某个阶段或唯一方向。上线需分开验收任务信息留存、答案质量与表达变化，失败时保留未经改写的请求和普通生成路径，而不把 neutral core 当作普遍无偏答案。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20512:start -->
repository guidance 从静态 README/AGENTS 文本变为 probe-and-refine：运行 coding agent，定位失败 step，再在固定 step budget 内修改 guidance 并跨模型验证；repo owner 持有发布/回滚，过拟合时保留旧指导。代价是 probe 成本和 benchmark leakage。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20512:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-26356:start -->
把模块间指令干扰作为可测试的组合边界，而非默认隔离；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-26356:end -->

## 本章在知识树中的位置

第 73 章交付 platform identity、policy 与 security。Prompt 是 Agent runtime 的第一个可变输入，但它只是一部分；下一章讨论 Context 如何在有限 token budget 中选择、排序并组装 Prompt、历史、检索结果和工具状态。

## 从机制演进到系统设计

Prompt 从临时文本演进成影响行为和权限边界的版本化输入 artifact。system instruction、task data、retrieved evidence 与 tool result必须保留来源和优先级，不能因为拼接到同一 Context 就获得同等 authority。

模板化和自动优化提高复用，却增加 injection、版本漂移和隐式 policy 变化。Prompt 只能提出行为约束，真实授权仍由 Tool/Workflow/Platform执行；高风险请求或来源冲突时，应缩小能力、请求澄清或拒绝，而不是让更长提示词代替 enforcement。

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

### 连续 Prompt 优化必须保留离散任务 Gate

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23180:start -->
固定离散 prompt 在任务稳定、人工维护成本可接受时最可解释；test-time 分支可以在 embedding space 中优化 prompt state，并用 demonstration likelihood 作为便宜的搜索 proxy。该 proxy 只负责提出候选，版本化 seed、步数和预算后，仍须由真实任务指标决定是否提交。

连续优化减少手工搜索，却可能利用 proxy 漏洞、产生不可解释的漂移，并让同一文本在模型升级后对应不同状态。现有结果只证明作者任务中的相关性和消融，不保证 likelihood 增益等于下游收益；两者不一致、预算失控或版本迁移失败时，应回退固定离散 prompt。arXiv:2605.23180v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23180:end -->

## Review notes

- `SF-2026-ARXIV-2604-08801`，Experimental：[exact-v1](https://arxiv.org/html/2604.08801v1) §3.2–3.3/Eq4–5、§4–5、§7。二元/iid response假设下分拆两类variance，选择用扣除噪声后的signal非不稳SNR；Qwen3-4B prompt generator，4B/1.7B冻结响应，4H100/3日预算，K×M大致固定。Ktop1过拟合，IFBench全量优于子集，不能将数学结果变成通用小数据规则；precision、完整服务并发/SLO未披露。本次必要原文与实际正文/相邻交接已由root独立复核通过，未复现实验。

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

### Daily integration evidence trace

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26356**：Primary `arXiv:2606.26356v1`；Method `https://arxiv.org/html/2606.26356v1 — §Instruction Bleed formulation; prompt-composed module interference`；Evaluation `https://arxiv.org/html/2606.26356v1 — §Cross-module interference experiments and mitigations`；未证明边界 `https://arxiv.org/html/2606.26356v1 — §Prompt/module families tested do not establish universal isolation or adversarial robustness`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-13449:start -->
- `SF-2026-ARXIV-2606-13449` — Daily `2026-06-12`；primary `arXiv:2606.13449v1`；Books review `books-review:SF-2026-ARXIV-2606-13449`。

  **已吸收的语义增量：** repository instruction 文件是可执行 control surface；评价必须区分规则存在、被读取、进入 context、被遵守与最终 outcome
<!-- daily-books-trace:SF-2026-ARXIV-2606-13449:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20512:start -->
- `SF-2026-ARXIV-2606-20512` — Daily `2026-06-19`；primary `arXiv:2606.20512v1`；Books review `books-review:SF-2026-ARXIV-2606-20512`。

  **已吸收的语义增量：** `Probe-and-Refine Tuning of Repository Guidance for Coding Agents` 路由到 `AGENT-PROMPT`：repository guidance 从静态 README/AGENTS 文本变为 probe-and-refine：运行 coding agent，定位失败 step，再在固定 step budget 内修改 guidance 并跨模型验证；repo owner 持有发布/回滚，过拟合时保留旧指导。代价是 probe 成本和 benchmark leakage。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20512:end -->

- `SF-2026-ARXIV-2601-09141` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09141v1) §3–6/Limitations 与 A 必要配置。5分针对身份语义相关性/核心与风格分责gap深入；不采唯一生成因果、公平安全保证或隐式身份全覆盖，误删/误留、质量反侧与调用成本相邻。root必要原源/owner写前通过，root实际两段/邻接及末注非作者POST通过，锁释放；未运行artifact或复现。

- `SF-2026-ARXIV-2602-20332` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20332v1) §3/4/5/A.1–3/Table7。2+1+2=5具体gap深入；仅feature→rewritearm选择与reference feedback边界，筛选人口/canonical非因果污染/额外调用/不授无标签在线自证近正文。root必要源/actual owner PRE通过并授两段+自身末注窄锁；作者actual正文/完整邻接/末注顺读，root非作者actual正文137–165/自身末注297 POST通过，锁释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2603-08806` — Daily `2026-03-12`补充Mar11自然日；[TDAD exact-v1](https://arxiv.org/html/2603.08806v1) §3–6/§8、§4.1–4.3/Table4/Appendix1必要操作定义。2+2+2=6，生成test oracle、hidden更新/激活mutation及成功编译人口分责的具体差额；18/24成功与失败账、未激活/排除人口和mock/singlemodel边界留证，生成/验证/mutation全费、冲突/预算失败与原Prompt退路近正文。必要Source/date/actual owner/逐字PRE经reviewer通过，root授指定单段及本人注窄锁；作者实际完整邻接及本人注顺读，root非writer实际正文/完整邻接及本人末注actualPOST通过，窄锁释放，不授DAY。未核artifact/复现。
