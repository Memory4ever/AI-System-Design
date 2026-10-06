# 2025-10-19 实际查询、分页与有限停止

本日原请求时间UTC `2026-10-05T02:38:37.646414+00:00` 至 `2026-10-05T03:46:42.577487+00:00`；每次实际URL/body/header/起止/退出/http在同名`*.receipt.json`，网络原响应为`*.raw`。派生文本不是阅读证明；下述是实际读取的限定。失败保留真实错误，不把空体当无事件，不补造执行收据。另11:40前的四精确标题身份辅助搜索结果原样保存为[actual](title-identity-web.actual.json)，不是第一公开证据。

## 十四每日源

| 来源 | 实际原入口、范围与停止 | 结果及限制 |
| --- | --- | --- |
| SRC-OPENAI | Research403后RSS200；XML仅核Oct22 16:00GMT/Oct22 00:00/Oct21 17:00及00:00→Oct15 00:00邻接，见`openai-rss.raw`。diarize当前官方model/changelog由web实际读取；curl/model及两`.md`403留原响应。 | RSS可见邻界无Oct18条目，不代表Research历史完整。model当前core支持speaker/segment接口；官方changelog October段Oct29/24→Oct6/1，没有恢复diarize精确first-public，隔离该家族。 |
| SRC-ANTHROPIC | Research200，实际解码自身Flight hydration publishedOn，Oct29→Oct14→Oct9/6/3附近即停，`anthropic-research.raw`。 | 区分publishedOn与_createdAt/_updatedAt，未将整库存全文化。当前hydration可见段不是所有历史发布无遗漏。 |
| SRC-GOOGLE-AI | DeepMind Research200当前2026导航；旧publications请求timeout。作者`https://deepmind.google/publications/page/2/`404是错路径，仅过程。root独立web实际成功取得正确`https://deepmind.google/research/publications/page/2/`，页面265selected，日期邻接Oct30→Sep29，stop2of9、不取3–9，见[root FINAL](FINAL_INDEPENDENT_REVIEW.md)。Google pubs正确`?category=2025&search=language%20model`与October月Blog各两次max20/connect8实际约8s连接超时，web同原页失败。 | DeepMind正确分页的有限slice已由root实际核，不再用错误404冒真实分页受阻；265不是265题摘或本窗候选。Google Research pubs/月页仍历史切片受限，不由Blog替pubs，不授全史无事件。 |
| SRC-META-AI | Research原请求TLS exit35/http000，web原页为当前MuseSpark/Glimmer/Image0 shell。 | 原Research历史切片未恢复；有限official Oct18检索无可用原历史条目，不授零事件。 |
| SRC-QWEN | 首查qwenlm旧页；新Research自身模块/config `969.js`恢复真实API。旧`/api/page_config?code=research.research-list&language=en-US`500；同接口`zh-cn`200/60，`/api/v2/article/retrieval?type=qwen_ai&language=en-US`200/40。只核身份/date窗口邻接。 | 旧目录60条的邻接Sep24 04:00Z→Nov12 20:59:26Z，新40最早Nov13 04:59:26+08；未见Oct项，历史切片缺段。60不是UI渲染60，UI还有allowlist/本地分页；未把返回内嵌正文当已读60全文。不再把可执行配置恢复冒hold。 |
| SRC-DEEPSEEK | homepage→自身`/news/`，ownbundle独立Research31项；More本地slice首10/全31，不存在由首页壳推定的外部hold。 | 实际Research日期邻接Oct21 OCR→May14 V3 hardware；核日期/标题与分页机制即停，不逐篇31题摘。可见目录不授所有网站历史无遗漏。 |
| SRC-MOONSHOT | Kimi Blog200当前26标题/日期，邻接Nov7/6→Sep16→Sep5，无可见Next；Nov7 release的native href实为`/blog/posts/changelog`。本日真实取得`https://platform.kimi.com/blog/posts/changelog`200，实际只读L1–20：页发表于Nov7，更新日期Nov6→Oct27→Sep5。MoonshotAI GitHub200导航。 | 26是目录标题不是26全文；changelog可更新，发表日不等每项release日，未见目标窗heading不授全史无事件。不以org updated时间授2025 release覆盖，不扩全部repo/全年附件。 |
| SRC-TENCENT-HUNYUAN | Research动态首查200；实际CUA iab不可用、enabled browsers空。ownbundle恢复`https://api.hunyuan.tencent.com/api/blog/publicList`，POST`{pageNum:1,pageSize:20,renderType:0}`；Content-Type JSON，默认EN9/total9，加accept-language:zh得CN11/total11。org200核当前10/83repo概览及T1原README开头。 | 两语言当前API全部2026；displayPublishTime/publicAt不同，不互代first-public，不授2025历史。T1仅核2月Preview/3月基座文字身份，不授本窗日期或性能。有限目录恢复结束，不扩83repo或内嵌content全文。 |
| SRC-ZAI | Research首15，真实page2累积18；ownFlight hasMore=false/nextPage3，至Dec7。官方release notes实际日期17heading，邻接Dec8 GLM4.6V→Sep30 GLM4.6，读取其对应说明至边界即停。 | 不以首15当末页；当前目录及release notes在2025Oct历史缺段，不授全史无事件。 |
| SRC-BYTEDANCE-SEED | Research/Papers原入口及ownbundle；真实get_article_list_v2，order_desc=true/count20，query/publish_year/research_area/work_team均空。type1加x-tt-locale:US，total242；type2 total115。 | type1 token0/20/40/60/80，真正停止为token80非pin **BJT Oct22/21→Sep22**；type2 token0/20，真正停止为token20非pin **BJT Oct23→Aug21**。Oct9/Sep9的pin不是排序停止。has_more仍true，不授total全量已读；后取得type1token100/type2token40/60仅留过程，不续120/80全年。 |
| SRC-BAIDU-ERNIE | Blog原页显示2/2，实际page2 200；Nov11/7→Oct16 PaddleOCR-VL→Sep12 PLAS→Aug14→Jun30，页末Prev1/2无page3。 | Oct16明确在前窗之外，仅有限原list日期浏览；不采用该旧事件到19，不扩所有repo。 |
| SRC-XIAOMI-MIMO | homepage ownasync6159 Paper八日期字段，2025May12/Jun4/Sep19/Oct21及2026Jan8/Feb3/Mar13/Jun29；More只是slice展开。 | 本日Oct21→Sep19日期邻接，没有把More当历史分页。无日期Blog不补造first-public；可见段不授全网无事件。 |
| SRC-MINIMAX | 原EN12 ReadMore、CN13阅读更多；EN首历史Oct27 M2，CN Oct27→Jan15 MiniMax01；独立Agent Tech Blog实际May13 2026。原页给`/docs/llms.txt`，本日一次真实`https://agent.minimax.io/docs/llms.txt`200，redirect至agent.minimax.cn，实际只读index，含techblog/agent-team及changelog链接。 | 两语言和Agent各自有限核；llms是当前index，无目标历史日期，未打开其全文附件。目录缺段/未来条目不授2025历史无事件；M2仅邻界路由，不声明全网首公开窗外。 |
| SRC-ARXIV | 下面四主题窗口查询、五类start0/max12标题补检及四精确相关标题身份恢复；官方availability实际阅读。 | 完整AB60/标题另3，不是日公开数。Fri/Sat常规无announcement只限制常规批次；提交/后续发表/索引日期不授首公开完全落窗。 |

