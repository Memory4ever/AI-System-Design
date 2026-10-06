# Daily Research — 2026-03-25

**规范：** V3
**窗口：** 2026-03-24T09:00:00+08:00 ～ 2026-03-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T04:23:03+08:00

## 1. 结论

本窗确定候选1个唯一家族：OpenAI Safety Bug Bounty的公开受理范围将“有可复验实际危害但未必是传统安全漏洞”的报告纳入独立流程，并保留与Security团队的归口。5分按安全scope变化深入受影响内容，作者必要审阅1/1完成，Books判断为仅报告1，整合/已有覆盖/结构候选均0，无实际Books修改。该计划的复现阈值与奖励范围是厂商版本事实，不是通用安全保证或新增防线性能证据；root已实际必要源/Books处置与最终日级Gate通过。

四个title主题有限首批只作发现；14份完整v1题摘中12个潜在家族日期未能完全落窗，2个在贡献前关闭，不评分、未作全文Evidence。另7项官方核心重呈现/产品/组织/政策pack具名关闭，总9个负侧样本；不将宽目录数量或75个交叉返回相加为本日候选分母。14来源均有有限入口/停止，4组必要历史切片限制保留。旧780行报告的628/21候选、评分、EffectiveDate及完成标签不继承，原文保留[旧快照](../_sources/daily-20260325/V3_LEGACY_REPORT_SNAPSHOT.md)。

普通待办0。无长工具、无Books待写或待POST，不等待下一批发现。

## 2. 来源覆盖

