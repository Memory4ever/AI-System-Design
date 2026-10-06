# 2025-07-03 增量补查来源范围独立检查

复核者：Codex / July03 source reviewer，非本轮 root 作者。日期：2026-10-11。仅核本日来源实际获取、查询参数、结果形态与有限停止，不审论文贡献、23 题摘或必要核心，不授 DAY。

**结论：来源获取与有限停止范围已独立核清；须按下列实值写回，受阻项不授正面 Coverage。** 不要求重扫机构、读完月库存或翻所有后页。root 的 README 整理、另一独立复核者的题摘裁决及最终日级工作仍属各自范围，本文不把它们宣称完成。

## 1. 上下文与证据权限

换日重新读取当前 AGENTS、Research / Report V3、Sources 使用说明 / 每日14源 / arXiv范围、Prompt、ROADMAP和 State 的2025路由，仅加载 July03 材料，未重新加载十月材料。原窗口 `2025-07-02T09:00:00+08:00 ～ 2025-07-03T09:00:00+08:00` 冻结，本轮新增窗口为 `2025-07-02 ～ 2025-07-02` 自然日。原候选0不因发现库存数改变。

以[作者补查记录](supplement-20261007.md)与[本轮原件](supplement-20261007/)核差额；[SOURCE_NOTES](SOURCE_NOTES.md)及[README](../../03/README.md)目前的旧轮来源表只保留旧权限，不据旧完成标签认证本轮。本文仅使用来源列表、日期字段、身份及分页元数据，没有进行新的网络请求或浏览器操作。

本轮非论文来源 / 发现请求记录共49份：HTTP200共34、400共6、403共1；另4次超时（returncode28 / HTTP000）、3次连接重置或SSL失败（35 / 000）、1次URL语法错误（3 / 无HTTP状态）。41份有对应raw，8份失败请求无raw。HTTP200包含初始空表单，不能统称34个有效查询结果。记录保存URL、checked_at、returncode、http及error，但没有原响应长度 / SHA256字段；本次本地计算指纹用于保护文件，不假称与作者哈希收据核对通过。

**Google网页和Hunyuan浏览器观察的权限：** 正确DeepMind publications page2、Google July archive的成功网页范围来自作者 tool observations，见作者补查记录。对应本地curl失败且无raw，本文没有自证网页读取、重放工具结果或复现浏览器。Hunyuan浏览器创建超时 / reset也仅继承作者观察；可独立验证的是保存的SPA和API原件，不声称点击过“全部”。

## 2. 六 Advanced 查询的实际范围

独立用HTML结构解析 `li.arxiv-result` 的首个abs身份与页面结果标题，不通读结果摘要；六个成功结果为 `advanced-original-*`，与 `query-inventory.json` 的90身份集合一致。Computer Science / include cross-list、all字段，日期过滤为 `submitted_date_first`、`2025-06-30` 至 `2025-07-02`；实际成功排序为 `-announced_date_first`，`advanced=`、start0、size25。这是提交池发现条件，不是新增7月2日首次公开事件条件；排序与日期过滤不可混同。

| 查询及原响应 | 实际结果 / 页面总数 | 首页最后身份与停止 |
| --- | --- | --- |
| [language model](supplement-20261007/advanced-original-model.raw) | 25 / 254 | 2507.02008；有Next/start25，未执行后页 |
| [transformer AND training](supplement-20261007/advanced-original-training.raw) | 25 / 52 | 2507.00287；有Next/start25，未执行后页 |
| [mixture of experts](supplement-20261007/advanced-original-moe.raw) | 6 / 6 | 2506.23635；当前查询结果末项 |
| [world model OR vision language action](supplement-20261007/advanced-original-multimodal.raw) | 25 / 105 | 2507.00984；有Next/start25，未执行后页 |
| [agent AND memory](supplement-20261007/advanced-original-agent.raw) | 12 / 12 | 2506.23689；当前查询结果末项 |
| [inference AND GPU](supplement-20261007/advanced-original-inference.raw) | 6 / 6 | 2506.23635；当前查询结果末项 |

合计 **99次出现 / 90唯一发现身份**，不是99篇当日论文，也不是90项必审队列。部分身份的原公告月份较提交筛选月份晚，进一步说明不能借此授具体公开日；本次不作它们的贡献或日期准入裁决。未读取后页是明确的有界停止，不是访问故障，也不称全部254 / 52 / 105条已筛选。

