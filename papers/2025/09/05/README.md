# Daily Research — 2025-09-05

**规范：** V3
**窗口：** 2025-09-04T09:00:00+08:00 ～ 2025-09-05T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T22:22:14+08:00

## 1. 结论

本日独立恢复14每日来源，四条大模型/系统/多模态/Agent主题查询126原始命中去重103题名；原86加独审定点重开3，共89实际读完整精确v1题摘，68保留潜力、21关闭，另14只读题名的范围外条目不是摘要/全文队列。官方核心另4家族，1正式、3关闭。93完整题摘/官方核心筛选家族最终为正式1+日期潜力68+关闭24；45家族实际读必要定点核心，未授93 FullEvidence。

arXiv提交记录不能替代本窗首公开。合法catchup原文明确历史超过90天，68潜力暂隔离，不能进入正面证据/Books或授“无遗漏”。Anthropic独审发现正文published_time/datePublished/visible time一致09-05T00Z，root实际独核接受08:00BJT发布事件；当前正文modified2026-07-08另列，不授所有现存文字冻结2025。两项精确撤回分别处理：06996 current Admin撤回，04104仅v1许可删除且v2后来恢复，不全家族删除。

正式Anthropic材料的有限贡献是文本安全代理的uplift不等真实过程能力、预防性门槛不是风险已被实证；深入受影响安全内容，root亲读具体Ch66/72后仅报告。另必要反侧揭示MCP真实ID不等语义正确、safety检索槽位不等完整合规、量化memory下降不等latency下降、probe高ID分数不等OOD语义安全；这些日期潜力不得写入Books。当前无书稿改动/未授已有覆盖。独立DAY已通过，正式1/1深入完成、1/1仅报告；本日已无可执行待办，日期/历史目录保留项仍隔离，不被授为Coverage或Evidence通过。

## 2. 来源覆盖

所有入口、HTTP原件与请求时间在[本日_sources](../_sources/daily-20250905/)，查询表达与停点见[capture.py](../_sources/daily-20250905/capture.py)、[筛选](../_sources/daily-20250905/SCREENING.md)及[有限历史补检](../_sources/daily-20250905/HISTORY_WEB.md)。下表不把当前网页/配置当2025冻结，也不把空结果当零命中。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS1247条按本窗过滤；09-04T11:30Z opportunity官方完整文章恢复，09-05T08Z/10Z的Greek/hallucination均窗外 | 已检查 | 不把RSS当机构全年研究全覆盖 |
| SRC-ANTHROPIC | Research当前目录到08-27→09-05 biorisk；官方正文0–44完整读；正文article:published_time/datePublished/time均09-05T00Z，root独核接受08:00BJT正式事件，modified另为2026-07-08 | 已检查 | 不授当前所有文字冻结2025；不是新classifier算法/实际风险已证 |
| SRC-GOOGLE-AI | Research Publications当前页+September Blog两页13条09-30→09-09；DeepMind Research/Blog page5实际24卡Nov→Jul，09-04 LIGO官方publication/文章恢复 | 受阻 | 当前Publications/Blog不能授2025窗冻结全覆盖；有限官方定点查询未恢复独立publication窗口表 |
| SRC-META-AI | Research及官方publication results page5/6实际到09-24→09-15→09-08→09-02→08月（混旧2017条目）；Blog实际href分页2/3，page2止10-31，page3见08-27/14/07与旧2024 | 受阻 | 不用Blog替代Research覆盖，不以排序/当前卡间空隙授2025冻结 |
| SRC-QWEN | 官方research-list JSON60项，日期段08-18→09-08/10/21/22/24；核draft/date字段 | 已检查 | 配置date/draft非首公开证据，不授历史目录完整 |
| SRC-DEEPSEEK | 官网当前V4.1与官方updates，08-21→09-22/29跨本窗 | 已检查 | 当前updates不是已冻结历史全站目录 |
| SRC-MOONSHOT | Kimi Blog当前2024–2025目录、09-05 K2-0905→08-22停点，完整09-05公告 | 已检查 | 不由日期标签或产品context/速度指标授新模型机制 |
| SRC-TENCENT-HUNYUAN | 首查Research动态页及实际publicList POST page1/pageSize100/renderType0，9/9条均2026；本日限定2025-09-04官方查询 | 受阻 | 缺2025本窗Research冻结/原始发布清单；不授零命中/全覆盖 |
| SRC-ZAI | Research实际page1/2共18卡，page2止12-07且无More；官方release09-30→08-11/08 | 受阻 | Research当前截断未恢复2025窗独立目录，不借release当全部论文 |
| SRC-BYTEDANCE-SEED | Research/2025 blog token0实际15/total49，09-08T16Z→08-20T16Z跨窗；paper token0/20/40/60/80响应，total94但仅20见SwiftSpec06-11T16Z、80 has_more=false，其余空 | 受阻 | 94是API total不是94条已读；空页/非单调目录不足授窗内0或论文全覆盖 |
| SRC-BAIDU-ERNIE | 技术Blog两页16卡，09-12→08-14→06-30停止，实际链接检查 | 已检查 | 不以当前目录授全站历史冻结 |
| SRC-XIAOMI-MIMO | 当前主页Paper8卡（2026→10-21/09-19→06-04/05-12）、Blog15卡；实际index/home/component JS核本地slice/More而非未核API | 受阻 | 当前8+15不是2025窗冻结；未由More字样推断隐藏日期或全覆盖 |
| SRC-MINIMAX | 英文真实12卡，中文13卡（额外MiniMax01），EN page2仍12；Agent Tech Blog实际当前May13 2026 | 受阻 | 当前列表/同内容page2不能授2025冻结；不采用旧13英文错误计数 |
| SRC-ARXIV | 四主题submitted区间原始39/19/20/48→103题名→原86+独审定点3，共89完整v1题摘；current comment轻核89，2精确撤回定点；合法CL/CV catchup真实400原文90天限制，日期型list400/月archive404/web恢复cache-miss | 受阻 | 68潜力缺精确官方公告/同窗v1冻结，不能以submitted或晚发现ID授落窗，也不授分类召回完整 |

