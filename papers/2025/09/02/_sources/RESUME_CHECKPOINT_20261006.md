# 2025-09-02 Daily 恢复检查点

记录日期：2026-10-06。作者：daily_20250902。状态：**研究未完成，按root协调保存恢复点**。这不是V3 Daily验收，也不声明Coverage、Evidence或Books通过。没有生成完成README，没有新增Books，没有操作stage、commit或push。

## 1. 窗口与关键阻塞

默认窗口为 `[2025-09-01T09:00:00+08:00, 2025-09-02T09:00:00+08:00)`，对应UTC `[2025-09-01T01:00:00Z, 2025-09-02T01:00:00Z)`。历史Daily独立从官方原始入口重建，未从旧Weekly反推。

尚未取得足以关闭arXiv实际公开批次归属的原始材料。官方历史政策 [`availability-before-20250903.md`](../../_sources/official-calendar/availability-before-20250903.md) 原文由arXiv官方GitHub精确commit恢复，并给出正常Sun–Thu公告、最终ID在公告时生成、不能backdate及2025-09-01 Holiday。按EDT换算，本窗唯一正常槽为2025-09-02T00:00Z。Holiday段只明确“deferred mailing”，没有当次actual announcement记录；因此**本窗arXiv announcement=0尚未证实**。不得由Holiday强制归零，也不得把submitted改名为公开时刻。

官方月份ID也不决定日归属：2509.00030v1的原始提交历史为2025-08-20T17:44:47Z，2509.00*前缀机械恢复374条的API `published`均为8月提交记录。它们不是09-02确定候选、不是09-02新论文数，也不是已完成初筛的分母。API返回当前版本摘要；必要时必须重取exact-v1，不能用当前修订支持2025事件。

已有09-01作者恢复的真实2508批次DataCite registry记录，root正协调其日期复核；本文未拿其created/registered上界等同实际公开时刻。恢复后须检查原始字段、批次对应、公开时间上下界是否完全落在本日窗口。只在官网schedule一般槽与较晚metadata上界跨截点时，保留具体日期缺口，不移动到发现日。

## 2. 已做的原始工作

全部14个每日注册来源已实际打开首查入口，HTTP与正文状态分别记录；其中Meta、Hunyuan的200响应是空壳。逐源范围及停止点见 [`source-screening.md`](./source-screening.md)，原始请求日志与压缩body同目录保留。没有扫描每周来源。

- OpenAI：Research → Index → 官方News RSS，1247条完整pubDate记录。窗口内RSS无条目；Sep2 Helpful更新的官方 `pubDate=2025-09-02T04:00:00GMT` 在本窗后，不因标题写Sep2而纳入本日。原始 `openai-rss.html.gz`、`openai-rss-records.json` 可供其他日期定点复用。
- Anthropic：Research原始Flight目录174条，`publishedOn`范围2021-12-01至2026-10-01；本窗无目录项，相邻Aug27与Sep5。保存 `anthropic-directory-records.json`，不扩成全站News覆盖声明。
- ERNIE：Blog共2页均已读，最早2025-06-30，Sep12与Aug14相邻；Publication初取503后重试200，四篇论文链接已恢复，精确版本/日归属仍需后续轻量核对。
- Moonshot：Kimi Platform Blog完整可见目录至2024-05-29，Sep5与Aug22相邻，未见本窗博客项；组织仓库补充扫描尚未完成。
- MiMo：完整8项Paper目录的Sep19/Jun4切片无本窗项；Blog日期与官方仓库补充尚未完成。
- Qwen：旧官方博客可读Sep23/Aug19相邻及selected publications；其已声明迁移qwen.ai，目标站CONNECT403。只确认旧站切片，未确认迁移后历史目录完整性。
- Z.ai：中文Research page2读到“没有更多”，数据库当前最早2025-12-07；官方Release Notes至2025-07-15，Sep30/Aug11相邻无本窗release。旧技术研究恢复未完成；release切片不替代它。
- DeepSeek：主页与News研究索引可见至2025-05-14；动态仅五条、有“查看全部”，需要真实展开或等价原始列表。
- Google：真实year参数是`?category=2025`，`?year=2025`被忽略。机械抓取46页已结束，原始stop为page46；提取676个唯一title/URL，filter显示677，差额未核。**只恢复了年份目录，没有逐项题摘/日期筛选，未当本窗命中**。`google2025-directory-fetch-log.json`、`google2025-directory-title-records.json`及46份原始body保留。本轮停止年度扩池。
- ByteDance Seed：Public Papers首页20条，仅2026；年份/翻页仍未处理，官方JS CDN访问被拒。
- MiniMax：英文Blog首屏到2025-10-27；`?page=2`返回相同内容，不能称page2覆盖。真实分页、中文历史目录或官方项目补充未完成。
- arXiv：12个注册分类长月份目录首1000条已抓，跨类只机械恢复2509.00*前缀374标题/API元数据；未关闭实际历史公告批次，未逐项进行贡献初筛。

