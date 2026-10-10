# 2026-02-16 自然日来源补查

补充窗口：2026-02-15 ～ 2026-02-15（北京时间完整自然日）。检查时间：2026-10-08T16:20～16:39+08:00。
作者：supplement_20260216。原窗口、原候选0、原§4连续正文冻结，见[基线](supplement-baseline-20261008.md)。旧完成只代表旧检查，不是本轮验收。
本日只写README及此_sources；未写Books/LEARNING_STATE/共享索引，未stage/commit/push。

## 实际来源与停止范围

只查清单14每日源与具名线索，不扫描每周组；没有清单按需发布批次触发。
west/east原件保留首查，date-search1～4保存14条实际query及结果；后续recovery/near-window/final-narrow保留定点恢复。搜索停在返回首屏，不当全站历史水位。多query出现跨domain噪声的结果明确不授机构研究权限，不将全部命中变队列。

| 来源 | 实际入口、日期/主题、停止 | 本轮结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research当前首屏→官方RSS GET200，读取后只解析Feb12～18日期邻接；[native](supplement-native-dates-20261008.json)为原始pubDate/标题/URL，Feb13后下一条Feb18；date-search1严格index日期query | 实際RSS切片无Feb15 item，停止此邻接；不保证RSS外未归档发布 |
| SRC-ANTHROPIC | Research首屏→官方HTML publishedOn Feb切片；zero-days Feb05、India Feb16、autonomy Feb18；date-search1日期query | 已核本页邻接，没有Feb15；仅本页，不声称历史全站 |
| SRC-GOOGLE-AI | DeepMind Research、Google Pubs→各Blog当前首屏；date-search1 after/before model主题、final-narrow分别精确Feb15官方domain；得到Dingle具名原文 | 一篇确切Feb15正式公开事件，完整题摘及必要§5/7定点主张后贡献前关闭（下文）；当前目录不能恢复完整Feb15模型主题列表，G-GOOGLE继续隔离，不称零发布 |
| SRC-META-AI | Research空→Publications page3与Blog page2；final-narrow实际取Feb26～13/11论文邻接与Mar11～Feb09 Blog，页后混入旧年 | 有限切片未见Feb15，停止page3/page2，不打开历年论文；G-META混合排序非连续历史水位 |
| SRC-QWEN | 旧blog迁移→qwen.ai动态0行，具体Qwen3.5→3.8 repo News Feb16、24、Mar02；final-narrow exactFeb15 query | 官方首次release日Feb16不属于补充窗；快照名Feb15不是公开。旧需要时分秒的G-QWEN不在自然日补查再请求；G-QWEN-DIRECTORY迁移目录历史缺片仍隔离 |
| SRC-DEEPSEEK | 官网→Change Log，final-narrow核2025Dec01与2026Apr24邻接，date-search2具体官方domain日期query | 本日志无Feb15，不外推所有研究；G-DEEPSEEK日志外历史研究片段继续隔离 |
| SRC-MOONSHOT | Platform Blog26标题截止2025Nov（不读旧26正文）、Kimi-K2.5当前README；date-search2本日query | 未恢复Feb15发布/重要修订列表，G-KIMI隔离；当前repo不是旧日期水位 |
| SRC-TENCENT-HUNYUAN | 首查Research超时；GET200是6885字节SPA壳；按来源清单尝试浏览器：create超时、state显示research?page=1标签，getTab再30秒超时；随后官方T1 README和date-search2本日query | 未取得“全部”列表，G-HUNYUAN隔离；不将当前T1相对“今年2月中”绑定本日。不重复无效浏览器循环或历年repo队列 |
| SRC-ZAI | 首查Research web两次timeout→GET官方HTML200，native中Feb21技术报告/Feb11开源/Feb02OCR；release notes邻接Apr07～Feb12；date-search3本日query | 有限官方日期段无Feb15，停止两个邻接，不深读窗外正文 |
| SRC-BYTEDANCE-SEED | Research精选及Publications1～20/242，未点击旧分页；date-search3及final-narrow本日query；具名Seed2.0正文日期Feb14 | 本日未确认新事件；排行榜as-of Feb16非发布，Feb14官方日精度按合同足够判本轮窗外，不请求时刻；G-SEED历史论文分页缺段隔离 |
| SRC-BAIDU-ERNIE | Blog第1页May09～Feb06～Jan29跨过窗口；date-search3本日中文日期query | 本页无Feb15，停止第1页；未打开2/2，不称仓库commit全审 |
| SRC-XIAOMI-MIMO | Paper Jun29/Mar13～Feb03～Jan08；Blog无日期当前15标题；date-search3官方本日query | Paper邻接无本日，无日期Blog历史片段G-MIMO隔离；第三方weekly star清单Feb15属于其他repo，不能转成MiMo-Code首发 |
| SRC-MINIMAX | EN Blog末尾Mar18～Feb14 Forge～Feb12 M2.5；CN迁移minimax.cn末尾Mar18～Feb12 Forge；Agent Tech Blog15行仅导航；date-search4精确本日query为空 | 两官方Forge日期均非Feb15，无具体重要修订信号，不请求首发时分秒/旧全文；G-MINIMAX-AGENT历史列表缺失继续隔离 |
| SRC-ARXIV | 实际availability公告表与2026 holiday、status首页、两条本日异常query、date-search4本日主题query；SkillJect精确v1 abs及定点cs.CR月页（cache miss） | 周六EST无公告；SundayFeb15 20EST=BJTFeb16，Feb15北京自然日无常规批次。Holiday表无本日；status/搜索不能保证历史无异常，但无具名异常线索。不开主题分类全文池、不用DOI/submitted作公开日 |

