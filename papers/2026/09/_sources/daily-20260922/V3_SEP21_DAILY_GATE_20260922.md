# 2026-09-22 Daily 有限独立复核

复核者：`sep21_resume_v3`（非本日报作者）。依据：当前 V3 Research/Report 合同；窗口 `[2026-09-21T09:00:00+08:00, 2026-09-22T09:00:00+08:00)`。

**结论：未通过。** 已有 53 家族的有效单篇证据及实际 Books 结果可复用；分层排除抽检发现七条具体误判，须局部处理后才能冻结最终候选、通过日级验收。七条是普通可执行工作，不是外部受阻，也不是需要重审全部 1746 发现记录。

唯一作者接续点：[当前正式日报](../../22/README.md)、[当前 reconciliation](V3_RECONCILIATION_20260930.md)。本文件只维护独立检查结果，不另造候选账本、不修改 Books 或共享学习状态。

## 1. 来源入口与停止范围

已核日报 §2 的 14 个 Daily 来源及表外 Harvard H-Spec 官方事件；读取当前来源合同使用说明、Daily 分组及实际适用的 arXiv 主题说明。没有扫描 Weekly 来源。复核了 [arXiv 恢复 §7.1–7.8](arxiv-recovery-20260927.md) 的入口、原始身份、有限题摘及停止位置，以及保留的机构入口记录；不把恢复文件此前其他日期的身份块当本日材料。

arXiv 本轮 1003 New、183 Cross、560 Replacement 的 1746 原始身份是宽发现边界，不是候选数或全文队列。官方十二分类窗口批次、New/Cross 的完整身份恢复与历史 Replacement snapshot 分开；当前 Tue22 公告 08:00 BJT 属本窗，Submitted 不代替公开时间。主题检索限定模型训练/推理、GPU/kernel/graph/并行/KV、模型与 Agent 执行机制；宽列表只作有界标题查漏。不能将这些记录宣称为全学科召回。

Google 年级目录、Qwen/ZAI 动态目录、MiMo 仅日期级发布及其他不可恢复的日内时间边界已在日报隔离。只有 09/22 日期而无日内可见时间的 Opus/Astra/ZCode/MiMo V2.6 等不能假定 09:00 前公开；这些隔离项不支撑零命中或覆盖保证。OpenAI 旧零命中已由窗口 RSS/官方核心说明纠正；第三方研究计划的权限/利益冲突/预注册/发布原则，不等于新增已验证的检测机制或运行安全保证。

H-Spec 保留更早官方网页事件 03:00 BJT；MiMo tool-flow #2456/#2463 按官方精确事件时刻和同家族处理，而不是模型发布日反推。来源检查记录可复用，但日级准入完整性尚受下述误漏影响。

## 2. 53 项正向结果的复用合法性

当前工作表 53 家族（42 整合、8 已有覆盖、2 仅报告、1 争议暂缓）不是配额，也未在七条重开之后冻结。已独立对读旧 38 的身份、精确版本、必要机制/对照/反证笔记与当前具体采用命题：26 份单篇证据、11 项 additional-evidence 和 WaveFront 自包含证据；不使用旧 Complete 标签代替复核。旧目录的日期归档错误由当前日报公开事件修正，不改变已核必要方法。旧 22170/23305 笔记的普通待办快照不冒充完成，采用当前后来完成的有效证据与实际正文。

旧 33 项整合的 actual body 与邻接均已定点复读，覆盖：22870、24322、23536、23478、24362、24048、24969、23033、22170、24093、23305、23432、22115、22215、22359、22816、22894、22897、22910、23269、23310、23366、23640、23731、23976、24106、24194、24380、24504、24788、24885、24976、24996。不是仅搜索 marker 或 Review notes。没有发现需要撤销这些未变化采用命题的反例；同一 Stable Node owner 和前后交接仍成立。

