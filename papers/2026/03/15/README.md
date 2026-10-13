# Daily Research — 2026-03-15

**规范：** V3
**窗口：** 2026-03-14T09:00:00+08:00 ～ 2026-03-15T09:00:00+08:00
**窗口说明：** 用户授权保留原窗口和原候选，仅补来源遗漏。
**补充窗口：** 2026-03-14 ～ 2026-03-14
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-11T09:53:00+08:00

## 1. 结论

本轮仅补北京时间2026-03-14完整自然日，原窗口、原候选0与§4三条关闭原文保留；[原README冻结](../_sources/daily-20260315/SUP_ORIGINAL_README_20261011.md)可核。14个每日来源按本日有效历史邻接字段复用及有限原始入口恢复处理，不启动Weekly、其他日期或机构历年研究。

本轮arXiv四主题查询恢复121/76/27/108行；这些是Submitted缓冲内未去重元数据，不是本窗332篇、摘要审阅规模或候选。定点完整v1题摘实际读5项：12529、13423、13426有具体机制潜力但缺本窗公开日期，隔离且不评分；12567、12694为当前暂缓科学应用，范围关闭。原三条关闭的有效判断复用，不将旧完成标签当补查验收。新增确定候选0，原候选0，确定候选证据审阅0/0；没有正面采用的新Evidence或Books产出，未改Books。

六个来源的必要历史切片及三具名公开日期门见§5，不支持正面证据、Books或“当天无相关论文／无遗漏”。非作者review_mar15_16实际完成首批准入及14来源／六部分DAY；root指出Anthropic同页HTML公开字段可恢复后，本轮定点恢复174个唯一publishedOn+slug，March9行BJT日期无03-14，其窄增量已实际独核通过。普通可执行待办0，补查达到安全终态，不把浏览器仅10卡继续称作历史无法取得，不授全机构无遗漏。

## 2. 来源覆盖

