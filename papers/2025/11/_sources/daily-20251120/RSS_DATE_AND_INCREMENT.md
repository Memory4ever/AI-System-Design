# 2025-11-20 官方 RSS 日期与单项增量

作者 Dalton；2026-10-04T17:13:31+08:00。请求 root 独立核原字段、准入及处置，不授日级完成。

## 日期与事件身份

官方 [RSS](https://openai.com/news/rss.xml) 从官方页脚获得；web打开因text/xml不支持失败，实际下载成功。原始 [openai_rss.xml](openai_rss.xml) 与 [receipt](openai_rss.xml.receipt.json) 保留。只解析具名ID及本日相关时间段，不把整个feed变成其他月份研究队列。

| 事件 | RSS pubDate 原值 | 本日意义 |
| --- | --- | --- |
| [Codex-Max发布](https://openai.com/index/gpt-5-1-codex-max/) | `Wed, 19 Nov 2025 00:00:00 GMT` | BJT11/19 08:00，早于20日起点；请root定点核19归属 |
| [Codex-Max card入口](https://openai.com/index/gpt-5-1-codex-max-system-card/) | `Wed, 19 Nov 2025 00:00:00 GMT` | 同上；入口发布不证明PDF正文首次公开同刻 |
| [External testing](https://openai.com/index/strengthening-safety-with-external-testing/) | `Wed, 19 Nov 2025 12:00:00 GMT` | BJT11/19 20:00，发布方声明时刻落20窗 |
| [Business evals](https://openai.com/index/evals-drive-next-chapter-of-ai/) | `Wed, 19 Nov 2025 11:00:00 GMT` | BJT11/19 19:00，落20窗，贡献排除见下 |
| [Target partnership](https://openai.com/index/target-partnership/) | `Wed, 19 Nov 2025 06:00:00 GMT` | BJT11/19 14:00，落20窗，贡献排除见下 |
| [Early experiments in accelerating science with GPT-5](https://openai.com/index/accelerating-science-gpt-5/) | `Thu, 20 Nov 2025 00:00:00 GMT` | BJT11/20 08:00，仍在20窗；AI for Science暂停范围关闭 |

字段是当前官方RSS声明，不是独立测量的首次可访问时刻。两个00:00条目保留原值，不用较晚社区转发覆盖，也不据此反推card内部日期或初版逐句同刻。首批包“Codex只有自然日、五项日期均未定”的旧快照被本次恢复更新；20暂不将Codex计为确定当窗家族。19只请求具名日期/事件核，不重扫19、不继承其Books结论。

## 外部测试核心与反侧 ready

原始 [WEB_RSS_WINDOW_CORE.json](WEB_RSS_WINDOW_CORE.json) 第一篇L40–96及footnotes实际读完。对象是公开合作协议，不是独立实测安全效果；当前核心没有明示纠错/撤回，不遍历站点证明无标记。

旧判断“外部机构用自己的方法，所以所有评价权与公开权都独立”过宽。L56–61允许外部实验室用自己的方法，但checkpoint、mitigated/helpful-only配置和少数机构CoT访问由合作方提供并受安全控制；L63–68区分独立运行实验与资源受限时仅审内部方法/结果。L70–73将SME能力探测与safeguard red teaming分开。实际访问与证据对象限制可修正第三方评估范围的解释。

必要反侧L77–82、Appendix L90–97：NDA与非公开模型输出限制披露，L91范例Research Publications条款要求书面审查批准；L96另一范例也列已经公开模型信息、既有/合法第三方来源等例外，不能合成“所有结果披露都必须批准”的统一实际合同。补偿可含支付/API credits，作者声明不随结果支付。方法自主不等于开放checkpoint、无限审计或不受限制的出版自由；不随结果付费不证明不存在激励偏差，受限访问也不自动证明评价无效。只采用公开说明与范例的存在，不作法律结论，不证明每一合作采用同条款、覆盖完整、模型安全或独立复现。

拟准入命题：模型评估独立性需限定到方法、模型/轨迹访问与结果披露三个层面；这是具名协议边界，不把“独立复核有益”的成熟原则评分。请root校准本窗局部证据价值。

Books初步倾向 **仅报告**。已重读Books context与ROADMAP，实际读 `PLATFORM-EVALUATION-SYSTEM` [Ch66开篇](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题)、第一个subject identity不变量及小结：现有claim/evidence/inference/decision分层、subject含checkpoint/runtime/tool permissions，条件证据不能越权获得发布结论；Ch65交接只拥有资源admission/placement，Ch67开篇只拥有observed health，不迁移owner。协议是当时版本案例，未有新通用算法或足以纠正正文的证据。关键词未命中不证明长期缺口，不请求名称补录、不直接改Books。如root认为访问/披露确有正文差额，精确重开Ch66该不变量与claim→decision段，先核论证，再决定小段差额，不追加完整政策摘要。无写入、无POST义务。

## 两项代表性排除 ready

原始 [WEB_RSS_NEGATIVE_CORE.json](WEB_RSS_NEGATIVE_CORE.json) 两篇核心实际读完。

- Business evals L37–75：contextual goldenset/error analysis、真实条件测试、人工审核LLM grader、日志反馈、A/B互补。L42–43说明广义最佳实践框架，未给改变测量解释的局部实验、具体替代机制或新失效证据。不是仅因成熟而关闭，而是实际只有框架建议和例子，未建立修正主线判断的增量证据；请root抽检是否遗漏具体反证。
- Target L24–48：下周beta购物体验、企业使用规模及FAQ应用，未披露新执行/授权契约、训练机制或可比评价。商业采用与产品场景不足以准入，不能把购买流程改写成系统控制术语冒充机制。日期已恢复，无需继续日期附件。

## 普通停点

root可现在核此包，不等全日。其余来源历史边界、arXiv有界标题补检及14份exact-v1语义分层仍属普通工作；题摘已实际读完不等于Evidence完成。外部测试若准入，评分与必要证据/Books最终决定待独立反馈，不把本包称为通过。

## 17:51恢复补正

对原RSS实际按UTC `[2025-11-19T01:00:00Z,2025-11-20T01:00:00Z)` 过滤，**4个当窗条目**而非只看Nov19自然日的3个。新增science项标题/官方描述明确科学协作案例；[官方当前core](WEB_RSS_SCIENCE_SCOPE.json) L47–85实际核范围和限制，未见明示勘误/撤回。其科学案例及限制不通过Data/Evaluation owner重新引入暂缓路线；未打开75页报告或案例附件，不用范围排除回避相关安全纠错信号。其余3项及两个窗前Codex入口原判断不变。4条仅代表当前feed目标切片，不认证历史删除/未列Research材料。

arXiv两批完整题摘及current信号处理已记录于两校准包；初始“仍待14份分层/标题补检”是过程快照。root单项准入/Evidence/OnlyReport仍待独立核，未改Books或自授通过。

17:57必要反侧补正：重新定点核L90–97及footnotes L103–115，保留上述范例/例外，公开helpful-only定义不授实际posttrain recipe。L79 Apollo标签指向METR同链接，不用该未核报告支持效果，中心命题不依赖该例子。原HTML直抓403保留于 `external_testing.html`/receipt，它不是文章正文；可读原核心仍是web原返回。当前未见明示纠错/撤回，不声称2025逐字快照已取到或所有签约副本已核。作者评分拟2+2+1=5，实际条款/安全受影响内容深入，不给机构声誉或一般原则加分；OnlyReport待root必要独立复核。
