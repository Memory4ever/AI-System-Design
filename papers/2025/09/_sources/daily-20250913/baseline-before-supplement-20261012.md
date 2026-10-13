# Daily Research — 2025-09-13

**规范：** V3
**窗口：** 2025-09-12T09:00:00+08:00 ～ 2025-09-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T20:48:12+08:00

## 1. 结论

本日1个确定落窗家族：OpenAI CAISI/AISI安全更新，传统软件漏洞与Agent hijacking组合使原本看似不可利用的漏洞进入实际权限风险路径。复用有效独立校准的6分、安全必要核心与Ch72具体已有覆盖，正文增量0；非作者整日验收已完成。arXiv123条只作提交主题查询线索：完整题摘处置82条，其中67具体潜力日期隔离、15关闭；另41明确领域标题范围关闭。非作者定点纠正了部分标题即关闭的过宽范围理由，以及两项只有一般综述的过宽准入，没有把宽库存扩为全文队列。

当前Books正文增量0，官方PoC没有公开足以复现的版本、trace、分母或patch，不能授总体安全率/已验证修复。VaultGemma有sequence级DP取舍潜力，但公开时间只相交，仍不采用本日日期。12份指定风险/理论精确v1必要方法与限制已非作者核读，Lipschitz概率代数/例值矛盾与安全争议保留；支持对话新增反侧仅支持局部标注评价，不授临床获益。Seed paper补到末页仍缺条目数组，其余日期/历史列表缺口作为精确终态保留，不支持正面Evidence、Books或无遗漏断言。

## 2. 来源覆盖

本日实际独立请求与有限停止见[原始目录](../_sources/daily-20250913/)，`transport.json`和针对性记录保留执行时间/URL/超时18秒/12MB上限；不继承其他日报结论。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS原pubDate本窗Sep12 12:00GMT安全更新；直接正文403后web官方全文真实恢复并保留工具原记录 | 已检查 | 1家族必要核心、独立准入及Books已有覆盖有效复用；RSS不是全站无遗漏 |
| SRC-ANTHROPIC | 本日Research SSR字符串实际解码，publication原日期Sep5→Sep15T09Z/T20:33Z跨窗 | 已检查 | publication目录切片，不遍历库存全文或已删除记录 |
| SRC-GOOGLE-AI | DeepMind page5 Nov2025→Jul2025，相关原文Sep25/22/17；Research月1→2/2共13条Sep30→Sep9，Vault核心本日完整读 | 受阻 | VaultSep12无时区/时刻，尚不支持完全落窗；月目录不授全部pubs覆盖，科学应用暂缓 |
| SRC-META-AI | Blog3主序Oct24→Aug27/14且旧pin分开；错误publications页45 bytes后实际正确results publication page5→6（275489/275691 bytes），末Sep15→首Sep8 | 已检查 | 错误route不是0；有限窗口前缘处理，不授全历史 |
| SRC-QWEN | 新官网research配置57428 bytes，10个9月对象原ISO；Next Sep10T20Z，ASR Sep8T06:38Z，余Sep21/22/24 | 已检查 | 不相交本窗；不以retrieval首页代历史或复制11采用 |
| SRC-DEEPSEEK | 官网+updates，本日实际Sep29/22→Aug21 | 已检查 | 仅官方公开更新切片 |
| SRC-MOONSHOT | 本日完整可见平台Blog Sep16→Sep5→Aug22 | 已检查 | 无具体本窗repo release触发，不扫普通PR |
| SRC-TENCENT-HUNYUAN | 首查Research shell；实际正确host POST pageNum1/pageSize100/renderType0，9=total9 | 受阻 | 全是2026记录，不能授2025历史；需历史全部列表/具体本窗原文 |
| SRC-ZAI | Research与notes Sep30→Aug11；真实page2→3重复18项，2026Aug26→2025Dec7、无更多 | 受阻 | 已执行窄分页仍未跨9月，Research历史不支持0事件 |
| SRC-BYTEDANCE-SEED | 本日type2/year2025/page0/count20/desc 15/49/has_more，非pin Oct22T16Z→Aug20T16Z→Jul；type1 page0→20→40→60→80实际请求，末页has_more=false、total94 | 受阻 | Blog非pin跨窗停止；paper20仅June SwiftSpec，其余页缺sub_article_list，不把94缺失记录记0，需完整历史数组 |
| SRC-BAIDU-ERNIE | Blog实际1→2/2；PLAS原datePublished/Modified Sep12T00Z→08BJT，窗起点前，原正文本日取得 | 已检查 | 不以date-only迁入13或继承前日贡献判断 |
| SRC-XIAOMI-MIMO | 本日8Paper/15Blog标题及home chunk实际读，More仅切初8/余7无新fetch；Paper Sep19→Jun4 | 受阻 | 历史Blog日期/条目未恢复；不是未执行More分页 |
| SRC-MINIMAX | 本日EN12/CN13、英文page2派生文本同首页；Agent techblog及llms.txt实际当前单项2026 | 受阻 | CN Jan15旧锚不证明中间无事件，历史分页/Agent列表仍缺 |
| SRC-ARXIV | 12分类+language model/Transformer/MoE/Agent/Diffusion/GPU/VLM/World Model submitted Sep11 18Z→Sep12 18Z；两个API均123/123；123标题→82完整题摘，41清楚领域标题关闭。advanced只恢复表单及announcement年/月说明；不重复全月扫描 | 受阻 | submitted≠first-public；67潜力精确日期隔离，当前v2/v3/v4不冒充历史v1；12指定风险/理论v1必要反侧及新增评价样本已核，不授正式落窗、完整Coverage/无遗漏 |

