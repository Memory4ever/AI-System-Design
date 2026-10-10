# 本日补查查询/停止记录

作者supplement_20260301，实际检查2026-10-08 21:20～21:30 +08:00。目标仅2026-02-28北京自然日。启动完整重读AGENTS、RESEARCH_CONTRACT、RESEARCH_SOURCES使用说明/每日/arXiv、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、ROADMAP；LearningState只查相关路由。baseline保存原报告完整正文；不重审有效OP1安全正文或Books，不继承旧Complete。

## 14源与实际停止

全部首请求身份/时间/URL/响应边界见SUP_FETCH_20261008.json与SUPPLEMENT_FETCH_20261008.py。200仅表示取得响应，不表示历史完整。新原件均本日SUP_*；不扫描Weekly/Live/其他年份/缺失Daily。

- OpenAI官方RSS单响应，按pubDate原时区转北京自然日：2/28仅旧OP1，去重，不增加家族；当前官方事件页通过web读取仅轻量检查显式更新信号，仍3/2分隔线，不重审原机制。原HTTP一次403、查询串替代一次403，不据403否定已有有效证据。
- Anthropic research单响应首10行到9/4，See more存在但没有可枚举历史，日期域首结果无目标新线索；停止该有限首段，D2维持，不由空搜授零事件。
- DeepMind research单首页，Google Research pubs?year=2026仅年级最新表，均不据首页/年份判落窗；实际复用root 100item RSS原XML（root记录时间2026-10-08T13:03:37Z，非本日精确发请求），本日查看100item，BJT2/27 NanoBanana2→3/4 FlashLite跨本自然日无feed项。feed不是Publications历史/删除事件目录；D3维持。
- Meta research网页取得动态shell无可读目录；日期域搜索首结果仅旧年个人页/Blog，不送全年摘要队列；D4维持。
- Qwen qwen.ai/blog动态shell，日期域首结果无目标新线索，不拿旧站2025库存代替2026；D5维持。
- DeepSeek /en/research实404后实际/en/news/恢复ResearchIndex10项（补请求2026-10-08T13:24:16Z），2/25 DualPath→6/24 V4跨窗口；单响应读到2025。ResearchIndex有限本窗段无条目，News隐藏ViewAll/API更新D6维持。
- Kimi /en/research重定向产品主页无research历史证据；实际/en/blog/恢复Research19项（补请求13:24:16Z），2/9 AgentSwarm→4/20K2.6，本窗段无条目；旧platform页不代替。
- 混元研究页单响应shell；本日POST实际endpoint https://api.hunyuan.tencent.com/api/blog/publicList，pageNum1/pageSize1000/renderType0，totalNum9/list9全en，显示2/13→4/23跨窗无条目。该EN9不证明CH历史。按照来源说明只读浏览器初建timeout；重建getState看到同URLpage1tab，再getTab timeout，停止（不发散nativeapps/登录）。旧CH11原件只冻结复用，不由当前EN9继承其完整性。
- ZAI research全可见日期段3/15→2/21跨窗，读至2025/12/09停止；不把GLM-5旧报告重审为本窗。
- Seed research可见1/27→4/11；public_papers响应首20、total242/page1of13。一次?page=80路由探针（13:29:56Z）仍相同page1，参数未恢复真实分页，不称已读80页/全部242；D9维持，宽库存不逐篇AB。
- ERNIE中文首页5/9至1/8可见，4/15→2/6跨窗，有限段无条目。
- MiMo Paper8项，2/3→3/13跨窗；Blog15项/More无日期历史，D10维持；NewMaterials研发明确科学应用仅标题退出。
- MiniMax EN/CN单响应可见目录读到2025，3/18→ForgeEN2/14、CN2/12跨窗无条目；AgentTechBlog只2个9月项，非历史证明。不统一双语日期、不把财报/活动当研究。
- arXiv官方availability日程/2026holiday实际单响应；无Friday/Saturday常规公告只作路由，不排除延期/非例行。四组SubmittedDate Feb28发现查询实际起止/词项/分类均在脚本与receipt：语言/学习69（start0,max50返50；start50,max50返19，末页请求13:24:14Z，即停止69），系统5（返5即止），多模态33（返33即止），Agent38（返38即止），跨源/分类去重103身份。仅相关题名读完整题摘，明确领域/科学应用停标题；16原始首提交字段转北京已03/01，所以该arXiv首次事件关闭，不造当窗公开日（不排除另有具名作者早发布）。旧月库存未重读AB、未送全文队列。45贡献潜力仅缺public日，当前abs一次有限恢复后逐项隔离；Social-JEPA当前withdrawn关闭，TraceSIR一次core定贡献。官定公开批次不能恢复，AX1维持。

## 辅助域日期搜索（有限首结果，不翻搜索分页）

四批、每源一query：OpenAI/index `February 28, 2026`；Anthropic `Feb 28, 2026`；DeepMind/GoogleResearch `February 28` `2026`；Meta `February 28` `2026`；Qwen/blog `2026-02-28`；DeepSeek `2026/02/28`；Kimi `February 28` `2026`；Hunyuan、ZAI/research、Seed、ERNIE/blog、MiMo、MiniMaxCN、MiniMaxAgent `2026-02-28`；MiniMaxEN `Feb 28` `2026`。搜索域/日期不严格：OpenAI返community用户贴，Meta返2025个人页，MiniMax返3/11活动回顾/space用户站。只具名身份查漏，不采用户站或索引为原证据。

唯一旧OP1原文web入口 https://openai.com/index/our-agreement-with-the-department-of-war/ 本日可见2/28页及3/2显式update；没有新的撤回/修订标记影响旧2/28范围。读当前更新信号不把3/2新条款回填2/28，也不使旧有效窄审重复计数。

MiniMax搜索命中[YC Hackathon回顾](https://www.minimax.io/news/minimax-ycombinator-hackathon-building-the-future-of-web)，正文实际3/11发布，2/28是活动日期，故窗外发现线索；活动支持与参赛数量，不具有模型/系统新增机制，不追全文。

## 普通工具恢复

初抓取脚本依赖bs4在系统Python缺失，尚未发网络请求即ImportError；按debugging技能定位依赖后换标准HTMLParser，复运行成功。未安装依赖、改环境或触及别日。HTML文本仅辅助读，原raw/XML响应保留。日期清单的只读identity-map首次把arxiv.org的字母v错分，修为仅split末段ID，清单45身份完整生成；没有修改源原件。


root准入校准实际核读原44潜力当前Atom摘要与原14组代表EX/TraceSIR摘要及Social官方撤回，非全部v1全文深审；RAIE领域EX撤销后作者一次精确v1方法core（14:03:33Z，§4.1.3～4.3必要式）确认动态region写入/扩张/新增/adapter路由潜力，随后一次abs日期请求（14:04:58Z）仍仅Submitted，纳入第45个精确外部日期保留项。root进一步实际核RAIE §4.1.3/§4.2式3–6/§4.3式9，认可窄潜力与日期隔离，不证明防遗忘/radius可靠；最终45潜力/其余13组代表EX、TraceSIR必要core、官方Social撤回、14源实际URL/分页stop及全部六部分DAY通过。新增确定0、Books新写0、普通待办0；相关core/abs本日原件保留，不遍历实验/版本，不授全覆盖/无遗漏。
