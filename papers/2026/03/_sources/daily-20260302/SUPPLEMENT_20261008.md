# 2026-03-02 增量来源补查原始记录

作者 supplement_20260302；实际检查2026-10-08T21:20:56+08起，补充窗口2026-03-01～2026-03-01。原README完整[baseline](./SUPPLEMENT_BASELINE_20261008.md)、原Source、候选/日期/评分/Books和原§4连续正文冻结；旧日期推导/周末公告推理/旧完成标签不当本轮新证明。旧有效审阅复用，只新增真实差额。新发现和判断融入原六部分，不建立替代报告。

## 14源实际入口、停止与边界

访问原件见[官方fetch](./SUP_FETCH_official.json)、[有限恢复fetch](./SUP_FETCH_recovery.json)；API见[五组查询](./SUP_FETCH_api.json)、[尾页/题摘](./SUP_FETCH_abstracts.json)。原HTML/XML/JSON均在本目录SUP_*；本节不是全覆盖或无遗漏声明。

| 来源 | 本轮实际入口和停止 | 结果与未检查范围 |
| --- | --- | --- |
| SRC-OPENAI | 官方news/rss.xml当前1255 item，按pubDate转北京时间仅筛Mar1自然日，0 item；停止feed末，不展开Index隐藏cursor | 有限feed已检查；不证明未列入feed或删除历史。原Index缺口冻结，需Mar1研究历史段官方归档/当时公告 |
| SRC-ANTHROPIC | Research HTTP200原HTML Publications日期段，相邻2026-02-25T20:02Z～03-05T19:59:21.508Z，Mar1无目录项 | 只对当前可见目录段；没有跨日全文/全机构召回 |
| SRC-GOOGLE-AI | DeepMind Research当前目录；复用root当前官方100-item RSS原XML(recordtime13:03:37Z，非精确请求时刻)，按pubDate转BJT Mar1为0；Google Research2026/03/?page=2真实第二页2/2，末段只有Mar6 SpeciesNet/Mar4 Bayesian reasoning；Pubs当前年级标题目录止首页面，非逐篇队列 | 原Google月p2访问缺口此次已恢复，能关闭该Blog可见段限制；RSS不替全部Pubs，Pubs首公开日仍外部隔离 |
| SRC-META-AI | Research HTTP200只提取title“Meta AI Research: Muse Spark, Muse Glimmer and Muse Image”，无历史目录；一次官方域Mar1精确日期补检无结果 | 受阻，壳/空search不是零命中；需Mar1 Research历史段/原始发布 |
| SRC-QWEN | 新Blog HTTP200可见text仅Qwen，无history cursor；一次官方域Mar1补检空；原小尺寸有效core/关闭理由复用不重读 | 动态Blog历史目录受阻；Qwen report是精确论文新发现，不将模型旧release自动当论文先公开 |
| SRC-DEEPSEEK | Research&News目录10项，相邻Feb25 DualPath～Jun24 V4；Updates HTTP200 ChangeLog相邻2025-12-01～2026-04-24 | 两个可见research/change段无Mar1，News隐藏ViewAll未展开；不授全站历史 |
| SRC-MOONSHOT | Kimi Research Blog完整可见19项，相邻2026-02-09 Agent Swarm～04-20 K2.6，停止可见列表末 | 当前公开Research段已检查，未见Mar1项；不读取窗外文章 |
| SRC-TENCENT-HUNYUAN | Research壳6893B；浏览器恢复一次67秒超时后止损；POST /api/blog/publicList pageNum1/pageSize1000，返回英文EN totalNum9/list9，核publicAt/publishedAt/display三字段，相邻Feb13 RLVR～Apr23 Hy3显示日，均无Mar1 | EN9可见段有限已检查，不证明CH历史/删除；三日期字段不互当首公开。CH目标自然日研究目录仍受阻；不复用旧CH11为本轮证明 |
| SRC-ZAI | Research全部当前时间排序相邻2026/02/21 GLM5报告～03/15 GLM5Turbo，读至可见列表及查看更多入口 | 可见目标段已检查，0目录项；不把查看更多后未读项授全历史 |
| SRC-BYTEDANCE-SEED | PublicPapers原页p1 1–20/242；唯一?page=3恢复仍实际p1 1–20/242，停止不继续13页；Blog与blog_publication返回壳；一次官方域Mar1补检无结果 | 目标历史research/blog段受阻，首页不证明零命中；没有242项AB/全文队列 |
| SRC-BAIDU-ERNIE | 技术Blog可见相邻Feb6 ERNIE5～Apr15 ERNIEImage，停止列表末 | 该可见Blog段无Mar1，不授所有Publication首公开 |
| SRC-XIAOMI-MIMO | Paper相邻Feb3 HySparse～Mar13 ARLTangram；Blog当前标题无日期/cursor，一次官方域Mar1补检无结果 | Paper有限可见段已检查，Blog历史日期目录受阻；不能按标题/更新时间归日 |
| SRC-MINIMAX | 英/中Blog相邻Feb14或Feb12 Forge～Mar18 M2.7，可见列表末；当前AgentTechBlog此次只两条2026-09-22/09-19 | Blog可见目标段有限已检查；TechBlog当前有日期仍不能证明此前页面删除/完整历史，原历史请求不授全覆盖 |
| SRC-ARXIV | 五个主线主题API submittedDate[202602280000 TO202603020000] start0/100上限，total104/10/54/103/43；model/agent尾页实际4/3，其他一页完。314原始记录去重214，40首次Submitted晚于Mar1 16Z无实际先前作者公告则关闭本次arXiv事件。剩余邻域相关标题择机制/含糊项，原4有效题摘复用，32新v1题摘；官方CL/DC月页各首100仅相关标题浏览，额外6具名v1题摘，停止无下一页 | Submitted仅发现不授公开日；月页只有month无day announcement。一次精确abs+官方month原入口恢复不给首公告日，各潜力精确隔离；不以ID年月/Registered/周末旧推导代替首公开。除具名实际38新AB，不称214/200全初筛；后续月条目不扩大 |

