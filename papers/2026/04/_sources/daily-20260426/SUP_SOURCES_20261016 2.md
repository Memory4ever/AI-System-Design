# 04-26 遗漏补查唯一补充记录

作者：supp_apr26_author_fresh。新补充窗口为北京时间 `2026-04-25 ～ 2026-04-25`；原小时窗口、空候选表与连续旧 §4 保留。先以不覆盖的文件复制保存 `baseline-before-supplement-20261016.md`。运行前及并发修改不属于本日作者，不 stage/commit/push，不改索引或 State。

## A1. fresh 上下文与复用权限

已实际完整读取本日 AGENTS、Prompt、研究/Report 合同、来源说明/Daily14/arXiv路由、ROADMAP，以及 State 的 2026 年恢复入口；旧作者记录 `V3_REOPEN_NOTES.md` 和 `V3_ROOT_DAILY_GATE_20260426.md` 只复用其中具体来源事实，不继承完成标签或旧小时门。Books 比较前读 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、Ch66 实际局部与 Ch65/67 交接。

旧层两条题摘线索的身份未变，但新窗不同：MegaScale-Omni 官网与出版方均标 Apr26，原目录事件不搬入 Apr25；ProEval 官网 Apr25 日级日期不再需要证明旧 09:00 截点。当前官网日期可支持机构题摘事件，arXiv Apr25 submitted 仍不是公告。本轮只用精确 v1 检查机构题摘所述机制，不采用 June v2 新增主张，不声称 Apr25 arXiv 公告或代码已公开。

## A2. 首批准入与代表 EX

