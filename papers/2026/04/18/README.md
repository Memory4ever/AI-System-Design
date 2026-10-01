# Daily Research — 2026-04-18

**规范：** V3
**窗口：** 2026-04-17T09:00:00+08:00 ～ 2026-04-18T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-27T12:14:54+08:00

## 1. 结论

在本次实际可恢复的官方窗口目录中，未发现能够确定落窗并进入贡献审阅的新增材料家族；当前确定候选为0，证据审阅和Books新增均为0。这个结果不是“互联网当天没有研究”：OpenAI Research历史分页、Google Publications日级停点、Meta混排历史目录、Kimi 2026 Blog及MiMo无日期Blog仍有精确覆盖限制，均不用于证明无遗漏。

本窗覆盖美国EDT周四21:00至周五21:00，不包含arXiv常规周四20:00公告；官方规则周五/周六无常规公告。旧报告以DataCite created日历日得到0条，不能作为这一结论的证据，本轮没有继承旧候选或旧Complete。机构发布仍独立检查：Qwen3.6-Max-Preview的官方时间为04/18 10:00，北京时间比本窗截止晚1小时，不移入本日、不评分。

来源检查已完成到具体可复查停点或隔离限制，非作者日级语义验收通过。Books判断纳入本次，但没有确定候选支持新增书稿；没有制造“已吸收语义增量”或主题相似的Existing记录。旧日报与旧证据保留于[当日保存稿](../_sources/daily-20260418/V2_1_README_BEFORE_V3.md)，本轮入口记录见[作者checkpoint](../_sources/daily-20260418/V3_REVIEW_CHECKPOINT.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方Research](https://openai.com/research/)本轮403后补[完整News RSS](https://openai.com/news/rss.xml)，实际1230项；邻界04/16T10:00Z Codex-for-almost-everything→04/20T00:00Z Hyatt，RSS本窗无项 | 受阻 | RSS不替代Research历史分页；尚无可复查该研究目录本窗停点，作为外部覆盖保留项 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)HTML实际publishedOn邻界04/14T13:01Z automated-alignment-researchers→04/22T14:12:30.673Z/14:27:03.434Z；没有落窗条目 | 已检查 | 只证明官网公开研究目录，不外推未列作者论文 |
| SRC-GOOGLE-AI | [Research四月页](https://research.google/blog/2026/04/)9项04/16→04/21跨窗；[DeepMind实际page3](https://deepmind.google/blog/page/3/)从May经April到March，七项April原文日期04/30、27、23、22、15、14、2均窗外；[Publications](https://research.google/pubs/?year=2026)实际参数页返回771页泛目录，无日级停点 | 受阻 | 两官方Blog已处理；Publication目录的历史本窗覆盖未证，不把全年列表送入全文队列 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)抽取0行后进入[Blog](https://ai.meta.com/blog/)及[Next page2](https://ai.meta.com/blog/?page=2)，分别混排04/08、04/06、July和03/27及旧项；[Publication入口](https://ai.meta.com/results/?content_types%5B0%5D=publication)恢复超时 | 受阻 | 混排列表没有可靠日期停点，不据空页或旧条目断言本窗无事件 |
| SRC-QWEN | [官方静态列表](https://qwen.ai/api/page_config?code=research.research-list)60项，最晚2025-12-23；[动态retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项，extra.date邻界04/15T10+08→04/18T10+08；组织created-desc58仓库至2023-08-03，本窗无新仓库；release API限流后[release页面](https://github.com/QwenLM/Qwen3.6/releases)实际跳Qwen3.8且无release | 已检查 | 官方公开研究列表本窗无项；repo当前重命名不冒称历史commit/release逐项闭合，不扩查普通提交 |
| SRC-DEEPSEEK | [官方news](https://www.deepseek.com/news)实际恢复200：动态04/24→2025-12-01，研究索引06/24→02/25；组织created-desc39仓库至2023-10-20，本窗无项 | 已检查 | 限该公开目录及新仓库，不外推全部未列作者稿 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)26项最新2025-11-07；组织created-desc43仓库至2023-03-28无本窗新仓库；release API限流后[Kimi-K2.5 release页面](https://github.com/MoonshotAI/Kimi-K2.5/releases)实际无release | 受阻 | 官方Blog缺2026历史停点，仓库和release列表不证明Blog覆盖 |
| SRC-TENCENT-HUNYUAN | 官方POST [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，pageNum1/pageSize100/renderType0，totalNum9/list9；displayPublishTime邻界04/23→02/13；组织83仓库至2024-05-10，最近HY-SOAR created04/16T06:34:05Z在本窗前 | 已检查 | 公开“全部”列表本窗无项；repo created仅仓库事件，不回拨论文公开时间 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)可读15条，04/29→04/07→04/01；[release notes](https://docs.z.ai/release-notes/new-released)日期06/16→04/07→02/12；组织53仓库至2021-05-25 | 已检查 | 当前这三个目录本窗无可见项，不冒称作者全部未列稿无更新 |
| SRC-BYTEDANCE-SEED | 官方[get_article_list_v2](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20)，header x-tt-locale US，papers page20的20项由05/13至04/09；PublishDate邻界04/20→04/16；blog type2 page0/20 total95，从04/23→04/09→04/01，page20已2025；组织63仓库至2024-04-19无本窗新仓库 | 已检查 | 官网PublishDate为日历桶，不改名精确首发；邻界不与本窗相交，所以不复审窗外论文或旧Seedance卡 |
| SRC-BAIDU-ERNIE | [官方Blog第一页](https://ernie.baidu.com/blog/zh/)10项，04/30→04/15 ERNIE-Image→02/06，尾项已到2025-11并带下一页；本页已越过左界，可见邻界没有本窗项 | 已检查 | ERNIE-Image整天04/15在本窗前，不重建其早发日期或重复深读正文 |
| SRC-XIAOMI-MIMO | [官方首页](https://mimo.xiaomi.com/)Paper8项06/29→03/13→02/03，Blog14项没有历史日期；组织created-desc18仓库至2025-04-26，本窗无新仓库 | 受阻 | Paper/新仓库已处理；无日期Blog无法作历史本窗覆盖证据 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)12项05/26→03/18；[中文Blog](https://www.minimax.cn/blog)13项04/27→03/18；[Agent Tech](https://agent.minimax.io/docs/techblog)本轮实际恢复一项2026-05-13；组织35仓库至2025-01-14 | 已检查 | 限官网当前可见两语言目录/AgentTech索引与新仓库；不声称历史未列条目绝不存在 |
| SRC-ARXIV | [官方availability](https://info.arxiv.org/help/availability.html)§Announcement Schedule/2026 holidays；本窗EDT Thu21:00→Fri21:00不含常规公告；bounded search针对17/18 Apr Announced+language model/Transformer/inference及17Apr withdrawal无结果 | 已检查 | 无搜索命中不是全互联网召回；正常公告规则不排除具体提前公开/异常恢复线索，发现后只重开该项 |

GitHub补检仅上述八机构官方组织created-desc各100上限，实际均不足100且停止到历史旧仓库；不扫描每周源，不逐个普通PR/commit建立审阅队列。命中数是目录项/仓库，不是当天论文数。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

本次没有能够确定落窗的贡献候选。窗外发布不写零分、不放入本窗候选；来源受阻也不伪装为零命中。没有完整摘要/全文审阅队列，不能以旧0条库存声称全量语义验证。

## 4. 证据与知识整合

### 公告窗口与旧库存的边界

arXiv官方说明新提交、replacement、withdrawal和cross-list通过公告过程公开；永久ID随公告赋予，提交和标识月可能不同。这里只用官方正常周历判断本窗不包含常规批次，不把Submitted、OAI当前datestamp、DataCite created/Updated等同first-public。明确来源线索可另行公开的事件仍按实际时间判断。

旧README只含DataCite-created的SRC-ARXIV收据，缺13个机构来源，且使用UTC日历proxy。其0/Complete不能直接得到V3验收。本轮保留旧材料，但没有从旧Weekly或旧候选反推本窗。

### Books决定

没有确定的当窗候选或支持新增长期命题的证据，本轮不修改Books，不将“模型/推理相关”拼成已有覆盖证明。必要的Books判断与非作者复核均已完成；若以后恢复的是窗内具体材料，只重开其贡献/证据/owner比较，不顺带重跑整月。

## 5. 缺口与下一步

普通可执行工作为0，非作者日级复核已完成。下列五项为终态保留项，不支持正面证据、Books 或无遗漏断言；定点重开条件为各项列出的官方历史窗口材料，而非重复已有失败请求：

- **OpenAI Research**：缺本窗可复查历史Research分页/清单；官方RSS已实际处理但只能证明RSS范围。恢复材料为官方历史列表及其日期停点，不以重试同一个403入口循环补偿。
- **Google Publications**：year参数实际返回泛目录而非日级列表；缺本窗公开记录/可靠发布日期和有限停点。两官方Blog结论可以保留，但不能代替Publication覆盖。
- **Meta**：Research空抽取、Blog混排和Publication超时不能证明本窗完整。恢复官方可靠排序/历史分页或本窗清单后，只复查该时段，不扩扫历年论文。
- **Kimi Blog**：现26项停止于2025，不能证明2026历史完整；需官方2026历史Blog目录/可验证本窗发布。组织与当前release结果只保留其实际范围。
- **MiMo Blog**：14个未标日期入口没有本窗停点；需官方原发布时间或历史列表。Paper8项和组织新仓库结论不受此影响。

以上是不能用于覆盖断言的本窗终态隔离，不是“已经完整覆盖”的证据，也不是尚未阅读的普通工作；非作者复核确认其隔离与恢复条件充分。

窗外线索（不阻塞本窗）：Qwen3.6-Max-Preview官方extra.date=`2026-04-18T10:00:00+08:00`，归04/19默认Daily窗口；本次不审其能力数字或追溯全部版本。HY-SOAR仓库创建早于本窗，仅作已存在家族线索，不按发现日重计。

## 6. 复核

复核者：root（非本日报告作者）。

结论：通过

root 完整对读本稿14来源的实际停点与作者新复核记录，并定点重新打开官方 arXiv 公告规则、Google Research 四月目录和 Qwen 官方40条动态目录：EDT周四21:00～周五21:00无常规批次；Google邻界04/16→04/21不相交；Qwen原extra.date的04/18 10:00在截点后，不能放入本日。混元全部9项、Seed20项及其他未变化的有效停点按实际记录复用，没有重新扩全年目录、附件或全组抓取。

复核区分了无确定候选与五处未证明的历史覆盖，不把空响应或旧DOI-created 0条当召回证据，也不制造主题相似的Existing。无必要Books修改的处置成立，五项限制保持具名、安全终态及有限重开条件，普通工作为0。格式/一致性与scoped diff检查通过不是此语义判断的依据；未复现实验，未stage/commit/push。
