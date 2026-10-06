# Nov27 本日来源与有限停止

作者Aristotle。窗口BJT[2025-11-26 09:00,2025-11-27 09:00)，UTC[Nov26 01Z,Nov27 01Z)。本日独立首查/恢复见各`*.receipt.json`的URL、参数、执行时间、状态、字节与错误，web实际请求汇总[web-queries.json](./web-queries.json)。没有加载Weekly来源、别日候选或旧Weekly。当前目录不是删除历史的完整证明。

## 十四来源

| 来源 | 本日实际范围/停止 | 结果与权限 |
| --- | --- | --- |
| SRC-OPENAI | Research403/9686bytes；独立RSS200/759641bytes，1245条、缺pubDate0，按本窗过滤一项Mixpanel | RSS一项日期确定；Research访问限制不等于零研究。RSS当前保留目录不认证已删材料；[窗筛](./openai-window.json) |
| SRC-ANTHROPIC | Research200/279365bytes；实际JSON解码NextFlight一chunk、172个唯一dated posts，Nov25 11:05Z Productivity→Dec1 00Z相邻 | 本日当前目录目标窗无项，不授全删除历史完整；[原字段](./anthropic.html.metadata.json) |
| SRC-GOOGLE-AI | DeepMindResearch200；初次`?page=4`实为新页不是历史分页，改真实`/blog/page/4/`200及page5 web原页；page4 Nov2025段至page5更老段。定点原日期image-verification Nov20、Gemini3 developers Nov18，科学应用标题停止不读全文 | **整组受阻**：Google pubs `?year=2025`与Research November Blog各12s timeout/0bytes，web未恢复。DeepMind部分成功不能冒充Google全组已检查；原目录只有月份，不据此补精确公告时刻。实际[page4原生目录](./deepmind-real-page4.html.metadata.json)、raw-bounded21/22 |
| SRC-META-AI | Research原生reset/0bytes，web失败；实际Nov26官方主题定点query首页无有效恢复 | 受阻，不能证明无当窗研究；停止重复空路径，重开需原历史研究目录或具名原release |
| SRC-QWEN | 旧Blog200/17307bytes日期至Sep/Jul；新Blog200/94344bytes动态内容web未恢复；本日Nov26官方query有限首屏无有效历史段 | 受阻：旧站片段不证明新站本窗无事件，需2025目标原历史段/原公告 |
| SRC-DEEPSEEK | 主页200/115583bytes真实Research More href为`/news/`；Carver原Research恢复动态五项/Research十题名，Nov27 Math-V2→Nov1 LPLB→Oct21 OCR→May14 hardware；实际读Math-V2完整v1 AB/官方repo引言；updates200仅API changelog | 已检查有限真实Research，Math-V2具名日期潜力保留；两个View all未穷尽，不授隐藏/删除历史。详见[实际独立恢复](./SOURCE_INDEPENDENT_REVIEW.md)，不重复网络 |
| SRC-MOONSHOT | 官方Blog200/13388bytes，web实际26个日期文章，最新Nov7/6，无Next；非文章导航不计文章 | 已检查当前有限Blog目录，目标窗无项，不继承别日计数；[本日原文](./moonshot.html.metadata.json) |
| SRC-TENCENT-HUNYUAN | 首查Research200/6893bytes但动态无列表；浏览器先subagent visibility不支持，默认重试30s timeout/kernel reset。随后POST publicList `{pageNum:1,pageSize:20,renderType:0}`200/315236bytes，实际data.totalNum9/list9、displayPublishTime均2026Feb→Sep | 受阻：API可用但只恢复2026，不替代2025 Research“全部”；本日Nov26原域query仅相关PDF线索不生成全文队列。停止此浏览器失败路径，需本窗历史Research列表/原事件 |
| SRC-ZAI | 首查Research200/1276382bytes，15条至Dec9；真实page2 native200/1397496bytes，NextFlight14chunks/一个UTF8 T-frame解码18个唯一CMS blogIDs，`hasMore:false`，最老createAt Dec7 16Z | 受阻：目录止于Dec8 BJT，无2025Nov历史段；不是零当窗研究。Nov26原域query无有效恢复，需原历史目录/具名事件 |
| SRC-BYTEDANCE-SEED | GET article_type1/2、publish_year2025/count20/page_token0/order_desc=true/headerUS；p0各18、totals94/45、has_moretrue/next20，保留未来pinned。p20 type1=20/type2=18，更老Jun→May和Jun→Feb，has_moretrue/next40；非pinned首项Oct22/23，停止更老后续页 | 已检查本日有限当前目录，非年度穷尽。type2pinned DA3原PublishDate1764172800000=Nov26 16Z落窗，但首事件已由官方项目Nov14公开记录排除重复；未来置顶不当历史边界 |
| SRC-BAIDU-ERNIE | 官方Blog page1 web十条至Nov21；实际Next page2六条Nov11→Jun30，无Next | 已检查有限原Blog目录；目标窗未见项，不授删除历史 |
| SRC-XIAOMI-MIMO | 主页200/58220bytes；Paper八个日期项2026Jun→2025May，Jan8→Oct21邻接；原HTML有全部十五Blog题名含折叠09–15，无日期，More实际button；Nov26原域query有限首屏无恢复 | 受阻：Paper可查不能覆盖Blog历史日期缺段；未声称浏览器点击，不把所有标题变全文队列，重开需目标Blog日期/原公告 |
| SRC-MINIMAX | EN Blog十二个dated项至Oct27，CN十三项至Jan15；Agent Tech原入口→llms五十行当前文档索引，含标题/分隔非五十篇文章，未恢复2025历史；Nov2025原域query有限首屏无有效段 | 受阻：EN/CN有限目录已读，独立Tech缺必要历史，不能整组写零研究；需2025目标Tech历史/具名原文章 |
| SRC-ARXIV | 四组窄主题API，submitted区间[Nov24 19Z,Nov25 19Z]，start0/max50/descending，30/5/2/26短页到末，共63返回/59唯一身份；有界DC月标题151–200、201–250（全月338只线索），只读直接相关机制题摘 | 已检查这些发现入口；关键词/可能词干不保证主题语义，提交不证明公告。日期不确定材料隔离，不授63/59为当日论文数量或全分类召回 |

