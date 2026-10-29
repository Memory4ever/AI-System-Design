# Daily Research — 2026-06-04

**规范：** V3
**窗口：** 2026-06-03T09:00:00+08:00 ～ 2026-06-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T08:08:10+08:00

## 1. 结论

本轮恢复两个确定落窗家族：Kimi Code 0.9.0 的执行/协议兼容边界，以及 Anthropic LLM ATT&CK Navigator 的优先级评分与自主编排评价盲区。两家族均为 6 分，必要受影响内容已深入审阅，root 非作者已通过必要源→实际 owner 与窄段提案；Ch81 和 Ch72 各两段已实际写入并经 root 非作者写后通过，形成 **2 项真实整合**。候选为 **2 家族、2 深入完成、2I**，最终日级安全终态复核通过。

旧 575 条宽发现列表不是本轮逐项全文队列；旧 64 个 arXiv 入选身份的 first-public 上界不能由 DataCite created/updated 或正常最早公告 schedule 证明，全部转为具名 DateHold。Seed MetaPoint 与该集合不重合，共 **65 个终态日期保留**，不计确定候选、不评分、不计 Evidence/Books 正面通过。旧 EvalStop 正文与其他有效研究证据保留，但旧 1I/55E/9Only 和旧 Complete 不作为此次采用验收。

OpenAI 当窗五条原始 RSS 事件均已按核心说明关闭，不以机构泛公告或科学应用凑候选。Dreaming 实际 RSS 为 06/04 17:00 BJT，属窗外，仅给 06/05 恢复线索。普通可执行工作为0，独立整日Gate已通过；外部日期和目录限制已单独隔离。唯一详细 packet：[当前恢复与保留证据](../_sources/daily-20260604/V3_RECOVERY_BLOCKERS.md)。

## 2. 来源覆盖