四个arXiv辅助search与四个机构官方域Mar1精确search，当前检索结果只有窗外2610.06973制造应用或空，停止一轮；搜索日期/空响应不作首公开或零研究证明。实际query为：`site:arxiv.org "March 1, 2026" "language model"`；`site:arxiv.org "2026-03-01" "inference" GPU`；`site:arxiv.org "Mar 1, 2026" "world model" OR VLA OR diffusion`；`site:arxiv.org "2026-03-01" agent memory retrieval`；`site:qwen.ai/blog "March 1" "2026"`；`site:seed.bytedance.com "Mar 1, 2026"`；`site:ai.meta.com "March 1, 2026"`；`site:mimo.xiaomi.com "2026-03-01"`。每条只本次返回结果，不分页续搜；网页搜索仅发现权限。没有每周来源扫描，没有其他年份/Live/缺失日。

## 差额准入与必要证据

38个新精确v1完整题摘身份和具体贡献链见[校准表](./SUP_CALIBRATION_20261008.md)。未进入当窗正面候选：潜力缺必要公开日期，先不评分、不读实验或为date全文、不Books。原4个旧具名身份的旧窗口/日期逻辑冻结，本轮不重建日期证明。所有新v1官方页轻量未见withdraw/deleted/erratum公告；不授完整版本史或安全保证。CurvatureWeighted当前API v3摘要收窄v1强支配/泛化claim，保留反证，绝不采用旧强claim。

root已实际全读原32精确v1题摘与AutoSkill一次core §3.4，DeepResearch9K具体EX通过；AutoSkill改为EX，见下。LoRA memory题摘贡献含糊，已一次必要v1结果/core§6/Q8–Q11及O/P：固定参数budget下oracle partition优势被实际routing削弱；确保正确模块召回仍N1→5合并递减，区别routing与composition错误，保有限潜力并不采数字。root已实际核LoRA差额与月页六个新v1完整AB，仅ActMem决定准入仍需一次core；已仅§3方法168–238读到NLLgate/负后果query二次召回的实际机制，见校准表，不把关联score当因果证明、不读实验绕date。最新38新AB、3必要准入局部core、36日期潜力、2具体EX、0确认新增/0Books；ActMem差额与DAY待验，不自行DAY通过。

明确EX：

- DeepResearch-9K 2603.01152v1：旧multi-hop转9K、Tongyi轨迹合成和支持既有RL/reward的框架加SOTA，没有实际新机制或修正数据/训练边界；不是benchmark名称/数据规模/缺date排除。
- AutoSkill 2603.01145v1：完整AB后一次必要core§3.4，query-only extraction、neighbor add/merge/discard、identity保留和versioned semantic union均为prompt中的成熟来源/去重纪律；没有新的冲突消解、反馈有效性条件、执行约束或效用反证。仅有一个具体维护流程不自动构成长久增量；不是缺日期/缺大实验排除。原core完整保存，未采其实验/productionclaim。

## 精确外部终态保留项与重开

已确认潜力但本次缺必要首公开日的精确v1身份全列于校准表，均不算零命中、不算确认当窗候选或Evidence完成、不用于Books/正面性能安全保证。每个身份已一次官方abs/月页日期恢复，不请求时分秒；替代为该精确论文/报告的官方首公告列表或邮件、可定位作者/project原文的首公开日期、官方归档。返回仅先核Mar1落窗/精确版本/同事件重复，再按实际分数展开必要证据；不是重扫整个month/year。公开日期证明不在此则保持外部隔离，不做正文绕date。

来源目录外部项：OpenAI Index、Meta、Google Pubs首公开段、Qwen动态Blog、混元CH历史、Seed目标research/blog、MiMo Blog、MiniMax旧TechBlog；需要Mar1目标历史段或该段原始带日期公告。GoogleResearch Blogp2此次恢复，不再保该已解决p2请求。限定替代和重开位置见日报§5，所有限制不支持全Coverage或无遗漏。

## 修改与验证界限

仅own本日README和本_sources，新原件不覆盖旧文件。Books/LEARNING_STATE/index/其他Daily不写、不stage/commit/push；工作树此前大量修改保留。报告六部分DAY非作者验收待root实际完成；格式/引用/冻结/diff检查在写后执行，不替语义验收。

最终非作者验收：root已实际核全部14来源有限停点/原请求URL时间分页错误恢复、全部38新精确v1完整题摘及AutoSkill/LoRA/ActMem三次必要准入core，并对baseline六部分增量逐段实核，DAY通过。最终36日期潜力/2具体EX/0确认新增/0Books，普通待办0。已同步本日报完成态；日期/目录外部保留不授Coverage/Evidence或无遗漏。原14Source行/旧window/原§4连续正文逐字冻结；V3、17有效本地引用、限定本日cached与unstaged diff/diffcheck写后复跑，不做全工作树clean声明。root总任务终检仍独立。