## arXiv真实主题与筛选边界

请求全文保存在[fetch_window.py](./fetch_window.py)及四个`arxiv-*-query.json`，实际URL在对应receipt。主题为CL/LG语言模型/Transformer/MoE；DC/AR/PL/OS/PF语言模型/GPU/kernel；AI/IR/MA工具/记忆/context+LM；CV/RO foundation/world/VL/VLA。`start=0,max_results=50`，实际total与返回数相等且短页，未发第二页。DC宽月只浏览两段标题弥补新命名；没有把338个条目变全题摘或全文队列。

完整题摘/贡献判断只对本日发现的相关材料，精确v1优先；API返回晚版摘要不是v1证据。明确MRI/PET、材料、病理、抑郁/医学错误应用等按标题范围停止；不经通用Evaluation重引AI for Science。需要题摘才能判断的读完整题摘，不因小模型、benchmark、局部负证据或既有组合标签自动关闭。实际搜索仅第一页、具名原源恢复，不循环空探针。

具名DataCite原字段集中[exact-date-fields.json](./exact-date-fields.json)，并保留每个原响应/receipt。Submitted是提交；Available只有2025-11；Created/Registered/Updated是元数据处理线索，不能填成作者首公开下界。created在本窗或终点之后均不单独决定真实first-public归属。官方常规20ET schedule不能补造精准公告时刻；终点09BJT不属于本日。允许真实原公告上下界完全落窗时采用，不以统一datehold规避已有确定日期。

## 表外触发与纠错

表外[Mixpanel原通告](https://mixpanel.com/blog/sms-security-incident/)只用于OpenAI具名事故的必要对照，日字段Nov27/时区未知，不新造当窗家族。表外[DA3官方项目](https://github.com/ByteDance-Seed/depth-anything-3)只为Seed文章的重复/受影响纠错：官方README明确Nov14 paper/project/code/models released；本日文章“Recently unveiled”没有新机制事件证明。当前model table说1.1 retrained after training-bug fix/original deprecated，已读受影响表，但没有精确修复公开日期，不把旧性能或当前修复回填本窗。README本窗path限定GitHub commits请求实际200/[]，只证明此path此API范围未返回项，不证明全repo无改动。

OpenAI事故当前Dec19 clarification实际受影响段已读；其后文非Nov26历史冻结文本。安全/负证据论文只补必要threat、comparison、限制，不扩大所有附件。NeurIPS文字标签不是本日会议发布触发；没有固定扫描OpenReview/MLPerf/Weekly来源。

## 终态保留与精确重开

历史目录缺段单独保留Google pubs、Meta、Qwen新站、Hunyuan2025、Zai2025Nov、MiMo Blog、MiniMax Tech；均有本日有限实际尝试，不支持正面候选、Books、无遗漏。收到上述目标历史列表/具名原事件才恢复对应行，不再反复相同空路径。论文具体缺少first-public下界或精度，在候选筛选笔记逐项身份保留；精确作者事件/官方公告上下界完全落窗才重开该项，不扩当日全文队列。DA3 bug只在原始具名修复记录到达时处理对应真实日期。
