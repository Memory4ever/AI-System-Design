# 2026-03-15 有限来源与筛选停点

执行日期2026-10-02；固定窗口[2026-03-14T09:00:00+08:00,2026-03-15T09:00:00+08:00)。作者mar01_v3。当前合同独立加载，旧V2.1规则/候选/EffectiveDate豁免不继承，不加载Weekly。以下只记录实际执行；当前目录不是完整机构历史，宽目录不变成题摘或全文队列。

## 14源实际入口及停止范围

| 来源 | 实际请求及有限停止 |
| --- | --- |
| OpenAI | https://openai.com/research/ 为当前精选；https://openai.com/news/rss.xml 实际解析1241项，仅筛3/13–3/16的pubDate，返回1条元数据 Why Codex Security Doesn’t Include a SAST Report，Mon,16Mar2026 00:00:00GMT（3/16 08BJT，窗外），未读其core。RSS原字段见V3_PUBLIC_DIRECTORY_FIELDS.json，不宣称所有历史Research覆盖。 |
| Anthropic | https://www.anthropic.com/research 当前10 publication，See more实际仍同页；https://alignment.anthropic.com/ March组5条，只定点header：coding-audit-realism3/23、automated-alignment-agent3/11、auditbench3/10、challenges-hopes3/5，均窗外；Abstractive仅March2026，读核心12–43及旧稿题摘做身份/贡献关闭。主Research历史分页未恢复。 |
| Google | https://deepmind.google/research/ 当前8项精选；https://deepmind.google/blog/page/3/ 实际24卡May→Feb，定点header cognitive-framework3/17、AlphaGo3/10夹住窗口；https://research.google/blog/2026/03/ page1的12卡，3/16→3/12夹住窗口，page2更早不扩；https://research.google/pubs/ 当前仅年份，未取得日级论文历史。没有全扫372条2026论文。 |
| Meta | https://ai.meta.com/research/ 实际0行；从Blog的publication导航请求 https://ai.meta.com/results/?content_types%5B0%5D=publication 超时；https://ai.meta.com/blog/ 10卡及?page=2的12卡非严格时间排序，3/11 MTIA、3/27 SAM3.1与更早卡无可见3/14–15条目。论文历史仍缺；本日没有IAB检查，不继承其他日browser失败。 |
| Qwen | https://qwenlm.github.io/ 明示迁移，新https://qwen.ai/blog 静态0行；直接public https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US 只投影title/path/date实际40项，2/16 Qwen3.5→3/19 Max Preview夹住窗口。初次full article正文截断所得3片段不是目录数，已用live slim projection修正；不保存内部git字段。 |
| DeepSeek | https://www.deepseek.com/en/news/ 实际Research10、News5；Research2/25 DualPath→6/24 V4、News12/1→4/24夹窗。停可见目录，View all未展开，不外推删除项。 |
| Kimi | https://www.kimi.com/en/blog/ 实际可见19条，2/9 AgentSwarm→4/20 K2.6夹窗；不拿旧platform只到2025反证2026无研究。 |
| Hunyuan | Research静态请求400timeout；使用官方脚本已观察到的生产public endpoint，实际POST https://api.hunyuan.tencent.com/api/blog/publicList ，body pageNum1/pageSize20/renderType0，total11且11/11返回，显示日期2/13→4/23夹窗。原字段见V3_PUBLIC_DIRECTORY_FIELDS.json。共享恢复文件只用于已公开endpoint定位，不继承其他日研究判断。 |
| Z.ai | https://www.zhipuai.cn/zh/research 实际15卡（2025/12/9→2026/8/26），停查看更；3/15 Turbo链接 /zh/research/155 实际读header及core16–90，具体关闭见下节，未把15卡全量题摘。 |
| Seed | Research当前5Blog/10Pubs、public_papers当前page1 20/242不是March历史。实际public get_article_list_v2?article_type=1&publish_year=2026&page_token=20&count=100&order_desc=false，x-tt-locale US，18项/total82、next40、has_moretrue，2/25→3/26切片；3/12→3/15 νTNS→3/16为邻接。只有νTNS完整题摘范围关闭；不扩其余64项。字段来自ArticleMeta/ArticleSubContentEn，初次18null投影错误已修正，null不是零命中。 |
| Baidu | https://ernie.baidu.com/blog/zh/ page1实际10卡，2025/11/21→2026/5/9，2/6→4/15夹窗；page2更早，无需扩。 |
| MiMo | https://mimo.xiaomi.com/ Paper8，3/13 ARL-Tangram→6/29 MOPD夹窗；Blog15无日期标题，More未提供可用历史分页；/blog/ 实际是2025/12/16 V2Flash单篇。需要Blog本窗日期切片，不全读15正文。 |
| MiniMax | https://www.minimax.io/blog 实际12卡；中文minimaxi redirect minimax.cn/blog实际13卡；3/18 M2.7→Feb Forge/M2.5夹窗。Forge英文2/14、中文2/12原值保留；Agent Tech仅heading，llms.txt48行提供当前docs/techblog.md但链接不可读。当前用户docs不是本窗历史技术发布。 |
| arXiv | 四组主题API与一次合并恢复均失败；实际参数/完整query/error见V3_ARXIV_QUERY_STOP.json。Submitted缓冲UTC3/13 01→3/15 01，start0/max200/sortsubmittedDate ascending，不是公开时间。无可用元数据，未将失败记0命中，未生成题摘/附件队列。 |

