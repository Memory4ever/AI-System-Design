# 2025-11-15 有限来源停点

作者Planck；实际检查2026-10-04，窗口BJT [Nov14 09:00,Nov15 09:00)。本记录只支持以下实际入口/切片，不支持全站无遗漏。raw-web-00～11保留真实web调用结果；各GET/POST原始文件的`.request.json`保留URL、参数、执行时间、状态和响应头。动态浏览器本日实际inventory返回空列表，未沿空路径重试。

## 每日14来源

| ID | 实际范围、结果与停止点 | 限制与精确恢复 |
| --- | --- | --- |
| SRC-OPENAI | Research及fresh RSS 1245条按UTC窗过滤，仅Ireland一条；[RSS](raw-openai-rss.xml)。Nov14 04:00GMT=BJT12:00；[核心raw04](raw-web-04.json)仅培训/合作，无系统机制，关闭。 | 当前RSS非删稿历史全集；出现本窗原始研究公告才定点恢复。 |
| SRC-ANTHROPIC | Research publicationList/Research实际171项传回数组，目标附近publishedOn Nov12 18:19Z→Nov21 14:32Z之间无本窗项；[目录](raw-anthropic-research.html)。115个2025字段不是论文数。另实际读[cyber原页](https://www.anthropic.com/news/disrupting-AI-espionage/)明确Nov14编辑说明，raw09：补report link，并纠正thousands requests/sec为总请求数/常multiple/sec。 | 留存Research数组可解析，不整组说历史不可读；目录不保证删除史。编辑只有日粒度、无时区/时刻，不能用Nov13原帖时刻替代修订。纠错须保留，不正面采用旧速度；取得官方修订范围完全落窗后重开该信号，不重读整份报告。 |
| SRC-GOOGLE-AI | DeepMind Research、Google pubs 2025条目发现入口及2025 Blog p1实际读到Dec18→Nov12；676条pubs仅入口，不变题摘队列。Blog Nov18后为Nov13/12，未见Nov14保留项。raw03/04留存正文；raw03另有未留query参数的empty结果，不据此重建精确日期查询。raw11实际AMD/Instella，撤销Google证据引用，不重试空检索。 | pubs未恢复当日公开列表；Blog当前p1不保证删稿历史。Nov13日字段不补时刻、不当本窗事件；有原始发布身份再定点恢复，不读676摘要。 |
| SRC-META-AI | Research本次web空正文；raw00；本窗精确官方域日期query raw03无命中。停止同一路径。 | 历史目录受阻，不记零事件；可读官方历史目录/具名原稿到达再恢复。 |
| SRC-QWEN | 旧官方首页实际5项，最新Sep23，越过本窗前边界停止；新Research实际HTML壳无历史列表，[raw](raw-qwen-research.html)，精确2025-11-14官方域query无命中。 | 新动态目录历史缺段；浏览器inventory空。取得可用当年目录页后恢复，不继承别日36条计数。 |
| SRC-DEEPSEEK | API Updates仅release边界。新增本日GET主页200/115583bytes，实际Research“更多”href /news/；沿原链接GET200/113863bytes，动态5/Research10题名及日期，目标邻接Nov27 Math-V2→Nov1 LPLB→Oct21 OCR。见[窄修原响应/执行](DEEPSEEK_SOURCE_REPAIR.md)。止可见目标边界，不读窗外正文。 | 两个查看全部未操作，不授隐藏/删除史或全部Research穷尽；Updates不替Research。具名本窗原始研究/修订或旧列表到达才定点重开。 |
| SRC-MOONSHOT | Kimi Blog fresh完整26个有日期标题，Nov7/6→Sep5及更早；raw01。停止当前目录末尾，无本窗相关触发。 | 26不是28；当前目录非删稿全集。只恢复具名本窗材料。 |
| SRC-TENCENT-HUNYUAN | 首查Research空；无可用浏览器。actual POST publicList page1,size20,render0：[raw](raw-hunyuan-p1.json)返回9条、均2026；不足20且仅9，不请求p2。松日期检索仅无关引用；精确Research 2025-11-14 query raw09无命中。 | 未恢复2025历史Research，不称9条穷尽2025。取得历史分页/具名原文后定点重开。 |
| SRC-ZAI | 首查Research，实际hashed page JS识别`page`参数及hasMore。p1 15项，p2 actual blogsItems18、hasMore=false、nextPage3，[p2](raw-zai-p2.html)；18项createAt非排序，均Dec7及后或2026，停止p3。[release](raw-zai-release.html)实际Dec22/11/10/8后Sep30，无Nov14保留字段，不替Research。 | 不把其他RSC字段createAt计成条目，不能从无November推断2025无研究。历史Research仍受阻，未扩GitHub。 |
| SRC-BYTEDANCE-SEED | actual 2025年type2/1,p0/20,count20,order_desc/headerUS四响应：[blog0](raw-seed-blog-p0.json)、[blog20](raw-seed-blog-p20.json)、[paper0](raw-seed-paper-p0.json)、[paper20](raw-seed-paper-p20.json)。blog18/18、total45；paper18/20、total94；均has_more=true、next20/40。pinned未来项隔离；非pinned p0最晚Oct22/21 16Z，p20已至June17/19，停止40。 | pinned不当按时序边界，has_more保留；旧日期边界只说明实际返回切片，删除/变更目录不保证召回。 |
| SRC-BAIDU-ERNIE | 中文Blog p1最早Nov21；实际p2六条Nov11/7→June30，显示1/2 prev，无继续next；raw03/04，停止p3。 | 无本窗保留项；当前目录历史限界，不当全网零事件。 |
| SRC-XIAOMI-MIMO | fresh首页8论文有日期、15Blog标题无日期；论文2026→Oct21/Sept19/June4/May12。Ohm2026-10-04T19:33:10+08:00实际GET官方native chunk `https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js`，成功25389字符；moreBlogs展开态/按钮aria绑定h，onClick仅u(e=>!e)，p.map渲染已返回列表，More为本地toggle而非分页，展开不补日期，见[独立原核记录](DAY_INDEPENDENT_REVIEW.md)。作者此前entry JS发现/blog/，GET200却为Dec16 MiMoV2Flash单篇，不是历史目录；只读身份/日期，[raw](raw-mimo-blog-route.html)，停止猜路由。 | More已核，无普通分页待办；undated Blog历史目录缺段，取得带日期Blog索引或具名本窗官方原文后恢复，不全读15篇。 |
| SRC-MINIMAX | fresh英文12、中文13保留项，Dec23→Oct27边界，中文版多Jan15；[英文](raw-minimax-en.html)、[中文](raw-minimax-zh.html)，无分页。Daily Agent Tech不是按需：本日另actual fresh GET[原Tech](raw-minimax-agent-tech.md)和所供[真实索引](raw-minimax-agent-index.txt)，仅1条2026-05-13，停止当前索引，不读窗外全文。 | Agent Tech必要2025段未恢复，来源组受阻，不写未触发/不适用；两普通目录有限已查不授历史无遗漏。 |
| SRC-ARXIV | 四组窄主题12分类，start0/max100，training51/inference6/agent12/multimodal10，未去重，均未满100停止start100。submitted字段仅发现。本月旧路径404后按实际abs月链接修正canonical；仅09700～10699相关ID切片109标题查漏，不全月题摘。三批36精确v1完整题摘实际读，[筛选](ARXIV_SCREENING.md)。新增真实历史Fri14公告页first50/78与2025官方规程存档，仅对照已有ID，16吻合、未扩AB；真实next的本日CDX空后停止。 | [Ohm](FIRST_INDEPENDENT_REVIEW.md)通过16项保守范围，注册上界撤销。16项作者必要Evidence/Books判断完成；其余19潜力日期终态隔离，PALMS范围关闭无日期请求。不支持无遗漏、正面证据或Books。 |

## 按需与表外

本日未观察到清单内MLPerf/HELM/harness、MLSys/OpenReview/USENIX当年本窗相关正式批次，或JAX/TRT-LLM/llama.cpp/TorchTitan/Kubeflow/llm-d/Gateway/Kueue/DeepEP/DeepGEMM/A2A重要release/RFC的具体触发。不进行常规全站扫描。论文comment的AAAI/WACV/ICLR等后续accepted字段不是本窗conference batch。

表外必要证据只用[Salesforce Echoing相关Blog](https://www.salesforce.com/blog/agent-to-agent-interaction/)Nov25身份、[NVIDIA MusicFlamingo项目](https://research.nvidia.com/labs/adlr/MF/)Published Nov03身份、AMD Instella March05/Long June11/Math Aug09原始发布线索，作为精确家族日期/重要差额检查，不扩扫机构。

arXiv当前36条metadata轻量信号实际读完：[raw](raw-arxiv-current-signals.xml)。没有条目comments明示withdrawn/erratum/correction；这不是全版本史无纠错保证。Instella v2 Nov14 02:08:46Z在窗内提交但标题/版本号不证明公开或重要改动；Harli v2 Nov19、其余晚修订隔离，不能用最新摘要覆盖v1。后续具体修订信号出现只重开依赖它的判断。
