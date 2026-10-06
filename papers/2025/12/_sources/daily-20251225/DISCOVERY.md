# 12/25 原始发现范围与有限恢复停止点

检查时间：2026-10-02T18:07:08+08:00。本窗 12/24 09:00 至 12/25 09:00 北京。以下是作者原始过程，不是覆盖或独立复核通过。

## 固定官方目录的原始邻接摘录

本节只保存实际读到的原始目录段；后续日期可按自己的窗口重读这些段，不复用本日完成结论。无时区的目录日期只保留日期，不补时刻。

| 原始入口和停止点 | 实际相邻记录或返回 | 能证明与不能证明 |
| --- | --- | --- |
| [DeepSeek updates](https://api-docs.deepseek.com/updates) | 2026-04-24 V4；2025-12-01 V3.2 | 可见更新目录的相邻段，非全部研究全集 |
| [Kimi Platform Blog](https://platform.kimi.com/blog) | 可见26项，最新2025-11-07/11-06 K2 Thinking，再至2024；另读 CLI changelog 0.69 Dec29 / 0.68 Dec24 / 0.67 Dec22 | 模型 Blog 与 CLI release 是不同事件入口 |
| [Z.ai Research](https://www.zhipuai.cn/zh/research) | 2026-01-13；2025-12-10 GLM-TTS；2025-12-09 GLM-ASR-Nano | 首查 Research 的实际历史段 |
| [Z.ai release](https://docs.z.ai/release-notes/new-released) | 2026-01-14；2025-12-22 GLM-4.7 | 不能替代 Research 目录 |
| [ERNIE 中文 Blog](https://ernie.baidu.com/blog/zh/) | 第一页相邻2026-01-08 / 2025-12-23排名 / 2025-12-09排名；第二页更早，共2页 | 目录本窗附近已到达，排名负侧另有准入记录 |
| [MiniMax English](https://www.minimax.io/blog) / [中文](https://www.minimax.cn/blog) | 英文可见12项相邻2026-01-27 / 2025-12-23 M2.1 / 2025-10-27；中文13项相邻2026-01-28 / 12-23 / 10-27 | 两原始目录均检查，不以宣传简介代替机制审阅 |
| [Agent techblog.md](https://agent.minimax.io/docs/techblog.md) | 从llms.txt定位后原始Markdown只有2026-05-13 Agent Team一项 | 当前目录不保证2025历史完整 |
| [MiMo Paper](https://mimo.xiaomi.com/) | Paper八项，目标附近2026-01-08 V2 Flash / 2025-10-21 MoE；Blog十五项不含可提取日期 | Paper邻接与Blog历史缺失分开 |
| [Meta Publications page3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3) | 2026-01-02 PhyGDPO / 2025-12-26 Safety Alignment of LMs via Non-cooperative Games / 2025-12-18四项watermark / 2025-12-16 SAM Audio；其后混入2020等旧置顶项 | 目录不是严格全局排序；page4另读到12-16/12-12/12-01；Blog page2读到12-18/12-16。12-26日期未给时区，不移到12/25 |
| [Seed public_papers](https://seed.bytedance.com/en/public_papers) | 原始页面组件公开GET /api/get_article_list_v2；article_type=1,publish_year=2025,count=20,page_token=0,order_desc=true，x-tt-locale=US。返回sub_article_list 18项,total94,has_more=true,next20；最晚12-15 Seedance、12-02 GR-RL，下一10-22 Seed3D | 排序段已低于目标，停止，不继续无关旧页。PublishDate为目录epoch毫秒，不是arXiv公告 |

## 有限外部历史缺口

- OpenAI：Research/index当前为2026；直接原始HTTP403；官方限定December24研究搜索及December2025研究搜索返回12-18 CoT monitorability、12-16 FrontierScience、12-11 GPT5.2等较早记录，没有原始完整日目录。停止重复入口尝试，保留历史切片缺口，不称零。
- Anthropic：Research当前十项为2026；实际See More返回同URL同十项；直接HTTP403。官方限定12/23至12/26及December2025检索只恢复12-02等较早线索。原始历史分页仍不可得，隔离。
- Google：DeepMind Research当前入口；Google Research 2025筛选676项仅年粒度；直接Google正文恢复但没有日粒度契约。官方域限定December24两站查询空；DeepMind带query历史入口不可得。年库不是日公告，不继续全676项，历史日切片隔离。
- Qwen：旧入口明确迁移，qwen.ai/blog提取空；官方搜索和HF卡用于2511必要证据。公开p_home-index.js实际读到articles和fetchData但无可用历史列表请求；不猜API、不遍历所有chunks。2511已贡献前关闭，其他本窗目录不可得隔离。
- Hunyuan：公开组件恢复POST https://api.hunyuan.tencent.com/api/blog/publicList，pageNum1/pageSize1000/renderType0，code0,totalNum11,length11，全为2026，最早displayPublishTime1770092288=2026-02-03 12:18:08+08。浏览器有限失败；官方域历史查询返回issues等而非完整研究历史。当前11项不是2025零证明。Foley#44/#45为speech/sample rate用户问题、WorldMirror#36为depth提问，没有官方新增机制答复，不评分。
- MiMo：Paper历史邻接可得；Blog日期空。定点/blog/mimo-v2-flash与公开路由组件都实际尝试，未恢复历史日期；官方限定December24检索无可用原始历史目录。仅Blog部分隔离。

上述恢复条件：原始机构发布列表/历史快照含本窗完整分页，或明确相关事件的作者原文及公开范围。只重开对应源/事件，不扫描周级来源、不根据搜索空补零。

## arXiv 主题与身份检查

已执行：language model摘要、LLM同义查询；因首次公告字段只支持年月，日粒度空响应作失败记录。随后submitted_date_first的12/22至12/24身份查询（语言模型）原始213项，首200页输出过宽，未称逐项筛选完成；另12/24至12/25语言线索79项，仅身份补检。提交范围不是本窗公开范围。

系统/多模态查漏：title OR vision-language / world model / vision language action / diffusion language / large language / LLM / GPU / kernel / transformer，computer all+cross include，submitted_date_first 12/22至12/24，size200,start0，实际154项无next。含通用kernel/transformer领域条目，收窄为大模型与系统相关身份，不把154项变成读文队列。

Agent补检：title OR agent / RAG / memory，同日期与分类参数，实际61项无next。排除标题明确的医疗/分子/电网领域应用、传统材料memory与暂缓AI for Science；相关但首公告不明的追加身份保留包括20798 outcome-driven constraint violations、20687 PHOTON、20458 Laser、20362 CRAFT、20278 procedural memory、20184 Reaching Agreement、20111 ABBEL、20092 Memory-T1、20083 embodied metamorphic testing、19539 StoryMem、19432 MobileWorld、19234 DeliveryBench、19154 non-Markovian memory。没有把这些未完成贡献判断项降分或称负侧；先隔离必要公开日期，不进入本窗候选或Books。

官方列表有界补检：[cs.CL长格式](https://arxiv.org/list/cs.CL/2025-12?show=2000&skip=0)1302身份库，仅相关654至678及cross条目附近；[cs.DC](https://arxiv.org/list/cs.DC/2025-12?show=2000&skip=0)332身份库，相关147至157附近；[cs.CV](https://arxiv.org/list/cs.CV/2025-12?show=2000&skip=0)可访问但无日公告，按已知VideoScaffold/VLA线索定点，不全量排队。cs.AR月列表有限尝试Cache miss，保留系统列表缺口；主题查询已跨computer分类但不宣称全召回。

实际打开官方abs题摘的相关身份（2512前缀省略；不是本窗候选数，也不是精确正文审阅数）：22238、22234、22226、22250、20940、19905、19879、19769、19682、19673、19606、19585、19562、19535、19443、19433、19428、19424、19399、19396、19350、19297、19250、19238、19219、19215、19210、19206、19179、19178、19173、19171、19159、19135、19134、19126、19125、19849、19011、19070、18987；另20920、20861、20839、20612、20573、20276、20237、20210、20188、20169、20168、20159、20080、20061、19941、19920、19378、19323、19243、19133、19115、19081、19069、22219、22245。

其中潜在增量包括Diffusion drafter动态投机长度、VLA跨请求prefill/decode管线、query相关性KV量化、RDMA代理通信、可逆MoE训练激活、Agent记忆反思检索；安全/反证身份19297、19215、20168、19238不因日期难而降分关闭。必要首次公开不可恢复，保留未评分。abs/v1有当前改名摘要风险：19179当前题名L4、19219当前ImageLoRA；URL含v1不保证题摘是当年精确版本。AXIOM20159官方abs题摘本身末段省略，不补造内容。

公开日期有限恢复已试：announced_date_first日粒度无效；官方长月表只能身份；版本published/Submitted不是首次公开；官方catchup/cs.CL/2025-12-24 Cache miss；OAI版本日期与datestamp语义不提供首公告。已直接读取2025原始holiday公告，仍无法据接收排期确定上述ID实际公告。安全隔离这些潜在线索，不用于候选、Books、零事件或覆盖保证。重开条件为逐ID官方new公告批次/历史首公开时间或作者可验证首次公开范围；确认所属日后再完成贡献及精确正文。

## 实际触发的安全线索

[GHSA-67mc-j5jh-9m9f](https://github.com/advisories/GHSA-67mc-j5jh-9m9f)在Hunyuan搜索中发现，实际完整读到GitHub ingested Dec24、NVD Dec23；不是首次披露。定点原始[ZDI-25-1032](https://www.zerodayinitiative.com/advisories/ZDI-25-1032/)明确coordinated public release与updated均2025-12-01，涉及MimicMotion create_pipeline不可信反序列化且需要用户交互。官方Tencent/MimicMotion commit6907bdcc259a6a048d41a365e840d22274f9256c实际API日期2025-11-18T06:29:06Z，patch为兼容低版本torch的safe_globals分支。事件在本窗外，不以GitHub收录改归属、不声称所有安装root或已安全修复；交真实日期恢复，不阻塞本窗。未因此扩扫安全数据库。

## 作者停点

普通可执行发现待办0；上述必要原始历史/公开日期为本窗终态外部保留，不等于Coverage/Evidence通过。确认落窗1家族Kimi0.68，准入已由root通过，受影响精确静态实现读完、未运行验证；唯一owner Ch83局部草案见KIMI_068.md，主线程协调Books与独立核验。报告继续进行中，作者立即推进12/26。
