# Daily Research — 2025-09-26

**规范：** V3
**窗口：** 2025-09-25T09:00:00+08:00 ～ 2025-09-26T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T13:42:53+08:00

## 1. 结论

本窗确认1个入选家族GDPval，官方RSS原09:00GMT支持落窗；root独立准入与必要证据判断通过，评分2+2+2=6，1家族深入审阅完成、实际Books整合1处。root已写入Ch66 EvalSpec之后、分析Agent段之前的一自然段，非写入者Archimedes实际原文/正文邻接/末注POST通过，root已同步最终末注；本日root独立DAY实际通过。异构职业交付物要求同时保存参考文件、artifact/rendered form与职业rubric；专家盲比不能由尚未达到专家可靠性的自动grader替代。纯API推理速度/费用不代表真实工作流的总成本。

arXiv三组主题查询195/57/54条，跨分类并集257，均是提交发现线索而非本日公开量。按实际标题收窄的165个相关/含糊条目已读题摘；其中1个截断摘要另从精确v1 HTML恢复。16份必要安全/反侧v1已读指定方法、评价和限制，不声称全文、实现核验或复现。RollPacker同步长尾调度、SuperOffload紧耦合offload、TyphoonMLA共享prefix选择翻转、CORE终态漏路径、FL全局模型抽取有具体潜力，root首批校准已确认潜力；首次公开仍未证实，未评分/采用。Google Wayfinding与LMSYS仍隔离日期依赖；Robotics1.5原schema支持25日08:00北京时间，属于窗外，不假设午夜为占位。

作者侧普通扫描、题摘筛选及必要反侧阅读已落盘，root已实际独核最终六部分、有限来源停点、全部正式候选与必要风险/设计反侧，并对其余关闭分层抽检。可执行研究及必要修正已到安全终态；外部历史公开/目录缺口仍不是正面Coverage/Evidence通过，不用于Books、零事件或无遗漏断言。日级完成不表示165项全部经独立复核。

root DAY抽检指出的五项错误关闭已逐项以精确v1完整题摘纠正：TTS合法schedule reconstruction、MixGate alignment-first、SoM专家文本/视觉误读负侧、RP/Flux混合runtime、Mojo atomic/fast-math portability；均保留具体潜力、日期隔离，不评分/Books。同理由扩查只重开当前关闭集合的TasselNet局部跨尺度表示潜力，其他关闭保持；精确版本/位置/新处置见[SCREENING差额](../_sources/daily-20250926/SCREENING.md)，不扩全文队列。

## 2. 来源覆盖