本轮按大模型架构、训练/后训练、推理资源、平台评价/安全、Agent 状态/执行、多模态主线限定入口；不扫描 Weekly 组，不以本机构全部研究作本项目范围。下表记录实际有限停止，不声明互联网或机构全站零遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 [RSS](https://openai.com/news/rss.xml) 实际 1240 记录按窗过滤；五条本窗原始时钟及对应核心说明已读，Dreaming另核为窗外 ；已检查：五条前分母关闭，无入选 | 已检查 | 页面后来 September update 不当六月事件；不外推全部附件已审 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 首屏/SeeMore；公开 HTML 内嵌 publishedOn 定位两条 June03 记录，读 research 与 news 核心，合并同一家族 ；已检查：Navigator 1 家族深入必要范围 | 已检查 | 厂商选定调查样本、潜在 impact 与 detector drift；非自然发生率/部署有效性证明 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) 的 curated latest；Google Research pubs年级目录及 Generative AI/NLP 标签第一页，分别读至 June03→May28、June05→May19；Machine Intelligence首12未到本窗，分页link web错误/direct原页timeout；有限官方域 June03/04查询 ；检索受限：洪水框架为暂缓科学应用，CVPR活动日程非first-public，不变候选 | 受阻 | DeepMind精选与Google年级publication不能证明本窗所有主题公开；需带公开时钟的目标目录/primary event恢复，不扩55页或大会全部附件 |
| SRC-META-AI | Research原路0行；Blog page1/2实际标题元数据至March及更早；从导航恢复 [publication page1](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)，2026前缀 June05→May27后进入旧库存；日期限定官方域补检 ；已检查：可见本窗切片无新增事件，不读窗外全文 | 已检查 | 旧库存乱序和精选目录限制，不声称全站无遗漏；首次timeout后page1已成功，不能仍报不可访问 |
| SRC-QWEN | 旧 qwenlm.github.io redirect 与 qwen.ai壳；公开969.js恢复只读page_config，news.news-list17最大2025/04/28、research.research-list60最大2025/12/23；两条配置实际无目标日期，限定官方域查询无可用原事件 ；检索受限：当前可恢复配置止于旧年 | 受阻 | 2026本窗原始研究/发布目录缺口终态隔离；旧77配置不证明零材料，不读旧全文 |
| SRC-DEEPSEEK | 官方首页→[研究与动态](https://www.deepseek.com/news/)；研究索引 June24→Feb25、动态Sept10→Apr24，停止目标前 ；已检查：可见研究/发布无本窗事件 | 已检查 | 查看全部为动态按钮；结果限定公开可见目录，不作全仓所有commit审计 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog) 当前显式目录到2025/11；官方 GitHub exact0.9 release API与所链368/338/380/365必要patch，确认原published_at ；已检查：0.9一家族深入受影响边界 | 已检查 | 平台Blog旧保留列表不证明2026全部模型事件；patch检查非实跑/跨client生产互操作保证 |
| SRC-TENCENT-HUNYUAN | Research壳后，直接只读POST publicList pageNum1/pageSize100/renderType0；code0/totalNum9/list9全项publicAt与displayPublishTime/publishedAt字段核，actualpublicAt Jul06与Apr30夹住本窗 ；已检查：当前目录9条无本窗publicAt | 已检查 | displayPublishTime不是publicAt，Hy3preview July publicAt/April display分开；目录字段不自动证明链接论文first-public |
| SRC-ZAI | 官方 Research全部日期目录前14，June16→May20后停止 ；已检查：目标日历片段无条目 | 已检查 | 不以目录日历制造论文首次公开时刻；不读更早全文 |
| SRC-BYTEDANCE-SEED | Research精选及 [public_papers](https://seed.bytedance.com/en/public_papers)首20，June04 electron-dynamics暂缓AIforScience、June03 MetaPoint、May29停止；只定点核MetaPoint exact身份 ；已检查：MetaPoint日期保留，非确定候选 | 已检查 | 目录Jun03日历精度、PublishDate占位与v1submission不能证明实际公开上界；不扫描其他日期论文 |
| SRC-BAIDU-ERNIE | 官方 [中文Blog](https://ernie.baidu.com/blog/zh/) page1（共2页），最新May09→Apr30→更早；已到目标前不翻page2旧年 ；已检查：可见最新目录无本窗条目 | 已检查 | 结果限官方Blog可见目录，不声称全部仓库release已扫 |
| SRC-XIAOMI-MIMO | 官方Paper8日期June29→March13；Blog15无日期。公开4752.2908c99e.js routes frontmatter EN/ZH实际CodeJune10、UltraSpeedJune08、pipelineMay30，无June03/04；限定官方域查询无原事件 ；检索受限：有限恢复无确定本窗事件 | 受阻 | undated custom routes不能证零，需目标发布clock/原目录快照；不读15窗外全文 |
| SRC-MINIMAX | 英/中文Blog actualJune09→June01→May；Agent Tech Blog只Navigation/TechBlog壳，未获取dated entries ；已检查主研究目录；Agent历史目录检索受限 | 受阻 | 主目录无本窗记录；Agent分支历史原始日期目录缺口独立隔离，不用空壳证明无事件 |
| SRC-ARXIV | 旧owner receipt41显式Created口径无效，source/submission receipts零字节；官方历史day路404，正确2026-06月2718无dayheaders，advanced公告只year/month；exact04145/04101原页及两次目标公告搜索 ；受阻：日期终态隔离，不是64 Evidence通过或零命中 | 受阻 | 64具名first-public上界未证；各主题历史公开批次无法恢复，不扩575列表、整月2718或无差别原文 |

## 3. 候选与判断

只列确定落窗且通过具体贡献筛选的两个唯一家族；root非作者已通过必要源→owner与两处窄段提案，实际写后亦经root独立检查通过，不能以日期保留充当候选。重要兼容变化与确认知识缺口触发深入受影响范围，不因6分停于release摘要。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.9.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.9.0) | 2026-06-03T22:01:42+08:00  | 已闭合history snapshot的ephemeral旁路、deny-all与lazy persisted-child恢复改变主turn/child生命周期取舍；2+2+2=6 | 深入完成 | 整合：实际两段经root非作者写后通过；AGENT-WORKFLOW — [Ch81 Resume](../../../../books/part-07-agent/81-workflow.md#resume-的语义必须比有-checkpoint更具体)，ACP分层由AGENT-MCP正文具体覆盖，不称whole-release已覆盖 |
| [LLM ATT&CK Navigator / ARiES](https://www.anthropic.com/research/attack-navigator) | 2026-06-04T02:00:00+08:00 | 优先级加法保部分enablement信号≠success probability、technique频次无法表达自主编排这一评价盲区；2+2+2=6 | 深入完成 | 整合：实际两段经root非作者写后通过；PLATFORM-SECURITY — [Ch72 Security Agent](../../../../books/part-06-ai-infrastructure/72-security.md#security-agent-的评估必须绑定-tool-trace-与-deterministic-predicate) |

## 4. 证据与知识整合

### [Kimi Code 0.9.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.9.0)

官方release API id333758230的published_at=2026-06-03T14:01:42Z，draft/prerelease=false，非updated_at代公开。release核心全读；exact必要commits与代码位置见唯一packet。

338把已投影、闭合tool exchange的history复制给无持久元数据/内存record的旁路child，继承tool definitions以cache reuse，但权限policy明确deny-all。prompt上的“不要工具”不是唯一边界；复制的context不是live parent history，也不证明事实成功。380只先resume main，child首次lookup才replay，promise去重、parent-chain cycle检查与记录重放失败在对应catch删除pending entry是受限生命周期机制；parent resume的await在try之外，不声称所有parent-chain失败都获相同清理。不证明全部已ready或外部effect exactly-once。365的正整数rounds/provider token-key/cap是兼容修正，不提供工具/端到端费用硬保证。

368 ACP docs及auth/cancel/approval局部代码实际读：stdio JSONRPC/log stderr；mode/model/thinking配置、history replay/load与resume跳过replay是不同表面，unsupported capabilities不宣称全协议。requestPermission失败拒绝；cancel notification未知session/错误只log，不能当取消完成receipt。Ch83:94–105实际覆盖adapter/runtime/policy分责；Ch81原revision/review与resume性质没有ephemeral问答branch和durable child的具体取舍。root通过窄gap后，已实际在Resume末→Logical Plan前写两段（当前1150/1152，唯一SF-KIMI-CODE-0-9），root非作者实际写后通过。代码审查不是测试运行、生产SLO、跨client完整互操作或撤销已发生effect。

### [LLM ATT&CK Navigator / ARiES](https://www.anthropic.com/research/attack-navigator)

官方Research内嵌publishedOn=2026-06-03T18:00:00.000Z，news=10:55Z；同报告去重一家族，时间均落窗。核心、dataset、score、novelty与限制实际必要读完。ARiES是选择调查优先级的加法分数，不是攻击成功预测；技术类型/数量对自主编排的表达也有限。确切新增是两类测量对象分账，不采用其未经校准的score为生产风险或模型因果uplift。

调查仅含832个有足够细节的banned accounts；score使用厂商classifier、Claude技能评分及实际/潜在impact，80%为ClaudeCode，不是自然流量人口。去掉skill后的r=.28和technique breadth r=.27只是受限关联；33.5→56.1%的时间变化含检测改进混杂。GTG个案自主阶段不等于全链无人，最后提取仍human-directed；防线发布是作者声明而非效果验收。Ch72原SecurityAgent/Containment有trace、authority/effect分层，但没有priority目标与ontology盲区；root通过窄gap后，已实际在SecurityAgent末→Containment前写两段（当前671/673，唯一SF-ANTHROPIC-ATTACK-NAVIGATOR），root非作者实际写后通过，不据安全新闻泛改书。

原64 arXiv的有效机制笔记、旧§4原文和采用快照保留在[唯一packet旧正式§4](../_sources/daily-20260604/V3_RECOVERY_BLOCKERS.md)，全部注明非本次日期/Books验收。UltraEP04101v1官方admin license-right removal/withdrawn已轻量核，保持去入选/评分/采用；不是外部访问障碍。EvalStop04145v1只有submission史，本轮不得把旧Ch31写入计为新I，但不删除有效正文。

## 5. 缺口与下一步

普通可执行待办为0：两个确定候选的必要审阅、owner对照、授权窄写、非作者写后及root最终日级独立Gate均已完成。以下均为不支持正面采用或无遗漏断言的精确终态保留。

本窗已隔离限制：

- **65个具名DateHold**：[packet统一身份表](../_sources/daily-20260604/V3_RECOVERY_BLOCKERS.md)。64旧身份+MetaPointdisjoint；缺first-public上界，不作候选/评分/正面采用或覆盖无遗漏断言。每身份只请求一次官方当批公告、带时区作者公开正文receipt或可靠原始公开快照；到达只重开该身份日期及依赖采用，不补造08–09。不是65篇证据全审。
- **Google/Qwen/MiMo/MiniMax Agent历史目录**：上述有限入口分别仅精选/旧配置/undated routes/壳，需本窗目标primary dated feed或原发布receipt。来源表的局限不可升级为零命中或全来源无漏项；其他已确定事件继续。
- **arXiv主题公开批次**：日级公告缺失、月级/提交字段不足，不能据旧575/全年索引宣布本窗主题筛选完整。定点恢复原目标公开批次后再处理相关主题线索，不无界回溯。

窗外恢复线索，不属于本窗、不阻塞本日：Dreaming官方RSS=2026-06-04T17:00:00+08:00，归06/05默认窗口；本日只核时钟，未复审其正文。其余窗外目录标题不构成后日已审候选。

## 6. 复核

复核者：root（非作者）。
结论：通过

root实际读最终六部分、唯一packet当前恢复/采用边界及65具名隔离行；两个必要primary→actual-owner、Ch81/Ch72各两段及相邻衔接实际写后均通过。独立API另核Kimi release333758230原时钟/flags；OpenAI三运营/政策事件原RSS时钟与Wasmer、blueprint核心负侧抽核通过，五条作者核心关闭均保留。UltraEP exact04101v1原页admin明确rights/license removal且新版withdrawn，风险负侧保持不采用。Anthropic两官方正文/日期与score核心由root独立读；精确内嵌publishedOn复用作者可复查原HTML记录，不声称root遭403后重新取得该字段。其余来源按实际有限stop与5历史覆盖缺口验收安全隔离，不作无遗漏断言。65保留项不是全文审阅、证据或日期通过；旧报告复核标签不继承。当前完成态V3与四文件限定diff-check已实际通过，普通待办0。未stage、commit或push；未改月索引/LEARNING_STATE，Books仅上述授权窄段。
