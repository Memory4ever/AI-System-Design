# 2025-05-01 来源增量补查

作者：主任务 root。执行日：2026-10-07。只拥有本日补查及共享进度协调，不改其他日期的作者文件。

## 冻结与窗口

用户明确要求只补遗漏、不调整已经进入 Report 的材料时间。补查前完整正文保存在 [原报告](baseline-before-supplement-20261007.md)，原22个候选的日期、身份、评分、有效审阅及Books处置保留。原精确窗口为2025-04-30 09:00:00至2025-05-01 09:00:00北京时间、左闭右开；当前正文的日期范围只展示它触及的两个自然日，不授权新增材料使用这两天。新增材料仅检查2025-04-30完整自然日，不创建缺失日报或Weekly，不stage、commit、push。

已读取当前AGENTS、研究/来源/Report合同、Prompt、ROADMAP、相关checkpoint；Books局部比较另读PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE及Ch66指定正文。旧完成标签只保存为历史事实，不代替本轮覆盖或验收。

## 实际来源与停止范围

原件和真实请求记录位于 [supplement-20261007](supplement-20261007/)。有request.json的记录保留实际URL、抓取UTC时间、HTTP与curl退出状态；超时无raw不冒充正文。额外Seed恢复使用实际`x-tt-locale: US`请求头，精确URL为`https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=<0/20/40/60/80>&count=20&order_desc=true`，响应及headers分别保存。原件下载不等于全文或贡献审阅。

| 来源 | 实际已读范围及停止 | 限制 |
| --- | --- | --- |
| SRC-OPENAI | 官方RSS当前1251项，标准XML解析目标日前后标题/日期；该日新增初报1项。Research直接请求403；初报正文用web回源实际读What happened/Why this matters/How addressing。 | RSS不是全站研究目录；本地初报raw是403挑战页，不是正文。 |
| SRC-ANTHROPIC | Research/News两页Next数据解码：April/May研究6项、News13项；Apr30只有diffusion-rule政策材料，核心说明已读并关闭。 | 仅该目录研究/News，不证明全部Engineering直发。 |
| SRC-GOOGLE-AI | Google Research April归档9标题，Apr30global-health核心关闭并获独立复核。Google pubs默认页及2025年筛选控件可读；DeepMind正确Publications第2/3页各30卡，Apr30邻接May1/Apr29，第3页首Mar24。 | Google pubs年筛选请求不可取，默认页年份不证明公开日；DeepMind是精选目录，不授全部论文覆盖。旧Blog page7失败不能代替Publications真分页。 |
| SRC-META-AI | Research与Blog历史page7连接失败；另用web核Research为0行，官方Publications不可访问。 | 未恢复2025研究目录；不记零命中。 |
| SRC-QWEN | 旧Blog首页及page2/page3实际标题日期：page2止Apr29Qwen3，page3从Mar28开始。 | 该分页Blog邻接未列Apr30，不授所有仓库/model artifact召回。 |
| SRC-DEEPSEEK | News的16项标题/日期逐项解码，Apr30邻接为Mar25与May28；主页链接定位既有ProverV2同家族。 | News没有全量论文库存；错误/en/research返回404，不计为Research检查成功。ProverV2不重列候选。 |
| SRC-MOONSHOT | 官方单页Blog26个日期标题逐项核，Apr7至May6间未列Apr30。 | 不授全部仓库直发；未扩读窗外正文。 |
| SRC-TENCENT-HUNYUAN | Research为动态壳；publicList两renderType的9/6项均2026。web回源超时；in-app browser创建该页实际60.8秒超时并重置kernel，未返回UI状态。 | 当前库存不能证明2025历史为空；没有取得可读“全部”历史列表，浏览器失败不是已操作或读过UI。 |
| SRC-ZAI | Research两页Next解码，累计18个独立标题/日期，page2 hasMore=false；最早Dec7/8，release notes辅助入口已取得。 | 当前终页是当前库存结束，不是2025四月全覆盖；旧Research缺段。 |
| SRC-BYTEDANCE-SEED | 默认Blog3页41/total49；US Blog3页18+18+4=40/total45，合并46独立身份，新5项日期均非Apr30。论文US5页85/total94，终cursor；CN同p40无数组。实际前端强制论文US头、读取has_more/total，空短页可续offset。返回条目的日期标题已核，近邻May2/Apr25（论文）、May12/Apr23（Blog）。 | Locale确实影响库存；前端未说明total/可见差额含义。49−46与94−85只是数量差，跨locale并集不保证属于同一total，不能确认遗漏3 Blog/9论文身份。保留库存口径限制，不猜造cursor或零发布。PublishDate非arXiv首公告。 |
| SRC-BAIDU-ERNIE | Blog两页10+6标题/日期，终页最早Jun30 2025；纠正此前May9误记。 | 当前目录没有Apr30历史段，不能由Jun30尾项推无发布；仓库直发未恢复。 |
| SRC-XIAOMI-MIMO | Paper8项最早May12；API取得Apr30 commit的精确README全文，实际含预训练/MTP、分级代码奖励、rollout异步等核心与模型下载表；未把后版全文当初版。 | commit时间不证明仓库当时已公开，原README无明确首发日期；raw回源失败后API恢复成功不再称全文不可取。当前Blog15卡日期不完整，仍需作者首次公开记录。 |
| SRC-MINIMAX | EN12/CN13当前标题；EN官方Blog web76行与raw均只有每卡Read More，没有下一页/More列表控制；结构化数据为当前CollectionPage。 | 每卡Read More不是分页，不能自造page参数授终页；当前切片不含四月完整历史，保留当期目录需求。 |
| SRC-ARXIV | 实测无效同日查询、相邻日年月退化；四主题submittedDate线索请求及有界月表标题补检，详见下一节。 | 日级公开证据受阻，不能以提交日、登记日或月目录推导Apr30；不授日窗覆盖。 |

