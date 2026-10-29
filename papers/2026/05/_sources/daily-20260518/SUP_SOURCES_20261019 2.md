# 2026-05-18 Daily 来源遗漏增量补查

## A1. 本地初态与边界

作者：`/root/may18_supp_author`；独立复核：`/root/may18_supp_reader`。本轮执行时间为 2026-10-19（Asia/Shanghai），不移动历史窗口。

已完整重读当前 AGENTS、Research/Report 合同、统一 Prompt、来源说明/每日组/arXiv主题与恢复，以及 ROADMAP；本日无既存 SUP 停点。LEARNING_STATE 月度路由只用于确认279日报补查范围，不继承他日论文池。当前任务不是仅报告。

真实运行前本地 README 无该路径 staged/unstaged 修改；已保存 [baseline-before-supplement-20261019.md](./baseline-before-supplement-20261019.md)，SHA256 `8bb461ee4c1f8cc1988abcc67c2ee71b9c8ba63abe91643ab5e7a08f485eb07e`。原64候选整行、日期评分、原小时窗 `2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00`、有效证据和连续原§4保持。旧537等统计只描述历史批次，不重新用当前合同审查整批。新增仅检查 2026-05-17 北京自然日。

只写本日 README、本文件及必要原件；reader独写 SUP_REVIEW；LEARNING_STATE/root及共享Books不由本作者未经协调写入。不扫描Weekly组，不扩Live/2025，不stage/commit/push。

## A2. 到期每日来源与实际停止

以下是本轮05-17补充窗结果，覆盖/受阻不继承原报告完成标签。所有宽目录只用于有限日期导航，未扩成逐条深审队列。

