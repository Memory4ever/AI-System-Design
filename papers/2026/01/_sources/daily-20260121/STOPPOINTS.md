# 2026-01-21 有限来源与筛选停点

执行日期：2026-10-04 BJT；记录截至03:35。窗口：2026-01-20T09:00:00+08:00 ～ 2026-01-21T09:00:00+08:00，含起点、不含终点。只读取本日材料与合同，LS顶部作路由；未读旧Daily/Weekly。宽索引不是题摘或逐项关闭队列。

## 官方入口及有限补检

- [official_initial_0.txt](./official_initial_0.txt)：OpenAI Research、Anthropic Research、DeepMind Research、Google pubs 首查。均为当前页，不假装历史全目录。
- [official_initial_1.txt](./official_initial_1.txt)：Meta Research（0行）、Qwen旧站（重定向；首页5项最晚2025-09-23）、DeepSeek主页（当前版本导航）、Kimi Blog（至2025-11-07）及MoonshotAI GitHub当前10条。
- [official_initial_2.txt](./official_initial_2.txt)：Hunyuan Research（抓取0行）、ZAI Research（目录跨过01/19至02/02）、Seed Research精选跨过2025-12-02至2026-01-27；Public Papers当前page1，1～20/242，13页，停在page1不把2026全年列为本窗命中。
- [official_initial_3.txt](./official_initial_3.txt)：ERNIE中文Blog有限可见目录；MiMo完整可见Paper8项（01/08至02/03跨窗）、Blog15项+More未提供可用日期索引；MiniMax英文Blog目录13项跨过12/23至01/27、中文重定向目录及Agent Tech Blog（15行无文章）。
- Tencent Research按来源合同用浏览器实际核查“全部”：page=1，11条，从09/22到02/03；最后两条是02/13 Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping、02/03 Learning from context is harder than we thought，下接footer，无本窗历史分页。不是0行抓取=0论文。另查Tencent-Hunyuan GitHub当前10/83，不逐repo普通修复扫描。
- Qwen新站 https://qwen.ai/blog web抓取0行；浏览器goto超时重置，已保留历史片段限制，不将失败当零命中。无安全/权限绕过。
- [recovery_3.txt](./recovery_3.txt)：ZAI release-notes完整可见日期组跨01/19 GLM-4.7-Flash至02/03 GLM-OCR；Qwen新站抓取0行，DeepMind当前Blog page1（停页1）；[date_recovery_1.txt](./date_recovery_1.txt)：Google Blog官方2026/01目录从01/28到01/12，01/15之后下一条01/22，无20日条目；Google pubs只有年份不能当首次公开。

以下辅助检索均停在一次返回的首屏，不声称全学科/全站召回；搜索引擎会返回无关日期、正文提及日期和GitHub普通issue，已作为线索而非原证。查询里的 OR 范围并不保证引擎严格遵守 site/时间条件，后续只核实际原源。

- [query_0.txt](./query_0.txt)：`site:openai.com (research OR model OR training OR inference) ("January 20, 2026" OR "January 21, 2026")`；Anthropic对应research/agent/alignment；Google对应DeepMind/Research+model/training/inference/agent；Meta对应research/model/training。返回多数窗外，不登记为本窗。
- [query_1.txt](./query_1.txt)：Qwen旧站、DeepSeek官方/GitHub、Kimi Blog/Moonshot，日期同义 `January 20/21`、`2026-01-20/21`，首屏；DeepSeek普通issue/PR不升级为研究事件。
- [query_2.txt](./query_2.txt)：Hunyuan Research、ZAI Research/docs、Seed，日期同义如上，空搜索结果只能限制搜索，不证明官网无事件。
- [query_3.txt](./query_3.txt)：ERNIE Blog、MiMo官网/GitHub、MiniMax英/中文Blog，日期同义如上。ERNIE结果01/15、01/29等为窗外；MiMo重复自定义指令等普通issue不当技术发布。
- [query_4.txt](./query_4.txt)：arXiv `Tue, 20 Jan 2026`/`Wed, 21 Jan 2026`+language model/transformer/agent/inference及world model/diffusion/vision language/GPU，首屏空，不能作零公告证据。
- [recovery_0.txt](./recovery_0.txt)：arXiv status/blog Jan19/MLK/holiday及历史list日期线索；Cornell主站一度502，迁移后从官方 https://blog.arxiv.org/2026/01/ 列表点击原文恢复。
- [recovery_1.txt](./recovery_1.txt)：精确OpenAI index Jan20、Anthropic Jan20/21、DeepMind20 January检索，恢复下面5项关闭事件。社区帖子只是检索噪声，不作为原源。
- [recovery_2.txt](./recovery_2.txt)：Google Blog、Meta、Qwen新站、Kimi精确日期首屏空；另做Seed Jan20、Hunyuan2026-01-20、Qwen January2026 20、Meta publications Jan20日期查漏，返回2025/2022旧条目，不挪日期入窗。

