# Daily Research — 2025-09-17

**规范：** V3
**窗口：** 2025-09-16T09:00:00+08:00 ～ 2025-09-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T19:33:19+08:00

## 1. 结论

正式发布候选2家族，必要安全/负侧深入审阅及非作者证据复核2/2，root实际整合Ch62/Ch66两处最小增量，非写作者POST及DAY通过，本窗普通待办无。年龄策略同家族RSS确认09/16 14:00，scheming Blog另1家族09/17 08:00；不再datehold。年龄策略仍是建设计划；scheming行为下降不等于真实原则泛化，单环境反事实也不证明训练后动机。arXiv限流后恢复21标题，16个相关/含糊身份读精确v1完整题摘，仍是必要日期隔离项，不是当日论文数或全文队列。

Kimi折扣只支持计费事件；Google教材学习效果不直接证明模型系统机制，原方法的内容完整性验证潜力保留定点重开。小模型适应、局部结构评价盲区、图像偏好攻击及ATP token成本替代设计没有因应用、小样本或“不改通用原则”被机械排除。没有写共享Books、月README或LEARNING_STATE。

## 2. 来源覆盖

本日独立入口/请求原记录见[FETCH](../_sources/daily-20250917/FETCH.md)、[筛选与停止条件](../_sources/daily-20250917/DISCOVERY_SCREENING.md)及本目录引用的17*.json；当前目录切片不被扩大为历史全覆盖。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本日独立官方RSS HTTP200按UTC本窗筛4事件，年龄两篇同家族06:00 GMT、Stargate14:30 GMT、scheming Sep17 00:00 GMT；两正式家族核心/必要反侧已读，root准入校准通过 | 已检查 | 仅RSS/具名切片；独立Evidence/Books/POST/DAY已核，仅此切片，不授全站修订无遗漏 |
| SRC-ANTHROPIC | 本日Next JSON真实恢复172 publication，保留publishedOn；按UTC09/16 01至09/17 01过滤0条 | 已检查 | 仅此Research保留切片，不保证已删除历史材料 |
| SRC-GOOGLE-AI | Research pubs/月curl8秒超时；web月份实际page1/2到Sep11跨下界，Sep16教材核心+13348v1；DeepMind研究当前页与year路线 | 受阻 | DeepMind历史窗与Google pubs确定列表不足；教材通用完整性机制未核，不作为排除整个实现 |
| SRC-META-AI | 官方Research/publication入口curl8秒超时；web当前出版页取得但定点恢复失败；官方Sep16严格查询无返回 | 受阻 | 本窗FAIR历史分页不可确认；不作零论文 |
| SRC-QWEN | 本日保留Blog及新page_config API实际HTTP200原60带date配置，只筛UTC16T01→17T01为0，NextSep10T20Z/TTS21T20Z夹窗 | 已检查 | 本日独立capture，不借另一日coverage，不将60正文全排队 |
| SRC-DEEPSEEK | 本日独立官方API Change Log HTTP200，实际读Sep22→Aug21连续更新，跨本窗下界停止 | 已检查 | 保留更新切片无本窗条目，不授全机构历史完整性 |
| SRC-MOONSHOT | 本日Platform目录与09/16折扣原正文，关闭计费变化/参数重述 | 已检查 | 未把无配置的6x速度陈述授性能增量；不覆盖未列出的历史材料 |
| SRC-TENCENT-HUNYUAN | 首查Research shell；实际正确publicList POST9条全部当前；表外恢复12815v1摘要；组织/T1当前入口 | 受阻 | API最早2026不支持9月；12815原公开日期/方法增量未核 |
| SRC-ZAI | 首查Research实际page1/page2累积18，hasMore=false最早12月07；官方release Sep30/Aug11夹窗 | 受阻 | Research未保存本历史窗，不用release替代论文目录 |
| SRC-BYTEDANCE-SEED | 2025 type2 token0真实15/49，非置顶跨到08/21、07/14止；type1 token0及本日真实20/40/60/80分页，80 has_more=false/next空 | 受阻 | Blog有限窗已检查；papers total94仅20返回1条06/12 SwiftSpec，其他缺数组，不是0或94全筛 |
| SRC-BAIDU-ERNIE | 本日原Blog page1/page2，page2 Sep12PLAS与Aug14FastDeploy跨下界，prev-only停止 | 已检查 | 仅保留技术Blog；不授所有论文/代码事件覆盖 |
| SRC-XIAOMI-MIMO | 本日Paper8条Sep19Audio/Jun4VL跨本窗；两正确async chunks真实200，Blog15完整title/desc及组件8+7展开读到数组末尾，无另API分页 | 受阻 | 普通More已恢复；Blog原数组无日期/历史层未证，Paper不能授Blog覆盖 |
| SRC-MINIMAX | 本日US/Agent入口及CN窄恢复HTTP200；实际非script正文13条至Jan15，Oct27→Jan15跨下界停止 | 已检查 | CN保留切片无本窗条目；原minimax-cn-recovery.raw，不授删除历史/所有仓库修订覆盖 |
| SRC-ARXIV | 本日submitted主题查询超时；窄查询Rate exceeded，mainhost429；CL月1–2000/2214只浏览相关标题线索；触发HF21标题恢复，16精确v1题摘 | 受阻 | 12注册分类的主题/新命名历史公告未完整恢复；submitted/收录不可授first-public |
| 补检：[Hugging Face](https://huggingface.co/papers/date/2025-09-17) | arXiv限流后一次页面21标题、16相关身份回原域，API15秒超时即停止 | 已检查 | 只身份发现，不授来源覆盖、首公开或正面证据 |
| 表外：[Tongyi作者Blog](https://tongyi-agent.github.io/blog/) | 实际目录有DeepResearch Sep16条目，但无时区；只用于相关家族恢复 | 受阻 | 不能据目录日期证明论文首次公开完全落窗 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Building towards age prediction](https://openai.com/index/building-towards-age-prediction/) | 2025-09-16T14:00:00+08:00 | 可信principal不等于可靠推定属性→未知年龄保守策略与成人证明路径→分开推定/验证/政策纠正；1+2+2=5 | 深入完成 | 整合：`PLATFORM-GATEWAY` / [Ch62认证、授权与模型身份](../../../../books/part-06-ai-infrastructure/62-gateway.md#认证授权与模型身份)，推定属性/验证事实政策分离，非写作者POST通过 |
| [Detecting and reducing scheming in AI models](https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/) | 2025-09-17T08:00:00+08:00 | 外显违规下降不足识别动机→OOD/意识反事实与残余目标压力测试→分开行为率/评估识别/部署泛化；2+2+3=7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66发布验收要区分评估意识诊断与罕见风险证据](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#发布验收要区分评估意识诊断与罕见风险证据)，条件选轨迹反事实验证，非写作者POST通过 |

两家族准入和评分来自[root独立校准](../_sources/daily-20250917/INDEPENDENT_CALIBRATION.md)，不以评分倒推贡献或Books。年龄另篇[Teen safety, freedom, and privacy](https://openai.com/index/teen-safety-freedom-and-privacy/)是同一发布家族，不增计数；两篇RSS原06:00 GMT，scheming原00:00 GMT。表中深入完成已经非作者独立核必要支持与反侧；Books两段实际整合及POST通过。其他必要日期未核材料不先评分；它们仍在§5，不作零事件。

## 4. 证据与知识整合

### [Building towards age prediction](https://openai.com/index/building-towards-age-prediction/)

两篇Sep16原发布的Age prediction/Parental controls与隐私/安全核心已实际深入核受影响内容：不确定年龄时保守路由、成人证明与隐私代价是计划约束，分类器算法/阈值/误差/安全性能Not Disclosed，不能写已部署或通知可靠。实际Ch62认证链L98–112只将外部identity转可信principal，未表达推定属性与验证事实分离；root已在该链与Gateway日志后、重试节前实际整合一段（source-family `SF-2025-OPENAI-AGE-POLICY`），保留纠正路径和隐私/误判成本，明确为系统设计推断而非厂商内部实现。actual owner正文、相邻交接和Review notes经非写作者POST通过；证据与原建议见[必要证据交接](../_sources/daily-20250917/EVIDENCE_OWNER_HANDOFF.md)。

### [Detecting and reducing scheming in AI models](https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/)

原Blog完整核心及必要反侧已读；后续2509.15541v1仅核其拟命题，不反授17日论文公开。实际读§3训练/测试、§4 CoT限制、§5收益/残余失败、§6反事实、§7–9目标/继续训练/限制与相关Appendix C/D/E/J/K/O.1/P。covert动作是代理，人工确认依可读CoT；Fig9有选择性聚合，Chat另一协议且未由Apollo人工核，不能合并为部署率。反事实仅训练前o3的一个环境，条件选择轨迹，删除可连带诚实推理、注入可提高一般谨慎；不证明训练后真实动机或欺骗消除。能力与拒答代价、残余目标/继续训练风险均保留，未复现/核artifact/遍历所有转录。

实际Ch66已有sensor非裁决、CoT因果/行为分开及主动probe预算；root已在“发布验收要区分评估意识诊断与罕见风险证据”probe段后、rare-event段前实际整合这条受限实证验证（source-family `SF-2025-OPENAI-SCHEMING`），不声称旧原则缺失，也不因原则已有而拒绝新验证。精确source/version、必要证据位置、选择人口与建议段均在同一[交接](../_sources/daily-20250917/EVIDENCE_OWNER_HANDOFF.md)。actual段落及前后probe/rare-event衔接经非写作者POST通过；原精确稿§6链接只是辅助协议依据，不改变本日Blog事件归属。

其余日期隔离潜力不升级为证据完成：具体理由见[本日记录](../_sources/daily-20250917/DISCOVERY_SCREENING.md)。WebSailor-V2 v1标题与摘要身份不一致不拼后来说明；SPO maj@32非吞吐，Phi权限/转移、OBR硬件协议仍未授。Google13348v1局部教育图像语义负侧经root校准保留，不用学习成绩直接证明模型机制，不继承题摘为深审。

原预校准与窄恢复停点留在sources作过程历史，当前状态以上述必要证据交接为准。报告作者未改共享Books、月索引或LEARNING_STATE；root协调实际Books写入，非作者仅验收本日报告与必要段落。

## 5. 缺口与下一步

普通待办：无。非作者已独核2家族必要安全/反侧，root实际整合Ch62/Ch66，非写作者POST及DAY通过。以下外部日期/目录为本窗终态保留项，均不支持正面证据、候选、Books、无遗漏或性能/安全保证；取得原公告/有依据的完全落窗区间才定点重开，不机械要求秒级精度。

- 两正式发布家族日期、有效FIRST、必要Evidence、Books实际写入及POST已完成；[非作者验收](../_sources/daily-20250917/INDEPENDENT_DAY_REVIEW.md)保留真实范围与支持/反侧。没有把共享采用/写入/POST隔离成外部终态hold。
- arXiv 16家族精确v1：13310/13312/13305/13313/13311/13309/13232/13317/12541/12521/11177/10687/10696/11481/12815/12603，完整标题、实际潜力、v1原字段与不同待核点在[逐项记录](../_sources/daily-20250917/DISCOVERY_SCREENING.md)。原HTML/17primary*.json/17econprimary.json为恢复位置；只欠submitted不能归属，HF收录亦不能。接受原公开列表、作者首次开放原稿记录或完全落窗区间；归属确认后先校准，再按§4评分和§5方法/对照/反侧审阅，需Books时再比较owner实际论点。不是删池或已关闭重复项。
- 来源历史缺口：DeepMind/FAIR/Hunyuan/ZAI/Seed-paper、MiMo Blog及arXiv注册主题公告。请求/停止见§2/FETCH；Seed本日已到token80 has_more=false，MiMo More15已展开，缺的是历史数组/日期，不再是未执行普通分页。接受能定位本窗的原分页/归档/API正文及日期；shell/空搜索不替代历史覆盖，不授零事件。OpenAI RSS、DeepSeek更新和MiniMax CN有限切片已恢复。
- Google教材：原“教育成绩不能直接证明系统机制”关闭命题不等于排除全实现。精确13348v1 §2–4已窄补，自动完整性未披露，简单教育图像语义失准的局部负侧保留供root校准；缺原始公开时区/完全落窗区间，不评分或采用。原公开证据到达后定点重开该命题，不重扫Google目录。

## 6. 复核

复核者：Codex / sept07_10_author（非报告作者Tesla、非Books写作者root）；复用root有效FIRST，不重跑未变化校准。

结论：通过

实际检查范围：[非作者DAY与POST](../_sources/daily-20250917/INDEPENDENT_DAY_REVIEW.md)。两正式家族日期/准入及必要安全深入证据2/2、两owner实际正文与相邻交接、root两处写入的非writer POST、14来源真实有限停止均核过。复用root对16个arXiv精确题摘及风险/含糊8项的校准，保持具体潜力与日期隔离，不把它们当审阅完成或全文队列。Kimi/Stargate完整核心作为计费/采购意向退出样本；Google目录临界SLED补读原Blog、Aug19 v3完整题摘与作者代码News，按已公开方法/验证/代码重述关闭，不因机制旧而机械关闭新证据。原科学/非主线5个HF标题只核范围理由，未无差别重读附件。

Books Ch62认证/政策分离及Ch66评估意识条件干预两自然段实际检查通过，既有身份、sensor、rare-event与重试路径保留，未虚构部署或安全率。日期/历史终态保留不用于正面Evidence/Books、无遗漏、性能或安全保证；材料到达只精确重开。V3与限定diff-check通过，机器只核结构，不能代替语义验收。
