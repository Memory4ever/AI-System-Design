# 2026-04-21 来源与首批准入独立校准

复核者：`/root/apr01/apr21_source_audit`；报告作者：`/root/apr01`。检查日期：2026-09-27。
窗口：`2026-04-20T09:00:00+08:00` ～ `2026-04-21T09:00:00+08:00`。

本轮只校准14个每日来源的实际边界及首批35家族中15个代表性完整题摘，不重抓1,260身份库存、不冻结分母、不验收整日Gate，不写Books、README或共享checkpoint。完整读取当前AGENTS、研究合同、Report合同、统一Prompt及来源清单每日组/arXiv路由，核对ROADMAP七Part与相关owner。已有Apr18相邻时段记录只用于复用未变入口边界，不把Apr18窗口结论移植成Apr21结论。遵循独立反证复核思路；这是非交互有界子任务，未追加跨模型调用或递归复核。

## 1. 来源覆盖校准

下表区分本复核实际打开/解析的原始入口与作者已有记录的复用，不把“检查过官网”解释为历史完整覆盖。建议作者将实际停点与隔离限制写入当日正式六部分报告；本表不是另一套完成收据。

| 来源 | 本复核实际检查及可复用边界 | 判断与修正 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)与[Research index](https://openai.com/research/index/)本轮均可读；index首屏9项止于2026-08-18，带Load more，未取得4月历史停点。另实际解析[News RSS](https://openai.com/news/rss.xml)1230项：04/20T00Z Hyatt窗外，04/21T00Z Codex enterprises窗内，04/21T12Z Images2.0窗外。作者已读取Codex企业合作核心说明并明确前分母关闭。 | **修正访问描述**：不是所有Research当前仍403，而是4月历史分页覆盖未闭合；RSS只支持其目录范围。Images2.0不移入截止09:00前窗口。历史覆盖保留项继续隔离，不循环重试或扩扫全年。 |
| SRC-ANTHROPIC | 实际读取[Research](https://www.anthropic.com/research)HTML并解析publishedOn；04/14T13:01Z与04/22T14:12:30.673Z、14:27:03.434Z邻界仍存在。 | 支持该公开Research目录本窗无可见条目；不外推所有未列作者论文。 |
| SRC-GOOGLE-AI | 实际读取[Research四月页](https://research.google/blog/2026/04/)9条及[DeepMind真实page3](https://deepmind.google/blog/page/3/)April条目。ReasoningBank博客04/21，作者已核链接2509.25140并关闭重复披露；本复核没有重复审其旧全文。DeepMind七条具体原文日期复用作者已读未变记录04/30、27、23、22、15、14、2，本轮只核目录身份。Publications year查询本轮网页工具不可取；已有作者实测为771页泛目录而非日窗停点。 | 两Blog按实际目录处理；Publications历史覆盖限制保留。不能将Google全年论文目录纳入当窗逐项队列，不能把Blog覆盖冒称Publication覆盖。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)本轮再次得到0行；复用作者实际Blog两页混排April/July、Publication超时记录，不据空抽取重写零命中。 | 精确历史研究目录保留项成立；未取得可靠本窗排序/分页。 |
| SRC-QWEN | 实际解析[动态文章API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)extra.date，04/18T10+08与04/22T10+08邻界；旧static60项只复用作者记录，未再全抓。 | 支持动态文章目录本窗无项；组织artifact的创建/发布历史另有下述隔离限制，不据当前repo名称判断过去release。 |
| SRC-DEEPSEEK | 实际读取[news](https://www.deepseek.com/news/)当前动态04/24→2025-12-01与研究06/24→02/25邻界。 | 支持这两个可见官方目录本窗无项；不外推未列稿/全部commit。 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)实际26条、最新2025-11-07；组织网页本轮可读但无本窗创建/发布停点。 | 2026历史Blog覆盖限制仍在；已有K2.5 release空列表只证明那个项目当前可见release，不能补齐所有2026研究。 |
| SRC-TENCENT-HUNYUAN | 官网网页工具超时后实际POST[publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，pageNum1/pageSize100/renderType0，totalNum9/list9；displayPublishTime有Hy3 preview04/23与此前RLVR02/13，另Real life04/30，均不落窗。只解析身份/日期，不将signed资源URL写入记录。 | “全部”公开列表可定点处理，不把空网页当无更新。组织artifact缺口单列；paper事件仍独立日期去重。 |
| SRC-ZAI | 实际读取[Research](https://www.zhipuai.cn/zh/research)与[release notes](https://docs.z.ai/release-notes/new-released)；复用Research邻界04/29→04/07与本轮release notes06/16→04/07→02/12。 | 支持可见目录本窗无项；作者未列稿与组织artifact不被这些目录自动覆盖。 |
| SRC-BYTEDANCE-SEED | 实际解析[官方papers API page20](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20)，20项、ID1635 PublishDate=1776614400000；作者已核其2604.18292链接。Blog type2 page0/20邻界04/23→04/09→04/01复用作者记录，不重建全目录。 | Agent-World目录日历桶与arXiv v1Updated02:14Z不够单独证明截点前公开；应保持精确日期消歧，不列确定当窗候选。不能将PublishDate午夜伪装实际首发时刻。 |
| SRC-BAIDU-ERNIE | 实际读取[Blog第一页](https://ernie.baidu.com/blog/zh/)10条与下一页提示；04/30→04/15→02/06邻界，末尾已2025-11。 | 本页越过左界，可见Blog无本窗项；不用重读已窗外ERNIE-Image。 |
| SRC-XIAOMI-MIMO | 实际读取[Paper/Blog](https://mimo.xiaomi.com/)：Paper8项06/29→03/13→02/03，Blog14入口无日期。组织页18条无created字段。 | Paper目录范围可处理；Blog历史日期和artifact历史各自隔离，不能用Paper无项补成全源无项。 |
| SRC-MINIMAX | 实际读取[英文Blog](https://www.minimax.io/blog)，05/26→03/18邻界未变。中文13项04/27→03/18、AgentTech05/13单项复用作者已有实际原目录记录，本复核未重读二者全文。 | 可见官方目录停点可复用；组织artifact仍受下述限制，不声称被删除历史条目不存在。 |
| SRC-ARXIV | 实际读取[availability](https://info.arxiv.org/help/availability.html)§ID assignments/Announcement Schedule/2026 holidays，Monday20:00 EDT对应04/21 08:00北京时间，04/20非列出holiday。读取原库存指定15个完整题摘，不重抓全列表。 | 1,260身份与577个早Updated均不是确认当窗分母。公告规则支持槽推断，不能仅以Submitted/Updated或当前OAI datestamp替代单项公开批次组合。本轮未验收所有候选日期或withdrawal状态。 |

### GitHub网页有界补偿的终点

作者已经两次有界API查询八个每日机构组织均403。独立复核实际打开以下官方组织网页一次，并为抽取字段进行一次同入口有限复查：
`QwenLM`、`deepseek-ai`、`MoonshotAI`、`Tencent-Hunyuan`、`zai-org`、`ByteDance-Seed`、`XiaomiMiMo`、`MiniMax-AI`。
入口统一为 `https://github.com/orgs/<org>/repositories?type=all&sort=created`。

网页均200且可取orgReposPageRoute，但这不是API创建排序的替代：payload只有lastUpdated而无created_at/published_at；可见顺序也是近期更新，不能由sort=created参数名推定实际排序。前页行数依次30/30/30/30/30/30/18/30，pageCount依次2/2/2/3/2/3/1/2。没有确认本窗新仓库或重要release的停点；本轮不翻遍所有仓库、普通PR或commit。

**建议终态限制**：这些组织的历史artifact发现范围未证，不支持“本窗无新仓库/无重要release”的断言；已被官方研究目录明确发现的具体artifact仍按候选需要定点核。可接受恢复材料是这些组织本窗created/published事件列表或带可靠时间的官方发布说明；有具体材料时只重开对应家族。不因为API与网页受限而无限重试，不把八组织目录行数加成论文数量。

## 2. 首批准入抽检

从首批35中读取原库存的完整标题与摘要：10个潜在项覆盖结构RAG/路由包装、窄领域反证、学习动力学、程序评估、合成训练数据与搜索合法性；5个关闭项覆盖访谈/工程流水线/记忆组合/process reward/表示理论，检查共同理由而非随机追求保留率。共15家族，不是首批35全量非作者通过。

| ID（2604前缀） | 独立判断及应限定的具体贡献 |
| --- | --- |
| 16312 | **最小消歧而非自动潜在**。三种索引、动态chunk与bounded extraction不单独证明新选择。必要§3.1及Table2实际可读，见下节；只能围绕关系粒度/上下文支撑的特定新增机制或可归因证据判断，不能只写“更灵活RAG”。 |
| 16318 | 窄反证可继续。摘要给500 users/3 seeds下retrieval coverage、exposure与score discrimination，能质疑这一cold-start pipeline的容量选型；但没有支持任意RAG或“LLM reranker通常不如popularity”。必要§V/VI实际显示baseline full-catalog与FAISS candidate pool不同，应隔离归因混杂，不能采用33.5倍为reranker能力比较。 |
| 16320 | 准入成立：原CRUXEval与程序/输入干预下排序/exception表现不同是具体评价反证；后审必须判断语义保持或正确truth重算，不能仅据highscore下降就宣称内部无worldmodel。 |
| 16322 | 可继续核actor反馈终止与schema组合演化的兼容性/覆盖控制，不因MCTS或coding数据集名字入选；若必要方法只复用标准难度采样且没有新增边界，应具体关闭。 |
| 16332 | 准入成立：LoRA和fullFT对high-disagreement样本loss方向不一致、匹配rank/部分相关/seed与dataset对照，是学习动力学的新窄证据；不能把annotation entropy相关当机制因果。 |
| 16349 | 可继续：执行式动态truth和temporal re-anchor failure可能改变动态QA评价有效性；新benchmark规模本身不够。必要审阅核truth更新时间、self-repair验证及lazy retrieval错误归类，不能以领域Finance/Sports误当AI for Science。 |
| 16383 | 准入成立：completeness排序与90%recall人工review代价是judge triage具体反证，不因医疗领域窄而关闭。作者已有必要审阅明确HealthBench真值并非全部独立clinician标签，保持此限定；本轮不重读其全文，未预支证据Gate。 |
| 16401 | **准入理由收窄后可继续**：成熟SFT/RL cost routing本身不够，但必要§4.1及§5.5.1的GraphRAG-first/LLM-first/one-time对照确实检查证据获取先于generator选择这一依赖顺序，不能仅因组件成熟而全部关闭。按这个局部设计分支审，不称所有GraphRAG路由新增。 |
| 16410 | 准入成立：匹配LR与多seed控制使FullFT/LoRA迁移保持的解释改变，低LR underfit限定是可保留边界；不把attention drift当因果。 |
| 16420 | 准入成立：中间AST可非法、由LLM修复到可执行code扩大搜索对象是具体合法性阶段分离；TSP/binpacking与population是否保留invalid均要限定，不外推自治代码执行安全。 |
| 16304 | 保持关闭：完整摘要为19人访谈、组织results-actionability gap和现有评估实践归纳，没有可定位的新评价有效性机制或改变该项目判断的重要证据；不是因为HCI或访谈方法统一拒绝。 |
| 16314 | 保持关闭：11任务runtime代码生成/集成的可行性分数未给hot state compatibility、权限或执行保证的新机制；不可因self-extension命名或Pass@1直接入选。 |
| 16331 | 保持关闭：三级memory、KG/经验guideline与检索在具身规划的已知组合，没有分离改变学习/记忆共存边界的具体机制或反证。 |
| 16335 | 保持关闭：rubric GRM筛轨迹相对terminal rejection sampling的任务收益没有在摘要分离新的reward有效性/机制，仍是已知process反馈应用；不是因SWE、GRM或未发明架构拒绝。 |
| 16426 | **不能沿旧泛化理由直接关闭，先最小消歧**：activation-region匹配对比参数ambiguity可能有主线机制关系，不能因MinHash/Hungarian成熟而否认。必要§10.4/§11.3已实际读出下述中心保证疑点与稳定性证据不足；它不自动成为正面候选或Books增量，作者据具体命题决定有依据的关闭或窄争议处置。 |

## 3. 为准入消歧实际补读的必要段落

以下不是四篇完整全文审计，尚未核全部日期/评价/Books owner；不把它们标为Standard/Deep Complete。

- [16312v1](https://arxiv.org/html/2604.16312v1)：§3.1 Document Set Processing / Dynamic Partitioning / Truncated Sliding-Window Knowledge Extraction，及§4.3 Table2。每document局部建结构，bounded prefix跨chunk提取并保留unmodified source span；Mix域组合消融检查hyperedge和cluster互补。尚未证明相较已知粒度组合产生值得Books保留的不同有效性条件，也不从指标上涨推定机制因果。不要为消歧遍历全部附件。
- [16401v1](https://arxiv.org/html/2604.16401v1)：§4.1 staged GraphRAG→generator选择；§5.5.1 Table3对比one-time、LLM-first、GraphRAG-first，前后顺序明确是控制变量。这个窄证据允许继续候选审阅，不能仅凭action-space O(G+L)与“cost-aware”名字入选；下一必要核对是对照预算/训练是否可比，而非再读全部引用。
- [16318v1](https://arxiv.org/html/2604.16318v1)：§V TableII及§VI-A/B。full-catalog baseline与FAISS候选池不同，observed ranking差距不能归因cross-encoder本身；有限用户/电影任务的selection bottleneck与曝光仍可作为受限诊断，是否值得仅报告由完整证据裁决，不反证全部RAG。
- [16426v1](https://arxiv.org/html/2604.16426v1)：§10.4 Proposition9.4、§11.3.1–11.3.4，Tables2/3。实验只两32-neuron网络、16k sample，比较exact Jaccard与MinHash matching，未给参数扰动flickering稳定性的直接对照。§10.4将同一组hash下`ρ(A,B)=mean 1[h_t(A)≠h_t(B)]`说成固定realization可能违反三角不等式；但每个t都有`1[a≠c]≤1[a≠b]+1[b≠c]`，求均值仍确定成立。这是定义与声明的窄冲突，不证明整个研究无价值。HTML标题含Aug24作者日期与arXiv v1标记时，不将作者排版日期改名first-public；若决定准入仍核实际公开批次。不能采用稳定canonical/普遍metric宣传。

本轮未重复审16324/16351全文；已读作者V3_EVIDENCE_NOTES以及其中apr02实际有限独立核验范围，只建议复用未变结论，不冒称本复核独立证明公式或Books写入。

## 4. 交付边界与下一步

本有界来源/准入校准完成，**整日状态未验收**。实质修正为16312准入理由、16401窄顺序对照、16426旧关闭理由与中心保证限制，以及OpenAI历史访问描述、八组织artifact覆盖隔离。
作者已收到这些发现；应按共同理由定点复查受影响组合型材料，不扩大为全类别或全部论文重读。其他已通过且未变化的准入项继续证据审阅，不等待此辅助任务。
当日候选冻结、所有必要exact版本/日期/撤回核对、完整采用命题/Books比较及实际写入、最终日级独立验收不在本轮范围，不能用这份抽检宣布Complete。

本轮仅创建此独占文件。检查Markdown、相对链接与该文件diff whitespace；没有stage、commit或push，没有改动既有证据和书稿。