- **ProEval，机构 Apr25 题摘事件**：[官方原页](https://deepmind.google/research/publications/238239/)完整题摘、[exact-v1](https://arxiv.org/abs/2604.23099v1)完整题摘已读。高成本评价下固定抽样难兼顾总体均值和罕见失效→跨模型历史结果/embedding 形成 GP surrogate，分别做 Bayesian quadrature 与 superlevel-set 查询→改变评价预算和估计对象如何分工。拟 `2+2+3=7`。非作者 root 已实际打开 v1 完整题摘，独立校准通过；8–65x、无偏与生产效果不由准入自动采用。
- **EX：Modeling an AI jobs transition**：[官方正文](https://openai.com/index/modeling-ai-jobs-transition/)实际读核心说明：按 AI 任务暴露、人是否仍是责任主体和降价后的需求变化解释职业转型。它提供劳动力/政策情景而非模型形成、训练、推理、评价或 Agent 系统的新机制；并非因实验小或未有 owner 而排除。RSS `2026-04-25T00:00:00 GMT` 是本补充自然日内，不沿旧窗前判断。root 已校准这个理由，作者随后实际读正文，非只读标题。正文 shell 请求 403 不妨碍本轮 web 正文成功；失败响应 `SUP_OPENAI_JOBS_20261016.raw.html` 不能当正文。
- **窗外而非 EX：MegaScale-Omni**：只保留旧身份与 Apr26 归属线索，不把其五月全文移到 Apr25，不重开 Apr24 已处理材料。

## A3. 本轮实际来源切片

执行日期：2026-10-16（Asia/Shanghai）。下列 raw 均在本目录；HTTP 200 只表示取得响应，以下另说明是否取得有效目标内容。未扫描 Weekly，无按需来源整站触发。

| ID | 实际入口与停止依据 | 本轮可支持范围与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research Overview 与 Research Index 实际 web 打开；Index 当前首屏无 April 历史停点。News RSS 完整响应 `SUP_OPENAI_RSS_20261016.raw.xml`，读目标日及前后项；Apr25 Jobs，前 Apr23 cards，后 Apr26 principles | Jobs 按 A2 明确范围关闭；Research 历史分页未恢复，不能由 RSS 代替或声称机构零发布 |
| SRC-ANTHROPIC | `SUP_ANTHROPIC_20261016.raw` 的 publishedOn Apr22 14:12/14:27Z → Apr29 20:26Z | 当前嵌入目录跨 Apr25；不声称所有未列作者稿或删除历史均覆盖 |
| SRC-GOOGLE-AI | web 实开 Google Research Apr2026 Blog、Google Publications、DeepMind Publications/Blog；ProEval 官方 Apr25 页面与 v1 已读，当前 arXiv v2 的 comments/journalref/version history 轻量核查未见撤回/纠错公告 | ProEval 单项进入 A4；Google Publications 仅当前年度/首页，无本日有序历史停点，DeepMind Blog 当前页也无本日档；不把它们记为零 |
| SRC-META-AI | 本轮官方 Research curl exit35/连接重置；旧有效 Blog 混排卡片仅作原停点复用；四组有界机构补搜之一未命中 | Research/Publications 必要历史切片仍受阻，搜索阴性不替代原目录 |
| SRC-QWEN | `SUP_QWEN_20261016.raw` 实际 JSON extra.date：Apr22 Qwen3.6-27B → Apr28 FlashQLA；Apr30 Scope；旧有限 qwen-code release 日期邻界复用 | 当前研究列表跨 Apr25；不推广到全仓 tag/普通提交 |
| SRC-DEEPSEEK | 本轮 News curl HTTP429，保存 `SUP_DEEPSEEK_20261016.raw`；旧有效 Apr24 V4→Sep10 News 与 Feb25→Jun24 Research 事实复用 | 当前请求不是有效目录；旧邻界可限定当前已知事件，但未恢复隐藏历史，不授全源覆盖 |
| SRC-MOONSHOT | `SUP_MOONSHOT_20261016.raw` 当前 Platform Blog 实际全可见目录止2025-11；旧 Kimi CLI 1.39 Apr24→1.40 Apr28 release 邻界复用 | Blog 没有2026档，不等于 Apr25 零研究；只保有限 release 层阴性 |
| SRC-TENCENT-HUNYUAN | `SUP_HUNYUAN_20261016.raw.json`，POST publicList `{pageNum:1,pageSize:100,renderType:0}`，totalNum/list均9；Apr23 Hy3 preview → Apr30 Real life | 当前全部公开目录跨 Apr25；不覆盖未列作者稿 |
| SRC-ZAI | `SUP_ZAI_20261016.raw` 当前 Research 可见 Apr7 GLM5.1 → Apr29 Scaling Pain | 两日期之间无当前目录条目；旧 release-notes 同区间事实复用，不称所有项目零更新 |
| SRC-BYTEDANCE-SEED | 同源 `get_article_list_v2`，article_type1/count20/desc/page_token0和20，US header；`SUP_SEED_US0_20261016.raw`有18条/next20，`SUP_SEED_US20_20261016.raw`有20条/next40/has_more=true；后页日期May16→Apr15，实际Apr26 MegaScale→Apr23 TriCast→Apr22 Seed3D，跨过目标日后有界停止。默认locale首次请求只有1条，不作为全页完成依据 | 当前所见目录没有Apr25项；MegaScale 原 Apr26 不入新窗。未把全站total246当题摘队列；不是全机构/作者零研究 |
| SRC-BAIDU-ERNIE | `SUP_BAIDU_20261016.raw` 可见 Apr15 ERNIE-Image→Apr30 Preview；旧官方唯一release2025-06-30复用 | Blog/该repo发布层跨 Apr25，不覆盖全部提交或未列论文 |
| SRC-XIAOMI-MIMO | `SUP_MIMO_20261016.raw` Paper八卡，Mar13 ARL→Jun29 MOPD；Blog15卡无日期 | Paper有界阴性；Blog本日资格未恢复，保外部历史限制，不以无日期卡否定潜在贡献 |
| SRC-MINIMAX | `SUP_MINIMAX_20261016.raw` 英文可见12卡，Mar18→May26；`SUP_MINIMAX_CN_20261016.raw`中文13卡Mar18→Apr27 Agent Team（英文同题May27）；`SUP_MINIMAX_AGENT_20261016.raw`实际三卡Sep19/Sep22/Oct8 | 中文本轮不是导航失败；同题中英文日期不同但两者均窗外。Agent目录没有四月历史停点，不由单仓CLI release推全机构阴性 |
| SRC-ARXIV | 官方 Availability实际 web读取及 `SUP_ARXIV_SCHEDULE_20261016.raw`；周五/六美东无正常公告，新Apr25北京自然日没有正常公告槽。另实际试四主题 Advanced day queries，全均返回表单错误，Announcement只支持年月；两月列表LG/AI各前2000只作查漏入口诊断，不逐项分类、不称当日池 | 四错误响应不是零命中。未取得本日异常公告/替换事件的可复核历史列表；正常日历只排正常槽，不排机构先发或特殊公告，保留该限定 |

有界辅助补搜四组原查询：`"April 25, 2026" (language model OR LLM OR multimodal OR evaluation)`限定Google/DeepMind/Meta；`"2026-04-25" (model OR agent)`限定Qwen/DeepSeek/Kimi/Seed；`"2026-04-25" (模型 OR model)`限定Hunyuan/Zhipu/ERNIE/MiMo/MiniMax；`"April 25, 2026"`限定OpenAI/Anthropic。当前搜索返回无结果，仅限该四组索引切片，不形成无遗漏保证。

arXiv四主题为 model/transformer；GPU/inference/distributed training；multimodal/world model/VLA；agent/RAG/RL。精确参数保存在各响应表单：date-from/to=2026-04-25，date_type=announced_date_first，size200。响应明确 `Whoops! Something went wrong` 且公告只支持年月，所以没有把这些请求记已完成题摘筛选或零项。月列表LG总3900、抓前2000及AI前2000不构成待逐项关闭队列，也不借此扩出跨日池。

## A4. ProEval 必要证据与现 owner 比较

精确采用域：[机构Apr25题摘](https://deepmind.google/research/publications/238239/)、[arXiv v1](https://arxiv.org/html/2604.23099v1)，本地 `SUP_PROEVAL_V1_20261016.raw.html`。必要 §2.1–2.4、§3.1–3.3/Tables1/3/4、Appendix B 对 Theorem3 及 Assumptions1/2。当前官方 arXiv 页只给 Jun1 v2/ICML引用，没有可见撤回或纠错标记；不据此保证不存在未列勘误。

方法：同题历史 model-score covariance 与 prompt-feature GP 是不同 prior 来源；BQ 的 acquisition 减少总体积分后验方差，失败搜索则在高错误区域兼顾 uncertainty，topic-aware生成另付generator预算。§2.2.3明确source失配会negative transfer，GMM筛选小于三模型时abstain。失败搜索偏置后的均值不是原目标人口错误率。

评价：Table1相同目标预算比较随机/主动选择与BQ，不把 prior 预测、选择机制和端到端总费混为单个收益。9 benchmark/16模型的错误评分人口与同一题库下历史结果有关；Table3/4生成失败实验是受限 reasoning人口、相同generator配置和100轮预算，非生产流量或安全率。样本节省不等wall-time、token费或冷启动全费；硬件、完整precision/length/batch/concurrency/SLO未披露或不属该统计查询目标，不补造。

理论：Assumption1要求score函数来自共享GP与Gaussian噪声，Assumption2要求历史评同题，Thm3含N≫t/有界kernel。其比较对象是条件posterior mean，不是任意真实有限题库S*的无条件无偏证明；prompt-feature与OOD迁移也不自动继承该保证。保留这些限制，不能只照抄摘要“unbiased”。

**现 owner 实际正文**：`PLATFORM-EVALUATION-SYSTEM`，[Ch66 Rare Failure Evaluation](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#rare-failure-evaluation-需要保留无偏-audit-floor)，当前824–828两段已经具体写入总体S/失败Xλ不同estimand、GP/covariance/目标一同保存、难题均值不得作总体、Thm3仅posterior-mean及negative-transfer/audit回退。并非仅同主题；本轮“已有覆盖”，不新增机制段落。只发现一个符号表述反侧：原“低于阈值的失败集合”，v1 f为错误评分且Eq12使用 f≥λ；root实际读必要源和Ch66完整818–836邻接后授唯一短语lease。作者已实际替换为“错误评分不低于阈值的失败集合”，其余正文不动，保存后顺读完整局部；root实际POST及六部分DAY通过见R1，窄lease释放。

root独立采用权限明确：官方Apr25研究题摘是有效日级事件；不证明arXiv同日公告或精确v1全文已在Apr25公开。v1仅作当前可复查的技术支持，不倒填June v2或任何四月benchmark先公开保证。root必要§2.1–2.4、Assumptions1/2、Thm3/AppB相关证明及negative-transfer与具体owner已实际核；不是全附件或所有benchmark倍率独核。

## R1. root 实际写后与六部分增量复核通过

非报告作者 root 已实际读取本轮完整六部分及 A1–A4：机构 Apr25 事件准入、Jobs 具体范围排除、14 来源的实际入口与停止范围、四个日检索错误而非零命中、旧窗与新自然日的权限区分均一致。必要独核范围为官方机构题摘、精确 v1 §2.1–2.4、Assumptions1/2、Theorem3 与 AppB 相应证明及负迁移；未全量复核所有实验表、代码或倍率，不采用未核部分。Ch66 818–836 的完整局部已读，已有覆盖是具体论点比较；实际保存后再次读 822–830，唯一短语已为“错误评分不低于阈值的失败集合”，与 Eq1/12 一致，其他正文及回退保留，POST 通过并释放该窄 lease。

本轮六部分语义复核通过，允许行政保存完成态后最小读回；不是旧 Gate 自动继承。实际 V3、限定 diff 检查、14 唯一 Daily ID、原小时窗口、旧空表与连续旧 §4 保留、本地引用零缺失均通过；机器结果不替代上述有限语义复核。1 新家族、深入审阅、已有覆盖成立，0 新机制整合，仅纠正一个原有符号方向。机构历史、特殊公告列表及旧小时可见性缺口仍隔离，不支持完整 Coverage/Evidence 或无遗漏保证。

## R2. 完成态实际读回

root 已实际读回 03:56:36+08 完成字段、§1 的1新增／已有覆盖／仅符号纠正及§6具名通过；与 R1 的已核范围和外部隔离一致。完成态 V3、README/SUP/State 限定 unstaged 与 README cached 差异检查通过；原候选为空、窗口和连续旧§4的保护结果未变。本轮正式验收，作者 ownership 释放；没有 stage、commit 或 push。未验收的其他日期不由本日推定完成。

## A5. 作者停止位

来源末端提取已处理；root A4必要Source/owner/采用权限、实际POST与完整六部分DAY已实际通过并保存R1，唯一阈值短语窄lease释放。作者仅行政同步README于03:56:36保存完成态，普通研究待办0；提交root最小完成态读回，不重审研究。外部历史入口和arXiv特殊事件列表限制不能支持正面覆盖或无遗漏保证。

作者已对当前进行中README运行V3校验通过，并核14唯一Daily来源ID、原窗口原样、连续旧§4逐字保留、本地引用路径存在与限定`git diff --check`。首次校验的两处标签/决定分隔符问题已仅改成合同枚举/冒号；arXiv本轮无法恢复必要历史子入口写“受阻”，不误用只适用于辅助补搜的“检索受限”。未改校验器或研究规则。当前Ch66文件工作树diff包含运行前/并发其他内容，作者只拥有824的一处短语；不把整文件51/1变化归于本日。
