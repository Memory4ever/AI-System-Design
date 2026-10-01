# 2026-09-21 arXiv 恢复与贡献单元（进行中）

- 执行人：`apr01`；2026-09-27 实际恢复。仅维护本日过程材料，不改正式 Daily 或共享 Books。
- 真实窗口：`[2026-09-20T09:00:00+08:00,2026-09-21T09:00:00+08:00)`。
- 已亲自完整读取当前 `AGENTS.md`、`CODEX_RESEARCH_PROMPT.md`、三份研究/来源/Report 合同与 `ROADMAP.md`。按当前贡献门槛判断，不继承旧 Complete 或旧候选总数。
- 当前状态：来源 New/Cross 批次已恢复；贡献筛选与必要证据仍有普通待办。不是本日或 W39 完成。

## 1. 官方批次与实际恢复范围

实际重新读取十二个 `https://arxiv.org/list/<category>/recent?skip=0&show=2000` 入口，仅提取 `Mon, 21 Sep 2026` 组。独立取得 CL87、LG149、DC17、AI125、CV98、RO114、AR6、PL1、OS0、PF6、IR8、MA7；跨分类唯一身份 **475**。每页目标组完整到下一标题/页尾，`show=2000` 覆盖实际页面总数。ID、分类与原始题名存于 [本日标题底稿](./arxiv-mon21-titles.md)。

