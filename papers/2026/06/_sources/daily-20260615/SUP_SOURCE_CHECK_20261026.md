# Jun15 补遗漏：本日来源检查

作者 `supp_jun15`；执行 2026-10-26（Asia/Shanghai），只补 2026-06-14 北京时间自然日。已完整加载磁盘 AGENTS、当前研究/Report 合同、来源使用说明及 Daily/arXiv 分组、Prompt、ROADMAP 和本日 State 路由。只保留旧 44 家族、日期/评分/小时窗及有效证据，不用其 471 身份宽池或别日/Weekly 候选反推本日。原件是本轮实际请求的 `SUP_RAW_*_20261026.raw`；未将下载等同阅读或覆盖。

## 十三 Daily 来源与停止界

- **OpenAI**：`https://openai.com/news/rss.xml`，200、1318 items、单响应。目标邻段：Academy courses 原 `Fri, 12 Jun 2026 10:00:00 GMT` → Partner Network 原 `Sun, 14 Jun 2026 17:00:00 GMT` → deployment simulation 原 `Tue, 16 Jun 2026 00:00:00 GMT`。Partner Network 实为 Jun15 01:00 BJT，不是 Jun14 当窗研究；这是日期关闭，不是以 Business 标题判无贡献。停止目标邻段，不展开其他日期全文。原件 `SUP_RAW_OPENAI_RSS_20261026.raw`。
- **Anthropic**：首查 `/research`，恢复 `https://www.anthropic.com/listing/research/default/2`，200、24 posts、`hasNextPage:true`，跨度 Jul28～Apr23；目标 `publishedOn=2026-06-12 / anthropic-public-record` → `2026-06-16 / claude-code-expertise`，越过 Jun14，停止第2页。`_updatedAt` 不作公开日期。
- **Google AI**：首查 `https://deepmind.google/research/`，200；`https://deepmind.google/blog/page/2/` 200 的六月月份卡不能单独授日级零。定点打开卡片原页 [Investing in multi-agent AI safety research](https://deepmind.google/blog/investing-in-multi-agent-ai-safety-research/) 显示 `June 11, 2026`，其后一卡 [UK house-building](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/) 显示 `June 16, 2026`，已跨过目标；不把其余月卡变成全文队列。Google Research 六月档 `https://www.research.google/blog/2026/06/` 经 web 实际读取全部12项、一页无下页，Jun12 Skin conditions/retired phones → Jun16 Earth AI，未见 Jun14。curl 对 Google 域连接超时不作零命中依据。`https://research.google/pubs/` 经 web 可读，但只有年级过滤（2026 430）和当前目录，未恢复 Jun14 日级首公开；这一 **Publications 历史日级缺口保留**，不是全 Google 研究零事件。
- **Meta**：`https://ai.meta.com/research/` 经 web 打开返回0可读行，curl Research/Blog 均连接超时。Blog 经 web 实际读取 `https://ai.meta.com/blog/` 与 `?page=2`：首页可见 June29 Brain2Qwerty、April08 Muse Spark，第二页 March27 SAM3.1、March11 MTIA 后到2025/Feb2026乱序卡；有限两页未见 Jun14，停止第2页，不把乱序目录视为完整历史。辅助查询 `site:ai.meta.com "June 14, 2026"` 返回历史/非目标日 Publications 页面，不构成当窗事件。**Jun14 完整历史目录保留**，无全源零保证。
- **Qwen**：官方 `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 与 `language=zh-CN` 均200、`success:true`、`data.articles` 各40项，无分页字段。目录 `extra.date`：Jun01 10:00+08 Qwen3.7Plus → Jun16 08:00+08 RobotNav/World/Manip、10:00+08 Suite → Jun23 11:30:30+08 AgentWorld；无 Jun14 目录项。仅用于目标邻段，不审阅窗外贡献，未用无参数空数组授零。
- **DeepSeek**：`https://api-docs.deepseek.com/updates` 200 单页，日期标题 `Date:2026-04-24 / DeepSeek-V4` → `Date:2026-07-31 / V4-Flash Update`，已越过目标，没有 Jun14 条目。停止日期邻段，不遍普通提交。
- **Moonshot/Kimi**：`https://platform.kimi.com/blog` 200，最新可见2025-11-07，不能冒充2026历史档；`https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=updated` 200 返回42，小于100，无2026-06新建项目。`created_at` 只作项目导航，`updated_at` 不是论文/release公开日。辅助查询 `site:platform.kimi.com "2026-06-14"` 未返回目标原始事件；**2026 Jun14完整发布历史仍检索受限**。无具名当窗项目线索，不扩成42仓全release/PR扫描。
- **Hunyuan**：首查 `https://hunyuan.tencent.com/research` 200；实际官方公开 `POST https://api.hunyuan.tencent.com/api/blog/publicList`、头 `accept-language:zh`、体 `{"pageNum":1,"pageSize":100,"renderType":0}`，200、`code:0`、`data.totalNum:11`、list11，无下页。显示日期邻段 `id100041 / Hy-MT2 /1779346800`（May21 BJT）→ `id100064 / Hy3 /1783320600`（Jul06 BJT），无 Jun14 显示项；不把显示日期改名为全球首公开。
- **Z.ai**：`https://www.zhipuai.cn/zh/research` 200，日期顺序首屏 May20 ZCube → Jun16 GLM5.2，已越过 Jun14，停止首屏，不点更早“查看更多”；对象创建/更新时间不作公开日。
- **Seed**：`https://seed.bytedance.com/en/public_papers` 200，第1页 `1-20 of247 / Page1 of13`，Jun11 Chemical Reaction → Jun19 Seed2.0 Model Card，已越过 Jun14，停止第1页。科学应用只作日期导航，不纳入暂缓领域候选。
- **ERNIE**：`https://ernie.baidu.com/blog/zh/` 200，首屏最新 May09 文心5.1，已早于目标，停止首屏不读更旧分页或正文。
- **MiMo**：`https://mimo.xiaomi.com/` 200，Paper日期 Mar13 ARL-Tangram → Jun29 MOPD。Blog无日期卡从官方页面已引用bundle `https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js` 恢复 route/frontmatter：May30 mimo-v2-5-inference、Jun08 mimo-tilert-1000tps、Jun10 mimo-code-long-horizon，后到Sep版本。无日期模型route再由官方 `https://mimo.mi.com/docs/en-US/updates/model` 200单页恢复 Apr23 V2.5/Pro/TTS → Jun02 ASR → Sep22 V2.6，已越过 Jun14；不把CSR壳视为无事件。
- **MiniMax**：`https://www.minimax.io/blog` 200，目标邻段 Jun01 M3 → Jun09 MaxProof，后卡为更晚内容，未见 Jun14。停止日期邻段，不重审 Jun09 的相关贡献。

## arXiv：Jun14 自然日，而非 submission 或整月池

当前官方 `https://info.arxiv.org/help/availability.html` 200原件说明 ET Sunday through Thursday 公告、Friday/Saturday 无常规公告，适用 new/replacement/withdrawal/cross-list/journal-reference；最终ID/DOI公告时分配。目标 June14 BJT 为周日，对应 ET周六12:00～周日11:59:59（EDT），没有常规公告批。前一正常公告 June11 20:00 EDT＝June12 08:00 BJT；下一 June14 20:00 EDT＝June15 08:00 BJT。不是把周日提交误当周日公开，也不是绝对排除异常/作者渠道。

历史适用规则复用合同指定 [2025-01-06 官方 snapshot](https://github.com/arXiv/arxiv-docs/blob/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md) 的已核有效层，不声称每篇重新下载历史文档。

本轮 DataCite 实际请求：

```text
https://api.datacite.org/dois
client-id=arxiv.content
query=registered:[2026-06-13T16:00:00Z TO 2026-06-14T15:59:59Z]
page[size]=1000
```

`SUP_RAW_DATACITE_JUN14_20261026.raw` 200，`meta.total:0,totalPages:0,page:1,data:[]`，无下页。正控同client参数、`registered:[2026-06-12T00:00:00Z TO 2026-06-12T23:59:59Z]`、size1，200、total1269，精确 `10.48550/arxiv.2606.13221`、`state:findable`、`registered:2026-06-12T02:06:17Z`；原件 `SUP_RAW_DATACITE_POSITIVE_20261026.raw`。正控只验证来源和日期过滤，不扩为Jun12候选。`registered` 不是实际公开时间，`created` 不作上界。

官方 `https://arxiv.org/list/cs.CL/2026-06`、`cs.LG/2026-06` 均200，总2722/5233，默认各1-50。本轮仅恢复这两个有界导航入口与列表范围，未把月默认页声称Jun14日清单或逐日全召回，也没有将其全部标题送入贡献初筛。在无本日正常批且本日registered检索为0时，不将整月宽列表转为逐项题摘队列。关注范围仍为 ROADMAP 模型训练/推理、Agent、多模态/world/VLA、GPU计算/通信等主线；没有具名当窗延迟公告、更早正文、撤回或修订线索触发窄主题正文恢复。若取得此类精确原件，只重开该家族；不以周末规则拒绝反证。

## 漏斗、保旧及复核边界

本轮未发现可进入当窗贡献判断的独立材料：新增候选0、评分0、正文证据审阅0、Books无改；日期导航关闭不冒称完成题摘/全文筛选，没有P/N集合可作贡献准入校准。旧44家族、评分和有效证据原块保持，不重新搬移日期。旧471宽池“全量”声明仅属于既有历史审计，不是本轮覆盖方法或全球无遗漏保证。

Google Publications 日级历史、Meta Jun14完整历史、Moonshot Jun14完整发布历史为三个具名外部保留项；不授这些范围正面Coverage/Evidence，不用于Books或无遗漏保证。可接受替代为有Jun14日期的官方列表/目录快照或具名原件；到达后仅定点重开对应来源/家族。没有把尚可执行的正文阅读或Books差额改称终态。待唯一非writer检查本轮实际入口和最终保存态，当前仍进行中。
