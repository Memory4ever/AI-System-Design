# 2026-01-27 有限发现与筛选

执行日期2026-10-04，目标仅BJT[2026-01-26T09:00:00+08:00,2026-01-27T09:00:00+08:00)。当前官网目录不是历史完整性证明；下列空搜索仅记录有限补检没有提供线索，不宣称0研究/无遗漏。正文与独立复核仍以精确事件原文为准。

## 原始主题查询与停止

arXiv API查询按submittedDate:[202601221900 TO 202601231900]，标准公告所对应提交slice，不把submitted当public时间。模型查询：(cat:cs.CL OR cat:cs.LG OR cat:cs.AI) AND (all:"language model" OR all:transformer OR all:"mixture of experts")；sortBy=submittedDate/sortOrder=descending/start=0,20,40,60,80,100/max_results=20。有效JSON为model-*.json，total103，第六页3条到尾。系统查询限定cs.DC/AR/PL/OS/PF且language model/transformer/GPU/inference/training（system.json，total6，到尾）；多模态限定cs.CV/RO/IR/MA且foundation/multimodal/world model/VLA/diffusion/large language/retrieval augment/agent memory（multi-0/20.json，total38，第2页18条到尾）。三个slice是发现线索且跨分类先去重，不是147个当窗新研究或全文队列。失败/截断Atom不用于覆盖。

补检cs.CL月列表只浏览16979～16276附近相关标题以检查新命名机制；2168条月目录不变成逐项摘要/全文队列。日期选中项逐一核abs/v1 history+DataCite原字段，后者只恢复身份/上界，不证明实验。特殊late announcement、早正文artifact和重要修订不能由这个标准slice保证召回，保留限制。

## 每日来源停止与限制

| ID | 实际入口/有限停止 | 原始线索与限制 |
| --- | --- | --- |
| SRC-OPENAI | openai.com/research及news；site:openai.com "January 26, 2026"、模型/训练/推理主题定点搜索 | Jan26 Maggie Hulce业务访谈不贡献机制；ChatGPT voice release说明为功能/质量事实无新机制。当前目录+补检不构成完整历史目录。 |
| SRC-ANTHROPIC | anthropic.com/research与Jan26/模型Agent主题定点搜索 | Jan15 EconomicIndex窗外；未得到本窗机制线索。当前入口未证明完整历史。 |
| SRC-GOOGLE-AI | deepmind.google/research、research.google/pubs及research.google/blog；Jan26定点主题补检 | 年度/分类目录只线索，未逐年/逐页扫；本窗没有可确认事件线索，历史缺段隔离。 |
| SRC-META-AI | ai.meta.com/research无法提取正文；site:ai.meta.com Jan26主题定点补检 | 空提取/空搜索不能证明0命中，历史目录缺段隔离。 |
| SRC-QWEN | qwenlm.github.io重定向qwen.ai，旧页2025文章；qwen.ai/blog无法提取；Jan26定点补检 | 无可确认原事件线索，动态历史目录未恢复，不证明无遗漏。 |
| SRC-DEEPSEEK | deepseek.com当前页面；api-docs.deepseek.com/updates官方完整可读changelog | 所列更新从2026-04-24跨至2025-12-01，本窗没有列出更新。范围仅该changelog，不覆盖未列研究。 |
| SRC-MOONSHOT | platform.kimi.com/blog可读25条最新至2025-11-07；MoonshotAI/kimi-cli exact release 0.88/PR681 | Kimi0.88正式published_at落窗；只核改变HTTP header ownership的patch，不遍整repo。K2.5 repo Jan30 created不是模型首次证明，模型历史入口仍缺。 |
| SRC-TENCENT-HUNYUAN | hunyuan.tencent.com/research动态页无正文；子线程browser一次超时，root独立IAB一次36.8秒超时并kernelreset | 无法核“全部”历史范围，终态隔离该必要目录缺段；不能说空目录或0研究，不继续无界重试。 |
| SRC-ZAI | zhipuai.cn/zh/research官方可读research目录 | Feb2 GLMOCR→Jan19 GLM4.7Flash→Jan13，停止到Jan19并核夹窗；仅此可见research目录无Jan26列项，不代表所有artifact。 |
| SRC-BYTEDANCE-SEED | seed.bytedance.com/en/research选择目录Jan27 Post-LayerNorm→Dec2；public_papers第一页20/242；Jan26定点补检 | 242条只route非13页队列。Keel作者Jan27页与arXiv19895v1提交Jan27T18:58:46Z不能唯一证明本窗作者首公开，精确日期保留。 |
| SRC-BAIDU-ERNIE | ernie.baidu.com/blog/zh官方首页 | Jan29 PaddleOCRVL→Jan15 ERNIE榜单夹窗，停Jan15；只此博客列项，不覆盖无独立时间artifact。 |
| SRC-XIAOMI-MIMO | mimo.xiaomi.com papers/blog | papers Jan8 MiMoV2Flash→Feb3 HySparse夹窗；blog少量未有精确本窗时间条目，不证明全部GitHub事件。 |
| SRC-MINIMAX | minimax.io/blog14条、minimaxi.com/blog重定向minimax.cn、agent.minimax.io/docs/techblog15导航项 | Jan27 M2her→Dec23 M2.1；M2her核心机制已读但展示日/JSONLD00Z不足精确首公开时刻，跨本窗边界日期保留。 |
| SRC-ARXIV | 上述有限3主题slice+相关官方标题补检；必要项exact-v1/identity metadata | 列表分页已到尾；特殊late、未匹配术语或早artifact不能从标准公告推定保证。不把143左右去重线索误称候选数。 |

