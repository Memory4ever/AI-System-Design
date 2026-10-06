# 2025-09-18 原入口与停止记录

最新窄恢复：本日独立Qwen page_config/research-list单次20秒HTTP200原60配置，UTC17T01→18T01筛0，原`qwen-config-recovery.raw`；不借别日coverage。实际重读本日`minimax-cn.raw`可见13条至Jan15，Oct27→Jan15跨下界；原US12不是CN计数，撤回原“九月Blog未保留”过宽缺口，只授有限保留日期切片。

作者Tesla。本日窗口2025-09-17T09:00:00+08:00至09-18同刻；2026-10-06 12:12:13～12:13:17+08顺序curl，每普通入口8秒一次。原响应为同目录`*.raw`，超时零字节无文件，不编造正文。OpenAI403；Anthropic200；DeepMind/Google pubs/month/month2超时；Meta连接重置；Qwen/DeepSeek/Kimi/Hunyuan Research/ZAI/page2/Seed Research/public_papers/Seed两API/ERNIE两页/MiMo/MiniMax US/CN/Agent Tech Blog均200。Hunyuan正确POST publicList `{pageNum:1,pageSize:100,renderType:0}`200。

Seed实际URL `/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true`；type1替换同请求。真实15/49及94无列表。ZAI真实`/zh/research?page=2`，不假设page被处理，实际Next blogsItems18/hasMorefalse已核。Anthropic使用Next JSON字符串解析，不用标签/正则误作publication数组。

arXiv主题submitted `[202509161800 TO 202509171800]`，题名language model/LLM/transformer/diffusion/world model/vision language/GPU/agent/quantization/kernel/collective/MoE/RAG，start0,max200,submitted升序，20秒超时。第二窄系统查询attention/quantization/kernel/collective/communication/accelerator/MoE/RAG/retrieval/memory/compiler AND12注册分类，start0/max100同bounds，12:17:36实际HTTP429。停止反复API请求，未获有效XML不报0命中。原day path web cachemiss。

12:15:02 HF `/papers/date/2025-09-18`curl10秒超时，web实际19标题（18recovery0.json）用于失败恢复，不固定扫HF/不授窗口。CL月首次10秒传1529200/3438218 bytes后超时，保留partial；12:16后25秒窄重试成功`arxiv-cl-month-retry.raw`1–2000/2214。不把部分响应当2000已读；成功月列表仍只相关标题/新命名线索，非全文队列或公告日证明。

17个相关/含糊恢复身份精确v1原HTML于12:16:36～46全部200，完整题摘实际读；MedResearcher/AERIS领域暂缓不进队列。不以HF PublishedOn代原公开时间。OpenAI scheming原curl403、Apollo误旧Blog路径404原记录保留，web原新`/science/`及antischeming.ai成功；15541v1提交09/19不得抹掉09/17作者博客事件。SLED原repoNews2024公开+code，不被博客“now”改日。

本日web原记录18web0/1、core0、recovery0、specific、ids、final.json包含入口、关键正文及查询；严格源域日期查询空结果只作有限补检，不授来源历史覆盖。普通源实际Next结构解析：Anthropic172按UTC09/17 01～09/18 01无记录；Seed非置顶跨08/21和07/14后停止；ZAI累计18最早12月07终页；Hunyuan9全部2026。当前目录结果不能推历史无遗漏。

12:20后窄恢复：官方OpenAI RSS curl15秒HTTP200，1247item按本窗UTC过滤0。原scheming Blog `Wed, 17 Sep 2025 00:00:00 GMT`=09/17 08:00，明确窗外，原猜测日期保留撤回；转17日归属，不授其已审完成。主站DeepSeek updates本日20秒HTTP404，API文档Change Log20秒HTTP200，实际连续Sep22→Aug21越下界；原响应均保留。Apollo正确`/science/stress-testing-deliberative-alignment-for-anti-scheming-training`20秒HTTP200，保留apollo-correct；HTML未恢复带TZ日期。Google SLED原URL及www变体各20秒超时，RSS web失败、定点官方搜索仍只Sep17日期；保留18datecheck，未以无关SLED同名搜索结果作证据或队列。

Google月目录临界Sep18 Sensible Agent也定点读原核心与官方Pubs完整题摘，18sensible.json/18sensibleidentity.json。仅Sep18无TZ不能排除边界相交，保留what/how决策与两阶段确认的代价/打扰权衡潜力，不按10人关闭；不是扩大19日。CL月原HTML有title/h1/h2但没有历史日公告头，不将ID区段当first-public。
