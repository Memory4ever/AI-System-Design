# Daily Research — 2025-10-04

**规范：** V3
**窗口：** 2025-10-03T09:00:00+08:00 ～ 2025-10-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T08:39:51+08:00

## 1. 结论

十四每日源按本窗主题有限检查。四个收窄arXiv主题去重54身份，相关标题补检5个精确v1，实际完整题摘59；8项贡献关闭、51项首次公开日期未核实隔离，不等当天59篇新论文。18必要安全/设计反侧核心与3准入消歧共21份有限阅读，另读Anthropic完整官方核心和OpenAI安全release短核心；不等全文/附件全审、独立评价或正面Evidence完成。

正式候选1：Anthropic网络防御研究说明，Curie FIRST已确认落窗与准入，评分2+2+2=6。其受测证据区分单次/$2与30次能力覆盖，补丁自评的参考等价也可能产生假阴性；训练机制未披露，不能由结果推断。必要安全评价核心深入完成，Books仅报告：这是Sonnet4.5版本实验，长期预算/候选覆盖与oracle边界已由实际Ch66正文承载，无窄长期差额。Books提案0、实际写入0；Curie DAY及作者两窄同步已实际回核通过，本次仅依据独立结论同步完成态。

作者扫描、题摘与必要有限core已收束，Curie已实际完成DAY与两项变化回核；据其独立结论同步完成态，不等待其他日期打包。[筛选](../_sources/daily-20251004/SCREENING.md)、[必要核心边界](../_sources/daily-20251004/CORE_BOUNDARIES.md)、[FIRST请求](../_sources/daily-20251004/FIRST_CALIBRATION.md)保留可复查依据。

## 2. 来源覆盖