按需触发仅MCP2025-06-18 transport规范（为Kimi兼容变化）；不扫描任何Weekly来源。DataCite、官方GitHub history为选中项身份/首公开定点恢复，不是新增广源扫描。

## 实际关闭与隔离

冻结家族36篇exact-v1+Kimi0.88，共37；12深入/25标准必要证据完成，4整合+4已有覆盖+29仅报告经本日独立Gate。准入句与证据见报告/evidence.md及review-16946.md；原CORD已在原36中，只改处置而不增加候选。窗口推定由官方[availability](https://info.arxiv.org/help/availability.html) Sunday20:00 Eastern下界2026-01-26T01:00:00Z与各DataCite created上界组成；二者含义不能互换。history/version有后来修订的只用来识别，不替代本事件v1。当前官方abs/HTML未发现这些采用命题的撤回/删除信号；没有为证明这一点遍历全站。

贡献关闭：16964 AgentDrive单域驾驶bench题摘未新增受控评价盲区/边界；16596成熟allpairs critics组合无独立失效条件；16278合成数据非单调仅既有diversity/difficulty/prompt实例；16280四类调用error/三invoice工具无新增runtime评估机制。后三项决定性core已读，材料保留，非时间/成本删池。其他宽目录条目没有自动进入完整题摘/全文队列；范围明确的科学应用不按通用Data/Agent映射绕回主线。

独立重开：16946 LogitMatch原题摘关闭遗漏连续input-span约束机制；单项DataCite created Jan26T02:41:42Z、history Jan23T18:03:10Z与官方批次支持本日，准入2+1+2=5不变，INFER-SGLANG Ch51具体接口gap定点深入并整合，root必要源与POST通过。见review-16946.md与identity-16946.json；不重开全列表。

首公开关闭：LongCat2601.16725官方旧commit PDF实际第1/9/10页已承载streaming/multiversion/controller/PD/CPU KV；Jan23官方body早于本窗，arXiv收录不产生新首次事件。原证据见longcat-history/early-pdf.json；不冒充别日报已处理。

日期保留：2601.17111与2601.17086标准下界Jan26T01Z而created分别Jan27T03:42:15Z/03:41:42Z，使区间跨09BJT截止，只能日期未唯一确认，不自动授Jan28owner。MiniMax M2her和Seed Keel同样不以“Jan27”日显示造时刻。恢复只需同事件作者首次公开timestamp/官方公告或可信artifact前后界，不需整历史全文。