只加载每日14源与必要原始证据，不扫Weekly，不把AI for Science领域研究经Evaluation/Agent类比引回。未恢复来源明确隔离，不依赖它们支持候选或“无遗漏”。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Anthropic：Why do we take LLMs seriously as a potential source of biorisk?](https://www.anthropic.com/research/biorisk) | 2025-09-05T08:00:00+08:00 | 文本代理uplift/真实过程结果不等价，预防性安全门槛不等实证风险；2+2+2=6 | 深入完成 | 仅报告 |

arXiv68潜力仅在§5日期保留，不能先列确定当窗候选、不能用访问/Books处置给分。其余24关闭见原筛选，不在此重列为候选。

## 4. 证据与知识整合

[必要核心](../_sources/daily-20250905/NECESSARY_CORE.md)记录44arXiv+Anthropic1实际版本、段落/PDF物理页、已证明/未证明内容；另两撤回状态只支持排除。HTML优先，04198/03828实际HTML404后PDF恢复，不把所有已下载core授全篇全文审阅。日期保留不进入正面采用链。

本次Books仍纳入流程；日期潜力暂缓并保留重开条件，不作“已有覆盖”伪结论。Anthropic仅报告、无书稿改动；不写共享书稿/索引，不把未读正文包装成知识已覆盖。

### [Anthropic：Why do we take LLMs seriously as a potential source of biorisk?](https://www.anthropic.com/research/biorisk)

采用当前官方正文0–44的限定证据说明及明确published_time事件；dateModified2026-07-08为当前版本边界，不宣称所有文字冻结2025。专家quiz与去safeguards Claude4的两日plan在internet-only控制下由专家rubric评出uplift，既有2024基础wetlab n=8未见uplift；更大实验仍计划，不能把文字代理成绩外推真实复杂过程能力，也不能由小样本未见效排除全部风险。

Opus4无法排除能力uplift时，以输入/输出constitutional classifiers和ASL3作precautionary门槛，是在能力/测量不确定下的发布取舍，不是已经证明现实风险或公开新classifier算法。root独核接受2+2+2=6且安全深入所需核心；Books裁决仅报告。

root亲读 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) proxy→真实outcome及safety refusal/harmful-uplift分账（约125、809–816行），以及 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) FSF治理要求≠控制有效段。本篇是已有测量原则的受限安全案例，未披露可再实现的新classifier/系统机制；当前2026 modified正文也不能充作2025 exact-body冻结，所以仅报告，不作新知识写入。这不是未经审阅而关闭：受影响安全核心深入完成，版本和外推边界仍保留。

