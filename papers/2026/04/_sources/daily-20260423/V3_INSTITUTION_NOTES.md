# 04/23 机构入口与实际贡献判断

root；固定窗口04/22 09:00～04/23 09:00+08。下表是本窗实际研究，不借相邻日的零命中结论，不扫描Weekly来源或全年论文。访问失败时用同一官方原文/API恢复，不将空响应称无研究。尚未结束的行继续处理；正文日期精度不足与目录完整性分别保留。

| 来源 | 实际范围与依据 | 当前结果和边界 |
| --- | --- | --- |
| SRC-OPENAI | 官方[News RSS](https://openai.com/news/rss.xml)1230项XML实际按UTC `[04/22 01:00,04/23 01:00)`筛选，4项；实际打开对应核心原文。 | WebSockets Engineering（原`pubDate`04/22 10:00 GMT）进入贡献/证据判断。Workspace Agents公告及Academy（同10:00 GMT）合一产品说明：共享cloud Agent、审批/连接器/团队导航是既有平台组合，未公开新的执行/恢复机制，贡献前关闭；当前网页GA与原文research preview并存，不能把后发更新回填原事件。Clinicians（15:00 GMT）核心§Designed/Continuing读完，临床应用及HealthBench Professional领域rubric/三医师adjudication是当前暂缓领域研究，不进入主线；99.6%作者评分不外推通用可靠性。RSS不是Research/Index全部历史分页，目录差集尚须处理或精确隔离。 |
| SRC-ANTHROPIC | 官方[Research](https://www.anthropic.com/research)原始HTML定位两项Apr22 `publishedOn`：14:12:30.673Z、14:27:03.434Z；实际进入两篇正文核心方法/边界。 | [81k economics](https://www.anthropic.com/research/81k-economics)是Claude用户自报生产力/职业影响与classifier关联；[survey announcement](https://www.anthropic.com/research/economic-index-survey-announcement)是随机抽取活跃用户的长期调查入口。经济背景不改变当前模型/系统机制，二者具体贡献前关闭，不评分、不扩PDF或社会影响研究。目录窗口邻界与其他入口仍需收口。 |
| SRC-QWEN | 官方`https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`实际取动态目录；[Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b)原metadata04/22T10:00+08，API内articleBody实际读完。 | dense27B模型公开、native vision及已有thinking模式的受限能力比较，没有新训练/架构机制披露。SWE/Terminal等harness、长度/预算条件不同，不能由dense超大MoE榜单推普遍资源优越；`preserve_thinking`推荐不是新增状态一致性保证。贡献前关闭为版本事实，保留官方已披露范围，不给品牌声望评分。静态研究列表及动态分页停点尚未收口。 |

## 后续实际入口与停止范围

下表复用本日实际取得且未改变的入口结果；没有可读历史目录的行保留限制，不作零命中证明。原created/updated不冒充publish。

| 来源 | 实际范围与停止点 | 判断及限制 |
| --- | --- | --- |
| SRC-DEEPSEEK | 官方News可读，邻界为04/24与更早2025条目；Research线索为Feb25 DualPath/Jan28 OCR2及后发V4。 | News不是完整Research；本窗历史研究目录的差集仍需有界处理，不能仅凭News称无研究。 |
| SRC-MOONSHOT | 官方Platform Blog实际26条，最新显示2025-11-07，没有2026历史列表。 | 本窗Blog覆盖受阻；需要本窗官方历史列表或确切原始事件链接恢复，不能记零。GitHub只定点相关原始家族，不全扫PR。 |
| SRC-TENCENT-HUNYUAN | 官方publicList API page1/pageSize100/renderType0实际9/9；本窗邻界Hy3-preview、04/30及02/13。100061原content核心、章节和限制实际读：295B/21B、256K、reasoning模式及案例/榜单/产品说明。 | 没有可定位的新机制披露，仅版本事实/已有架构；co-design口号及成本宣称不足准入。displayPublishTime=1776873600与cover日期Apr23是日期精度，另publicAt/publishedAt/createdAt在后月，不能回填本窗精确首公开。贡献前关闭，不为不影响处置的日期建材料请求。 |
| SRC-ZAI | 官方Research实际15卡，邻界展示May20/04/29/04/07/04/01/03/15；再取原HTML核04/20～21字段是media或页面createdAt/updatedAt。 | 未把页面维护日当论文首公开；可见卡中本窗无日期匹配。历史删除/未列项不由当前目录证明不存在，保留目录局限，不扩整站。 |
| SRC-BYTEDANCE-SEED | 官方get_article_list_v2：paper type1/page_token20/count20返回20、total242/next40，实际邻界May12→Apr8；blog type2/page0返回15、total95/next20，置顶后相邻Apr23→Apr9→Apr1→2025。 | ContextUnrolling1669的日期bucket Apr23与arXiv21921提交时刻不是本窗首发证明；Seed3D2 paper1443 Apr22与blog132 Apr23的bucket也不提供09截点时刻。只隔离这两个具体原始家族的日期，需本窗精确原始公告；AgentWorld1635与18292为已定位旧家族，不重算。本次不为置顶未来或窗外条目扩深审。 |
| SRC-BAIDU-ERNIE | 官方Blog当前第一页10项，邻界May9/04/30/04/15/02/06，已越过本窗。 | 此可见列表无窗内条目；不宣称历史未列研究不存在。 |
| SRC-XIAOMI-MIMO | 官方页面实际8论文/14Blog，未给可恢复的ISO事件日期。 | 历史本窗目录日期覆盖受阻；须相关官方日期索引/事件原文恢复。不由空日期推零，不扩全年正文。 |
| SRC-MINIMAX | 官方EN邻界May27/26与03/18，CN邻界04/27与03/18；Agent Tech Blog原页208085字符无本窗可定位日期。 | EN/CN可见列表无窗内事件；Tech Blog历史日期列表受阻，不把它算空列表。恢复仅需本窗日期索引或确切技术原文。 |
| SRC-GOOGLE-AI | Google Research April Blog archive实际9卡；04/22官方“It's all about the angle”核心为3D camera/recomposition→holes diffusion inpaint。DeepMind blog page3原gzip已解码，页面没有可抽取April日期片段。 | Research文章是成熟表示/渲染/补洞组合的受限应用，贡献前关闭；Blog不替代Publications。Research Publications与DeepMind历史本窗目录的确定性停止依据尚需收口/精确隔离，不能以regex未命中宣称无论文。 |
| SRC-META-AI | 官方Research动态入口在本次可读响应中未恢复历史论文列表。 | 本窗历史目录受阻，需可读官方本窗列表/确切原始事件；不以JS空壳作零命中。 |

OpenAI Research Index本次CLI 403、网页只显示Sep23→Aug18及Load More，未取得本窗历史分页；RSS已核事实与Index差集分开，隔离未恢复Index覆盖，不称RSS全站替代。Anthropic核心事件和Qwen动态/静态已有原始结果继续核邻界停止，尚未借这些记录宣布全日Coverage、候选冻结或Books完成。arXiv有界窗口筛选及日期合并见本日screening/checkpoint。

### 两个可恢复目录的实际停止依据

Anthropic Research原始HTML本轮已取得可读的连续列表：本窗Apr22两项之外，下一邻界为Apr29/30，前邻界为Apr14 automated alignment（13:01Z）、Apr9 trustworthy（16:34Z）、Apr7 Mythos（09:35Z）和Apr2 emotion（10:56Z）。此前两项原始publishedOn及核心原文判断不变；这一有界可见目录已越过窗口，不再留普通分页待办。当前可见目录不证明历史删除项不存在，不扩其全文或经济研究。

Qwen动态API再次实际取得40项数组，April相关项为Apr2 04:00+08 Plus、Apr15 10:00 35B-A3B、Apr18 10:00 Max Preview、Apr22 10:00 27B、Apr28 10:00 Flash QLA和Apr29 12:00 Scope；Apr18/28夹住已审Apr22事件，数组日期已实际解析并越过窗口。原静态60项及一次仅旧2025项的响应不作零命中证据；以本次实际40项的窗口邻界收口动态目录。27B核心原文仍为版本事实的前分母关闭，不因入口恢复而新增候选。
