# Daily Research — 2025-09-11

**规范：** V3
**窗口：** 2025-09-10T09:00:00+08:00 ～ 2025-09-11T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T14:17:56+08:00

## 1. 结论

本日正式候选1个唯一家族Qwen3-Next：root实际读取官方完整正文/精确config对象及Ch22完整相关段后，新增准入、日期与三项机制Books已有覆盖通过。6分，版相关runtime兼容及native/YaRN分界按必要受影响内容深入审阅；只采用条件化hybrid机制与作者有限图趋势，不采用10x或3:1普适因果。Books正文增量0，Aristotle13:59独立DAY及有限返修复核通过。arXiv两feed各146、交85、并207、各独61，仅submitted-window discovery而非当天新论文；月分类表只作ID带标题查漏。35差额最小潜力路由已按非作者实际题摘复核同步，日期仍隔离，不扩全文队列，不写零事件或无遗漏。

关键保留：异构 GPU 可按模块而不只是阶段分工；expert 缓存单位可小于整 expert；interaction horizon 可为训练课程；合成数据支持集和 downstream utility 不等价。这些仍有日期边界。Selective Induction 的一般 Claim 尚未完整证明，RewardDance 的 variance 不证明无 hacking，安全 guide 的 single-tool executor 不证明完整 control-flow integrity。所有未确认日期/安全中心争议均不进入 Books。共享 Books 没有作者写入；root最终核对六部分及独立裁决，未授实验复现或无遗漏。

## 2. 来源覆盖

扫描实际运行于2026-10-06，本日原响应/失败与替代路径均保留在 [本日原始目录](../_sources/daily-20250911/)。停止指有限入口已处理，不认证机构历史没有未列出材料。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 `news/rss.xml` 全返回760851 bytes；原 pubDate 保留，Sep9 SafetyKit 与 Sep11 14:00GMT 公告夹住窗口；相关题目有限检查，`openai.raw` | 已检查 | RSS 不是全部未公开/删除研究的保证；本窗没有 RSS 落窗事件 |
| SRC-ANTHROPIC | Research Next.js 实际解析 self.__next_f.push 的 JSON 字符串，恢复172个 publication；publishedOn 原值，9月条目 Sep5、Sep15，不命中本窗，`anthropic.raw` | 已检查 | 不把172库存视为全文队列或删除记录覆盖 |
| SRC-GOOGLE-AI | DeepMind Blog 实际页3→4→5，页5从Nov2025跨至Jul2025；相关9月原文 JSON-LD Sep17/22/25；Google `/blog/2025/09/` 实际1→2/2，共13条，末Sep9；Sep11 cascades 核核心并回 linked 2405.19261，`deepmind-page*.raw`/`google-month*.raw` | 已检查 | 月/日期标签不自动授精确窗口；Speculative cascades 是既有2024方法的新说明，无当前新研究增量；不授所有 pubs 无遗漏 |
| SRC-META-AI | Blog实际1→3主序Oct24→Aug27/14与旧pin；publication page5 Nov18→Sep15，再到真实`results/?page=6&content_types%5B0%5D=publication` Sep8→Sep2→Jun13。Aristotle05:35:02Z实际补GET200/275689 bytes及身份停止见[DAY §2B](../_sources/daily-20250911/INDEPENDENT_DAY_REVIEW.md) | 已检查 | page5不含Sep8/2；泛用page6的45-byte unavailable不是0。非严格排序/旧pin不授全历史保证 |
| SRC-QWEN | 旧首页Sep23→Aug19不是完整目录；实际执行新站研究配置API，原日期/tokenLinks定位Qwen3-Next，date=`2025-09-10T20:00:00.000Z`，正文101627 bytes；[窄重开](../_sources/daily-20250911/QWEN_REOPEN.md) | 已检查 | root已核此公开日期/准入与限定Books覆盖；不授官方目录全部删除记录或无遗漏 |
| SRC-DEEPSEEK | 官网+官方更新说明实际Aug21→Sep22/29，`deepseek.raw`/`deepseek-updates.raw` | 已检查 | 只授该官方公开更新切片 |
| SRC-MOONSHOT | 平台Blog实际列表Sep16→Sep5，`moonshot.raw` | 已检查 | 未据列表穷举全部repo artifact；无具体本窗release触发，不扫完整GitHub |
| SRC-TENCENT-HUNYUAN | 首查Research动态shell；实际提取JS路由，正确host `api.hunyuan.tencent.com/api/blog/publicList` POST pageNum1/pageSize100/renderType0，9条=total9；错误host404保留，`hunyuan-api-correct.raw` | 受阻 | 返回全是当前2026记录，不能授2025历史；浏览器恢复调用超时，无有效UI证据。需历史全部列表/原始9月条目后只重开本窗 |
| SRC-ZAI | 首查Research与发布说明Sep30→Aug11→Aug8→Jul28；后实际执行 `/zh/research?page=2`、`?page=3`，均1397454 bytes/相同18可见条目，2026Aug26→2025Dec7并称没有更多，`zai-page2.raw`/`zai-page3.raw`及派生文本 | 受阻 | 窄分页已执行但重复当前18项，未跨2025Sep；release-notes切片可用，Research历史未恢复，不把该重复页当0或完整覆盖 |
| SRC-BYTEDANCE-SEED | 官网论文shell→实际 `/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true`：15返回/total49/has_more；非pinned Oct23→Aug21→Jul足以跨本窗，pinned Seedream Sep9在窗外；type1 US/CN均total94/has_more却无sub_article_list，`seed-*-api.raw`/`seed-paper-*.raw` | 受阻 | Blog已实际有界恢复并停止page0，不把仅旧pinned当停止依据；论文API缺正文列表，不记0或完整覆盖。需可读历史paper条目 |
| SRC-BAIDU-ERNIE | 技术Blog真实page1→2/2，Sep12 PLAS→Aug14 FastDeploy，`ernie.raw`/`ernie-page2.raw` | 已检查 | 无当前列表落窗项，不授repo全部研究覆盖 |
| SRC-XIAOMI-MIMO | 官网Paper8条、Blog15可见，Paper Sep19Audio→Jun4VL，`mimo.raw` | 受阻 | Blog无可核日期且More未恢复历史；需要9月原始Blog目录或具体首发正文，不称整目录无命中 |
| SRC-MINIMAX | 英文12条末Oct27、中文13条末Jan15，分列端点；英文`?page=2`同首页，Agent当前切片，`minimax*.raw` | 受阻 | 仅CN可见切片跨本窗，EN/pagination与Agent历史未恢复，不授全历史0事件；需历史分页/原文 |
| SRC-ARXIV | scoped12分类主题和无该分类限制的supplement同义组，submitted UTC Sep9 18→Sep10 18；各start0/max200/146，无尾页，交85/并207/各独61。月ID08000～08840的256标题查漏及11+37精确v1另述；[原筛选](../_sources/daily-20250911/SCREEN.md)/[35差额](../_sources/daily-20250911/DAY_DELTA_ROUTES.md) | 受阻 | 偏宽attention/GPU/agent返回仅发现缓存，后续按模型/系统/LLM Agent/多模态语义收窄，不扩整类。CV/RO截断、CL2000/2214非全月；day-list失败/advanced月级。207不授公开日期/候选/全文分母，schedule/API/DataCite不授first-public |

