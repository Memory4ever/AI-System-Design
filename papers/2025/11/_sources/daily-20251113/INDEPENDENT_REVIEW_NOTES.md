# 2025-11-13 独立复核 Notes

复核者：Codex，非作者；作者：Planck。author != reviewer。

检查时间：2026-10-04T15:54:24+08:00（工具实际 clock：2026-10-04 07:54:24 UTC）。不是沿用作者手填时间。

结论：日级未通过，须定点修正后回交；不授 daycomplete，不修改日报状态。

## 1. 范围与顺序

本次 fresh 重读 AGENTS、当前 RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES 使用说明/每日/按需/arXiv、CODEX_RESEARCH_PROMPT 与 ROADMAP 相关 owner。仅加载 11/13 报告及本日材料。先核入口、停止范围与准入，再核 Project Fetch 日期/证据/具体 Existing，最后核六部分和 validator。

复用 FIRST_CALIBRATION_READY 记录的 root 首批 8 份完整题摘校准（7 项潜在贡献、07641 sentiment application 关闭）；未变化部分未重新全文审阅。复用的是准入层，不把首批作者 Evidence、日期或 Books 自动授通过。本次没有重读首批所有附件，没有加载他日历史报告反推候选。

## 2. Project Fetch：单项通过

- 身份与日期通过。亲读 [官方正文](https://www.anthropic.com/research/project-fetch-robot-dog) 的实验、结果、限制与 footnote 3，并核 [原正文记录](./raw-web-16.json)。对 [保存的官方 Research HTML](./raw-anthropic.html) 和本次 live 官方 Research HTML，结构化解码 Next/RSC JSON 后，递归定位同一对象：`slug.current=project-fetch-robot-dog`、title 与 `publishedOn=2025-11-12T18:19:00.000Z`。不是邻近字符串拼接。换算 BJT 11/13 02:19，落在 11/12 09:00 至 11/13 09:00 窗口。
- 准入通过，采用命题与 1+2+2=5 相容：接入/编程辅助收益不能替代自主物理闭环成功。这是局部评价边界的实际证据，不因是机器人应用准入，也不因 Books 已有覆盖关闭贡献。
- 必要证据通过。两组各四人、单日便利样本；7/8 与 6/8 是子任务数；约半耗时只针对双方都完成的任务。主要收益是连接与传感器接入，自主取球未完成。控制器不等价、对照获连接提示、视频接口不同、坐标/背景识别问题都限制归因。近碰撞来自人的速度/距离命令，不能归因为自主模型决定。正文与报告没有把此实验推成普遍 2x、生产安全或未来能力预测。未披露配置不补造；未核实现、未复现。
- Books Existing 通过。[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 的开篇 proposal/controller 权限分离、`Evaluation ladder`（当前约 872 行）及其下真实机器人结果绑定项（约 894 行）具体覆盖局部进展、重复成功、恢复、安全/干预、部署证据的分层，以及 demo 只证 feasibility。定点读取相邻 Ch25/Ch27 与 owner 交接，不仅匹配章节标题。`MULTIMODAL-EMBODIED-VLA` 是 ROADMAP owner。无需添加 Project Fetch 名称或制造 Books diff；实际写书 0，没有 POST。

GPT-5.1 是另一保留家族，不是 Project Fetch 的名称、来源或确定日期证据。

## 3. 追加准入与代表性关闭

亲读 [第一组精确 v1 完整题摘](./raw-exact-ab-2511-07776v1.json) 和 [第二组精确 v1 完整题摘](./raw-exact-ab-2511-07689v1.json)，核 13 个身份的 HTTP 200 / response_url 与 submission history。其中 12 项潜在贡献校准通过，暂不授日期、Evidence 或 Books：

| 身份 | 可继续核验的具体增量 / 不得越过的边界 |
| --- | --- |
| 07776v1 STeP | 动态 routing/memory/shape 执行抽象；性能仅 cycle-approximate simulator |
| 07869v1 Autospeculation | 同 oracle、sequence-level speculative rejection；any-order conditional marginals / diffusion conditional means 与 bounded-support 等理论前提不能换成普通有限参数 CLM 的实测加速 |
| 08083v1 HipKittens | tile 接口通用不等于 AMD 实现与 schedule 通用；作者 Nov11 无时区博客的更早公开问题须保留 |
| 08086v1 Dynamic Sparsity | ground-truth dynamics 反驳全局先验，保留局部 state/contact 结构；不采用 Nov14 v2 |
| 08113v1 Cross-modal composition | 单项模态能力不认证组合能力；cascade 信息/预算公平性待审，v2 submission 不认证本窗公开 |
| 07689v1 Factuality stress test | 保义变换与 claim density 暴露长文指标失效；变换真保义/预算仍待核 |
| 07691v1 CAPO | confidence-based loss scaling；reward accuracy 不是人类生成偏好增益 |
| 07732v1 ViPRA | actionless pretraining 与 robot-specific action decoder 分工；100–200 示教、22Hz 不认证零样本闭环 |
| 07772v1 SALT | CoT 泄漏人口与 test-time steering；安全/隐私必要深入，改善幅度不认证隐私安全 |
| 08525v1 Monitorability | verbalization 与 monitor reliability 分开；安全/反证必要深入，监测成功不反推真实因果 |
| 08389v1 Speech fusion | 跨 model/layer 接口与 upstream selection 归因分开 |
| 07931v1 SpeechJudge | naturalness judge 与人类偏好失配；BT、公平预算和 @10 成本待核 |

本轮只是准入校准，不核上述理论证明、全配置、消融或实现。拟评分可沿用 NARROW_CALIBRATION_READY 的局部命题；将来日期成立才推进相应审阅，不为日期缺口先造全文队列。

3D4D 08536v1 当前范围关闭通过。完整摘要及 [System Framework / Rendering Video / Evaluation](./raw-web-18.json) 已读：PLY 序列、WebGL/Supersplat 编辑、VLM importance map 到 shader 的精度分配是实际 graphics/frontend 增量，不能说它完全没有资源策略。当前原文未建立新的模型训练目标、action-conditioned dynamics 或模型推理执行接口；60fps、CLIP 指标也没有建立模型系统主线所需关系。关闭理由限定为这个具体差额，不以 Demo Track、领域名称或未证明真机安全排除。日期不影响此范围关闭，不反复恢复日期。

## 4. 来源有限停止与负侧抽检

逐行核对 README 的 14 Daily 来源记录与入口身份；不是 14 个完整历史库已恢复。原入口 [raw-web-00](./raw-web-00.json)、[raw-web-01](./raw-web-01.json)，补入口 raw-web-10/11/12/15 的日期/分页片段均定点核。当前 6 行“已检查”、8 行“受阻”是报告记录数，不是完整覆盖通过数。

具体原样本：

- Seed 四份 JSON 的实际 ArticleType、PublishDate、18/18/18/20 行、next token 与 has_more=true 已核；p0 已跨过窗口，p20 到六月/更早，停止 p40 有界合理。文件名 `raw-seed-papers-p0` 实际 type2；没有声称全库已尽或历史无删除。
- Hunyuan 原 JSON 的 totalNum=9 与 2026 blog 身份已核；不代替历史 Research。Meta/Qwen 空文本、旧 Qwen Sept23 与新站空页不认证零发布。DeepMind page2 的当前内容不算已恢复历史第二页。
- Moonshot 原页面实际 **26** 个日期条目（链接编号 0–25），不是 README 的 28；Nov7/Nov6 边界成立。这是小计数错误，不改变停止理由。ERNIE 第二页 Nov11/Nov7 与 2/2，MiniMax Dec23/Oct27、MiMo dated Paper 与 undated Blog 的分开记录可保留；无删除保证未授。
- 四主题 XML 的实际 query、totalResults 与 entry 数核为 92/92、16/16、29/29、25/25。原错查询 total28897/只100条不是有效负覆盖；“revisions”原响应实为 submittedDate、131/100，不证明修订覆盖也不要求按错误入口读余31条。实际类别还包括 CL/LG 等交叉类，README 类别概括不应当作精确 query。月份 CL ID 切片不是日公告，81/33 标题也不变全量题摘池。
- Orion DataCite 与 OAI 的 Submitted/Updated/registered/month-Available/datestamp 身份字段定点核；它们不合成首次公开下界。其余 18 个已识别潜力身份同样不凭 submission 授落窗。后版本增长不能当重要修订证据。
- raw-web-29/30/31 的有限失败与精确重开条件可以终态保留；04/05 无原 query 的空检索不作负覆盖。GPT-5.1 midnight RSS/current card 和空 commit 返回保留，不扩大论坛或他日任务。

负侧采用分层抽检，不无差别重读全部附件：复用 root 的 07641 sentiment application；追加读现存 XML 的 Auto-US 07748v1 与 TurkEmbed 07595v1 完整摘要，当前只见领域分类/模型组合或既有训练法迁移，可范围关闭，未据此否定医学有效性或多语价值。安全/设计反证信号另见下面普通缺口，不把它们作为一般应用关闭。

未检查范围：未重建动态历史库、未全扫 arXiv 学科/月表/676 条 Google pubs、未对首批七项做第二次 Evidence/Books 全审、未核 12 项新增方向的全文或代码、未复现实验。历史缺段按原有限尝试与精确重开隔离，不能冒充全网零命中或无遗漏；这些外部保留本身不要求无限重试。

## 5. 普通可执行缺口：交 root / Planck

1. **JAX-Privacy 博客的筛选未闭合。** README 37 行“博客独立新差额未确认”与 81 行“July release 不属于本窗”只能处置 artifact 身份，不能处置 [11/12 官方博客](https://research.google/blog/differentially-private-machine-learning-at-scale-with-jax-privacy/) 本身。raw-web-07 已有可读核心 104–143 行：DP primitive/相关噪声、分布式 batching、accounting/auditing、Keras/Gemma 示例；July release body 也已给 DP-SGD/Keras/examples/DP-FTRL/accounting。请用这些现有核心记录，明确博客是否仅重述已有 release，或哪项独立接口/有效性边界仍有潜力。不能仅凭 July 日期断言整个博客无新贡献；也不能把这个尚未作出的筛选判断标成“外部缺段”。只核该已发现身份，不扩 JAX runtime 或历年目录；若决定所需具体原版本确实不可得，再明确缺什么及终态重开条件。
2. **负侧主线信号未给出终态。** 现存作者 XML 已发现 `07876v1 LoopLLM`、`08487v1 Agent Safety/OASIS`、`08568v1 DLRM tiered memory`，但当前 FIRST/NARROW/EVIDENCE/README 没有具体筛选处置。本次亲读这三个 v1 的完整 API 摘要：分别有低熵重复引起能耗/延迟攻击、意图隐藏/复杂度混杂的安全评价反证、embedding cache/prefetch 的模型内存机制。它们不能以普通应用或不属 LLM 关闭。请定点记录准入/具体关闭，日期未定则纳入相同隔离与精确重开条件；**不要求先展开全文或补造公开日期**。另抽到 `07645v2` dynamic safety、`08484v2` policy patch、`08003v2` VideoLLM pruning，只有当前 API 晚版本摘要，不能冒充 v1；需说明这些已发现信号如何被版本/日期范围处置，不用这次 v2 内容反推历史贡献。只重开这组实际信号，不扩整批92。
3. **报告同步。** 修正 Moonshot 28→26（若另有原记录支持28，给出定位）；将已通过的 Project Fetch、12 项准入、3D4D 关闭从“待核”同步，来源与候选分母在前两项处理后才能冻结。六部分结构已齐，但 §5 普通工作与 §6 尚未收束；普通缺口不能混入日期终态保留。root/作者同步时取实际 clock 更新 metadata，不沿用本 notes 时间当未来检查时间。

## 6. 验证与权限

当前进行中 README 的 `python3 scripts/validate_research.py --report papers/2025/11/13/README.md` 本次实际通过。仅接口一致性通过，不是完成态或语义通过；本次不改状态来制造完成态校验。

仅新增本 notes。Ch26 运行前已有共享修改，未触碰；Books/月索引/state/他日未修改。未 stage、commit、push。前三节单项通过可复用，日级仍未通过；修正上述定点缺口后只回核变化与最终六部分/validator，不重复本次已通过附件。

## 7. 三项返修局部回核（2026-10-04）

检查时间：2026-10-04T16:24:18+08:00，工具实际 clock 为 08:24:18 UTC。仅核 [REPAIR_READY](./REPAIR_READY.md)、新增原材料 raw-web-32-repair 的精确 tag README 必要段，以及 README 改动的结论/来源行/§5/§6；未重新审 Project Fetch、追加12项或首批附件。

结论：**原三项问题返修通过**，此前 §5 问题按以下依据收束，不把历史未通过记录删掉或冒充新全量研究。

1. JAX 博客已对 primitives、DP-FTRL/相关噪声、batching、auditing 分开作具体差额判断；精确 tag README 支持框架分层、DP-SGD、Keras/Gemma 入口，高层 DP-FTRL 仍 future；链接 main 不认证 July 具体代码。作者没有把 auditing 合成 July 已有，关闭依据是博客未建立独立的新机制/接口/有效性边界，不再仅凭 July 日期去重。这个有限贡献关闭可以通过，不需继续恢复不影响处置的日期。
2. LoopLLM/OASIS/RecMG 三份 v1 的机制与反侧保留正确，加入相同首公开隔离；没有借摘要授安全或性能，也不因 DLRM 非 LLM 关闭。三个当前晚版明确不反推 v1，缺的是必要首公开链而非声称 v1 下载永久不可执行；日期终态保留不扩全文队列。22 个潜在贡献日期家族与另3个晚版信号分开，1 个确定落窗候选的分母相容。
3. Moonshot 26（0–25）已纠正；报告六部分同步了已通过层与终态保留、不支持正面证据/Books/无遗漏，以及精确重开条件。仍保留进行中/未通过，作者没有自授完成。

当前 13 进行中 validator 本次实际通过，不冒充完成态校验。原三问题不再阻塞 root 依据累计独立结果收口；本回核不直接修改 §6 结论或状态，正式复核/状态同步与实际完成态 validator 由 root 处理。只追加本段，未改共享 Books/state/month 或报告，未 stage/commit/push。
