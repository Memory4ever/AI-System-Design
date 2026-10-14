# Daily Research — 2026-04-12

**规范：** V3
**窗口：** 2026-04-11T09:00:00+08:00 ～ 2026-04-12T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T15:37:13+08:00

## 1. 结论

当前可确认的本窗贡献候选为 **0**，不是从旧稿的零候选或 DOI 注册日倒推。按十四个每日来源检查，本窗不含 arXiv 常规公告槽；旧 submitted-window 库存中的十二个研究信号，其版本元数据与后续公告链指向 04-14，而非 04-12。原始证据保留，等待真实归属日处理，不在今天重复评分、审稿或写 Books。

机构目录中未发现能够确认落窗的新贡献事件；若干历史目录的完整性仍不能恢复，已在第5节隔离，不以“目录没显示”宣称全网零遗漏。由于本窗没有确定候选，Evidence 和 Books 的当窗集合均为空，书稿无新增修改。非作者复核通过，普通待办为0；完成仅指本次合同允许的终态，不表示外部目录缺口已恢复。

[旧V2.1稿](../_sources/daily-20260412/V2_1_REPORT_ARCHIVE.md)保留仅作溯源。其 created-day proxy、只列一个来源和旧完成标签均不作为本轮验收依据。

## 2. 来源覆盖

