# 2026-04-18 V3 作者 checkpoint

当前状态：已完成。2026-09-27 12:14 北京时间由 root（非报告作者）实际对读本稿与停点，定点核官方公告规则、Google 四月目录及Qwen动态目录，复用未变化的有效来源记录；0确定候选、0必要Books新增、五项安全终态覆盖限制。正式README §6为日级验收入口，V3校验通过；以下作者阶段记录不覆盖当前状态。

- 窗口：`2026-04-17T09:00:00+08:00`～`2026-04-18T09:00:00+08:00`，左闭右开。
- 本轮实际检查：2026-09-27 01:48 起，北京时间；最终报告会取实际时钟。
- 已完整重读当前 AGENTS、研究/Report 合同、统一 Prompt，读取 Daily 14 来源、arXiv 路由与 ROADMAP 当前七 Part / AI for Science 暂缓边界。
- 旧 README 已原样保存在 `V2_1_README_BEFORE_V3.md`；旧 DOI-created 0 候选与 Complete 不继承，旧正文与原始证据不删除。

## 已实际检查的来源边界

| 来源 | 本轮实际入口及停止依据 | 处置与限制 |
| --- | --- | --- |
| arXiv | 官方 availability §Announcement Schedule 明确 Friday / Saturday 无常规公告；本窗对应美国 EDT Thu 04/16 21:00～Fri 04/17 21:00，不包含 Thu20:00 或 Sun20:00 批次 | 只支持常规公告批次为空；若机构发现同版本提前公开、重要安全/撤回等具体事件，按该事件定点判断，不将旧 DOI 登记为 first-public。 |
| Anthropic | 本轮 Research HTML publishedOn 邻界04/14T13:01Z（automated-alignment-researchers）→04/22T14:12Z / 14:27Z | 官方这个目录本窗无条目，不用 modified 代入公开时间。 |
| OpenAI | 官方 News RSS 实读1230项，邻界04/16T10:00Z Codex-for-almost-everything→04/20T00:00Z Hyatt；Research原入口本轮403 | RSS本窗无项；RSS不冒称Research历史分页闭合，精确历史目录缺口将隔离。 |
| Google AI | Research月份页9项，04/16→04/21跨本窗；Publications实际year参数页返回泛目录（771页）；DeepMind首页发现pagination后正在按实际href恢复 | Research Blog本窗无项；Publication目录没有本窗停点，不将全年泛目录变成逐篇审阅队列。 |
| Meta | 官方Research抽取0行后实际打开Blog，混排April08/06与July，带Next；这不是日期排序停止点 | 待有界Next/Publication检查，不能据空页或混排列表称完整无更新。 |
| Qwen | 动态官方retrieval40项 + static page_config60项（static最晚2025-12-23）；邻界04/15T10+08→04/18T10+08；组织created-desc58仓库到2023-08-03，无04/17-18新仓库 | 官网研究列表本窗无项；Max-preview在截止后1小时，不评分或扩窗。重要release补核待做。 |
| DeepSeek | 官方news本轮恢复200，所见动态04/24→2025-12/01，研究索引06/24→02/25；GitHub组织39仓库到2023-10-20 | 当前公开目录及新仓库没有本窗条目；不冒称未列作者稿皆无更新。 |
| Moonshot | 官方Blog26项最新2025-11-07；GitHub组织43仓库到2023-03-28，本窗无新仓库 | Blog历史2026覆盖仍是精确缺口，组织列表不代替Blog全覆盖。 |
| 腾讯混元 | 官方POST publicList，pageNum1/pageSize100/renderType0，totalNum9/list9；displayPublishTime邻界04/23→02/13；组织83仓库到2024-05-10 | 官网“全部”列表和新仓库本窗无项；HY-SOAR仓库created04/16T06:34Z在本窗前，不能因本次发现而改归属。 |
| 智谱 | 官方Research本轮可读15条，04/29→04/07→04/01；组织53仓库到2021-05-25 | 官网首查目录和新仓库本窗无项；重要release补核待做。 |
| Seed | 官方get_article_list_v2本轮papers page20、blog page0已真实成功，正在提取实际PublishDate及分页邻界 | 普通可执行检查，不能标外部受阻或继承相邻日结论。 |
| ERNIE | 官方Blog第一页10条，04/30→04/15→02/06，目录有2/2翻页；ERNIE-Image日历日整个04/15在本窗前 | 这段有序目录本窗无项；不重读04/15模型正文或重建早发日期。 |
| MiMo | 官网本轮Paper/Blog入口可读，组织18仓库到2025-04-26 | Paper邻界正在解析；未标日期Blog不能当完整日级覆盖。 |
| MiniMax | 本轮英文12条05/26→03/18；中文13条04/27→03/18；组织35仓库到2025-01-14；AgentTech本轮真实恢复一项2026-05-13 | 可见两语言Blog及组织新仓库本窗无项。AgentTech恢复结果与旧空页不同，应只按本轮公开目录支持的范围，不声称历史删除项不存在。 |

## 作者收口（2026-09-27 02:01 之后）

上述普通待办均已处理，正式README是最终维护入口：Seed实际papers type1 page20的20条04/20→04/16跨窗、最尾04/09；blog type2 page0/20 total95，04/23→04/09→04/01、page20已2025。DeepMind真实分页是 `/blog/page/3/`，不是无效的 `?page=3`；本轮七项April原文/已核未变日期04/30、27、23、22、15、14、2均不在本窗。Meta已读Blog两页与Publication恢复超时。MiMo Paper8项06/29→03/13，Blog无日期隔离。Qwen/Kimi release API限流后，实际官方GitHub release页均无release；Qwen当前repo跳Qwen3.8，不能据当前名字证明全部历史提交。

当前确定当窗候选0、Books新增0；不继承旧DOI-created库存，也不声称所有外部目录已经得到证明。五个精确历史覆盖gap（OpenAI Research、Google Publications、Meta、Kimi Blog、MiMo Blog）已隔离，不用于无遗漏或正面Books断言。普通作者工作已无剩余身份，下一步为非作者日级语义验收；未通过前README保持进行中，不能自行Complete。

## 12:12 续跑与作者提请验收

本轮实际重新读取AGENTS、统一Prompt、研究/Report合同全部、Daily组及arXiv路由、ROADMAP和月checkpoint最新段；固定窗口不变，不以先前稿或月总账替代规则。已经存在的本日V3记录不是旧Complete授权：只复用可核实且未受影响的实际停点，未复制旧候选/评分/全文标签。

定点再核范围：官方arXiv availability说明及EDT到北京换算；Google Research四月页9项（04/16→04/21邻界）；Qwen官方retrieval完整40项的extra.date（04/15T10+08→04/18T10+08）；混元publicList完整9项的displayPublishTime（04/23→02/13邻界）；Seed type1 page20完整20条PublishDate（04/20→04/16邻界，尾04/09）。这几个未变范围实际可读、与正式稿一致；Qwen初次传输截断后用compressed请求恢复完整JSON，不将一次读取失败冒称外部必要材料受阻。

其他已在上文具体记录的来源停点与隔离缺口没有发现失效信号，按研究合同§7复用，不再抓取全部组织/全年目录。结果仍为0确定候选、0证据/Books新增、0普通作者待办；五个覆盖gap只作为不支持覆盖断言的具名终态保留，不是Coverage通过。V3 validator与本日scoped diff检查已实际通过；作者已提请root非作者日级验收，尚未自行Complete。