公告标签依据来自 [09/22 恢复记录 §1–2](../daily-20260922/arxiv-recovery-20260927.md)：实际 `/new` 与 `recent` 同名日组126个身份完全对齐，结合 [arXiv 官方公告规则](https://info.arxiv.org/help/availability.html)，Mon21 对应 Sunday20 20:00 EDT，即 **09/21 08:00 北京时间**，不是 Monday21 20:00 EDT。本次475身份重新取得并与该记录一致。提交、OAI updated、DOI created 均不单独充当公开时刻。

这修复旧日报的零 arXiv 断言，但只证明合同十二分类可见的 New/Cross 批次。历史 Replacement 原清单仍未恢复，不能据此宣称所有修订没有更新。题名范围浏览用于查漏；475不是贡献分母、475篇完整摘要或全文审阅队列。

宽列表也含早于本月的永久ID（例如2310.03860、2312.01020、2412.07151、2511.16923、2605.15418、2608.27259）。官方规则说明ID月份在first announcement时赋予，因此它们的原家族不是September21首次公开；本次Cross listing不创造新首发。明确领域应用可范围关闭，dSTAR等主线旧家族若有具体重要revision信号再定点查当前说明，不无差别补完整版本史。

## 2. 旧67项迁移：保留证据，不继承完成标签

[09/22 恢复记录 §3.1](../daily-20260922/arxiv-recovery-20260927.md) 已实际读取68项完整精确题摘，其中67个 v1 全在上述 Mon21 组、0个在Tue22组。本单元复用其具体题摘准入问题，迁移到真实09/21事件；不把建议 owner 当作 Books 已覆盖。

- `2609.22000v1` 与09/21既有 RecreationWorld 官方发布是同一家族，paper用于补证，不重复家族计分。
- `2609.12748v2` 属 Replacement，纠错正文有具体证据，但公告归属未恢复；不自动算进本日67项，也不按 submitted 时间回填。
- 旧 `evidence-notes.md` 声称读过25篇但没有逐篇精确 locator；只有本次实际重新打开且能对应正文的项目才计审阅完成。原始记录仍保留于旧目录。

### 本次已经重新完成必要正文并核实际 Books 的三项

| 家族 / 精确正文 | V2 评分及最低投入 | 实际证据与边界 | 当前 Books 对账 |
| --- | --- | --- | --- |
| [2609.20830v1 — Reviser](https://arxiv.org/html/2609.20830v1) | 2+2+2=6；实际知识缺口深入例外 | §6.1–6.2/Alg1、§7与§8.1：INSERT/MOVE/STOP的因果动作历史更新可变文本；实验没有 canvas encoder、DAgger/RL，也没有真实serving吞吐。30B action tokens不等同30B最终文本tokens。 | Ch24“Autoregressive 不必等于 Append-only Final Text”实际承载该分支；工程KV/rollback身份判断与作者实验分开。本次作者对读完成，非作者日Gate未完成。 |
| [2609.21058v1 — Kernel addressability](https://arxiv.org/html/2609.21058v1) | 3+2+2=7；深入纠错 | §2–3、§4.2–4.3、§5–6：真实模型wall-clock share限制搜索价值；absolute tolerance能错收近零/不完整写出的结果。scale-invariant relative检查、operation invariants与写出比例分账，不能把oracle通过当生产正确性保证。 | Ch49实际正文 addressable fraction 与 correctness admission 已存在；A10080GB/BF16/具体KernelBench和软件范围仍须保留，未采用普遍性能数。作者对读完成。 |
| [2609.21079v1 — DLB](https://arxiv.org/html/2609.21079v1) | 2+2+2=6；实际知识缺口深入例外 | §2–3：cell root/leaf层次、P2P probing、时延模型、boulder离散/sand渐进分配；drain是Little型近似模型，不是即时恒等式。内部22个月部署不构成公开通用SLO。 | Ch56实际路由正文承载模型/观测freshness、endpoint admission及fallback；并非只见marker。作者对读完成。 |

其余旧64项仍是须按具体问题继续的工作信号，不谎称64个已冻结候选或全部已完成Evidence。审阅完成后才能填写最终处置；普通待审不标外部受阻。

## 3. 首批补漏题摘与最小消歧

已完整读取官方 `/abs/<id>v1` 的12项题摘：21113、21407、21672、21704、21899、21960、21325、21484、21515、21996、21299、21465。以下为实际作者裁决/待办，不是冻结分母。

- **21113**：representation drift 与 EAP 定位的重要性不等价、跨任务共享组件不保证transfer，具体测量反证可准入；只按EAP代理范围，不称找到完整内部因果真值。精确v1题摘已读，必要评价普通待审。
- **21407**：量化denoiser的历史窗口→Gaussian observation/prior→Kalman后验纠正是具体采样机制，可准入；需要核必要假设与反例，不由W4A4收益推广到所有采样器。
- **21899**：finite-n exponential-noise BoN分解与GSI交接，可准入待必要公式/预算边界；估算compute不等真实wall-clock。
- **21960**：tau-leaping因子化误差与依赖profile调度的常数/阶数分离，可准入；正则profile条件不可删。
- **21484 / 21515**：分别是密文端response-return控制和公开monitor盲子空间下受限read-factor admission，准入成立且保护合同深入例外。root已独立读完整摘要校准；仍需必要方法/证据，不泛化到全部后门或任意guardrail。
- **21996**：内部识别与concealment/unlearning的测量分离，可准入待必要协议；候选答案/可用标签依赖须查明，不能把probe成功叫内部知识真值。
- **21325 LEGIT**：题摘中的signed config/task/budget绑定、cost测量是成熟身份原则，Sybil deposit/fee为市场机制。拟贡献前关闭，root已校准此范围；若最小必要段存在新的可执行acceptance/失效合同再重开，不说credential本身无价值。
- **21672 L0-MoE**：已最小读§2 Eq1–3、§3.1–3.3与限制，实际不只有速度数字：domain curriculum与冻结non-MLP、独立L0 expert构造/拼装是具体分支。保留为待目标Ch21实际对照的工作信号；sequence-domain/token-router exposure偏差、总参数和naivePTQ执行路径成本不能藏。不能沿初读“仅速度”关闭。
- **21299 BrainAPI**：最小读§3–4与§11.1–11.6。OPA到scalar/quantifier DSL的覆盖缺口与Cedar default-allow/default-deny极性错误是具体语义可移植性反证；审计记录并不自动提高正确性，ranking/context尚未完整实现。保留待Ch84/Ch72实际命题比较，不因“已有治理原则”关闭。
- **21704 SpecQuant**：最小正文页列 ICPC2T 2026-03-11～13、DOI `10.1109/ICPC2T68221.2026.11646348`。已实际读[官方Crossref同题记录](https://api.crossref.org/works/10.1109/ICPC2T68221.2026.11646348)，published-print=`[[2026,3]]`，activity start/end=03/11–13，created=08/19。更早March正式同族已确认，不计September新首发候选；不假造March精确日，更不以created推公开。正文路由/量化/验证组合本身也不证明新的exact采样保证。
- **21465 OmniVChat**：题摘与精确PDF p1–7已实际读，生成脚本/渲染证据/参考回复、tier分数、fixed-reference-history与single-turn human probe已分账。后续PDF读取连续截断，reward/评价必要段仍普通待办，不把已可读机制写成整篇不可取。

### 首批之后的真实数量更新

另完成有界完整题摘消歧，总共本轮53个身份，见[逐项裁决](./arxiv-title-abstract-screening.md)。实际交集21299/21465属于旧67未决重开，**真正额外51，合并完整题摘层118**；不能重复计成120。新51作者工作裁决为9具体贡献前关闭、1更早家族关闭、41待必要证据/处分信号；与两条旧未决一起本表43工作行。尚未冻结贡献分母，没有把118或43都认作真正长期候选，也没有将所有宽列表无关项送全文。

必要证据/Books对照准备到三项旧实际正文和三项新精确提案（21484/21515/22083），见[精确队列](./books-queue-restoration.md)。其他部分源阅读保留具体范围，不继承旧“25已读”的完成数。

## 4. 普通下一步与外部保留项

1. 对旧64项先以完整题摘的具体增量再校准贡献；只有真实准入且需处理的项才进入必要证据与真实owner对照，不把旧64/139工作信号自动成为全文队列。不机械把旧25阅读标记复制为完成。
2. 对标题底稿的明确主线/含糊信号读取完整摘要，贡献判断后才评分；不把475全部送入全文。
3. 已核三项Books真实写入交root做有限非作者采用/写后复核；没有授权自行改共享章节。
4. Replacement原批次与12748v2公告仍为具名日期缺口；SpecQuant更早公开身份已关闭，不再列本日普通待核。其他普通证据不随具体缺口停止。

## 5. 当前可验收范围与精确接续（2026-09-27 10:43:35 北京时间）

- 来源恢复完成的范围：12类Mon21 New/Cross 475唯一题名、new/recent+官方公告clock与真实日窗口；不是历史Replacement全集。
- 贡献工作完成的范围：有效复用旧67完整题摘与逐问题索引；本轮实际53完整题摘（2旧+51新）及逐项作者裁决。9前关闭+1更早家族有具体依据；关闭侧仍需非作者分层抽查，不能称全475摘要已审。
- 单篇准备：旧3实际正文对读完成；HE/ServeGuard/MintAct 3必要来源与真实owner差异已具精确提案。旧67中除已核3外的64工作信号仍须按真实增量继续，51新中41工作信号仍未全部评分/审阅/处分；两旧未决也未伪装完成。准备包不是日终态。
- 接续优先：root有界独立核6单篇（3旧源/body+3新提案），实际批准后协调共享章写入；再对题摘工作按评分最低投入分流。无需重抓已恢复475题名或重复读已核方法。
- 外部日期保留：原Mon21 Replacement清单与12748v2公告时刻；只重开此具体事件，不用submitted/updated代替，不扩大到全年。
- 检查范围：本日作者材料和本地链接/数量/空白；非作者贡献/采用/日Gate尚未通过。正式Daily与Books没有被本子任务改写。

本次只新建5个日内材料文件；既有暂存的books-queue.md、evidence-notes.md、screening-ledger.md原状保留，没有stage/commit/push。53表行、475标题行与交集2核对通过，Books目标路径存在；scoped diff与5新文件no-index空白检查均无错误输出（新文件差异exit1不等于空白错误）。结构校验不能替代未完成的语义/证据Gate。

本文件不是最终Report，尚有可执行工作；尚无本日独立语义Gate。