上述只为Daily每日组及具名证据，不扫描Weekly来源；没有实际触发额外按需release扫描。不能把机构RSS/Blog子集作为全机构无遗漏证明。

## arXiv入口错误及有界恢复

- 同日Advanced from/to=2025-04-30、announced_date_first，HTTP200实际是`End date must be later than start date`；HTML第350行。不是0论文。
- 改Apr30至May1后头为1–200/2979；40秒超时仅807449/952285 bytes。条目只写`originally announced April 2025`，帮助明确announcement排序只有年/月。并非有效Apr30日池，停止这一过宽入口，不逐篇关闭2979项。
- 官方月表取得cs.CL April尾100（skip1513）、May首50、cs.DC April首100。实际浏览相关标题用于新命名查漏；月表数量分别1613/2833/319，不称当天命中，不把其余月库存变成必审队列。日路径`/list/cs.CL/2025-04-30`实际400，不是空日。
- 15:47北京时间另以官方catchup实际表单参数请求`https://arxiv.org/catchup?subject=cs.CL&date=2025-04-30&include_abs=True`，响应和headers存`arxiv-catchup-correct.raw/.headers`。实际响应明确`Catchup only allowed for past 90 days`，不是路径猜测失败；当前官方入口不能恢复2025这一天。这一外部限制不改变旧候选日期，也不证明当日没有论文。
- 四API请求完整参数见`arxiv-topic-{model,systems,agent,multimodal}.request.json`，均以`submittedDate:[202504280000 TO202504302359]`作邻近恢复线索而非公开窗口。模型225返回100、systems22返回22、agent202返回100、multimodal95返回95；317条响应按当前版本ID去重241，不称241篇当日论文。实际读取8项下述系统题摘及有界相关标题，未完成241个题摘的全量筛选；不宣称原始查漏线索的召回或贡献关闭完成。
- 旧`april/may-2025-arxiv-announcement-recovery.json.gz`的authority实际含DataCite Updated:v1与公告日程推导，不是独立官方日列表。用户冻结的旧22候选不因此搬动或降级；该推断不能授权新候选公开日。旧375=22+353只是旧流程数字，不是本轮确认的官方公开分母。

已实际读完整题摘、但公开日待证的代表性系统线索：

