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

若同一指令会被反复使用，也可以在发布前拟合一份参数侧近似，而不永远随请求重复传它：在代表性示例上分别取得有/无该context的attention激活差，用向量均值或线性最小二乘拟合可复用patch。[这一受限拟合分支](https://arxiv.org/pdf/2510.08734v1)必须区分两层：理想block里逐token重新构造的patch可匹配给定计算，跨token固定patch却只最小化所选组件/样本上的误差，不保证任意新context、整段输出或指令语义等价；激活span不足时，矩阵解也不唯一。原逐点乘法patch与后文加法写法尚有身份差额，不能按符号相似补成完整模型编辑recipe。指令、base/layer、paired激活、拟合/归一规则和超参应随artifact冻结，分别验原任务、未见输入和旧能力；有限算术/翻译结果仍有不稳定及低于原prompt的反侧。所有双路激活、拟合/择step、patch保存与独立生成回归均计费；分布、语义或摊销不足时，保原版本化prompt、显式context和成熟受控适配，不由无反传或可存权重宣称免费、永久知识或执行授权。

<!-- source-family:SF-2025-ARXIV-2510-08734 -->

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

角色字段、文字标签与最终位置还应分开测试，不能把其中一个的胜率当作抽象优先级的实现。[一个受控冲突研究](https://arxiv.org/html/2610.33201v1)固定指令文字，分别移动消息边界、任务行和system/developer或user载体；同一句operator文字换到真实高层role后，工具任务中的遵从反而可能下降，但chat template同时改变它与工具定义的相对位置，因此这不是纯role因果或后置策略更安全的证明。两条指令的胜负也不能唯一预测三条以上的冲突。应版本化实际序列化结果，并分别保留decided、拒绝/无行动和截断等人口；短英文合成指令、有限label与不同serving/sampling配置不授部署层级保证。对照与重复运行计费，变体收益不稳时保留已验布局和明确澄清，真正的优先级与副作用仍由模型外执行器强制，而不是继续叠加文字tiers。<!-- source-family:SF-2026-ARXIV-2610-33201 -->

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

示例数量也应作为待验预算，而不是越多越好的容量旋钮：在同一模型、标签协议与选择方法下，分别比较少量和更多示例的任务结果，并把宏平均与按类频率加权的指标分开。[受限需求分类对照](https://arxiv.org/html/2509.13196v1#S4)中，部分模型随示例增加而退步，另一些模型或指标仍改善，因此不能把某个最优数量、8B门槛或TF-IDF选择推广成通用规则。示例检索、数量搜索和更长输入都付费；转折点、标签或模型版本改变时，重新做独立回归，保留短固定示例与原选择器，不用更多上下文代替目标任务验收。
<!-- source-family:SF-2025-ARXIV-2509-13196 -->

固定示例数之后，还要决定几条示例是否提供互补信息，而不只分别像当前query。一条[受限主题覆盖分支](https://arxiv.org/html/2509.12451v1#S3)先为训练候选标主题并学习覆盖预测器，再用有标签候选上的zero-shot正确率形成模型知识proxy，逐次选择能补当前主题缺口的示例；这让标签制备、候选池和模型版本成为选择器身份。预测topic不是完整语义集合，正确率加权也不是内部知识真值，累计mean-embedding的增量不保证非负，知识为零时的归一化更不能默补成可靠规则。应以独立任务结果验收选择而非只看coverage分数，并计GPT标注、全池zero-shot、预测器训练、超参搜索与最终输入费用；有限分类对照中的检索阶段提速不代表全链更便宜。主题代理、模型版本或任务回归失配时，保留相似检索、随机/固定示例和较短prompt，不以覆盖更广替代真实答案验收。
<!-- source-family:SF-2025-ARXIV-2509-12451 -->

示例本题答对，还不等它适合教下一题。可以先让同一批候选轨迹分别作为其他题的示例，以后续解题效用选择可复用轨迹，而不只按原题reward排序。[CodeAdapt的受限分支](https://arxiv.org/html/2510.20909v1#S3)因此把单题正确、跨题teaching utility和最终任务质量分开；相同base但不同版本的生成器与learner不构成完全同模型对照，数学切片也存在原reward排序更好。效用依赖下游任务人口、示例顺序与consumer版本，不能固化为轨迹本身的永久质量。全候选/失败重试、跨题验证、工具和最终prompt都计费；少输出token不等整条选择更便宜。跨题收益或全费不稳时，保留原题reward、固定少量示例、相似检索与独立答案verifier，不由正确轨迹批准通用教学价值。

<!-- source-family:SF-2025-ARXIV-2510-20909 -->

示例还可能只监督单个skill，而目标要求未知的skill组合；此时多给单skill示例不保证能辨识组合接口，甚至会把学习规则推向错误组合。可将单步identity显式交给learner，分别检验单skill准确率与未见组合的结果。[受限skill-composition分析](https://arxiv.org/html/2510.22993v1)在有限假设类、特定分布可辨识与存在学习规则的条件下给出这种区别，不证明真实Transformer会执行该规则，也不把某个logarithmic示例关系搬成通用ICL定律。小模型对照仍受任务与训练人口限制，step提示还改变输入信息和长度；示例制备、结构标注、组合验证与完整推理均付费。组合identity不可得、语义或净收益不稳时，保留少量完整任务示例、原选择器与独立终局核验，不从单skill学会或更多examples批准任意组合能力。
<!-- source-family:SF-2025-ARXIV-2510-22993 -->

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

两套指南都进入了有效Context，也不表示它们的兼容规则会被联合执行。同任务skill中的单边worked example可能让模型整体选一种格式，连另一份不冲突的要求也丢掉；[SkillClash的有限对照](https://arxiv.org/html/2610.25064v1#S3)因而分别检查各源规则、必须择一的冲突与可共同达到的输出，而不只看任务完成。合并时应保每条原要求的去向，并验证示例确实满足联合规则；多写优先级、拼成一份文件或steer换赢家都不自动恢复联合遵从。手造可执行check的有限人口不认证真实skill语义，错冲突标签和错example反会扩大损伤。Merge、检查与逐源回归增加维护成本；共同解不明或原语义无法核验时，保留明确分阶段的独立指南与人工裁定，不因规则已加载或新稿更短就删除兼容义务。<!-- source-family:SF-2026-ARXIV-2610-25064 -->

<!-- source-family:SF-2026-ARXIV-2605-27784 -->

当多个 system、project、user 与 tool instruction 同时出现时，仅靠文本顺序和人工 review 解析 precedence，在规则少且冲突罕见时足够；规则增长后，同一组局部合理约束可能不存在共同可满足解，或只在某些输入上冲突。可执行的 prompt specification 可以先把候选约束编译成逻辑谓词，用 SAT/SMT 类检查发现 collision，生成最小 witness，并把选择的 resolution profile 绑定到部署版本。

形式检查拥有的是“抽取后约束是否一致”，不是自然语言意图真值。抽取错误、开放世界知识与概率行为仍需 regression、canary 和人工判断；过度形式化也会抬高维护成本。短 prompt 仍可直接审阅，只有多层 policy、重复继承与高代价冲突出现时，才值得用 executable spec 提前暴露不一致，并让 witness 成为可复现测试，而不是把求解器当作模型行为保证。

### 自动 Prompt 优化还要区分设计信号与采样噪声

反复测试候选 system prompt 时，reward 的波动同时来自 Prompt 对成功概率的真实改变和冻结 response model 的随机生成。若任务只返回二元正确性，同一 Prompt 的多次 response 可估计后一个噪声项；候选间总 variance 减去这项估计，才近似反映可优化的 Prompt 差异。将许多异质任务直接平均，可能互相抵消不同任务对 Prompt 的偏好，增加数据却削弱优化信号；这不是“少数据总更好”，也不等于 reward variance 越大越可学习。

一条受限分支先用足够重复采样估计这两类 variance，再选真实候选差异较大的小任务子集优化 prompt generator，并在未参与选择的任务上验收。额外采样、穷举子集和选择偏差都要计入预算；单题可过拟合，低噪声而容易的样本也会使 signal/noise 比值不稳定。[作者数学实验](https://arxiv.org/html/2604.08801v1)中小子集优于全量训练，但更同质的 instruction-following 任务仍以全量更好，跨模型迁移也只在受测 Qwen 家族内成立。任务偏好一致、数据少或二元反馈假设不成立时，人工 Prompt、全量 regression 与固定候选比较继续合理；选择器拥有的是实验预算，不是外部真值和安全权限。<!-- source-family:SF-2026-ARXIV-2604-08801 -->

Prompt控制的对象也可以是如何向用户补齐信息，而不只怎样组织最终回答：当完整需求由用户持有、Agent只收到模糊版本时，可以让它在短文本澄清和结构化表单之间选择，并用已完成交互的轨迹修订这份选择指令。[受限沟通对照](https://arxiv.org/html/2606.14314v1#S3)中，开放两条channel并不总优于单路，针对任务完成度选出的prompt不保证披露成本代理与persona合规同时改善。应把policy文本、工具catalog、表单渲染、用户可释放信息及模拟回应规则一起版本化，分别验任务结果、信息获取和成功条件下的偏好分母；模拟用户的敏感性标签不是实际隐私代价或墙钟。搜索中保存的验证集best数值单调，也不认证重跑质量或独立test单调。全部patch、失败rollout、重复选择、UI/VLM与执行费用都计入，规则、真实用户或净收益不可靠时保留单一澄清路径、原prompt和独立用户/任务验收，不让较高模拟完成分扩大信息索取或执行授权。
<!-- source-family:SF-2026-ARXIV-2606-14314 -->

决定是否澄清，还应把“请求缺少哪项决定性信息”与“给定当前解释后，对拟议动作有多自信”分开。一个动作在模型选定的解释下很确定，仍可能没有获得用户真实目标；反过来，动作自信低也未必能靠用户补充属性解决。[受限问询对照](https://arxiv.org/html/2606.19559v1#S3)先输出请求欠规格信号，再生成动作与动作confidence，把前者交给澄清路由，后者留作行为诊断；同一API call生成多个字段不等一次物理forward，自报数值也不是已校准的用户意图概率。应保存原请求、已知/缺失约束、实际提问与返回信息、动作及独立任务结果，分别验澄清触发与任务完成。人工删除信息后询问即揭完整原目标的协议，不能替代自然用户反馈；较高clarification F1仍可伴更低任务成功，阈值、额外解释和历史长度也改变质量及费用。解释、上下文、询问与执行回归均计费；信号或净收益失配时保明确缺字段规则、原已验澄清channel与人工确认，不让动作自信、更多字段或一个聚合分自动批准理解正确和执行授权。<!-- source-family:SF-2026-ARXIV-2606-19559 -->

数值输出的错误还可能来自整批分布收缩，而不只某条指令写错；可以先让模型同时比较多例预测与label，按系统性误差提出少量prompt修订，以独立dev选定版本，再把同一输入的多个数值rollout交给另训的小aggregator。一条[受限回归分支](https://arxiv.org/html/2508.21762v1#S3)将排序后的预测及简单统计量作为聚合输入，同时约束点误差与分布一致性；这改变两个不同对象，不能把head校准收益全归prompt或真实reasoning，也不由多次采样签发正确性概率。Label若只是人类感知偏好，输出也不取得事实真值；较低平方误差可能伴方差收缩，较高一致系数同样不保证逐题准确。Prompt搜索、dev选择、聚合器与其训练/目标应分别版本化，并在独立人口核最终误差、分布和失败切片；全部反思/训练/多rollout都计费，三次可并行也非一次调用。分布、label或净费用失配时，保留人工固定prompt、单次预测/简单平均及真实任务校验，不因更连续的数字批准作为可信reward、业务决策或普遍更优模型。
<!-- source-family:SF-2025-ARXIV-2508-21762 -->

固定一条改写规则在请求同质、预算紧或缺少可信反馈时最简单；不同问题的指代、句式与约束却可能需要不同处理，统一展开或简化还可能丢失关键语义。可把保持原意的几种改写作为有限arm，用本次query的语言特征选择arm，再根据可核验答案反馈更新选择器；更新的是外部选择policy，不是模型参数，更不是发现了幻觉的唯一内部机制。Original query、feature/rubric、arm prompt、selector state与reward身份都应随版本保存。<!-- source-family:SF-2026-ARXIV-2602-20332 -->

[有限QA实验](https://arxiv.org/html/2602.20332v1#S4)的收益来自“原题能答对、语义扰动后部分答错”的筛选人口，reference answer参与judge与词面reward；不能外推到无标签自然请求，也不能把canonical原题不改写更优解释成已证明训练污染。特征标注、改写、回答、judge和探索均有成本，proxy偏置或语义保持失败时回退原请求与固定基线；反馈不可独立核验时只冻结离线选出的policy，不能靠自己的答案继续认证自己的改写。

局部改写还可同时选择“改哪一段”与“用什么操作”，而不把整份prompt每次重新生成。先固定分区边界和允许的编辑operator，以联合候选在任务反馈上积累经验，保留未被选中的有效片段；[受限分区编辑分支](https://arxiv.org/html/2510.12246v1)由此缩小单次变更面，却不证明分区之间独立，未编辑的文字也可能因上下文变化而改变作用。分区revision、operator/改写器、选择历史、实际diff和评价人口应共同保存，分别核局部修改、原规则保持和完整任务。原更新式/概率与算法交接未闭时，不补成可靠bandit或RL配方，更不以有限接口保留推导全局下降。全部候选、失败试验、长prompt前向、反馈与独立回归均付费；交互效应、语义保持或净质量失配时，保人工小改、原已验prompt与全量回归，不由少改文字或更高内部score批准规则正确和自动发布。
<!-- source-family:SF-2025-ARXIV-2510-12246 -->

跨语言改写还应把中间处理语言与原题数量规则分开，而不只要求模型“用英语想”：保留源题，在较熟悉语言的中间说明中列出实体、数量、单位与关系，再显式核源语言中折扣、计量和指代的含义，最后回到请求语言回答。[受限结构提示分支](https://arxiv.org/html/2510.02648v1)提供这种消费顺序，但抽取与补充仍由模型自身生成，不是外部知识或真实内部推理；英文pivot也不保证适合每份checkpoint。应绑定原题、源/中间/输出语言、各派生产物与完整prompt，分别验关系保真和最终答案，不把结构清楚、解释一致或跨语言均分当语义等价。译题可能遗漏native用法，局部语言与模型也会反退；全部中间token、调用/翻译、模板选择与独立语义回归都付费，较短decode或无需训练不签零开销。语言知识、关系抽取或净收益不可靠时，保留原语言题与直接/普通CoT路径，必要时由可信词典、真实标注或人工澄清补证，不让自产结构覆盖原文。<!-- source-family:SF-2025-ARXIV-2510-02648 -->

当关键判断依赖尚未记录的专家知识时，检索已有文档并不能补齐这份输入；可先让模型提出因素与层次，再由专家确认每个因素的有序取值、方向及组合判断，把得到的规则作为后续Prompt的条件。一条[受限知识制备分支](https://arxiv.org/pdf/2509.10818v1)在专家确认单调性后，将已接受组合的结论向更高组合传播、已拒绝组合向更低组合传播，避免重复询问已被这些前提蕴含的答案；这不允许模型擅自用多数阈值替代专家，也不允许概括题丢掉原叶题。因素树只是待学习的specification，亲答、按已确认前提推得及仍未知的规则应分别保留；专家模型反映其决策偏好，不自动取得外部事实或执行权限。原案例未验证普遍询问量界、幻觉减少或完整任务收益，因素生成、问答/重问、人审、规则制备和独立任务回归均付费。单调性不成立、因素遗漏或专家回答冲突时，回到原叶题逐项澄清、固定人工规则与独立结果检查，不让省下的询问或更完整的树自行批准最终判断。

<!-- source-family:SF-2025-ARXIV-2509-10818 -->

规则集也可从带标签的局部对照学习，而不是仅汇总人工追加的约束。先按input语义分cluster，再用output分布相对全局的差异调整局部样本，避免每个cluster只有一种结果；A/B对照提出IF/THEN规则，按相近THEN合并IF并保留例外，后续错误样本与规则关联的anchor共同约束最小改写。这里cluster定义候选的训练支持，规则ID只是模型报告的参与线索，不是因果归因；anchor通过也不认证所有旧语义保持，最终部署仍需独立regression。<!-- source-family:SF-2026-ARXIV-2604-09418 -->

[AIR的五任务对照](https://arxiv.org/html/2604.09418v1)支持有限显式规则适配，但不授通用赢家：source-specific QA中42.08不优于原prompt、低于KNN81.67，结构化提取亦有反退。聚类、全部base/reflection调用、合并/修订、dev选择与独立test共同计费，各角色token账不能代替总美元或latency；持续增量更新尚未实验。噪标、冲突合并、anchor覆盖或质量回归时，保留人工短prompt、原规则/例子检索或参数适配，不让可读规则和自报ID自行批准删除guard、安全或上线。

持久instruction还可由逐turn反馈与旧prompt/反馈replay共同改写，而不把每次建议直接变成当前答案：独立feedbacker读取交互与可用目标信息，rewriter提出少量新prompt，再用validation选择下一版本。[Prompt reinforcing的受限分支](https://arxiv.org/html/2510.05921v1#S3)保存的是文本经验与版本选择，TD-style文字并不提供已校准的数值value、真实TD-error或收敛保证；自报满意/预期成功与API字符串也不代真实目标完成和外部effect。Replay可保旧义务，也可延续错误归因/陈旧接口，须绑定原用户目标的可见权限、反馈/rewriter模型、历史instruction和选择人口，另验新旧任务。全部先前交互/模拟用户、反馈/改写、replay驻留、候选validation搜索与独立回归均费，只部署最终prompt不等全生命周期免费。来源、选后偏差或真实质量不稳时，冻结已验instruction、保原prompt/history和有限人工/规则核验，不由更好文字或局部均分批准自主持续改指令。

<!-- source-family:SF-2025-ARXIV-2510-05921 -->

多模块工作流只有最终标签时，还可以把反馈先写成各节点的目标输出，再改各自prompt，而不把同一失败文字广播给所有模块。一条[有限单隐藏层分支](https://arxiv.org/html/2606.14155v1#S4)缓存实际输入输出，从下游目标反推“上游应提供什么”，以原输出与这份target的差异约束局部claims编辑。逆向target是优化器提案，不是已识别的真实责任或可实现中间答案；多个后继可能要求互不兼容的target，原单聚合器结构避开的冲突不能当作任意DAG已解。缩小可编辑条数也不保证语义更新趋零、全局下降或最优，仍须重新执行完整workflow，在独立人口验最终任务和各节点接口。全部前向、逆向target生成、prompt改写、选择及部署多模块调用均付费；调用少或输出短不能跨输入/输出token账认证净省费。目标不可信、局部修订互相破坏或预算不合时，保留固定prompt、已验局部/全局reflection与人工责任划分，不把target propagation命名为真实梯度或自动发布证书。
<!-- source-family:SF-2026-ARXIV-2606-14155 -->

搜索产物也可以是一份供实例选择的目录，而不总交付同一条全局 prompt：先以离线实例反馈制备若干 anchors，再用 instance–context 的相对评分训练选择器，按其潜在方向挑已有 seed、由模型反思改写并重新实测，逐步扩展离散 context catalog；线上只让冻结 router 对目录评分、取一条给 solver。[受限目录共演化](https://arxiv.org/html/2605.15721v1)分开了候选制备、反馈与当前选择，不是连续 embedding 直接解码文本，也不取得线上最优 context 的真值。稀疏观测中如何确定所有候选失败、未观测值与新增反馈身份仍须闭合；理论的条件概率界/全局方法上限不足以批准最优目录或单调收益。相同目录的选择器对照支持局部作用，但更多 anchors 可退步，更密采样的 test 收益可饱和，dev 与 test 的偏好也不同。全部 LLM 改写/GT评价、router 训练与网格、线上 encoder 和全目录打分均计费，不用较少 online tokens 抹掉制备预算。目录、实例分布或支持质量失配时，保留原 query、短人工 prompt 或已验固定/检索选择，重新按独立任务结果回归，不让相对分数替 solver 批准正确性或执行权限。<!-- source-family:SF-2026-ARXIV-2605-15721 -->

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

即使规则已带版本，主动收到一次Add/Edit/Delete也不等于已有足够反馈来安全改写整套prompt。可把旧值留在不对solver展示的shadow评价中，同时检查当前active set、非目标回归和删除后的默认行为，避免均值掩盖旧规范回弹；shadow不是要求模型继续服从已删除规则。[受限delta-only实验](https://arxiv.org/html/2606.06698v1)中，现有self-play适配未明显胜过每题直接附完整active set，内部fitness还可能伴随陈旧约束、拒答或格式污染；把全约束也交给适配能恢复大部差额，却新增显著token成本。因此不能把协议结果升级为全部主动适配不可能，也不由更多self-play批准删guard；没有真实反馈、约束枚举或净收益时，保留短人工prompt、明确当前规则与独立regression，制备/测试及所有适配调用一并计费。<!-- source-family:SF-2026-ARXIV-2606-06698 -->

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

搜索对象也可从一份prompt变成有依赖的skill bundle：任务solver先产生失败trace和pass/cost，另一个消费者提出删除、替换、重排或重写的child，并更新下一轮使用的optimizer提示。每个child仍需重新执行原任务；可按pass与调用cost保存非支配archive，再以parent-relative质量guard拒绝明显回退。这分别拥有候选生成、局部继承约束和最终operating-point选择；relative guard不是固定绝对发布门，optimizer提示也不得在同一反馈上自行提高verifier权限。<!-- source-family:SF-2026-ARXIV-2604-09297 -->

[SkillMOO的有限三任务对照](https://arxiv.org/html/2604.09297v1)支持这一bundle-search分支，runtime只是末级tie-break，不是另一个独立优化目标。最大原bundle、单模型、population1/五代及同扩展test反馈不证明held-out任务泛化；删除/替换频率只是观察，不能独归某类编辑因果。原bundle与空skill在不同质量/费用点仍可合理，共同计入全部solver、optimizer、test扩展与搜索花费，不能用HV相对小分母提升替净收益或break-even。新任务、verifier或依赖身份变化、质量退步或搜索摊销不成立时，保留已核bundle/人工改写与独立holdout，不从Pareto archive批准部署。

对一份反复修改的procedural skill，还可以把编辑强度和负反馈显式变成优化状态：失败/成功minibatches先各提局部patch，再合并冲突并按本轮edit budget截断；候选只有在固定selection split上严格胜过当前版本才接纳，失败patch连同分数下降留在epoch内rejected buffer供后续反思。跨epoch的slow guidance写入局部patch不能覆盖的保护区，optimizer-side meta经验只帮助提出编辑，不随部署skill输出。保护区保持的是编辑责任边界，不是不可错的知识或安全证明。

[SkillOpt的有限对照](https://arxiv.org/html/2605.23904v1#S3)支持这条有界文本优化分支，但反复用于筛选的holdout不是每次新独立检验，严格加分也不保证全局泛化或部署单调改善。Rollouts、optimizer、被拒绝候选的评价与更长skill的在线Context都计费；没有新增optimizer calls不等于零部署成本。任务、harness、judge或依赖改变后须重验，反馈不可靠、规则冲突或净预算不值时，保留人工短skill、旧已验版本与独立最终测试，不让更高selection score获得事实、工具或发布授权。<!-- source-family:SF-2026-ARXIV-2605-23904 -->

相同 skill 的表达也应随实际消费者验收，而不按模型大小预设“更短”或“更详细”：在 task model 冻结时，可把其能力描述与失败轨迹交给 teacher，先搜索通用指南，再固定它们搜索各任务类型的规则；另用这些高分改写训练小 rewriter，将后续适配从环境搜索摊销成一次文本生成。[MASA 的受限对照](https://arxiv.org/html/2605.30723v1)支持 model-conditioned 文本分支，却不使 model card 成为能力真值，环境状态未变化也只是停滞代理。No-skill 与不同粒度在部分模型/任务可更好，有限跨环境迁移不授任意新消费者可直接复用；搜索结果更非全局最优。全部探索/弃选、teacher 与 card、检索/更长 Context、rewriter 训练和生成均计费，较少交互步不证明净省时。消费者、harness 或反馈改变时，保留无 skill/原已验版本与独立任务回归，不让改写器取得事实、工具或发布授权。<!-- source-family:SF-2026-ARXIV-2605-30723 -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

身份信息还需按任务语义分责，而不是一律删除或一律个性化。年龄、性别等显式线索有时是问题不可缺的条件，有时只是改变生成倾向的无关输入；一个受限分支先定位这些片段，再以“移除后是否丢失解题信息”的反事实问题提出 relevance 判断，仅对被判为无关的片段做 neutralization，生成语义核心答案。若需要面向不同读者调整表达，再在核心之后做 style-only 改写并核查内容保持，核查失败回退核心。这个顺序把任务必要信息与呈现偏好分开，却不赋予判断器删除事实的权限：相关性与内容保持都只是可能出错的模型 proposal，不确定时保留原条件或先澄清。<!-- source-family:SF-2026-ARXIV-2601-09141 -->

定位、反事实判定、改写和核查增加模型调用与维护成本；隐式身份线索也可能来自语境而非可识别词片段。有限英文任务与三个模型的实验中，作者既观察到关键身份误删、无关身份误留，也有任务准确率退步；500 条单任务人工核查的高一致率不构成公平或安全保证。身份仍可由 probe 读出，更不能据此认定生成偏差只来自某个阶段或唯一方向。上线需分开验收任务信息留存、答案质量与表达变化，失败时保留未经改写的请求和普通生成路径，而不把 neutral core 当作普遍无偏答案。

表达偏好还可以从一段角色描述变成独立、可复用的结构化输入：让一个teacher按约定维度为persona提出数值profile，再把原persona或其聚合profile交给冻结的生成模型。这分开了偏好表示的生产者与文本消费者，不更新消费者参数，也不使0–100的标签成为真实心理特征或可校准概率。[PILOT的受限对照](https://arxiv.org/html/2509.15447v1)中，同一数值接口能改变风格聚类，但profile通常由一组persona平均而来，组内个体差异可能被抹平；结构化提示还额外要求分析/解释，因此不能把全部变化归因于schema本身。内容与persona分组纯度应分开测，较短回复或更高词汇比率不证明更丰富的n-gram，人评未显著也不表示质量等价。Teacher、维度定义、聚合成员与规则、生成器和实际提示应共同版本化，制备/聚合、额外分析、全部生成与独立内容/个体偏好回归都付费；偏好失真、事实变化或预算不值时，保留原persona、简单style-only提示或无个性化路径，不让画像替任务信息或权限签字。

<!-- source-family:SF-2025-ARXIV-2509-15447 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20512:start -->
repository guidance 从静态 README/AGENTS 文本变为 probe-and-refine：运行 coding agent，定位失败 step，再在固定 step budget 内修改 guidance 并跨模型验证；repo owner 持有发布/回滚，过拟合时保留旧指导。代价是 probe 成本和 benchmark leakage。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20512:end -->

把彼此独立的任务合进同一 prompt，也不是只节省重复说明的无害 batching：模型可能在 context 远未填满时缩短每项推理，而单独可答对的长推理任务可能更易退化。这里应同时测单题与组合后的逐题质量、实际推理/答案 tokens、截断和解析，不能用容量够或孤立准确率预测组合可靠性。[有限同类任务对照](https://arxiv.org/html/2610.27190v1#S3)支持按 model-specific fragility 选择小或大 composition，而非固定打包数；但 tag 归因与强制截断仍有测量差异，预算缩短的成因未明，也未实测混域依赖任务或长程 Agent。目标任务反复预采样才得到的 fragility 不是线上免费信息，held-out 预测器的节约也更小且局部退步；probe、表示/拟合与全部生成均计费，少 output tokens 不等低总时延。估计不稳、任务互依或质量回归时，保留逐题调用、较小语义批和独立验收，不把它与 GPU 请求 batch 合并，亦不由平均预算门签发逐题正确。<!-- source-family:SF-2026-ARXIV-2610-27190 -->

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

- `SF-2026-ARXIV-2606-19559`，Jun20补Jun19；消费sole§44 exact-v1§3–8/A1.1/A3.1必要，2+2+2=6，作者actualCh74优化噪声/澄清channel完整前肩及数值prompt后肩、Ch73/75交接已读，仅request欠规格-v-actionconfidence两个消费者差额深入。保baseline同问询权限、人工50%删除/完整goal揭露、F1-v-SR反侧/单run与全费，Eq16geommean不采指数坍塌通律；未核实现/复现，sole§51完整PRE通过，SAVE/selfread/actualPOST仅本日实际层。

- `SF-2026-ARXIV-2610-33201` — Daily2026-10-28；exact-v1 §3/4.3–4.6/Limits必要，2+2+2=6。只采serialized role/label/position及多路冲突不能从二路胜负外推；保1080合成场景/五seat、1.887m回复非独立样本、decided人口、工具定义相对位置与thinking/sampler/serving混杂，不授后置安全或角色层级无效。唯一reader必要/实际owner/PRE通过；未运行实现，实际SAVE/POST以本日ARXIV_AGENT及REVIEW为准。

- `SF-2025-ARXIV-2510-05921` — Cicero，Daily2025-10-09补Oct08BJT；[Prompt reinforcing exact-v1](https://arxiv.org/html/2510.05921v1)R297唯一首次必要§3–6/Eq1–5/T1–3/伦理/复现/A–B与Ccaption一次采用，2+2+2=6，仅逐turn文本反馈/replay→持久instruction consumer深入。保TD非数值value、goal权限/10interactions非全epoch、.477/.333与54.2%聚合未合、选参/原能力及全费，不采收敛/医疗效用/真实goal完成或免费。未核图片prompt/曲线像素/代码或prompt优化复现；PRE/SAVE/selfread/solePOST仅本日canonical，不以本注预签。

- `SF-2025-ARXIV-2510-02648` — Meitner，Daily2025-10-07补Oct06；[SoT exact-v1](https://arxiv.org/html/2510.02648v1)§3/式1–4/§4/T1–6/Limitations及A1/A2必要，2+1+2=5，pivot/源语言关系规则与派生输入差额深入。保抽取非真值/内部无关性、语言反退/译题支持、计时.1与四格均值张力及全费，不采全语言无损、英语普适或零成本。未核像素/全附表/代码/复现；PRE/SAVE/POST仅本日canonical真实层。

- `SF-2026-ARXIV-2606-14314` — Daily2026-06-16补Jun15；[exact-v1](https://arxiv.org/html/2606.14314v1)§3–6/Alg1/T1–4/A/D/E/G/J/Limitations必要，2+1+2=5，monotonic/评价权限受影响深入。只沟通channel-prompt版本与三目标分责，保重复val非独立泛化、persona成功条件分母/Cost代理、SWEpatchF1非执行正确与真实反退，不授硬预算可行/真实个性或UI部署；未核像素/code/复现。作者唯一首备，reader§113必要/actualowner/整体PRE修精度句通过且直接窄授，已真实SAVE且reader§114唯一实际POST通过，指定窄位释放，不预DAY。

- `SF-2026-ARXIV-2606-14155` — Daily2026-06-16补Jun15；[exact-v1](https://arxiv.org/html/2606.14155v1)§3–7/Alg1–4/T1–3与A.1–4受影响证明，2+2+2=6，逆向localtarget与prompt更新/实际credit分责深入。保单hiddenlayer/多后继冲突、λ未求解/缩entry非语义稳定、Eq17与globalrate未获支持、预算/architecture混杂和全费，不采任意DAG/真实gradient/最优收敛；未核图像素/实现/API复现。作者唯一首备，reader§84必要/actualowner/整体PRE通过直接窄授，已真实SAVE，reader§87唯一实际POST通过、窄位释放；本注仅行政同步既成，不预DAY。

- `SF-2026-ARXIV-2606-06698` — Daily2026-06-09补Jun08；[exact-v1](https://arxiv.org/html/2606.06698v1) §2–4/Limitations，2+2+2=6，主动delta-only与shadow旧规范评价具体gap深入。保prompt-only/四backbone/72条件、full-set适配恢复但未胜baseline及2.8×token直接反侧，不授主动适配不可能或生产发生率；未核实现/复现。root SUP_REVIEW §9/10实际准入/date/必要/owner与literal通过，授本单段+注；作者已真实保存并完整自读新增、直接完整两侧及自身H2注；root SUP_REVIEW §12唯一非writer实际POST已通过，指定窄位已释放，不预DAY。

- `SF-2025-ARXIV-2509-15447` — Singer，Daily2025-09-23补Sep22；PILOT exact-v1方法/实验/T1/Discussion/Limitations及A/B/C必要A239→Sartre R163通过，原2+1+2=5，仅teacher profile producer/冻结生成consumer与聚合输入身份差额深入。保25组/250合成persona、额外分析混杂、内容纯度非persona纯度、n-gram反侧、588/567与检验口径差异、未显著非等价及全费；不授真实人格/公平或结构独占因果。未核像素、实现或复现。A259原三项经Sartre R178 purePRE/root本轮fresh独立新窄授，原技术段/standalone/本人注已按批准窄位真实保存，A275已实际完整自读/限定检查，Sartre R189本项soleactualPOST通过，I30生效/指定窄位释放；本尾仅同步既成行政态，不第三Source/PRE/POST或授DAY。

- `SF-2025-ARXIV-2509-12451` — Socrates，Daily2025-09-18补Sep17；[exact-v1](https://arxiv.org/html/2509.12451v1)§3–4/式2–8/T1–6/Limitations/A/B必要，2+1+2=5，proxy/归一化反侧深入，reader53必要Source通过。仅互补topic选择与有标签正确率知识proxy；保非集合union/非单调、零分母、prior不等accuracy及式4非完整softBCE，六任务/三seed/API5shot人口分开，37x只retrieval、不授全费用/普遍优势。未核代码/复现；原三项按root独立fresh窄授真实保存并完整自读，Helmholtz71唯一actual完整新增/完整两侧及binding/本人注POST已通过，I11生效且指定位已释放；本尾仅同步既成行政事实，不第三正文/Source/PRE/POST或授DAY。

- `SF-2025-ARXIV-2509-13196` — Daily2025-09-18补Sep17；[exact-v1](https://arxiv.org/html/2509.13196v1)§III–V/TablesI–IV/Figs5–8正文与图注必要，2+1+2=5。仅示例数量/选择方法/模型与label协议相关的非单调和metric分验；保80/20搜索与10fold排名不同人口、DeepSeek/Mistral反例、重标注混杂及全费，不采8B阈值/架构因果、TF-IDF普遍最优或1%通用优势；API snapshot/解码/seed与端到端费用未披露，未核图像全部点/实现或复现。

- `SF-2026-ARXIV-2610-25064` — Daily2026-10-21窗Oct20；exact-v1必要域与采用边界见本日AUTHOR R-A39，reader R194已核必要Source、实际owner及完整PRE。root按批准原单段保存并自读完整直接两侧；reader R197已一次非writer actualPOST通过并生效释放，不预签日级或实现/复现。

- `SF-2026-ARXIV-2610-27190` — Daily2026-10-22，[Composition Fragility exact-v1](https://arxiv.org/html/2610.27190v1)§3–5与必要协议/反侧，2+1+2=5。只同dataset独立任务prompt composition与每task预算诊断，不授预算缩短唯一因果、混域/依赖任务或长程Agent。保tag遗漏、forced截断非完美因果、目标预采样/预测器反侧和全部费，不采用headline净节约。作者E15/reader R60条件Source/具体owner/PRE通过，actualPOST另见本日REVIEW；未核实现或复现。

- `SF-2026-ARXIV-2605-23904` — Daily2026-05-26补May25；[SkillOpt exact-v1](https://arxiv.org/html/2605.23904v1) §3–4/B/C，2+2+2=6，有界patch/rejectedbuffer/protectedslow/meta具体差额深入。严格selection gate非独立反复检验或部署安全，保新harness/更长skill、训练/弃选/评价全费；未核完整prompt/artifact/复现。指定reader必要Source/actualowner/逐字PRE通过，root授本两段及本人注；指定reader已实际重读保存正文、完整直接两侧与本人注，唯一非writer POST通过，窄位生效释放，不授DAY。

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

- `SF-2026-ARXIV-2604-09297` — Apr14补Apr13，exact-v1§2–5/T1–4，2+1+2=5具体bundle支持域差额深入；仅failuretrace-driven bundle edits/optimizer prompt共同状态、pass-cost archive与parent−.05 guard分责，不授三objective/heldout泛化/净省费。保GLM5/三最大bundle/GPT5.4扩40test/pop1/5gen/10run及search2.2676/1.8611/1.7641、no-skill成本反侧与编辑非唯一因果；reader必要Source/date有效，reader finalPRE实际通过；supp_apr14_reader实际正文/完整上下邻及本人末注POST通过，作者已实读回，未核实现/复现。

- `SF-2026-ARXIV-2604-09418` — Apr14补Apr13，exact-v1§3.1–3.3/§4–6，2+1+2=5具体labelled-contrast→rule修订支持域差额深入；K5 inputcluster/output分布balance、THEN/IF/exception与mistake/anchor分责，不采ruleID因果/anchor语义certificate或未测online更新。保test64/30/78/60/60异metric、dev8/5/12/60/60、GPT4.1mini/GPT5reflection/QA5.1judge、AIR95.31<GEPA96.88/QA42.08<81.67/IE35.90<36.54、PUPA8steps5无改善b3、完整tokens与美元/runtime/hardware/seedsCI ND。reader必要Source/date有效；reader finalPRE实际通过；supp_apr14_reader实际正文/完整上下邻及本人末注POST通过，作者已实读回，未核实现/复现。

- `SF-2025-ARXIV-2508-21762` — Godel，Daily2025-09-02补Sep01；[exact-v1](https://arxiv.org/html/2508.21762v1)2.1–2.4/3/4.3–4.4/T1/6/C必要，2+1+2=5。仅batch-error prompt与独立数值aggregator两consumer；保标签构造/感知非truth、NMSE/CCC/逐题分责、局部反退/不同budget与全费，不采内部因果/完整rewardrecipe/通用65%。独立验收/退路为项目推导，未看全prompts/像素/核实现或复现；Newton63实际必要Source/具体owner/本逐字PRE通过，root已协调本指定单段/独立marker/本人注；已按稿实际保存，Newton67一次真实完整新增/完整直接两侧/本人注POST通过，本指定窄位生效释放；不预整日DAY。

- `SF-2026-ARXIV-2605-15721` — Daily2026-05-19补May18；exact-v1 §2–4/T1–2/A Al1–2/B/C/E/F必要域reader R134唯一原证、作者实际完整消费，2+2+2=6。只离线catalog/线上router接口；保ξn/ε界错误简写、upperbound非global天花板、allfail观测契约/recipe未闭、K反退与density收益饱和及全部GT/API/router费，不授最优/显著支配、实现或复现。

- `SF-2026-ARXIV-2605-30723` — 作者jun02_supp_author_b；Daily2026-06-02补Jun01；[MASA exact-v1](https://arxiv.org/html/2605.30723v1)必要域见本日B3，原6。只consumer-conditioned文本资产/搜索蒸馏分责；保card非能力真值/NoSkill反侧/完整费用与原版本退路；未核实现/复现。jun02_supp_author_a A9.1必要Source/完整owner邻接/原B3 PRE通过并本轮新授，作者原单段/唯一marker/本人注保存，jun02_supp_author_a A11唯一实际非writer POST通过生效释放，不预DAY。
- `SF-2025-ARXIV-2509-10818` — Bernoulli，Daily2025-09-17补Sep16；exact-PDF-v1必要pp3–5/7–24、Alg1–4/T1–2，正式2+1+2=5/唯一AGENT-PROMPT Ch74条件知识制备小gap，Lovelace141必要Source/owner通过。只采用因素/ordinal及已确认单调前提的专家问答供给，不授因果发现、通用询问量或幻觉减少；保specification不等已学model、专家偏好非事实/授权及全部制备/回归费，未核全图/旧证明/代码或复现。Lovelace143原三项纯PRE通过，root本轮fresh仅授本三项窄位；现按原稿真实保存并完整自读新增/全部直接两侧/本人注，Lovelace148唯一实际完整非writer POST通过，I24生效/窄位释放，不授整日完成。

- `SF-2025-ARXIV-2510-08734` — Daily2025-10-14补Oct13；Planck R52独占exact-v1 PDFp1–10/13–19及renderp3–5首次必要，writer只p3–5原式/OLS关键核，2+1+3=6，逐点exact与固定样本拟合的prompt→参数边界gap深入。保非零activation/inverse条件、乘加patch身份差额、翻译低原prompt/择step和全费；不采固定patch全输入精确/生产。未核代码/复现，整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

- `SF-2025-ARXIV-2510-12246` — Herschel，Daily2025-10-16补Oct15；消费Cicero R8与本日既成最低/独核§9、meta-prompt/operator/ablation实际层，2+1+2=5，仅section×operator联合候选/实际diff差额深入。保Q/prob/loss/算法引用冲突，未采完整MSGD-RL recipe/收敛/普遍因果，全部失败/feedback与回归费保留。未第二Methods/代码/复现；整体PRE/真实SAVE/fullselfread/solePOST仅本日canonical实际层。

- `SF-2025-ARXIV-2510-20909`：Daily2025-10-28补Oct27；exact-v1§3–4/限制必要、2+1+2=5，R14受限Evidence通过。仅跨题示例utility与本题reward分责，保跨版本/AIME反侧与全部候选验证费，不采普遍省时或正确教学保证；未核实现/复现。完整PRE/SAVE/全自读/sole actualPOST按同日canonical实际层，不预签。

- `SF-2025-ARXIV-2510-22993`：Daily2025-10-29补窗；复用sole已成exact-v1必要支持/反侧，writer已实际读具体结论与owner差额，未核代码或复现。按R40实际gap补单skill监督与组合接口可辨识性，不重复已有示例数量/主题互补/teaching utility；理论权限不外推真实模型。
