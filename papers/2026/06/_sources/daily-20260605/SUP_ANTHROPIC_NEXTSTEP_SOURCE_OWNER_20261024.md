# Anthropic Jun04 next-step评价：必要Source / actual owner / 最小PRE

作者supp_20260605_author，2026-10-24。采用R35已核Jun04官方Institute卡片与具名贡献，不第三准入/日历。精确来源[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)，本地SUP_ANTHROPIC_SELFBUILD_20261024.html（262815bytes），目录SUP_ANTHROPIC_INSTITUTE_20261024.html。原页含Update9/18的session-success图说明，非本项129时点评价；只采用当前官方原说明的此接口，不称历史逐字/所有旧实验Jun04首发。未见影响本项的撤回/纠错提示，不扩全版本历史。

## 评分、支持和停止

2+2+2=6：Design Delta2为从整任务成功到真实trace截断点下一步判断的具体可测接口；Reach2跨会话取样、actor信息边界与hindsight evaluator；Durability2为条件化构念/信息分责。不给RSI前景、代码量/组织倍数、成熟Amdahl或机构身份加分。因与通用“胜过人类研究判断”解释存在边界差额，深入直接评估/脚注必要域，足够停止，不扩April实验/全部system card/外部METR。

实际完整读Evidence from within Anthropic中“Claude is getting better at steering research sessions…”原段、紧接How to read this图注、Footnote8及相邻研究goal/执行分工反侧。原实验：January–March2026真实ClaudeCode研究会话，选human detour且后来回归正轨的时点，actor模型只见偏离前prefix并提议next-step；另一个Claude能见实际完整后续，比较人类原下一步和模型建议。原129个时点刻意有human改进空间，模型只是在这个切片由Opus4.5 51%到MythosPreview64%被判较优。图中practical ceiling是可见完整会话的模型“ideal”建议，不是独立最优真值。

关键反侧Footnote8：另127个human下一步本已较强时点，同test中模型建议仅约20%被判更好。这能反驳“同一protocol必然偏向模型”的最简单解释，但没有消除选择偏差或校准judge真值，也不能把两组加权成部署总体胜率。两组仅局部conditional preference，不是执行替换后的真实研究结果、随机人机判断能力、自由选择研究方向或已实现RSI。

Not Disclosed：原129/127筛选流程、query集合/逐条labels、judge精确模型版本/prompt/候选顺序blind/randomization、各actor采样预算/重复/置信区间、人工真值校准、同人/session聚类，以及模型建议真正执行的反事实结果。没有这些不等零价值；当前只采用可复查接口/反侧，不作统计显著性、因果净收益或绝对研究能力保证。hardware/并发/SLO不适用于本项行为偏好构念；采样、历史处理、actor/judge/人审和真实重放完整费用未披露。本文未读原私有数据、未运行或复现。

## actual owner差额

按ROADMAP唯一`PLATFORM-EVALUATION-SYSTEM`，Ch66；非Ch79研究planning实现或Ch31训练目标。实际读Ch66开头交接、186–236 EvalSpec/eligible population与分析规范、1127–1180切片/不确定性组、5372–5398失败定位/可拦截接口、5444–5461人机team组；邻Ch65/67开头以及Books三公共上下文/2026路由已读。

现有一般切片/选择偏差及整轨迹failure定位，不能具体承载“同一prefix的下一步提议由可见完整未来的judge比较”这一不对称信息接口；team评价也没有这份真实研究counterfactual replay构造和强human反侧。不需要结构候选；建议在平均值/统计单位后补最小两段，保原校准统计对象与后文slice。不是只为放129数字加论文摘要。

## PRE literal，尚未授写/SAVE/POST/I

完整前锚：

> 这个式子只提供直觉。真实评估常有同一 prompt 的多次采样、同源数据、用户聚类和时间相关性，样本并非独立同分布。此时应采用与采样结构匹配的 bootstrap、clustered analysis 或重复运行，而不是机械套用置信区间。

