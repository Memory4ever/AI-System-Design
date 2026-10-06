# Nov28 本日来源、真实查询与停止

作者Aristotle。BJT窗口 `[2025-11-27 09:00,2025-11-28 09:00)`，UTC `[Nov27 01Z,Nov28 01Z)`。首查10:40–10:41Z，后续有限恢复至11:18Z；每次native请求实际时间、URL、参数、错误、字节保存在对应receipt。只复用解析器代码，不复用27响应或候选。当前目录不能认证已删材料完整。

| 来源 | 实际入口与有限停止 | 结果/剩余权限 |
| --- | --- | --- |
| SRC-OPENAI | 本日Research403/9686bytes；RSS200/759641bytes，独立解析1245项/缺pubDate0，UTC窗口过滤0项，原窗筛openai-window.json | 已检查当前RSS；403非内容覆盖，RSS不保证删除历史完整/全网0研究 |
| SRC-ANTHROPIC | Research200/279365bytes；NextFlight独立解码1chunk/0T-frame，172唯一dated posts；publishedOn相邻Nov25 11:05Z→Dec1 00Z | 已检查当前目标段，无当前目录窗内项，不授删除历史；原字段anthropic.html.metadata.json |
| SRC-GOOGLE-AI | DeepMindResearch200，真实Blog page4 native12s timeout、page5 native200/179714bytes，web原目录恢复Nov→Oct；具名developers Nov18与image verification Nov20实际原页日期；Google pubs2025/November Blog各12s timeout/0bytes，web未恢复 | 整组受阻；DeepMind成功不能代Google pubs。科学应用标题停止，不打开全附件 |
| SRC-META-AI | Research native12s timeout/0bytes；web0lines；Nov27官方域模型主题query有限第一页无原历史恢复 | 受阻；不记0研究、不重复空路径 |
| SRC-QWEN | 旧站200/17307bytes至Sep23，新Blog200/94344bytes动态无目标目录，web0lines；Nov27原域query发现具名TTS/VC，原TTS文日期Dec4，VC Dec22；TTS模型1128/2025-11-27名字段不授首公开 | 受阻；2025目标历史目录尚未恢复，窗后文章只身份/日期线索 |
| SRC-DEEPSEEK | 主页200/115583bytes真实Research More→本日news200/113863bytes；动态5、Research10题名，Nov27 Math-V2→Nov1 LPLB→Oct21 OCR；两个View all未穷尽。API updates只是changelog | 已检查有限Research；Math-V2具名日期潜力非0研究；原Nov27日字段无时区，不能补造完全落窗 |
| SRC-MOONSHOT | Blog200/13388bytes，本日解析26个dated文章，最新Nov7/6，无Next，导航不计 | 已检查当前有限目录目标段；不授所有删除历史 |
| SRC-TENCENT-HUNYUAN | Research200/6893bytes动态；本日浏览器实际“全部”中文11项2026Feb3→Sep22，未见Next | 受阻；浏览器此次成功不意味着2025恢复，不继承27失败/9条API；需本窗原历史段 |
| SRC-ZAI | 首查Research200/1276425bytes，真实page2 200/1397410bytes；12Flightchunks/1UTF8 T-frame，18唯一CMS IDs，hasMorefalse/nextPage3，最老createAt Dec7 16Z | 受阻；当前目录没有2025Nov目标历史段，不等于本窗0研究 |
| SRC-BYTEDANCE-SEED | GET type1/2、year2025/count20/desc/headerUS；p0各18，totals94/45、moretrue/next20；p20=20/18、moretrue/next40。保留未来pins，非pinned首项已Oct，下一页Jun→May/Feb边界停止 | 已检查有限目标段，不授年度穷尽；DA3 PublishDate1764172800000=Nov26 16Z，早于本窗起点，不取其全文/造本窗family |
| SRC-BAIDU-ERNIE | Blog主目录200/28100bytes，十条最新至Nov21；实际Next page2 200/20533bytes，六条Nov11→Jun30，无Next | 已检查有限16个dated条目，不授删除历史完整 |
| SRC-XIAOMI-MIMO | 主页200/58220bytes；八个dated Paper中Jan8→Oct21邻接；native已有全部十五Blog题名，无日期；Planck20:07:17本日原JS与作者回读确认moreBlogs/aria展开态绑定h，onClick仅u(e=>!e)，p.map渲染已返回列表，More/Show less本地toggle，不分页/补日期；Nov27原域query未恢复日期 | 受阻；Paper成功不代Blog必要历史日期段；无More普通待办，不扩所有Blog题摘/全文；原JS见[Planck raw](PLANCK_RAW_MIMO_NATIVE.js) |
| SRC-MINIMAX | EN12/CN13 dated目录跨Dec23→Oct27；Tech200动态15行，llms.txt原raw52物理行文档索引；由实际链接恢复techblog.md200/829bytes，仅2026May13 Agent Team，停止窗外正文 | 受阻；独立Tech的2025历史未恢复，索引行数不当技术文章数、不授全组0研究 |
| SRC-ARXIV | 四窄提交查询27/7/12/12=58返回，55唯一身份；每组start0/max50，total等于返回、短页末停止；DC月338只查skip200/show50标题201–250，新增五个相关身份 | 已检查有界发现；关键词/词干不保证语义，submission区间不授公告日期，全月表不变全文队列 |
| SRC-STANFORD-CRFM | StructuredPrompt具名HELM PR3893触发；实际原PR JSON，created Sep27、merged Oct4；dspy-helm repo元字段创建Sep26 | 已检查具名旧integration身份/日期，不造本窗release，不扫描HELM全站 |
| 表外：[作者项目/代码](https://tracegen.github.io/) | MLPMoE具名gist API、TraceGen项目、Matrix具名repo API；有限一次必要日期恢复；Aragog/MemFine/Matrix具名搜索第一页 | 已检查身份恢复范围；creation/update/commit不是正文首次公开证明，不造代码新事件 |

## 查询与权限

四组原query完整保存在[fetch_window.py](./fetch_window.py)和`arxiv-*-query.json`：

- model：`(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:transformer OR ti:"mixture of experts")`。
- systems：`(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR ti:GPU OR ti:kernel)`。
- agents：`(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:agent OR ti:"tool calling" OR ti:memory OR ti:"context management") AND (all:"language model" OR all:LLM)`。
- multimodal：`(cat:cs.CV OR cat:cs.RO) AND (ti:"foundation model" OR ti:"world model" OR ti:"vision language" OR ti:"vision-language-action")`。

共同提交发现索引为`submittedDate:[202511251900 TO 202511261900]`，descending/start0/max50；不把该区间写成本日公开区间。实际58返回/55身份只是发现规模，词干命中不是主题或准入保证；没有新增失败探针。宽DC201–250只浏览相关标题查漏，不对338整月题摘/全文审阅。

Web实际queries与原响应保存`web-source-0..8.json`。0：DeepMind page4/page5、Google November Blog、Moonshot、ERNIE原页；1：原域/入口有限恢复，原响应保留其Source命令；2：具名MLPMoE/TraceGen/StructuredPrompt/DOPD日期搜索四条；3：DeepMind4/5、Google pubs、MiniMax Tech原页；4：原目录真实click72/74及Tech llms click0、MiMo原页；5：Google/Meta/Hunyuan Nov27与Qwen2025-11-27原域四条；6：四具名安全exact-v1 HTML；7：TraceGen/Aragog/MemFine/Matrix四具名搜索；8：Google image原日期与Math-V2官方repo。完整query与返回权限以raw为准，不把有限搜索无命中变必要原正文已检查。

Math-V2原news日字段、完整exact-v1、原DataCite已本日取；release API `per_page=5`200返回`[]`，raw README一次reset，web官方repo恢复。release空数组仅此接口未返回，不证明从未公开；submitted Nov27 16:01:22Z、Updated Dec1不证明first-public上下界。其训练验证机制潜力隔离而不是按数学标题关闭。

原56份完整精确v1题摘与DataCite字段保留[题摘](./exact-v1-abstracts.json)、[日期](./exact-date-fields.json)及每份abs/date raw。Submitted、Updated、Available、Created/Registered各按原权限：元数据处理/月份不证明公开下界/上界，常规20ET schedule也不补造09BJT精确公告。具名作者项目的News或原release完整落窗才允许采用。几份Available Dec按真实原字段保留，不按Nov提交倒填。

## 停点与重开

没有Weekly固定扫描，会议标签不构成本日按需发布触发。必要安全/纠错/反侧只读支持准入命题的threat、方法、对照和限制，见[有限筛选](./BOUNDED_CANDIDATE_FINDINGS.md)，不授全部方法/实验。

Google pubs、Meta、Qwen新站、Hunyuan2025、Zai2025Nov、MiMo Blog、MiniMax Tech为具名历史缺段。接受对应本窗原列表/官方事件才定点重开该行；不反复空路径，不授正面证据、Books、0研究或无遗漏。51潜力首公开不确定的精确重开位置为对应原公告/作者首次发布或完全落窗上下界，而非要求所有附件。20:35:05作者已同步root题摘/必要核心与Planck来源/六部分通过及MiMo本地toggle，研究普通0；[独立记录](SOURCE_DAY_INDEPENDENT_REVIEW.md)保留实际分工权限。当前缺段为终态保留，不支撑正面采用或无遗漏。
