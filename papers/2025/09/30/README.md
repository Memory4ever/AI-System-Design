# Daily Research — 2025-09-30

**规范：** V3
**窗口：** 2025-09-29T09:00:00+08:00 ～ 2025-09-30T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T20:35:00+08:00

## 1. 结论

六个唯一官方家族的落窗身份、具体准入命题与2+2+2=6评分已由root独立校准，必要受影响证据已核；深入的是安全/发布/评价约束或知识缺口，不借产品排名、价格与硬件倍率加分。Books已实际整合两家族：Ch14的DSA选择器训练与核心稀疏读取分账、Ch72的Sora人物consent许可与来源证明分账，非写入者POST通过；其余四家族具体已有覆盖。Sora精确撤销/creator scope/草稿处置未当作Sept card事实，许可生命周期与副本分责只是工程推导。非作者日级复核通过，无普通可执行待办；未复现或授生产安全/性能保证，日期及历史目录缺口按§5隔离。

arXiv三页278个提交发现加月尾13个定点题摘恢复，身份去重291：44明确关闭、247潜力/日期隔离；不是本日公开量或247已审候选。实际必要13精确v1题摘及相应风险/理论反侧已读，日期尚不支持入选，不评分或Books采用。14日源都执行有限入口恢复，历史缺口保留而非零事件/无遗漏；原件与精确处置见[SCREENING](../_sources/daily-20250930/SCREENING.md)、[Books差额](../_sources/daily-20250930/BOOKS_HANDOFF.md)。

## 2. 来源覆盖

原请求/执行时间在[fetch-log](../_sources/daily-20250930/fetch-log.json)、[有限恢复](../_sources/daily-20250930/30-finite-recovery.json)，不以可恢复但未执行API结束。以下仅授实际范围，不授机构历史全覆盖。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS1247条原记录按窗口解析11条：Sora三条归一、两安全发布、六内部series；全部11对应必要core实际读。原RSS/pubDate与core保留。 | 已检查 | 当前正文含2026更新，剥离后不回填Sep；厂商效果不作独立评价。 |
| SRC-ANTHROPIC | Research Next Flight恢复174 publication并保留publishedOn；九月邻近3条无本窗数组条目。定点Sonnet/Code schema17Z、card必要受影响部分及Context core已读。 | 已检查 | Context仅9/29日/TZ未知，相交隔离；当前card后修订非冻结Sep版本。 |
| SRC-GOOGLE-AI | Research `/blog/2025/09/`12条Sep30至Sep11跨窗停止；PHA/Alpha完整必要core。真实year+language-model pubs三页15+15+7/37标题；DeepMind Research及RSS100条尾Nov5。 | 受阻 | Google两BlogSep30只有日字段无TZ；pubs全年标题不作当日正文/先发；DeepMind RSS未达Sept历史，有限恢复不授目标历史覆盖。 |
| SRC-META-AI | Research壳；Blog真实page1–3为10/12/12卡，非单调featured2019/2024，普通尾Aug27至Jul31跨窗停止。 | 受阻 | Blog有限切片已处理，Research历史正文目录未恢复，不以壳/首页授无事件。 |
| SRC-QWEN | 本日实际`qwen.ai/api/page_config?code=research.research-list`60条非单调目录，原日期逐项筛本窗，无明确本窗项；Blog壳辅助。 | 已检查 | 有限目录非全部历史公开，不把未命中授无遗漏。 |
| SRC-DEEPSEEK | 官网18news/sidebar；V3.2-Exp原官贴官方嵌入200，created_at29Sep10:10Z；固定Sept报告与先前已读main逐字节一致。 | 已检查 | 未核代码/real-world SLO；Git commit只固定artifact身份，不授公开时间。 |
| SRC-MOONSHOT | 官方Blog26元数据，最早2024、无More，邻近Sep16/5；有限主题检查停止。 | 已检查 | 不保证表外/完整GitHub历史。 |
| SRC-TENCENT-HUNYUAN | 正确publicList POST pageNum1/pageSize100/renderType0，code0、total9/list9，全2026原记录；Research壳留存。 | 受阻 | 当前API不能授2025历史覆盖；浏览器未核目标历史，当前9条不记零事件。 |
| SRC-ZAI | 官方Research实际两页15/18、hasMore true/false，Dec2025至Aug2026；release-notes定位GLM4.6后执行原598B壳与官方11296B模块，完整英/中core按贡献关闭。 | 受阻 | Research目录未到Sept；已恢复4.6 core不补授Research历史，非伪成4.5报告。 |
| SRC-BYTEDANCE-SEED | year2025/type2/page0/count20原15/49/true；pinnedSep8、普通Oct22→Aug20/Aug13/Jul跨窗停止。type1 US/CN各total94无array，page20仅SwiftSpec。 | 受阻 | type1不完整不是0；Blog有限跨窗已处理，非全49/论文全量。 |
| SRC-BAIDU-ERNIE | 官方RSS18记录实际16post+2navigation，Oct16/Sep12夹窗停。 | 已检查 | 导航不作论文，有限RSS不授全站无遗漏。 |
| SRC-XIAOMI-MIMO | 实际route/home两个chunks，8有日期paper、15无日期Blog；完整home/More相关逻辑实际读，More只slice同静态数组，无HTTP下一页。 | 受阻 | 有日期paper有限切片已处理，Blog历史日字段缺失，当前2026发布不能回填2025。 |
| SRC-MINIMAX | EN12/CN13有限cards无More；Agent原TechBlog与llms索引实际恢复，唯一May13 2026帖子，两原件同身份。 | 受阻 | 公司Blog有限切片已处理，Agent2025历史未恢复，不记0，停止后待官方archive。 |
| SRC-ARXIV | 十二分类十标题主题复合submitted前缘三页100+100+78；月列表相关标题查漏，尾214标题浏览仅挑13个id定点完整题摘，13/13后停；13必要v1 HTML200。 | 受阻 | 此主题发现已处理，submitted非公开；官方日路径400，moderation导致公告不能按提交机械推定；247潜力隔离，不授首次公开覆盖。 |

