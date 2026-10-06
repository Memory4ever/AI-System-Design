# 2603.09884 — 风险评价的model×prompt交互与可比性边界（非作者Source/date/具体NC通过）

[Benchmarking Political Persuasion Risks Across Frontier Large Language Models exact-v1](https://arxiv.org/html/2603.09884v1)。第二包完整题摘已root独立准入校准；作者本轮实际完整Study1/Study2（HTML Sx2/Sx3）、Comparative Analysis Sx4/Table1与Conclusion Sx5必要文字。首个合并工具返回Study1中段截断，已单独恢复Sx2/Sx4完整；不把截断当全文。未核全部图像、Online Appendix数值/完整prompt、代码或复现。仅保留评价风险与设计边界，不生产政治说服prompt、策略或定向建议。

raw SUP_EXACT_BATCH2及本轮fresh官方题摘/history/DOI轻核：exact/current同v1、comment空，无已见withdraw/纠错信号；Mar10UTC16:42:05提交只是机会线索。official noadvance/announcement规则最早Mar11BJT08下界与arxiv.content owning/findable registeredMar11UTC02:24:13已可发现上界同BJT03-11夹证；注册不能单独充公开日。无具体先稿信号，不追全会议/仓库史；日期待root必要字段核。

2+1+2=5标准；既有风险排名不等prompt干预效果可迁移→同研究的两个实验出现model×prompt效应异号与人类baseline身份缺口→风险比较须绑定被测模型/完整配置、构念与对照，而不是从某模型策略收益授全模型安全/危险阈值。评分不加成熟随机实验/回归分。

## 必要证据与直接反侧

Study1 August2025 Prolific/Qualtrics N12988，两议题随机分配；四具体模型及两prompt条件在AI组内随机。Immigration有30–60秒human video和interactive AI text，处理形式/暴露长度不同；MinimumWage human video技术故障显示blank，重分类placebo，故human来自旧Chen样本Hajek-style协变量权重而非本轮随机同期human。median7turn/human68words/AI614words；立即post-treatment 5-point Likert与二元重编码，不是持续行为/投票结果。前处理回归/SE与预注册存在不自动消除形式和跨样本偏移。

Study2 earlyNov2025 N6157，同两议题但不设human组；四模型、AI/placebo与prompt随机，stance由participant前测反向确定，非stance随机。立即Likert/二元结局，median7turn/68humanwords/757AIwords。作者pre-registered固定效应inversevariance pooling，改random-effects/REML以容异质性并报告robust，不把其自动当未变预注册或完全独立复现。stance间人口易感性、Prolific选择、议题差异未分离，不能从较大一侧均值授普遍方向因果或固定政治倾向。

Sx2模型内prompt条件文字估计支持有限交互：GPT4.1 info .127(SE.011) vs plain .171(.012)，与其他模型point方向不同。Sx3 GPT5 info .110(.029) vs plain .204(.040)，而Claude4.5 .203(.052) vs .174(.054)、Grok4 .137(.040) vs .104(.023)；Gemini3 .136(.037) vs .159(.047)。这里只采用效果异质、不能跨模型移用“干预必提高”这一边界；不因point差或重叠CI声称各交互全部显著，也不采用未实际核A23/A25或图像精确高度。两议题/七总models不是普遍排名、更强通用能力导致风险的因果证据。人类与LLM形式不matched，不采“普遍超过人类说服”安全门槛。

Sx4会话标签由GPT5mini探索/正文GPT5.2给4790会话1–5评分，图caption写GPT5，版本描述保留；100会话人工相关不授全部标签真值。策略未随机，探索回归未预注册，固定效应不消除会话响应/受众敏感性等混杂，作者明确关联不是因果；不把高/负回归系数改成可执行最佳说服策略或模型内部机制。本文必要风险命题不依赖复刻这些prompt/策略细则，不扩附录。

曝光长度、模型/prompt版本、参与者与attrition、proxy标签/人工核、后测构念、跨样本对照与完整请求预算须分别绑定；token调用、调查/标注/复评均付费，硬件/precision/latency/服务SLO Not Disclosed。即时态度变化不能自签持久现实影响，也不单独认证部署安全或隐藏意图。

## 实际Books比较：拟具体已有覆盖

唯一owner PLATFORM-EVALUATION-SYSTEM，Ch66；作者实际完整214–235局部（truth sensor→监控配对→224方向翻转审计→joint/conditional→可识别假设）和271–311局部（构念/自动判分→完整EvalSpec/identity→realized comparison），Ch65/67开篇交接已读且未变。

224完整段已明确同baseline冻结matched cue、两个方向分别比较、不对称/backfire和model/reasoning条件化效应，sensor标签非真值/部署安全；285–310完整identity与realized comparison要求model/prompt/数据/预算/scorer冻结，区分bundled配置、实际请求与归因；274附近构念/仪器分责不许自动代理签真实能力。现有具体正文完整承载拟采用的有限model×prompt干预反侧与可比性边界，不新增Books或任意安全阈值。

root非作者实际官方v1 Study1/Study2关键设计、异号prompt点估计与Sx4关联非因果/Sx5限制、原batch2 owning/findable/noadvance日期，及Ch66 210–237/282–312完整具体owner已核，必要Source/date/具体NC通过。只采用条件化评价/构念/人口/对照与完整identity边界；不授普遍排名/持久行为/说服策略，未核全部Appendix/像素/代码，不授本日DAY。
