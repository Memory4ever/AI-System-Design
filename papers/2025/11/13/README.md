# Daily Research — 2025-11-13

**规范：** V3
**窗口：** 2025-11-12T09:00:00+08:00 ～ 2025-11-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T16:34:41+08:00

## 1. 结论

唯一由官方精确发布字段确定落窗的候选家族是 Project Fetch：人工编程辅助在硬件连接/传感器接入上的收益，不能直接替代自主物理闭环成功。必要标准审阅完成，Ch26具体已有覆盖；日期、准入、必要证据与具体Existing已获非作者独立通过，实际改书0，无需POST。Ohm三项局部回核通过，root实际读取最终六部分后通知收口；普通待办0，本日完成。外部日期/版本/历史目录保留仍不支持正面采用或无遗漏保证。

arXiv首批7项的贡献已获root独立校准，作者必要方法、评价与反侧已读，但首公开链尚未闭合，未计作确定当窗候选。Private-RAG只提出selection/accounting实际接口差额；OutputDrift不采用模型规模因果，Orion不把参数倍数当运行加速。追加12方向准入及3D4D具体范围关闭已获独立通过，不授其日期/Evidence/Books。本次返修保留LoopLLM、OASIS、DLRM三项潜在贡献，合计22个arXiv日期保留家族；另三个晚版信号不反推v1。JAX-Privacy博客核心已作具体贡献关闭，不由July日期代替筛选。

14每日来源均实际进入原源作有限检查，6行已检查、8行受阻不等于14个历史库已恢复。四个arXiv主题查询的92/16/29/25是含跨分类重复、最新API版本和待核公开日期的发现记录，不是当天论文数。有限筛选与查漏收束，确定落窗清单1家族已核；不把宽标题库存变全量关闭/全文队列，也不将外部保留计为审阅完成。

## 2. 来源覆盖