以上实际结果及限制均为本日作者核，不继承Feb14/15候选、Source/PRE/POST或完成声明。

## 完整题摘与代表关闭

初包及root独立校准见[admission](supplement-admission-20261008.md)；root持久独核文件由root写入。本日新增确定候选0，不评分已明确贡献前关闭/窗外/日期未确认材料。

### Dingle/Hutter：新增窄query命中

[官方DeepMind事件](https://deepmind.google/research/publications/225507/)与[出版社](https://www.mdpi.com/1099-4300/28/2/226)标正式公开Feb15；完整题摘保留last-two-originals、dingle-original，不将正式发表自动当first-public，也不为已明确贡献关闭追更早稿。
题摘三命题是组合最优解描述复杂度、按算法概率采样、两个简单目标的最优点重合概率。歧义只在是否支撑模型学习机制，故有界补读作者原稿§4范围段、完整§5/7，不读全文证明/引用附件。MDPI direct与PMC web受限后，一次EuropePMC官方article fullTextXML200恢复，见[dingle-xml](supplement-dingle-xml-20261008.json)；访问受限没有决定准入。
§5 Eq31～36仅比较组合样本等待次数；作者明确忽略生成样本的计算资源，Kolmogorov复杂度不可计算，近似可能耗时失准，实用性留未来。DNN generalization与LLM training仅引用既有工作，非此稿新增parameter-function map或训练机制证据。§7对象是离散几何/配置/序列，低描述复杂度也不保证直观规则或短对象效果。准入两入口均未获得“可改变本项目哪项模型学习/系统设计”的直接命题；不能靠组合搜索类比weight learning入池。贡献前关闭，不是理论/小实验/非LLM一律不收，也不进入Ch4已有覆盖比较。root已实际读完整题摘、§5/7与范围段，并明确同意此family-specific判断。

### 其他具名事件

- MemGUI Feb15：官方README只记录已有bench采用/榜单，而官方MobileAgent News另标GUI-Owl1.5 release Feb14；这次没有评价盲区或可比失效证据。关闭的是本次采用事件，不否定旧bench机制，不用当前June runtime反推旧实现。
- open-terminal0.2.3/0.2.2：官方CHANGELOG本日核心说明为MCP包装/字面null查询参数防422；未新增长期执行/权限或隔离机制。旧Feb14 unauth链接和JSONL不是本日新变化，不能声称已审全部安全。无需为了明确贡献不足追本日时区。
- nanobot：第三方镜像Feb15 OAuth接入是兼容组合；官方当前README无旧news，不授exact旧版或安全已核。窗外Feb13 security标签不据标签无差别深审。
- OpenAI社区：计费/开源请求、未诊断MCP故障无新的因果机制/可比反证；没有厂商根因，不照录用户归因。MiMo/Meta领域应用则不绕过AI for Science暂缓。
这些实际核心均在signals/originals/final-narrow原件；并非逐项关闭搜索全结果。

## 精确隔离与恢复

本窗外部保留仅上述G-GOOGLE/META/QWEN-DIRECTORY/DEEPSEEK/KIMI/HUNYUAN/SEED/MIMO/MINIMAX-AGENT，均不支持Coverage通过、零发布、候选或Books采用。所缺是目标自然日官方日期主题切片/具名事件原稿，而非时分秒。可接受替代是本日具体原始文章与公开日期；每个来源只请求一次，在对应表行定点重开。

SkillJect独立身份线索：原arXivv1完整题摘贡献潜力明确，但v1提交已是BJT Feb16，之后公开不可能落Feb15；本日不把submitted当public。更早作者公开稿没有本日证据，确切首次公开日未确认，不指定日报归属。需官方announcement/list或更早作者首次公开稿的日期；仅恢复该家族，不开Feb16/17其他论文队列、不把current v3/OpenReview后继正文用于本日采用。

## 当前停点

作者来源、贡献筛选与No Change六部分已同步；root首包、Dingle具名关闭及本轮完整DAY均实际通过，见[独立复核](supplement-20261008-independent.md#完整日级验收)。普通扫描/题摘/必要候选审阅/Books新写/独立验收待办0。完成态V3、原窗口/0候选/连续原§4及本地引用与限定unstaged diff通过；cached冻结基线末空行告警仍保留，不改index、不声称cached通过。九来源限制与SkillJect窗外线索继续隔离，不授正面Coverage/Evidence或全网零遗漏。作者本日结束，不自行开始下一日，未stage/commit/push。