实际执行于2026-10-06；入口、原响应与失败均保存在[本日_sources](../_sources/daily-20250926/)。以下范围仅回答本窗的有限检查，不宣称机构全部历史召回。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research、原[官方RSS](https://openai.com/news/rss.xml)实际解析本窗；原[RSS](../_sources/daily-20250926/openai-rss.xml)、[解析](../_sources/daily-20250926/openai-rss-window-parse.json)。GDPval09GMT、shared projects11GMT落窗；Pulse00GMT在窗前，不移归属 | 已检查 | 当前Blog论文链接是Oct版，不倒填Sept精确报告 |
| SRC-ANTHROPIC | Research Next.js Flight恢复全部174 publication records至2021，保留原publishedOn；[解析](../_sources/daily-20250926/anthropic-publications.json)。实际数组无本窗字段，不读其他日期正文 | 已检查 | 只支持该官方publication数组，不声明全部互联网无事件 |
| SRC-GOOGLE-AI | Google Research `/blog/2025/09/`首屏12条Sep30至Sep11，越过本窗后停；Wayfinding核心已读。[26open4](../_sources/daily-20250926/26open4.json)。pubs真正`category=2025&search=language model`3页1–37/37；[原页](../_sources/daily-20250926/google-pubs-actual-filter.html)、page2/3保留。DeepMindRSS100条仅到Nov5；Robotics1.5原schema2025-09-25T00Z即25日08BJT，窗外 | 受阻 | 年份catalog不是first-public；Wayfinding日期无TZ，DeepMind当前RSS不覆盖Sept；不以午夜是假时间重开Robotics |
| SRC-META-AI | Research原响应仅title；Blog实际page1–3 metadata、Next真分页，非单调列表含featured旧文，page3普通尾部到Aug/Jul2025后停；[分页](../_sources/daily-20250926/meta-pagination-corrected.json)。目标日期补检未恢复新原文 | 受阻 | Research历史目录未恢复，非单调Blog不授完整历史覆盖；初次误用旧featured停点已补page3，原记录保留 |
| SRC-QWEN | 旧Hugo首屏跨窗停；新官方 `qwen.ai/api/page_config?code=research.research-list` 本日实际请求200，完整JSON数组60项，原date保留；[原响应](../_sources/daily-20250926/qwen-research-api.json)、[60项元数据](../_sources/daily-20250926/qwen-research-metadata.json)。非时间排序，检查全部date后停，无本窗数组项；最近窗前Qwen3-Max原2025-09-24T04Z | 已检查 | 仅支持该官方可恢复数组，不授所有历史修订/发布无遗漏 |
| SRC-DEEPSEEK | 首页后恢复官方news实际侧栏，新闻18项从2026至2024；目标由Sep22与Sep29夹住，未加载窗外正文作本窗候选；[原页](../_sources/daily-20250926/deepseek-news.html) | 已检查 | 当前官方新闻侧栏的有限范围，不授研究全史 |
| SRC-MOONSHOT | Kimi Platform Blog实际26条目录，从2024至2025Nov，Sep16/Sep5均窗前，无More；[26narrow-sources](../_sources/daily-20250926/26narrow-sources.json) | 已检查 | 只支持可恢复官方目录 |
| SRC-TENCENT-HUNYUAN | 首查Research；正确POST `api.hunyuan.tencent.com/api/blog/publicList` `{pageNum:1,pageSize:100,renderType:0}`返回code0/totalNum9/list9；[原响应](../_sources/daily-20250926/hunyuan-api-corrected.json)，均2026。浏览器恢复在本子代理环境不可用，未声称执行过浏览器核查 | 受阻 | 全9条当前目录不是2025历史覆盖；需原2025目录或本窗原文 |
| SRC-ZAI | Research真`?page=2`执行，Flight数组直接JSON解析后18条、hasMorefalse，首页15/hasMoretrue；[成功解析](../_sources/daily-20250926/zai-page2-direct-array.json)，先前解析空结果保留不算0。release notes Sep30/Aug11夹窗 | 受阻 | Research两页仅到Dec2025，createAt也不自动是公开时间，Sept历史缺口 |
| SRC-BYTEDANCE-SEED | type2/year2025/page_token0/count20真实返回15/total49/hasMoretrue；去除置顶后降序最早Jul15，跨窗停，[原响应](../_sources/daily-20250926/seed-blog.json)。type1同请求total94无sub_article_list；page20只恢复SwiftSpec一条，原[page2](../_sources/daily-20250926/seed-paper-page2.json) | 受阻 | Blog本窗有限范围已处理；论文API不是94条零命中，也不是可靠完整分页，需有效目标历史论文记录 |
| SRC-BAIDU-ERNIE | Hugo原RSS全部18项（16 posts+2 sentinel），目标由Oct16/Sep12夹住；[原RSS](../_sources/daily-20250926/ernie-rss.xml)、[解析](../_sources/daily-20250926/ernie-rss-parse.json)，year1导航不算研究事件 | 已检查 | 只支持官方Blog/RSS范围 |
| SRC-XIAOMI-MIMO | 首页8 papers、15 Blog；实际获取home chunks确认More仅slice展开同一静态数组，[home1](../_sources/daily-20250926/mimo-home1.js)、[home2](../_sources/daily-20250926/mimo-home2.js)。Paper Sep19/Oct21夹窗；87路由frontmatter只作日期恢复，不读全部站点 | 已检查 | 部分当前Blog无date；已恢复目录无Sep目标项不授未知日期/全部历史事件 |
| SRC-MINIMAX | EN/CN完整cards12/13，无目录More；[EN](../_sources/daily-20250926/minimax.html)、[CN](../_sources/daily-20250926/minimax-cn.html)。Agent Tech Blog实际200，完整可读目录只有2026-05-13 Agent Team；官方llms.txt全部索引同样只列该技术文章，无历史分页，停；[Agent文本与链接](../_sources/daily-20250926/minimax-agent-text.json)、[索引](../_sources/daily-20250926/minimax-agent-index.txt)、[请求](../_sources/daily-20250926/qwen-minimax-recovery.json) | 受阻 | 公司Blog有限检查已处理；当前Agent目录不授2025覆盖，需目标历史目录或本窗原事件 |
| SRC-ARXIV | language/systems/multimodal三组Atom，start0/max200、total195/57/54。submitted `[202509241800 TO202509251800]`仅发现，跨类257；[题摘](../_sources/daily-20250926/focused-title-abstracts.json)。cs.CL月表2214取1–2000作相关题名补线索；日路径无效、advanced日范围未恢复公告。availability实际说明moderation可能延迟 | 受阻 | 未恢复逐篇first-public公告，不能按submitted或DataCite注册归日；不授月表后214条覆盖或当日零命中 |
| 表外：[LMSYS](https://lmsys.org/blog/2025-09-25-gb200-part-2/) | 由本窗题名触发，只读GB200 PartII必要Methods/Experiments/限制，不扩每周SGLang整站；[原文](../_sources/daily-20250926/lmsys.html) | 受阻 | Blog日期只有Sep25无TZ，first-public区间未确认 |
| 补检：[web search](https://www.google.com/) | 本窗Sep25、机构domain与主题有界查询；原26search1–7保留。早期site词宽噪声不授coverage，后用domain filter；只回原始来源 | 检索受限 | 空/噪声结果不能证明无事件 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Measuring the performance of our models on real-world tasks（GDPval）](https://openai.com/index/gdpval/) | 2025-09-25T17:00:00+08:00 | 文本题无法覆盖职业artifact验收 → reference files/异构deliverables与专家盲比，自动grader未达到专家可靠性 → 评价对象与判分资格需保留；2+2+2=6（Design Delta/System Reach/Durability） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) EvalSpec后实际一段，root写入、Archimedes非写入者POST通过，root最终末注同步与DAY通过 |

GDPval评分和评价对象增量已由root独立校准、必要证据与日级复核通过。日期未决的潜力不列为确定候选；明确关闭及纠正后的当前题摘处置见[SCREENING](../_sources/daily-20250926/SCREENING.md)。

## 4. 证据与知识整合

### [Measuring the performance of our models on real-world tasks（GDPval）](https://openai.com/index/gdpval/)

采用9/25官方Blog发布说明，不采用其当前论文链接`2510.04374v1`倒填Sept原版本。实际核心已读：任务来自44职业/9 sector，1320 full set与220 gold set；reference files与文档、幻灯片、表格等artifact，而非单段文本。专家匿名比较模型与任务作者交付物，职业rubric增加一致性；experimental automated grader尚不替代专家。原文[26candidates.json](../_sources/daily-20250926/26candidates.json) L49–54、165–181、191–193保留可审位置。

为支持具体Books差额，额外核验评价对象、判分资格、分项反侧、完整限制与artifact示例，按研究合同§4–6加深到采用命题所需内容；仍维持6分，不以写书提高评分。

作者结果支持该任务/模型集合的专家偏好，不能证明人类岗位替代、生产正确性或所有任务代表性。aesthetics与accuracy切片可能不同；Blog的“double”与图注“tripled”同时保留，不采用增长倍率。100x速度/便宜仅inference/API billing，不包含监督、迭代与系统整合。one-shot未覆盖澄清、客户反馈或任务选择中的歧义。

root实际比较`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)原论点后确认差额，已在EvalSpec定义后、分析Agent段前写入artifact可见渲染、职业rubric与内容/呈现分账的一自然段，标记`SF-2025-OPENAI-GDPVAL`。Archimedes作为非写入者重新核官方Blog必要核心、实际完整新段/前后邻接与main末注，POST通过：保存渲染/冻结身份为工程推导，原文并未认证实现或费用；没有十月论文、模型排名、100x生产成本或double/triple冲突数字。与[Ch65](../../../../books/part-06-ai-infrastructure/65-kai-scheduler.md)资源政策、[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md)observed health交接不冲突，详见[handoff POST](../_sources/daily-20250926/CALIBRATION_HANDOFF.md)。Books由root写，最终末注已实际更新为POST通过，root最终正文/末注及本日DAY复核通过。

### 必要反侧与未确认日期的潜力

[EVIDENCE_BOUNDARIES](../_sources/daily-20250926/EVIDENCE_BOUNDARIES.md)逐项记录16份精确v1实际读取位置、条件与非证明：FL抽取权限/先验、CORE路径定义/合成DFA、MCP描述攻击oracle、量化复杂shift/伪相关退化、改写隐式泄漏、SNCE残余ASR、MMR1假设与A.4等。root已校准的五项潜力与两项关闭见[独立校准原记录](../_sources/daily-20250926/INDEPENDENT_CALIBRATION.md)。这些阅读保留局部与负面价值，但日期未取得前不提供本窗正面采用链。

root已独立定点核这16个v1的必要方法/评价/限制；其中21173的HTML “Abstract”实际为附录引言，root另读原abs/v1完整真摘要，不使用v6。六项题摘误排恢复也经root逐项再读实际v1通过，仅保留潜力，不授日期/评分/Evidence/Books；详见[实际DAY记录](../_sources/daily-20250926/INDEPENDENT_DAY_REVIEW.md)。未称16篇全文、代码或复现均完成。

## 5. 缺口与下一步

可执行研究、必要修正、实际Books写入/POST与独立DAY均已完成。以下外部保留项仍隔离，不用于正面采用；主线程在完成态机器检查及最终字段核对后维护月度计数，作者不写共享索引或LEARNING_STATE。

本窗终态保留项：以下外部缺口不用于正面证据、Books或无遗漏断言，也不授正面Coverage/Evidence通过；仅在下列必要材料恢复时按对应身份和来源停点定点重开。

- arXiv上述257提交发现中的相关/含糊潜力，精确身份在题摘数组与SCREENING、16份必要v1在EVIDENCE_BOUNDARIES。缺逐篇原首次公开或本窗重要修订的公开区间；日公告恢复失败、schedule有moderation延迟，故当前不评分/采用。官方first-announcement、原作者首次公开正文及完全落窗的有证据区间可接受；只重开对应家族，不要求补造秒级。EnergyFlow完整题摘已恢复，余下同样仅日期依赖。
- [Wayfinding](https://research.google/blog/towards-better-health-conversations-research-insights-on-a-wayfinding-ai-agent-based-on-gemini/)核心有双栏澄清/最佳当前回答的协作潜力，但Sep25无TZ；需原发布字段或完全落窗区间。[LMSYS PartII](https://lmsys.org/blog/2025-09-25-gb200-part-2/)Sep25无TZ，同样不借硬件倍率评分。各仅请求一次日期材料。
- Hunyuan9条当前API、Zai两页Dec后目录、Seed论文type1不完整、MiniMax Agent仅2026目录、Meta历史Research、Google论文年份目录/DeepMind当前RSS的缺口见§2具体停点。Qwen实际API60项已恢复，不再保留未执行动态API为终态hold。其余原入口不能提供目标历史覆盖；恢复目标原目录/有效分页或具体原事件时仅窄补受影响源，不授Coverage通过。

窗外版本：[Robotics1.5](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/)原schema`2025-09-25T00:00:00+00:00`换算25日08BJT，早于本窗起点一小时，归25日，不阻塞26；没有具体calendar-placeholder证据，不假设午夜字段失真。GDPval现论文链接的`2510.04374v1`提交字段Oct5，不属于本窗精确论文版本；若需其论文事件，应由真实归属日恢复，不扩本日/本月任务。Pulse原00GMT也不移入本窗。未处理其他月份、Weekly或当前日。

## 6. 复核

复核者：root（主线程，非本日作者）。

结论：通过

root实际日级记录见[INDEPENDENT_DAY_REVIEW](../_sources/daily-20250926/INDEPENDENT_DAY_REVIEW.md)，截至2026-10-06T13:40:02+08:00。实际范围包括十四源有限入口/分页停点、全部正式候选GDPval的RSS/核心/反侧、16个精确v1必要风险与设计反侧、Books实际段落与末注，复用[首批准入校准](../_sources/daily-20250926/INDEPENDENT_CALIBRATION.md)。其余关闭分层抽检累计10身份：20615、20940、20513、20968、21079、20819、21039、20857、21147、22723；五项误排及同理由扩查20857经精确v1恢复、root再读纠正。未检查范围包括其余165题摘非必要部分及无关附件，不能把分层样本称全量验证。Archimedes非写入者GDPval POST已通过，root核最终正文/末注，不以自身写入替代独立POST。

此前完成态V3校验因§5终态隔离措辞与§6结论行格式两项未通过，不计作通过。本次仅修正这两处措辞后实际重跑完成态V3通过；6份本日Markdown的63个本地引用及围栏检查无错误，限定路径diff-check通过。机器一致性不能代替上述语义复核，untracked文件也作本地引用检查；未stage/commit/push。外部隔离项不授正面Coverage/Evidence或无遗漏/生产保证。
