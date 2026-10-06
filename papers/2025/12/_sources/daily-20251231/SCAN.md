# 12/31 原始窗口、检查与停止点

检查2026-10-02T19:20:06+08:00；窗口[2025-12-30T09:00:00+08:00,2025-12-31T09:00:00+08:00)。启动与恢复独立重读AGENTS、研究合同、每日来源/arXiv段、Report合同、Prompt、ROADMAP及本日停点；启动无旧README/checkpoint。只逐源读固定原始历史邻接，不从前日结论反推本日。

## 原始历史目录按本窗独立比较

原值来自[25 DISCOVERY固定目录段](../daily-20251225/DISCOVERY.md#固定官方目录的原始邻接摘录)、[17 SOURCE_STOPS原始恢复](../daily-20251217/SOURCE_STOPS.md)、[25 ROOT原始恢复段](../daily-20251225/ROOT_ADMISSION_REVIEW.md#可恢复的-blog-范围补正与最终结论)。只复用观测，不继承25日Gate。

- Seed type1 query article_type1,publish_year2025,count20,page_token0,order_desc=true,headerUS：实际18,total94,next20，两置顶Dec15/Dec2后Oct21至Jun25；type2采用root最新HTTP200实际18,total45,next20，五置顶Dec24Prover1.5/Dec18Seed1.8/Dec16Seedance/Dec2GRRL/Nov27DA3后混合下降至Jun25。分别比Dec30至31，在过窗邻接停止；非严格全局排序。旧15/49不同次响应不复用。Prover日编码1766505600000不授准确上线/历史正文，相关25日期保留由root协调，不挪成本日。
- DeepMind正确/blog/page/4/24项Feb26至Nov25，December最新Dec23为旧事件年度回顾；后GemmaScope2 Dec19T12Z/Genesis Dec18T19Z/Flash Dec17T16Z/audio Dec12T17Z/AISI Dec11/UK Dec10/FACTS Dec9。GoogleResearch2025Blog Dec18/15至Nov12。AnthropicAlignment Dec19Bloom/Oracles、Dec16faking、Dec12replication、Dec8masking至Nov。恢复Blog不升格Google publications年库676与AnthropicResearch10项/失效分页为完整日覆盖。
- Zai Research page2累计18且无更多，Dec21/10/9/8/7；release Dec22至Jan14分别比较。DeepSeek updates Dec1至Apr24；Moonshot26 Blog Nov7/6至2024、持续changelog Nov6→Oct27，无已见December模型项；CLI0.69只定点复用已读精确差额关闭，不借0.68评分。
- Meta publications page3 Jan2→Dec26 AdvGame→Dec18watermark/Dec16SAM，page4到Dec16/12/01，Blog2 Dec18/16；混入旧置顶不是全局排序。ERNIE两页Jan8→Dec23/Dec9；MiMo Paper8 Jan8→Oct21、Blog15日期空；MiniMax英文12/中文13 Jan27或28→Dec23→Oct27、Agent Markdown只有May13/2026。均按本窗比较，不逐项深读窗外产品/科学库存。
- OpenAI历史必要分页原始403、RSS403及有限官方替代仍不可恢复；AnthropicResearch同URL十项/SSL EOF；Qwen迁移动态空和公开组件有限恢复；Hunyuan公开all API11/11全2026、最早Feb3，MiMo Blog历史路由日期空。上述只隔离不可恢复部分，不把当前目录/搜索空当2025零事件。本日December30,2025 research限定OpenAI/Anthropic/DeepMind/ResearchGoogle辅助空；2025-12-30 model限定Qwen/Hunyuan/MiMo排除community实际恢复Qwen2512，另Tencent-Hunyuan官方GitHub定点发现HY-MT1.5，两项核心已实际读见OFFICIAL_CORE。

## arXiv 主题与有界分类补检

官方advanced查询submitted_date_first=2025-12-29至2025-12-31、cross include、size200/start0、order=-announced_date_first，title OR三组：large language/LLM/MoE/Transformer/GPU实际99；vision-language/world model/vision language action/diffusion/multimodal63；agent/RAG/memory58。均实达无pagination-next；语言组大输出截断后单组重取完整。组间交叉不求和成唯一候选数；分类all参数过宽命中physics/领域应用，以题摘语义收窄，不把宽库存当逐项正文队列。

官方[cs.CL月长表](https://arxiv.org/list/cs.CL/2025-12?show=2000&skip=0)1302身份，定点HY-MT entry858相邻850–870（0-based）相关标题；首次title解析空后纠正single-quote HTML属性，实际读21标题。恢复LoZA、CEC-Zero、RISE、DATAMASK、FIGR等8新相关身份完整v1题摘，不扩整月。月表只身份，非日公告。catchup/cs.CL/2025-12-31?abs=True实际Cache miss；announced_date_first日参数不受支持，不再反复无效接口。

2025[原始holiday](../ARXIV_DATE_RECOVERY.md)明确Dec29 14EST至31 14EST接收且接受延期至Dec31 20EST=Jan1北京09，应是Jan2窗起点；不能给逐ID赋此时刻，也不把整天公告挪到9点以前。本窗右端Dec31北京09不包含；Submitted/API版本日期都非first-public。新86个2512相关题摘+HY-MT精确v1已读，70 potential/16关闭及HY-MT潜力另列；9个含糊关闭已必要原文核准重开，非因深审耗时删池。

跨年datehold仅定点已发现相关身份，不扩January库存；[13项完整v1题摘](DATEHOLD.md)已补完，10 potential/3关闭。HY-MT官方release API首20实际[]，不当未发布证明，不用commit代public时刻。普通扫描/已发现相关题摘/含糊准入补读待办0重新建立；后续是必要first-public/历史目录外部保留与非作者核验。保留项不正面采用、不评分、不进Books、不支持Coverage/Evidence/零遗漏/性能/安全保证；接受相应官方历史日分页或逐IDnew/RSS/可验证完全落窗首次公开范围，定点重开真实所属日。作者ready后交root唯一ownership，不等待日Gate。