## arXiv 公告时间与查询纠偏

官方 [availability](https://info.arxiv.org/help/availability.html) §Announcement Schedule：EST20:00=UTC次日01:00=BJT次日09:00。官方 [MLK announcement](https://blog.arxiv.org/2026/01/14/attention-authors-temporary-change-to-announcement-schedule-due-to-mlk-jr-holiday-3/) L21～22（[实际返回](./holiday.txt)）明确Jan19无公告；Jan16 14ET～Jan20 14ET收到并接受的文章在Jan20公告。该次公告是本窗排除的终点。故本窗无正常arXiv新稿/替换公告批次；不以API submission日期推断early release。

曾试两条过宽API（submittedDate01/19 14→01/20 14，total241/start0/max100；01/16 19→01/19 18:59，total448/start0/max100），发现日期不是first-public后立即停止，未分页、未全量关闭、未据此生成候选。月目录cs.CL首页只暴露全月起始条目，cs.LG及cs.CL skip1150/cs.DC窗口页恢复失败；不把全月作为本窗标题查漏。由上面的官方节假日原证处理本窗announcement，而非遍历这些库存。

实际执行本窗submission元数据主题同义探测（UTC01/20 01～01/21 00:59；每组start0/max1）：

1. language model / Transformer / foundation model / LLM：total253，首条Hidden in Plain Text。
2. Agent / tool use / retrieval augmented / long context / memory：total118，首条CMind。
3. multimodal / world model / vision language / diffusion / VLA：total109，首条CARPE。
4. GPU / kernel / compiler / distributed training / inference serving / scheduling：total37，首条JAXMg。

上述数字是重叠的submission检索库存，不是当日公开家族、题摘数或候选分母。没有以title/摘要关闭这些库存，也不请求reviewer全量复核；本窗正常公告为空的原证已经足够停止。提前作者公开仍需另外的实际发布证据；当前有限官网查漏未找到此类可确定落窗的机制项。

## 贡献关闭与校准

核心/完整说明原证：[primary_0.txt](./primary_0.txt)，release说明：[recovery_1.txt](./recovery_1.txt)。身份均为官方页面标注January20，时区/时刻未核实；贡献已明确排除，所以不为了不影响处置的日期继续追查。

| 材料 | 实际位置与判断 | 层级 |
| --- | --- | --- |
| [Our approach to age prediction](https://openai.com/index/our-approach-to-age-prediction/) | How age prediction works L36～58：账户/行为signals触发未18保护、低confidence安全默认及误判Persona纠正；无公开新分类机制/阈值/评价或安全保证。读了受影响的安全core，未借成熟风险routing/申诉原理当原创贡献。08/25 EU更新是后加事件，未倒填本窗。 | 安全部署/具体贡献关闭，root全核此项 |
| [ServiceNow powers actionable enterprise AI with OpenAI](https://openai.com/index/servicenow-powers-actionable-enterprise-ai-with-openai/) | Key takeaways、Powering actionable AI workflows L22～50：商业接入、governance等描述，未给新执行机制/失效边界/对照；不能由Agent关键词准入。 | 平台/Agent，机制不足 |
| [Horizon 1000](https://openai.com/index/horizon-1000/) | title/intro：医疗部署资助，不改变模型/训练/推理机制。没有经Evaluation绕回应用。 | 领域应用范围外 |
| [Stargate Community](https://openai.com/index/stargate-community/) | 核心L24～49：容量与地方能源、社区、技能承诺，不是GPU调度/执行机制证据。 | 物理基建政策，机制不足 |
| [Voice Updates](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | #January20：指令遵循提升与重复custom instructions修复标签，无实际算法、可比较评价或新保证；age段归同家族不重复。 | 版本/修复说明，机制不足 |

root已独立校准以上5类具体关闭理由，并在日级Gate实际核上述5项官方core、六部分、有限查询/停止范围及MLK原证；安全项全核。未独立验证宽API库存、全部目录/普通issue或未知历史遗漏，作者也未逐项声称关闭这些材料。候选冻结0，Evidence采用0，Books No Change，root日级Gate通过，普通执行待办0。

## 终态保留边界

具体历史片段/日期缺口见本日报§5。原文与必要采用命题没有候选被访问问题砍掉；未确定来源片段不支持正面Coverage/Evidence、Books、zero-event或无遗漏保证。恢复只重开对应原入口/日期，不重跑整月。
