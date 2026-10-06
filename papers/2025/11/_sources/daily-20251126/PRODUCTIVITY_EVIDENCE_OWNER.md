# Nov26 Productivity 单项必要证据与 owner 对读

作者 Aristotle；当前只审本日UTC[2025-11-25 01Z,2025-11-26 01Z)。此包可单项独立复核，不等待14来源全部结束；准入/日期及Books尚待root，不自授通过。

## 日期与身份

[官方文章](https://www.anthropic.com/research/estimating-productivity-gains)本日native GET保存productivity.html及receipt，published_time与JSON-LD datePublished均`2025-11-25T11:05:00.000Z`，正文Nov25。Research首页本日GET/真实JSON Flight解码的172个去重dated records中，目标相邻为Nov24 15:10Z prompt-injection-defenses、Nov25 11:05Z estimating-productivity-gains、Dec1 00Z smart-contracts；见anthropic-window-metadata.json。这是第三个官方发布字段支持Nov25，不是由别日报覆盖继承。

Bibtex仍`date=2025-11-05`，不删除、不把它自动当first-public；作者判断其citation日期与独立CMS/文章发布字段冲突，优先采用具名官方发布事件，但需root独立核此权限判断。当前dateModified为2026-08-25，本文不保证历史逐字冻结，也不把修改日期当当窗新事件。无当前可见官方撤回/纠错说明；没有为证明不存在遍历历史。

## 准入命题与必要证据

原有“稳定模型估计可代表任务工时”的判断，受到作者局部外部对照与估计范围限制的反证；拟采用的选择是分开instrument稳定、外部校准和任务完成成本。2+1+2=5标准审阅，不给宏观经济外推贡献分。

原源实际核心、Validation、Limitations已读，raw-core-and-boundaries1.json、raw-screening-core2.json、raw-first-calibration-core3.json保留工具原响应，native HTML保留完整正文。不是只摘要改写：

- 100k Claude.ai conversations是模型对有/无AI任务时间的估计，不是100k实测工时。1800份同意用于研究的对话上，多prompt估计自相关r=.89～.93只能说明仪器稳定。
- 外部1000 JIRA tickets上，模型只取title/description；human拥有codebase背景。human Spearman .50/log-Pearson .67，Sonnet4.5分别.44/.46；加10examples后分别.39/.48。因此不能把few-shot说成全面更准，也不是同信息条件的human-vs-model能力排名。
- 短/长工时估计被压缩，且验证、迭代、多session及chat外工作不完整可见。chat内估算省时不能取得端到端实测收益权限。自然人口、不同岗位和长期产出不能由该ticket对照保证。

原文的80%省时及1.8%宏观增速不采用为实测系统结果。未运行代码/重算数据/复现实验；不扩宏观模型、所有附件或RCT队列。这里的收益只是发现proxy授权边界，不承诺提出一个已验证的更优工时估计器。

## Books 实际对读

本次实际读ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、最新checkpoint及以下owner/邻接。Books仍root独占，未写共享书稿。

Owner `PLATFORM-EVALUATION-SYSTEM`：[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L50～110区分runtime/contract/semantic/policy/outcome与条件性proxy；L270～290特别是L283明确“prompt扰动的仪器稳定”与独立human anchor alignment分开，稳定与高相关不授正确；L450～476的ResourceBudget段区分实际消耗与控制，明确输出token不能证明工具/等待/重试总费用下降。相邻[Ch65](../../../../../books/part-06-ai-infrastructure/65-kai-scheduler.md)L100～126交接资源placement与有效产出，[Ch67](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)L1～30区分observed aggregate health与质量定义。

**建议已有覆盖，不提长期缺口、不新增Books。** 本文的“prompt自一致非外部正确”已有具体论点承载；外部工时与chat后成本是该既有测量对象边界的本次局部实例，不因为没有本文名字或JIRA这个场景就需要整合。few-shot的rank/log相关方向分离留在报告的评价条件，不从一组相关系数推广通用校准定律。请root独立判断准入/日期及此No Change；若认为它改变未覆盖的具体设计选择，应指出准确差额再协调写入，而非先造段落。

## 可执行停点

单项原源与owner对读准备好；root可独立核三个发布字段与Bibtex冲突、1000-ticket对照的信息不等量、few-shot两个指标方向及Ch66L283/L460。作者继续无关来源和八项具名有限日期恢复。此单项待独立判断，不等于26日Evidence/Books/day通过。
