# Oct25 有限来源差额

## 1. 自然日与原有效层

仅Oct24完整BJT自然日，不继承前日Source成功。原本日SCREENING/FETCH/RECOVERY/EXTRA、Peirce FIRST/FINAL按入口/字段/命题复用；旧Research/Googlepubs/Meta/IAB失败不重试，不legacy/catchup。当前原目录不授全历史或first，不读未来正文/扩全年。

本日own `openai_rss.raw`1245条实际XML按BJT Oct24重新过滤，**0条**，只单RSS这个有限结果；旧Research403是必要原历史缺段，报告应受阻而非把feed0当Research已全检查。没有新的具名OpenAI正文队列。原Anthropic本月publishedOn3/6/9/14/29/目标Oct14～29邻接有效，止本目录/原域内query首屏；不等全站召回。Google原DeepMind8当前News/6pub与OctoberBlog page1十二标题、Oct27～Oct23邻接/页1of2有效，不读未见页/未来body；pubs正确category/search原18秒curl/web失败仍受阻，不第三次抓。Meta原Research18秒失败/两原query首屏保留，不重执行或宣0。

## 2. 本日own Qwen当前字段恢复

本日原 `qwen_new.raw` 确切引用 `https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/969.js`；本日已有main/Research route依赖44467与type=qwen_ai/language调用，未猜接口。本轮独立GET [969](SUP_QWEN969.js)/[headers](SUP_QWEN969.headers)200/10114，实际module44467明 `/api/v2/article/retrieval` 与 `research.research-list`、39759明page_config code：

- `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`：[原40](SUP_QWEN_ARTICLES.json)/[headers](SUP_QWEN_ARTICLES.headers)，200/4781799。
- `https://qwen.ai/api/page_config?code=research.research-list`：[原60](SUP_QWEN_CONFIG.json)/[headers](SUP_QWEN_CONFIG.headers)，200/57428，本次默认英语title；不充中文配置或lang误请求。

实际全100 id/path/title/date白名单读取：CONFIG的id本身是slug，真实没有path字段，不将打印None当身份缺失；ARTICLES id为UUID/path为slug。按slug归并93身份/7重复：DeepResearch、SAPO、ImageEdit2511、ImageLayered、OmniFlash20251201、TTS1128、TTS-VC。UTC/BJT同一eventdate分责，2025目标邻接Sep24Max→Nov13DeepResearch，没有Oct24目录字段，不授全史零事件。

实际读40的extra.date与content仅head published_time白名单，未来body/introduction未读；17冲突：ImageEdit2511 Dec23/Dec22，VLembedding2026Jan08/Jan07，TTS0115 extra2026Jan22/body2025Mar24，Image2512 Dec31/Dec30，MaxThinking Jan26/Jan23，CoderNext Feb03/Feb02，3.5Omni Mar30/Jan07，Image2 Feb10/Feb07，Scope Apr30/Apr29，3.7Plus Jun01/May21，LiveTranslate May19/May11，3.7 May20/May16，AgentWorld Jun23/Jun22，Image3 Jul21/Jul16，3.8Flash Aug26/Aug03，3.5 Feb16/Feb14，3.8Omni Sep18/Sep14。非列明2025者为2026字段，保每个原口径，不由extra覆盖body；无一支持Oct24原发布。止两个caller/必要route，不扩所有chunk/旧站，历史受阻。

## 3. Hunyuan / Kimi / Z.ai独立有限尾段

Hunyuan原本日EN9/全部2026有效。另own `https://api.hunyuan.tencent.com/api/blog/publicList` POST `pageNum=1,pageSize=200,renderType=0`、accept-language zh：[JSON](SUP_HY_ZH.json)/[headers](SUP_HY_ZH.headers)，200/442610、total11/list11。实际全id/title/customUrl及publicAt/publishedAt/displayPublishTime，转UTC均2026；id100061 Hy3preview显示Apr22UTC16=BJTApr23，publishedJun24/publicJul05，不互当created/updated。原EN九≠ZH十一，两者都不证明2025不存在；只字段不读futurebody，历史受阻。