Public目录安全字段：[RSS/Qwen/Hunyuan/DataCite](V3_PUBLIC_DIRECTORY_FIELDS.json)、[Seed论文原值/UTC/BJT与页停点](V3_SEED_FINITE_FIELDS.json)、[本日Seed Blog定点字段](V3_SEED_BLOG_FINITE_FIELDS.json)。

最终Gate发现Seed Blog历史部分未交代，已本日一次定点恢复type2/year2026/page_token0/count100/order_descfalse、US locale，仅投影title/path/PublishDate/UTC/BJT。实际返回14项、total19、next空、has_morefalse，2/16 Arena Preview→4/1 Recruitment夹窗，返回条目无本窗日期；不把14当19/19，不推断为何5条未返回。剩余5项/本窗Blog历史切片在README§5精确隔离，未扩全部Blog/附件或继承03/14判断。

## arXiv 有界查询与日期权限

Systems：CL/LG/DC/AR/PL/OS/PF×large language model/distributed training/speculative decoding/kernel/inference，timeout。Learning：CL/LG×Transformer/MoE/language model×optimization/scaling/representation/attention，429。Multimodal：CV/RO/CL×world model/VLA/video generation/multimodal foundation，timeout。Agent/eval：AI/MA/IR/CL×LM/LLM×agent/retrieval/evaluation，timeout。一次四组OR合并恢复也429；停止，不继续代码考古或抓整个March。

官方 https://info.arxiv.org/help/availability.html 已实际读170–189：公告Sunday–Thursday Eastern20:00，Friday/Saturday无通常公告，ID/DOI只在announced后生成不能提前给。DST后邻接常规slot为3/13 08BJT与3/16 08BJT，均窗外；不能因此反推作者稿首次公开或全部相关事件为零。

曾请求 /list/cs/2026-03-14 和03-15但未建立这类YYYY-MM-DD路径是有效按日入口，两次cachemiss只表示请求无可用资料，不叫“官方按日历史列表受阻”。必要缺口是四主题历史slice/可核具体dated原event，而非这些路径必须恢复。

DataCite实际client-id:arxiv.content AND registered:[2026-03-14T01:00:00Z TO 2026-03-15T01:00:00Z]，page size10，meta total0/pages0，仅辅助索引响应；不用registered替代exact公告，不用0支持无遗漏。Submitted/created/目录显示日期不能单独证明first-public。

## 具名关闭与独立校准

1. **GLM-5-Turbo**：https://www.zhipuai.cn/zh/research/155 ，header原值2026/03/15 16:00（页面未明确时区，不补first-public时刻）。实际core16–90：训练只说明对OpenClaw场景的工具/指令/长任务/高吞吐目标，未披露具体objective/data/预算机制；ZClawBench给场景类别/排行与Skills比例，不给改变具体评价选择的独立protocol/盲点控制；Claw Enterprise RBAC、audit、encryption、human approval是产品特征承诺，没有可审新约束/实现反证。关闭本次公开增量，不泛化排除新模型，不采用安全保证。无需对已贡献前关闭项穷查日期。
2. **Abstractive Red Teaming**：https://alignment.anthropic.com/2026/abstractive-red-teaming/ ，仅March2026，core12–43实读；唯一 https://arxiv.org/abs/2602.12318v1 完整题摘/历史Feb12T18:12:12Z。category search、CRL/QCI与7×12评价同旧工作，未见独立revision或新机制说明；关闭本次重呈现，未宣称旧论文全文Evidence已验收，也不按发现日期归入本日。
3. **νTNS**：https://arxiv.org/abs/2603.14425v1 完整题摘/历史，SubmittedMar15T15:09:00Z；Seed id1414 PublishDate1773504000000→Mar15 00BJT先于Submitted，显示字段不是first-public证明。neural disentangler/CNN+tensor-network为量子manybody/J1-J2 Heisenberg物理求能量，当前AIforScience暂缓，没有foundation系统增量；贡献前关闭，不为目录/Submitted差异另开日期请求或全文队列。

root已实际读Turbo core/header、νTNS v1题摘/历史、Abstractive core+唯一v1题摘，2026-10-02首批独立校准通过。其余目录元数据不是root逐项题摘/全文验收。候选0；未写Books或共享LS/索引。

## 停止与重开

当前可用原始入口的有限检查已停止；七组必要历史缺口（增加Seed Blog）见正式README§5。外部终态保留项不支持正面证据、Books或无遗漏断言。只在得到本窗官方历史切片/原始作者event与可核日期时重开该来源受影响材料，不重扫整月，不将宽目录转换为任务队列。root实际读完整正式六部分/本停点/3原JSON，三关闭独立证据已通过；其指定Seed Blog补查与精确隔离已落实，按授权最终日Gate通过。普通待办0，没有Books写入待POST。