拟新增两段：

开放式研究的下一步判断也可从真实轨迹构造局部比较，而不只验整项任务是否结束：先挑出人类偏离后又回到正轨的时点，让被测模型只读偏离前的历史并提出下一步，再由能见完整后续的judge比较模型建议与人类原动作。此时取样条件、actor可见prefix与judge可见未来必须分别保存；得到的是该切片上的建议偏好，不是替换动作后真实研究成功，也不证明模型会自行选对研究目标。

[Anthropic的受限研究会话评价](https://www.anthropic.com/institute/recursive-self-improvement)刻意选择129个有改进空间的时点；另127个人类下一步本已较强的时点，模型仅约20%被判更好。后者限制“模型普遍胜过人类”的解释，却不消除选择偏差或使hindsight judge成为正确性oracle；看到完整会话的理想建议同样不是可部署actor。应冻结筛选、模型/prompt、候选呈现与信息边界，补独立校准、较代表性人口或有权限的真实重放；轨迹处理、生成、判分和验证均计费。原始标签、judge资格或重放结果不可得时，只保条件化结果与Unknown，不将局部偏好外推为自主研发能力或生产增益。<!-- source-family:SF-2026-ANTHROPIC-NEXTSTEP-0604 -->

完整后锚：

> 校准的统计单位还必须和最终报警单位一致：先用所有局部窗口拟合“正常分数分布”，再对每张图或每次请求取最大分数，并不能把局部95分位直接解释为整次请求5%的误报率。一条[受限重构检测分支](https://arxiv.org/html/2509.03179v1)暴露了这个局部到聚合的接口；窗口数量、尺寸、重叠关系与聚合器改变后，应在独立干净请求上重新检查最终统计量的阈值和FP/FN，而不是把相关窗口当更多独立样本。高AUROC也不批准某个手选阈值，detect到异常不等过滤后任务已恢复，更不能认证未告警即无污染。干净校准人口、所有窗口/失败尝试、阈值选择、额外编码与下游回归都付费；tail支持或净收益不足时，保留原始分数、明确未知区间及受限抽查/隔离，不让一个局部分位数替完整请求签发安全。

当前只申请非writer必要Source/actualowner/PRE；本人注仅获新授后可加true-H2 Review notes，保精确原说明/6分/必要域/反侧与未复现，不动他人注。单篇ready先交root，余十三必要层和官方标题stop普通，不等齐、不扩新Methods；无Books/State/index修改。

## 当前R39–40采用与真实SAVE

实际读回reader R39–40，必要Source/actualowner/原两段PRE通过，无literal修句。root本轮明确新窄授上述Ch66两个完整锚之间原两段，作者已apply_patch真实保存，现有true-H2 Review notes增加本人一注。已完整实际自读新增两段、直接完整前/后段与本人注；原literal两段逐字存在且恰一处、正文family marker恰一处。删除本两段及本人注后的完整Ch66字节与本轮写前快照一致（SHA256 7722bef3b45d07d3f16f6cf6c956334576adf47374e896f109bc0de944873dac）；未改其他正文或他人注，未因共享文件的既有diff覆盖其工作。

README§1“129/127-session”已行政修为选中时点，不将它们当独立session。当前仅真实SAVE/完整selfread待唯一非writer actualPOST，未预I或DAY；既成新增8I、旧Kimi另保/合计9I和DistIL7争议不变。其余十三必要Source及官方相关标题stop普通保持，不为等待POST扩Methods。无State/index/他日写入或stage/commit/push。

当前R41–42已实际采用：唯一actualPOST通过，本项整合生效/窄位释放，累计新增I9，旧Kimi另保合计10I。仅行政同步README/本人注/Source，不重技术正文/第三Source或POST；十三普通必要层与标题有界stop/日级独核保持，不授DAY。
