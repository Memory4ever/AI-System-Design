# 2025-09-19 原入口与停点

窄恢复：完整重读当前合同/路由及本日停点后，仅补`https://qwen.ai/api/page_config?code=research.research-list`。本日独立curl单次20秒上限HTTP200/57428bytes，原qwen-config-recovery.raw为60配置全部有date，只有限筛UTC `[2025-09-18T01:00:00.000Z,2025-09-19T01:00:00.000Z)`，0命中；两侧原date Next `2025-09-10T20:00:00.000Z`、TTS `2025-09-21T20:00:00.000Z`。到夹窗即停，无60项正文队列、不继承别日覆盖、不重扫已恢复月标题。

作者Tesla。本日默认窗口09/18 09:00～09/19 09:00+08，独立重读适用合同/来源/ROADMAP及月度路由，当前无既有本日停点。只写本日README和sources；不继承其他日候选、准入或覆盖结论。

本轮原入口各单次8秒上限，RSS/指定API20秒；顺序执行，保存原响应。来源实际结果和停止条件在请求后补入，不以本页计划当覆盖。

## 实际来源请求 12:44～12:56+08

原请求顺序：OpenAI Research403→官方news/rss.xml200（1247条，按本窗UTC09/18 01:00～09/19 01:00过滤无匹配）；Anthropic Research200，Next字符串JSON结构解析172唯一publication，原publishedOn过滤本窗无匹配。Google DeepMind/Research Pubs/2025/09月页各8秒超时，web补开真实月份页12标题已至09/11；并实际打开Sensible/TTD-DR核心与DIVE publication。Meta reset35，严格Sep18 primary域名search未返回；不授整个历史零事件。

Qwen首页200有Sep23→Aug19连续博客停点；Kimi200到Sep16/5跨下界；DeepSeek首页200且准确`https://api-docs.deepseek.com/updates/`200，实际正文连续Sep29、Sep22 V3.1-Terminus→Aug21 V3.1跨下界，不把主站/updates404路由当可用。ERNIE首页及page/2均200，第二页9/12PLAS→8/14FastDeploy，停止。MiMo官网200 Paper8条包含Sep19Audio→Jun4，date-only事件另核，当前Blog无历史完整性保证。

Hunyuan Research200动态shell，正确API POST `https://api.hunyuan.tencent.com/api/blog/publicList` body`{"pageNum":1,"pageSize":100,"renderType":0}`200,totalNum9，实际最早displayPublishTime1770090898（2026年），不授2025覆盖；browser恢复在本执行环境原先已失败，技术路由限制复用，不复用别日内容。ZAI Research/page=2均200，Next blogsItems18 hasMore=false,nextPage3；数组非排序，实际min createAt=`2025-12-07T16:00:00.000Z`，不能用末项Dec21授覆盖。

Seed两官网页面200；API`/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true`200，15条/total49/has_more=true,next20；按ArticleMeta区分置顶：非置顶Oct22T16Z→Aug20T16Z→Jul14T16Z，已跨本窗下界，停止不追全49；置顶Sep8T16Z亦窗外。type1同参数200,total94,has_more=true但无sub_article_list，不计零。MiniMax三入口200：英文12条最早Oct27；中文实际13条含Jan15（跨本窗，无本窗条目），Agent TechBlog只May13 2026一篇；不把当前页当全历史保证。

arXiv第一主题API（export.arxiv.org/api/query）：12分类CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA与title主题language model/LLM/transformer/diffusion/world model/vision language/GPU/agent/quantization/kernel/collective/MoE/RAG，submittedDate[202509171800 TO202509181800]，start0,max200,submittedasc；20秒timeout28零字节，不计0。第二main API系统主题DC/AR/PL/OS/PF同date,max100，10秒301后timeout零字节。官方`/list/cs.CL/new?date=2025-09-19&show=2000`10秒仅452425/1380237字节，date参数并未恢复可审历史日头，不计公告证据。月`/list/cs.CL/2025-09?show=2000`25秒2164807/3438218字节；独立30秒retry2724222/3438218字节，均原样保留、不能计2000全读。只浏览其中完整出现的ID14500～15500段62标题；ID范围不决定公开日期。相关/含糊标题补精确v1题摘，不将整月剩余条目当队列。

本日API失败实际触发HF19页19标题恢复，仅作身份：17相关/含糊v1完整题摘（06216关闭），2明确领域标题关闭。全部v1需原公告/先发上下界；submitted不当公开。额外月段题摘与判断见FIRST_BATCH后续记录。

MiMo身份恢复误试`2509.14727v1`虽200但不是由官网链接确定的Audio身份，不作为本日证据/计数；随后primary检索准确身份为12月2512.23808，与9月先发分开。正确官方Blog来自GitHub链接`https://xiaomimimo.github.io/MiMo-Audio-Demo/`，不是猜测的MiMo-Audio-Blog404；原错路由保留。本日README历史20上限API实返5commit，最早`9bc65b003c18`09/19T00:48:29Z，下一`3b278795224c`01:05:50Z；commit日期不自动授repository first-public。