| 原始身份/当前读取版本 | 潜在增量与不能采用的原因 |
| --- | --- |
| [Triton-distributed / 2504.19442v3](https://arxiv.org/abs/2504.19442v3) | OpenSHMEM原语与tile级通信/计算编译；可能改变kernel通信边界。未读精确初版方法/评价，未证Apr30首公开，不评分、不进入Books。 |
| [Bullet / 2504.19516v4](https://arxiv.org/abs/2504.19516v4) | 协调prefill/decode的空间、时间与SM资源分配；需核TTFT/TPOT、SLO、预算和干扰代价。纠正“在线离线任务”误读，当前后版不回填首版。 |
| [FlashOverlap / 2504.19519v2](https://arxiv.org/abs/2504.19519v2) | 完成tile信号及前后重排使NCCL与计算重叠；潜在局部机制不能因单点优化排除，未证明日归属。 |
| [FineQ / 2504.19746v1](https://arxiv.org/abs/2504.19746v1) | 细簇异常值编码与时序硬件协同；须核数值质量/硬件成本，而非直接采用3bit速度宣传。 |
| [Semi-PD / 2504.19867v1](https://arxiv.org/abs/2504.19867v1) | 分SM计算而共享权重/KV存储；可能改变PD的复制/容量取舍，尚无公开日与方法证据。 |
| [SYMI / 2504.19925v2](https://arxiv.org/abs/2504.19925v2) | 优化器静态分片、专家权重动态placement；需要核专家流量/更新一致性，不能据当前摘要授训练实现。 |
| [Genie / 2504.20854v1](https://arxiv.org/abs/2504.20854v1) | CPU网络试验床模拟GPU流量、结合ASTRA-sim；潜在测量替代条件而非真实GPU结果。 |
| [OSVBench / 2504.20964v2](https://arxiv.org/abs/2504.20964v2) | 长形式化规格与OS代码验证题；须先确定是否真实改变模型长上下文/验证边界，不能仅因benchmark名称准入。 |

这些是有身份的待核线索，不是新候选、不算证据完成。恢复需要当期官方Apr30日公告/列表快照或作者明确首次公开发布记录；只要日历日期，不需要精确时分秒。取得后仅重开对应材料、核初版/事件，窗外记真实归属，不动旧候选。尚未读完的正文不是外部阻碍；在日期获得授权前不扩读全部后版来绕过门限。

## 已校准的新事件与Books比较

[OpenAI初报](https://openai.com/index/sycophancy-in-gpt-4o/)由官方RSS的Tue,29 Apr2025 18:00GMT确认北京时间Apr30；当前官网显示Apr29，原口径和实际时区换算均保留，不虚构时刻。新增贡献是厂商承认短期用户反馈代理与实际行为失配并回滚的生产反例；3+2+2=7，实际纠错强制深入受影响内容。

实际读What happened、Why this matters、How addressing，能支持回滚、短期反馈过度权重与拟改训练/评价方向；不能支持受控单一因果、内部reward公式、训练权重/数据、未来修复效果或全模型可靠性。当前正文非冻结2025逐字快照；本地403不能充当证据。详细独立审阅见[首批复核](supplement-first-review-20261007.md)。

唯一Books采用命题限于评价代理：`PLATFORM-EVALUATION-SYSTEM`，Ch66“为什么选一个分数不是评估系统”第33～58行实际包含点赞非随机、短期满意不等于正确/长程风险、scorer激励影响行为及限制；“Offline、Shadow、Canary与Online”第3208～3227行实际承载离线/线上/长期证据不可互代。主任务与Gibbs均读这些局部，裁决已有覆盖，不写Books、不借事故未披露训练机制扩写RLHF。

05-03原OpenAI May2 postmortem与本次初报是同一事故家族的不同事件，旧May3候选不移动、不改评分；跨日汇总不能把两次说明当独立研究家族相加。DeepSeek-ProverV2是本日原22之一，只去重，不增加数量。

代表关闭：Anthropic Apr30 diffusion-rule原核心为出口管制政策，没有新增本项目模型/系统机制，Gibbs独立关闭通过。Google Apr30全球健康评价含临床人格/疾病合成，项目AI for Science/医疗应用暂缓，不借通用Data/Evaluation词汇重新引入；Gibbs已回源独立确认本项具体范围关闭，不外推所有医疗材料。8项系统线索完整题摘也已独立校准为保留贡献潜力、公开日待证，不关闭或采纳后版性能。

## 进度与精确停点

新增确定落窗1家族/1事件，深入受限审阅与Ch66已有覆盖局部独立通过；原22候选复用不重算。本日增量补查的写回差额、来源范围及外部隔离已获Archimedes最终独立裁决，root于17:50同步完成态；不宣称已扫完2025或无遗漏。

当前外部终态保留项为上述arXiv日公告、Google pubs公开日/Meta/Hunyuan/ZAI/ERNIE/MiniMax历史切片、MiMo首发记录和Seed可见库存口径；需要当期官方目录或明确作者首次公开记录。这些不用于正面证据、Books、零命中或无遗漏断言。续跑实际50题摘、44新线索首校准与9处决定性core经Archimedes独立核验，三项改判写回后35潜在/9关闭，具体身份/边界见[Advanced记录](advanced-resume-20261007.md)。最终写回差额已独核通过，普通待办无；材料到达仅定点重开对应身份。

15:54附近定点补检MiMo首次发布，实际查询`site.github.com/XiaomiMiMo/MiMo "2025-04-30"`、`site.huggingface.co/XiaomiMiMo "2025-04-30"`、`site.x.com/Xiaomi "MiMo" "April 30"`；又用官方候选域mi.com/blog.mi.com/xiaomi.com/huggingface.co/github.com限制`MiMo "April 30" "2025"`及HF/GitHub/ModelScope限制`"MiMo-7B" "2025-04-30"`。返回第三方Nightly、新闻摘要、镜像和回顾及无关事件；未恢复作者明确发布日期。它们只是线索，GitHub/HF域名上的第三方笔记仍非MiMo原作者，不能作为日期或方法证据，也不据检索失败否认Apr30发布。停止有界搜索，保留具名原始发布需求，不无限遍历社交/版本史。

16:04～16:12的有界补正：DeepMind从实际Publications分页链接进入第9、3、2页，非自造参数；第9页25卡均2023，仅用于定位，不作2025队列。第2页Oct30～Mar28，Apr30邻接May1/Apr29；第3页Mar24以下，无Apr30目录项。Google pubs默认2025控件显示678，Year/Title排序与年份不能证明首次公开日。来源URL为`https://deepmind.google/research/publications/page/2/`、`/page/3/`及`https://research.google/pubs/`；web实际显示文本，不是假设curl已恢复。Meta正确Publications回源失败、Hunyuanweb及browser上述实际失败、MiniMax页面无列表分页均按实际停止，不要求无限穷举网站。

Seed客户端原件`seed-client.raw`实际代码令article_type=1强制`x-tt-locale: US`，用offset作为page_token，has_more=false停止；它未解释发布状态过滤前后total。CN论文p40只返回total94和cursor、无数组，不能恢复具体身份。Blog追加US p0/20/40的headers/raw，返回18/18/4且终页false，40独立ID；与默认41合并46，新增5项ID672/1504/2156/2171/702日期分别Jan23/Dec2/Jan20/Feb25/Jan6，均非Apr30。并集46不保证是默认total49的子集，49−46=3只为数量差，不能确认漏了3项；同理94−85=9不能替代具体身份核验。没有采用5项窗外摘要或扩读全年正文。保留库存口径与历史目录限制；请求可核的当期官方条目或目录，不把total94/49说成全读完。

MiMo raw历史README请求curl35；随后实际GET`https://api.github.com/repos/XiaomiMiMo/MiMo/contents/README.md?ref=0f485cc820d855f38a7878fad338f02f4a2f38da`恢复成功，正文由标准base64解码完整读到（`mimo-apr30-content.raw`）。本文可以核该commit的内容，不能核仓库当日公开状态；正文“open-source”未标发布日期，不能把commit作者时间直接授权Apr30公开。既有后续技术报告链接/数字不因此次恢复获得当日审阅或Books权限。
