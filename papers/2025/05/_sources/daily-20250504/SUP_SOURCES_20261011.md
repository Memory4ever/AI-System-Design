# May04 实际来源切片与停止

只处理May03完整BJT自然日。以下请求均2026-10-11执行，具体UTC执行时刻、请求/最终URL与响应在同名`SUP_*_20261011.request.json/.raw`；不把当前页面、HTTP200、未读正文或旧完成标签授为历史召回。本文只是本日原件导航，正式README自包含各源边界。

## 14每日源

1. **OpenAI**：[RSS](https://openai.com/news/rss.xml)，`SUP_openai`，实际1287 item pubDate完整日期字段按BJT筛May03；邻接May02 sycophancy说明（08:00GMT即16:00BJT）到May05，无目标日item。完整所返回feed即停止，不catchup May02、不授已删除/未入feed的所有Research。
2. **Anthropic**：[Research](https://www.anthropic.com/research)，`SUP_anthropic`，实际publishedOn字段177处含重复，日期元数据完整核，邻接Apr28到May29，无May03日期项。不是177新论文或完整AB；当前目录返回终点停止，不扩参考论文/历年目录。
3. **Google AI**：DeepMind主入口及[Blog page6](https://deepmind.google/blog/page/6/)实际24月度item，其中9个May。为无日月份标签恢复9篇primary元数据（`SUP_deepmind-May-meta1..9`，308入口采用实际slash重试），datePublished为May20六篇/May14 AlphaEvolve/May06两篇，非2026 dateModified；page6已到April，停止，不继续全站。Google Research实际[May Blog归档](https://research.google/blog/2025/05/)9个日期条目May23/22/14/13/12/07/06/02/01，无May03；May02 Amplify原页日期只有官方日，不猜小时或跨日。仅必要日期/简介读，不把9篇全作研究队列。
   [Publications](https://research.google/pubs/)真实脚本`SUP_google-pubs-js`给search/category/page参数，实际`category=2025&search=`四主题：large language model共19（page1/2，止16–19）；inference11（止1–11）；multimodal14（止1–14）；agent37（page1/2/3，止31–37）。原件`SUP_google-topic-*`。这些是所返回年度题名/出版年份字段，不是May03的81唯一论文；存在跨查询/同题名重复及2026会议字段，未按年份反推首次公开，未逐项读全部AB/原稿。已读返回题名与入口日期能力，实际终页后不扩全年680条或更宽search；仍缺May03首公开事件切片，不能由有界年主题查询授当日无遗漏。
4. **Meta/FAIR**：Research实际200但当前Muse入口没有publication/datePublished历史字段（`SUP_meta-research`）；Blog实际[page2](https://ai.meta.com/blog/?page=2)→[3](https://ai.meta.com/blog/?page=3)→[4](https://ai.meta.com/blog/?page=4)。page3夹有Apr29但tail July31，未用非单调featured旧项提前停止。page4目标附近May21/14/13→May01→Apr29尾，已跨至目标前停止，不打开5；无May03日期项，仅题名/日期元数据，不读2026正文。三条官方域May03定点search为空只作辅助，不证明Research历史全空。
   **新必要入口实际恢复**：Blog footer给出[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)，实际逐个Next链接page1→7，每页24日期块：前12当前发布段共84元数据（page1 Oct02→Jul17,2026，page2 Jul13→Apr16，page3 Apr14→Jan02，page4 Dec26→Nov19,2025，page5 Nov18→Sep15，page6 Sep08→Jun13，page7 Jun11→May14/13→Apr28/25/17）；后12是2016–2021乱序旧条目，逐页日期已核不提前stop，也不作84旧论文队列。第7页当前段已经跨至目标前，实际next8未打开，无May03日期项。原件`SUP_meta-publications`及`SUP_meta-publications-page2..7`；按必要目标日期导航，未做跨年研究/全文扫描。这个具体可访问入口恢复后，H2原“缺Research历史入口”普通差额闭合；只声明所返回Blog/Publications切片，不授删除历史或每篇论文首次公开均等于目录日。
5. **Qwen**：[首页](https://qwenlm.github.io/)及真实[/page/2/](https://qwenlm.github.io/page/2/)，`SUP_qwen-page2`，July22至Jun27 TTS/Jun26 VLo/Jun05 Embedding到Apr29 Qwen3，无May03日期项；到目标前即止，不开3。TTS正文所提May22 API不是Jun27帖日期。只Blog切片。
6. **DeepSeek**：主入口/官方[changelog](https://api-docs.deepseek.com/updates)，`SUP_deepseek`，实际完整目录邻接Mar24→May28，无May03事件；止返回目录，不扫每个GitHub仓库、不授全部论文史。
7. **Moonshot/Kimi**：[Blog](https://platform.kimi.com/blog)，`SUP_moonshot`，26日期item，邻接Apr07→May06，无May03日期项；止目录返回，不遍历MoonshotAI所有项目。
8. **Hunyuan**：首查[Research](https://hunyuan.tencent.com/research)真实动态shell；浏览器必要尝试超时，随后通过实际JS（`SUP_hunyuan-{js,blog-js,api-js}`）恢复官方API [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)。实际POST`{pageNum:1,pageSize:1000,renderType:0}`，这是UI“全部”参数，不是猜全年端点。`SUP_hunyuan-public-list` code0、totalNum11/list11，displayPublishTime及publishedAt全部2026；11<1000且total=11即止。实际当前11不等May2025历史目录，未凭未来列表写不适用或零命中，缺May03历史研究事件。
9. **Z.ai**：首查[Research](https://www.zhipuai.cn/zh/research)，按真实More的`page`到[2](https://www.zhipuai.cn/zh/research?page=2)；返回18个累计条目最早Dec07,2025、hasMore=false/没有更多。实际page3同一18确认终点后停止，不能说3页54论文。官方[release notes](https://docs.z.ai/release-notes/new-released)实际8日期条目最早Sep30,2025。两入口均未恢复May03历史，未扩全部zai-org仓库，不能把未到窗口当零命中。
10. **Seed**：真实JS的`get_article_list_v2`、publish_year=2025/order_desc=true/count20；**type1=论文/ContentType0，type2=Blog/ContentType1**，原`blog0/papers0`文件名不决定类型。最初无显式locale原件保留；随后按UI真实`x-tt-locale:US`重取，五个`SUP_seed-US-type*-token*`请求记录header，ID次序逐项与原响应相同。论文token0/20/40实际18/20/19，total94但未读全94，末页May05 MxMoE→May02液态电解质科学应用→Apr25 ShadowKV（且末页到Mar22），已过目标止40，不请求next60；Blog0/20实际18/18，total45但未读全45，May12 Embedding→Apr23，到目标前止20，不请求next40。所有target日期元数据已读，无May03日期项；May02科学应用只由明确题名关闭范围，不读无关全文。未用UpdateTime2026或提交日期代替正文公开；只所返回US目标切片，非全locale/全站保证。
11. **ERNIE**：[技术Blog](https://ernie.baidu.com/blog/zh/)首页10条及实际[page2](https://ernie.baidu.com/blog/zh/page/2/)6条，page2为末页（仅prev、无next），最早Jun30,2025。全部返回日期/题名已核，无历史May段；真实终页不证明May时尚无来源，也不打开Paddle所有项目。
12. **MiMo**：[首页](https://mimo.xiaomi.com/)实际JS恢复Paper8与Blog完整15（含7隐藏More，不只可见8；`SUP_mimo-{content-js,home6159,home8557}`）。Paper最早May12 MiMo7B。Blog是15个列表身份，不是15个已验证日期：五个列表页frontmatter有日期（2026年的tool-call/Code/TileRT/inference及HSS Dec19,2025），另实际Flash原页header Dec16,2025；content中额外Safety Dec18并非这15列表之一。其余九个custom页面frontmatter无date，已逐个恢复真实列表给出的URL（`SUP_mimo-blog-meta{2,3,7,8,9,10,11,12,13}`，均200，仍无可提取日期），不从V2名称推公开日、不读未来核心正文。当前实际已验证日期至少早至Dec16，不能写HSS为最早。无更旧分页；`/blog/`请求实际显示MiMoV2Flash内容，不伪称目录。定点读取由Paper给出的[MiMo README](https://github.com/XiaomiMiMo/MiMo)，`SUP_mimo-github`，Updates May30、技术稿2505.07608，只恢复必要身份，不扫其他repo。未证明该模型首公开May12或Apr30；缺May03历史Blog事件快照。
13. **MiniMax**：[EN Blog](https://www.minimax.io/blog)12条最早Oct27,2025；[CN](https://www.minimaxi.com/blog)实际最终[www.minimax.cn/blog](https://www.minimax.cn/blog)，13条含Jan15,2025 MiniMax01与Oct27后的M2等。全返回日期/题名已核，无May03字段；26个“阅读更多”均13条单篇链接及其序列化重复，不是额外分页/待读26项；没有pagination/nextPage/hasMore控件。Agent Tech Blog真实3条Sep19/Sep22/Oct08,2026，仅日期元数据，不采用未来正文。止这些公开目录，不授删除历史/全机构召回，不因May无项把GitHub所有模型变成队列。
14. **arXiv**：见下节。实际发现与题摘已结束；必要May03官方公开批次仍不能恢复，不授Coverage或“当天无论文”。

## arXiv 主题发现、公开日期与列表停止

提交线索仅`submittedDate:[202505021600 TO 202505031559]`，完整覆盖May03 BJT对应UTC提交段；API分钟字段是发现条件，**不是小时公开门或catchup**。每个start0/max150、submission ascending，total=returned且<150停止：

| 路由 | 分类 | 主题同义表达 | 返回 |
| --- | --- | --- | --- |
| model | cs.CL/LG | language model、transformer、mixture of experts、foundation model、post-training | 38 |
| systems | cs.DC/AR/PL/OS/PF/LG | large language、GPU、inference、distributed training | 25 |
| agents | cs.AI/IR/MA/CL | language model、tool calling、retrieval augmented、agent | 47 |
| multimodal | cs.CV/RO/LG | vision language、world model、vision-language-action、video generation、diffusion model、foundation model | 22 |

精确表达式与执行UTC在`SUP_arxiv-{model,systems,agents,multimodal}`；132出现去重75家族，75完整当前/精确v1题摘已实际读，贡献闭合50P/24EX/1OLD。不是全类/全月库存、75全文或本日公开分母。

公开入口恢复：`/list/cs.CL/250503`404、短月2505的bounded请求400/404只是对应失败；**canonical [/list/cs.CL/2025-05?skip=0&show=25](https://arxiv.org/list/cs.CL/2025-05?skip=0&show=25)200**，`SUP_arxiv-category-longdate`，真实月2833总数，只浏览首25题名作入口能力核验（ID00001起、无公开日header）。它不是本窗官方公开slice或2833待办；日期粒度不支持识别May03后即止page1，不扩整月25→2833。长日`2025-05-03`实际400，同名request留存。

官方高级搜索May03→May03返回form错误end date须晚于start，**不是有效0命中**；页面明示announced date只支持年/月。错误field=arxiv的旧单ID请求也不计有效查询；以paper_id纠正后CHORUS唯一结果为originally announced May2025，Contextures旧稿为April2025（足以在May03前），不是submitted推定。具体50P再按paper_id OR分四批13/13/13/11，size50、无分页，actual returned与请求ID集合完全一致、每项仅May2025公告月；`SUP_arxiv-public-Pbatch1..4`。没有漏页或把May月级条件当May03。

缺口：需要May03 BJT首公开批次/可归日公告原件或对应家族作者第一次公开正文的日期；不能用ID/月、API published（提交）、PDF内部date或一般周末公告日程补造。先保留这50个窄P及必要身份反侧，原件到达只核具名项/相应主题slice，不能catchup邻日或全月补查。

## 辅助检索与表外触发

Web只定点检索arXiv具名01572/CHORUS、May03公告、Google May03/May归档、Meta May03、MiMo具名页与Adaptive DOI/标题。多数为空；Google May归档与AIRC非www PDF已回primary实际读取。空搜索/有界搜索不证明不存在，不用返回的其他月/年度结果启动新队列。AIRC出版PDF只触发04637必要身份，不产生新音乐论文候选。具体身份差额见[三项必要包](SUP_NARROW_EVIDENCE_20261011.md)。

以上明确历史缺段是目标事件/日期原件缺失，不是把全部未读官方目录叫外部停。已关闭24EX不额外追不影响处置的公开日；未确认50P当窗前不全篇投入/评分或Books。已完成来源有限入口工作可交非作者核，外部保留权限以README§5及[精确请求](SUP_DATE_REQUEST_20261011.md)为准。
