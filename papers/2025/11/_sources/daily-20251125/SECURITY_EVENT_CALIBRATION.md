# Nov25 安全事件追加准入校准

作者Aristotle，恢复阶段定点原源发现。不是全池重新校准，不授日级通过。

[Mitigating the risk of prompt injections in browser use](https://www.anthropic.com/research/prompt-injection-defenses)，实际完整核心L11～45在[raw-resume-official-slice12.json](raw-resume-official-slice12.json)，原HTML在[native-prompt-injection.html](native-prompt-injection.html)。独立本日GET后的article:published_time、JSON-LD datePublished、time datetime一致为`2025-11-24T15:10:00.000Z`，即BJT11/24 23:10，完全落窗；dateModified为2026/09/10，保留当前正文版本限制，不冒称逐字历史快照。当前页无已列具体撤回/纠错标记，未遍历全历史。

拟准入命题：浏览器行动扩大不可信内容入口和可执行动作；作者用每环境100次尝试的自适应Best-of-N攻击对比原preview与此次beta配置，报告当前约1% ASR仍有实质风险。这个局部负证据可改变“低平均ASR足以授权高价值行动”的判断，不采用通用领先/已解决/生产安全承诺。作者同时改变模型RL防护与外围classifier/intervention，图对比不能单独证明某一层收益。试验环境/样本规模、模型与防护独立消融、置信区间及生产基率尚未披露，必要时只读对应系统卡安全评价的条件，不遍历附件。

拟评分2+2+2=6；属于安全约束变化，受影响内容深入而非因6分只读摘要。原文实际新增是有攻击预算限定的beta配置局部证据与残余风险，不把成熟“不可信输入”原则计为新基础理论。它与本日Opus release属关联事件，默认归入既有`SF-2025-ANTHROPIC-OPUS-4-5`家族，不因另一个URL自动增加家族数；若root判Chrome安全配置需独立family，请给具体边界。

请root独立校准此窄命题/版本采用边界。Books目前不申请改动；ROADMAP实际owner为PLATFORM-SECURITY Ch72，需先读其承载的具体论点，名称未出现不是差额。已有覆盖或仅报告都可成立。原页全文核心已准备好，作者继续其他无关来源收束，不等待此校准停止全部25～29。

代表性新关闭：OpenAI [JetBrains客户案例](https://openai.com/index/jetbrains-2025/)核心L32～96实际读，只有模型集成、人机review与客户工作流程，无可辨认的新模型/执行机制、受控比较或成立边界；贡献关闭，不把客户采用当训练/系统增量，不为关闭项另核无关日期。raw同上。

## 实际 owner 比较（2026-10-04T16:21:09+08:00）

已读 Books context 与 Ch72 开篇、L600～630、L1308～1340、相关执行门禁段，并核 Ch71/73 交接。具体已有覆盖：Ch72 L600 区分 matched model population、单轮与 adaptive 威胁，classifier 是 sensor 而非授权；L1326～1328 已要求保存攻击访问权与搜索预算，且把 checkpoint 修补与 monitor/部署防线更新分别回归，不把完整服务更新归因于模型训练。故本页拟采用的局部残余风险与复合配置限制已有实际论点承载，不申请重写成熟机制。

建议 Books 为已有覆盖 `PLATFORM-SECURITY`，beta/browser 发布与作者当前 ASR 留报告，不把约1%或Best-of-N100换成开放威胁概率、生产安全或单层因果效果。具体核心已读足以支持这个收窄命题；模型与防护独立消融未披露，不用扩读所有安全附件填补。仍待root独立确认此追加事件及处置，不授家族或整日新增通过。
