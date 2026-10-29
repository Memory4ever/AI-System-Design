# 2026-03-15 补充窗口有限来源停点

作者supp_mar15；执行2026-10-11 09:36–09:45 BJT；只补2026-03-14完整自然日，旧09→09窗口不动。原README已原文冻结SUP_ORIGINAL_README_20261011.md，旧候选0/原§4三关闭连续保留。适用AGENTS、Research/Report合同、Prompt、Daily/arXiv来源路由、ROADMAP及本日原材料均实读。未从Weekly/月度候选推断本日，不读其他Daily。

## 来源有限恢复与复用

- OpenAI：本日V3_PUBLIC_DIRECTORY_FIELDS的RSS已含3/13–3/16实际pubDate切片，仅3/16 SAST；这份历史字段覆盖新增03-14自然日，只复用此切片，不声称当前Research全历史。无需重开SAST正文。
- Anthropic：本轮浏览器Research10卡/See more同页后，root指出同URL HTML嵌入publishedOn历史字段可恢复。一次curl只投影公开日期+slug并去重，实际174唯一对、March9行（BJT03-06/03-13/03-24/04-01）无03-14，本日原值见SUP_ANTHROPIC_PUBLIC_FIELDS_20261011.json。有限公开字段提取不是读取174正文队列；主Research当前嵌入历史切片已恢复，原H1不再隔离不可得，不推删除历史。AlignmentMarch5及Abstractive旧v1有效关闭仍复用。
- Google：本轮Pubs实际1–15 of11612，选择只有year/Title，不支持公开day；March Blog12卡的3/16→3/12邻接复核仍在。DeepMind page3本轮打开当前24卡，复用本日原3/17与3/10具名header。Research精选/Pubs日级论文历史仍缺；不读年度全部论文。
- Meta：本轮Research0行，正式publication入口Internal Error；有限可用Blog原page1/2非严格日期切片仍只支持自身可见范围，不授全论文来源零。未捏造browser失败或继承他日browser结论。
- Qwen：本日旧public safe40项实际字段完整读过，2/16→3/19邻接覆盖03-14自然日，复用身份/入口/可核字段，不将40篇全文队列；未授未公布分页total。
- DeepSeek：复用本日V3_SOURCE_STOP明确Research10/News5可见切片2/25→6/24、12/1→4/24；旧日期关系覆盖新自然日，不外推删除项。
- Kimi：当前官方Blog本轮打开，复用本日19可见条目2/9→4/20邻接，身份入口一致。未把旧platform止2025当无研究证据。
- Hunyuan：本日原public11/11 safe字段完整读过，2/13→4/23邻接与发布字段无03-14；原静态失败已由公开API恢复，不重复代码考古，不授删除历史。
- Z.ai：复用本日Research15卡与GLM-5-Turbo /155已独核core关闭，仅新增窗口排除关系：header3/15不据此反改旧处置；无公开新增机制不打开新附件。
- Seed：本日原type1 page20的18/total82 next40有限2/25→3/26切片完整读过，原display νTNS3/15范围EX不动。新type2/year2026/page0/count100/ascending US locale再实际返回同14/total19/next空/has_morefalse，2/16→4/1邻接且返回无03-14。其余5项仍精确隔离，不授19/19。SUP_WEB_RECOVERY只记录公开api web入口恢复失败，实际curl US响应成功，是不同请求不能混为失败。
- Baidu：复用本日Blog10可见卡2/6→4/15邻接，覆盖补充自然日；不外推其他历史修订。
- MiMo：本轮首页Paper8（3/13→6/29）、Blog15无日期标题；/blog再次实际旧12/16单篇不是archive；HTML有限日期字段检索未恢复Blog历史（结果只有公开CDN资源，不扩静态bundle）。缺03-14 Blog日期slice，未读15篇正文。
- MiniMax：本轮英文Blog与本日英12/中13跨窗邻接复用，不新读正文。Agent Tech本轮从原heading变为三张有日期卡：2026-09-19/09-22/10-08，都窗外；llms.txt当前54行仅3条同名文章，无March历史日期slice。不能把“当前三卡”提升为全部历史为零；缺口仍隔离，旧“仅heading不可读”状态不再当当前事实。
- arXiv：四主题API本轮恢复。SUP_API_*保存精确query与完整安全title/id/submitted/latest字段，系统121/learning76/multimodal27/agent108，各start0/max200且返回=total；332为未去重的跨组元数据行，不是本窗论文或摘要review规模。Submitted UTC3/13 00→3/15 00只是缓冲；当前latest不是精确v1。月列表show2000实际web结果仅开头片段，skip800/show200 cachemiss；没有全月浏览、逐项题摘或附件队列。official advanced search当前明确announcement filter只有year/month（实际HTML447–458/554），不能恢复逐日公告日期。失败错误day路径不再请求。availability只作常规排窗背景；未授全部作者原发0。

新入口原证：SUP_LIMITED_DIRECTORIES_20261011.txt、SUP_RECOVERY_STOP_20261011.txt、SUP_WEB_RECOVERY_20261011.txt。多页web返回可能只显示页header，不能把Total lines当实读正文；MiMo实际Paper8/Blog15单页全文原件见SUP_MIMO_DIRECTORY_20261011.txt，MiniMax Agent三卡有日期单页原件见SUP_MINIMAX_AGENT_DIRECTORY_20261011.txt，Seed US curl安全14行/total19原值见SUP_SEED_BLOG_FIELDS_20261011.json。本日旧有效safe字段与V3_SOURCE_STOP各自保留原执行日期，不冒称全部新抓。语义复核待SUP_INDEPENDENT_REVIEW_20261011.md。

## 具名初筛与日界限制

SUP_ADMISSION_20261011.md记录3个潜在增量+2科学应用EX。12529v1/13423v1/13426v1只读完整题摘与当前history/轻量修订说明，均只有Submitted，无本窗可核first-public；旧DataCite+schedule派生3/16、3/17、3/17仅辅助，不能据其自动公开日归属。必要日期slice或原始作者event到达才定点重开，不评分、不准入、不深审，不影响本窗其他可执行项。未见三潜力当前原页撤回标记；12529后来v2是窗外，不无差别审v2。

12567完整v1题摘为预训练TabPFN材料AL应用，12694完整v1题摘为酶反应注释应用，按ROADMAP当前AIforScience暂缓具体范围关闭；未从关键词直接推增量。12694初次多页仅header不是访问失败，补单页AB成功。二EX无可见撤回/纠错header，不穷追不影响处置的日期；原文科学任务可能有价值但本项目不回收。

最终确定新增候选0、旧候选0，Books0；未写共享Books、LS或索引，未stage/commit/push。作者将六来源历史slice与三具名日期门精确隔离，不支持正面Evidence、Books或无遗漏；非作者review_mar15_16首校、14来源/六部分DAY及Anthropic同URL174字段/March9窄增量均实际通过，普通可执行待办0，正式README已同步完成。完成态validator曾指出§5缺终态保留项字样，已按合同补足，不改工具；最终V3通过、15localrefs/6新JSON有效、原窗口/连续§4保持、限定cached/unstaged diff-check无输出。源缺口到达后仅重开受影响材料，不接其他日期。
