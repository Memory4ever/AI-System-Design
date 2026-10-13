# Sep21 补Sep20自然日：来源边界

作者Schrodinger；实际执行2026-10-12 BJT。只Daily14组/实际触发原件；不扫Weekly/全年/别日队列。请求URL、HTTP/transporterror、UTC、bytes/SHA见各`SUP_*.request.json`，对应`.raw`完整保留；200partial/403/空body都不当成功覆盖。早期TLS失败逐入口正常curl有限恢复，不关验证、不执行网站代码。

## 实际入口与停止

| 来源 | 本日实际范围和停止 | 局限/恢复条件 |
| --- | --- | --- |
| SRC-OPENAI | Research403→RSS urllib/curl前两失败，独名retry200/784414bytes，XML1287items按pubDate换BJT自然日。Sep22合作→Sep17scheming夹Sep20，无匹配，停止feed，不审窗外正文 | RSS未收录内容不保证召回，不能全网零事件 |
| SRC-ANTHROPIC | Research TLS失败→curl200，Next结构174唯一slug publication。实际Oct3→Sep15两条→Sep5，Sep20无publishedOn匹配，停止该目录 | 原旧Sep26夹窗说法只属旧快照；新实际停止Oct3/Sep15，非整个工程站 |
| SRC-GOOGLE-AI | Google月页新urllib/curl/retry三次timeout；本日旧`GOOGLE_SEPT.raw`实际重读12 datedcards，Sep23→19→18→17/16/12→11，仅复用旧快照日期切片。早期category=2025未验证year选中、TLS/curl失败；注册/pubs/独名本地timeout后web首切片实际恢复1–15/11612、Year filter2025计680，未选中2025、年级字段不证day，停止首页，参数恢复失败详见下文。DeepMind新正确Publications p1/2各30datedcards，p1止Nov4未跨、p2Oct30→Sep18DIVE首次跨下界→Mar28，停止p2元数据，不读窗外论文 | Google2025筛选未成功、日级字段及月快照更新限制精确保留，不称全源不可达。必要Sep20历史日级event/修订快照到达定点重开，不扩46页/全2025 |
| SRC-META-AI | Research TLS/curltimeout，另官方Publications实际curltimeout；限定official域Sep20研究query首返回无可用primary。旧META.raw只有title不作新成功目录 | 当前必要历史研究入口未恢复，不是无研究/0候选证据；收到主题相关Sep20原列表/具名event才重开 |
| SRC-QWEN | 注册qwenlm.github.io新200迁移提示及Sep23→Aug19夹窗；跟当前qwen.ai Research空壳→官方page_config200完整60date对象，新BJT Sep22Omni/TTS→Sep11Next两侧，无Sep20，停止config单页 | migration/list未收录事件不保证召回；date是原UTC字段按日换算，不设小时门 |
| SRC-DEEPSEEK | 注册主页新200及updates TLS失败后curl200；日期Sep29→Sep22→Aug21跨下界，停止日期，不读更晚机制/普通PR | 未收录独立GitHubevent不保证召回 |
| SRC-MOONSHOT | Blog TLS失败后curl200，26项可见单页，Nov7/6→Sep16首次跨下界→Sep5，停单页，无Sep20项 | 不以Blog等全GitHub发布；后续具名原event再定点恢复 |
| SRC-TENCENT-HUNYUAN | Research first TLS失败后curl空壳200；本日浏览器visibility不支持→不带options自动review超时→工具允许一次retry仍timeout/kernelreset，无DOM。官方公开API POST page1/size100/renderType0新200，code0/list9/total9，最早displayPublishTime对应2026Feb3，当前新版单页停止。具名SRPO官方README实际News Sep8 paper/checkpoint/inference、Sep12training，未见Sep20event | 当前9/9不是全部历史。不得继承旧11/11或他日浏览器success；需可核Sep20历史全部列表/具名原发布，相关缺段隔离 |
| SRC-ZAI | Research初查TLS失败、curl200但transfer-timeout部分body161896；不当完整首15。真实page=2新200 Next blogsItems累计18、nextPage3/hasMorefalse，最早createAt 2025Dec7T16Z。另注册new-released新200当前有限8日期，最早Sep30，停目录 | createAt展示发布日期与createdAt CMS2026字段分开；18累计恢复不保证Sep20历史，原局限精确保留 |
| SRC-BYTEDANCE-SEED | Publications首查timeout/partial→Research注册新200；实际API默认type2 15/49/type1缺数组105bytes，发现curl语言头漏传后只修本日helper、独名explicit-US恢复。US2025token0：Blog18/45，next20/moretrue，非置顶Oct23→Aug21首次跨；paper18/94，非置顶Sep22ByteWrist/MEF→Sep2PXDesign首次跨。停止token0，不沿next20扫描旧月库存。前默认paper-next20只1JuneSwiftSpec并已停止，不能称完整覆盖 | 默认与US是具体请求差异，不是站点一直外部缺数组。固定目录日级无项仅该切片，未收录event不保证召回 |
| SRC-BAIDU-ERNIE | Blog TLS失败后curl200，follow真实page/2/200末页。p2六项Nov11/7、Oct16、Sep12→Aug14→Jun30，只有previous/1of2；停止完整两页，无Sep20 | 只注册Blog的日期切片，不代表所有独立代码event |
| SRC-XIAOMI-MIMO | 首页新curl200：Paper8datedcards，Oct21→Sep19→Jun4；Blog15项无date字段。按实际script src/main t.p+t.u/route恢复8557+6159 async JS，More只是8+7同15array本地toggle，不是网络分页，停止这有限切片。一次错路径Nuxt及两次漏async-prefix404作为恢复错误保留，后来真实7920/25477bytes200 | 新Blog日级历史不可由当前无date15项恢复；旧MiMo-AudioSep19时区缺口历史冻结，不传播为新hour门。已具名Sep20原event才重开 |
| SRC-MINIMAX | EN新curl200及?page=2新200各h3 datedcard12，完整序列相同，止2025Oct27，不当真实分页。CN新200有13card，Oct27→Jan15夹过Sep20。Agent TechBlog新2003篇date均2026Sep/Oct（非footer年份），llms.txt新200只当前3techblog路径，停索引，无目标历史entry；不读取2026正文机制 | EN动态历史缺段/CN稀疏切片/Agent历史完整性保留。一次仅/news/anchor计2是错误selector，不使用该值计datedcard或Coverage |
| SRC-ARXIV | 新官方availability200实际读排程，Sep20自然日无常规batch，但非异常/他站先发证明。12注册分类四主题API start0/max150、submittedSep20BJT仅发现：49/23/35/48，114unique，全部response本页足总数无more；不是114首公开。宽命中按题义收窄，105unique精确v1全AB、9明确范围title止；不114全文/Books。新advanced表单实际字段后，announced_date_first+Sep20→21、CS/crosslist、model/system/agent/multimodal同义OR查询size50各200noresult，止各首页；只是这些query，不正面覆盖所有公告或用空结果给P判outside。当前latest comments轻撤回唯一SKILL-RAG20377v2，currentabs已确认paperwithdrawn，不采用 | 需官方Sep20BJT首公开/异常批次或已具名作者原发布日证；Submitted/announcement年月/索引date均不替代。显式无常规batch不消掉institution源/必要ordinary |