Kimi原本日26带日期入口=25文章+11/07聚合，org10of42当前非历史的有效层保持。own [native](SUP_KIMI_CHANGE.html)/[headers](SUP_KIMI_CHANGE.headers) `https://platform.kimi.com/blog/posts/changelog`200/14815，完整article实际读：页published2025Nov07、段Nov06/Oct27/Sep05/Aug01/Jul30/Jul17/Jul11/May20/May06/Apr07/Feb17/Jan13及更早2024；Oct27 CLI/docs/cache事项不是Oct24，0916–1015是活动区间不当原发布。止native，不开未来模型正文或追org旧commits；必要历史缺段受阻。

Z.ai原本日page2累计18、hasMorefalse/next3/末Dec07有效。另本轮实际官方 [release目录](https://docs.z.ai/release-notes/new-released)八title/date：2026Aug26GLM5.3Flash、Aug18GLM5.3、Jun16GLM5.2、Apr07GLM5.1、Feb12GLM5、Jan14GLMImage，2025Dec22GLM4.7/Sep30GLM4.6。只读目录title/date，不采用页面未来摘要宣传/不点未来body或全Docs。目录不补October原缺段，仍受阻。

## 4. 独立MiniMax / 其余本日有限层

MiniMax原EN12/CN13 title/date有限层有效，Agent原May13单项不当未变字段复用。本轮own一次 `https://agent.minimax.io/docs/techblog`：[main](SUP_MINI_AGENT.html)/[headers](SUP_MINI_AGENT.headers)200/225926；显式 `https://agent.minimax.io/docs/llms.txt`：[完整索引](SUP_MINI_LLM.txt)/[headers](SUP_MINI_LLM.headers)200/8404。实际可见main三日期/title/path：2026Oct08 Agent监工困境/coding-agent-workflow-and-skills、Sep22试验场/coding-agent-eval、Sep19Code开源/minimax-code-harness；canonical agent.minimaxi.com，modified2026Oct08另责。完整llms显式索引三Tech链接，不进入futurebody或全Docs；原main含script/style未作为文章研究内容。当前三项不授2025不存在，历史受阻。

DeepSeek原本日own/news五News/十Research目标Nov01～Oct21，ERNIE page2六末条Nov07～Oct16，Seed US/type1/2各18/token0/total94与45/next20/hasMore目标PaperDec02～Oct22、BlogNov27～Oct23，均原本日有效字段和有限停止，不重抓/不把置顶当严格时间排序或全集。Seed已知Oct23独立Blog日不合本轮Oct24，只排该介绍事件，不排全部familyartifact；原论文潜力资格另责。

MiMo原本日8Paper日期/15Blog标题、index/4752两bundle dated metadata最旧Dec18/19及2026有效，More非历史分页，必要Blog历史仍受阻。未见新的具名current/release差额，不扩全年或为证明不存在盲扫。上述有限目录/首屏不认证全球first-public或无遗漏。

## 5. 停止与交接

十四到期来源均有本日具体入口/停止与失败权限；arxiv主题/具名最低域及current见[本轮包](SUP_ARXIV_20261015.md)。未触发按需会议/框架release发现扩扫，具名HTML不变全部P方法队列。必要历史/公开日未知不支持正面证据、Books 或无遗漏断言；可接受原机构历史公告/date-only研究发布/明确重要版本差额，只定点重开对应身份/入口，不重全Source或追秒。

root通过内部协调确认，持久记录见本日SUP_INDEPENDENT§6：本日Qwen60/40全必要date/headmeta、HY11三时间、MiniMax独立目录/索引、Kimi全文/RSS1245自然Oct24真0、原DS五News十Research和ERNIEp2字段已实际读，通过这些有限字段层。最终本包归并可直接比对，不再请求重复原字段；不把字段通过等同全历史Coverage或日级DAY。研究/准入有效层不重，无本日Books锁/写入/共享State/index修改；外部Dec23 Ch75窄锁不触碰，保护全部cached/并发改动，不stagecommitpush。