初始 `advanced-{model,training,moe,multimodal,agent,inference}.raw` 六份HTTP200均为Advanced Search表单，没有result条目；`advanced-valid-*` 六份为HTTP400 / Bad Request。二者都不是no-hit，不提供零事件或阴性覆盖。成功恢复后的六份与这些失败阶段分别保留，不按文件名“valid”推定有效。`arxiv-cl-first25.raw`请求为July月列表skip0/show25，只作有界标题导航，不授整个分类或本日公开覆盖。

## 3. 每日14来源的可用实值

下表“独核”均指保存原件 / 请求的本地读取，不是本次实时网页访问。成功获取与来源覆盖是两层。

| 来源 | 实际获取与可验证停止 | 限制 / 可结束权限 |
| --- | --- | --- |
| SRC-OPENAI | [RSS原件](supplement-20261007/openai-rss.raw)独立XML解析1251项；近窗BJT7/1 18:00 Genspark →7/8 15:00教育合作，没有7/2 feed项。Research请求HTTP403。 | 可结束该feed的有限检查，不能把403或feed可见段推为全部Research无事件；旧1247与当前1251分开。 |
| SRC-ANTHROPIC | [Research raw](supplement-20261007/anthropic-research.raw)含174处publishedOn字段；[结构化inventory](supplement-20261007/anthropic-publication-inventory.json)172个唯一slug/date，日期能回对解码Flight。近窗UTC6/27两项→7/15，日期字段不是图片创建日。 | 只支持当前保存research目录 / 日期范围，不称172篇正文已读或全站召回。 |
| SRC-GOOGLE-AI | [错误query page2请求](supplement-20261007/deepmind-publications-p2.request.json)为SSL失败；[正确publication page2请求](supplement-20261007/deepmind-correct-p2.request.json)为40秒超时。作者工具观察：`/research/publications/?page=2`是page1；从真实Page2链接进入`/research/publications/page/2/`，30卡Oct30→Mar28，近窗July13→July1 Refract→June26。July archive两次curl超时，作者工具观察9卡July29→July2；年度Pubs language-model请求亦超时。 | 30卡 / 9卡 / 错query实际呈现均明确继承作者tool observations，非本次独核网页。不能用旧DeepMind blog page5/6冒充publication页，不能用年度Pubs失败记空目录。SpeechCompass未变旧范围判断只复用，不重审正文。缺历史pubs / 日级事件范围，保留受阻。 |
| SRC-META-AI | [Research请求](supplement-20261007/meta-research.request.json)连接重置35/000、无raw。第一次page6 URL含未转义方括号，returncode3，尚非有效网络获取；[转义后恢复请求](supplement-20261007/meta-historical-p6-recovery.request.json)仍连接重置35/000、无raw。 | 不能称page6已读或零条研究。必要历史目录未回，受阻隔离；语法错误不是“Meta服务器无数据”。 |
| SRC-QWEN | [page2 raw](supplement-20261007/qwen-p2.raw)五卡：July22→June27 / June26→June5→April29，含Next且页面提示新blog迁移。 | 可停于这一已跨目标日的旧站列表段；Next未执行不是故障，不授新站迁移后的全研究历史。 |
| SRC-DEEPSEEK | [updates raw](supplement-20261007/deepseek-updates.raw)日期序列的近窗August21→May28，页面含2026至2024公告。 | 当前官方changelog可见范围可结束；不外推全部research / release。 |
| SRC-MOONSHOT | [Kimi Blog raw](supplement-20261007/kimi-blog.raw)近窗July11 K2→May6 thinking，无可见7/2卡。 | 仅可见Blog段，不把仓库普通commit当发布，不授未展示历史完整性。 |
| SRC-TENCENT-HUNYUAN | [Research raw](supplement-20261007/hunyuan-research.raw)为SPA；[publicList raw](supplement-20261007/hunyuan-list.raw)code0、totalNum9/list9；[请求](supplement-20261007/hunyuan-list.request.json)保存POST pageNum1/pageSize100/renderType0。9个displayPublishTime独立换算全部2026，最早BJT2026-02-03、最晚09-22。 | page1的这个payload读完，不等2025“全部”研究目录恢复。浏览器超时来自作者观察，非本次浏览器验证；历史2025缺段受阻隔离。 |
| SRC-ZAI | [page2 raw](supplement-20261007/zai-research-p2.raw)可见18个dated card，2026/08/26→2025/12/07及“没有更多”。 | 本轮是18，不沿用旧20；只说明当前返回页，July历史未回。没有执行浏览器翻页验证，不补造全历史分页。 |
| SRC-BYTEDANCE-SEED | [type1 token0](supplement-20261007/seed-us-1-0.raw)18、[token20](supplement-20261007/seed-us-1-20.raw)20，38唯一ID；[type2 token0](supplement-20261007/seed-us-2-0.raw)18、[token20](supplement-20261007/seed-us-2-20.raw)18，36唯一ID。均真实sub_article_list；请求头x-tt-locale=US，count20/order_desc=true，token20均next40/has_more=true，total94/45。 | 两个已读payload恢复旧metadata-only问题，不能继续把同一已取数组列为缺失。BJT论文July10 / July4→June27，blogJuly15 / July14→June28 / June25，所读记录无7/2；不代表94 / 45全站、全部正文或无遗漏，剩余可见差额与历史完整性保留。 |
| SRC-BAIDU-ERNIE | [page2 raw](supplement-20261007/ernie-p2.raw)六卡November11→June30，末页界面，无7/2卡。 | 该可见Blog段可结束，不搬June30事件或外推全机构。 |
| SRC-XIAOMI-MIMO | [8557 raw](supplement-20261007/mimo-home-8557.raw)首页Blog数组15项、initialVisibleCount8；[6159 raw](supplement-20261007/mimo-home-6159.raw)组件按`o.slice(0,c)` / `o.slice(c)`分组，More只切换本地useState；Paper数组8项日期为2025 May12 / June4 / Sep19 / Oct21及2026 Jan8 / Feb3 / Mar13 / June29。 | 静态组件代码可验证本地展开，不是假装点击验证。15博客不能写“全2026”：末项HSS在[route/frontmatter原件](supplement-20261007/mimo-page-bundle.raw)日期2025-12-19。未带日期或未匹配metadata的路由不猜年份；July2025 Blog历史仍未恢复，不授来源无事件。 |
| SRC-MINIMAX | [英文raw](supplement-20261007/minimax-en.raw)12张dated card，最旧2025-10-27；[中文raw](supplement-20261007/minimax-zh.raw)13张，另含2025-01-15而未展示June M1。 | 只核当前列表，不完整chronology或July无事件；历史目标段受阻隔离。不因当前列表存在就声称新增按需 / 周级来源已扫描。 |
| SRC-ARXIV | 见§2六查询99出现 / 90唯一的真实结果及第一页停止，初始表单、HTTP400、月标题导航均分别界定。 | submitted / 公告排序或月份不替代具体首公开日。论文题摘、贡献准入、日期恢复及必要证据交其他复核链，不由本来源检查授通过。 |

