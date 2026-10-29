# Daily Research — 2026-06-01

**规范：** V3
**窗口：** 2026-05-31T09:00:00+08:00 ～ 2026-06-01T09:00:00+08:00
**窗口说明：** 用户授权保留已有候选日期、评分和原小时窗口，本轮只增量补查遗漏来源。
**补充窗口：** 2026-05-31 ～ 2026-05-31
**冻结候选日期：** [补查前真实原档案](../_sources/daily-20260601/baseline-before-supplement-20261021.md)
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-21T16:31:18+08:00

## 1. 结论

本轮仅补 2026-05-31 北京时间完整自然日，原1候选 MiniMax M3 的完整行、日期、8分和连续原§4均保留；确定新增0，Books新写0。旧 M3 的官方事件、限定采用命题与 `MODEL-LONG-CONTEXT` 具体已有覆盖已由非报告作者 root 在[独核R3](../_sources/daily-20260601/SUP_REVIEW_20261021.md#r3--旧-minimax-m3-有效证据与具体已有覆盖复用通过)实际核实复用，不把原Jun01事件移入May31新分母。

每日14源的有限入口已处理；本窗处于 arXiv 非常规公告日，日历门只支持常规公告0，不把旧 DataCite `created` 或 Submitted 日期当公开日。补检两份完整题摘中，APEIRIA有机制潜力但常规公开下界晚于本窗，MAAD为未显示通用机制差额的应用组合；官方 Meta 使用指南及有限论坛噪声按具体贡献排除。没有新增候选需要评分、深审或写书，不等于互联网上没有其他发布。

来源历史目录、Google年度论文目录与 arXiv 非常规公开保证的限制见§2、§5，不支撑“无遗漏”或正面 Evidence。普通扫描/审阅/Books待办0，本轮完整六部分已由root实际日级独立复核通过；不是沿用旧完成标签。完整查询、分页与具名处置见[本日增量来源](../_sources/daily-20260601/SUP_SOURCES_20261021.md)。

## 2. 来源覆盖

以下均指本轮May31补窗，不沿用旧多日RECERT的零结果；只查清单每日组，没有按需会议/协议发布触发。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml) HTTP XML解析当前1303条，仅核当窗与边界；May29发布后直接到Jun01，无May30/31条目，停止RSS已返回历史切片 | 已检查 | 当前RSS不是删帖/隐藏历史及全站无遗漏保证 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)实际JS恢复[default/1](https://www.anthropic.com/listing/research/default/1)、[default/2](https://www.anthropic.com/listing/research/default/2)，各24条，page2 Aug28→May22跨过窗口；六相关team有限日期边界补检，未见May31身份，停止page2 | 已检查 | 当前迁站目录不可变历史保证未取得；不读别日正文 |
| SRC-GOOGLE-AI | [DeepMind publications](https://deepmind.google/research/publications/)第1页30条，Jun04→May28；[Google Research May archive](https://research.google/blog/2026/05/)仅May28/27/19/01四条且到底，无May31；年度pubs入口两次HTTP超时，定点May31搜索无具名补项 | 受阻 | Google Research年度论文历史slice未取得；不把搜索零命中认证为全覆盖 |
| SRC-META-AI | [publications](https://ai.meta.com/research/publications/)不可用；root实际[results page2 most_recent](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2&sort_by=most_recent)片段Jul17→Jun05→May27→May04后混入旧年；May31 publication/blog定点查询无新身份。唯一具名portfolio指南核心EX | 受阻 | 可见片段没有May31，不等有序分页或完整历史；原目录/有效当日切片到达才定点重开 |
| SRC-QWEN | 官方[retrieval API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)当前40条逐条只核title/date；May29 Qwen-VLA→Jun01 Qwen3.7-Plus，后者content published_time May21与extra Jun01分开，两者均窗外 | 已检查 | 当前迁站目录隐藏历史保证缺失；日期冲突不制造May31事件 |
| SRC-DEEPSEEK | [首页](https://www.deepseek.com/)→[研究动态](https://www.deepseek.com/news/)实际5动态/10研究；动态Apr24→Sep10、研究Feb25→Jun24，无May31；“查看全部”未认证，停止可见片段 | 已检查 | 不授隐藏历史/所有分页保证，非官方社区帖不作厂商证据 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)静态列表止于Nov2025；实际[kimi-code API page8](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=10&page=8)/page9共13tag/date，May29 0.6.0→Jun02 0.7.0无May31，page9到May26停止 | 已检查 | Blog2026迁站前历史缺失；不把当前release范围外保证为零 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)真实publicList POST，zh/page1/size1000/renderType0，现有11条日期/title，May21 Hy-MT2→Jul06 Hy3；publicAt与displayPublishTime分开，无May31 | 已检查 | 当前目录不证明迁站前隐藏历史 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)首查“全部”可见15条，Jun16 GLM5.2→May20 ZCube→Apr29，跨窗停止，未见May31 | 已检查 | “查看更多”以下更早历史不展开，不授历史不可变保证 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)/[Papers](https://seed.bytedance.com/en/public_papers)真实get_article_list_v2，US/type1 count100：p1实际18 next20，p2实际20至May15后停；type2 p1实际15 has_more false停；May29 TaskMem→Jun03 MetaPoint无May31 | 已检查 | pinned/可见数不等总数或完整历史；目录日期不代论文首次公开 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)p1十条最新May09，其后Apr30/Apr15，已经早于窗口，未见May31；更早p2不展开 | 已检查 | 静态目录不证明删除/迁站前无隐藏发布 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)8个Paper日期/title与可见Blog标题；实际官方4752 JS frontmatter确认推理优化May30→UltraSpeed Jun08/MiMo Code Jun10，Paper Mar13→Jun29，无May31身份 | 已检查 | 无日期旧产品页/迁站前发布序列不认证；May30不迁入本日 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)/[CN](https://www.minimaxi.com/blog)当前13/14条有限边界均直接至Jun01 M3，无May31；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)4条均Sep19后且到底。M3 JSON-LD为Jun01 BJT，旧行复用而非新增 | 已检查 | 两语AgentTeam May27/Apr27均非当窗，不选择其一制造事件；历史隐藏内容不认证 |
| SRC-ARXIV | [官方availability](https://info.arxiv.org/help/availability.html)适用日历：May31 BJT不含常规公告点；CL/LG/AI/DC May列表404/timeout，三个限定主题补搜恢复01215/01385仅SubmittedMay31，精确v1/history均不支持本窗公开 | 受阻 | 常规0与非常规/历史列表保证分开；后者未认证，不读取全分类/旧宽raw队列 |

查询、字段、分页、有限反例及实际失败范围见[来源记录](../_sources/daily-20260601/SUP_SOURCES_20261021.md#当日发现与实际停止点)。未列为新增候选不取消实际来源检查。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [MiniMax M3](https://www.minimax.io/blog/minimax-m3) | 2026-06-01T01:31:18+08:00 | MSA 把长上下文稀疏选择与 KV-outer block execution 联合设计，并披露原生多模态训练与 Agent workload；3+3+2=8 | 深入完成 | 已有覆盖：`MODEL-LONG-CONTEXT` — [章节](../../../../books/part-02-model/22-long-context.md)；正文锚点「稀疏选择器本身还需要明确 gradient ownership」 |

原1唯一家族保持；本轮May31补窗新增0。旧M3位于原小时窗内而非补充自然日，按用户授权冻结，不据此推断May31候选。下面连续原§4保留旧事件的有效证据与采用范围；本轮增量不改其文字。

## 4. 证据与知识整合

### [MiniMax M3](https://www.minimax.io/blog/minimax-m3)

官方 Blog 的 JSON-LD 把发布时间固定为 `2026-05-31T17:31:18Z`。正文披露 MSA 以 blockwise selector 缩减 full attention，并把执行组织为 KV-outer gather-Q，使命中同一 KV block 的 query 共享连续读取；同时说明 native multimodal 从训练起点混合 modality。它证明的是厂商公开架构和作者实验，不证明 1M Context、4×/9×/15× 或能力分数可跨模型、硬件、精度、batch、并发和 SLO 外推；Blog 当时也说明完整 technical report 与权重将在以后发布。

`MODEL-LONG-CONTEXT` 后续已用 `arXiv:2606.13392v1` 把 selector gradient ownership、GQA-group/block selection、KV-outer reuse、hot-block load balance 与 dense fallback 写入正文。因此本事件是同一机制家族的首次官方公开，本次不重复写 Books；模型与多模态产品声明不替代其后 exact-v1 的证据边界。

撤回家族 `arXiv:2606.24369v1` 已从 selected、candidate 与 Books queue 清除。本次再次确认本日报告及对应 owner queue 中没有该家族的正向采用链；其他有效材料的证据不受该撤回清理影响。

### 本轮补查的证据与Books差额

非报告作者root实际核M3官方核心/唯一JSON-LD与Ch22 selector gradient ownership→GQA/block selection→KV-outer/hot-block→dense fallback完整局部及MSA末注，原8分/具体已有覆盖有效（[R3](../_sources/daily-20260601/SUP_REVIEW_20261021.md#r3--旧-minimax-m3-有效证据与具体已有覆盖复用通过)）。本轮无新增采用命题，无Books改动、待写或待POST；不重审其后续全文/artifact，不把后版细节回填为首次Blog已公开内容。

本轮完整题摘/官方核心的代表性排除与日期边界已通过root有限独立校准（[R5](../_sources/daily-20260601/SUP_REVIEW_20261021.md#r5--首批代表排除与日期误读独立校准)）：Meta指南只是作品集/SEO使用建议；MAAD四角色/RAG/设计史记忆应用未给出通用系统机制增量。APEIRIA的神经符号trace→3D MLLM蒸馏潜力没有被否定，但v1提交与适用公告日程给出的常规最早公开日已晚于May31，未评分或采用。论坛缓存只作发现及有限贡献初筛，不证明厂商机制、实现或实际首公开日期。

## 5. 缺口与下一步

普通来源扫描、题摘筛选、证据审阅、Books及独立六部分复核待办0。下列均为有限恢复后隔离的本窗终态保留项，不是未知候选已通过；不支持正面证据、Books或“无遗漏”断言，定点重开条件分别列明：

- Google Research年度pubs历史切片：两次HTTP未取得正文；May归档四条可读但不能代全部论文。取得May31可复查公开列表或具名原稿后，只恢复该入口/身份。
- Meta：publications不可用、实际results片段混序；root有限恢复仍不能认证有序分页。取得May31原目录、官方当日研究页或有效有序分页后，只重开该历史切片。
- 当前机构目录的历史隐藏/删除保证：OpenAI RSS、Anthropic、Qwen、DeepSeek“查看全部”、Moonshot Blog2026迁站前、Hunyuan、Z.ai、Seed、ERNIE、MiMo无日期旧产品页及MiniMax当前目录，均仅认证§2所列实际可见片段；必要当日官方存档或具名遗漏到达时定点恢复，不据空目录推互联网零发布。
- arXiv历史列表/非常规发布保证：官方日历限定常规公告0，但May分类列表当前失败；若恢复May31非常规公告或具名更早作者正文，只重开相应事件。旧created receipt不作当前日证，Submitted/updated不改变归属。

窗外线索，不属于本窗且不阻塞本日：[APEIRIA 2606.01215v1](https://arxiv.org/abs/2606.01215v1)最早常规公开下界Jun02 BJT，不把它写成实际公告日；未来真实归属日仅恢复其必要日期资格、贡献证据与Books判断。本轮不处理该日其它材料。已明确EX的MAAD不为不影响处置的日期额外建请求。

## 6. 复核

复核者：`root`（本轮独立非报告作者）；旧有效层按[独核记录](../_sources/daily-20260601/SUP_REVIEW_20261021.md)定点复用。

结论：通过

root已实际完成R2日历门、R3旧M3具体已有覆盖、R4有限机构恢复、R5～6代表性准入与来源权限校准，并在R7完整读回本日报六部分和当前SUP后日级通过；这里只同步真实既成结果。全部拟新增正项（0）已覆盖，分层实际核官方使用指南、第三方状态确认实践、MAAD组合与APEIRIA窗外多模态蒸馏，明确纠错/安全/重要修订无具名未处理信号；其余来源与EX仅在实际记录范围，不称全网逐条验证。

作者与root实际检查：V3通过；8个本地链接均存在；冻结原候选1完整行/日期/评分、原窗口和连续原§4不变（正文1192字节，含标题1219字节），baseline与启动真实副本逐字节相同；限定working/cached diff检查通过，未改index。无Books新写或待POST，没有复现实验、核验所有附件、认证历史全覆盖或“无遗漏”。