旧 5 项已有覆盖的 actual 论点已核：22478 Ch66 的 run identity/数值可复算不等于同实验；22246 Ch76 的同源支持不等于独立 corroboration；24090 Ch81 的 reader certificate/journal 与未知依赖保守重算；24243 Ch72 的 controllability/monitorability/faithfulness/outcome safety 分账；24895 Ch84 的 anytime-valid acceptor 及其认证范围。不是以主题相似作已有覆盖。

其余 15 项按有效独立结果复用并对照本轮实际：H-Spec 既有必要源与写后；NSP 22755、SPLASH 23816、SPECTRA 24847、CKDA 24797 的 root 必要源/owner 与写后通过；Exactness 24942 中心 necessary criterion 未证，root 独立争议裁决不正面采用。未变化的这些单篇结果无需另一个人无差别重读全部附件。

本复核者完成其余九项必要原文→实际 owner，四项新增写后已通过：

- 22547v1：paired prompt multiplier simultaneous bands 与 conditional kernel；固定有限 k、prompt iid、点态渐近条件；实测截断率与假定概率修复的反事实敏感性分开。Ch66 实际修正后通过，不认证有限样本统一显著性。
- 23570v1：reference solver 的四 seed 平均 outcome 选择最佳 memory combination，不是挑 seed；42% memory-off 4/4 pairing 是 headroom，不是 oracle ceiling。strip/random 不能唯一归因为 instruction pollution。Ch77 实际修正后通过。
- 13718v2：同一 average/diagonal flow 的 global jump→re-noise→local 两 NFE；默认初始噪声与独立 fresh-noise variant 分开。Ch24 实际修正后通过；实机限定运行条件，不宣称所有任务优胜。
- MiMo #2456/#2463：whole-batch finish 前不执行、step-local FIFO、只读重叠、失败 cascade 的例外及完成副作用不可回滚。Ch78 actual 两段与邻接通过。
- 08151v4：Hit@1/MRR 改善而 R@10 未优于 BM25；parseable、模拟 utility 不等于 patch success。Ch76 实际 ranking/recall/效用分账可承载长期命题，因此 E；该版本数字本身仅报告，不新增 Books。
- 28021v2：prompt class 与 human corpus 不匹配；Table II functional 密度两类均高于 human，幅度/分类解释敏感不是方向反转。当前 Report/packet 纠正后 Only 通过，不采纳通用安全机制。
- 15322v3：intended arguments 评价不能补成历史已测；历史 names-only/binary fixture 未测 grounding，r≈−.11 不证明独立。Ch66 实际 trace/effect/outcome 分账 E；版本事实本身仅报告。
- 16859v3：固定 gold-positive 分母的 coverage×条件质量，与 FP/precision、reach/solve 分开；native/cascade 对照和固定 judge 不认证无偏或流式 latency。Ch66 actual E 通过。
- MPS 22991v1：完整必要 §3/4.3/5/6.2 已读；单 M2 Ultra、11 版本、bmm forward、CPU float64 oracle/CUDA 控制；post-hoc/inclusive guard 误阻、device-view offset 未测及 CUDA arange 故障均保留。深入 Only 通过，不把所测 shape/版本 guard 泛化为数值安全。

## 3. 必要风险 negative

16639v2 official abs 明确 withdrawn（作者 agreement 不足）：不准入、不评分。当前 Books 定点无该版本 marker/采用正文，root 清除依赖链写后有效；窗外 v3 正文恢复不自动恢复旧授权与公开归属。

15795v2 official Comments 为 title typo/manuscript unchanged；09646v2 为 reference/DOI/URL 更新而结果不变，当前具体 metadata 关闭合法，不展开未变正文。22419v3 已有限读必要 §5：DB engine 1.8.0 的修复/探针不形成新的长期 AI 系统机制，无正面 Books 采用，negative 通过。

