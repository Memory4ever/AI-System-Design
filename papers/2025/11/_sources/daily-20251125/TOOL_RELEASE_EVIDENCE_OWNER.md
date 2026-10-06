# Nov25 advanced-tool：关联背景与单项证据/Books判断

**当前裁定：** root独立原源复核已否定下文初始19Z独立API事件推定，见末段及TOOL_INDEPENDENT_REVIEW.md。原始研究过程保留，不能把下文初始“now available”当原文引语、确认新事件或现行计数。

作者Aristotle。root已独立准入校准文章全文核心/接口；这里完成release身份分离与受影响兼容边界的必要深入，送独立证据/Books判断，不等待整个本日池。

## 事件身份

[Opus release](https://www.anthropic.com/news/claude-opus-4-5)已核三处published=`2025-11-24T19:00:00.000Z`，BJT11/25 03:00。正文明确随着此次发布，Developer Platform增加effort、context compaction与advanced tool use能力，并链接[工具说明](https://www.anthropic.com/engineering/advanced-tool-use)。采用的是**本窗明确平台API release**，不是宣称工具文章首次公开19Z、也不是把三项接口分别计成三个family。

工具文章原published=`2025-11-24T00:00:00.000Z`，BJT08:00在窗口起点前，保留不改；日精度正文不授权用19Z覆盖这个字段。原生HTML在native-tools.html，原release在native-opus.html；必要正文原响应见raw-date-and-trigger.json、raw-finite-mechanism-controls10.json和raw-tool-release-core13.json。beta header `advanced-tool-use-2025-11-20`、tool版本后缀20251119/20250825是接口身份，不是各组件首次公开证明。若此前已有部分接口，不能据本文反说首次发明或首次文章公开；本次只采用发布正文明确“now available”的新平台事件及其兼容/调用约束。

拟family=`SF-2025-ANTHROPIC-ADVANCED-TOOL-USE`，文章与release组合支持同一家族；2+2+2=6。新可用API把目录按需加载、程序内tool调用与示例接口绑定到显式版本/调用者/observation路径，改变集成方式和信息可见性；不将成熟检索、schema或代码控制流原理计新基础理论。

## 受影响内容必要深入

实际读文章完整核心及接口、使用/不使用条件：

- Tool Search：`defer_loading`只推迟schema曝光，默认保留少量高频工具；regex/BM25检索有额外搜索步，small catalog或所有工具常用时收益小。这里描述接口的目录/上下文控制，不授权工具，不证明开放目录召回或安全。
- Programmatic Tool Calling：§How works L190～263须工具显式`allowed_callers:["code_execution_20250825"]`，返回caller.type及caller.tool_id绑定调用代码实例；tool results被代码环境处理，不逐项进入模型context，完成后stdout成为模型observation。调用路由/可见性不是业务permission或side-effect正确性保证；原文没有提供每条backend授权实现，不声称已核生产reference monitor。
- 只需要aggregate/summary、大量独立调用时可以减少model round-trips；模型必须查看每个中间证据或单个短查询时不宜过滤，且额外code execution有成本。代码解析/筛选错误可以丢掉决策证据，作者未给通用fidelity保证；不能用上下文少证明端到端总成本或权限更安全。
- `input_examples`提供嵌套字段、日期/ID惯例与参数相关性的样例；合法JSON/学习样例不代semantic validation。样例增加context tokens，简单格式或可由schema验证的约束未必值得增加。
- 37% token、72→90参数准确率等仅为作者内部任务结果；精确模型版本、数据人口/样本数、等总预算、hardware/precision、并发、SLO、误差CI等未完整披露，不采用通用性能优势，不跨协议合并。没有运行API、核实现或复现。

只读取决定采用的核心/接口/限制，不扩读GIA benchmark全文或全部engineering文章。当前正文未列本项撤回/纠错，不为“无标记”扫描全历史。

## 实际owner比较与决定

已实际读取Books context、ROADMAP及最新相关checkpoint；唯一owner为`AGENT-TOOL-CALLING` [Ch78](../../../../../books/part-07-agent/78-tool-calling.md)。目标范围为L1～52、80～198、286～326、422～468；相邻为Ch77 L1516～1548的information-state→action交接、Ch79 L1～30的planning→execution状态问题。

具体已有正文：Ch78 Tool Contract保存identity/version、typed input/output、authorization、audit；L80分开schema、semantic validation与真实principal；L180附近目录按授权检索→shortlist→schema exposure且tenant-aware/versioned；L304附近程序化typed holes/control-flow仍由runtime检查capability，未给生成代码授effect authority；L436～454分开调用、permission、execution/outcome、cost/recovery及trace spans。上述论点实际承载本文的目录/校验/程序proposal边界，不需要重新写成熟机制。

**作者建议本项仅报告，不申请Books diff。** API调用者字段与最终stdout的具体路由是本次可核的版本兼容事实；必要证据没有证明一个现有解释失效，也未提供足以扩成通用程序执行安全模型的受控结果。模型必须看完整中间证据时的旧typed-call路径保留。它不等于“章节提过tool所以全部已有覆盖”：中间结果可见性细节在本次读段未展开，root若认为可形成长期条件分支，请以这个具体差额独立判断，而不是因PTC名称缺位整合。

请root核19Z release措辞与00Z文章字段、allowed_callers/caller实例身份不等业务授权、过滤后的stdout不等完整原始证据，以及仅报告决定。准备好的单项不等待日级全部来源；共享Books由root协调，作者未写。

## Root 独立回传后的实质纠正

已实际读取TOOL_INDEPENDENT_REVIEW.md。机制与仅报告通过；19Z Opus链接早工具文章和平台组合说明，不证明工具API再次release或有独立新增差额。原工具00Z且自称today release，保持窗前身份；作者初始“now available”措辞不是核实原文，不再采用。正式报告已移除独立工具family/评分，作为Opus必要关联背景，不因深审费时关闭贡献。若将来真实官方独立change/release和新差额到达，仅重开本事件；本次不继续空查询、不改文章首公开。实际Books写入0，无POST。
