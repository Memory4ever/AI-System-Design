# Nov27 来源独立复核与局部修正

复核者：Carver；作者：Aristotle。实际新恢复2026-10-04T18:58:59+08:00起，结论尚未授日级通过。只本日14源有限停止，不复用别日响应。

## 已发现的普通修正

1. **DeepSeek Research入口实际遗漏。** 本日原生[主页](./deepseek.html)页尾“研究/更多”href为`/news/`，updates是API changelog，不能代替Research。非作者实际打开[官方Research索引](https://www.deepseek.com/news/)：动态段5个当前条目；Research段10个题名，相关邻接Nov27 DeepSeekMath-V2、Nov1 LPLB、Oct21 OCR、May14 hardware。两个View all按钮仍存在，本次只读取当前返回10项、已跨目标段，不声称完整隐藏/删除历史。不能保留“当前目录无本窗项”的旧断言。
2. **新增具名潜力而非确定当窗候选。** 上述官方Nov27日字段无时区，非作者继续实际读[DeepSeekMath-V2 exact-v1完整题摘](https://arxiv.org/abs/2511.22570v1)L16–19/history L27和[官方仓库Introduction](https://github.com/deepseek-ai/DeepSeek-Math-V2)L169–175。终答案正确不保证推导正确；准确/忠实verifier作为generator reward并鼓励自检自修，通过增加验证计算标注困难proof维持generation-verification gap，足以保留训练/验证机制潜力，不是数学科学应用名称收录。未核IMO/Putnam评分、训练预算、验证因果或全部method，未借宣称得分为正面证据。原v1 submitted `Thu,27 Nov 2025 16:01:22 UTC`在截止后，但**提交不是首次公开**；官方索引日期和当前仓库未给完整落窗first-public上下界，不能单凭submitted授窗外，也不能补造窗内。有限原恢复后具名日期隔离；作者应把原46改为47总潜力，并把这项放§5，不列§3/不评分/不进Books。重开只需原公告或作者首次发布上下界，届时只恢复本项。其题摘/引言未显示撤回，未遍历版本史。
3. **MiMo More不是anchor。** 本日原生[mimo.html](./mimo.html)实际已返回15个Blog题名，包括折叠09–15；More为`button`，不是可分页anchor。当前无日期仍不足恢复2025 Blog历史，保留这一真正缺口；仅修正文与SOURCE_CHECK的界面/停止描述，不扩15题名全AB/全文队列、不授历史无遗漏。未声称完成本日浏览器点击或全部JS核查。

非作者已完成上面最小材料恢复；作者所需只是README §1/2/5/6、SOURCE_CHECK及BOUNDED的局部事实同步。不是等待外部服务，也不是要求重新扫描其他13来源。日期真正保留与普通报告同步分开。

## 十四来源实际有限终审

本次非作者截至2026-10-04T19:06:27+08:00实际重读六部分及SOURCE_CHECK，检查对应native receipts的URL/参数/执行时间/status/error/bytes；成功材料字节数与文件相符。Google两12s timeout/0bytes、Meta reset/0bytes和OpenAI403均不作零事件证据；失败receipt而没有body符合实际错误，不由此授内容覆盖。未重复失败网络请求或浏览器操作。作者Hunyuan浏览器visibility/timeout记录只按作者过程说明，非作者没有独立重现该浏览器故障；独立确认的是native Research动态页及publicList原响应/receipt。

| 来源 | 非作者实际范围与停止 |
| --- | --- |
| OpenAI | XML独立解析1245项/缺pubDate0，唯一窗内Mixpanel；Research403的原receipt。单项日期/安全/Books按MIXPANEL_INDEPENDENT_REVIEW，不重读全部安全附件 |
| Anthropic | 原HTML Next Flight独立解码1chunk/0Tframes/172唯一dated posts，Nov25 11:05Z与Dec1 00Z相邻，目标窗无当前目录项；不授删除历史 |
| Google AI | 原Research及真实page4 native日期/链接，page5 web原目录Nov→Oct；纠正`?page=4`不是历史分页。Nov20 image-verification与Nov18 developers原页字段实际读；明确科学应用标题范围停止。Google pubs/November Blog失败使整组受阻，DeepMind成功不代全组 |
| Meta | native reset receipt、web返回0lines和原域有限query记录；历史必要原事件仍不可得，不支持零研究 |
| Qwen | 原旧BlogSep/Jul范围、新Blog94344bytes动态无目标日期、web0lines及有限原域query；旧站Next不必扩历史，当前新站缺口仍隔离 |
| DeepSeek | 原主页Research More真实`/news/`，非作者新原Research有限10题名及一个exact-v1/官方repo恢复；旧updates不能代Research，以上普通修正必须同步 |
| Moonshot | 原HTML独立解析26个dated文章，最新Nov7/6至2024，未见Next；导航非文章，不继承别日响应 |
| Hunyuan | 原Research动态页与API原data.totalNum=9/list=9，逐条displayPublishTime均2026Feb→Sep，20短页停止；不以可用API替代2025 Research全部历史 |
| ZAI | 原Flight首查11chunks/0Tframes，15可见卡片、16嵌入CMS dated身份（含额外未展示项）；page2 14chunks/1UTF8 T-frame，18唯一CMS IDs/hasMorefalse、最老Dec7 16Z。Nov缺段仍受阻，不拿首查/嵌入计数差异造2025新项 |
| Seed | 独立原四页18/18/20/18共74标题/date/pin；year2025/count20/US，totals94/45、next20/40、has_moretrue，非pinned已跨至Oct22/23及后续更老Jun段停止，不授全年穷尽。DA3 pinned PublishDate落窗与Nov14首事件分开，当前bug另隔离 |
| ERNIE | native首查10条至Nov21与真实Next原page2全部6题名/date至Jun30、无Next；有限目标段未见项不授完整删除历史 |
| MiMo | 原HTML八个Paper日期，Jan8→Oct21邻接；全部15Blog无日期、More原生button，不是分页anchor，真正历史日期缺口隔离；不扩所有标题全文 |
| MiniMax | 原EN12/CN13 dated条目跨Dec23→Oct27；独立Agent原入口与真实llms index L0–49读取50行（含标题/分隔，不能称50篇Tech文章），Code/CLI/current Agent Team及Tech链接未恢复2025必要历史；已触发/受阻不是未触发 |
| arXiv | 独立四XML解析30/5/2/26，totalResults等于实际返回、start0/itemsPerPage50，59去重身份；查询参数实际绑定窄主题及submitted发现区间。两个DC native标题页真实skip150/200、show50仅查漏，月338不成为全AB/全文队列。原46日期/反侧另核，不授公告或全分类召回 |

表外Mixpanel、DA3、Agent0均由具名材料触发，本次核必要对照/纠错/日期节点，不触发会议/Weekly整站。原47潜力日期、具名历史缺段和DA3修复日期保留只允许定点重开，不支持正面Evidence、Books、性能/安全保证或无遗漏。全部原46题摘与关键反侧及Mixpanel独立结论可复用，不要求重读附件。

另需顺手精确修正MiniMax SOURCE_CHECK的“llms五十条”：原材料是50行文本，不是50篇文章；写50行当前文档索引即可。这是报告计量普通修正，不是新增材料队列。

本日范围复核已经完成；剩余仅上述作者局部同步及日级复核确认同步结果，不能把这些普通工作授为external。最终结论见[DAY_REVIEW](./DAY_REVIEW.md)。