没有扫描每周来源组。按需清单没有实际新发布触发；作者项目页与精确论文版本是已发现材料的必要证据，不是按需全站扩扫。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Qwen3-Next: Towards Ultimate Training & Inference Efficiency](https://qwen.ai/blog?id=qwen3-next) | 2025-09-11T04:00:00+08:00 | 纯线性状态recall与完整历史成本冲突→GDN/gated-attention混合发布分支→重新核条件化state/KV取舍；2+2+2=6 | 深入完成 | 已有覆盖：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md#hybrid-与迁移明确两类状态怎样共同承担历史)；配置/recipe及图仅作版本事实报告，正文不增 |

Qwen新增独核由root明确给出，Aristotle必要core/owner独核仍通过该单项，不扩为DAY。七首批/代表/安全见[交接](../_sources/daily-20250911/HANDOFF.md)及[校准](../_sources/daily-20250911/INDEPENDENT_CALIBRATION.md)，未授日期。新增35差额只保留题摘支持的最小潜力，读取者为Aristotle、作者复用有效判断，见[差额](../_sources/daily-20250911/DAY_DELTA_ROUTES.md)；EvolKV08315遗漏已补，08120 FL thesis/08318 early-exit分开，08157风险预算/可行性改判。全部日期未授，均不赋本窗分数或进Books。

## 4. 证据与知识整合

### [Qwen3-Next: Towards Ultimate Training & Inference Efficiency](https://qwen.ai/blog?id=qwen3-next)

官方研究配置直接绑定题名、id、tokenLinks与原date=`2025-09-10T20:00:00.000Z`，UTC转北京时间11日04:00；不是以search/index/submitted补造时刻。正文当前官方token版本、实际三图和限定命题保存在[Qwen证据](../_sources/daily-20250911/QWEN_REOPEN.md)。75%GDN/25%gated full-attention与稀疏MoE共同改变了state、显式历史、计算和recipe，不隔离hybrid因果或3:1最优。吞吐图未披露hardware/precision/batch/concurrency/SLO/runtime；不采用10x通用数字。RULER的192K与1M有比235B更弱的切片；262144 native与1M YaRN扩展分开，static YaRN可能伤短序列。Blog提示main分支、实现依赖与Transformers MTP限制，只采用作者声明边界，未运行/核验runtime实现或复现。

root实际读完整正文Introduction→References、config中精确对象，以及Ch22 Hybrid/Outputgate完整段，已授准入2+2+2=6、日期和Books NoChange。三项机制由Ch22 501～509的GDN写入/衰减、781～801的双状态/KV取舍、863～871的output gate与memory gate差别实际承载；不是凭主题相似判已有覆盖。版本配置、训练recipe和局部图保留报告，不重复堆进书稿，无拟增自然段。该独核不授整日DAY。

[精确 v1 证据笔记](../_sources/daily-20250911/EVIDENCE.md)保存七项必要方法/评价反侧、08646实际威胁模型与A.1代码、08151v1版本修复；每项说明真正读到的节/页、未读而将来命题需要的内容和不采用的主张。AgentGym PDF首次部分传输与后续完整11939091字节分开保留，Fig7实际渲染核查；没有复現或运行作者实现。

Speculative cascades 官方Sep11 Blog没有明确时区/时刻，但处置不依赖落窗：核心方法、deferral rule与Gemma/T5评价均回到链接的2405.19261（v1 May29 2024/v2 Oct21 2024），没有当前新增实验/方法/纠错，不作为本窗新贡献；不是“已有有效审阅”去重声明。首次公开/重要修订分别处理，不借新Blog日期迁移论文。

其余日期/必要证据项仍暂缓，正面写入0；没有将潜在owner主题相似称已有覆盖。Ch15/27/31/54/55实际论点与条件路由见证据笔记，仍缺差额/实现的明示；恢复落窗且证据经root独核后才交精确自然整合建议。

## 5. 缺口与下一步

本窗可执行待办0。Qwen/七必要core有效工作不重跑；Aristotle13:36 DAY要求A/B/C已有限同步，13:59仅重核差额及最终六部分通过：207计数、35最小潜力、Meta真实5→6、身份修正与风险预算改判。以下均为本窗终态保留项，不用于正面证据、Books、完整Coverage、无遗漏或安全保证；恢复后只重开具体受影响项。

外部保留项：

- arXiv：七原潜力、安全08646、SCREEN及35差额具体身份缺first-public完全落窗支持；需官方公告/作者首次正文或有据完整落窗区间，不机械要求秒级。对应abs/feed重开日期和家族后才定点补拟命题，不把并集207或35差额变全文队列。late ID、后续v2/v3等不倒授本日日期/旧版结论。
- Hunyuan历史目录、Z.ai Research历史论文、Seed type1论文API、MiMo dated Blog/More、MiniMax Agent历史与有效分页：实际尝试及原响应见§2；历史材料恢复后只查本窗相关主题。当前记录不支持Coverage通过、零事件或无遗漏；不进入Books。
- 08646安全保证争议：即使日期恢复也需可信plan验证、参数/调用次数/重规划授权边界或有效adversarial证据才能采用control-flow抵抗结论；现在只保留风险反侧，不自授该声明。

窗外线索不属于本窗：Google linked2024论文、DSM作者更早家族、ExRAP NeurIPS2024、CAI ICLR2025workshop等仅保留实际身份恢复需求，不称旧报告已有效审阅，不创建别日报。

## 6. 复核

复核者：root、Aristotle（均非作者）。

结论：通过

七首批及Qwen单项有效通过；Aristotle13:36 DAY发现A/B/C，作者13:49有限同步后，Aristotle13:59仅重核差额和最终六部分通过。实际[DAY](../_sources/daily-20250911/INDEPENDENT_DAY_REVIEW.md)读195唯一arXiv身份完整题摘（162在207并集/33定点查漏），其余45只标题范围，未审全月/全文附件；Qwen完整官方正文/config/三图/Ch22及七必要core、安全反侧实际范围见该记录。35差额读者不是作者，复用不等新增全文或候选。来源Meta普通补查已核，外部日期hold不授Coverage/Evidence/安全或无遗漏。root通读最终六部分与差额裁决后同步本次完成状态，不重跑有效研究或改Books。

机器校验：本次 V3 结构、全部本地 Markdown 引用与限定范围 diff-check 已检查；仅验证结构、链接和一致性，不替代语义复核。
