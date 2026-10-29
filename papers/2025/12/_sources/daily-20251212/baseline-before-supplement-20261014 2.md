# Daily Research — 2025-12-12

**规范：** V3
**窗口：** 2025-12-11T09:00:00+08:00 ～ 2025-12-12T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T20:46:57+08:00

## 1. 结论

本日十四每日源有界原始检查与四组arXiv主题/官方邻接补检已执行。晚恢复Google两家族确定落窗：Interactions API职责接口与DeepSearchQA完整答案集合评价，Popper实际限定准入/证据校准通过，不等日Gate。原133项及反馈15项恢复/同一有界段26项新增精确v1潜在、GPT5.2与Replication局部安全/设计反证均保留；必要首公开未授窗，未评分、不当Evidence完成、不正面采用。

晚恢复两篇的完整核心与必要评价正文已处理，不重跑其余有效source/题摘层。Books：Interactions API实际已有覆盖，root已将DeepSearchQA两段融入Ch66 RAG gold审计与exposure诊断之间，绑定`SF-2025-GOOGLE-DEEPSEARCHQA`，Popper于2026-10-02T20:24:04+08:00完成真实非写入者POST；GPT5.2草案仍条件化。作者没有写共享Books，不将新增评价反证统一仅报告。作者普通差额已收束，非作者新增题摘校准/日级复核继续，不授日级通过。

## 2. 来源覆盖

[原始查询、停点与逐项潜在判断](../_sources/daily-20251212/SOURCE_SCREEN.md)仅复用固定历史字段，不套用前日候选或完成状态。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/12/11查询；GPT5.2核心/27页card必要§3.3/3.7；Popper原始RSS两个精确link的00:00GMT字段已恢复 | 受阻 | RSS按字段为12/11 08:00BJT窗前，但小时精度/旧27页事件关系未核，不直接授窗；不再泛称RSS失败 |
| SRC-ANTHROPIC | Research十项历史入口、本日日期查询；Alignment实际December六项至November两项，12/08→12/12邻接 | 受阻 | Alignment显示段可读，其他Research历史缺口不由该切片替代 |
| SRC-GOOGLE-AI | Research/pubs、本日查询；DeepMind page/4实际24条，UK→AISI；Research12/10→12/12；晚恢复两篇Google blog原HTML17Z及完整核心、DeepSearchQA PDF必要§1–5 | 已检查 | 两项限定准入/证据已有非作者校准；DeepSearchQA实际写入与POST已有原始记录，不等目录全源或日级通过 |
| SRC-META-AI | 原始publication page4的本窗12/01→12/12邻接、本日查询 | 已检查 | 发表日不当论文first-public，全机构未认证 |
| SRC-QWEN | 旧站09/23/跳转、新动态Blog与本日12/11查询 | 受阻 | 2025目标历史切片有限替代未恢复 |
| SRC-DEEPSEEK | 官网/固定V3.2 12/01、本日日期查询 | 已检查 | 当前首页不证明完整历史，无新机制命中不等全源零 |
| SRC-MOONSHOT | 原始Blog/changelog11/06→10/27、组织当前段与本日查询 | 已检查 | 只支持显示目录，不认证所有repo历史 |
| SRC-TENCENT-HUNYUAN | Research首查历史渲染全部十一项至2026/02/03、组织有限替代与本日查询 | 受阻 | 2025目标段隔离，不重复同一失败接口 |
| SRC-ZAI | Research本日内部错误、release12/10→12/11→12/22、Open-AutoGLM核心及本日检索 | 已检查 | Multilingual声明无独立执行增量，关闭；Research未显示部分隔离 |
| SRC-BYTEDANCE-SEED | 官方2025 paper/Blog各18条、total94/45、next20；本日paper12/15→12/02、Blog12/16→12/02，pinned逐项日期核 | 已检查 | 未续全年库存；目录PublishDate不授论文首公开或全源零 |
| SRC-BAIDU-ERNIE | 原始Blog12/09→12/23与repo说明、本日12/11查询 | 已检查 | 仅显示目录段，排行不作独立机制 |
| SRC-XIAOMI-MIMO | Paper八项10/21→2026/01/08，Blog/组织及本日查询 | 受阻 | Blog目标历史部分隔离 |
| SRC-MINIMAX | 两语Blog10/27→12/23、组织/Agent导航及本日查询 | 受阻 | Blog显示段已处理，Agent历史技术部分隔离 |
| SRC-ARXIV | 四主题/六分类有界邻接，原133项题摘；反馈15项恢复及原CL326–375/DC76–100/CV1076–1175相关标题的26项新增精确v1 | 受阻 | 无有效个体首new批次，日期隔离；10102误关撤销；宽库存非逐项全文队列 |