## 3. 候选与判断

以下六家族已通过root独立准入及必要证据复核，Books最终处置与实际写入如下；非写入者POST不代替最终DAY。其他日期潜力只在§5及原记录，不伪落窗列入评分。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Sora 2](https://openai.com/index/sora-2/) | 2025-09-30T08:00:00+08:00 | 生成可描绘真实身份→明确opt-in consent/likeness controls与provenance分账→发布必须分别验许可与来源；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)provenance后1104及末注3180；root实际写入、非writer POST通过。 |
| [DeepSeek-V3.2-Exp](https://x.com/deepseek_ai/status/1972604768309871061) | 2025-09-29T18:10:00+08:00 | dense再删不能省选择→训练cheap indexer选支集而核心稀疏读取→selector预算/复杂度与core分账；2+2+2=6 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md)路由反侧后128/130两段及末注580；root实际写入、非writer POST通过。 |
| [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5) | 2025-09-30T01:00:00+08:00 | 排除verbalized-awareness仍漏潜在测试识别→SAE/干预局部证据→行为低风险要条件化realism，不推部署保证；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，representation/verbalization/control分账；root已核。 |
| [Claude Code checkpoints](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously) | 2025-09-30T01:00:00+08:00 | code/conversation恢复只涵盖Claude edits→user/bash外部状态不回退→恢复scope不能等全environment；2+2+2=6 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)，joint state及受控snapshot/外部compensation；root已核。 |
| [Parental controls](https://openai.com/index/introducing-parental-controls/) | 2025-09-29T11:00:00+08:00 | 模型风险flag→trained human审急性风险→有限家长通知不等聊天访问权；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)model verdict非authority及recipient/purpose/披露范围；root已核。 |
| [Combating CSEA](https://openai.com/index/combating-online-child-sexual-exploitation-abuse/) | 2025-09-29T11:00:00+08:00 | known hash/novel classifier与人工审分责，上传描述/roleplay模式→只审核生成请求不足；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)输入、上下文、输出policy gate及sensor/enforcement分责；root已核。 |

## 4. 证据与知识整合

### [Sora 2](https://openai.com/index/sora-2/)

实际原Sept30七页card§1–6及Table1，不把当前2026停服声明当Sep事实。§3.4支持明确opt-in consent/likeness controls的cameo与初始no video-to-video/public figure text-to-video；§3.3来源机制不代签被描绘者同意。当前Blog/Launching responsibly明写creator scope/revocation/草稿处置，但用characters且含后来更新，未冻结Sept，故本日不把这些精确功能/identity验证流程称Sept card已证。帧、audio transcript、scene caption与人工是sensor，不是许可真值。not_unsafe/not_overrefuse分别评价selected adversarial prompts，N/CI Not Disclosed，不授生产recall。长期对象差额identity permission≠content provenance已实际整合：root在Ch72 provenance后1104新增自然段，许可控制面/核验/误拒成本与不确定时限制人物路径近文，未来生成、产品存量、外部副本分责明确为工程推导而非Sept撤销实现；末注3180绑定初始card边界。非写入者实际顺读1088～1106及末注并回原§3.3～3.4，POST通过，见[精确handoff](../_sources/daily-20250930/BOOKS_HANDOFF.md)。

### [DeepSeek-V3.2-Exp](https://x.com/deepseek_ai/status/1972604768309871061)

原官贴created_at支持落窗；report commit只提供固定版本，已实际200取得并与已读main同字节。6页§1–3、Eq1–4/Fig1–3/AppA：低维FP8 indexer仍O(L²)，core O(Lk)；k2048、dense indexer warmup2.1B后sparse continued943.7B/独立KL gradient，MQA共享latent为kernel约束。不同训练预算/推理长度与局部benchmark退步限制归因；H800/$2GPU-hour估计、短序列masked-MHA与real-world validation未来不作生产收益。root已在Ch14“先dense再选非加速”后、SLA2前128/130实际整合两段：dense冻结teacher目标预热→稀疏继续训练/选集KL，indexer detach/KL与主模型LM loss分责；core与selector复杂度及质量/预算反侧、dense共存条件近文，末注580绑定固定版本。非写入者实际顺读118～134及末注并回原机制/直接反侧，POST通过。Ch49已有indexer/TopK/gather融合不重复拥有。

### [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5)

当前149页card必要§7.2/7.6–7.7实际读，cover/changelog保留Oct/Dec两后修订；不冒称149页全读或冻结Sept。单轮synthetic100、multi-turn50、matched random SAE及probe反侧支持表征/发言/干预不可混同，strength ad hoc、mixed features、earlier auditor/response-included posthoc限制因果；未发现sophisticated strategic deception，不授真实部署绝无风险。SWE预算异质不合并。Ch66实际194–270与4018–4055已写最低长期命题，已有覆盖不制造厂商摘要diff。

### [Claude Code checkpoints](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)

原core Checkpoints：代码/对话分开或共同恢复，Claude edits之外user/bash不覆盖，VCS仍必要。Ch81实际580–624已有controlled snapshot、external effect compensation、Git非transaction rollback；厂商版本事实报告保留，不声称新全局恢复机制。

### [Parental controls](https://openai.com/index/introducing-parental-controls/)

Getting started/Stronger safeguards/Notifications/Looking ahead实际core，RSS原03GMT；unlink通知、可bypass/false alarm、未来age prediction保留，不倒填2026 violent alert/Study Mode。模型flag≠危险定论，human review≠全chat grant。root独核6分发布对象命题后接受Ch72已有覆盖：Policy-as-Data的model verdict非authority、recipient/purpose/transmission绑定与最小披露权限共同承载告警/收件人分责，不为加入产品例子再写摘要，未授临床/安全保证。

### [Combating CSEA](https://openai.com/index/combating-online-child-sexual-exploitation-abuse/)

Train/Detect/Patterns实际core，known hash与novel classifier分责/人工审及输入分析滥用模式；P/R Not Disclosed，不授无绕过。只采用原厂商公开机制/约束，不把法律/合规叙述作为经验证结论。root独核后接受Ch72已有覆盖：policy gate把输入、上下文、输出分别验收，模型/检测signal只作sensor，由独立规则与人工处理执行；因此上传内容分析而非仅生成请求的审查对象已有具体承载，不新增孤立产品摘要。原安全core已读，不虚列工具阻断。

## 5. 缺口与下一步

**可执行工作：** 无。六候选的准入、必要证据、Books裁决及两处实际写入的非writer POST均通过；非作者完成13必要反侧、分层关闭样本与14有限来源的日级验收。以下仅为隔离的外部保留项，不把有材料不可得写成正面Gate通过。

**外部终态保留项（本次隔离，尚不授正面Coverage/Evidence）：** 247个arXiv潜力的精确v1首次公开/重要修订事件尚未恢复；当前submitted/updated/月编号不能决定日报归属。日列表请求400及常规公告规则不解决moderation个体日期。获得对应官方公告、版本首公开字段或可信先发全文落窗范围时仅重开该身份、必要风险和候选判断，不重扫291/整月。原13必要反侧已读但不作当窗正面证据、评分或Books。

Google PHA/AlphaEvolve与Anthropic Context各日字段/TZ未定；已实际读core、原页/metadata/窄搜索仍无可含窗时间。可接受原RSS pubDate、官方带TZ字段或完全落窗的first-public区间；只重开三条日期及随后需要的证据，不把Google科学应用收益采用。没有未执行已知API被伪终态hold。

Hunyuan当前9条2026、Zai两页Dec2025之后、Seed type1缺array、DeepMind RSS尾Nov2025、Meta Research壳、MiMo无日期Blog、MiniMax Agent唯一2026入口均为有限历史缺口。可接受原官方2025archive/API历史字段/目标窗口原始发布；按§2对应入口定点恢复，不要求遍历历年。以上保留项不用于正面证据、不进入Books、不支撑无遗漏或性能/安全保证；实际有限检查不是这些缺口Coverage/Evidence通过。后来材料到达仅重开受影响处。

## 6. 复核

复核者：root（非报告作者，FIRST与DAY）；Archimedes（非Books写入者，POST）。

结论：通过

root已实际独核六家族必要原主体、精确版本/落窗证据、6分具体增量与采用边界，接受两整合/四已有覆盖。非写入者POST实际顺读Ch14 118～134及末注580、Ch72 1088～1106及末注3180，并回固定六页DSA§1～3/Eq1～4/AppA与Sept Sora card§3.3～3.4：训练/梯度分责与indexer二次开销近文，consent与provenance独立，许可生命周期/副本明确工程推导，前后衔接通过。

DAY另实际读SCREENING列出的13精确v1必要威胁、理论假设、主要限制与直接反证位置：验证器诚实/在线与数值条件、concolic under-approximation、94.2%非全约束成立、已发prefix不可撤销、同任务污染残余、KB authority与exchangeability等均被限制，不授全部定理证明或全文复核。44关闭项按科学应用、领域组合、综述、评价和模型发布分层，实际完整题摘抽检24895、25043、24866、24322、24024、2510.00055、2510.03270、22926八项；官方内部应用抽核support、inbound-sales、contract-data、GTM与research core，以及GLM4.6英核心，未发现须重开贡献判断的共同理由。未独立逐篇重读其余无信号关闭项或247日期潜力；它们不是已证当窗候选。14实际入口、分页停止、RSS与版本日期依据及缺口隔离已对读；不将submitted、当月库存或当前版本当首公开证明。

作者侧完整筛选与以上独立核查分别保留；不是291全文复核，未读无关card附件/未核实现/未复现。当前V3、正文引用与围栏及限定路径空白检查通过；下载原README的上游相对LICENSE/email不当作作者引用错误。机器检查不替代以上语义复核。