## 已触发的有界补检

仅首返回页、可核查询（执行见本聊天web调用，不把索引片段当原Evidence）：`site:arxiv.org "20 Sep 2025"`按language/transformer/GPU/agent与diffusion/worldmodel/kernel及retrieval/RL/safety等主题补检；`"September 20, 2025" model/LLM research`；中文目标日混元/智谱/Seed；Meta/GoogleResearch/DeepMind/MiniMax official域目标日查漏。结果的二手日报/SAM旧更新/音乐/广告与MiniMax用户space不是official研究原件，未采用索引日期或扩为池。仅回具名作者稿/项目：RelRepair、Challenging、PLLM、PING、SRPO等，见FIRST/AB/MIN_CORE；no HF固定扫描/周源触发。

具体原日期/家族恢复：SCAN作者项目200无原公开日；MANZANO官方Apple当前publishedJanuary2026只发表元数据，不迁Sep2025first；DiffusionNFT官方GitHubactivity web可见initialbranch/assetsSep22（本地staticraw没有完整timeline），不能凭commit时间证明paper首次；Shift找到官方May29ArcticBlog与July稿同机制，Blog本地403/web原字段可读、July精确v1全AB实际已读，尚必要first/delta事件处理，不把名称相同当已审重复或Book已有覆盖。AIPsycho出版方curl403/webrobotcheck，comment称August发表不是已独立确认日期；保留具体原出版日需求。SFT admin-overlap原AB/新§4/5形成恢复差额另见MIN_CORE，不扩2024旧论文全文。PING v2 XML真恢复和行政修订关闭，未采用旧first的正面研究结论。

## 普通停点

Google注册入口参数纠正（2026-10-12 BJT）：先前`/pubs/?category=2025`仅失败请求，未验证year选中，表中“2025入口”不可作成功筛选。实际新增`SUP_curl-google-pubs-registered_20261012.request.json/raw`为注册`https://research.google/pubs/`连接timeout/0bytes；随后web原入口真实恢复，首页有Year过滤器（2025计680），结果1–15/11612，条目元数据只年/venue，未选中2025，不研究更晚正文。必要`?year=2025`与原`?category=2025`web恢复均不可访问，停止首页，不扩46页/年度题摘；本地连接失败与web成功观察分开。原件web调用`turn4400view0`及参数失败`turn4401view0/1`可在本线程复查，非本地raw成功。日级历史/实际year筛选仍不足，精确保留，不写“Google全源不可访问”。

Sources有界首查/必要恢复与停止、Shift局部及最终集合已实际独核，Anscombe完整六部分DAY§15已读回通过。研究普通0，剩完成态窄FINAL；105题摘/具名core有效层不重读，98窄P日期和历史缺段为终态保留，不全读、不支持正面Coverage/Evidence/Books或无遗漏。没有Books写入或actualowner覆盖判断，不称0事件或全站覆盖。前文家族/准备停点只保历史，当前以README及独核§15为准。