## 4. 给 root 的精确写回校正

1. 将本轮99出现 / 90唯一、六查询逐个结果数及三个有Next的首屏停止写成发现范围；初始form200与随后400不能标无命中，成功阶段才有真实结果。
2. Seed本轮38论文 / 36博客、四个真实数组与next40写回；旧metadata-only为旧轮事实，不再作为已恢复payload的当前请求。未取余页不改为故障，也不能写已穷尽94 / 45。
3. MiMo保留8557的15项 / 初显8和6159本地slice / toggle事实；明确至少HSS为2025-12-19，删除或限定本轮“blog当前仅2026”的外推。不从模型版本名猜其余路由日期。
4. Hunyuan9条全部2026、2025目录未回；本次复核未获UI，浏览器创建超时仅继承作者观察，不能写“全部”按钮操作通过。
5. Google正确publication `/page/2/` 与错误 `?page=2`、旧blog page5/6分开；30卡 / 9卡写为作者网页工具观察，curl失败和没有raw的事实同时保留。Meta语法错误与修复后连接重置分别写，不称失败请求读回目录。
6. 本轮RSS1251、Anthropic174字段出现 / 172唯一记录、Z.ai18卡与旧轮1247 / 20分开，原件不覆盖；各项仅授保存的目录段权限，不升级为全机构无事件。

这些是root当前六节整理中的具体普通写回事项，不是外部访问故障。本文没有编辑README，也未核作者写回后的实际正文；来源限定事实可直接复用，无需重抓同入口。

## 5. 可结束边界与重开

本次来源范围复核本身完成；可结束已执行的有界发现和可见日期段，不要求90身份逐项关闭、三处Next全翻或全部论文全文。尚未恢复的OpenAI Research、Google Pubs、Meta、Hunyuan2025、Z.ai July、MiMo July Blog、MiniMax历史段及Seed / Qwen等未展示完整性，只能按具名限制隔离，不授正面Coverage或“本日零事件”。可接受重开材料为各源可核7月2日的官方历史列表 / 公告 / 原文发布；到达后仅重开该源该窗或对应身份，不扩全月 / 全站。