12748v2 official 摘要已撤回因果解释，而非撤回整篇；request logs 不证明 delivery/causal use，shared substrate、page choice 与行为关联仍是主要替代解释。实际命中 Ch84:925–927 已有采用段，旧 §7.7 “无采用链”的概括不准确。现有段只承载可见性≠消费≠因果、缺 read log 不推传播、缺 outcome 不推效用，符合 v2 边界，因此不删除有效合同；作者已同步纠正。v2 公开 replacement 时间未恢复，保持精确 DateHold，不算本窗新正面采用；重开只需可核官方公告/历史 archive，而非 Submitted 字段。

OpenAI 第三方研究 official 核心说明已直接核：计划政策不等于已测安全/独立效果，贡献前关闭可以保留；不能据机构来源排除，也不能转成部署证据。

## 4. 分层排除抽检与七条重开

实际完整题摘抽检 **19 个具名 negative 样本**：7 个范围/应用/综合层（22358、24713、22814、22775、23009、23766、23130）；7 个旧 §7.7 贡献层（22091、22100、22106、22302、22712、23184、24815）；4 个设计反证/机制样本（22098、22101、22109、22135）；1 个旧 additional-evidence 的 23551。Conduit 的既有有限核心说明关闭结果复用，SPECTRA 已转正并计在 53，不重复作为 fresh negative 样本。

领域范围样本关闭仅限其实际问题：市政水数据/地震领域 surrogate/小型 spiking RTL/LispBM 微控制器没有直接形成本项目大模型主线的新机制；HERMES mempool 非模型通信；TriFleetRCA 和 vLLM synthesis 是已知方法的领域实现或未新增论证的综合。不是因小规模、单 backend 或缺 owner 关闭。22302 的医疗 proposal/action 与 cohort 权重是 EvalSpec 领域实例；22712 术语框架没有新综合证据解决具体分歧；23184/24815 的原题摘只给组合 operating point，不建立所声称 causal identification 或新流式质量边界。22106 PRQuant 的 contiguous permutation/static correction 避免 gather，已有 Ch49 actual physical layout/compatible permutation/backend 消费和静态 correction/fusion 分支可承载，局部增量不是单 backend 拒绝。

以下七项由本轮抽检具体重开，不能因已有主题、小模型或深审成本关闭。下表保留准入时的必要范围；后续实际复核结果见 §5 追加，不将必要源通过当成实际写后：

