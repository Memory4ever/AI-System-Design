# SNEAK 唯一 owner 窄 PRE

Owner `PLATFORM-EVALUATION-SYSTEM`；路径 `books/part-06-ai-infrastructure/66-evaluation-system.md`。root已实际必要Source通过，真实`2+1+2=5`；因明确长期接口差额加深必要命题，不借通用原则重评分。尚未授写锁，未写Books。

实际比较Ch82 294–314共享先验/接收方interrupt，仅通信预算；Ch66 112–136 EvalSpec及privacy/measurement正文尚未承载同message两个信息状态的竞争测量。只Ch66 owner新一段，原GDPval与native artifact邻接不改。

## 当前完整局部

~~~~markdown
`intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明：

```text
EvalSpec =
  target behavior
  + eligible population
  + failure taxonomy
  + metrics and scorers
  + slice definitions
  + thresholds / comparison rules
  + uncertainty requirement
  + owner and review policy
```

当验收对象从文字答案变为文档、表格或幻灯片，EvalSpec 还应保存输入参考文件、输出 artifact 及其实际可见的渲染。只抽取正文在纯文本任务里仍是合理基线，却会丢失图表、版式和交付可用性；职业 rubric、匿名比较对象与 scorer 资格因而要和 artifact 一起冻结。内容准确性与呈现质量分别报告，不能让总体偏好胜率把其中一项的退步掩盖掉。[GDPval 的官方发布说明](https://openai.com/index/gdpval/)提供了这一受限评价分支：职业专家盲比异构交付物，自动 grader 仍是不能替代专家的实验服务。这增加渲染、审校与参考文件治理成本；one-shot 的交付成功也不代表完成真实工作流中的澄清、多稿迭代与监督，纯模型 API 费用不能代替这些端到端成本。无法稳定渲染或 rubric 尚未校准时，应保留人工检查和分项结果，而不是只发布一个总胜率。<!-- source-family:SF-2025-OPENAI-GDPVAL -->

~~~~

## 拟新完整局部（只新增一段）

~~~~markdown
`intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明：

```text
EvalSpec =
  target behavior
  + eligible population
  + failure taxonomy
  + metrics and scorers
  + slice definitions
  + thresholds / comparison rules
  + uncertainty requirement
  + owner and review policy
```

同一消息是否有用，还取决于接收者已知什么。一个受控的单轮测量让已知 secret 的合作者从候选消息中识别发送者的提示，同时让未知 secret 的观察者从候选词中猜测 secret；分别报告 utility 与 leakage，不能以少说信息同时压低两者就宣称更安全。[SNEAK 的具体接口](https://arxiv.org/html/2603.29846v1)按各自 chance baseline 归一、零截断，再以 utility×(1−leakage)表达取舍，但这些是有限候选下的行为概率，不是互信息、访问授权或不可推断的隐私保证。候选词更多会降低所测 leakage，decoy 更多会降低 utility，因此消息、两类已知信息、候选/decoy 构造与 evaluator 必须一并冻结；人类一致性也只校准这份受限代理。多候选生成、双角色判分和重复 evaluator 都计费，额外 test-time scaling 亦可能退步。人口或代理不匹配时，保留分项结果、真实威胁模型与独立人工/行为检查，不由低泄漏或乘积高分放行公开消息。<!-- source-family:SF-2026-ARXIV-2603-29846 -->

当验收对象从文字答案变为文档、表格或幻灯片，EvalSpec 还应保存输入参考文件、输出 artifact 及其实际可见的渲染。只抽取正文在纯文本任务里仍是合理基线，却会丢失图表、版式和交付可用性；职业 rubric、匿名比较对象与 scorer 资格因而要和 artifact 一起冻结。内容准确性与呈现质量分别报告，不能让总体偏好胜率把其中一项的退步掩盖掉。[GDPval 的官方发布说明](https://openai.com/index/gdpval/)提供了这一受限评价分支：职业专家盲比异构交付物，自动 grader 仍是不能替代专家的实验服务。这增加渲染、审校与参考文件治理成本；one-shot 的交付成功也不代表完成真实工作流中的澄清、多稿迭代与监督，纯模型 API 费用不能代替这些端到端成本。无法稳定渲染或 rubric 尚未校准时，应保留人工检查和分项结果，而不是只发布一个总胜率。<!-- source-family:SF-2025-OPENAI-GDPVAL -->

~~~~

## 本人静态注

保留当前末注：

~~~~markdown

- `SF-2026-ARXIV-2604-00265` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00265v1)§3.1–3.3/4/5.1–5.2，2+2+2=6，仅SR decision/FR conjunction与questioner/oracle/navigation人口分责；保target-last shortcut、description与SeenSynonym反侧、人类小样本和全部费用，不授oracle普适/3×70×bundle因果或物理安全，未核实现/复现。
~~~~

仅后追加：

~~~~markdown
- `SF-2026-ARXIV-2603-29846` — Daily `2026-04-02`补`04-01`；[SNEAK exact-v1](https://arxiv.org/html/2603.29846v1)必要§2–4/6，`2+1+2=5`，同message双信息角色与utility/leakage测量接口差额。保1394/117类别、10–12候选/5decoy/≤5词/单轮与3evaluators、有限human proxy、候选规模及额外scaling反退，归一/clip/乘积非MI或privacy/授权保证；全部生成/判分费用，未核artifact/复现。
~~~~

申请只新单段与本人静态注窄锁；保持全部原正文/其它family，root逐字PRE/授权前不写，实际写后由root nonwriter POST。

