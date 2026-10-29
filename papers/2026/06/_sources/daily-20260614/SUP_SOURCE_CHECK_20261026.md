# Jun14 补遗漏：本日来源检查

作者 `supp_jun14`，检查 2026-10-26 11:06～11:18 +08:00，仅补 2026-06-13 BJT。已读当前合同，不把旧零候选、旧 recert 或他日池当新增覆盖。以下原件均为本轮实际请求；`SUP_RAW_*_20261026.raw` 存在本目录。未引入 Weekly、Live、2025 或缺失 Daily。

## 十三 Daily 源：入口、日期邻段与停止

- **OpenAI**：`https://openai.com/news/rss.xml`，200、1318 items、单响应。目标邻段原 `pubDate`：`Fri, 12 Jun 2026 10:00:00 GMT` / Academy courses、`Fri, 12 Jun 2026 00:00:00 GMT` / Preply → `Sun, 14 Jun 2026 17:00:00 GMT` / Partner Network。全部不落 Jun13 BJT；停止这一日期邻段，不阅读历年正文。原件 `SUP_RAW_OPENAI_RSS_20261026.raw`。
- **Anthropic**：首查 `/research`，再恢复 `https://www.anthropic.com/listing/research/default/2`。200，24 `posts`、`hasNextPage:true`，该页跨度 Jul28～Apr23，目标原 `publishedOn=2026-06-12` / `anthropic-public-record` → `2026-06-16` / `claude-code-expertise`；已越过目标，停止第2页，不继续更旧页。`_updatedAt` 不作公开日。
- **Google AI**：首查 DeepMind Research；Blog `/blog/page/2/` 的六月卡只有月份，不能据字面无Jun13判零。按其顺序定点恢复原页：相邻 [Investing in multi-agent AI safety research](https://deepmind.google/blog/investing-in-multi-agent-ai-safety-research/) 为 `June 11, 2026`（raw `DM_MULTIAGENT`），前一 [UK house-building](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/) 为 `June 16, 2026`（本轮 web 直接打开）；更晚 [Securing agents](https://deepmind.google/blog/securing-the-future-of-ai-agents/) 为 `June 18, 2026`。邻段内无 Jun13 卡，不把11张月卡变成全文/题摘队列。另四个实际日期原件 `DM_MULTIAGENT/DM_DIFFUSION/DM_TRANSLATE/DM_SIERRA` 是日期核验，不是贡献候选。Google Research 原域连接超时后从同站 `https://www.research.google/blog/2026/06/` 通过 web 恢复：完整12项、一页无下页，目标邻段 Jun12 的 Skin conditions / retired phones → Jun16 Earth AI，无Jun13。Google Publications 通过 web 可读，但只有年级筛选（2026 430条）与当下目录，不能恢复 Jun13 首公开；**仅此日级 Publications 历史缺口隔离**，不称 Google 全研究零事件。curl失败未授覆盖。
- **Meta**：`https://ai.meta.com/research/` 的 web打开无可读正文；curl Research/Blog 均连接超时并有限重试。`https://ai.meta.com/blog/` 经 web成功，当前可见相邻卡 June29 Brain2Qwerty 与 April08 Muse Spark，首屏无Jun13；底部 `Next` 存在且排列不严格按日期，不据首屏证明完整历史。定点辅助搜索 `site:ai.meta.com "June 13, 2026"` 无结果，只作有限补检，**Jun13完整历史目录隔离**，无“零研究”结论。
- **Qwen**：官方 `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 与 `language=zh-CN` 均200、`success:true`、`data.articles`各40项，无分页字段。六月 `extra.date` 为 Jun01 10:00+08 Qwen3.7Plus → Jun16 08:00+08三机器人/10:00+08套件 → Jun23 11:30:30+08 AgentWorld，无Jun13。只核日期邻段，不审阅其他日正文；未用无参数空数组证明零。
- **DeepSeek**：`https://api-docs.deepseek.com/updates`，200完整单页，原h2从 `Date:2026-04-24 / DeepSeek-V4` 到 `Date:2026-07-31 / V4-Flash Update`，无Jun13；停止邻段，不遍普通提交。
- **Moonshot/Kimi**：`https://platform.kimi.com/blog` 200，完整可见表最后为2025-11-07，不能冒充2026历史全档；`https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=updated` 200返回42（小于100），本响应未见Jun13新建研究项目。`created_at`只作项目导航，不证明release/论文公开日。定点辅助查询 `site:platform.kimi.com "2026-06-13"` 无结果；**2026本日完整发布历史仍检索受限**，不是全源零保证。无具名当日release线索，不扩为42仓全release/PR扫描。
- **Hunyuan**：首查 Research，采用官方 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，头 `accept-language:zh`，体 `{"pageNum":1,"pageSize":100,"renderType":0}`；200、`code:0`、`data.totalNum:11`/list11，无下页。目标邻段 `id100041 Hy-MT2 / displayPublishTime1779346800`（May21 BJT）→ `id100064 Hy3 /1783320600`（Jul06 BJT）。显示日期仅支持目录邻段，不改称全球首公开；无Jun13显示项。
- **Z.ai**：`https://www.zhipuai.cn/zh/research`，200，实际可见日期顺序 May20 ZCube → Jun16 GLM5.2，已越过目标，停止首屏。未用对象`createdAt/updatedAt`替代可见公开日期，不展开更早“查看更多”。
- **Seed**：`https://seed.bytedance.com/en/public_papers`，200，第1页 `1-20 of247 / Page1 of13`，目标邻段 Jun11 Chemical Reaction → Jun19 Seed2.0 Model Card，已越过Jun13；停止第1页。科学标题仅日期导航，不以AI for Science进候选。
- **ERNIE**：`https://ernie.baidu.com/blog/zh/`，200，首屏最新May09文心5.1，已早于目标；不继续更旧分页，不读窗外贡献。
- **MiMo**：首查 `https://mimo.xiaomi.com/`，Paper目标邻段Mar13 ARL-Tangram → Jun29 MOPD。Blog卡片无日期，因此恢复官方页面引用bundle `https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js`：route frontmatter `/blog/mimo-v2-5-inference` May30、`/blog/mimo-tilert-1000tps` Jun08、`/blog/mimo-code-long-horizon` Jun10；更晚V2.6内容Sep22。其余无日期模型route由官方 `https://mimo.mi.com/docs/en-US/updates/model` 单页恢复：Apr23 V2.5/Pro/TTS → Jun02 ASR → Sep22 V2.6，已越过目标，无Jun13新项；不把CSR壳当零、不继续窗外正文。
- **MiniMax**：`https://www.minimax.io/blog`，200，目录邻段Jun09 MaxProof、Jun01 M3，后项更晚；目标Jun13无卡。停止相邻日期，不因标题相关重审Jun09。

## arXiv：自然日与合法元数据核查

`https://info.arxiv.org/help/availability.html` 本轮200原件（`SUP_RAW_ARXIV_RULES_20261026.raw`）说明：按ET周日到周四20:00公告，周五/六不公告，涵盖新稿、replacement、withdrawal、cross-list、journal-reference；最终ID/DOI公告时分配。2026年六月为EDT。Jun13 BJT是周六，前一常规公告Jun11 20:00 EDT＝Jun12 08:00 BJT，下一Jun14 20:00 EDT＝Jun15 08:00 BJT。因此无本日常规公告批次，不能从本日submission造论文新公开。

适用历史规则由当前合同指定的 [2025-01-06官方版本](https://github.com/arXiv/arxiv-docs/blob/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md)承载同一日程及发号规则；本轮重取raw连接超时不作为反证，复用当前合同已核规则而非假称重新下载成功。

DataCite原请求（`curl -G`等价URL编码，原响应已保存）：

```text
https://api.datacite.org/dois
client-id=arxiv.content
query=registered:[2026-06-12T16:00:00Z TO 2026-06-13T15:59:59Z]
page[size]=1000
```

`SUP_RAW_DATACITE_JUN13_20261026.raw`：200，`meta.total:0,totalPages:0,page:1,data:[]`，无下页。正控同client参数、`registered:[2026-06-12T00:00:00Z TO 2026-06-12T23:59:59Z]`/size1，`total1269`，首项`10.48550/arxiv.2606.13221`/`registered2026-06-12T02:06:17Z`；见`SUP_RAW_DATACITE_POSITIVE_20261026.raw`。正控不扩为Jun12候选池，`registered`不改名为实际公开时刻，未用`created`或`submitted`作公开日。

官方历史月导航 `https://arxiv.org/list/cs.CL/2026-06` 与 `cs.LG/2026-06` 本轮均200，月总2722/5233、默认各首50。月首页不是Jun13清单，无本日公告批次时不把月池转为逐项审阅/全文配额。未使用`/2606`或catchup历史入口。暂无具体更早正文、延迟公告、实质修订或撤回线索需要恢复；如取得精确Jun13事件，只重开其家族，不用周末规则拦截反证。

## 独核补充的有限入口

`jun14_review` 在本轮独立复核实际打开 Meta Blog `https://ai.meta.com/blog/?page=2`，可见 March27 SAM3.1、March11 MTIA，之后为Dec2025/Feb2026及2025乱序卡。并非把Next当外部故障：实际续到第2页后未见Jun13，停止已越目标的有限两页。此补核扩充Blog可见范围，不恢复Research完整日级档案；正文已同步。Google六月12项、UK Jun16、security Jun18均由该reader独立实际打开确认，不再重复请求。

## 本轮漏斗与隔离

尚未发现可进入本日贡献判断的独立材料，新增候选0、评分0、证据审阅0、Books无改；日期邻段核查不是“0篇全文读完”，也没有可供准入校准的P/N题摘集合。原旧候选0与§4空保持，旧小时窗不搬移。

Google Publications日级历史目录、Meta完整历史目录、Moonshot2026完整发布历史是上述**具名外部保留项**；不支持正面Coverage/Evidence、无遗漏断言或Books。替代材料分别为可复查Jun13有日期官方清单/当日原件/目录快照，取得后仅定点恢复相应来源与材料。无已知本日拟候选的日期、正文或owner普通待办。待唯一非writer核本轮真实源范围及报告保存态后才能结束。