| exact-v1 | 原关闭遗漏的具体增量 | actual owner 差额与必要下一步 |
| --- | --- | --- |
| [22098](https://arxiv.org/abs/2609.22098v1) | parent-conditioned Markov head 的 edge acceptance 校准/path survival；without-replacement sampling 与 matching recursive residual 的 exactness | Ch48 只有一般 survival/budget 与 residual 原理；核条件头、残余证明及 matched budget/temperature/load 对照，不泛化成任意 tree exactness。 |
| [22101](https://arxiv.org/abs/2609.22101v1) | effective hard-negative 数而非原始 context length；softmax 检索抽象的 margin Ω√logN 边界 | Ch22 linear-Gaussian memory 极值压力不是同一假设/定理；核 N 定义、概率条件、alias/dilution 与 mitigation 证据。 |
| [22109](https://arxiv.org/abs/2609.22109v1) | shared LR 非 neutral、arm×LR/Adam 有效更新与 live/frozen selector 分解，LoRA/full-FT/MATH 的异质反证 | Ch31 一般匹配 data/step/LR 没有该选择反馈与调参干预；核统计 family、重复与幅度边界，不宣称所有 selective OPD 无效。 |
| [22135](https://arxiv.org/abs/2609.22135v1) | 跨三 omni 模型 read-best≠steer-best，paired random-direction 控制与层选择的具体因果 handle | Ch23 一般 probe≠语义不足；核方向/norm/任务/模型匹配及有限 crossmodal 外推。 |
| [23551](https://arxiv.org/abs/2609.23551v1) | 固定 token、token-distance-exact estimator、density-matched random paragraph null 区分 mere compression 与真实结构的 compression depth | Ch13 没有该实际对照边界；旧无 large-LM/serving 不是排除门槛。核干预/随机轴/跨 corpus 限制，不采纳普遍优胜位置方案。 |
| [22100](https://arxiv.org/abs/2609.22100v1) | 同次 query-conditioned forward 产生 soft memories+relevance，在固定总 token budget 内按 query 分配/omit；matched OSCAR uniform allocation 对照 | Ch76 一般 compression controller/shared encoder 非同义覆盖；核 allocator、训练/候选预算及质量/端到端 latency，避免按名称或收益数字准入。 |
| [22091](https://arxiv.org/abs/2609.22091v1) | dated/trigger commitment ledger、offline linkage 与 multiplicative relevance 保留；resolved trigger 与 scope finding | Ch77 actual body 一般 intervention/cue/authority 不能替代具体 prospective retrieval；15405 尾部 trace 不等于实际论点覆盖。核 ledger/链接构造及盲题、hard stratum/已解决触发负侧，不外推未发布 TriggerBench。 |

作者已获精确必要范围，处理只沿这七个身份，不新增查询或宽池全文。必要证据可能支持 I/E/Only/争议，准入本身不预判 Books；版本/公开日期仍须在正式 candidate 行核实。现有 53 的有效结果保留，最终分母待七项处理后冻结。

未核范围：未逐项独立复查其余宽列表标题/摘要关闭记录，未遍历 silent Replacement 的完整正文或全部版本史，也未无差别重读既有有效附件。分层抽检不能称为全量无遗漏；共同错误只恢复相关排除理由与依赖判断。

## 5. 机械检查与交接

本文件写后，`python3 scripts/validate_research.py --report papers/2026/09/22/README.md` 通过 V3 格式/一致性检查，正式 Report、reconciliation 与本文件限定 `git diff --check` 通过；新审阅文件为未跟踪文件。这只证明可判定格式一致，不改变本次语义结论“未通过”。未 stage、commit 或 push；运行前 staged/dirty 文件保持，未改作者 Report、Books、LearningState 或索引。

可复用终态：53 既有单篇结果、来源真实停止边界与风险 negative；普通待办：七项必要证据/Books 判断及可能的实际写后、最终分母冻结、日级独立复核汇总。不把材料尚未读完标外部 blocked，不把本审阅者本文件当日报作者自签通过。下一轮只加载变化的七项及 actual owner，不重跑上述未变化结果。

### 七项有限源→owner 与首两项写后（同轮追加）

非作者 sep21 已逐项直接核 exact-v1 的拟采用必要支持/关键反证与 actual owner，七项均支持局部整合；每项的 author packet 为 `V3_RECONCILIATION_20260930.md` R 单元，不复读未变 53 或扩大 negative inventory。

- 22098：§3/Proposition1、§4/Algorithm2、§5 的同条件与负侧、§6支持 Ch48 条件人口/同 draw-order residual 差额。actual 新两段位于 Verify Length 的旧 block 统计限制之后、37532 binding之前，保留 pre-draw、无放回、chain/target-only fallback 与模拟边界，实际写后/邻接通过。
- 22101：§3定理、AppendixA/C/D/F支持 Ch22 单 decisive/faithful decoder 的受限 softmax 极值压力，与已有 TAM 不是同一定理。actual TAM之后两段完整保 iid Gaussian、ρ/a₀/γ上界、有效 N、gate recall penalty 与跨零/边缘 CI，实际写后/邻接通过。
- 22109：§2–6/A/B直接核支持 Ch31 arm×rate 差额；θ₀冻结的是评分模型而非每轮 mask，TV n12交互不扩到 entropy/MATH，FullFT 不同硬件且无 frozen。拟两段 source→owner通过，待实际写后。
- 22135：§III/V/VI/VIII直接核支持 Ch23 单层扫描的 read-best≠steer-best；r阈值未过而 peak-gap条件过，H1失败、MiniCPM多层null。26x四层对单层含注入层数混杂，不采用为纯位置收益。拟两段 source→owner通过，待实际写后。
- 23551：§3/4.3/5/7及B.2/C支持 Ch13 固定token/p₁干预、精确距离与每步random轴对照；OWT real-random gap未定、三seed方向证据、flat小代价/无下游。拟两段 source→owner通过，待实际写后。
- 22100：Methods、KILT-SCR/matched OSCAR、消融与AppendixA–D支持 Ch76 固定B分配，而非一般compression controller同义覆盖。连续log-utility与nearest rounding proof不证明真实answer最优，也不含每passage候选bank cap；bank先编码及同16x更慢/更多peak memory必须保留，feasibility检查是工程要求。拟两段 source→owner通过，待实际写后。
- 22091：§3–6支持 Ch77 dated/trigger ledger离线链接与query-time算术rank差额；oracle抽取未构建、cos0/负值不保证提升、小W ceiling、13/16paraphrase与53resolved仅局部集合，不转action权限。拟两段 source→owner通过，待实际写后。

当前仍为日级“未通过”：首两项写后通过不替代后五项 actual write-after、正式新增条目/分母与普通0复核。原有效53与风险终态不重开。

### 2026-10-01 后五项实际写后

独立复核者 sep21 本次直接读取每项实际两段与前后邻接，复用已通过且命题未变的必要源→owner，不进行第三次全文审阅。五项实际写后分别通过：22109 Ch31:945/947，22135 Ch23:753/755，23551 Ch13:176/178，22100 Ch76:649/651，22091 Ch77:212/214。实际保留 frozen θ₀ 与动态 mask 分权、TV交互不外推其他selector、r阈值失败与 peak gap/注入层数混杂、random paragraph null 与 OWT 未定/flat损失、先编码 bank 的成本与 cap 工程验收非证明，以及 oracle ledger 未构建/负cos/小W/有限resolved和paraphrase边界。五处各有独立唯一 SF marker、来源链接，前后衔接自然，不把工程 fallback 当作者已验证实现。

至此七项必要源→owner及七项实际写后均通过。剩余普通工作仅作者正式六部分与60家族冻结同步、复核者对最终变化包/ordinary0核对；日级结论仍未通过，不能在作者同步前抢先验收。原53及风险 negative 终态不重开。

### 2026-10-01 最终变化包与日级结论

复核者：`sep21_resume_v3`（非本日报作者）。结论：**通过**，本段替代前述过程中的“未通过”，不是继承旧完成标签。实际重新核作者六部分同步：§3单一表头60行，新增七项正式题名/exact-v1/09/22 08:00公告归属、评分与深入例外/真实owner及actual状态一致；§4末七项支持、反证、实际写后位置自含；§1/§5/§6与唯一packet最后精确停点一致。计60家族=54深入完成+5标准完成+1中心争议；49实际整合+8具体已有覆盖+2仅报告+1暂缓，无普通待审阅、Books待写或写后队列。

原53全部正向 identity/version/claim/actual采用复用、14到期来源和H-Spec表外实际入口/停止边界、具名风险negative、19项分层排除抽检及共同错误仅局部重开七项，分别沿本文件有效复核不再无差别重读。七项本轮源→owner与七项actual写后闭合，原风险negative结论不变。DateHold、动态/年度目录的缺口及24942必要性中心争议维持隔离：不计日期未定候选，不支持正面机制/安全性能或互联网无遗漏断言，精确重开条件自含。普通工作已归零，这些精确外部保留项不伪装为Evidence/Coverage通过。

最终V3格式校验及Report/唯一packet/本独立审阅文件限定diffcheck通过；机器不替代上述语义验收。未核完整1746题摘、silent Replacement全正文/版本史或其他日无关资料，19分层样本不能称全量验证。本轮未改作者Report、共享索引/LearningState，未stage/commit/push，既有dirty/staged保留。作者可同步最终状态为完成；同步后只需机械一致性复跑，不重复有效语义审阅。