下列检查只针对本窗模型与系统主线。原入口保存于 [raw-web-00](../_sources/daily-20251113/raw-web-00.json)、[raw-web-01](../_sources/daily-20251113/raw-web-01.json)；有限补查于 [raw-web-11](../_sources/daily-20251113/raw-web-11.json) 等本日原始材料。全年或当前目录不能证明历史无删除。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research、11/12 GPT-5.1 release/card核心与官方RSS；[RSS](../_sources/daily-20251113/raw-openai-rss.xml)午夜字段不当实际首次公开；定点时间检索见raw-web-31 | 受阻 | 事件必要首公开范围及历史原版card/新版措辞分离未闭合，不能把新版全文静默归本日 |
| SRC-ANTHROPIC | Research原始目录按本窗记录定位Project Fetch及Skills webinar；[raw-anthropic](../_sources/daily-20251113/raw-anthropic.html)发布字段绑定实际核；Project Fetch单项独立通过 | 已检查 | 当前官方目录能恢复的切片，不保证被删除历史项 |
| SRC-GOOGLE-AI | DeepMind Research/Blog、Google Research dated blog与pubs主线切片；Nov12 JAX Privacy线索定点核release，Nov13 science/forest条目未纳本窗；旧Blog page=2重定向当前目录，不计历史第二页 | 受阻 | DeepMind旧分页与Google pubs历史本窗公开字段不能完整恢复；不把当前676条pubs当本日队列 |
| SRC-META-AI | 官方Research返回空文本；有限主线历史补检未恢复原目录 | 受阻 | 缺本窗官方列表/公开字段；搜索受限不能证明0事件 |
| SRC-QWEN | 旧站目录可见最新到Sept23，新qwen.ai/blog空文本，未获得有效历史page2 | 受阻 | 本窗动态历史段未恢复，不据旧目录断言无发布 |
| SRC-DEEPSEEK | 官网及官方[updates原始页](../_sources/daily-20251113/raw-deepseek-updates.html)保留Dec1→Sep29日期边界；未见Nov12保留行后停止 | 已检查 | 仅现存changelog切片；官网news重定向首个API说明，不是历史news覆盖 |
| SRC-MOONSHOT | Kimi Platform Blog实际26个日期条目（链接0–25），窗口附近保留Nov7/Nov6边界；未触发特定模型artifact，未扩GitHub全站 | 已检查 | 现存目录不保证删改历史；无已发现本窗新事件 |
| SRC-TENCENT-HUNYUAN | Research浏览器有限三次失败后，publicList POST pageNum=1,pageSize=20,renderType=0实际取得9个2026 blog；[原返回](../_sources/daily-20251113/raw-hunyuan-p1.json) | 受阻 | blog不是历史Research论文。三次分别timeout/子任务visibility不支持/无visibility timeout；停止重复空路径 |
| SRC-ZAI | Research首20项只到Dec9/10、load more未取得旧段；官方release notes Dec8→Sep30未见本窗保留行 | 受阻 | 历史Research目录段缺失；release notes不能代替论文覆盖 |
| SRC-BYTEDANCE-SEED | GET get_article_list_v2，article_type=2及1，publish_year=2025,count=20,page_token=0/20,order_desc=true，header x-tt-locale:US；p0各18行，p20 blog18/paper20行，未置顶段已到六月及更早停止，不取p40；原type1 p0、两份p20保留pinned/next/has_more | 已检查 | 当前返回的窗口上下界未见Nov12非置顶条目；has_more仍true，不声称全库结束或历史删除不存在。raw-seed-papers-p0实际type2，名称不决定身份 |
| SRC-BAIDU-ERNIE | Blog页1最低Nov21，页2由Nov11/Nov7至June，2/2结束；只浏览日期与主线标题，不追窗外正文 | 已检查 | 现存两页无Nov12保留行，不保证历史未删除 |
| SRC-XIAOMI-MIMO | Paper8个日期Oct21→Jan8，本窗未见；Blog15个无日期标题及More隐藏段 | 受阻 | Blog历史分页/公开时间缺口，不用Paper日期代替Blog覆盖 |
| SRC-MINIMAX | 英文12及中文13日期条目，Dec23→Oct27窗口边界；未见本窗保留行后停止 | 已检查 | 仅现存目录切片；无事件触发Agent Tech Blog深查 |
| SRC-ARXIV | 四主题官方API start0/max100，submittedDate14位查询规范化12位，total92/16/29/25；分别限定CL/LG/DC/AI语言模型、DC/AR/PL/OS/PF系统、CV/RO多模态、IR/MA检索记忆；本月CL列表只取ID07555–08579附近81标题/33未见标题查漏，选7份v1摘要 | 受阻 | submitted不等public；原宽范围误解析28897未分页，lastUpdatedDate被API静默改为submitted不算修订覆盖；缺真实历史公告/当日list。月表ID段不是日公开表，也不授全学科召回 |
| 表外：[JAX Privacy](https://research.google/blog/differentially-private-machine-learning-at-scale-with-jax-privacy/) | Nov12博客核心与July v1.0.0 release对照；一次补读精确tag README，见[返修依据](../_sources/daily-20251113/REPAIR_READY.md) §1 | 已检查 | 博客具体贡献关闭：未建立独立November机制/接口/有效性边界，不是仅以July日期去重；auditing不宣称July已有。无日期恢复待办；不冒充SRC-JAX runtime检查 |
| 表外：[Hazy Research HipKittens](https://hazyresearch.stanford.edu/blog/2025-11-09-hk) | 因2511.08083v1定点读作者说明、原日期Nov11 2025；[原核心](../_sources/daily-20251113/raw-web-18.json) | 受阻 | 原日期timezone/时刻未明，不能由论文批次抹掉可能更早首次公开；不扩作者Blog全库 |
| 补检：[原源身份/日期检索](https://arxiv.org/) | raw-web-29三条历史list/announcement定点检索为空；raw-web-30日list/updates尝试路径失败且语义未确认；raw-web-31三条GPT-5.1/HipKittens时间检索保留实际query | 检索受限 | 不以失败路径或搜索转载授必要日期/缺失证明；停止重复空检索。早期raw-web-04/05缺query恢复，不能作为负覆盖依据 |

按需清单没有明确新评测轮次、正式批次或runtime/protocol发布触发；JAX Privacy是表外隐私artifact，不是SRC-JAX执行语义release。未扫描Weekly来源。窄主题完整query及停止范围见 [校准原记录](../_sources/daily-20251113/FIRST_CALIBRATION_READY.md) 与 [新增方向边界](../_sources/daily-20251113/NARROW_CALIBRATION_READY.md)。

## 3. 候选与判断

仅列有真实官方精确落窗字段的拟入选家族；首公开未确认的arXiv材料列§5，不先算当窗候选。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Project Fetch: Can Claude train a robot dog?](https://www.anthropic.com/research/project-fetch-robot-dog) | 2025-11-13T02:19:00+08:00 | 硬件接入uplift与自主任务未完成并存，要求分开接入/辅助/自主能力验收；1+2+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)的Evaluation ladder及真实机器人结果绑定项；非作者独立核具体论点通过，无需写书 |

## 4. 证据与知识整合

### [Project Fetch: Can Claude train a robot dog?](https://www.anthropic.com/research/project-fetch-robot-dog)

官方Research同一post对象绑定slug与publishedOn=`2025-11-12T18:19:00.000Z`；UTC换算后的BJT时刻落窗，不采用一般schedule或RSS。What were we doing?/Results/Limitations/Footnote3：两组各四人随机分队，单日便利样本，阶段任务从厂商控制器到计算机连接/传感器/人工操作，再到无人工指向的取球。

7/8对6/8是子任务数，不是自主闭环成功率；共同完成任务平均约半耗时，主要优势在连接与sensor access，最终自主取球未完成。阶段一控制器不均且未使用Claude，对照收到实验者连接提示；两队控制程序视频能力不同。定位坐标翻转/并行方案绕行、绿色球草背景混淆和人的速度距离指令近碰撞，均限制模型收益与安全归因。精确模型版本、调用预算/硬件/SLO Not Disclosed；未复现或核artifact实现。不采用未来自主能力预测、普遍两倍加速或生产安全。

Ch26开篇定义proposal与controller权限分离，Evaluation ladder将真实进展、重复成功、扰动恢复和安全分开，真实机器人结果绑定robot/controller/task/initial states/trials/scorer/checkpoint/latency/incidents；少量demo只证feasibility。这些具体正文承载本项采用边界，不因缺Project Fetch名称整合。相邻Ch25/Ch27与owner交接已定点读。非作者已核原文、同对象日期和具体Existing通过，见[独立Notes](../_sources/daily-20251113/INDEPENDENT_REVIEW_NOTES.md) §2；原[单项材料](../_sources/daily-20251113/PROJECT_FETCH_READY.md)保留，不重复审附件。没有实际写入，故无需POST。

## 5. 缺口与下一步

### 普通可执行工作

无。Ohm已实际回核[三项返修](../_sources/daily-20251113/REPAIR_READY.md)通过，见[独立Notes §7](../_sources/daily-20251113/INDEPENDENT_REVIEW_NOTES.md)；root已实际读最终六部分并通知同步完成态。复用已过Project Fetch、追加12项准入、3D4D关闭与有界来源/负侧抽检，不重复附件。无需Books写入或POST；不等待月计数。

### 本窗终态保留项

以下材料与目录限制明确隔离，**不用于正面证据、Books或无遗漏断言**，不是Evidence/Coverage通过；日期含糊不等于没有贡献。每组只按所列定点重开条件恢复。

首批七项：[07555](https://arxiv.org/abs/2511.07555v1)、[07568](https://arxiv.org/abs/2511.07568v1)、[07572](https://arxiv.org/abs/2511.07572v1)、[07581 Orion](https://arxiv.org/abs/2511.07581v1)、[07585](https://arxiv.org/abs/2511.07585v1)、[07637](https://arxiv.org/abs/2511.07637v1)、[07685](https://arxiv.org/abs/2511.07685v1)。贡献已校准、必要证据见 [EVIDENCE_NOTES](../_sources/daily-20251113/EVIDENCE_NOTES.md)，但日期不用于正面采用或Books。Orion保留Submitted=2025-11-10T19:49:55Z、Updated=2025-11-12T01:05:29Z、created=2025-11-12T02:49:07Z、registered=2025-11-12T02:49:08Z、Available=2025-11、OAI datestamp=2025-11-12；这些各有原事件权限，不能合成首公开下界。一般公告规则不能排除本篇非标准公开。

追加日期未定身份：2511.07776v1、07869v1、08083v1、08086v1、08113v1及有界查漏的07689v1、07691v1、07732v1、07772v1、08525v1、08389v1、07931v1。12项准入已独立通过，未授日期/Evidence/Books，完整题摘/身份在校准记录，不扩全文池。HipKittens另有作者Nov11无时区日期，必须先解决家族早公开；各后来版本提交不等本窗公开或重要修订，不能静默采用。3D4D具体graphics/frontend差额的范围关闭已独立通过，不为不影响关闭的日期反复恢复。

返修三项：[LoopLLM 07876v1](https://arxiv.org/abs/2511.07876v1)、[OASIS 08487v1](https://arxiv.org/abs/2511.08487v1)、[DLRM 08568v1](https://arxiv.org/abs/2511.08568v1)。完整题摘分别建立重复解码资源攻击、能力不足混淆安全、embedding cache/prefetch placement潜在贡献，作者拟各2+2+2=6，不按普通应用关闭；但提交字段不能授本窗首公开，不先采用实验数字或请求Books。确切字段、尚待核的方法/反侧及定点重开条件见[返修§2](../_sources/daily-20251113/REPAIR_READY.md)。只有对应v1官方首公开链完全落窗，才进一步必要审阅；不重开整批92。

三个当前晚版：[dynamic safety 07645v2](https://arxiv.org/abs/2511.07645v2)、[policy patch 08484v2](https://arxiv.org/abs/2511.08484v2)、[VideoLLM pruning 08003v2](https://arxiv.org/abs/2511.08003v2)，分别updated于2026-04-01、2026-04-27、2025-12-04。版本事件窗外，当前完整摘要不能反推v1贡献或安全结论；不称v1无价值/无法取得、不评分。定点重开条件为可核历史v1文本与首公开归属链，见[返修§3](../_sources/daily-20251113/REPAIR_READY.md)；若归他日只留真实归属线索。

有限恢复已执行精确v1/部分官方DataCite/OAI、历史定点检索和日list路径尝试；缺的是2025真实历史公告、精确v1的官方实际当日list身份与可对齐的首公开上界。停止当前空路径；只有这组原始证据共同给出完全落窗range，或作者真实精确公告/首公开上下界，才定点重开相应家族。仅DataCite registered或submitted字段不够。上述身份暂不支持确定候选、Books、Coverage通过或无遗漏断言，不是因贡献无价值关闭。

GPT-5.1官方RSS midnight与当前release/card不能解决首公开及历史原版问题；一次原源时间补检/官方openapi窗口commit返回空，不再扩论坛或他日内容。重开需官方精确公告/原card可核版本与该发布事件的真实时间范围，不能用转载或后来release notes补造时刻。14源中Meta/Qwen/Hunyuan/Zai/MiMo、DeepMind/Google历史缺段按§2有限范围隔离，重开需本窗官方历史list或可定位的原源事件，不重扫整月。

### 不属于本窗

JAX Privacy v1.0.0官方July10 release已核身份，不恢复7月报告、不称已审重复或11月新release；Nov12博客另作贡献关闭。11/14已独立fresh启动并保存停点，本次返修未加载其候选；11/15～18未启动。

## 6. 复核

复核者：root（首批准入与最终六部分）；Ohm（本任务独立分工，本日Notes署名Codex，非作者）

结论：通过

root首批8份完整题摘校准的7项准入与sentiment application关闭复用。Ohm实际核Project Fetch的日期/准入/必要证据/具体已有覆盖通过；追加12项准入与3D4D关闭通过；14源逐行有限停止和负侧分层抽检已记于[独立Notes](../_sources/daily-20251113/INDEPENDENT_REVIEW_NOTES.md)。负侧样本包括sentiment、Auto-US、TurkEmbed，不称全量验证；未复现、未重建动态历史库、未核追加12项全文/代码。原日级因三项问题未通过的历史记录保留；Ohm在2026-10-04T16:24:18+08:00实际局部回核（Notes §7）通过，确认博客差额关闭、三份v1潜力/三晚版隔离、Moonshot26与报告同步。root本轮实际读取最终六部分后通知收口，作者据累计独立结果同步完成态，不以机器检查授语义通过。

执行检查：完成态正式日报的`python3 scripts/validate_research.py --report papers/2025/11/13/README.md`实际通过；本日8份Markdown/44个本地引用、直接尾随空白与46份JSON解析通过，限定路径`git diff --check`通过。此前内存完成态试测保留未通过结论时按预期拒绝，仅为历史测试，不替代本次正式检查。未stage、commit、push；本次收口仅写本日报与_sources，Books/shared state/其他日期未写。独立语义通过依据上段实际复核，不是validator结果。
