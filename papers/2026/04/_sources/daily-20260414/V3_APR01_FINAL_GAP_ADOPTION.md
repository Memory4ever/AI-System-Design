# Apr14 最后四项有限采用复核

独立复核者 apr01；实际重读当前 AGENTS、研究与 Report 合同、统一入口、来源范围和 ROADMAP。仅核四个拟采用命题的必要官方 v1 方法、评价反证及实际 owner；不核全日来源/日期、不复现实验、不写 Books。本记录的通过是 source→actual-owner 窄采用通过，仍须实际落笔和作者外写后检查。

## 2604.10495 — Uncertainty Sources

[官方 v1](https://arxiv.org/html/2604.10495v1) 实际读 §3.1–3.2、§4.1–4.2、§5 及限制；对读 Ch66 Calibration Slice 与 Atomic Claim estimand 交接。**2+2+2=6，gap 深入采用通过**：现文已分 sensor 身份与校准分布，却缺知识不足、合法多解、输入不完整对应不同 action 的受控对照。宜在 Calibration Slice 末尾补该条件分支，再交整体 claim 事件。

539 个配对问题/类、GPT-5 改写和判分及人工核验仅支持作者问答切片；PRR 是与 oracle/random 比较的拒答排序指标，不是 calibrated factual probability。不能从此推出开放任务已能自动识别原因，或合法多解必然只有一种处理策略。查证/拒答、接受合法答案、澄清的工程选择应按任务要求，而非强制共享 entropy 阈值。

## 2604.10496 — CodeQuant

[官方 v1](https://arxiv.org/html/2604.10496v1) 实际读 §3.1–3.4、§4.1、§4.3–4.4 与硬件设置；对读 Ch49“量化为什么不自动带来加速”及后续质量恢复。**2+2+3=7，深入采用通过**：实际现文给成本清单与格式验收，尚未解释非均匀 centroid/assignment 表示怎样要求 product LUT、decode/布局与执行路径共同变更。可在该成本结论后窄补，不重复写通用 PTQ。

activation code×weight centroid 的 LUT 取代部分乘法；rotation/permutation 折入相邻算子，MoE aggregate 与 router-KL 校准不保证 route 完全不变。GPU 为修改 tensor-core/shared-memory 的 Accel-Sim，真实 A100 仅部分基线，不能称新 kernel 为实机收益。CPU 路线、预计算/银行冲突与校准成本分开；推理质量仍低于若干 BF16 切片，不采用无损或生产 SLO 保证。

## 2604.10539 — IceCache

[官方 v1](https://arxiv.org/html/2604.10539v1) 实际读 §4.1–4.5、§5.1、§5.3.2 与质量表；对读 Ch45 physical access-plan→Grid/Chunk/Page→causal repair。**2+2+3=7，深入采用通过**：现文缺按 key locality 而非逻辑 token 顺序组织物理 page、GQA page union 与 host gather/bulk PCIe/device scatter 的组合责任。适合在层级访问计划后作为物理布局分支，不能改变 causal identity。

ANN/索引动态维护、staging buffers 与跨层复用误差须保留；36k Llama 的 TT2T 不是 TTFT，query 开销仍大于部分 decode 开销，因此不采用“索引已无成本”。仅作者 PCIe A100/H100、64 CPU threads 与有限模型/任务；稀疏预算仍存在质量损失。dense read/普通逻辑页在短或密集访问时继续成立，不把局部近似声明成 exact attention。

## 2604.10547 — Agent2 RL-Bench

[官方 v1](https://arxiv.org/html/2604.10547v1) 实际读 §2.1–2.5、§3.1、§3.3–3.4；对读 Ch66“Post-training 与 Agent Optimizer 都会改变 Evaluation State”及过程/终局分账。**2+2+3=7，深入采用通过**：现文已有 regression/harness 独立 owner，但未承载外层 workspace/code/train/artifact/submit 与内层 static-rule、static-judge、stateful-rollout 的验收区别，以及 route 名称与实际执行路线的差异。

best-within-12h 必须连同提交次数/轨迹、driver/scaffold、资源与反馈可见范围解释；test 不挂载、scalar feedback 不等 adaptive-selection 无泄漏。single-run/partial factorial 不证明 scaffold 唯一因果。Free 的 SFT 成绩不是在线 RL 已完成，DeepSearch 变化在作者 seed 噪声内仍未决。可补窄 evaluation contract，不照录 headline 能力排序。

四项窄采用均通过，未核全日 Gate；日期仍由 Apr14 作者归并。新增文件空白/Markdown 检查后提交 root，实际写后由非作者另验。

## 实际写后独立检查

复核者 apr01（不是这四处 Books 作者）。本轮实际顺读新增正文、上下交接和章末具名 Review notes；复用上文已核且未变的必要官方 v1 证据，不重读全部附件，不验收 Apr14 日级来源或日期。

- **10495 — PASS**：Ch66 L1591–1593 的两段位于 Calibration Slice 输入身份之后、Atomic Claim 之前。知识不足、合法多解、输入含糊对应不同任务动作，并明确 entropy 不自动决定原因；539 配对问题/类、构造者与 judge、PRR 排序而非概率、额外误判/标注成本与保守回退均在正文。没有把受控切片写成开放任务原因识别保证。
- **10547 — PASS**：Ch66 L2869–2871 两段接在 Post-training/Agent Optimizer 状态合同之后、表面成功分账之前。workspace/code/train/artifact 的外层验收与内层规则/judge/rollout 反馈分开，SFT fallback 不冒称在线 RL；best-within-12h 的模型、driver/scaffold、资源、反馈与提交轨迹均绑定，single-run/部分交叉混杂及 seed 噪声保留，没有能力普律或唯一因果宣称。
- **10539 — PASS**：Ch45 L188–190 两段由 Grid/Chunk/Page 过渡到 key-locality 物理布局，再交 causal repair。GQA union、host gather/staging、bulk PCIe/device scatter 改物理访问而不改逻辑 token/因果身份；动态索引、缓冲、近似误差与 dense fallback 具体，36k TT2T 不写成 TTFT，query 成本没有被消去。
- **10496 — PASS**：Ch49 L739–741 两段承接量化端到端成本清单、再交低位 Probe。centroid/assignment、activation-product LUT、合法 rotation/permutation 与 execution plan 的身份相连，router-KL 不被写成 route 不变；校准/decode/布局/银行冲突成本、CPU 与 Accel-Sim GPU 证据区别、BF16 质量反例与常规 GEMM/高精度回退完整，没有 A100 新 kernel 实机保证。

四个 Review notes 与实际采用命题/边界一致，但检查时仍写“真实正文写后待非作者核”；root 可据本节仅同步这四行的通过状态。实验未复现、生产能力未验证、本文件不是日级 Gate。行号为本次实际读取位置，后续编辑可能移动。

## 六项早期普通工作的有限独立采用/处置核

复核者 apr01。本轮定点重新打开以下原始版本的必要方法、对照/反证及实际 owner 正文，不审 Apr14 日期归并或全部 raw，不写 Books。六项均按所述窄命题通过；三个 gap 仍需真实写入与写后核。

### 09557 SPEED-Bench — 6 分 gap 深入，采用通过

实际读 [官方 v1](https://arxiv.org/html/2604.09557v1) §6–8.4及必要配置：随机输入可产生易预测应答或 topic latching，影响接受长度；高 batch 的 draft-length 最优点可反向。§8.2 是 draft 词表剪枝的长尾覆盖/接受质量代价。Ch48“一个可审计的实验至少要固定”及 accepted-progress 成本段已有广义 workload/并发，未具体表达语义分布、固定长度合成流量和剪枝词表的这条失效链；窄补位置合理。

措辞限定：被削弱的是 proposal 的长尾覆盖与接受质量，**不能推 exact target verification 下最终输出必然更差**。sampling contract/目标输出质量仍须同条件验收，但原文 AL 下降不是 target accuracy 下降证据。B200/多卡例外、Table1温度、client GIL和padding范围保留，不采用通用23%或生产SLO。

### 09678 NetAgentBench — 6 分标准，已有覆盖通过

实际读 [官方 v1](https://arxiv.org/html/2604.09678v1) IV-C/V/VI-B–C/VII-C；理论correctness依赖Perfect Observability，实际CLI parsing与收敛timeout不提供该保证。5-task×4-model×25应为500而非300/75每模型，原统计分母不能统一采用；早退减少风险暴露和token量，不等更稳定。当前Ch66 Outcome Witness、risk分解的environment opportunity、Long-session Stamina与删失段确实承载该采用命题，不是主题匹配。保留受限网络实例及分母冲突，不额外改书。

### 09687 Grid2Matrix — 5 分 gap 深入，采用通过

实际读 [官方 v1](https://arxiv.org/html/2604.09687v1) §2.3/3.1–3.2/4.2/5.1–5.2：冻结VE浅层probe在同1024patch下仍可读细格，而输出失败；密度与patch边界合成比例影响aggregate；规模与probe/output方向可不同。当前Ch23 encoder+projector段只明确接口瓶颈，没有完整分开encoder可读、融合可访问和输出可表达。拟在该段之后补诊断分支成立；probe增加监督/训练且不证明原模型已能调用。对齐、压缩、distillation解释均不是唯一因果，不能用这一例否定通用语义接口。

### 09712 LAST — 5 分标准，仅报告通过

实际读 [官方 v1](https://arxiv.org/html/2604.09712v1) §4.1/4.3、Tables4–5。No-tool SFT移除训练输出，Text/Image-only在完整模型推理时遮一路，不是同一干预；SPBench-SI的Text-only66.90高于Full66.76，不能说全slice联合hint最好。Ch78 typed-output及Ch23表示兼容只承载接口责任，不声称整套LAST算法已有；受限工具返回/consumer证据可以仅报告，无须复制训练recipe或通用收益。未披露执行/SLO条件照留，未复现。

### 09870 Relational Preference — 6 分纠错深入，窄争议隔离通过

实际读 [v1方法/结果](https://arxiv.org/html/2604.09870v1)、[当前v2 Erratum](https://arxiv.org/html/2604.09870v2) E1–E3/修正表，并打开官方版本页。作者明确固定order prior与跨split source-item泄漏是两个不同错误；原95.2/84.5/21.75不能再支持v1中心采用。v2修正仍留较小paired优势，不等整篇withdrawn。April保留其原中心主张不采用/暂缓，不将July纠错当April新事件；按具体split/order/antisymmetry及固定artifact重开，不要求无关后续稿或完整版本史。

### 10044 LoopGuard — 6 分 gap 深入，采用通过

实际读 [官方 v1](https://arxiv.org/html/2604.10044v1) §4.2–4.3/5.2–5.4/6.1/6.3–6.5。三次greedy相同输出不是独立seed；loop label含长度≥2480与低多样性/高冗余，因此更短输出不能单独证明语义恢复。多信号持续触发→anchor/sparse/tail-cleaned集合→cooldown及逐级aggressiveness是有损KV改写，不是exact reset。当前Ch45静态/attention-mass/learned-importance与workload-aware段未给生成退化事件触发的责任分支；可按所拟位置窄补。保正常合法重复、遗漏证据、monitor/index-gather成本与FullKV/中止fallback；诱发LoopBench和单2Wiki QA不证明自然loop率或广泛保真。

以上三个必要gap为09557→Ch48、09687→Ch23、10044→Ch45；09678已有覆盖、09712仅报告、09870中心采用隔离。仅源→真实owner及处置通过，未计新增实际整合，非日级Gate。

## 六项批次三处实际写后独立检查

apr01 实际顺读三处新增正文及相邻交接、具名 Review notes，复用上述已核且未改变的 exact-v1 必要证据；本轮不重读全篇或审阅日级日期。

- **09557 Ch48 — PASS**：L180–182 接在 matched sampling/workload 清单之后，先区分相同 shape 下真实语义与合成流量的 proposal 可预测性，再分开 draft 词表长尾覆盖与 exact target 输出合同。没有从接受长度推最终准确率变差，保留 draft/verify/client/padding 代价、高 batch 反向选择和 target-only 回退；与后续 lossy verification 分支交接没有把 exact 与 lossy 混同。
- **09687 Ch23 — PASS**：L63–65 接在 modality encoder/projector 的合理性与瓶颈之后，分开可恢复、可访问、可表达三个问题，明确浅 probe 新监督/训练成本及其不能证明原模型能调用。合成网格、patch 边界和不同 readout 容量未被压成 projector/压缩唯一因果；成熟 encoder+projector 与专用 readout 保持条件共存，再自然交持续任务接口漂移。
- **10044 Ch45 — PASS**：L371–373 在 workload-aware eviction 入口增加退化事件触发分支，组合信号、持续越界、cooldown 与一致 keep-index 改的是有损可读集合。实际正文没有把干预叫 exact reset/正确 commit，保留合法重复误判、遗漏证据、monitor/gather 成本、三次 greedy 非独立 seed 和长度标签的局限；与 residency/latent-memory 分支的压力区别明确。

三个 Review notes 的采用命题与正文一致，检查时状态仍写“待写后”；root 可仅同步这三项为实际写后非作者通过。未复现实验，本记录不替代 Apr14 日级 Gate。

## 82 家族日期范围的有限独立判断（2026-09-27）

复核者 apr01。实际读取三份 `datacite-created/2026-04-14-page-01.json`～`03.json` 的原始日期字段、作者所给 82 身份，以及现有 04/07～08 公共日期 reconciliation；本次重新打开[官方公告规则](https://info.arxiv.org/help/availability.html)、[09557 v1](https://arxiv.org/abs/2604.09557v1)与[10556 v1](https://arxiv.org/abs/2604.10556v1)。不以此验收全日准入、全部正文或外站首次公开。

三页去重实际为 **2262 条，09548～11809**；其中连续 **09548～10881 是 1334 条子范围**，不是三页的全部记录。原有 replay 的 1166 也不是这个子范围的全量数，不混为同一个统计口径。按 v1 原始 `dates Updated` 在 `2026-04-14T00:00:00Z`～`01:00:00Z` 的筛选仅用于检验时间链一致性：得到 997 条，最小09548、最大10566；它不是候选集合，也不证明997均有贡献。

作者给出的82家族全部在三页中找到，均 `Available/v1=2026-04`，v1 Updated 的最早/最晚分别为09557的 `00:00:18Z` 和10556的 `00:59:09Z`。边界09548为 `00:00:05Z`，10566为 `00:59:51Z`，10567为 `01:00:01Z`。DOI created 分别较晚，例如09557 `03:12:16Z`、10556 `03:36:00Z`，不拿这些注册时刻作截点前公开上界。09548/10556的当前OAI datestamp是04/14；09557当前是05/29，明确是后续变更元数据而非首发证明。官方abs中的09557 Submitted=Feb10、10556 Submitted=Apr12，只是提交历史，不回拨论文公开日。

**有限结论：这82项可以使用合同允许、并与先前公共日期审计一致的组合推断范围 `[2026-04-14T08:00:00+08:00,2026-04-14T09:00:00+08:00)`，必须标明“公告批次与原始版本元数据的一致性推断”，而非逐篇已取得精确公开时刻。** 依据是永久ID在公告流程赋号、相邻批次与当日版本处理簇、April公告月份及 Monday20:00 EDT常规槽相容；不是把 Updated、DOI created 或 Submitted 任一字段重命名 first-public。没有具体异常的早段不因尾部跨截点或一般可能延期而全体永久隔离；已发现更早原始正文、版本污染或跨截点例外仍按家族单独处理。

本轮[cs.DC 月列表](https://arxiv.org/list/cs.DC/2026-04?skip=0&show=2000)恢复，实际388条，但只支持月级身份，不能补成日公告日志；两个尝试的历史日列表仍 cache miss。没有取得逐篇公告邮件/公开动作成功日志，所以不得写成确定的08点同刻发布或全互联网首次正文保证。晚段10567以后不能用82项的早段证据硬套本窗；已有28潜在晚段的精确日期隔离应保留。若正式报告要主张精确时刻或解除具体晚段/早公开例外，最小恢复材料是对应家族正式公告记录或可验证的截点前正文公开记录，不需要重读全部1334正文。

此结论仅通过上述**有据且显式限定的日期推断**；日级来源、所有拟入选的采用证据、Books终态与否定侧语义检查仍须独立完成，不能由本节预支 Gate。

## 最终六部分报告的独立日级验收（2026-09-27T20:55:37+08:00）

复核者 apr01；正式报告作者 root。**结论：PASS，允许作者完成最终状态同步。** 本轮实际顺读新 V3 README 六部分、82 行唯一家族表及对应82项正文裁决；复用上文82项有限日期判断、各具名必要原文审阅与25项实际正文/邻接写后核验，不重新抓取机构历年目录、不重审未变的全部论文附件。本次没有改正式报告或 Books，也没有把校验当语义证明。

- **窗口、来源和筛选边界：通过。** 窗口为04/13 09:00至04/14 09:00；14个Daily入口均列实际目录/分页停止范围、已处理事件与具体历史限制，不加载Weekly来源。Research历史目录、组织artifact和arXiv日公告的缺口仍隔离，不凭RSS、空响应、month listing或少数release宣称组织零事件/覆盖无漏。2262原始身份与1334有界子范围、325标题线索和155完整题摘分别表述；宽列表未被转成全量证据队列。复用有效正反准入校准（09557/09595/09666及09574/09577/09588/09617等）与具体关闭核（09604、09606、09718、09791、09917、10493），不是全155或1334的无遗漏证明。
- **日期与例外：通过。** 82表项完全采用上文限定的08:00～09:00组合推断，不把Submitted、DOI created或Updated孤证叫首次公开；28晚段仍在§5逐身份隔离，且不把它们全部当贡献候选。09940只因较早正式公开线索而保留日期恢复问题，不从ICLR accepted标签捏造first-public；09945保留原库存与当前正文身份冲突，不用污染版本支持April结论。10091的出版方2025-07-20证据已在有效单篇记录核实，正式稿正确去重，不迁到本窗或新写April Books。09870当前勘误只限制原版采用，不把July纠错或整篇withdrawal虚构为本日事件。
- **逐项状态与真实Books：通过。** 实际表格计数82唯一身份=25整合+7已有覆盖+42仅报告+8暂缓，审阅32深入完成+42标准完成+8中心争议，与§1及§4相符。25个整合分别映射当前ROADMAP owner与有效真实写后记录；既有单篇PASS未被泛化为所有实验复现/生产能力。8中心争议的正文限制与§5精确重开材料一致，争议不进入正面采用；仅报告项保留具体方法或反证而非假称Books全部承载。
- **七项已有覆盖：通过。** 本轮再实际读当前Ch66的行为预测/配对辅助干预、Tool→Information Use→Outcome、Document Agent导航及opportunity、Outcome Witness/提前终止删失，Ch45的CPG→chunk预算→protected span→物理KV段，Ch82 Collective Risk，以及Ch36 finite-SDC/phase guard/optimizer commit段；分别与有效09678、09890、10015、10235、10261、10290、10390源→owner审阅对账。Existing指所采用命题已承载，不指完整算法、benchmark或全部领域细节已写入。
- **Moonshot CLI事件的负面处置：通过。** 本轮重开官方1.32.0 release，并经官方GitHub PR API实际读取#1843核心说明：100K统一字符预算、超大媒体丢弃、未知类型placeholder及截断提示，为避免context overflow/wire stalls和turn crash的具体实现修复；不能据此声称多模态证据语义保持或全部工具输出安全。前分母关闭的是该公开实例未建立新的长期设计判断，不是否认真实修复或保护作用；Ch75现有observation载入前容量admission和partial/truncated状态责任是具体对照。release事件落窗，PR合入Apr12只是原实现先行，未把两者计两个家族；模型研究/其余组织入口的缺口仍保留。

机器结构校验与本报告/独立文件的scoped空白检查本轮通过；82候选、六部分及Stable Node链接一致。未发现需要新增研究或Books正文的普通未决。作者仍须把正式§1/§5/§6的“最终验收待办”与开头状态同步为本次PASS，再运行最终校验。**本窗可以安全闭环，不意味着上述来源保留项获得Coverage通过、所有争议被解决或互联网绝无遗漏；材料后来到达只定点重开相应家族/入口。**