[实际查询、原参数、有限停止及具名负侧](../_sources/daily-20260325/V3_FINITE_DISCOVERY_STOP.md)保留；下表只宣称这些入口，不授全机构/全学科召回。复用其他日仅原身份/目录字段，本窗日期与贡献另判。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/RSS本日403后定点复用[官方RSS六邻接原pubDate](../_sources/daily-20260326/V3_OPENAI_RSS_FIELDS.md)，1242只筛Mar24–27：四事件在窗内且core已读，ModelSpec25T10Z/STADLER27T22Z窗外；不扩全RSS正文 | 已检查 | 无必要入口缺口；当前dated核心不授历史实现/launch版本逐字一致 |
| SRC-ANTHROPIC | Research最新10之外，独立对读[20实际Sanity九March publishedOn原值](../_sources/daily-20260320/V3_WORKING_STOPPOINT.md)；唯一相交LearningCurves24T10:41Z，真实economic-index-march-2026-report core19–122；Mar23T23Z三篇左界前 | 已检查 | 有限Research March，不外推全部News |
| SRC-GOOGLE-AI | March Blog204行12cards/2pages，24日Turbo/S2core及旧精确稿题摘、25日XR核心/tech题摘；page2独立复用05原2cards。DeepMind真实/blog/page/3/24cards含6March，Lyria原JSONLD25T16Z窗外；pubs当前766行 | 受阻 | H1仅目标publication历史切片；Blog日期未必要者不追exact |
| SRC-META-AI | Research0行；Blog页1 10+Next页2 12有限非日序，Mar27/26→Mar11/10邻接；publication正确results入口444行当前Sep/Aug已恢复 | 受阻 | H2目标Research/publication历史切片，非全部正文故障 |
| SRC-QWEN | [真实API40原title/path/extra.date](../_sources/daily-20260325/V3_QWEN_FIELDS.json)，MaxPreviewMar19→OmniMar30跨本窗，无返回24/25；停止API可见40 | 已检查 | 无total/paging，不证明删除项/全机构历史无遗漏 |
| SRC-DEEPSEEK | /en/news39行5可见之外，定点复用20完整Next16posts与Research array：ResearchFeb25→Jun24跨窗无可见项 | 已检查 | 仅有限公开数组，不继承动态访问阻塞 |
| SRC-MOONSHOT | 真正kimi.com/en/blog/155行19dated cards Feb9→Apr20，当前全部可见19本窗无项，非旧platform2025目录 | 已检查 | 不外推GitHub所有release |
| SRC-TENCENT-HUNYUAN | Research超时后复用[21生产publicList11/11原字段](../_sources/daily-20260321/V3_HUNYUAN_FIELDS.json)，renderType0/page1,size20，Feb3/13→Apr23display(pubJun24)跨窗无March | 已检查 | display与published不互换first-public；仅当前可见目录 |
| SRC-ZAI | 正确Research15cards Mar15→Apr1、release-notes16条Feb12→Apr7跨窗，无返回24/25；旧库存未扩 | 已检查 | 非全机构News保证 |
| SRC-BYTEDANCE-SEED | 独立读[21实际v2原字段](../_sources/daily-20260321/V3_PUBLIC_DIRECTORY_FIELDS.json)：type1/year2026/token20/count100/US18/82，next40跨到Mar26停；三相交论文完整题摘。type2/token0同参数14/19,next空/false，Feb→Apr跨窗 | 受阻 | H4 Blog未返5身份/date不明；SIMART/Uni/Topo仅目录整日，不当精确原发 |
| SRC-BAIDU-ERNIE | 原/blog/en/63行10卡May9/Apr→Feb6/Jan29→2025，有限第一页跨窗无可见项，语言EN明确 | 已检查 | 不宣称ZH全审或旧页清空 |
| SRC-XIAOMI-MIMO | 首页Paper8 June→Mar13→Feb3；Blog15无date。正确Pro/Omni原route time datetime2026-03-18，整日窗前；不复用误猜/blog故障 | 受阻 | H3仅本窗dated Blog历史切片 |
| SRC-MINIMAX | EN12/CN13卡Mar18M2.7→Apr27(CN)/May26(EN)跨窗；ForgeENFeb14/CNFeb12均窗外。AgentTech当前.md已恢复880B仅May13dated行，定点复用19实际raw | 已检查 | 当前可见AgentTech index仅May13窗外；无其他具体缺失线索，不新造historical slice阻塞，不扩guides |
| SRC-ARXIV | [四title主题查询](../_sources/daily-20260325/V3_THEME_DISCOVERY.json)submitted buffer23T18Z→24T18Z，start0/max25/升序，5/5、20/20、25/25、25/34，相关完整14题摘；合法cs.AI月标题补检web Cachemiss | 受阻 | 12家族公开时间未完全落窗；agent_eval未展开9，不授全学科/无限召回 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Introducing the OpenAI Safety Bug Bounty program](https://openai.com/index/safety-bug-bounty/) | 2026-03-25T08:00:00+08:00 | 传统security vulnerability受理之外，新增可复验AI abuse/safety危害与Safety/Security归口，改变公开报告接纳范围；2 + 2 + 1 = 5 | 深入完成 | 仅报告：厂商program scope/版本阈值，不是已验证新运行防线或长期普适阈值 |

## 4. 证据与知识整合

### [Introducing the OpenAI Safety Bug Bounty program](https://openai.com/index/safety-bug-bounty/)

本次证据是官方dated Blog当前公开core26–55；原RSS `Wed, 25 Mar 2026 00:00:00 GMT`换算BJT08完全落窗。先前本地RSS403已由同identity官方原字段恢复，不据搜索日期补时刻。作者读足受影响scope，不展开Bugcrowd历史或无关项目。

新的公开program接受 meaningful abuse/safety，即使不满足传统security vulnerability分类；两团队可按scope/ownership转交。Agentic第三方prompt注入必须导致harmful action或用户敏感信息泄露，当前文本要求至少50%可复现；其他agent行动要有plausible material harm。超出authorized permissions的feature/data/functionality仍报Security。General content-policy bypass本身在本public program范围外；direct harm且可discrete remediation的flaw可能case-by-case接纳，私人Biorisk活动另属其他campaign。MCP测试须遵守第三方TOS，奖励计划不授未经授权的访问/测试权。

这些是公开接纳/归口条件，不是模型伤害发生率、50%统计保证、统一红队预算或防线有效性。原文没有controlled benchmark、实际triage结果、risk下降估计或完整实现：model/hardware/precision/token length/batch/concurrency/SLO/evaluator performance设置均不适用，因为未采用性能命题；不会把program存在当已安全。当前dated页没有可见修改说明，未取得launch snapshot，不声称所有当前句在发布当刻已逐字一致，采用的是公开program及当前scope事实。

Books实际比较定位 `PLATFORM-SECURITY`：[Ch72 run evaluation](../../../../books/part-06-ai-infrastructure/72-security.md#safety-evaluation-的单位是-run不只是-prompt)676–719已要求目标注入与行为扰乱分账、run身份/预算、severity/actionability/人审及独立release verdict；2822–2831 integration-aware case已绑定connector/credential/effect及安全fixture；539–554 policy-as-data分离sensor与enforcement。新披露并非这些主题“已完全审过”的证据，但新增的厂商受理分类/50%门槛尚未获得长期通用性验证，故仅报告，不为企业配置重写长期机制。71 tenant identity与73release gate交接已读，Books上下文完整加载，无实际Books改动或待POST。

## 5. 缺口与下一步

普通待办0。作者已执行的主题、日期字段和来源恢复均已回收；无长工具或普通全文审阅队列。

以下为本窗外部终态保留项，不支持正面证据/Books/无遗漏断言；以后只按具体条件重开受影响材料。

D1–D11原精度秒的arxiv.content-owned/findable `registered`与v1 Submitted来自[首5字段](../_sources/daily-20260325/V3_FIRST_ADMISSION_DATE.json)及[尾字段](../_sources/daily-20260325/V3_TAIL_DATE_FIELDS.json)。本日实际核[no-advance与schedule](https://info.arxiv.org/help/availability.html)、[arxiv DOI](https://info.arxiv.org/help/doi.html)、[DataCite registered定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)与[states](https://support.datacite.org/docs/doi-states)：Submitted+14Eastern cutoff给最早常规03/25BJT08下界，registered原秒+1秒给上界。区间跨09右端，不能把计划slot、Submitted、created或updated变成exact first-public；不证明更早作者原稿公开。合法月表一次请求未获得可用时间证据，停止。

| 身份 | 原registered UTC（区间上界另+1秒） | 需核验的具体潜在贡献/隔离范围 |
| --- | --- | --- |
| D1 [22446v1](https://arxiv.org/abs/2603.22446v1) | 2026-03-25T02:00:55Z | token cross-sampling区分RL分布稀疏变化与实际gain；非entropy相关即因果 |
| D2 [22774v1](https://arxiv.org/abs/2603.22774v1) | 2026-03-25T02:08:35Z | process separation/CUDAGraph仍CPU-side launch/communication/tokenization瓶颈；非普遍CPU配额 |
| D3 [22751v1](https://arxiv.org/abs/2603.22751v1) | 2026-03-25T02:08:04Z | CIPL execution/observable/extraction跨channel隐私，latest改题不反填v1 |
| D4 [23414v1](https://arxiv.org/abs/2603.23414v1) | 2026-03-25T02:23:51Z | length-aware completed rollout提前update与cache off-policy degree，scheduler/learning耦合 |
| D5 [23500v1](https://arxiv.org/abs/2603.23500v1) | 2026-03-25T02:25:50Z | UniGRPO CFG去分支和latent KL→velocityMSE具体替代；不因text+flow组合准入 |
| D6 [22455v1](https://arxiv.org/abs/2603.22455v1) | 2026-03-25T02:01:08Z | SkillRouter metadata-only selection假设的body-removal反证；attention比例不单独因果 |
| D7 [23184v1](https://arxiv.org/abs/2603.23184v1) | 2026-03-25T02:18:25Z | ImplicitRM反馈选择偏差/latent groups条件；unbiased只作者待核假设 |
| D8 [23355v1](https://arxiv.org/abs/2603.23355v1) | 2026-03-25T02:22:27Z | Bellman step-consistency与trajectory验证组成replay value-RL替代 |
| D9 [23149v1](https://arxiv.org/abs/2603.23149v1) | 2026-03-25T02:17:35Z | latent/action→distilled language next-outcome主动steering，不授真实控制安全 |
| D10 [23117v1](https://arxiv.org/abs/2603.23117v1) | 2026-03-25T02:16:50Z | TRAP patch→CoT→VLA action的信息流安全反证，不采用ASR因果外推 |
| D11 [23386v1](https://arxiv.org/abs/2603.23386v1) | 2026-03-25T02:23:11Z | SIMART分解/kinematic联合预测与Sparse3D token表示可行性；不把70%单指标当机制证明 |
| D12 [24278v1](https://arxiv.org/abs/2603.24278v1) | 2026-03-26T02:13:54Z | TopoMesh GT/decoder统一DMC建立mesh-level对应；arxiv事件在后窗但Seed25整日原作者event未定 |

每材料只请求一次：D1–D11可接受 exact-v1实际公告时间/日批次并有正文可取上界，或可核作者原首次公开记录，范围须完全落本窗再重开准入→证据。D5/D11 Seed PublishDate1774281600000(BJT24整日)可能更早原event，ArticleID/UpdateTime在April不当first-public。D12 Submitted25T13:10:34Z=25BJT21:10、常规最早26BJT08在窗外，Seed ID1606 PublishDate1774368000000(BJT25整日)相交但不是exact原发；只请求该Seed/作者original version/first-public证据，不将v2或whole family强纳/强否。否则转真实归属日定点恢复，不扩月份。

H1 Google pubs本窗可定位历史导出；H2 Meta Research/publication本窗可读历史slice；H3 MiMo目前15无日期Blog的本窗dated切片（正确Pro/Omni正文及Mar18日字段已恢复，不再请求）；H4 Seed type2返回14/total19未返5的身份/日期或差额解释。恢复仅相应入口/窗口，非无限历史/全repo队列。

具名负侧9项完整范围与理由见[有限停止N1–N9](../_sources/daily-20260325/V3_FINITE_DISCOVERY_STOP.md)：Turbo/S2旧机制与有效条件重呈现，XR既有模板/API封装及simulator新benchmark未改设计边界，LearningCurves观测采用而非新的系统因果合同，ProductDiscovery/基金组织公告无新机制，Teen具体pack不增加已披露运行语义，SoK/BioShield题摘未识别新的反证/适用条件。必要安全范围只实际core/题摘，不授防护有效性；后两日期未核不影响具体preclose，不新造请求。ModelSpec25BJT18/Lyria26BJT00明确窗外，不用于本窗。

## 6. 复核

复核者：root（非作者）
结论：通过

root已实际完整读正式六部分、有限来源/停止依据、SafetyBugBounty忠实原core26–55及Ch72旧具体论点，5分安全scope深入且仅报告通过；首5+尾8及TopoMesh共14完整v1题摘准入层校准，12 potential日期held不授Evidence、2负侧具体关闭。Teen pack/Ch72、其余限定官方负侧原core、原日期与采用边界通过；不称12篇全文深审或宽库存全量复核。日Gate发现MiniMax仅当前May13 index不能无具体缺失线索制造历史请求，已删除原H4、4历史限制保留；过程原访问失败仍保留，不扩研究。

唯一候选必要证据/Books处置、14源有限停止与外部隔离已达安全终态；root非作者最终日级Gate实际通过，无普通待办，完成态同步。实际运行 `python3 scripts/validate_research.py --report papers/2026/03/25/README.md`：1 V3 interface/consistency PASS；本日README/_sources限定 `git diff --check` 无输出，不能代替以上语义验收。无实际Books写入/待POST，无stage/commit/push；仅本日README/_sources ownership。