## 5. 缺口与下一步

普通可执行工作：无。本日报独立DAY及发现的定点修正已完成。三个含糊题名10526/19305/04169完整v1题摘已补，root FIRST与DAY实际核两恢复/一具体贡献关闭，10526/19305必要资源/生成核心已独读并同步分母；03918已改为thought路径/树冗余而非表格flatten。Anthropic出版字段FIRST/Books裁决已独立核验；剩余潜力不是任意全文队列，没有以日期受阻跳过普通待办。

本窗终态保留项（不用于正面证据、不进入 Books、不支撑“无遗漏”或覆盖完整/安全/性能保证）：

- arXiv68项，精确身份与完整题摘逐项在[SCREENING潜力表](../_sources/daily-20250905/SCREENING.md)。缺2025-09-05官方公告与相应v1当时公开冻结/可信等效原始时间材料；合法CL/CV catchup正文明确90天期限，月份恢复404，有限网页恢复失败。所需不是再读68篇全文，而是公共公告/同版首公开时间证据。恢复后逐项确认是否全落本窗，才评分、审阅与Books；只重开受影响事件，不移submitted字段归属、不扩邻日。
- Hunyuan、Google Publications、Meta Research、Z.ai Research、Seed论文、MiMo、MiniMax当前目录不能证明本窗历史覆盖。具体已尝试入口/停止见§2及原始请求；替代是本窗可核官方冻结、原始日期目录或具体发布事件。到达后只补该源本窗相关切片；保留项既不是零命中也不是Coverage通过，不无限追全站历史。

06996 current撤回与04104v1许可撤回是排除，不是访问故障或日期潜力。06996仅在官方撤回解除/有效替代且事件能落窗时重开；04104后来有效v2按11月真实事件处理，不属于本窗、不阻塞本窗，也不删除它。

## 6. 复核

复核者：root（独立FIRST有限准入校准）；sept07_10_author（非作者独立DAY）

结论：通过

root实际FIRST范围与具体改判见[SCREENING](../_sources/daily-20250905/SCREENING.md)：14关闭、8潜力题摘及必要信号、04343/03658/04549核心、04534/03828局部反侧、04250科学应用关闭、两精确撤回；另实际独核Anthropic全文/出版字段/正式评分/Books，以及10526/19305/04169完整v1题摘两恢复一关闭。FIRST不替代DAY。

DAY实际检查14源有限查询/分页停止、89完整v1题摘与4官方核心（93完整筛选全部准入层）、14范围外题名，27 arXiv必要定点核心+Anthropic1及两撤回状态；原有明确关闭按机制组合/综述/应用/归因分层核，未变化root核心校准复用。独审发现04250范围、Anthropic三实际出版字段、三个含糊题名、03918措辞，均已窄修；合法show=250月表本日定点重试CL/CV仍真实404，不扩月队列。正式候选1/1深入证据和仅报告处置验收通过，实际比对Ch66/72长期责任边界，无新Book改动或POST待办。未授作者其余17核心全篇独验、所有定理/附录、实现/复现或68项日期通过；实际段落、样本与未检查范围见[独立日级验收](../_sources/daily-20250905/INDEPENDENT_DAY_REVIEW.md)。

DAY同步完成后，本日报V3格式校验通过；六部分和全部本地引用可解析。本日限定diff检查无空白问题；因文件未跟踪，另对README及独核记录逐一作no-index空白检查，均无诊断。机器结果不能替代独立语义验收；无stage/commit/push、无共享文件写入。