原执行2026-10-02的本日历史字段覆盖补充自然日者明确复用；2026-10-11有限恢复不冒称全部重新抓取。目录只读相关标题/日期，新增完整题摘5项；宽列表没有变成逐项题摘或附件队列。本轮实际查询、恢复结果与复用边界见[补充来源停点](../_sources/daily-20260315/SUP_SOURCE_STOP_20261011.md)，旧入口、页停点和原值见[有限来源停点](../_sources/daily-20260315/V3_SOURCE_STOP.md)、[public字段](../_sources/daily-20260315/V3_PUBLIC_DIRECTORY_FIELDS.json)、[Seed论文字段](../_sources/daily-20260315/V3_SEED_FINITE_FIELDS.json)、[本日Seed Blog字段](../_sources/daily-20260315/V3_SEED_BLOG_FINITE_FIELDS.json)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)当前精选；[官方RSS](https://openai.com/news/rss.xml)实际解析1241项，只取3/13–3/16 pubDate切片1项SAST Blog，原值Mon,16Mar2026 00:00:00GMT→3/16 08BJT，窗外；未扩正文 | 已检查 | RSS与精选不证明全部历史Research无遗漏 |
| SRC-ANTHROPIC | 本轮[Research](https://www.anthropic.com/research)浏览器10卡/See more同页之后，root指出同URL嵌入字段可恢复；一次curl只投影公开publishedOn+slug，174唯一字段对，March9行BJT为03-06/03-13/03-24/04-01，无03-14；[本日安全字段](../_sources/daily-20260315/SUP_ANTHROPIC_PUBLIC_FIELDS_20261011.json)。[Alignment](https://alignment.anthropic.com/)March5条具名header与Abstractive旧v1重呈现关闭仍复用 | 已检查 | 当前嵌入列表本日切片已恢复，不继续说主Research历史无法取得；不外推删除项或全机构历史无遗漏，month-only旧重呈现不造本日候选 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/)8项精选；[实际Blog page3](https://deepmind.google/blog/page/3/)24卡May→Feb，header3/17 cognitive-framework与3/10 AlphaGo跨窗；[Google March archive](https://research.google/blog/2026/03/)page1的12卡，3/16→3/12跨窗，page2更早未扩；本轮[Pubs](https://research.google/pubs/)实际1–15 of11612，排序/筛选只年与标题，未提供公开day | 受阻 | Pubs及精选Research日级论文历史未取得；没有全扫年度论文，旧目录数量不当当前总数 |
| SRC-META-AI | 本轮[Research](https://ai.meta.com/research/)0行；本轮[publication](https://ai.meta.com/results/?content_types%5B0%5D=publication)Internal Error；[Blog](https://ai.meta.com/blog/)10卡与[page2](https://ai.meta.com/blog/?page=2)12卡，非严格日期排序，3/11与3/27及更早条目无可见本窗卡 | 受阻 | 本窗模型/架构/训练论文历史入口未取得；本日没有IAB核查，不沿用他日browser失败 |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/)明示迁移，qwen.ai/blog静态0行；实际public retrieval type=qwen_ai/language=en-US，safe title/path/date投影40项，2/16 Qwen3.5→3/19 Max Preview跨窗；初次输出截断3片段不作目录数 | 已检查 | 未公布分页total；仅40可见范围，date不等于论文first-public |
| SRC-DEEPSEEK | [官方/en/news](https://www.deepseek.com/en/news/)实际Research10、News5，2/25→6/24及12/1→4/24跨窗；停可见目录，不扩View all | 已检查 | 不宣称删除项或完整机构历史 |
| SRC-MOONSHOT | [现官方Kimi Blog](https://www.kimi.com/en/blog/)实际19可见条目，2/9 Agent Swarm→4/20 K2.6跨窗；不以旧platform止2025反证2026缺研究 | 已检查 | 仅可见19条，不推及删除历史 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)静态timeout后，本日实际publicList POST pageNum1/pageSize20/renderType0，total11、11/11返回，display2/13→4/23跨窗，pub字段无本窗；[官方endpoint恢复依据](../_sources/V3_HUNYUAN_LIST_RECOVERY.md)只作入口定位 | 已检查 | 动态静态失败不再解释为整个目录不可访问；不推及删除项 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)实际15卡，2025/12/9→2026/8/26，停查看更；定点[Turbo155](https://www.zhipuai.cn/zh/research/155)header2026/03/15 16:00及core16–90，公开增量关闭 | 已检查 | header未明确时区，已贡献前关闭，不为不影响处置的日期穷查；不全审15卡 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)与[论文目录](https://seed.bytedance.com/en/public_papers)当前页非March历史；实际get_article_list_v2 article_type1/year2026/page_token20/count100/order_descfalse，US locale，18项/total82、next40/has_moretrue，2/25→3/26；3/15 νTNS题摘关闭。另本日原type2有效字段及本轮同入口US locale恢复均返回14项/total19、next空/has_morefalse；显示2/16 Arena Preview→4/1 Recruitment跨窗，无可见本窗Blog项，只读title/date | 受阻 | PublishDate不证明first-public；type2的14返回与total19不一致，缺其余5项/本窗Blog历史切片，§5精确隔离，不声称19/19或全Blog无命中 |
| SRC-BAIDU-ERNIE | [Blog/zh](https://ernie.baidu.com/blog/zh/)page1实际10卡，2025/11/21→2026/5/9，2/6→4/15跨窗；下一页更早未扩 | 已检查 | 仅当前页范围，不推及其他历史/修订 |
| SRC-XIAOMI-MIMO | 本轮[首页Paper](https://mimo.xiaomi.com/)实际8项，3/13 ARL-Tangram→6/29 MOPD跨窗；Blog15标题无日期，More无可用历史分页；[/blog/](https://mimo.xiaomi.com/blog/)本轮仍2025/12/16单篇而非archive；有限HTML日期字段未恢复Blog历史，不扩静态bundle | 受阻 | 本窗Blog历史日期/正文切片未取得，不能由无日期标题授no-hit |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)12卡、[中文](https://www.minimaxi.com/blog)redirect后13卡，3/18→Feb跨窗；Forge英文2/14、中文2/12原值不同均窗外。本轮[Agent Tech](https://agent.minimax.io/docs/techblog)恢复3张09-19/09-22/10-08窗外卡，llms.txt54行含同3篇及当前用户docs | 受阻 | 当前3卡没有本窗历史切片／归档完整性，不用旧heading-only当现事实；当前用户文档不是历史发布证明 |
| SRC-ARXIV | [API](https://export.arxiv.org/api/query)本轮四主题延续本日systems CL/LG/DC/AR/PL/OS/PF×LM训练推理kernel；learning CL/LG×Transformer/MoE/LM×优化scale表示Attention；CV/RO/CL×WorldModel/VLA/video/multimodal；AI/MA/IR/CL×LM/LLM×agent/retrieval/eval。Submitted UTC3/13 00→3/15 00缓冲，各start0/max200/ascending，实际121/76/27/108=total无截断。[精确参数与4响应](../_sources/daily-20260315/SUP_SOURCE_STOP_20261011.md)；官方月列表仅开头片段、skip800/show200 cachemiss；advanced announcement只年/月 | 受阻 | 主题发现接口已恢复，不再把旧API失败当现事实；仍缺本窗公开日期slice／具名原event，不以Submitted、DOI+slot派生或周六无常规slot授日期与无遗漏；3具名潜力隔离 |

未触发每周源、会议全站、实现repo/release或科学应用队列。Hunyuan/Qwen/Seed恢复public endpoint是原始公开入口恢复，不是以搜索摘要代替证据。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

原确定候选0保留；本轮新增确定候选0。四主题121/76/27/108行未跨组去重，仅发现线索；本轮5项完整v1题摘中3项仅具名日期保留，2范围EX，不计候选、Evidence完成或评分，不把访问状态和Books已有覆盖用于缩池。

## 4. 证据与知识整合

没有可正面采用的候选Evidence或Research→Books产出。以下为具体准入前关闭及身份依据，不是候选深审完成：

- [GLM-5-Turbo](https://www.zhipuai.cn/zh/research/155)：header原值2026/03/15 16:00，无显式时区；实际核心16–90只公开OpenClaw训练能力目标、工具/指令/长任务/吞吐目标，未披露可改变训练选择的objective/data控制。ZClawBench场景分布/排行没有建立可审独立protocol或评价盲点；Claw Enterprise的RBAC/audit/encryption/human approval仅产品特征与承诺，没有披露可采用的新约束、控制机制或反证。不采用安全保证，不因“没有新权限schema”一条机械拒绝，也不泛化所有新模型无贡献。
- [Abstractive red-teaming](https://alignment.anthropic.com/2026/abstractive-red-teaming/)：month-only Blog core12–43与[唯一v1](https://arxiv.org/abs/2602.12318v1)完整题摘/Feb12历史相同工作，category search、CRL/QCI、7模型×12原则评价已在旧稿。未见独立revision/新机制说明，关闭本次重呈现；不是旧论文无价值或旧Evidence全审宣称，不追不影响此处置的月级日期。
- [νTNS 2603.14425v1](https://arxiv.org/abs/2603.14425v1)：完整题摘为neural disentangler/CNN+tensor-network求量子manybody/J1-J2 Heisenberg能量。当前暂缓AIforScience，没有foundation模型系统增量，不借表示owner回收。Seed id1414原PublishDate1773504000000→3/15 00BJT与v1 Submitted3/15T15:09:00Z不一致，显示日期不证明first-public；范围明确关闭，不开日期请求/附件队列。

当前官方页轻量检查未见上述Blog新的撤回/纠错说明，νTNS唯一v1未见撤回header；没有为了证明“无标记”遍历完整历史。三项由root实际读对应core/题摘/历史，首批独立校准通过。完整有限记录见[停点](../_sources/daily-20260315/V3_SOURCE_STOP.md)。

### 本轮补查增量判断

[首批准入包](../_sources/daily-20260315/SUP_ADMISSION_20261011.md)及[完整v1题摘](../_sources/daily-20260315/SUP_AB_SAMPLE_20261011.txt)保留具体证据位置。[TERMINATOR 12529v1](https://arxiv.org/abs/2603.12529v1)提出用首个答案位置构造终止器训练数据，潜在改变推理质量／计算取舍；[KWM 13423v1](https://arxiv.org/abs/2603.13423v1)提出Kalman式递推替代反向AD的训练思路；[OATS 13426v1](https://arxiv.org/abs/2603.13426v1)离线以成功查询centroid修正工具embedding，并报告稀疏outcome条件下小MLP未获益。三项潜在增量在准入层成立，但精确原页只给Submitted，未证03-14首公开；不把作者摘要效益当已审结论，不读无关附件，不评分、不准入、不进入Books。缺日期门不等于无贡献，恢复条件见§5。

[Accelerating materials discovery…12567v1](https://arxiv.org/abs/2603.12567v1)完整摘要L16–20是既有预训练TabPFN用于材料active learning及领域评估，本项目当前AIforScience暂缓；latest API标题变化不替换精确v1。[RXNRECer 12694v1](https://arxiv.org/abs/2603.12694v1)完整摘要L15–18是以蛋白LM/active learning直接预测酶反应的科学应用；[单页原证](../_sources/daily-20260315/SUP_AB_RXNRECER_20261011.txt)。两项不以foundation/LM关键词回收为通用训练新机制，贡献前范围关闭；不追不影响处置的公开日期，不扩大全文队列。

非作者review_mar15_16实际独读上述5份完整v1题摘/header/history，3日期隔离与2范围EX首批校准通过；这些不是标准／深入Evidence通过。当前轻量原页未见撤回／纠错header，12529后来v2及12567后来v3均不据版本号触发本窗全文复读。无确定候选改变长期认知，Books新增0，不申请共享owner写锁。

## 5. 缺口与下一步

普通可执行待办0，非作者review_mar15_16整体DAY及Anthropic同页日期字段恢复窄增量均实际通过。以下必要外部材料按补充自然日明确隔离为外部终态保留项，不支持正面证据、Books或无遗漏断言；以后只按具体条件重开受影响来源／材料，不重扫整月。旧root完成仅对应原检查，不替代本轮实际验收。

| 身份/入口 | 必要缺口、当前限制与定点重开条件 |
| --- | --- |
| [Google Pubs](https://research.google/pubs/)、[DeepMind Research](https://deepmind.google/research/) | 当前仅year/精选不能证明日级公开：请求03-14自然日主线论文官方原始event/date或历史清单。Blog可见跨窗邻接仅支持自身切片；只重开受影响材料，不全扫年度论文。 |
| [Meta publication](https://ai.meta.com/results/?content_types%5B0%5D=publication) | 本轮Internal Error/Research0行，缺本窗模型/架构/训练论文清单与原始日期。官方带date历史目录或确切作者版本可替代；到达只恢复该窗论文部分，Blog原可见卡不作无命中证明。 |
| [MiMo Blog](https://mimo.xiaomi.com/) | 15标题无date、More无可用历史页，/blog为旧单篇。请求本窗Blog官方历史分页或原始文章日期/正文；只重开该窗具体发布，不把全部15标题变审阅队列。 |
| [MiniMax Agent Tech](https://agent.minimax.io/docs/techblog) | 当前可读3张9–10月card、llms当前用户docs非历史；未恢复03-14历史。请求本窗原始技术Blog及date/官方可核归档，按具体事件恢复；英文/中文目录跨窗不授Agent历史无遗漏。 |
| [Seed Research / Blog](https://seed.bytedance.com/en/research) | 本日type2有限元数据实际返回14、total19且无next；返回日期跨窗，但剩余5项不知，当前5Blog精选也不是历史切片。请求足以解释这5项的官方Blog目录/历史日期，或本窗带可核date的原始Blog；只恢复该来源该窗，不将所有Blog或论文变全文队列。 |
| [arXiv主题API](https://export.arxiv.org/api/query) | 本轮四主题元数据已恢复，仍缺03-14公开日期slice/确切dated原event。有效月列表本轮只见开头片段，skip800/show200无响应，advanced只年/月；需要实际公告事件或可核作者原发日期，不拿Submitted缓冲/DOI+slot派生/周六背景替代。具名潜力12529v1、13423v1、13426v1仅缺first-public公开日或本窗作者原event（不要求时刻），本日没有足够日期证据；到达只定点重开对应项，不继续全March扫描或公告代码考古。 |

日期背景只作限定：[官方availability](https://info.arxiv.org/help/availability.html)实际170–189说明Sunday–Thursday Eastern20:00公告、Friday/Saturday无常规公告，DST后邻接slot为BJT3/13 08与3/16 08，窗外；moderation可延迟。此事实不是所有作者原发/更新事件为0。原两次/list/cs/YYYY-MM-DD cachemiss未证是有效官方按日入口，仅请求无可用资料；本轮不再请求。原DataCite client-id arxiv.content、registered UTC3/14 01→3/15 01实返回total0，只辅助旧窗口索引，不当补充自然日exact公告或无遗漏证明。

[本轮日期入口权限和停止依据](../_sources/daily-20260315/SUP_DATE_LIMIT_20261011.md)明确官方advanced仅年/月、原页Submitted以及旧DOI映射只能作线索。另12567v1和12694v1已明确科学应用范围EX，不另建日期请求。窗外/日期粗糙但已具体关闭的Turbo、Abstractive、νTNS不用另建材料请求。RSS SAST 3/16、A3 3/11、AuditBench3/10、AlphaGo3/10、MiMo3/13等仅目录邻接，不宣称其研究已完成，也不扩张本窗或处理归属日。

## 6. 复核

复核者：review_mar15_16（非报告作者）
结论：通过

首批已实际独读12529v1、13423v1、13426v1、12567v1、12694v1五份完整题摘、header与history，3具名日期隔离+2AIforScience范围EX通过；核四API真实query及121/76/27/108全返回，各start0且未超200，标题线索不变332逐项队列边界通过。最终实际独读六部分、14源有限停止、本日有效字段及新增MiMo／MiniMax Agent／Seed原件，原窗口／0候选／连续§4冻结通过。首包“1 AB+1标题EX”已修为2完整AB EX，12567v1与latest改名区分，Google旧数量已删除，Meta旧timeout与本轮Internal Error已区分。其余宽标题没有逐项AB／附件验收，不将抽检当全学科验证。[本轮独立复核记录](../_sources/daily-20260315/SUP_INDEPENDENT_REVIEW_20261011.md)末章承载最终DAY实际范围。

最终新增Anthropic同页HTML恢复174唯一公开日期+slug、March9实际安全字段均由review_mar15_16独读及按BJT公开日期校核，无03-14；§1/2/5/6窄变更实际独核通过，必要来源限制7→6，不将174字段变逐项队列或全机构保证。原root三关闭独校/旧来源有限stop判断仅在未变化处复用，不继承旧root完成标签，未让旧API失败和MiniMax heading-only冒充当前事实。无Books实际写入待POST。完成态V3校验通过、限定本日报告／日_sources cached与unstaged diff-check无输出；15本地引用有效，6新JSON可解析，原窗口与完整§4连续前缀保持，实际diff已检查。这些只验证接口与变更范围，不替代语义Gate；未stage、commit或push。