## 3. 候选与判断

以下两家族由原始JSONLD确认落窗，贡献先于评分，Popper已实际限定准入/证据核验；日期未授潜在材料不提前评分。最终日级独立核验已通过，范围与限制见§6。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Interactions API](https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api/) | 2025-12-12T01:00:00+08:00 | stateless响应与服务端history/后台loop职责拆分；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)52–96；具体接口背景不重复改书 |
| [DeepSearchQA](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/) | 2025-12-12T01:00:00+08:00 | 单答案/F1不能验收完整且无多余答案集合；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 RAG](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#rag-端到端评估必须保留阶段级归因) gold审计后两段，`SF-2025-GOOGLE-DEEPSEARCHQA`；root写入/Popper非写入者POST已记实 |

## 4. 证据与知识整合

### [Interactions API](https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api/)

完整发布核心支持可选server history、typed/interleaved模型/工具记录、background loop与remote MCP；beta仍可能breaking，generateContent继续标准生产路径。它披露职责迁移，不证明durable workflow、幂等、取消回滚、授权继承或确定cache降本。实际Ch84 52–96已有KV/Context/AgentRun/Memory四对象、terminal evidence、typed UI事件与服务端状态回读且禁止仅为恢复展示重提任务；Ch83 100–108/245–257承载protocol五轴与远端对象→本地attempt/未决effect映射。相邻Ch82分工不变。拟已有覆盖不是用相近主题关闭；未运行API，不采用当前GA后文档反推beta。

### [DeepSearchQA](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/)

原博客及16页[技术稿](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf)首页2025-12-11、§1–3/4关键反证/5限制实际已读。评价以final answer set而非轨迹，去重/实体同义由Gemini2.5Flash zero-shot judge判；§3分别算每题precision/recall/F1再平均，并区分strict equality、missing与extraneous。§2三人独立research/冲突仲裁及time-anchored/static sources减少但不消除gold错误；§5承认缺轨迹难分可靠推理与幸运，web删除/变化仍需维护。performance表有CI但不同agent/backends/搜索预算未匹配，不采rank或推因果收益；博客66.1与稿81.9分别strict/F1，不合并为一个成功率。未运行模型，hardware/precision/batch/concurrency/SLO Not Disclosed，不作提速/成本比较。

长期知识缺口触发深入必要评价审阅，评分不变。原Ch66 RAG前两段拥有retrieved necessary-information coverage，不拥有final entity-set无多余项与strict equality；Context/FACTS分账也不等答案集合完成。root现已在gold审计后/exposure诊断前写入两自然段：规范化gold集合与strict/F1分账、matcher身份，以及gold维护成本、仅看结果的限制、开放世界Unknown和旧exact-match基线。作者本次实际重读该段与前后及来源末注，位置现为918/920行，稳定绑定`SF-2025-GOOGLE-DEEPSEARCHQA`；Popper真实POST于2026-10-02T20:24:04+08:00记录了原文→新段→前后/Ch65/67检查。只授两段写后，不认证整章、在线穷尽保证或日级完成。原始证据与提案过程见[晚恢复记录](../_sources/daily-20251212/GOOGLE_LATE_RECOVERY.md)及[非作者原始记录](../_sources/daily-20251212/ROOT_ADMISSION_REVIEW.md)。

潜在GPT5.2的必要证据与[Books条件草案](../_sources/daily-20251212/EVIDENCE_BOOKS.md)已保留，不冒充当窗候选或Evidence Gate。厂商缺图切片与生产流量是不同分布；严格输出失败不能被平均指标吞掉。Popper实际可读RSS两个精确link原pubDate均为Thu, 11 Dec 2025 00:00:00 GMT，按字段是12/11 08:00BJT、在本窗前；缺的是历史小时精度及与旧27页稿的first-public关系，而非RSS不可读。有限必要入口之后具名终态隔离，不从标签或当前链接授11/12确定候选。

owner `PLATFORM-EVALUATION-SYSTEM` Ch66已有条件性分数/五层成功/EvalSpec（实际14–105），Context Evaluation（898–900）仅承载证据存在/使用/扰动；不等完整承载缺输入×格式约束反证。相邻Ch65为资源公平，Ch67为监测分工。拟局部增加输入完整性/输出合同交叉切片及其成本、旧正常输入基线共存边界；必要日期授予与root协调前不写入。不作已整合/已有覆盖结论。

## 5. 缺口与下一步

**作者ordinary：0；非作者新增题摘校准与日级复核已通过，见§6。** [FEEDBACK_BC](../_sources/daily-20251212/FEEDBACK_BC.md)已补15项潜在、10102误关、Replication必要反证与12–13未授关系，原CL/DC/CV有界段只补26项精确v1题摘；原133有效层保留。原始RSS恢复及小时精度/27页关系已同步，不无限追时刻。两Google限定校准可复用；root实际Ch66两段/来源家族与Popper真实POST已同步，日Gate已通过，实际范围与边界见§6。

**终态保留项：** GPT5.2两RSS原字段均Thu, 11 Dec 2025 00:00:00 GMT→12/11 08:00BJT，按字段在窗前，但未确证历史小时精度/与精确27页first-public关系；原HTML403、当前card转后续Safety Hub，不能冻结旧稿或授12/11确定候选。重开需具名原始timestamp/可访问界限与27页版本对应。arXiv原表及反馈新增精确ID/v1缺first-new；Replication缺时区/公开范围，12与13均未授；第二节滚动/动态目录仅未显示部分保留。可读题摘/core已处理，不因缺日期列未读。API/OAI是提交/修改，月字段与日空不证明零；只接受匹配ID/v1原始new RSS/email/list或正文范围完全落窗，目录只需12/11–12缺段，定点重开不扫全月。

所有终态保留项不支持正面证据、Books或无遗漏断言，不正面采用、不进入Books、不支撑Coverage/Evidence通过或安全/性能保证。20:00EST若实际公告恰在次日09:00BJT右端，归下一份Daily；不凭排期套个体。Replication不再以12/12日标签证明窗外或强移13，只有公开范围恢复才定点路由。

## 6. 复核

复核者：Popper（主线程委派的独立非作者agent；不是作者Plato或Books写入者root，不使用共同chat ID）。
结论：通过

检查时间：2026-10-02T20:46:57+08:00。Interactions API实际owner已有覆盖，DeepSearchQA实际两段POST及作者§1/3/4/5真实同步已核；新增26项精确v1题摘全部独立读取，B/C修复已核。用户随后窄授权§5既有终态否定句收束，普通差额0，日级独立验收通过；最新完成检查时间见metadata/root追加。详见[ROOT_ADMISSION_REVIEW](../_sources/daily-20251212/ROOT_ADMISSION_REVIEW.md)，不以作者ready或机器通过授内容通过。

实际范围：逐日重读AGENTS、研究/报告合同、每日来源用法、Prompt、ROADMAP与相关state；读README、SOURCE_SCREEN、ADMISSION_CALIBRATION、EVIDENCE_BOOKS及晚恢复记录。两Google完整核心及原始JSONLD实际读取，均datePublished=2025-12-11T17:00:00+00:00，日标签和modified不替代published；DeepSearchQA当前16页技术稿首页、必要§1–3/§4评价与失败/§5.1实际读，不认证历史字节冻结或排行。核Ch84 52–96、Ch83 100–108/245–257、Ch82开篇及Ch66 Context/FACTS/RAG实际段、inventory段、Ch65/67开篇：平台权威状态与终态证据已承载API的限定职责差额，不证明该beta实现durable/幂等/取消回滚；检索信息覆盖和expected-fact inventory不等最终entity-set的strict equality/extra-items合同，DeepSearchQA不判全覆盖。

GPT5.2发布核心与精确27页PDF必要§3.3/3.7/Table6、Ch66 14–112及Context段实际对读，局部缺输入×严格输出反证保留，不信生产均值等价该切片；未授本窗/评分/Books。官方RSS本次HTTP200并解析两个精确条目，原pubDate为Thu, 11 Dec 2025 00:00:00 GMT，不再支持“RSS替代全失败”；当前card页转向后续Safety Hub，条目字段不能直接冻结27页原稿first-public。原值按字段换算为12/11 08:00BJT（本窗起点之前），实际首次可访问精度/稿关系仍须具名解释或安全隔离，不擅自挪入11候选。

原133项精确v1题摘全部重新取得原站可读内容，10363/10365输出缺片另重取；10522原摘要尾缺失不补造。另读作者自己CL326–375/DC76–100/CV1076–1175段里的17项及两个晚段locator题摘，15项遗漏/误关潜在需补，见独立表。必要正文抽检10102 §1/4/5.3及Table3、09730 §2/4/5/6、10440 §III/IV、10080 PDF必要§5/7/8；10102有parent-ID metric与多pass/GT初始化边界，撤销“只有任务/库存”关闭。10080无独立新验证保留关闭；10440披露模型内层改写但无可核版本/接口/受控实现，闭于主张证据不足，不闭于成熟组合。Replication原核心/replication procedure、redteam/audit非assistant边界与讨论实际读，不能只看12/12标签就宣称证明窗外或忽略安全反证。

分层来源/负侧：实际重开DeepMind正确历史page/4、Alignment目标December→November邻接，核AISI合作无新增技术评价与OpenAutoGLM multilingual核心；科学数学案例按ROADMAP暂缓范围停止。Seed两类2025接口及Meta/ZAI/MiniMax同一固定目录字段复用本次此前实际读取，只重新选择本窗相邻身份，不继承前日完成。CL/DC/CV原始有界列表实际取得；临床诊断、传统ID/领域评论仅核明确范围外标题，不冒称全文负样本。

当前普通差额0。用户窄授权后只明确§5已有终态“不支持正面证据、Books或无遗漏断言”，未改变潜在判断、日期或Books。新增26项全部精确v1完整可读题摘HTTP200并独立核：10780输入script/语义识别与最终分类分离、09626 seq-length=1仍含时窗特征、10244 softmax置信阈值导致未标注样本零使用等潜在边界合理，不按领域或成熟组合关闭；原133层、15项恢复、Replication/RSS具名终态和真实DeepSearchQA整合/POST同步均闭。无需重写Books、扩全池或恢复所有外部日期。

未检查边界：未全量重放14源查询，未独立重扫LG/AI/AR或其他CV页/全月库存；未全读133+15+26项正文/附录/代码、未跑模型或API，未恢复逐篇first-new，未读27页card所有附录。Replication必要附录A/B/C本会话13日核验可定点复用，未全读其他附录。DeepSearchQA实际新段、前后gold/exposure/Context及Ch65/67开篇已核；仅结果协议不证过程或开放世界穷尽，当前PDF不认证历史字节。两个DC晚段locator仅查停止边界，不变成本窗候选队列；不凭月ID授窗外。真正穷尽first-public可安全终态，不等Coverage/Evidence通过、零事件、性能或安全保证。

机器检查：本次只改metadata/§6、root记录及用户新授权的§5终态否定句；Books只改新增DeepSearchQA末注POST状态，未改正文、index/state或其他日正文，未stage/commit/push。完成态V3/本地引用/限定空白及窄句范围保护实际结果见root最新追加；机器不替代上述语义验收。