机构目录未变化的实际读取结果复用[相邻日期的来源停点](../_sources/daily-20260411/v3-reopen-notes.md)，只复用已跨过本窗的元数据范围，不继承相邻日报状态。root另核 arXiv 公告规则、当窗OAI缓存、十二个v1元数据、七个官方组织仓库列表及下表注明的当前入口；不扫描每周来源或普通commit。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | News RSS1230项的已核历史日期，04-10T00Z→04-13T06Z跨过本窗；本次直取RSS为403，News首屏及Research历史分页不足以覆盖April | 受阻 | RSS现行失败不推翻既有日期证据；历史Research目录缺口见第5节 |
| SRC-ANTHROPIC | Research嵌入170项publishedOn，04-09T16:34Z→04-14T13:01Z跨窗；不是lastmod | 已检查 | 所检查目录未列本窗事件，不代表所有机构作者稿 |
| SRC-GOOGLE-AI | April Research Blog实际9项，04-09→04-13；DeepMind selected264项所选目录04-22→03-22跨窗；未把全年pubs扩成队列 | 受阻 | Publications历史日级目录停点未恢复 |
| SRC-META-AI | Research本次仍0可读行；可复用Blog04-08→04-06邻域，无本窗日期项 | 受阻 | 不把空Research响应算零，缺历史Publications |
| SRC-QWEN | 官方动态40项及静态60项；动态04-02T04+08→04-15T10+08；QwenLM58仓库全部公开创建元数据无本窗新建 | 已检查 | 新建仓库检查不代表所有旧仓库commit |
| SRC-DEEPSEEK | 本次News可见research06-24→02-25，动态04-24→2025-12；API Change Log同样04-24→2025-12，跨过本窗 | 受阻 | News“查看全部”历史完备性没有恢复；不声称首屏全集 |
| SRC-MOONSHOT | Platform Blog末端2025-11，KimiCLI已核release1.31.0=04-10T14:45:26Z早于本窗；MoonshotAI43仓库创建元数据无本窗项 | 受阻 | 2026年April完整Research/Blog目录缺口 |
| SRC-TENCENT-HUNYUAN | 官方publicList page1/100，total9/list9；displayPublishTime04-23→02-13；Tencent-Hunyuan83仓库创建元数据无本窗项 | 已检查 | 无当窗可见事件，不扩扫旧commit |
| SRC-ZAI | Research日期04-29→04-07→04-01；release目录04-07→06-16；zai-org53仓库创建元数据无本窗项 | 已检查 | CMS更新时刻未用作首发 |
| SRC-BYTEDANCE-SEED | 官方papers type1页0/20/40，04-10T16Z→04-12T16Z跨本窗；Blog type2页0/20，04-08T16Z→04-22T16Z；ByteDance-Seed63仓库无当窗创建 | 已检查 | PublishDate是目录字段，未冒充外链论文首发；有界停点非全部242论文全文 |
| SRC-BAIDU-ERNIE | Blog04-15→02-06并已到2025；唯一release=2025-06-30T01:15:24Z | 已检查 | 无当窗可见事件，不扫普通PR |
| SRC-XIAOMI-MIMO | Paper八项06-29→03-13；XiaomiMiMo18仓库创建元数据无本窗项 | 受阻 | Blog卡片未恢复历史发布时间 |
| SRC-MINIMAX | 英文目录05-26→03-18，中文04-27→03-18；MiniMax-AI35仓库创建元数据无本窗项；CLI26条release由apr02独立核完，本窗0，邻界v1.0.7=04-10T08:31:19Z、v1.0.8=04-16T19:13:05Z | 受阻 | Agent TechBlog现行文档缺历史目录/日期；release检查不替代此缺口 |
| SRC-ARXIV | [公告规则](https://info.arxiv.org/help/availability.html)无周五/周六20ET槽：前槽北京04-10 08，后槽04-13 08；04-12的cs/stat/eess OAI缓存均无header；旧十二信号v1必要日期核查见第4节 | 已检查 | 只说明常规公告及可读历史记录；不保证不存在表外早发或未留存异常事件 |

七个组织列表均少于100条，page1已读完公开新建仓库元数据。没有因此检查其全部代码或认定release零更新；没有已发现的重要release线索被普通commit替代。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

本窗没有可确认落窗的贡献候选；不是零分，也没有把窗外材料改成“已有审阅的重复项”。不沿用旧十二项的评分或Books结论。

## 4. 证据与知识整合

### arXiv窗口与旧库存纠正

[官方规则](https://info.arxiv.org/help/availability.html)区分Submitted与公告：最终ID随公告分配，常规新稿、replacement、withdrawal均随公告公开。04-11星期六至04-12星期日北京时间09点的窗口不含常规公告。缓存OAI无header是辅助范围记录，不是对表外公开的保证。

旧 `screening-ledger-final.json` 有207个submitted-window身份，范围为Submitted/v1 04-11T01:02:47Z～04-12T00:52:27Z；它不是当天207篇公开论文。十二个旧信号 `09970/09975/10015/10027/10044/10096/10152/10180/10235/10311/10352/10390` 已逐项重取[官方DOI元数据](https://api.datacite.org/dois/10.48550/arXiv.2604.09970)：各v1 Updated为04-14T00:17:35Z～00:49:46Z，与ID批次及公告节奏共同指向后续公开批次，不支持本窗。Updated本身仍不是公告时刻；created也没有被换名为first-public。版本与既有方法笔记保留在原目录，待04-14作者结合公告链核验真实owner再判断贡献，不能据此次元数据核查宣称十二篇全文审阅完成。

剩余旧库存只是宽列表恢复线索，不因文件存在就形成207项必须在本窗重读的工作量；其旧通用closure与Books状态均不继承，也没有在本次宣称195项逐项复核通过。若得到本窗表外早发/重要修订证据，只重开相应家族。

### Books判断

本次没有可采用的当窗证据，故没有新增Books写入，也不以旧主题相似性作Existing Coverage。此前其他日期的书稿与证据保持原样；此处无修改不意味着否认十二个窗外信号的潜在贡献。

## 5. 缺口与下一步

本窗已隔离的外部缺口均为终态保留项，不支持正面证据、Books或无遗漏断言；取得指定材料时只重开对应来源/家族，不扩扫全月：

- **SRC-OPENAI历史Research目录**：[Research](https://openai.com/research/)。现行首屏与RSS不能独立证明April研究全集；需要覆盖04-11～04-12的官方历史分页、feed或已保存的dated列表，才能恢复该子入口的覆盖判断。
- **SRC-GOOGLE-AI历史Publications**：[Publications](https://research.google/pubs/)。当前年级facet不能还原日级停点；可接受带首次公开日期与时区的官方导出或原始发布目录。Blog与selected停点只支持各自范围。
- **SRC-META-AI Research/Publications**：[Research](https://ai.meta.com/research/)。当前空解析不能判零；需要可读官方目录/HTML、对应历史快照或逐篇原始first-public链接，恢复本窗发现判断。
- **SRC-DEEPSEEK News“全部”**：[News](https://www.deepseek.com/news/)。当前首屏与Change Log仅覆盖已展示范围；需要官方全部历史列表/接口证明该研究子目录的April范围，不拿其他日期材料补充本窗。
- **SRC-MOONSHOT April研究目录**：[Platform Blog](https://platform.kimi.com/blog)。可见末端2025-11及仓库新建/release局部检查不能证明2026年April全集；需要官方dated Research/Blog列表或对应原始发布。
- **SRC-XIAOMI-MIMO Blog日期**：[MiMo](https://mimo.xiaomi.com/)。Paper目录不能代理无日戳Blog；需博客原始发布时间/时区及April条目列表，届时定点筛选。
- **SRC-MINIMAX Agent TechBlog历史目录**：[TechBlog](https://agent.minimax.io/docs/techblog)。现行llms索引不提供April发布日期；需官方历史目录或文章first-public字段，不以文档当前可读性当本窗事件。

**窗外恢复线索，不阻塞本窗：** 上述十二个arXiv信号交04-14核验；尚未在该日处理完，不冒称已审重复事件。其余旧submitted库存按真实owner再定位，不使用DOI-created日历日回拨。本窗普通可执行待办为0。

## 6. 复核

复核者：apr02（非作者）。
结论：通过

apr02实际重读十四行范围和七项隔离边界，复核已读取且跨窗的机构目录，独立重取十二个exact-v1 Updated、检查旧207项库存范围、三类OAI noRecordsMatch及官方周末公告规则，并补核MiniMax CLI26条release。确认没有把Updated/created冒充首发、没有宣称207项逐摘要或十二项全文审阅、没有因空候选跳过必要Books写入。未独立重取七组织全部仓库列表，不保证全网或异常早发零遗漏；没有复现实验。日级语义复核与scoped validator均通过，必要Books修改为空集；不stage、commit或push。