原请求/真实执行时间及范围见本日[acquire](../_sources/daily-20251004/acquire.py)和各对应receipt。下表有限原件只覆盖声明范围；历史缺段、日期含糊和访问失败均不解释为无事件。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research首查403；searchA/B限定本窗机构主题及已知Oct3发布标题，官方ChatGPT release Oct3安全核心已实际读；Academy培训/企业Auto配置关闭贡献 | 受阻 | 原Research历史列表未恢复，安全release只有Oct3日期没有精确timezone/time；不授零事件 |
| SRC-ANTHROPIC | Research原页与own PublicationList bundle，本地SeeMore对应Flight171只核本窗边界：9/15→10/03 18:31 UTC→10/06 11:10 UTC；完整cyber defenders官方core | 已检查 | 无本窗已知可执行来源修补；首批/证据非作者校准待办不等历史缺口 |
| SRC-GOOGLE-AI | DeepMind原Research、实际publication path /page/2/（?page=2被忽略不作覆盖），页2首10/30→9/29；独立Google pubs search=language model/category=2025第1页15/37，年份精度停止；Blog实际2025/10页1、?page=2末页2/2，10/7→10/2→10/1相关标题，本窗无可确认相关原发布 | 受阻 | pubs年度元数据没有Oct3首次公开批次，不把37年库存逐项审，也不以Blog代pubs历史 |
| SRC-META-AI | 原Research200但为当前Muse动态页壳；本窗official域主题补检及具体相关标题恢复止于searchA/B | 受阻 | 未恢复Oct3官方历史Research清单；搜索零相关原件不等无事件 |
| SRC-QWEN | 原Blog五项9/23→7/24；实际meta refresh指qwen.ai/research，own新站请求200为动态应用壳，有限原路与搜索到此停止 | 受阻 | 新站当前应用壳没有Oct3历史列表；不把旧Blog9/23尾当整个品牌末页 |
| SRC-DEEPSEEK | 原主页→/news/及own bundle，实际31条Research本地数组/ViewAll slice(0,10)；本窗邻界10/21→5/14，News9/29→12/1 | 已检查 | 仅这条官方Research/News列表，不授全网召回 |
| SRC-MOONSHOT | Kimi Blog26项，邻界9/16→11/6；Moonshot org first100只核官方身份，不将repos作论文池 | 已检查 | 仅可观察Blog历史边界 |
| SRC-TENCENT-HUNYUAN | 官方Research首查动态壳，有限实际browser打开30s超时；own官方publicList pageNum1/pageSize20/renderType0，返回total9/list9，最早displayPublishTime为2026/02，stop1/1 | 受阻 | 当前全部9项不含2025历史，不以接口成功/浏览器失败证明本窗无研究 |
| SRC-ZAI | 首Research→own LoadMore bundle及?page=2，18累积项，页面没有更多且hasMore=false；最早2025/12/07，stop2/2 | 受阻 | 现目录没有10月历史段，不拿首屏15条作末页 |
| SRC-BYTEDANCE-SEED | 原Research/Papers→ownbundle API：type1加US头，2025升序tokens0/20/40/60/80，19/15/19/19/13=85可见/total94、最后has_more=false；邻界9/22→10/9。type2无US头tokens0/20/40，17/18/6=41可见/total49、末页false，邻界9/9→10/23 | 已检查 | 后端total与语言可见数不同，未声称94/49全题摘；真实数组与本窗邻界已核，不把年度列表变队列 |
| SRC-BAIDU-ERNIE | 原中文Blog与实际path /page/2/，页2六项含10/16→9/12，stop2/2；旧?page=2忽略不算第二页 | 已检查 | 仅技术Blog可观察历史范围 |
| SRC-XIAOMI-MIMO | 原Paper/Blog及own6159 Paperbundle，实际8日期：2025/05/12、06/04、09/19、10/21，2026/01/08、02/03、03/13、06/29；More是slice本地展开不是历史分页 | 已检查 | 仅这8份Paper日期导航，不授不存在其他发布 |
| SRC-MINIMAX | en12可见到10/27，中文13到1/15；独立Agent Tech Blog目前只2026/05/13；本窗official域与相关标题有限补检，hosted用户space排除机构权威 | 受阻 | Agent历史段与两Blog之外的Oct3原发布未恢复；不能拿当前首页/用户space当本窗零研究 |
| SRC-ARXIV | 4主题start0/max40全部返回，54去重；官方CL/CV/DC/PL/IR各首25只相关标题补检5 exact-v1，停止范围见SCREENING；没有整类逐项队列 | 受阻 | 51潜力身份没有官方历史首次公开时刻/完全落窗bounds；submitted/API published不替代公告 |
| 补检：[官方域与标题恢复](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | searchA/B限定本窗机构主题与相关标题，并恢复所链官方release；只作发现/身份恢复，不沿社区结果建立证据 | 检索受限 | 搜索不证明全网无遗漏 |

每日14源之外未触发常规按需/每周扫描。官方cyber正文自足支持其发布事实与限制，不把引用的benchmark目录扩成新扫描队列。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Building AI for cyber defenders](https://www.anthropic.com/research/building-ai-cyber-defenders) | 2025-10-04T02:31:00+08:00 | 单次预算可能低估重复覆盖→新增受测试次/成本与patch参考等价假阴性证据→重新审视安全能力曲线及oracle；2+2+2=6 | 深入完成 | 仅报告：Sonnet4.5版本上下文；长期边界已由PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)承载，无新差额 |

正式候选1，51论文仍仅日期潜力，不评分或采用。没有将题摘59当证据审阅完成59。8项明确关闭有实际AB与具体理由，含糊或局部/负面潜力保留；FIRST与DAY实际范围见§6。

## 4. 证据与知识整合

### [Building AI for cyber defenders](https://www.anthropic.com/research/building-ai-cyber-defenders)

Curie FIRST已校准，DAY已实际核官方core及Books正文，R-SYNC同步限定结论与R-MOON已通过变化回核。own Research `publishedOn=2025-10-03T18:31:00.000Z`即BJT10/04 02:31完全落窗；[当前原正文](../_sources/daily-20251004/anthropic-cyber.raw)的Cybench、CyberGym、Further research into patching及其余完整core已读。

Cybench评测37/40问题，3项因implementation difficulties排除，k=1/10/30为至少一次成功覆盖；Sonnet4.5 k10为76.5%、3.7为35.9%，不把不同代际差额归因未披露训练机制。CyberGym已知vulnerability的$2单次为28.9%，30次为66.7%/约$45任务；Opus4.1单次没有相同$2约束，不能签等成本排名。新漏洞发现5%/超过33%项目又是不同事件，不与已知漏洞复现成功合并。

补丁让Claude评自己的输出与人类参考的语义等价，15%是这个judge事件；多个有效修法可引发假阴性，人工核的是highest-scoring子样本而非全patch。没有独立验证全部修复/功能保持，更没有生产安全概率。伙伴反馈不是受控独立实验；风险监测提到组织级汇总，不披露算法。费用字段只是LLM API，硬件、precision、并发、完整工具/人工和端到端SLO未披露，不用38分钟单例推吞吐。

实际owner `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：1574–1609的single→candidate coverage→selector链，1973–2007攻击预算及Security Agent Cost-Success-Refusal Curve，399–412合法替代路径/false reject，708–725 oracle分责及多种有效patch已承载这些长期判断。Ch65收尾是共享调度政策，不接管能力评价；Ch67开篇只持续测已有信号，不定义质量。实际Ch72开篇/97–116信任边界与漏洞信息→真实运行激活，Ch71/73邻接不把离线结果授部署权威。Curie已实际核对应正文并确认无窄长期差额；本材料最终仅报告，不把版本数字再写成长期知识，不改共享Books。

### 日期隔离的必要安全/反侧阅读

[21份有限核心笔记](../_sources/daily-20251004/CORE_BOUNDARIES.md)保留VeriGuard运行参数/策略验证边界、CS-RLHF与KG-MASD证明假设争议、FocusAgent低ASR低TSR、Abstain/PlanVerification条件分母、TRACE/SurveyBench/SEER/PLSemantics测量混杂等。不因反证删除潜力或按高分模板扩大附件；每个命题读到必要支持/反侧就停。它们没有first-public准入，不形成正面Evidence或Books。

OpenAI Oct3安全release短core明确训练Instant识别/回应mental/emotional distress并减少急性危机reroute，但only-date身份未准入；“同等表现/更快”未披露对照/指标。此处保留实际行为变化与采用限制，不作心理/医疗建议或能力保证。

## 5. 缺口与下一步

历史窄修已完成：Curie于2026-10-05T07:29:19+08:00实际回核通过R-SYNC正式家族/限定证据/Books仅报告同步及R-MOON 26条修正。FIRST与DAY其余实际检查范围复用，未重抓59题摘/21核心；Books无窄提案、实际写入0，无改书待办。此处不是待办或作者自审。

作者常规扫描/题摘/有限核心剩余0，独立复核已通过，无可执行研究或Books写入待办。以下保留项经独立复核作为本窗终态保留项存在，不用于正面证据、Books、无遗漏断言或性能/安全保证；完成态不授这些保留项Evidence或Coverage通过：

- 51论文具名身份在SCREENING。缺真实官方首次公开公告或完全落窗bounds；仅同身份原历史公告/可靠真实发布记录到达才重开日期准入及受影响证据/Books，不遍历月/年全部条目。v1题摘/HTML页日期与submitted字段不足。
- OpenAI Oct3安全release缺公开时刻与时区。补同一release官方带时区记录后定点重开；不把整体GPT5旧模型发布身份替代当前变更事件。
- OpenAI/Meta/Qwen历史Research、Google pubs Oct3公开批次、Hunyuan2025历史段、ZAI10月和MiniMax Agent历史段：当前原入口与有限恢复已处理到表内停止。仅历史目录/对应官方原公告到达才重开对应源/窗，不用当前年度/动态首页证明零事件，不将语言隐藏total扩成全库存审阅。

这些缺口与8项已明确贡献关闭不同，后者不为不影响处置的日期新增请求。窗外明确日期标题只作归属线索，不扩本窗，不把未来日期正文纳入本日材料。

## 6. 复核

复核者：Curie（非作者Huygens；FIRST与DAY、两窄同步回核通过）

结论：通过

实际读回[Curie FIRST](../_sources/daily-20251004/FIRST_INDEPENDENT_REVIEW.md)与[DAY](../_sources/daily-20251004/FINAL_INDEPENDENT_REVIEW.md)开头最新结论：2026-10-05T07:29:19+08:00通过。其实际核Anthropic落窗身份/全文核心、14有限源、18必要反侧与3消歧、两官方核心及Ch66/相关交接；R-SYNC/R-MOON两项作者同步已实际回核通过。FIRST四分层关闭加DAY Financial Risk核心合计5/8关闭样本，其余3关闭和51非安全潜力未全库存重读，不称全量验证。Books提案/实际写入均0，无写后待办。此次只同步完成态与终态隔离接口，不重读已通过原件；机器检查不替代上述语义验收。
