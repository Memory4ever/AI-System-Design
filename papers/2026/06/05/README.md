# Daily Research — 2026-06-05

**规范：** V3
**窗口：** 2026-06-04T09:00:00+08:00 ～ 2026-06-05T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T08:33:07+08:00

## 1. 结论

本轮只有 **1 个确定落窗候选家族**：Kimi Code 0.10.0/0.10.1 的未来目标队列、完成晋升与 fork 意图继承边界。6分候选因具体执行/兼容变化及知识缺口，已深入审阅必要受影响代码；Ch81 两段已真实写入并获 root 非作者必要源→owner和实际写后通过，形成 **1 项真实整合（1深入、1I）**。这不是整份 release 的安全、生产可靠性或测试复现保证。

OpenAI Dreaming/Endava 两条本窗 RSS 事件原时钟已取回，核心具体贡献筛选与 root 负侧校准均关闭，不凑候选。旧71 arXiv身份的 first-public 上界不能由 DataCite created/updated 或最早正常公告 schedule 证明；全部具名 DateHold。Google Agentic RAG与 SIRA v2 两个新目录cue也只有相交日历/提交时刻，与旧71不重合，共 **73 个终态日期保留**，不计当窗候选、评分或本轮 Evidence/Books 正面通过。旧706宽池不是逐项全文队列，旧72/67E/4Only/1I不继承；保留有效证据与旧 LexicalDensity 正文但不计此次I。

14来源已按本日实际有限入口处理到明确停止/隔离终态，不声明全网或机构无遗漏。扫描、筛选、必要审阅、修改及非作者最终日Gate均已完成，普通待办为0；root非作者日级安全终态复核通过。详细唯一记录：[恢复与证据 packet](../_sources/daily-20260605/V3_RECOVERY_BLOCKERS.md)。

## 2. 来源覆盖

