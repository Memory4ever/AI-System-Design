# Daily Research — 2025-09-28

**规范：** V3
**窗口：** 2025-09-27T09:00:00+08:00 ～ 2025-09-28T09:00:00+08:00
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-10-06T12:45:00+08:00

## 1. 结论

本日原始来源独立重建后，尚无同时确证落窗、通过贡献筛选的材料家族；确定候选0、相应证据审阅0、实际Books修改0。此数量只描述本次有界检查的结果，不是本日零发布或历史无遗漏结论。动态目录、历史公开公告和限流缺口按§5隔离。

作者侧来源处理及本次Books No Change判断已就绪；root尚未独立日级复核，故保留进行中。原始抓取、压缩恢复与停止点见[交接](../_sources/daily-20250928/CALIBRATION_HANDOFF.md)。没有以当前目录中的2026年成果反填2025年。

## 2. 来源覆盖

执行时间和完整请求见`../_sources/daily-20250928/fetch-log.json`及`recovery-log.json`；下表的“已检查”仅授所列实际切片。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方`https://openai.com/news/rss.xml`原RSS实际解析1247条，保留pubDate原值，按本窗UTC起止筛选，无落窗条目 | 已检查 | RSS不是全部历史Research正文全集 |
| SRC-ANTHROPIC | Research原HTML中Flight字符串实际恢复publication数组，174出现、172唯一slug；逐项publishedOn字段筛窗，无落窗记录 | 已检查 | 字段精度保留原值；未以它证明未收录内容不存在 |
| SRC-GOOGLE-AI | Research `/blog/2025/09/`页1读12条，Sep30至Sep11已越过本窗，停止未追页2；pubs实际category=2025、search=language model页1～3，1～37目录只作年份发现线索。DeepMind Research原gzip解压恢复；Blog及RSS实际取读100条，最早Nov5，未达9月 | 受阻 | pubs年份不是首公开日期；DeepMind当前目录/有限RSS不能覆盖9月，未把压缩解析错误当空目录 |
| SRC-META-AI | Research返回当前标题壳；官方Blog页1～3实际卡片读取。页2混有Feb20置顶/旧卡，未据此提前停止；页3普通卡Oct24之后跨至Aug27、Aug14、Jul31，停止 | 已检查 | 非单调/精选目录不授历史全集；Research动态历史未恢复 |
| SRC-QWEN | 旧Blog首屏跨窗停；本日本地实际API `qwen.ai/api/page_config?code=research.research-list` 返回200完整60项非时间排序数组，逐一检查原date无本窗项；[原JSON](../_sources/daily-20250928/qwen-api.json)、[元数据](../_sources/daily-20250928/qwen-api-metadata.json)、[请求](../_sources/daily-20250928/narrow-qwen-agent-fetch.json) | 已检查 | 限实际完整数组，不授全部历史发布/修订无遗漏 |
| SRC-DEEPSEEK | 官方news侧栏18条标题日期，Sep29 V3.2-Exp与Sep22 V3.1 update夹住本窗；只读发布身份，未扩读2026正文 | 已检查 | 目录日期精度仅日；无本窗相关事件身份 |
| SRC-MOONSHOT | 官方Blog完整可见26条，Sep16/Sep5后至2024历史，目录本窗无条目 | 已检查 | 不授所有GitHub临时发布覆盖 |
| SRC-TENCENT-HUNYUAN | Research首查仅壳；正确publicList POST pageNum1/pageSize100/renderType0实际totalNum9/list9，保留displayPublishTime与updatedAt，全部2026 | 受阻 | 当前9条不覆盖2025；未授历史零发布，子代理无可用可见浏览器 |
| SRC-ZAI | Research Flight实际blogsItems页1 15、页2 18，页2hasMore=false，最早Dec7；release notes实际Sep30与Aug11夹窗 | 受阻 | 当前Research截断至12月，不授9月全集；release notes切片已读 |
| SRC-BYTEDANCE-SEED | type2/year2025/page0/count20实际15条、total49、has_more=true、next20；分离置顶后非置顶已到7月，停止。type1/page0 US与CN均total94但无sub_article_list；真实page20仅SwiftSpec（Jun12），停止 | 受阻 | Blog该段无窗内记录；论文接口第一页内容缺失不能记0，后页不能补授缺失前页 |
| SRC-BAIDU-ERNIE | 官方RSS18 item实际解析（含导航项），普通博客Oct16与Sep12夹窗，无本窗条目 | 已检查 | 非论文全集 |
| SRC-XIAOMI-MIMO | 官方主页及两实际JS读8论文日期（Sep19/Oct21夹窗）与15 Blog；More是本地slice展开。另取原route metadata，现存Blog日期2025-12-18/19及2026，不把未标日期补成午夜 | 已检查 | 若未来出现其他历史chunk只重开相关目录，不授当前路由历史全集 |
| SRC-MINIMAX | EN/CN当前目录12/13技术卡，EN尾Oct27、CN附Jan15；Agent Tech Blog本日实际200完整可读目录仅2026-05-13文章，官方llms.txt全索引也仅该技术文章，无历史分页后停；[目录文本](../_sources/daily-20250928/minimax-agent-text.json)、[索引](../_sources/daily-20250928/minimax-agent-index.txt)、[请求](../_sources/daily-20250928/narrow-qwen-agent-fetch.json) | 受阻 | 当前公司精选列表及Agent目录不授完整2025历史覆盖，需本窗原事件或历史目录 |
| SRC-ARXIV | 12主线分类、LLM/language model/Transformer/inference/world model/vision language/VLA/GPU题名发现，submittedDate Sep27 01UTC至Sep28 01UTC、start0/max100；首请求429，单次重试仍429。日列表路径400；官方availability说明实际读取 | 受阻 | 无本窗原始公开公告，submitted查询不等于first-public；周末无定时公告也不授零事件 |
| 补检：[Web主题搜索](https://www.google.com/) | 3组Sep27官方机构/中文机构/arXiv系统主题实际结果，保存search.json；未把搜索排序当历史覆盖 | 检索受限 | 返回多为社区使用问题/匿名行为投诉，无新增可证原始研究事件 |

## 3. 候选与判断

本窗确定候选0。未取得首公开证据的宽年份目录不进入确定候选、评分或Books。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

无确定候选，不编造全文阅读、实现核验或复现。Books No Change限于本次没有可支持采用的新命题，不声称所有目录材料均已有覆盖。共享Books由root集中写入，本作者未修改。

补检中的“模型被暗换”“模型404”“filename必填”均是用户问题/主张而非厂商原始发布。实际结果中404线程最终由提问者归因自己的旧代码；filename讨论区分base64与uploaded ID，未提供可比较的新失败机制；agent框架替换帖是征求设计经验、无实现或实验。模型替换投诉未给可核的后端身份与受控证据，故不能作为已证设计反证或安全变更采用。保留原线程文本，不因投诉性质删除负面线索；若后续获得原始变更/可核artifact，定点重开。

## 5. 缺口与下一步

可执行普通作者研究待办0；root独立准入/排除校准与最终日级复核待执行，不自授通过。

外部保留项：DeepMind/Hunyuan/Z.ai/MiniMax历史Research切片及Seed论文前页内容未取得；当前原响应、实际分页与恢复路径已在§2具名。Qwen完整实际API已恢复，不再将未执行动态入口留作终态hold。重开条件是官方历史列表、可追溯原发布正文或真实API含缺失前页条目，不接受当前首页“无条目”或注册时间代替。只补受影响来源和本窗，不扩整站/月度；这些缺口不支持正面Coverage、Books或无遗漏。

arXiv本窗题名查询在首次及一次重试均429，日路径400；必要替代是含首次公告时间/日期区间的官方历史列表或具体v1公开证据。官方周末排程仅说明常规发布机制，不能排除例外、延迟或修订；恢复只处理本窗相关标题/家族，不把整月库存转为全文队列。当前无必要正文可借submitted字段先采用。

## 6. 复核

复核者：root（待实际执行，非报告作者）。结论：未通过（尚未复核，不是已有否决）。请求核14来源真实停点、gzip原响应与恢复、Seed缺失前页、arXiv有限失败，以及补检负面/使用问题的具体关闭理由。首批准入没有确定拟入选，不能因此跳过排除/来源独立检查。

作者机器检查：V3校验通过；本日两份自写Markdown的1处本地链接存在；限定路径`git diff --check`通过。机器检查不代替语义验收。