## arXiv实际查询

统一发现切片`submittedDate:[202510180100 TO 202510190100]`，UTC值；只是发现条件，不是首次公开窗口。`https://export.arxiv.org/api/query`，start0/max_results25/sortBy=submittedDate/sortOrder=ascending。原请求字符串已在`arxiv-<theme>.receipt.json`，对应Atom原件保存：

- model：`(cat:cs.CL OR cat:cs.LG) AND (ti:language OR ti:transformer OR ti:foundation OR ti:MoE)`，实际23/total23，停止首响应。
- system：`(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:inference OR all:training)`，实际8/total8，停止首响应。GPU偏宽只作线索，经题摘贡献筛选，非整个GPU队列。
- agent：`(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:agent OR ti:retrieval OR ti:reasoning) AND (all:LLM OR all:language)`，实际20/total20，停止首响应。
- multimodal：`(cat:cs.CV OR cat:cs.RO) AND (ti:vision-language OR ti:VLA OR ti:multimodal OR ti:world-model OR ti:diffusion)`，实际11/total11，停止首响应。

五类有界官方标题补检：`cat:<cs.CL/cs.CV/cs.DC/cs.PL/cs.IR> AND submittedDate:[202510180100 TO 202510190100]`，start0/max12/ascending。原export CL/PL/IR timeout、CV/DC429；alternate`https://arxiv.org/api/query` CL/CV/DC/PL429、IR200/total8。只在IR浏览八标题；已有五家族，另三标题关闭，详见[筛选](SCREENING.md)。未沿整类offset继续，不称失败类别已浏览完毕。

四相关标题16333/16449/16384/16474已取得并读精确v1，不依赖搜索摘要判断。最初辅助query没有原样落盘，不回造；本次真实窄身份补检依次为`site:arxiv.org/abs/2510.16333 "RL makes MLLMs"`、`site:arxiv.org/abs/2510.16449 "TrajSelector"`、`site:arxiv.org/abs/2510.16384 "SemOpt"`、`site:arxiv.org/abs/2510.16474 "SCALAR"`，结果见actual JSON。前三恢复目标官方ID，SCALAR无目标有效结果；返回未来同名SemOPT及其他scalar旧文全部只当不相关检索噪声，不形成队列。SCALAR身份以本日已取官方exactv1为准。

## 其他实际辅助检索与按需

之前有限web query：`site:openai.com OR site:developers.openai.com "gpt-4o-transcribe-diarize" "October" "2025"`；`site:deepmind.google OR site:research.google "October 18, 2025" language model`；`site:ai.meta.com "October 18, 2025" research`。搜索不授日期/实验权限。先前web输出未另存原JSON，这里只记录实际query和结果限制，不伪称保有原响应。OpenAI官方model当前core与changelog已读，Oct18社区帖子仅发现；Google/Meta未恢复历史必要正文。

GitHub仅为注册每日源必要概览/T1定点辅助，不是每周release扫描。未触发新的MLPerf/HELM/OpenReview等会议整站；poster/comments不自动触发全部评审附件。arXiv HTML精确v1优先，UTAP HTML404后仅必要PDF；正文可得不等代码已核/复现。终态保留及定点重开见日报§5。