只处理本窗的大模型架构、训练/后训练、推理资源、平台评价/安全、Agent执行状态与多模态主线；不扫Weekly，不将目录全部领域条目变成候选。下表的“已检查”限实际原入口与停止范围；受阻部分已隔离，不支持零命中或全来源无漏项。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方[RSS](https://openai.com/news/rss.xml)实际1240条按窗口过滤，2条原pubDate与两核心已读；Dreaming=June04 09UTC、Endava=12UTC | 已检查 | 两项前分母关闭经root校准；不展开全部图表或客户外链，不把后来update当本窗事件 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)首屏及原HTML173个publishedOn；目标前后为Navigator June03 18UTC、news10:55UTC、chemist June05 20:57UTC；本窗字段无条目 | 已检查 | 结果限官方目录字段；chemist明确窗外且science范围暂缓，不沿旧calendar归属 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) curated latest/年级publication；Google Research GenerativeAI第一页读至June03→May28，NLP至June05 AgenticRAG→May19，MachineIntelligence首12至August21；分页click错误/原HTMLtimeout，两条目标官方域查询 | 受阻 | AgenticRAG core实际读但June05日历交窗、两次原HTML0bytes缺时钟；MachineIntelligence/DeepMind目标历史主题批次不完整，有限stop不扩55页 |
| SRC-META-AI | Blog入口timeout；[publication page1](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)实际成功至June05 SIRA→May27→May26后混旧库存；SIRA官方完整摘要、exact-v2完整摘要/版本史已读，CDN PDF一次cachemiss | 已检查 | SIRA日期/官方PDF版本身份隔离；不能沿旧“非重要修订”去重，目录日历不证明公开时刻，不读全部旧库存 |
| SRC-QWEN | qwenlm.github.io redirect/qwen.ai壳→只读page_config：news17最新2025Apr28、Research60最新2025Dec23；本日有限官方域June04/05查询仅chat分享噪声 | 受阻 | 2026目标原始研究目录缺口；旧77配置不证明本窗零材料，不扩旧正文 |
| SRC-DEEPSEEK | 官方[研究与动态](https://www.deepseek.com/news/)研究June24→Feb25、动态Sept10→Apr24，停止目标前 | 已检查 | 动态“查看全部”局限保留；只证明可见目录，不作全仓commit审计 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)全部可见27条最新2025Nov07；官方GitHub exact0.10.0/0.10.1 release API时钟/flags与393/383/399/443必要patch | 已检查 | Kimi一家族深入；旧Blog不代表2026所有模型事件，代码阅读不是运行测试或生产SLO |
| SRC-TENCENT-HUNYUAN | Research壳→fresh只读POST publicList pageNum1/pageSize100/renderType0：code0/totalNum9/list9全publicAt/display/published字段，publicAt July06→April30夹住目标 | 已检查 | 无本窗publicAt条目仅限该9条目录；display不是publicAt，字段不自动证明论文first-public |
| SRC-ZAI | 官方Research全部日期目录前14，June16→May20后停止 | 已检查 | 可见日历片段无本窗条目，不制造论文公开时刻，不读旧全文 |
| SRC-BYTEDANCE-SEED | [public_papers](https://seed.bytedance.com/en/public_papers) page1/13首20，June04 electron-dynamics范围暂缓、June03 MetaPoint在本窗日历之前、May29停止 | 已检查 | 不拿目录日历证明linked paper first-public，不扩242条/science正文 |
| SRC-BAIDU-ERNIE | 官方[中文Blog](https://ernie.baidu.com/blog/zh/) page1/2最新May09→April30→更早，已到目标前不翻旧page2 | 已检查 | 可见目录无本窗条目，不声称全部仓库release已扫 |
| SRC-XIAOMI-MIMO | 官方Paper8日期June29→March13、Blog15无日期；fresh4752.2908c99e.js 688092bytes，EN/ZH Code June10、UltraSpeed June08、pipeline May30 | 受阻 | undated Blog不能证零；需目标发布clock/原目录快照，不读15窗外全文 |
| SRC-MINIMAX | 本日EN/中文Blog June09→June01→May停止；AgentTechBlog15行壳，所链llms.txt当前48行使用目录已读、无历史dated Blog | 受阻 | 主目录无可见本窗条目；Agent历史分支缺口独立隔离，不以壳/index作零命中，不读48用户指南 |
| SRC-ARXIV | 旧owner receipt68items显式DataCitecreated口径无效；source/submission receipts不存在。历史day短路404，正确2026-06月2718无dayheaders，advanced公告仅year/month；exact05241v1原页和有限目标公告搜索 | 受阻 | 71具名first-public上界未证；各主题本批原始公开目录不可恢复，不扩706宽列表/整月2718/全部原文，不把404作空批次 |

## 3. 候选与判断

只列经具体贡献准入和原始公开时钟确认的唯一家族。首批准入、全部拟入选的必要源→actual owner、实际窄写均经root非作者通过；不是日期保留项的全证据验收。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.10.0 / 0.10.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.10.0) | 2026-06-04T21:46:30+08:00 | 未来objective与active goal分开，complete-clear/turn-end/idle晋升及fork丢future intent改变连续任务生命周期；2+2+2=6；同家族0.10.1事件另于2026-06-05T01:35:34+08:00，两事件合并计一家族 | 深入完成 | 整合：AGENT-WORKFLOW — [Ch81 Task State Alignment](../../../../books/part-07-agent/81-workflow.md#task-state-alignment-是每次-dispatch-的前置条件)现118/120两段，root实际写后PASS；非whole-release覆盖 |

## 4. 证据与知识整合

### [Kimi Code 0.10.0 / 0.10.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.10.0)

两exact release API id334363633/334501678，published_at分别2026-06-04T13:46:30Z与17:35:34Z，draft/prerelease=false；updated_at为13:50:09Z/17:39:56Z，不代公开。两个事件同一家族；root亦独立核其API原字段。

393 exact beb12ac 的event handler/goal-store/session-store及goal beforeSend路径实际必要读：TUI upcoming-goals.json保存future objective，active goal另持；completion通知、cleared goal snapshot、turn-end、idle且queued-message空才尝试晋升，blocked/paused/cancel不等complete。创建active goal后才beforeSend移队列项，失败可能留下active而未dispatch；queue mutation锁仅进程内，direct writeFile非事务。fork丢custom.goal与future queue，复制history不自动继承future intent。跨进程/crash一致性验收和新branch重新受理是工程推断，不是作者已证明exactly-once。

383 exact15d71b5的reload/controller/core/session/harness必要patch：active turn拒绝reload，关闭ready agents/cron、flush metadata/MCP/log后resume、TUI撤销旧handlers并重订阅；runtimeOverride保留，不保证任意live热更新/外部effect恢复。399 exact232ed87的managed credential/ref、auth/provider/refresh及toolkit必要函数：normalized oauthHost+baseUrl决定slot，manager key绑定host，login/provision/status/logout/refresh消费相同ref；不证明endpoint可信、全部custom refs安全或hash无碰撞。443 exact15a4c64保host receiver修正TUIgoal crash，相关回归测试只读未运行。后三项为受影响版本/风险事实，不借成熟凭证或reload原则额外增分/新增正文。

当前Ch81已有activation/head与dispatch前stage/evidence/memory/executor对齐，但没有future intent queue、完成晋升及fork继承选择的具体取舍。root亲读393必要源→actual owner并授权Task State Alignment尾→相对指代前窄锁；两段已实际写入现118/120（唯一SF-KIMI-CODE-0-10），root再实际读前后衔接通过。低风险single-session可保轻量队列，高风险effects仍服从authority/checkpoint/effect ledger；不宣称测试复现、全release安全或生产可靠性。

Dreaming/Endava原RSS时钟与核心关闭依据、Google/SIRA日期保留线索、71旧材料具名身份及旧必要证据全文，集中保存于[唯一packet](../_sources/daily-20260605/V3_RECOVERY_BLOCKERS.md)。旧§3/§4已明确标legacy，不再并列为当前positive。2606.06203旧LexicalDensity正文及其他有效来源不删除，但本轮未验收其日期/采用，不计新I。

## 5. 缺口与下一步

普通可执行待办为0：扫描、筛选、必要审阅、修改及root非作者最终日Gate均已完成。以下已穷尽当前有界原始入口，均为本窗终态保留项，不支持正面证据、Books或无遗漏断言，也不用于候选、评分或性能/安全保证；取得所列具体替代材料才定点重开。

- **73具名DateHold**：[packet身份表](../_sources/daily-20260605/V3_RECOVERY_BLOCKERS.md#73具名终态日期保留非候选evidencebooks通过)。71旧exact-v1逐身份只请求一次原始当批公告/带时区作者公开正文receipt/可信原快照，给first-public上界，不能由Created/Updated/最早schedule补造08–09。Google AgenticRAG需原June05发布timezone/clock；SIRA2605.06647v2另需其公开receipt与官方PDF精确版本身份。后两项与71disjoint，不继承旧“非重要修订”判断。原必要证据只保留，不是73篇全文/Evidence通过。
- **五类历史覆盖缺口**：Google目标主题/DeepMind历史批次、Qwen2026目录、MiMo dated Blog、MiniMax Agent历史Blog、arXiv目标主题原公开批次。上表已给实际停止/失败，不将精选、旧配置、undated routes、空壳或月级目录当本窗零命中。原目标primary dated feed或可靠公开receipt到达后，只重开对应来源/身份，不扩其他日期或全年。
- **旧采用链本轮未验收**：原1I/67E/4Only不计当前状态，但保留有效研究与正文。日期恢复后再定点核相应必要源和actual owner，不以本轮DateHold一刀删除旧Books。

窗外线索，不属本窗、不阻塞本日：Anthropicchemist实际publishedOn=2026-06-05T20:57:00Z（June06 04:57BJT），只记原时钟与暂缓science范围；其余窗外目录条目不当后日已审候选。

## 6. 复核

复核者：root（非作者）。
结论：通过

root实际通读当前正式六部分、唯一packet最终stop/两新DateHold与73具名表（73rows：72unique arXiv含SIRAv2+Google，无重复），核14到期源与五具体历史缺口、1家族双release正确落窗/6分深入及actual Ch81实际写后。独立release API时钟/flags、393必要source→actual owner和两段前后衔接PASS；Dreaming官方core39–69/timefreshness257–262/scalable301–305与actual Ch77:273–289、Endavacore43–111负侧复用有效非作者核。旧72/67E与全Evidence标签已隔离legacy，有效正文保留。普通0、日级安全终态通过；73日期/目录保留不是Evidence通过或无漏项保证。代码测试只读，不冒充实际运行。

当前V3和三文件scoped diff-check已实际通过；机械校验只证明可判定字段一致，不替代语义验收。未stage、commit或push；未改月索引/LEARNING_STATE，共享Books只写获准两段。