初始表单及400已由真实结果恢复，Seed数组已取到，MiMo本地展开机制已从原件核实；不能继续把这些已解决事项列为受阻。未执行的作者写回、题摘独立核或必要事件处置亦不能改成外部终态。本文不裁决论文日期准入、证据 / Books或整日完成；root应合并另一独立复核结果后据实际剩余工作作DAY判断。

## 6. 校验与写入范围

本线程仅以apply_patch新增本文，不改README、State、Books、作者记录或原件，不执行Git写操作；未stage / commit / push。只读运行当前README的V3：1份V3 schema / consistency通过，不能替代本文来源语义检查或尚未完成的DAY。本文本地引用、Markdown / 尾空白、限定diff及既有同日文件保护的写后结果记下方。

写后检查：本文34个本地路径引用全部存在，尾空白 / NUL无错误；新增文件限定no-index diff-check无错误输出，返回1只表示相对空文件有新增内容。实际读回正文。运行前325个既有同日文件SHA256均未变；同日另新增`second-calibration-supplement-20261011.md`为并行任务产物，本线程未写、未读取其题摘结论、不回退。README和既有原件保持原样，本文不声称共享任务已闭合。

## 7. 新差额：22项精确v1独立准入校准

2026-10-11，用户另行授权接[作者新增观察](resume-observations-20261011.md)的22项。下文是本文来源复核完成后的新增职责，不追溯改变§1～6的来源证据权限。重读当前Research / Report、Prompt、Sources每日与arXiv范围、ROADMAP及State2025路由，只加载July03；复用首14及另一复核链的23项，不重复其题摘 / 9core，不扩month25或query90的页数、池或日期。

**实际独立读取：22/22官方精确v1的完整题名、摘要及身份字段。** 仅为决定准入补读01264v1 §III/IV、00214v1 §3～6与附录A.2、00355v1 §3～5、00601v1 PDF §III/IV、00606v1 §3/4、05125v1测试执行 / 评价段；00297v1仅PDF封面与§1.2家族目录，另定点核两个目录指定的早期原始身份，不通读博士论文。SAFER只补必要版本页。网页工具实际返回可读文本，不是继承作者题摘，不声称浏览器操作、本地raw保存、代码核验或实验复现。00601 PDF文本可读；两次页截图返回Cache miss，未获像素验证。00540 PDF请求返回Internal Error，关闭只基于已完整读取的v1题摘，不假称读过其PDF。

**裁决：18P、3C、1V，数量恰与作者初判相同，但成员不同。00601由P拟改C；00606由C拟改P。** P是明确潜在贡献，不是当窗候选或已完成Evidence；C是本次贡献关闭，不否定学术价值；V是具名版本隔离，不是访问受阻或全部版本撤回。各P的本次首次公开日仍未确认，不由submitted、ID、查询月份或一般公告日程反推July02。原候选0、原日期、原09:00窗口和既有有效审阅冻结。

