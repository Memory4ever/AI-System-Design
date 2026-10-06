# 2025-10-08 FIRST 独立复核

复核者：Codex 独立复核会话，非作者 Mill；继承当前模型，未切换。
记录时间：2026-10-05T04:50:20+08:00。
本日窗口：`[2025-10-07T09:00:00+08:00,2025-10-08T09:00:00+08:00)`。
实际读：[本日日报](../../08/README.md)、[CALIBRATION_REQUEST](CALIBRATION_REQUEST.md)、[CURRENT_STOP](CURRENT_STOP.md)，以及本轮必要原始材料。
启动时鲜读 AGENTS、研究合同、来源使用说明/每日组、Report 合同、统一 Prompt、ROADMAP 与当前10月 checkpoint。跨日只定点解析 root01 RSS 的同报告记录，不读其他日期整池。

**FIRST 结论：Gemini 最小准入与6分通过；历史精确接口/安全效果尚未验收。OpenAI 同家族的两个页面发布记录可区分，Oct7主发布core对已读case命题可有界复用，不授同事件重复已审或整PDF历史首公开。不是 DAY、最终 Evidence、Books 或14source验收。**

root补充事件区分建议后，本轮以已实际打开的两类原入口独立核对：接受“案例页发布”和“主报告发布页发布”的命名分工，收窄此前对首次公开矛盾的判断。日期字段不同不自动构成不同页面事件的矛盾；只有采用命题需要整份报告首次公开/精确历史版本时才保留对应缺口，不要求互联网无遗漏证明。

## 1. 给 Mill 的可执行反馈

1. Gemini 可以进入正式必要证据审阅。把采用命题写成“当前官方对该产品发布的说明明确区分模型动作提议、模型外逐动作安全检查、用户确认与客户端执行”；不要把通用 screenshot/action loop、安全sensor分层或有guard即安全当新增贡献。不要声称“原有工具安全只依赖模型输出”，既有系统也可有独立执行器权限/approval。
2. 6分维持 `Design Delta2 + System Reach2 + Durability2 =6`，只评上述公开边界与需要重新核验的控制契约：2是具体安全控制分工，2是模型/API与客户端执行跨边界，2是可复用的适用约束。不是机构、preview版本、性能宣传或多个owner加分；安全约束触发受影响核心深入审阅，不由6分自动授安全效果或Books差额。
3. 正式证据同步保留 model card 的注入/不可信网页、误解用户意图、不可逆错误动作/数据外泄与敏感信息输出风险，以及要求确认时开发者不得绕过确认。模型外服务不等可证明的reference monitor、全动作fail-closed、无误判或注入免疫；卡片没有给出这些保证的量化证据。
4. 版本限定必须保留：[gemini_release.html](gemini_release.html) 原 `datePublished=2025-10-07T19:00:00+00:00` 落窗，`dateModified=2026-01-07T18:57:02.363124+00:00`。当前 card 标题含 updated2，正文保留 October7 发布标签，不能称本轮拿到了不可变2025原始字节。尤其当前开发文档已改为 Gemini3.x，不用其现在的 `safety_decision`/字段/API默认行为补证2025精确接口。最小发布说明可以继续审，未确认的历史接口细节应收窄/隔离，不用新版材料静默填满旧版缺口。
5. OpenAI应写“10/01 October威胁报告的七个案例页发布；本窗10/07主报告发布页发布，同一材料家族的两个页面事件记录”。不要写成“报告于10/01首次公开，因此10/07同事件重复”。本轮实际读主发布core L22-L26，只有季度案例、既有攻击流程提效、未观察到新攻击能力、账户处置/合作的概括，没有相对已读case最小命题的新机制、安全反侧或具体评价纠错。可有界复用01已读case命题，不新增候选/不重复评分；说明关闭的是主发布core的新增贡献判断，不是“整份PDF已审无新贡献”。若不采用整PDF首次公开或原字节的历史事实，不必为此阻塞上述关闭；确实依赖时才保留下面的精确缺口。

## 2. Gemini 实际原文与安全反侧

本轮实际打开 [Google 原发布 HTML](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)，不是复用作者“已读”标签。

