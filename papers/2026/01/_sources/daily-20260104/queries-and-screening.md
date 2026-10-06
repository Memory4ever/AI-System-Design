# Jan04 独立来源与停止记录

访问日2026-10-02。窗口[2026-01-03T09:00:00+08:00,2026-01-04T09:00:00+08:00)，UTC[Jan3T01,Jan4T01)。换日完整重读AGENTS、研究合同、Report合同、每日来源/主题、Prompt、ROADMAP；LEARNING_STATE未找到Jan/Feb相关checkpoint。仅本日README/月_sources owned；不加载旧Report候选、评分、摘要/Weekly池。沿模型能力形成、模型组件、多模态、训练/推理、平台/Agent主线，AI for Science暂缓。宽目录不变逐项队列。NoWrite共享Books。

## 真实查询与材料

本日official-entry-0～4.txt为14清单原入口的新调用，不复用别日报取值。supplemental-official.txt为DeepMind Publications/Qwen新Blog/ZAI release/官方holiday本日原响应；arxiv-public-policy.txt为availability/Agenttechblog/catchup/月列表本日原响应。机构Jan3/Jan4多种日期表示+model/research/agent四组官方域查询见date-search.txt；每组止返回首组，均空，空搜索不是无发布。

official-date-slices.jsonl每条保存实际源URL/请求/条目数/窗口hit/邻接字段；只元数据切片不读全年摘要：
- OpenAI Research首屏→RSS实际1243项 title/link/pubDate定位：窗内0，邻接Grove raw Fri,02Jan2026 10GMT（Jan2T18+08）/Jan7Health。Grove已确定窗外，不在本日重复筛贡献。
- Anthropic Research当前首屏→HTML 174 publishedOn字段，窗内0，邻接Dec19T19:45Z Bloom/Jan8T00Z Critical Infrastructure Defense。只同一有限Research目录。
- Google DeepMind Research currentnews止May2026；Publications page1 30行（265项9页）Jan9→Dec3跨窗止page1；GoogleResearch pubs当前年过滤/首屏，无日级原始日期队列。未读全年pubs。
- Meta研究原入口0行，Qwen旧BlogSep23 2025及新qwen.ai/blog0行；均官方日期query停止首组，动态历史未恢复。
- DeepSeek /news/研究10项Jan12→Dec31邻接，无本窗行，动态5项“查看全部”不是全部机构；date-label不能当首公开时刻。
- Kimi平台26行Nov7 2025→May2024。定点官方原changelog0.72/0.71 Jan4完整核心：Python3.14安装、ACP client file/shell sync、/model、on-demand skill slash、info/Toad。没有推断完整执行约束或已核代码。日期含糊初始拟版本接入负侧交root校准；随后精确定位release。限定git ls-remote tags只0.71/0.72实际tag；官方ReleaseAPI原published_at：0.71 Jan4T05:08:41Z，0.72 Jan4T06:01:07Z，两个都严格窗外→Jan05，created_at不当公开。未读Jan05 PR，不成为Jan04候选/评分，也不冒充重复已审。可能更早PR/artifact是不同事件，没有本日定点线索不扩大其发现。
- HunyuanResearch网页超时；fresh官方POST api/blog/publicList {pageNum:1,pageSize:1000,renderType:0} 成功，totalNum9/list9，只题名/date字段，display最早1770090898=Feb3T03:54:58Z。publicAt/createdAt/publishedAt/display/updated全部原值保留。目录可提取无需再无限browser；当前九条不证明Jan04历史无隐去项。
- ZAI原Research14项/查看更多止Dec9 2025；release说明Jan14→Dec22桥接无本窗行；release不是完整研究目录。
- Seed API type1/2、2026ASC/2025DESC各page_token0/count20，actual19/14/18/18 metadata；2026最早Jan20/Feb12，2025最晚Dec15/Dec24。pinned不当停止理由，nextpage/token/has_more保留，有限窗口桥接不用读全年摘要，不能证明API locale/status过滤无缺口。
- ERNIEBlogpage1 Jan8→Dec23跨窗止page1；下一页2/2更老，不读窗外正文。
- MiMo当前8 Papers Jan8→Oct21跨窗及15 Blogs/More，Blog日期未恢复；MiniMax English12 dated Jan27→Dec23跨窗，CN跳minimax.cn只68行壳，Agenttechblog15行导航。止有限入口+date query，不把旧论文日期或当前题目当Jan04公开。

## arXiv：新公告与revision权限分开

本日实际读availability L172/175–186及holiday L17/21/29/32。一般公开包括new/replacements/withdrawals/crosslists，通常Sun～Thu20ET，Fri/Sat无公告；specific新年受影响accepted批延至Jan4ET20=Jan5BJT09。本窗处在Jan2FriET20→Jan3SatET20，没有常规公告。只对公告过程作判断，不能证明非标准公开、作者镜像或全部修改不存在，也不把Submitted推成公开。

本日四主题API查询原式在arxiv-and-kimi.jsonl：
lastUpdatedDate:[202601030100 TO 202601040059] AND submittedDate:[199001010000 TO 202601030059] AND (主题)；
start0/max20/lastUpdatedDate ascending，模型、系统、多模态、Agent均total0。限定早于起点的提交以定位可能旧稿更新，不扫描本窗新提交池；API日期是元数据，0不证明公开revision覆盖。不得把关键词或索引当原文贡献。catchup本日cs.CL Jan04网页cachemiss、HTTP400，月首25 cachemiss，止此不展开全分类逐项。
没有已定位需完整题摘贡献判断的当窗论文，也未评分。raw0只指四组该查询，不能称全网本日0篇。

## 校准与安全终态

首批已发root：Kimi Jan04变化拟负侧及官方announcement边界，随后原release日期证明两事件窗外。拟入选0；没有把仅Submitted标题纳入或沿用另日报候选。实际候选审阅完成0，BooksNoChange。

GoogleResearch、Meta、Qwen、Moonshot全研究/重要修订、Hunyuan历史、ZAI全研究、MiMoBlog日期、MiniMaxCN/Agent历史，以及arxiv非标准公开revision/作者镜像，均精确隔离；当前可用有限入口/原API已检查，但历史完整性不可授。可接受重开证据是同一本窗官方dated历史目录/批次/具体版本公告或可核author-first-public，恢复只该源/该事件，不扩月份。不用于正面证据、Books、Coverage/Evidence无遗漏或安全/性能保证。