| 精确v1 / 本次裁决 | 约束 → 原文增量 → 需重估的选择；采用边界 |
| --- | --- |
| [00390 MoNE](https://arxiv.org/abs/2507.00390v1) / P | 专家常驻内存而单看路由频次不足 → 联合访问频次 / 输出方差，用novice估计替代冗余专家 → 重估裁剪与校准稳定性。Owner `MODEL-MOE`；不把摘要的无偏 / 鲁棒说法当已证明。 |
| [01016 VQ-VLA](https://arxiv.org/abs/2507.01016v1) / P | 动作表示规模与迁移受限 → 大量合成轨迹训练VQ tokenizer → 动作编码与真实域差距须联合评价。Owner `MULTIMODAL-EMBODIED-VLA`；两真实任务不授通用sim-to-real。 |
| [00938 WebArXiv](https://arxiv.org/abs/2507.00938v1) / P | 动态网页 / 固定历史使评价及反思失真 → 固定snapshot、确定答案与动态选择历史 → 重估可复核评价及反思上下文。Owner `PLATFORM-EVALUATION-SYSTEM`，历史选择交接 `AGENT-REFLECTION`；**v1为275任务，不能沿用当前版510**。 |
| [00401 MIV-head](https://arxiv.org/abs/2507.00401v1) / P | 冻结骨干不能适配 → 将分类改写为多实例验证并训练head → 改变低访问权限下的适配选择。Owner `MULTIMODAL-REPRESENTATION`；CNN/ViT、ImageNet1K条件不外推闭源LLM。 |
| [01264 Driving Video](https://arxiv.org/abs/2507.01264v1) / P，窄设计边界 | 符号场景可控不等生成画面事件保真 → Scenic/CARLA到条件视频的交接 → 不能用视觉真实度代替碰撞 / 时序条件验证。Owner `MULTIMODAL-WORLD-MODELS`；增量不计在借用的Cosmos/ControlNet成熟机制。必要读段见§8。 |
| [05125 Robotic BDD](https://arxiv.org/abs/2507.05125v1) / C | 原文确有时间约束、DSL/图谱到可执行BDD测试的贡献；实际测试对象为Isaac Sim现成pick-place程序。增量止于通用机器人验收建模，未建立学习模型 / VLA / 环境预测的具体机制或独有可靠性条件；不凭机器人类别、无owner或日期关闭。 |
| [00152 TableEval](https://arxiv.org/abs/2507.00152v1) / P | 通用表格分数掩盖领域和表示差异 → 五格式、跨域与context相关性比较 → 改变评价切片。Owner `PLATFORM-EVALUATION-SYSTEM`；科学表格是模型能力对照，不误关为暂缓的科学应用。 |
| [00210 LineRetriever](https://arxiv.org/abs/2507.00210v1) / P | 语义相似 / 截断遗漏行动信息 → 按planning horizon挑观察行 → 当前动作所需信息不等文本语义相关。Owner `AGENT-CONTEXT`；selector成本和动作成功条件待证。 |
| [00214 Reasoning-Infused](https://arxiv.org/abs/2507.00214v1) / P，局部监督边界 | 标签条件rationale构造后，Q→RA与Q→A对照 → 监督形式可能改变预测，却可伤害少数类 / 产生不忠实解释 → 重估rationale质量门。Owner `TRAIN-SFT`；不是已证通用推理迁移。 |
| [00216 RASTA](https://arxiv.org/abs/2507.00216v1) / P | 翻译语义相近仍可能风格失配 → 学得风格概念的检索式对齐与非西方语言失败 → 重估文化 / 风格条件评价。Owner `AGENT-RAG`；不授普遍文化理解。 |
| [00239 Refused Knowledge](https://arxiv.org/abs/2507.00239v1) / P，安全反侧 | 拒答不等表征信息消除 → 线性probe、base到aligned迁移与间接输出相关 → 拒答与遗忘应分开验证。Owner `PLATFORM-SECURITY`；偏见预测值不等现实事实，相关不证因果使用。 |
| [00246 EfficientXLang](https://arxiv.org/abs/2507.00246v1) / P | 英文默认推理预算 → 三模型 / 七语言且回译trace仍有差异 → 重估语言与推理预算关系。Owner `MODEL-TOKENIZER`；token量不等端到端时间、价格或各语言通用最优。 |
| [00258 Memorization](https://arxiv.org/abs/2507.00258v1) / P，隐私反侧 | 适配效用相近不等记忆风险相近 → prompt / parameter微调的MIA比较 → 更新方式须同时评估泄漏风险。Owner `PLATFORM-SECURITY`；低MIA不等DP或全面隐私保证。 |
| [00322 Interference](https://arxiv.org/abs/2507.00322v1) / P，可靠性反侧 | 输出错误不必说明缺正确部件 → heads / FF贡献竞争与RASteer → 机制存在和输出可靠性分离。Owner `MODEL-TRANSFORMER-LAYER`；124M～7B、括号 / 算术条件不授任意推理修复。 |
| [00355 Question Decomposition](https://arxiv.org/abs/2507.00355v1) / P，局部质量 / 资源条件 | 多跳证据分散 → 分解扩大池、rerank控噪并作四配置比较 → 重估覆盖、指标与延迟的取舍。Owner `AGENT-RAG`；不能只称“现成模块”，也不能称所有证据指标更优或成本未披露。 |
| [00389 CAPITAL](https://arxiv.org/abs/2507.00389v1) / P | CoT投票未控虚假相关 → front-door分解与聚类/NWGM/对比学习近似 → 重估推理链选择。Owner `AGENT-PROMPT`；因果识别假设及近似有效性未审完，不授真实因果。 |
| [00509 Ad Co-Evolution](https://arxiv.org/abs/2507.00509v1) / P，安全反侧 | 检测分数被误当透明可信 → 检测器指导SFT / BoN降低广告可检测性 → 固定评估器遭优化后的适应风险。Owner `PLATFORM-SECURITY`；不关成广告应用，不传播隐蔽操作，不授跨检测器通用成功率。 |
| [00601 Low-Resource Transfer](https://arxiv.org/abs/2507.00601v1) / **C，改判** | PDF明确为Adapter/LoRA式可调模块、普通L2对齐、soft prompt、正则与冻结组合。必要对照未建立区别于成熟组件的机制或成立条件，汇总分数无法识别组件增量；不能据泛称framework形成长期设计命题。不是因日期、费用或读PDF费时关闭。 |
| [00606 Mixture of Reasonings](https://arxiv.org/abs/2507.00606v1) / **P，改判** | 手工任务prompt → 教师从采样模板中按题选择、生成并筛正确答案后SFT → 潜在改变策略监督的构造与模板多样性选择。Owner `TRAIN-SFT`；正文足以推翻“无selector”的宽关闭，但不证明学生内部自主路由。 |
| [00297 African Languages](https://arxiv.org/abs/2507.00297v1) / P，**更早家族门** | web噪声 / 未见语言 → 质量而非仅数据量、少量单语数据适配 → 重估数据与跨语言预训练条件。Owner `TRAIN-DATA`；不因博士体裁关闭，但已核两个旧公开家族，不能将其重复计为July02新贡献，见§9。 |
| [00540 Capsule Intent](https://arxiv.org/abs/2507.00540v1) / C | 完整题摘描述现成CNN、capsule routing与margin loss用于intent，比较仍为领域指标及routing次数。未提出新的通用学习机制或足以修正主线表示设计的条件；不是因小模型或旧方法而一概关闭。 |
| [00665 SAFER](https://arxiv.org/abs/2507.00665v1) / V，保留安全潜力 | SAE特征信号指导偏好数据改动，潜在改变reward安全审计，拟归 `TRAIN-RLHF`。v2撤回 / v3恢复正文事实各自独立；本次不以新版恢复授v1采用，也不宣称v1官方撤回，详见§9。 |

## 8. 决定准入的最小核心与反证

**01264v1：** [§III-A/B、IV-A/B](https://arxiv.org/html/2507.01264v1)可核脚本到结构控制图再到视频的链路；方法写segmentation/depth，实验写edge/depth，尚须解释。实验声明每类20变体、展示三类各三碰撞样例，视频比较仍定性；没有用事件 / 时序指标证明条件保真。P限定为这条交接的设计验证问题，不授底层模型新颖性、安全测试有效性或sim-to-real。本文未读其他章节，更未观看 / 逐像素验证视频。

**00214v1：** [§3～6及A.2](https://arxiv.org/html/2507.00214v1)说明标签只用于离线训练rationale构造，推理输入仅Q，不能误称推理时输入真标签。单emotion测试中Q→RA总体准确率58.4对49.7，而surprise从13.8降到1.5；原文还展示标签正确但解释错位的反例。因此局部实验确会改变“解释监督总是更好 / 解释即忠实”的选择，保留P。未隔离额外输出token、教师数据 / 合理化影响，不采用通用泛化或机制因果归因。

**00355v1：** [§3～5、Tables1～4](https://arxiv.org/html/2507.00355v1)有naive、QD、RR、QD+RR，最终k=10，但RR初池20、QD用原问题及至多五子问题，不能称等检索预算。Hotpot支持事实EM/F1反而RR更高；250个MultiHop问题的retrieval-only延迟为0.03 / 0.88 / 16.7 / 18.9秒，并非无成本披露。缓存去掉QD调用不去掉rerank开销，不能照录“与baseline同延迟”。局部补充证据 / 噪声 / 成本取舍足以P，非已验收端到端收益。

**00601v1：** [PDF §III/IV，物理页2～4](https://arxiv.org/pdf/2507.00601v1)的公式为L2特征对齐、soft prompt拼接及参数偏离正则，冻结本体仅更新适配模块；没有具体新增运算或组合成立条件。Table1拿Ours与不同多语骨干作汇总比较，Ours底座 / 选定训练样本及配对对齐实现不清；稳定性分数无可核定义 / 重复条件，伪数据曲线也没有控组件对照。这不是“细节不足就否定潜力”：补读后实际增量仍仅拼装与未归因的领域指标，故C。将来只有具体新增机制或可比的条件性证据才重开，不索要全论文 / 全代码。

**00606v1：** [§3、§4 / Table1](https://arxiv.org/html/2507.00606v1)实际有教师从随机五模板选择策略、按正确性筛生成结果再SFT，不能写“完全无选择步骤”。模板规模与IO/CoT结果不单调，潜在监督选择命题可进入后续证据层；P严格不等学生自主自适应已证。没有相同数据量普通rationale蒸馏 / 随机模板的对照，故不采用“自主选择”“模板越多越好”或普遍收益；非因样本少、收益小而关闭。

**05125v1代表C：** [测试执行与§V](https://arxiv.org/html/2507.05125v1)确有计时、碰撞 / 放置判断及机器人 / 位置 / 容器变化，不能写完全无可靠性实验。其step函数人工实现并测试Isaac Sim提供的pick-place，新增是通用验收规格与生成测试；未给学习策略、生成模型或模型驱动闭环的新增成立条件，不将这套通用软件测试类比当项目准入。00540不需要为已明确的题摘关闭无限恢复PDF。

安全反侧00239、00258、00322、00509均已独核完整v1题摘，具体潜力见表。它们不可因负面、隐私、广告应用或“不产新模型”关闭；本文未深审其威胁模型、可比预算与普遍性，不把作者实验视为独立复现。SAFER隔离亦不取消这四项有效潜力。

## 9. 日期家族与SAFER版本门

**00297不是纯“日期未知的新论文”。** [v1 PDF封面及§1.2](https://arxiv.org/pdf/2507.00297v1)写Saarbrücken2022、答辩2023-06-27，并将章节明确映射到2020～2022已有论文。封面 / 答辩本身不证明首次公开日；但目录的两个相关身份已定点回到原始入口：数据质量 / embeddings对应[2020.lrec-1.335](https://aclanthology.org/2020.lrec-1.335/)，出版页实载2020年5月；少单语语料 / 多语适配对应[2204.06487v1](https://arxiv.org/abs/2204.06487v1)，原始稿身份为2022。这证明至少所列两条贡献家族已有更早公开材料，不是由2507 ID推日期。保留主题P，不计这些旧贡献为July02候选；作者若主张2025新增，须给区别于旧家族的具名命题与首次公开证据。不扩读旧论文方法、博士其余章节或所有历史家族。

**SAFER版本实值：** 独核[v1](https://arxiv.org/abs/2507.00665v1)、[v2](https://arxiv.org/abs/2507.00665v2)、[v3](https://arxiv.org/abs/2507.00665v3)。v1可读；v2于2025-10-14 withdrawn，comments明确为某机构需额外发表批准，**不是已公布实验错误**；v3于2026-01-30恢复正文。v1页面的旧缓存还只展示v2，不能当当前版本总史；v2 / v3页可交叉看到三版本。不能写全部版本撤回、v1实验被证伪或v3追认v1；亦不能从作者名单变化自行推断撤回原因。

V表示保留作者所设早期采用门，不授v1评分 / 采用 / Books；重开要点是具名解释v2审批撤回、v3修订与v1拟用命题的关系，以及v1本次首次公开归属。若这些处置尚未执行，是普通版本核对待办，不能仅凭网页能读就报Evidence完成，也不能把v2撤回改称访问失败。本文不机械比较v1/v3全文。

## 10. 本轮结束边界与验证

新增22项准入校准至上述最小范围完成。给root的实质差额为：00601改C、00606改窄P；00214保留少数类 / 不忠实解释反侧；00355写入已披露延迟、非全指标改善和非等候选池；00297保留更早家族门；SAFER记录审批原因而不扩大撤回。01264不能按底层成熟模型评分，WebArXiv不得回用当前版510。其余明确P可停题摘，不要求机械全文来换日期证据。

本文不确认22项中的任何新增July02事件，不评分、不作Books覆盖判断，不授最终DAY或正面Coverage / Evidence。来源读取仍按§1～6独立边界，不再扫描；作者新增Meta page6成功仅继承[其tool observations](resume-observations-20261011.md)，未由本复核重放，不能消除先前Research reset或授July完整历史。最终README仍须root把上述成员改判、具名日期 / 版本门及真实普通待办写回，再交非作者日级包。**README未整理、必要处置未执行均不能伪称外部受阻或待办0。** 原§4 / 旧有效结果不因本轮潜力表改写；外部受限项仅按具名权限隔离。

本次仅apply_patch追加本文；未改作者观察、原件、README、State、ROADMAP、Books或索引，未stage / commit / push。写前只读V3检查当前July03 README：1份V3 schema / consistency通过，不是本轮语义 / DAY验收。追加后的本地引用、原文前缀保护、限定diff与文件指纹结果记录如下。

写后实检：本文36个本地路径引用全部存在，无尾空白 / NUL，§1～6运行前全文前缀逐字保持。326个既有同日其他文件SHA256全部不变，无新添同日文件；作者观察、State和ROADMAP保护指纹不变。本文限定diff-check通过；相对空文件的no-index check无错误输出，退出1仅表示有差异。

**当前README的V3最终实值为失败，不能沿用写前通过。** 并行root已改变README指纹；两次写后只读检查均返回：六个固定二级章节顺序缺失、两处来源行列数错误、候选表列定义不匹配。定点读回发现README行44前缺第3节标题，行46～47的五列候选表因此仍落在第2节来源覆盖内，可直接解释上述结构 / 列数错误。请root恢复当前合同第3节标题并再跑V3；这是普通可执行整理，不是外部阻塞。行57虽声明新轮普通待办，行59及旧§6仍保留“无可执行工作 / DAY已完成”，必须在最终包清楚标为原轮而非本轮。本文未修README，未做其完整日级语义验收；所有校准结果仍须写回实际六节再交包。

## 11. SAFER版本普通待办定点关闭：V改窄P

2026-10-11，按用户追加授权，仅核2507.00665版本门。**本段取代§7 / §9的SAFER旧V及“先等作者澄清”的门；SAFER现为窄P，版本核对普通待办关闭。这批22项更新为19P / 3C / 0V。** 其他21项和来源范围不重开，旧记录只保留判断演进，不再作为当前采用隔离依据。

实际独立重读[v1完整题摘](https://arxiv.org/abs/2507.00665v1)、[v2状态及comments](https://arxiv.org/abs/2507.00665v2)、[v3完整题摘](https://arxiv.org/abs/2507.00665v3)及[当前官方入口](https://arxiv.org/abs/2507.00665)。当前入口明确指向2026-01-30的v3，有正文且不标当前版本撤回；v2仍为2025-10-14 withdrawn，说明为机构发表审批，未声明实验错误。v1缓存的“较新版本撤回”提示不能覆盖当前官方恢复状态。官方恢复足以解除这项因审批撤回而设的旧准入门，不等于官方替实验真实性背书；v2自身仍不评分 / 采用。

为核决定性命题，只比较[v1 §2.2.1～2.2.3](https://arxiv.org/html/2507.00665v1)与[v3同名窄段](https://arxiv.org/html/2507.00665v3)，未全篇diff。两版均为reward隐藏表示经SAE、chosen/rejected特征对比、筛选安全相关特征后评分偏好数据；v1式9与v3式6的特征对比分数相同，v1式11与v3式8～9的偏好评分只是等价拆写。v3补充上下文相关语义 / 数据集级信号解释，没有改变这条链路的符号方向或撤销其潜力。题摘保留同一机制及安全影响主张，警示措辞等文字调整不是实验勘误。v3目录另有消融扩展条目，本文不采用未读的新消融结果，也不据此虚构v1结果被修正或两版全文完全相同。

**当前可保留命题：** reward标量不透明且偏好数据敏感 → SAE特征对比用于定位安全相关数据影响 → 有理由重新考虑只看总reward的安全审计 / 数据处理选择，Owner仍为 `TRAIN-RLHF`。这是v1自身已有的窄贡献潜力，不从2026版反填2025结果。所核题摘 / 决定性方法及官方说明未出现取消这项P的实质冲突；因此没有具名必要版本问题要继续隔离，不机械索要作者证明“所有版本无差异”。

**仅剩v1本次首次公开日。** 可接受当期官方公开列表 / 公告或作者首次公开原文日期；submitted与ID不替代公开日，v3恢复日不迁移v1归属。日期到达仅重开2507.00665v1的日期准入，然后按届时拟采用命题开展必要证据审阅；现在不评分、不授Evidence完成、普遍安全保证、Books或DAY。因果解释、定量安全效应及chat能力不受损等仍未由本次版本核对证明，它们属于日期准入后正常证据问题，不是继续维持V或当前等待作者澄清的理由。以后若出现具体勘误或同条件相反结果，再只重开具名受影响命题。

本次重读适用AGENTS / 合同 / Sources每日与arXiv范围 / Prompt / ROADMAP及State2025路由，仅追加本文，不改README或其他文件，无来源重扫、无扩日、无stage / commit / push。只读V3当前July03 README为1份V3 schema / consistency通过；这是本次实值，§10的失败是先前并行整理阶段结果，不再作为当前格式结论，也不替代root最终六节的日级语义验收。追加检查结果记下方。

写后核验：运行前全文前缀保持，36个本地引用全部存在、无尾空白；限定diff-check无错误，no-index退出1仅表示新增内容。326个既有同日其他文件指纹不变，无同日新增文件。实际读回本段，只有本文追加发生。