- How it works L240、L244-L247：请求/截图/动作历史输入，function call提议，某些动作必须确认，客户端执行，随后回传截图与URL；主要为browser，非已优化desktop OS控制。
- How we approached safety L265-L271：训练内安全与模型外inference-time逐动作检查服务并存，开发者可指定拒绝/确认，仍建议发布前充分测试。原文没有把逐动作检查服务描述成独立、无误的授权证明器，也没有证明只靠system instructions就能阻止客户端违规执行。
- 实际打开 [Gemini 2.5 Computer Use Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Computer-Use-Model-Card.pdf)，重点完整读取物理p4-p5的 Known Limitations、Ethics and Safety、Additional Risks & Mitigations（web L66-L130）。它保留网页注入、误操作/泄露、输出危害，区分后训练确认与推理期monitor/filter、网址限制、输入输出过滤，并写明必需确认不得绕过。
- Card 的 Frontier Safety Assessment 不在框架范围，是工具能力范围判断，不是“通过前沿安全测试”。卡片借用Gemini2.5 Pro评估并列出内部red team/review类型，不提供本轮最小安全命题的完备性或生产风险消除证明。
- 实际打开 [当前开发文档](https://ai.google.dev/gemini-api/docs/computer-use) 的导言与控制循环 L88-L95、L196-L209，识别其 Gemini3.x 与新API内容后停止历史接口采用，不继续遍历全部示例。它只作版本漂移反侧，不能证明2025当时字段。

因此，“具体公开控制分工及其剩余风险”值得继续核验；这不是发明分层治理原则，亦不因章节已有同类原则而立即排除有边界价值的发布实例。ROADMAP 路由 `PLATFORM-SECURITY`（Ch72）、邻接 `AGENT-TOOL-CALLING`（Ch78）合理；本轮没有读Books实际论点/邻接或验收已有覆盖、仅报告、写入。性能比较/latency/跨harness排序不在本轮采用命题内，未授其通过。

## 3. OpenAI：两个页面事件与当前PDF身份

实际结构化解析 [08存档RSS](openai_rss.raw) 与 [01存档RSS](../daily-20251001/openai.xml)，两份各1245 item，都同时包含下列两个不同日期的页面事件记录；不是两个抓取时点先后覆盖字段的差异。若强行把两者都解释为“整份报告首次公开”会冲突，按原入口身份分开则不必然矛盾。

| 必要原始依据 | 实际原字段/声明 | 能证明什么 |
| --- | --- | --- |
| 七case RSS记录 | 各 `Wed, 01 Oct 2025 00:00:00 GMT`，BJT `2025-10-01T08:00:00+08:00` | 按官方字段权限支持七case页面发布记录的日期，落01窗口；不能单独证明整份PDF当时已公开。 |
| 本轮打开的 [Russian case](https://openai.com/index/disrupting-malicious-uses-of-ai-russian-speaking-malware-tooling/) 与 [Stop News case](https://openai.com/index/disrupting-malicious-uses-of-ai-stop-news-2025/) | HTML页首 October1；L24明确称case原先发表于October2025报告；PDF链接一致 | 页面内容归属报告，但“originally published”本身不给报告首次公开日/时，不证明PDF与case页面同日公开，也未明说Oct1先case再Oct7整报告。 |
| [主发布页](https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/) 与RSS主条目 | HTML页首 October7；RSS `Tue, 07 Oct 2025 03:00:00 GMT`，BJT `2025-10-07T11:00:00+08:00`；L24季度更新，L26链接报告 | 主发布页面记录落10/08窗口；不是明确的“首次报告公开”或“再次发布/修订”声明。 |
| [官方Forum活动页](https://forum.openai.com/public/events/virtual-event-disrupting-malicious-uses-of-ai-xmv3xd7zlq) | October7，22:00-22:40 GMT；说明讨论latest threat report | 支持10/07推广/讨论事件存在，不证明报告当日首次公开；没有打开视频或其他活动全文。 |
| 当前 [PDF原件](openai_threat_report.pdf) | title为October2025 update；封面只有October2025；37页；13,394,397 bytes；metadata只有Title/Producer，无CreationDate/ModDate | 当前存档身份；目录列七case。没有精确首次公开日/时，也没有原版可用性证明。 |

两HTML入口链接同一当前URL：`https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf`。本地SHA256：`e119c3e9ebbbc321838a1fc5720305ed40853dccbfef5b8b26cf7f31777dc535`。本轮只一次官方HEAD，HTTP200、`Content-Length=13394397`、`Content-MD5=rhWcsHdrqgeUim9RcAUzCw==`，与本地MD5一致，支持本地就是当前官方字节。

**必要新增边界：** HEAD原 `Last-Modified: Wed, 08 Oct 2025 03:03:09 GMT`，BJT `2025-10-08T11:03:09+08:00`，比本日报终点晚2小时3分9秒。该字段是当前对象最后修改标签，不是首次公开、不等于首次上传、不证明修订重要，也不说明改了哪段。不能由此把当前PDF具体内容冒称在10/01或10/07已存在，更不能机械新增10/09重要修订候选。

### 独立裁决与停止

- 采纳root的事件命名：01是“October威胁报告的七个案例页发布”，日期权仅case原页+RSS；08是Oct7主报告发布页面记录，日期权仅主原页+RSS。两个页面事件同家族，不必然同事件重复；不称Oct7“再次发布”或Oct1“先公开整份PDF”。
- 本轮主发布core实际增量检查停止于L22-L26，没有超出已读case最小命题的新贡献/安全反侧。因此可以按原命题身份、证据位置和适用边界复用01的Russian/Stop News内容核验，不重复评分，不再要求无差别读整PDF。不能把这种命题复用写成“Oct7事件已在01处理”或“PDF全部内容已在01深入完成”。
- 必须保留的边界是**整份报告历史首次公开/当时PDF字节未由本轮材料确定**，不是所有页面日期都不可信。确切官方记录分别为BJT10/01 08:00和10/07 11:00；当前PDF对象最后修改BJT10/08 11:03:09。不能捏造报告first-public落二者之间的可靠区间，也不能把当前PDFmtime当新贡献事件。
- root01有效内容审阅不被推翻；仅需将曾扩大到整报告首次公开的命名/依赖收窄到案例页事件。此次不修改01文件或共享状态。主发布core无新增贡献的判断无需等待互联网无遗漏证明；本轮不把这一最小范围之外的PDF原版日期问题升级成全日必须抓全历史归档的普通待办。
- 若后续确实需要当窗整PDF新贡献、报告首次公开或精确原版历史事实，定点恢复官方解释/勘误或可信的对应历史正文/PDF及公开时间即可；没有必要材料则将该具体命题隔离。再次取得相同RSS、当前对象mtime、搜索索引时间或旧完成标签不足，但不要求证明整个互联网此前从未出现，不反查全部版本史、不无限Wayback、不扩其他日期整池。

## 4. 必要安全/纠错内容与代表性排除

本轮PDF只读封面/目录与物理p6、p7、p9、p30，不读取全部37页/附件；以原HTML相关小节交叉核核心。p6-p7保留Russian构件“可能组装”、跨会话迭代以及模型未执行工具/无法验证平台外活动；p9保留未观察到超公开资源的新能力。p30确有Stop News旧Category3因疑似虚构合作证据而修正Category2。这些信号已经实际核对，作者不能按“只是又一批案例”忽略；主发布core对其概括可按已读命题复用。内容核对仍不证明PDF历史原版日期、全部37页已读、完整攻击成功或安全保证。

代表性排除实查3项：

- [VecInfer原abs](https://arxiv.org/abs/2510.06175)：实际读完整题摘及Submission history；v1字段确为 `Tue, 7 Oct 2025 17:35:28 UTC`。摘要有outlier处理/VQ/融合kernel潜在增量，不能因缺日期证据改判贡献不足；提交时刻不是公开公告时刻。日期未确认隔离成立，不授已审/零事件；未读全文或再扩官方分类库存。
- [ERNIE页2原件](ernie_page2.raw)：实际看具名条目的title日期字段，PLAS `2025-09-12 00:00:00 +0000 UTC`、PaddleOCR-VL `2025-10-16 00:00:00 +0000 UTC`，均不与本窗相交。窗外排除通过，无需读正文；不继承真实归属日报完成状态。

未验证其他来源的全体排除项、arXiv完整检索/first-public列表、S2R日期或所有14source历史停止点。当前FIRST范围只指1个Gemini拟入选家族与1个OpenAI同家族跨日页面事件裁决，不是已冻结全日分母。

## 5. 交接与文件验证

Mill应继续Gemini正式必要证据及Books处置；将安全边界/版本漂移与OpenAI具体日期隔离写回作者文件，再提交最终包。FIRST未变化的实际检查可复用，不要求无差别重读附件。没有通过最终日报六部分、Coverage、Evidence或Books，也没有要求修改共享Books/index/state。

反馈可由root直接转交Mill：本轮未从可用聊天列表取得可核实的Mill接收ID，不向可能无关聊天发消息，不声称已经送达。唯一工作区写入是本文件，保持未暂存；未stage、commit、push。

写后本文件8个本地链接均存在，Markdown与引用已读回；未跟踪文件以 `git diff --no-index --check` 对空文件检查无空白诊断（存在新增差异返回1）。这些检查不代替语义验收，也未执行最终日报V3校验。日报仍为进行中，本轮不以结构检查关闭DAY。