| 来源 | 实际检查/停止位置与原件 | 结果与边界 |
| --- | --- | --- |
| SRC-OPENAI | Research→index；官方RSS原始XML1299条仅解析May10–22 pubDate相邻段，[SUP_ROUTE_0](./SUP_ROUTE_0_20261019.json)，05-16 Malta→05-18 Dell；[状态事件](https://status.openai.com/incidents/01KRP6FM6HSKWB3MS1EJTY6AT4)全部3更新，原件[WEB_D](./SUP_WEB_D_20261019.json) | RSS无05-17研究新事件；status有恢复信号但无机制/根因/新保证，按A3明确排除，不赋新候选。 |
| SRC-ANTHROPIC | Research HTTP嵌入完整publishedOn五月字段，[EXTRACT_0](./SUP_EXTRACT_0_20261019.json)；05-14T17:06:12.172Z→05-22T17:00/18:00Z | 已检查本目录相邻段，无05-17事件；不用createdAt/updatedAt判断发表。 |
| SRC-GOOGLE-AI | DeepMind publications page1的30条已跨过May28→May6→Apr25，见[WEB_D](./SUP_WEB_D_20261019.json)，止page1；Google Research pubs/2026及blog定点恢复见[WEB_A](./SUP_WEB_A_20261019.json)、[BOUNDED_2](./SUP_BOUNDED_2_20261019.json)、[WEB_F](./SUP_WEB_F_20261019.json)、[WEB_G](./SUP_WEB_G_20261019.json) | DeepMind该目录无05-17；Google Research当前出版目录只有年份，blog无可用五月分页，日期主题搜索无具名新命中；Google子入口历史日级召回受阻，不能当完整零命中。 |
| SRC-META-AI | Research直取空内容→官方results page2/filtered及GIM详情定点恢复，见[SEARCH_B](./SUP_SEARCH_B_20261019.json)；相邻May19/GIM17/May12，止越过日期后；另TransText精确页见[WEB_G](./SUP_WEB_G_20261019.json) | GIM目录05-17/详情05-18冲突继续隔离，不入新候选；TransText有April14官方正文，非May17首次公开，不把宽列表错配当新事件。 |
| SRC-QWEN | qwenlm旧站明示迁移至qwen.ai；新/research和/blog web与HTTP均仅shell，见[WEB_B](./SUP_WEB_B_20261019.json)、[RECOVERY_3](./SUP_RECOVERY_3_20261019.json)、[WEB_F](./SUP_WEB_F_20261019.json)；新站精确May17主题检索未得具名事件 | 新站历史日期列表受阻；旧2025目录不能证明2026五月覆盖。没有把空响应记零命中。 |
| SRC-DEEPSEEK | Research首页→news，HTTP公开研究索引和动态列表见[RECOVERY_2](./SUP_RECOVERY_2_20261019.json)；动态04-24→09-10，研究02-25→06-24，止越过日期后 | 已检查此官方发布切片，无05-17事件；不把未来当前型号覆盖历史。 |
| SRC-MOONSHOT | Kimi blog已读完整旧目录；GitHub官方org created-desc一页42仓库到底，见[FINALNAV_1](./SUP_FINALNAV_1_20261019.json)；仅做日期导航，不认created_at为公开；Kimi-K2.5 release页明确无release，见[WEB_H](./SUP_WEB_H_20261019.json) | 未得05-17具名技术事件；旧blog停2025，仓库列表不是完整历史发布索引，历史技术博客覆盖保留，不宣称全组织零事件。 |
| SRC-TENCENT-HUNYUAN | Research初web超时/HTTP动态壳；按清单实际浏览器尝试73秒超时并reset；随后从前端绑定的公开publicList恢复：正确api.hunyuan host、renderType0、page1/pageSize50，中文11/11与英文9/9全部读完，见[FINALNAV_0](./SUP_FINALNAV_0_20261019.json)、[HUNYUAN_PUBLIC](./SUP_HUNYUAN_PUBLIC_20261019.json)；中文显示04-30→05-21 | 已检查当前中英文“全部”目录，不取createdAt做发表；无05-17字段事件。前端配置displayPublishTime和publishedAt均保留，不把回填值改写成真实首次公开时刻。 |
| SRC-ZAI | Research当前page1中文目录，04-29 Scaling Pain→05-20 ZCube，见[WEB_C](./SUP_WEB_C_20261019.json)；止跨过日期后 | 已检查此目录相邻段，无05-17事件。 |
| SRC-BYTEDANCE-SEED | Publications原page1→前端get_article_list_v2同绑定API paper offset20/count20第二页，见[DETAIL_0](./SUP_DETAIL_0_20261019.json)、[PUBLIC_0](./SUP_PUBLIC_0_20261019.json)；page1末05-26→page2首05-16 Charon。Blog同API type2/page0/count20实际15条，06-19→04-23，见[DATA_2](./SUP_DATA_2_20261019.json)；下页全更早即停 | 已检查论文/技术博客跨窗邻接；没有05-17事件。只有日期导航，不把整个246论文/96博客当筛选队列；未用UpdateTime代替PublishDate。 |
| SRC-BAIDU-ERNIE | 技术博客page1最新05-09→04-30→04-15，继续已越过日窗，见[WEB_C](./SUP_WEB_C_20261019.json)；止page1，不扫2025 page2 | 已检查当前目录，无05-17条目，不外推不可见历史删除项。 |
| SRC-XIAOMI-MIMO | Paper完整8项日期03-13→06-29，Blog主页15卡无日期且有More；有限打开/blog实际为2025-12-16 Flash release而非归档，见[WEB_C](./SUP_WEB_C_20261019.json)、[WEB_F](./SUP_WEB_F_20261019.json)、[WEB_H](./SUP_WEB_H_20261019.json) | Paper目录无05-17；Blog历史日期/More归档未恢复，独立隔离，不用Paper邻接授Blog无命中。 |
| SRC-MINIMAX | 英文Research 03-18→05-26/27，中文04-27→05-25，均当前全目录；Agent Tech Blog仅09/19、09/22、10/08三篇，见[WEB_E](./SUP_WEB_E_20261019.json) | 已检查三技术入口，无05-17事件；中英同家族不同日期都保留且均窗外，不为此无限精确日期追索。 |
| SRC-ARXIV | [官方日程](https://info.arxiv.org/help/availability.html)实际读取，见[WEB_D](./SUP_WEB_D_20261019.json)；BJT05-17对应EDT05-16 12:00～05-17 12:00，常规无公告；new/replacement/withdrawal/crosslist同受该日程。CL五月目录旧格式404/现代格式超时，见[BOUNDED_1](./SUP_BOUNDED_1_20261019.json)、[WEB_F](./SUP_WEB_F_20261019.json)；已有限按日期+LLM/Transformer/Agent/world-model主题搜索与官方status日期检索，见[SEARCH_B](./SUP_SEARCH_B_20261019.json)、[WEB_E](./SUP_WEB_E_20261019.json) | 可确认通常无本日批次，但历史实际日标题/延期公告未恢复，不能把日程或当前搜索零命中当完整覆盖。CL/LG/DC/AI及CV/RO、AR/PL、OS/PF、IR/MA十二主题入口均按同一无常规批日期边界限定，未扫全年或把宽表成队列；历史异常公告与新命名标题补检保留。 |

## A3. 首批准入校准集合

本轮尚无确认窗内、通过贡献筛选的新候选。现有具名线索逐一如下，交独立reader校准，不用零候选逃避信号检查：

1. **OpenAI GPT5.5 Performance Degradation**：实际全读Investigating/Monitoring/Resolved三更新。仅报告部分用户表现下降、已缓解、恢复；没有根因、调度/模型机制、成立边界或可重用安全/正确性修正，不因“恢复/安全”标签自动深入。即使恢复落05-17，也不改变本项目具体解释或设计；不准入、不评分。日期页面时区未披露，不为不影响排除的字段另建缺口。
2. **Meta GIM**：完整官方题摘确提出通过多认知操作而非专业知识提高难度、2PL IRT与污染诊断的潜在评价增量，不能按benchmark标签排除。但同一官方家族results标05-17、detail标05-18，原报告已隔离；本轮重现同冲突，没有新可用日期证据或具体修订信号，仍不记确定当窗候选、不做Books。不是“无贡献”。
3. **TransText / arXiv:2603.17944**：完整题摘的Alpha-as-RGB、latent spatial concatenation避免重训VAE是实际机制，不按字形应用硬排；但精确Meta详情与作者页已有04-14正文，搜索results错配的05-17不是首次公开，未见本日重要修订信号。只关闭May17事件，保留真实旧归属恢复线索，不扩本日。
4. **邻接条目**：OpenAI Malta05-16、Seed Charon05-16、Hunyuan Hy-MT2 05-21、ZCube05-20、MiMo ARL-Tangram03-13/MOPD06-29、MiniMax sparse-token05-25/26、Mavis04-27/05-27均窗外；无新本窗事件，不搬旧日、不新评分，不冒充已证贡献排除。

此前64旧候选只用于身份去重/冻结，未重读其全部证据。没有新增候选，故新增必要Source/Books逐项审阅为0，不对旧31/33结果重背书或重写共享Books。

## A4. 精确保留项与重开条件

普通研究/Books可执行项：无。reader R5 Source/准入安全终态与R6实际DAY通过；报告已保存完成态，提交最小actualFINAL读回。以下不是普通待办，经过有限恢复后的外部保留项不支撑正面Coverage/Evidence、Books或“无遗漏”：

- **GIM日期资格**：[官方results](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2&sort_by=most_recent)与[精确详情](https://ai.meta.com/research/publications/gim-evaluating-models-via-tasks-that-integrate-multiple-cognitive-domains/)矛盾；需能统一同家族公开日的官方发布记录、带时区精确事件或早正文。回到本记录A3第二项，不重扫Meta全站。
- **Google Research历史日目录**：当前pubs仅年份、Blog现页未涵盖五月且日期参数不可取；需2026-05-17主题检索结果/官方归档页或精确当日论文原始发布。只重开Google子入口；DeepMind邻接不受影响。
- **Qwen新站历史列表**：旧站2025停止且新站research/blog只动态shell，HTTP/官方日期搜索未恢复真实分页。需新站五月官方内容列表/日期数据或具名May17原文；不把空页面作“无发布”。
- **Kimi历史技术博客段**：平台blog停2025；org一页仓库身份和K2.5无release只能关闭这些切片，不证明历史博客齐全。需五月官方技术博文索引或具名当日记录，定点重开此段。
- **MiMo Blog历史日期归档**：Paper邻接有效，Blog卡片无日期且More不可用作完整归档；/blog是旧Flash单篇。需五月Blog官方列表或卡片实际日期链接，只补此段。
- **arXiv实际日公告/标题补检**：日程无常规批但历史CL月表404/timeout、官方历史规则GitHub访问cache miss，status日期搜索未取得具体历史公告；需May17实际公告/延期说明，或当日十二分类主题标题片段。没有具名May17拟入选论文，不从邻日Submitted或DataCite created推日期，不建立全月文献恢复队列。触发时只恢复具名异常/受影响主题。

同日已有合格来源片段不因这些缺段推倒；本次不预支“14源全部覆盖通过”。

## A5. 合并与限定检查（进行态）

2026-10-19T11:08:47+08:00 已将补充窗、授权/基线、14源实际范围与停止、零新增、六项精确保留及本轮复核状态合入原六部分。原§4未添加或改写任何字符；本轮没有需新增Evidence/Books的小节，也没有实际Books写入。

- 原64候选整行均在当前正文中恰好一次；连续原§4 `162931` 字符整块恰好一次；原小时窗口与baseline SHA256一致。
- `python3 scripts/validate_research.py --report papers/2026/05/18/README.md` 通过。初次未标正确冻结字段曾报旧候选跨补充窗，改用现有 `冻结候选日期` 指向同日真实baseline后通过；没有改公共脚本或旧候选日期。
- README与本SUP共111个本地引用路径检查零missing；新增SUP JSON原件全部可解析，保留失败恢复的HTTP403为明确失败数据，不用空响应证明覆盖。
- README与本日_sources限定unstaged及cached `git diff --check`均通过；没有检查或改写整个并发index，也不声称全仓clean。
- reader R1–R4实际子集层可复用；已请求最后Source/准入/DAY，保存完成态与actualFINAL仍普通待办，未提前填通过。

## A6. reader DAY通过与保存完成态

独立reader R5/R6已实际通过最终Source/准入安全终态及六部分DAY；包括全部拟入选0、具名信号3项与来源/主题分层邻接样本，并实际复算原64行/连续原§4、78+33本地引用、V3与限定working/cached检查。没有普通Source/Books对象，新增0且共享Books未写。

本轮已将README状态、§1、§5、§6和A4更新为完成态，原六项外部保留明确继续隔离。A5是此前进行态的真实检查，不抹除旧失败或预支验收；保存后交reader只核行政差额与最终磁盘字段，不第三遍来源。actualFINAL尚待reader实际读取后另记，不在此代填。