8篇exact-v1完整题摘已定点读取，原始HTML与`.abstract.txt`保留：2509.00031、00036、00072、00105、00217、00100、00244、00047。fresh_review已实际读取8篇题摘，对四项准入与MODE/UDR排除通过局部校准；00072限纵向时序信号缺失的评价反证，00047确认范围内且可定点读负面边界。日期未核，不评分，不冻结候选，不冒充全文证据完成。00072v1原题为Beyond Memorization；原页标较新版本撤回，定点v2官方页证实v2于2025-10-06T14:10:14UTC撤回，未提供原因，后续v3/v4恢复并改题为Test of Time。v1自身未标撤回，不删除有效原始v1，但真实撤回/纠错信号须纳入后续审阅。当前v4中心证据已变化，禁止代替2025v1；没有采用其正面主张。00047v1的latent-overlap解释是否超出成熟tradeoff仍待正文核验，不因CIFAR100实验而自动范围外。

## 3. 外部必要材料与可接受替代

| 缺口 | 已试原始路径及失败 | 为什么必要 / 可接受替代 / 定点重开 |
| --- | --- | --- |
| arXiv当次actual公开批次与日期归属 | longmonth只有月份；历史日URLinvalid；当前new的date参数不能证明旧公告；status.arxiv.org、blog.arxiv.org、api.datacite.org与info.arxiv.org实测CONNECT403。官方GitHub历史availability已恢复，仍无实际延期批次记录 | 需要2025-08-31～09-02官方dated announcement/new/cross/replacement批次或当次官方status/blog延期说明；DOI registry原始metadata只能与实际批次证据限定时间界，不能直接作为public事实。只重开09-02对应批次，不重扫整月。 |
| Qwen迁移后历史目录 | 旧站meta/js指向qwen.ai，新站CONNECT403 | 可接受官方历史目录分页/日期API或对应时点官方原始发布索引。已有旧站切片继续有效；仅重开迁移后本窗覆盖。 |
| Seed与MiniMax真实历史分页执行所需脚本 | 官方原HTML识别Seed CDN lf-flow-web-cdn.doubao.com、MiniMax CDN file.cdn.minimax.io，均CONNECT403；主站仍200 | 可接受正常proxy/TLS下官方脚本与分页接口、浏览器完成的历史列表，或官方导出的等价日期列表。不得拿首页200或被忽略的page参数冒充完整历史枚举。 |

网络失败是当前实例的实测，平台状态工具stale不推翻实测，也不把draft保存等同已发布。没有绕过代理或关闭TLS验证。上述同类需求已交root统一协调，无额外向用户重复请求。

## 4. 普通待办与续跑顺序

以下是尚可执行或尚未处理的普通工作，**不是外部阻塞的替代名义**：Meta/Hunyuan浏览器目录检查（root共享结果待到）；DeepSeek动态“查看全部”；Z.ai旧研究补充入口/脚本503的定点重试；MiMo Blog；Moonshot及相关官方仓库补充；ERNIE论文身份/精确版本轻量核对；Google年度目录title范围与日期恢复以及DeepMind历史Blog；准确批次恢复后arXiv题摘逐项初筛、日期去重、版本事件说明、评分、相应证据深度、Books比较与独立复核。

root于2026-10-06要求在真实外部日期/历史枚举阻塞下保存本检查点，停止全年度/未定日扩池。因此这里保留普通待办的实际停止点，不宣称这些工作已穷尽或整日已完成。恢复时先用明确新材料修复批次/目录缺口，复用未变化的有效原始内容；不从旧Weekly复建Daily，不因本检查点存在就创建零候选完成日报。

独立事实核对：fresh_review已检查窗口界限、RSS1247条与本窗无项、Anthropic174目录、Google46页机械抓取/676title与普通待办区分、内部链接、无README/Books/评分/冻结候选，以及Holiday仅mailing不足actual零公告；并实际核对00072v1/v2原页的标题、撤回版本/原始日期及未给原因，增量核对通过。**事实复核通过的范围仅本恢复点，非Daily研究验收**，不外推family全部撤回或v1已撤回，也不用v4证明v1。机器格式检查仅适用于后续V3报告；本检查点没有运行`validate_research --report`来伪造日报验收。当前未有采用命题、Books决定或Books写入。
