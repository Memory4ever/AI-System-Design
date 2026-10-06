# Daily Research — 2026-04-26

**规范：** V3
**窗口：** 2026-04-25T09:00:00+08:00 ～ 2026-04-26T09:00:00+08:00
**窗口说明：** 用户授权仅补来源遗漏，保留旧候选、日期、评分、原小时窗口及连续旧 §4；旧层结论按原窗口理解，不以旧完成声明代替本轮验收。
**补充窗口：** 2026-04-25 ～ 2026-04-25
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-16T03:56:36+08:00

## 1. 结论

本轮仅补北京时间 Apr25 完整自然日：新增 [ProEval](https://deepmind.google/research/publications/238239/) 一个机构题摘事件家族，必要深入审阅完成，Ch66 具体已有覆盖；非作者必要证据/Books、实际写后及完整六部分增量复核通过，普通研究待办为零。它区分总体性能估计与主动失效发现，不能把搜索得到的难题均值当部署总体错误率，也不能从摘要的省样本数推出端到端收益。Books 新机制整合为0，仅纠正一处原有阈值方向。旧候选表为空、旧连续 §4 按授权原样保留；ProEval 只新增到本轮，不追改旧小时窗口归属。

十四每日来源按本轮实际取得内容与可核旧邻界分别处理；OpenAI Apr25 就业转型正文属于宏观政策情景，范围关闭。Seed MegaScale-Omni 当前官网 Apr26 仍是新窗外线索，不搬移。arXiv 实际核官方公告规则并尝试四主题日检索；日检索返回只支持年月的表单错误，不能记成零篇。机构历史目录与异常公告列表未恢复的部分隔离，不支持无遗漏保证。[唯一补充记录](../_sources/daily-20260426/SUP_SOURCES_20261016.md)保存当前范围、准入、证据与停止位；[旧 Gate](../_sources/daily-20260426/V3_ROOT_DAILY_GATE_20260426.md)只对应旧窗口，不代替本轮验收。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 实开 Research/Index 当前页与完整 News RSS；Apr25T00Z Jobs 正文已读并按宏观就业政策范围关闭，前Apr23/后Apr26；[记录A2/A3](../_sources/daily-20260426/SUP_SOURCES_20261016.md#a3-本轮实际来源切片) | 受阻 | RSS不能替代Research历史分页；本轮Apr25自然日内确有Jobs，不沿用旧窗前判断 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 可见 publishedOn 邻界 04/22T14:12/14:27Z → 04/29T20:26Z，当前目录跨过本窗 | 已检查 | 仅限当前可见官方 Research 目录，不证明未列作者稿不存在 |
| SRC-GOOGLE-AI | 实开Research四月Blog、Google Publications、DeepMind Publications/Blog；本轮保存DeepMind目录Apr23→Apr25 ProEval→May6，ProEval官方日级机构事件及v1具体机制已读 | 受阻 | 本轮不再追旧9点门；Google Publications/DeepMind Blog缺有序本日历史停点，不能由有限Blog阴性推广 |
| SRC-META-AI | 本轮Research请求连接重置；旧有效Blog混排Apr8/Jun29卡片停点有限复用，有界机构主题补搜未命中 | 受阻 | 连接失败/搜索阴性不证明Apr25无发布；需原站有序历史切片或具名正文 |
| SRC-QWEN | [动态研究列表](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 的 extra.date 邻界 04/22T10+08→04/28T10+08；[qwen-code release p338](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=1&page=338) 04/24T12:11:44Z→[p337](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=1&page=337) 04/26T06:49:56Z，两个 release 均窗外 | 已检查 | 研究目录与该仓库 release 层停点有效；不据此断言其它仓库 tag/普通提交均无事件 |
| SRC-DEEPSEEK | 本轮News返回429；旧有效News Apr24→Sep10与Research Feb25→Jun24邻界复用，不改变旧V4事件 | 受阻 | 本轮429不是有效目录或零命中；旧邻界不保证隐藏历史完整 |
| SRC-MOONSHOT | [Kimi CLI 1.39.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.39.0) 04/24T06:22:19Z→[1.40.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.40.0) 04/28T13:51:04Z；该仓库 release 层跨窗。[Platform Blog](https://platform.kimi.com/blog) 当前列表止于2025-11 | 受阻 | Blog 缺 2026 可核历史档；release 阴性不替代 Blog 或其它仓库 |
| SRC-TENCENT-HUNYUAN | 官方 Research“全部”同源 [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，pageNum1/pageSize100/renderType0，实际 totalNum=9/list=9；displayPublishTime 04/23→04/30 跨窗 | 已检查 | 仅全部公共列表，不声称所有未列作者论文已被枚举 |
| SRC-ZAI | [官方 Research](https://www.zhipuai.cn/zh/research) 当前可见 04/07 GLM-5.1→04/29 Scaling Pain；[官方发布说明](https://docs.z.ai/release-notes/new-released) 04/07→06/16，均跨本窗 | 已检查 | 限两项可见官方目录，不推广到所有仓库/作者稿 |
| SRC-BYTEDANCE-SEED | 本轮同源papers API/US header/page0及20实际18+20条，后页May16→Apr15中Apr26 MegaScale→Apr23 TriCast→Apr22 Seed3D；旧Blog邻界有限复用 | 已检查 | 当前目录无Apr25新项；MegaScale的Apr26不迁本轮，旧小时窗隔离不变；不覆盖未列作者稿/删改历史 |
| SRC-BAIDU-ERNIE | [ERNIE 技术 Blog](https://ernie.baidu.com/blog/zh/) 当前可见 04/15 ERNIE-Image→04/30 Preview；[官方仓库 release API](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100) 当前一条旧版，均无本窗可见项 | 已检查 | 限 Blog/该 repo release 层，不推断全部作者论文或无 tag 提交 |
| SRC-XIAOMI-MIMO | [MiMo 首页](https://mimo.xiaomi.com/) Paper 卡片 03/13→06/29 跨窗；同页 Blog 卡片无历史可核日期 | 受阻 | Paper 停点有效；Blog 需原始发布时间或可排序历史入口 |
| SRC-MINIMAX | 本轮完整英文12卡Mar18→May26，中文13卡Mar18→Apr27 Agent Team；Agent Tech当前仅Sep19/Sep22/Oct8三卡；旧CLI Apr17→Apr26 release邻界复用 | 受阻 | 中文本轮有效，不沿用旧仅导航；Agent Tech缺四月历史档，当前中英文同题日期不同但均窗外，不推全机构零研究 |
| SRC-ARXIV | 实核官方正常公告规则；Apr25北京自然日无正常槽。四主题Advanced日检索实际返回公告日期只支持年月的表单错误；LG/AI月列表各前2000仅作有界诊断，没有逐项分类或声称当天论文 | 受阻 | 错误响应不是零命中，月列表非当日池；必要异常公告/替换事件历史列表未恢复，隔离该覆盖断言；机构先发单独检查 |

补查 Github 官方当前可见新仓库创建层与少量主线 repo release，只用于查漏，不能把组织新仓库零结果或上述几仓的 release 阴性扩大成全组织零更新；实际八组织、新仓库及 VeOmni release 停点见[本日原始记录](../_sources/daily-20260426/V3_REOPEN_NOTES.md)。未扫描每周来源；无实际触发的按需来源不整站扫描。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [ProEval](https://deepmind.google/research/publications/238239/) | 2026-04-25 | 固定评价预算难兼顾总体估计与失效发现→历史GP prior分别服务BQ积分与superlevel查询→区分预算/估计对象；2+2+3=7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#rare-failure-evaluation-需要保留无偏-audit-floor)，只纠正失败阈值方向短语，非作者实际写后通过 |

本轮新增ProEval是官方Apr25机构题摘事件，不把arXiv提交当公告，也不回填June v2；旧空候选层不变。MegaScale保持旧Apr26身份，不混入Apr25补充候选分母。root已实际完成首批准入、必要方法/反侧及Ch66具体已有覆盖的独核；唯一阈值方向短语在授权窄位纠正后，非作者实际写后及六部分增量复核通过。

## 4. 证据与知识整合

### [MegaScale-Omni](https://seed.bytedance.com/en/public_papers/megascale-omni-a-hyper-scale-workload-resilient-system-for-multimodal-llm-training-in-production)

官网目录标 04/26，Seed API 的 PublishDate=1777132800000 毫秒对应本窗 04/26 00:00 北京，题摘提出 encoder 长短序列并行、LLM 5D 并行、统一 encoder–LLM 表示/流水线和按 rank 的自适应 resharding，作者给出自有动态多模态负载相对四个系统的吞吐 1.27×–7.57×。这是题摘主张，不是已核实验配置、控制对照或普遍生产收益。该卡片 UpdateTime 在07/01，当前外链 [arXiv 2605.08962](https://arxiv.org/abs/2605.08962) 的 v1 在五月才提交；[Crossref DOI 记录](https://api.crossref.org/works/10.1145%2F3767295.3803587) created=04/24T20:20:04Z 是记录建立，published-online=04/26 只有日期，不能判断 09:00 北京前后。ACM PDF 直连未取得。没有本窗公众可读原始全文的时刻链，不能将后来全文机制/实验回填本日。源与同一研究家族的会议发表身份可保留，但不据此决定本窗 Books。

### [ProEval](https://deepmind.google/research/publications/238239/)

DeepMind 官方页标 04/25，完整题摘描述以预训练 Gaussian Process 为性能函数 surrogate，用 Bayesian quadrature 估计和 superlevel-set sampling 发现失败，涉及 Ch66 Evaluation 的潜在设计选择。当前页 JSON-LD 的 datePublished=2026-04-25T00:00:00Z 与日级显示相同且为整点零分秒；同站另一条 04/22 出版页也将日级日期写成 UTC 零点，不能独证真实上线时刻。[arXiv 2604.23099v1](https://arxiv.org/abs/2604.23099v1) 的周六 04/25T01:33:57Z 是提交，不是本窗公告；官方日历无正常周末公告。机构 [ProEval GitHub repo](https://api.github.com/repos/google-deepmind/proeval) created=04/17T23:59:55Z，但当前可见最早 commit 为04/27T18:13:15Z，截止本窗的 commit 查询与 release 均空：只约束这一仓库的可见记录，不证明官网未先发，也不证明本窗已发。未确定首次正文 owner 前，不读后续 v2 的方法/表来做本日证据和 Books 正面判断。

### Books 决定

Books 纳入任务范围，但两条潜在贡献都处于首公开日期隔离，尚无确认落窗候选可支持写入；本次 Books 实际新增 0。不是仅因 Ch36/Ch66 主题相关就宣称“已有覆盖”。若后续原始时间链证实其中一条属于本窗，再按精确当时版本读必要方法、主对照与反证，并与实际知识 owner 比较；共享章节动笔前先协调写锁。

### 本轮 Apr25 自然日补充（旧连续 §4 以上原样保留）

ProEval 的官方 Apr25 日级研究题摘事件在本补充自然日有确定归属，不再以缺旧09:00时钟隔离。精确v1只作当前可复查的必要技术支持，不证明其全文当时已经公开；June v2或四月benchmark先公开不倒填。已读方法/主对照/反侧，结论限定为：总体积分估计与高错误区域搜索是不同目标，历史score covariance或embedding prior有负迁移风险；采样省数不等全费，Thm3不提供有限题库S*的无条件无偏证书。当前 Ch66“Rare Failure Evaluation”两段实际承载这些论点，root必要Source/owner独核通过，决定已有覆盖；只将原“低于阈值”纠正为“错误评分不低于阈值”，与v1 Eq12方向一致，没有新机制整合。root已实际顺读修正正文与完整前后邻接，写后通过、窄位释放；细节见[唯一SUP A4/R1](../_sources/daily-20260426/SUP_SOURCES_20261016.md#a4-proeval-必要证据与现-owner-比较)。不声称Apr25代码公开或原站全文历史快照已认证。

## 5. 缺口与下一步

普通可执行研究待办为零；非作者必要Source/owner、实际写后及完整六部分增量复核已通过。本次完成保留下列不能支持正面断言的外部终态限制，不等于全部历史来源覆盖或无遗漏。

本窗外部终态保留项只隔离受影响断言，不删除已核目录事实，也不支持正面候选、Books 或“无遗漏”保证：

- **Seed MegaScale-Omni 首公开：**需作者/ACM/会议原始论文正文在 04/25T01Z～04/26T01Z 内公众可访问的精确时刻，或可验证历史卡片/全文快照；当前 Seed CMS PublishDate、后续 UpdateTime、五月 arXiv 和 Crossref created/日级 online date 的组合不能证明。若确认窗外，只迁回真实 owner 日，不把此题摘算本窗候选。
- **DeepMind ProEval 旧小时窗：**旧9点归属/当时全文历史快照仍未证，保留原层而不改写；新Apr25机构日级事件不以此阻塞。arXiv提交不是本日公告，June v2不倒填。
- **来源历史入口：**OpenAI Research、Google Research Publications/DeepMind Blog、Meta Research/Publications、DeepSeek本轮429、Kimi 2026 Blog、MiMo 无日期Blog、MiniMax Agent Tech四月档缺可复查本日分页/发布时间；需要原站有序历史切片或具名正文才重开。MiniMax中文当前日期邻界本轮已恢复，不沿用旧缺口。RSS/有限目录/release不替代这些子入口，隔离不等于零发布。
- **正常公告与索引边界：**arXiv正常日历不排特殊公告；四本轮日级Advanced请求被年月粒度限制，需官方历史公告/替换事件列表或具名先发正文才能定点重开该覆盖层。旧419按submittedDate的宽身份、两月列表前2000及DOI created均不作Apr25公开队列，不做无遗漏保证。

窗外已核 release 不阻塞本轮：MiniMax CLI v1.0.12 于04/26 09:40:29北京、Qwen qwen-code v0.15.3 于04/26 14:49:56北京均在Apr25补充窗外，Kimi CLI 1.39.0在Apr24。ProEval本轮已获得机构自然日事件与有限技术处置，不能再以旧精确小时缺口伪装成未读全文待办；其旧历史可见性限制不授予额外证据权限。

## 6. 复核

复核者：root（非本轮补充报告作者）。
结论：通过

旧层[独立Gate](../_sources/daily-20260426/V3_ROOT_DAILY_GATE_20260426.md)保持有效范围，不自动覆盖本轮。本轮[root R1独核](../_sources/daily-20260426/SUP_SOURCES_20261016.md#r1-root-实际写后与六部分增量复核通过)已实际核首批准入、Jobs范围排除、必要ProEval机制/反侧、具体Ch66已有覆盖与唯一符号修正写后、十四来源停止范围及完整六部分；未全量复核所有实验表、代码或倍率，不采用这些未核部分。V3、14唯一来源ID、本地引用零缺失、原窗口/旧空表/连续旧§4及限定diff检查通过；机器检查不替代有限语义复核。外部历史与版本可见性限制仍不授全Coverage/Evidence或无遗漏保证。