未扫描每周组。表外NIST由官方安全候选链接触发必要身份/反侧检查，非全站扫描。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Working with US CAISI and UK AISI to build more secure AI systems](https://openai.com/index/us-caisi-uk-aisi-ai-update/) | 2025-09-12T20:00:00+08:00 | 传统漏洞原看似不可利用→Agent hijacking串联局部反例→安全验收需跨软件/模型控制边界；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)的executor effect-time授权、run单位与集成fixture/effect身份；root单项独核通过，正文增量0 |

其他67题摘潜力未确定落窗，不计候选或评分；15完整题摘关闭及41标题范围关闭分开计数。原判与反证保留在[筛选](../_sources/daily-20250913/SCREEN.md)、[有效首批校准](../_sources/daily-20250913/INDEPENDENT_FIRST_CALIBRATION.md)及[整日独立验收](../_sources/daily-20250913/INDEPENDENT_DAY_REVIEW.md)。

## 4. 证据与知识整合

### [Working with US CAISI and UK AISI to build more secure AI systems](https://openai.com/index/us-caisi-uk-aisi-ai-update/)

采用身份为Sep12官方发布，时间由本日RSS原GMT支持；当前官方完整核心web L39–74真实读到，HTTP403不冒充正文已得，[原工具记录](../_sources/daily-20250913/openai-caisi-web.json)与[交接](../_sources/daily-20250913/HANDOFF.md)保留证据位置。厂商披露传统漏洞与Agent劫持组合的局部失败路径；约50% PoC没有公开attempt/样本分母、精确漏洞、完整trace/实现或修补版本，不作总体率或修复实现审计。关联NIST是Jan2025 AgentDojo及Dec2024 o1评价，不是此次July ChatGPT Agent漏洞的独立复现；特权访问测试与普通用户条件分开。

作者实际读Ch72 1245–1297的untrusted输入/effect-time executor控制，764–812的run/attempt/集成评价条件，2989–3012的connector/credential/destination/fixture/effect身份；Ch71 1–75、Ch73 1–55与Ch78 167–197相关交接已读。root有效单项独核实际原文、RSS及owner相邻论点，裁决已有覆盖、无拟增自然段；本次非作者复用该有效结论，再独立核剩余本日处置，见[整日验收](../_sources/daily-20250913/INDEPENDENT_DAY_REVIEW.md)。不把厂商合作声明当生产保证，未复现或执行攻击。

Vault本日完整核心支持1024-token packed sequence级DP、Poisson采样与fixed-batch处理，不能授user/doc DP；尚缺本窗公开日期，不采用。arXiv82完整当前题摘不等于精确历史v1证据。独立指定的11风险信号与10439理论已定点核精确v1机制/限制，见[必要反侧](../_sources/daily-20250913/NECESSARY_CORE.md)：privacy SSIM/ARX局部测试不授DP或任意重识别保证；firmware log扫描不授coverage/物理WCET；LLM想象干预不授可识别因果；Local SGD只在convex、i.i.d.同分布、无偏有界方差及联合stepsize下成立。10298v1概率权重和数值例子矛盾、作者承认global Lipschitz未验证，保留争议。新恢复10184的情绪支持反侧中Severe标注一致性明显较低，1490是配对回复而非1490独立用户/临床测量；10059图像数学测试需区分11场景/814实际车辆与16k车辆样本，不能从题量授独立场景泛化。全部日期隔离不进入Books，不把已读称安全已证实。

## 5. 缺口与下一步

普通可执行待办：无。正式项的日期、准入、必要深入和具体已有覆盖有效复用；其余本日必要处置及日级非作者复核已完成。

- 本节唯一候选的官方原文/日期、6分准入和Ch72/71/73邻接No Change已核验。未公开漏洞细节/patch仅约束可采用范围，不请求无关实现或授已修复保证。
- 终态保留项——arXiv67潜力：原`scoped-abstracts.json`扣除最新关闭、补入`INDEPENDENT_DAY_REVIEW.md`九项恢复身份；需要官方公告/作者首次正文公开支持完全落窗区间，及拟采用项必要历史v1。submitted与month不授权。12项指定必要v1核心已核，不把普通未读核心当外部终态。日期材料真实回归才重开该身份，不将123全文入队；10298的代数矛盾与global bound争议不可隐去。不支持正面Evidence、Books、零事件或无遗漏断言。
- 终态保留项——[VaultGemma](https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/)缺公开时区/时刻或完全落窗区间，Sep12日期仅相交。原公开元数据/artifact记录回归时重开该家族，不凭DataCite/仓库创建日迁移；不支持正面Evidence/Books或无遗漏断言。
- 终态保留项——Hunyuan、Z.ai Research、Seed paper、MiMo dated历史Blog、MiniMax历史Agent/分页：§2实际有限停止，Seed已补20/40/60/80至has_more=false仍缺数组。原完整历史列表/具体原文回归后只重开本窗主题；不支持正面Evidence、Books、无遗漏或零事件。

窗外PLAS原ISO在Sep12 08BJT、Qwen Next在11日04BJT，不属于本窗，不扩另日报。

## 6. 复核

复核者：sept07_10_author（本日非报告作者；复用root有效FIRST/唯一正式项结论）。实际补读原余35完整题摘、定点重开13份含糊题摘；核12指定风险/理论v1必要原件、新增评价反侧和14来源停止，补Seed真实分页；关闭分层与日期/Books隔离见[独立日级验收](../_sources/daily-20250913/INDEPENDENT_DAY_REVIEW.md)。未复读有效已通过34份、未授全量附件或来源无遗漏。

结论：通过

恢复本轮已运行V3报告结构/一致性校验与限定范围diff检查，均通过；不替代独立语义复核。
