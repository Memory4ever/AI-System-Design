# 2026-03-18 来源遗漏补充：独立复核

复核者：review_mar17_18（非报告作者 supp_mar18；非 Books 写入者）。仅 own 本文件，不 stage/commit/push。

## 1. 单日上下文

切日已重读当前 AGENTS、研究/报告合同、CODEX 入口、ROADMAP、来源使用说明/每日/arXiv 主题与最新相关 LEARNING_STATE；本日补充只含 2026-03-17 BJT 完整自然日。原确定候选 0、原窗口、日期/评分、连续 §4 保持。旧完成标签不代替本轮 DAY 验收。

## 2. 首批准入校准

实际完整独读 [官方 v1 题摘/历史/信号窄原件](./SUP_AB_FIRST_DIRECT_20261011.json) 首十及 14712/15523 两个代表 EX，不以 web 后半只有元信息的文件充当完整 AB：

| v1 身份 | 具体潜在增量与不自动采用的边界 |
| --- | --- |
| 14591 FlashHead | 词表 dense head 改为 balanced-cluster/multiprobe retrieval 与全词表采样/选择性量化；近似误差与实际端到端资源要分开核 |
| 14633 Scanners | 固定 attack 和 output 改 evaluator 仍改 ASR 的直接测量反证；independent verifier 不天然是真值，须深入必要反侧 |
| 15031 AttnRes | unit-weight residual 改 input-dependent depth softmax/block memory+communication；不是仅新模块组合 |
| 15202 LMetric | new-prefill×batch routing 与线性调参取消条件/失败条件；不混用较晚 v3 数字 |
| 15340 DOS | 以 attention 近似依赖并优先已解掩码信息改变更新顺序；attention 非因果独立性证明 |
| 15401 SWE-Skills | pinned repo/requirement 配对执行揭示弱收益、token成本与版本不兼容反收益；负面局部结果可有贡献 |
| 15530 DUET | hybrid SSM/matmul 失配使 prefill 与 decode 采用不同 package/dataflow/memory；模拟不等硅片测量 |
| 15589 LEXI | lossless exponent coding+multi-lane LUT 无损通信分支；布局/codec/端到端成本待正文核 |
| 15619 MoDA | sequence/depth KV 同 head 选择及非连续内存 kernel，post-norm 反侧；Seed 03/16 官网页可能先稿，定点核而非较晚 arXiv 覆盖 |
| 15727 ClawWorm | message→persistent config→reboot payload→peer传播完整信任越界；v1不能被AgentWorm v3重述代替，公开日期跨日保留 |

十项准入方向均有具体机制或设计反证，不以高保留率倒推问题，也不将摘要数字当 Evidence。14712 完整 AB 只提出自动数据准备与动态选择/混合研究方向，无本次具体机制或验证，贡献前关闭；15523 的特定形态匹配误差/数据评测未改变本项目主线设计选择，贡献前关闭，不是按语言标签或 benchmark 类型一律排。两 EX 覆盖系统展望与语言应用/局部匹配理由；其余 EX 未独立全读，不称全量语义验证。

## 3. 首批日期独核

实际逐项 fresh 只读 exact DOI endpoint 十次，和 [作者日期原字段](./SUP_DATACITE_FIRST10_20261011.json) 回对：全部 publisher=`arXiv`、client=`arxiv.content`、provider=`arxiv`、state=`findable`、isActive=`true`，题名/原 arXiv URL 与精确 v1 身份对应。当前 15727 家族题名为 AgentWorm，只作实体对应，不拿当前 AB 代替 ClawWorm v1。

官方 availability 的公开公告流程、ID/DOI不能提前分配与 schedule 已实际独读，方法经 root 定点裁决：v1 Submitted 只作最早常规公告自然日，官方 DOI registered 只作已有公开上界；同一 BJT 自然日才推断首 arXiv 公开日，不伪造时间，不排除具体作者先稿信号。14712/15523 已明确贡献关闭，不为不影响处置追日。

| 身份 | v1 Submitted 原值（UTC） | fresh registered 原值（UTC） | 自然日判断 |
| --- | --- | --- | --- |
| 14591 | 2026-03-15T20:26:42Z | 2026-03-17T04:19:03.000Z | 最早及上界均 BJT 03/17 |
| 14633 | 2026-03-15T22:08:16Z | 2026-03-17T04:19:58.000Z | 同上 |
| 15031 | 2026-03-16T09:32:21Z | 2026-03-17T04:29:13.000Z | 同上；repo创建不等先公開 |
| 15530 | 2026-03-16T16:56:01Z | 2026-03-17T04:41:00.000Z | 同上 |
| 15589 | 2026-03-16T17:48:30Z | 2026-03-17T04:42:23.000Z | 同上 |
| 15202 | 2026-03-16T12:43:32Z | 2026-03-17T04:33:13.000Z | 同上 |
| 15401 | 2026-03-16T15:16:31Z | 2026-03-17T04:37:53.000Z | 同上 |
| 15340 | 2026-03-16T14:28:39Z | 2026-03-17T04:36:27.000Z | 同上 |
| 15619 | 2026-03-16T17:59:55Z | 2026-03-17T04:43:06.000Z | 首 arXiv 同上，官网先稿单独待核 |
| 15727 | 2026-03-16T17:55:43Z | 2026-03-18T02:15:29.000Z | BJT 03/17～18 跨日，不能确定本日候选 |

MoDA 官网页 03/16 日级 published、同稿完整 AB/作者与当前 Download→arXiv PDF 已由作者/root 定点取证；当前链接不能倒证 03/16 正文已公开，且与首次 arXiv 03/17 构成具体跨窗信号。root 裁决同一家族在 17/18 隔离、不计确定候选；保留同一具名请求：03/16 原 PDF/当时正文公开记录或官方日期口径，不重复请求、不查全站历史。

## 4. 必要 Evidence 与 Books 局部复核

已实际独读 [作者保留原始核心 A](./SUP_METHOD_A_20261011.txt)、[C0](./SUP_METHOD_C0_20261011.txt)、[D](./SUP_METHOD_D_20261011.txt) 的必要原文，并补读 [FlashHead exact-v1 HTML](https://arxiv.org/html/2603.14591v1) §4.3–5/C/D/D.1；合并输出截断处已以必要段补全，不以文件存在当已读。

- 14591：限定 Source 局部 PASS，2+1+2=5、采样语义差额定点深入。§3 的等容量离线簇索引、centroid 无放回抽簇与候选内 softmax 支持近似分支；全词表非零机会不证明 dense 目标分布等价，Appendix D 的边缘期望恰需区分两者。五 clustering runs 只支持局部波动，100 条概率任务/10000 probe-set MC 与零概率 clip 不是 exact likelihood；4h A40 离线费用、head 与全模型 TPOT 差额、8B BF16 OOM、batch1 RTX3500Ada、未来 large-batch 分支均保留。未核实现/复现。实际比较 Ch20 L19–190 的 dense 目标、top-k/top-p renorm、processor/RNG，与 Ch19 末 KV handoff/Ch21 首 MLP handoff：唯一 MODEL-SAMPLING 与最小两段 PRE 方向通过，不接管 Ch12 projection 计算。逐字 PRE 尚只需将“小模型、batch1消费级GPU”改为“已披露模型、batch1 RTX3500Ada”，使人口/硬件比泛称更准确；尚无实际写入/POST。
- 14633：限定 Source 局部 PASS，3+2+2=7、评价设计反证深入。实际 §4/5/6/8/A.1–A.2 支持同 response/evaluator 替换的稳定性诊断；D 阈值不决定谁正确，GPT5.2 参考标签不是真值。200 第一作者单标/共享 rubric、4 static 优势类别、majority 低于最强单 judge 与17类局部升级后全替换反退均保留；名义 23K 与最多1800/scan、base $14.38/$14.86 矛盾不能硬拼统一分母/预算。未给全样本独立 accuracy、scanner安全或生产保证。PLATFORM-EVALUATION-SYSTEM 的实际正文差额与最终 Books 决定尚待核，不授 PRE/POST。

FlashHead 后续修订定点回读：作者已将第二段改为“受限词表头实验只在已披露模型、batch1 RTX3500Ada条件下显示任务均值与端到端延迟取舍”；其余逐字 PRE 不变。正式 Source/唯一 MODEL-SAMPLING/两段逐字 PRE 局部 PASS，替代上面的措辞待修停点；可按 root 窄锁写入，尚待非 writer 实际 POST，不授 DAY。

FlashHead **实际非 writer POST 局部 PASS**：写后实际回读 Ch20 L31–82 的完整局部（dense softmax/数值稳定→新两段 L50/52→固定 logits 例子→Greedy/temperature 交接）与本人末注 L620；回对必要原证，两段保持随机集合边缘化、全 support≠dense、greedy miss 与近似语义、MC clip/费用与回退限制，未将相似任务均值授概率等价。原 dense/截尾/RNG 主线不被覆盖，唯一 owner 与 Ch19/21 handoff 不冲突。末注 exact-v1/章节/分数/采用边界匹配；实际局部 diff whitespace 检查通过，不授实现复现或 DAY。作者只可据此更新该注 POST 状态，然后定点回读。

## 5. 停点与验收

压缩恢复后已重读本日适用合同/入口/ROADMAP/来源与最新相关 checkpoint。FlashHead 更新后的末注 L620 已实际定点回读，准确仅授局部 POST，已通知 root 可释放 Ch20 窄锁。

Scanners 最终 [逐字一段 PRE](./SUP_BOOKS_SCANNERS_PRE_20261011.md) 实际回读通过：独立标签/审核是系统验收推断，不声称第一作者样本已完成独立真值校准；全面替换 vs 局部升级、majority vs 最强单 judge 两个协议不混并，保留静态优势/unknown/成本。此前实际 Ch66 仪器分账与安全 ASR 局部、Ch65/67 handoff 仍适用；唯一 PLATFORM-EVALUATION-SYSTEM 的这一段及本家族末注正式 PRE 局部 PASS，实际写后 POST 待做。

后八 [exact-v1 完整题摘](./SUP_AB_SECOND_20261011.json) 已逐项独读：14893 的温度改变 sensitivity 而不只是 criterion；14903 的固定源位置槽改变 KV/position 兼容；15159 的正确私库文档仍不足与图演化/剪枝训练替代；15389 的受控稀疏度/深度/方差；15611 的对抗 Code/Test 奖励与防 collusion 必要反侧；14672 的 concealment classifier 跨主题/架构/规模反证；15417 的 base 安全依赖/self-consensus 放大与 reasoning tax，均有具体潜在增量而非主题映射，尚不是 Evidence。15164 科学 idea 评价范围尚须决定性核心校准，不经 Evaluation owner 绕暂缓范围。后八必要 v1 history/public DOI 实体字段尚待核，registered 单值不是日期证明。

[有限来源停止点](./SUP_SOURCE_STOP_20261011.md) 已实际读：四组窄 query 的类别/同义主题、Submitted buffer、start0/max150/ascending 和 41/43/18/46→130 unique 只作发现，当前 AB 与 exact-v1 采用分账正确；官方本窗相关标题 dated slice 尚缺，不凭空标零。14 入口均有当前范围/停止或历史差额，尚待最终六部分自包含及普通来源补检结束，不能授全 Coverage。WorkerBench 官方核心 §23–32 已独读并同意贡献关闭：用途/工资估算与 median 比较无新增主线系统机制，不是仅按经济标签排除。MoDA 追加窄实体原字段 id1426/PublishDate1773590400000/path/Download 与 ArticleType=1 查询已实际核对；query 参数不冒作实体字段，当前 PDF 仍不倒证 03/16 正文。

首十准入/两 EX、fresh entity/date 与两项必要限定 Source 局部复核已做；等待其余必要正文、最终 Books PRE、实际 POST 和全部六部分 source/query/官方相关标题补检/停止记录。当前结论：未通过（普通可执行独核未完）。仅上述两项受限 Evidence 局部通过；不授整日 Evidence、Books、DAY 或无遗漏，外部日期/来源保留须精确隔离。

## 6. 后续局部复核（不授 DAY）

Scanners 实际非 writer POST 局部 PASS：完整回读 Ch66 L4618–4650 的 ASR/attack-profile→新增一段→scope 测量交接，及 L4683–4697 本注和邻注。固定 attack/response 的配对诊断、独立校准作为系统验收推断、全面替换与局部升级/majority 与最强单 judge 两协议、静态优势和 unknown/成本均回对必要原证；没有将作者单标样本冒作独立真值。正文及本人注身份/来源范围匹配。作者声称更新注后实际 L4689 仍写 POST 待核，已要求仅修本人注；此不改变本次实际正文 POST PASS，更新状态仍须定点读回。

实际独读 [六项最终证据 notes](./SUP_EVIDENCE_SIX_20261011.md)，不是拿 notes 代替原证。15031 的既读 C1/D/J/L/M 必要 §2–5.3，与 Ch17 L426–458 深度 residual/history→block summaries、状态/通信/训练部署成本相对应；learned query 不依赖输入、weight 依赖历史内容，compute-equivalent≠wall throughput、低开销未绑定完整运行条件，限定 Source 与 MODEL-TRANSFORMER-LAYER 已有覆盖 PASS。15401 的既读 E/L 与 exact-v1 §3–5，以及 Ch84 L1110–1133/846–855，支持 pinned WITH/WITHOUT、净效用/版本漂移与回退；CPU task container≠推理硬件、模型生成测试≠独立需求 oracle、ceiling/零 observed≠等效、CE 符号缺陷不采用，限定 Source 与 AGENT-PLATFORM 已有覆盖 PASS。两项不重复写 benchmark 摘要。

15164 的 exact-v1 决定性 §1–4 已实际读：将时间切分搬到科学研究 idea 与未来 citation/venue 代理，未新增本项目训练、执行或通用测量机制；按具体范围/贡献关闭 PASS，不通过 Evaluation owner 绕 AI for Science 暂缓，不以成本或现文覆盖关闭。生成器 cutoff 晚于观察 cutoff，亦不采用宣传的无未来泄漏/真实 impact；无需为已关闭范围项再追日期。

[后七日期原字段](./SUP_SECOND_DATE_20261011.json) 已逐项实读 exact-v1 history、官方 public DOI endpoint/URL/title 与共有 arxiv.content/arxiv/findable/active 字段。14893、14903、15159、15389、15611、14672、15417 的 Submitted 最早常规公告与 registered 上界同为 BJT 03/17，按 root 已核官方 availability 的同日夹证仅作首 arXiv 自然日推断。较晚版本不代替本窗 exact-v1；15417 旧日期保留不是有效 done。日期局部 PASS 不授其必要 Evidence。

15530 实际读保留原文 F/G/J §3.2–3.3/4.1–4.4，并补 [官方 exact-v1 §4.4–4.5](https://arxiv.org/html/2603.15530v1)：state-stationary SSM 递推与可切 GEMM systolic、decode vector reduction/local state/HBM 的阶段硬件差额成立。SV/TSMC28 synthesis、CACTI/Ramulator 与 RTL 校验过的 cycle/events 模型不等成品芯片，B200 也在同一 in-house 仿真。4.4 假设吞吐匹配且两池满载、不显式模拟多请求 scheduler；资源/容量不等，batch1–128 与超64存不下反侧保留。4.5 缩到7nm与40%面积余量也是模型假设，不采用普遍性能、功耗或生产 SLO。2+2+2=6、具体硬件差额深入及受限 Source PASS。实际 Ch55 L1–125 的阶段差异/goodput/handoff，与 Ch54 memory/Ch56 scheduling 交接不承载专用计算数据流；唯一 INFER-PD-DISAGGREGATION、逐字一段 PRE PASS。Notes array 数量须写192×16/96×8，不能漏每 chiplet 单位；正文 PRE 无此数字，实际写后 POST 待做。

15589 实际读 I/J/N §3–5.4（截断的必要解码/setup 段已补全）：保留 BF16 sign/mantissa，按 layer 在线 histogram/Huffman book 与 flit/header、最多32-entry及24-bit escape+8-bit raw，支持恢复数值的 wire codec 机制，不是改算术精度。78-cycle book pipeline、10 lanes/8 cache 的55ns histogram设计点与4-stage平均11.6ns不混成免费单周期；未见异常不授总缩小，短 payload/header/entropy 漂移反侧保留。RTX3090只 profiling，6×6 Simba/HeteroGarnet trace模拟与GF22 synthesis/scaled16面积不授 GPU serving/成品运行验证。2+2+2=6、具体链路机制深入及受限 Source PASS。实际 Ch54 L220–255 的减少Bytes和L703–709权重ANS/tile，与Ch55 L102–119 PD exponent-transfer比较：本次在线 activation/SSM state per-layer book/prefix codec差额可承载于唯一 INFER-GPU-MEMORY；Ch53/55交接与逐字两段 PRE PASS，不复制PD协议。实际写后 POST 待做。

15202/15340 委派 root 实际必要原证、owner/邻接、逐字 PRE 与后续 POST，不无差别重复附件。root 已核发现15202第二 alarm为持续 >2×|M| requests、非两次BS翻倍；15340 A.1有单L40 48GB/batch1/temp0/seed42，Table9有TPS/Time，不能写硬件ND或未测walltime。作者须窄修实际证据与报告；root最终回执到达后汇总，不提前授实际写入完成。

后续定点读回：Scanners本人注现L4691按唯一family精确回读正确，只标实际局部POST通过、不授DAY，已通知root释放。15530 notes的array×chiplet单位已实际修正读回，不改变已核PRE。

15530/15589 实际非 writer POST 局部 PASS：Ch55 L15–37完整两阶段→新一段L22→共驻干扰/下一节交接，及L559–570本人末注；Ch54 L224–252完整减少Bytes→新两段L233/235→retention及选择代价交接，及L774–788本人末注。写入与已核逐字PRE一致，实际回对必要原证与本人注：保留simulation/synthesis及非生产SLO、资源不等与未模拟scheduler；保留wire数值身份而非算术降精、escape/短payload/entropy/完整成本与raw回退。未覆盖同构GPU/原共驻/未压缩旧路径，与PD transfer owner不重复。作者只可更新各自本人注POST身份，再定点读回；不授DAY、代码或成品验证。

有限目录恢复的实际关键字段独核：Qwen40条title/path/published date已全量读字段，当前可见03/17无项，不能推删除项无遗漏；Zai15当前dated卡最近03/15→04/01不冒本窗0全覆盖；GoogleMarch page2确见03/06 SpeciesNet与03/04 Bayesian reasoning两个题名，当前March目录两页边界成立，不误将其当本窗03/17材料。该字段补核与其他历史dated-slice保留分开，不将目录总数当全正文已读。

## 7. 后七必要原证与实际 owner 复核

换回本日后已完整重读当前 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX入口、SOURCES使用/每日/arXiv、ROADMAP与最新相关checkpoint；合并输出截断部分已另行完整补读。有效Books公共上下文复用，未载其他日研究材料。首批DUET/LEXI更新后的唯一本人注已实际读回正确，仅标局部POST；15202/15340由root实际必要Source/owner/PRE及非writerPOST有效复用，范围为Ch56 475–501/1576–1588、Ch24 492–510/1931–1942，不把代读扩大为本日验收。

实际读后七notes并回对必要原始正文 O/P/R/T/V/W/X/Y/Z（只选择相应必要段，未核全部附件或复现）。

- 14893：exact-v1 §2–5.5限定Source PASS，3+2+2=7。温度改变答案人口、teacher-forced fluency与truth分离、UVSD拟合/别名噪声及非显著反侧不授潜在能力提高。实际Ch66 1180–1194/2507–2524/2612–2626已承载teacher fluency、ranking/calibration与decoder人口身份，PLATFORM-EVALUATION-SYSTEM已有覆盖PASS，不另添通用Gaussian recipe。
- 15611：exact-v1 §3–4/Table1–3/A.3–A.4及必要function/GT反侧限定Source PASS，2+2+2=6。可信solution修正assertion后才核候选，dual reward/TopVar不证明collusion消失；频率book、10s sandbox及health/retry、8H20与每policy资源不授matched总算力。实际Ch33 755–771完整同机制正文已有覆盖，TRAIN-GRPO NoChange PASS，不凭末注代替正文。
- 14672：exact-v1 §2–6/9/A/B/E/F限定Source PASS，3+2+2=7。构造concealer、跨model+topic失败/单类collapse只限定检测适用域；不授自然意图真值或规模因果。实际Ch66 205–223/2281–2294/4637–4660已有人工organism、known/unknown与domain校准边界，PLATFORM-EVALUATION-SYSTEM NoChange PASS。inference多数8A40与concealer训练2H100已区分。
- 15417：exact-v1 §2–4.5/AppA/Table5限定Source与一段逐字PRE PASS，3+2+2=7。majority数值parser不检查完整harmful completion，数学-only与harmful-injection表不混；初始安全/有限mixed exposure、judge与硬件ND保留。实际Ch33 724–780 generic correlation/动力学/dual verifier尚缺format admission与完整response安全门差额，唯一TRAIN-GRPO最小一段是明确工程推断，不冒作paper已提供安全算法；实际写入/POST待核。
- 15389：exact-v1 §2–4/B.6–B.7/C必要原证独核完成，2+2+2=6。仅局部实验反证和成熟边界限定Source PASS；实际Ch17 245–260/369–376/395–401已有初始化vs训练、容量质量与具体干预，NoChange PASS。中心统一理论另行隔离：B.6的group内独立均值应随ng缩小而增方差，额外1/G与真实共享KV不由声明证明涵盖；§2 bounded norm不直接推出convergence/identity。一个具名请求修Lemma1到identity条件、B.6真实GQA/聚合及C.4实现映射；不授统一稀疏recipe，不以NoChange绕中心争议。

上述限定结论不授DAY。官方有界相关标题新批与实际停止点、新增候选准入/Evidence/Books仍须本日继续核实。

15417 实际非 writer POST 局部 PASS：实际完整顺读 Ch33 729–785 的安全动力学/dual verifier→新增760→后续协议交接及本人3178注，回对必要原证与已核逐字PRE。格式准入不检查完整harmful completion、两实验协议、初始安全与预算责任没有混并，回退/独立回归明确为工程推断。作者随后更新的唯一本人3178注已实际定点读回，仅授局部POST；root已释放锁，不授DAY。

## 8. 官方有界标题补检的新批局部复核

只处理作者/root已限定的20标题批；不把月目录或Submitted发现库存扩成全文关闭队列。三项 exact-v1 完整AB/history及public DOI身份字段已实核，同日夹证仅推断首arXiv公开BJT03/17。

- 15195：必要§2–3/4.2–4.4/4.6–4.8/5.1/5.6限定Source PASS。dense forward与稀疏historical influence transport分开；tanh实验固定随机mask与ViT随机head不混，dense masked einsum不授实际加速，Lorenz UORO反侧、延迟任务失败、Fisher选择反退、单subject BCI不授普遍/临床优势。实际Ch28 337–351的RTRL主线尚缺此分离，唯一TRAIN-PRETRAINING两小段方向通过，逐字PRE/POST待核。
- 15590：必要§3–4/Limitations/D.1–D.2限定Source PASS。同head窗口/sink与mLSTM两条记忆动态gate、分阶段冻结到联合训练有迁移差额；top256 teacher条件、域专家同base参数平均不等runtime ensemble，未证独立held-out sweep、STEM回退及NIAH限制保留。实际Ch22 909–940有层级替换但未有同head并行记忆分支，唯一MODEL-LONG-CONTEXT两小段方向通过；Ch28 1438–1443已有泛merge，不复制。硬件/预算、印刷预算矛盾与单H100 microbench不授生产收益；逐字PRE/POST待核。
- 14923：必要§2–8独核，中心争议隔离PASS、Books暂缓。router以整个sequence mean生成各head gate，attention causal mask本身不证明该路径只见prefix；不是已证泄漏，而是online/prefix-only生成与PPL的必要实现桥缺失。一个具名请求实际visible-prefix协议与同口径prefix-only结果；保留具体机制潜力与原评分，不采用当前headline收益、不用局部KO绕该桥。
- 15042：必要exact-v1§4.1–4.5/5/6.1–6.3独核，中心争议隔离PASS、Books暂缓。RCK/stream未披露instruction-block暂停状态协议，lazy closure迁移未披露一致性与缺页恢复桥，global ECC/MMU后状态来源/fencing及故障验证未见。launch不变不自动排除kernel内部非确定性；局部SLO反侧与开销不授strict determinism。一个具名机制/语义验收请求即可。当前官方abs题名Vitamin-E与public DOI对应，v1同家族history明确，不用较晚正文修补本窗v1；首arXiv03/17为同日夹证推断。

此批只授上述必要段和实际owner方向，尚有普通可执行PRE/POST与其他具名Source，不授DAY或无遗漏。

20标题批日期独核已逐项实际读SUP_DATE_TITLE_COMPLEMENT的DOI/URL/title/publisher/registered/created/client/provider/findable/active与SUP_AB_TITLE_COMPLEMENT全部exact-v1 history；均Mon03/16 18Z前Submitted、registered BJT03/17。除15569/14833具体先稿信号继续隔离外，18项首arXiv自然日同日推断PASS，不授作者更早公开不存在或必要Source。15042当前官方abs已直接核改题名同家族v1历史，未追版本全文diff。SUP_SOURCE_STOP最新Googlepage2两题窗外/有限20停止/9整合6覆盖与15389中心隔离已实际读回；普通队列未完，不授DAY。

后批逐字PRE追加复核：15195两段已实际回读新版notes/PRE与Ch28 335–355完整邻接，dense forward—historical transport分责差额正式PASS；n512限于fullRTRL数值发散/过参数化，不归为sparse特有失败。15590两段已实际回读PRE与Ch22 905–940完整邻接，同head双记忆/staged迁移差额正式PASS，泛merge只交接Ch28，不复制。15059复用root必要Source，另实际核Th4.1/Eq24/A2与Ch28 550–618，窄修PRE已补loss下界、β=0、p∈(1,2]，jointbatch一段正式PASS；严格更快/缺秩桥仍隔离。15377实际Ch20 323–360正文已有coverage/selection、相关错误及selector失配，有限负面证据具体NoChange PASS，Gaussian/GEV不授有限safe width。均尚不代替实际写后POST或DAY；锁由root分次协调。

新增四项必要Source/Books独核（未授其他库存）：14825实际exact-v1 §3.2/4.1–4.3/5.1–5.2/6.2及C.3必要反侧，有限blank-anchor/SVD投影限定Source PASS；Lemma2不能仅由加性Eq1推出语义⊥W，实际Ch23 116–128已有条件正交、bank人口/rank/消费者/旁侧与成本，NoChange PASS。C.3/Table9为攻击后Perspective/Detoxify平均toxicity，表头ASR不能使其等同ASR，约56–78残余只小幅改善，不授全面安全。14989实际§3/4.1–4.4/5.1–5.2/A.2–A.3限定Source PASS；600样本/两backbone/4A100/batch1及不同method配置、throughput≠latency、attention相关非唯一因果，§5max/A.3ratio不采精确ViSkip配方；Ch48 297–319/969–978已有proposal-budget vs targetverify/视觉负载与全费，NoChange PASS。15599实际§3.1–3.7/4 Tables3–7/5必要范围限定Source PASS，raw-passages/NER/CE+ColBERT仅受限路径；预算/prompt混杂、Table5离线模拟、三路fusion及temporal反侧不外推memory无用。实际Ch76 512–630/126–131/1283–1293已有packing→固定工作集→sufficiency及ingestion/query分责，NoChange PASS。15183复用root实际核心并独读§3.3/4.2–4.4/5.1–5.3关键桥：传输cache不等模型不消费、换baseline成本与authority metadata未齐；AS1不crash/partition、AS3及quiescent映射不授恢复一致。中心隔离/Books暂缓PASS，单请求同baseline完整费用及authority故障协议/验证；不以成熟MESI为EX，不授正面Source、DAY或无遗漏。

共享Books实际POST回执（仅局部，不载跨日研究）：15195非writer实际顺读Ch28 337–361完整tPC-RTRL→新345/347→zero-order及1859–1873本人1865注回对原证/PRE，dense forward/历史transport、ViT另一mask、真实费用/旧一阶路径边界正确，POST PASS。15590实际顺读Ch22 907–947完整逐层hybrid→新930/932→完整映射bridge及1369–1382本人1375注，同head双state/gate、staged转换、merge仅交接28、微测不授生产SLO与旧分支保持，POST PASS。作者仅可更新唯一本人注身份/范围，再定点读回释放窄锁；不授DAY。

## 9. 用户暂停 checkpoint（2026-10-11）

用户明确暂停等待额度刷新；停止新Source/PRE/Books与DAY复核。暂停前15195本人1865注、15590本人1375注已实际按唯一family定点读回，更新后的非writer POST身份/完整范围与局部通过状态准确；两家实际POST及本人注最终回读均PASS，已告root，但暂停后不触发Muon或其他后续Books写入。

15059一段Source/PRE已通过、实际落实与POST未发生；15377具体已有覆盖及中心有限宽度隔离有效。14825/14989/15599具体必要Source与已有覆盖判断、15183中心隔离结论有效；14825作者新增Table9 notes尚未由本reader更新后回读，不借作者消息授新状态。本20标题批其他具名必要Source/owner/PRE仍普通待办，按SUP_SOURCE_STOP及作者实际材料恢复；日期隔离和争议保留项不支撑正面Source、Books或无遗漏。最终候选归并、六部分DAY仍未通过，不增加验收分子、不stage、commit、push。

## 11. 补充自然日最终 DAY 复核（2026-10-11，resume_review17_18）

结论：通过。本人不是日报作者；本结论仅验收03-18现存日报的03-17完整自然日补查，不继承原09→09旧通过，不验收03-17或其他日期。压缩恢复独立重读当前AGENTS、研究/Report合同、统一prompt、完整ROADMAP、来源使用/每日/arXiv主题、LS恢复路由与本日停点后，实际最终回读当前正式稿六部分、34家族归并及新14源表；先前已实际读过且身份、精确版本、命题未变的必要Source/PRE/actualPOST按本文件具名范围有效复用，未重复同核心附件。

34个唯一候选＝首15＋标题批18＋纠正无依据日期门的14833，逐项准入、日级日期、必要证据及Books处置已覆盖。17项actual整合、14项actual已有覆盖、3项中心争议Books暂缓；所有整合正文、完整局部邻接、本人/邻注非writer POST与一次真实同步后的最终本人注回读通过，普通研究/Books待办0。root具名实际承担的DOS/LMetric/ExPosST/PriCoder/Flash-Unified必要Source/PRE/POST仅复用其正式限定范围，不假称本reader重读其所有附件。WorldDrive完整958–985/1723–1731、HYDRA256–284/1682–1695、14833474–500/867–877的actualPOST和各末注最终回读均已在§10真实持久化；§10采用顶部逆序追加，文件尾仍PromPrune并非后续回执丢失，不另建保存位置或递归改注收据。

正式六部分的34家族逐篇证据/唯一owner/评分/有限配置、费用、反退与未披露项和§5采用边界相符。纠错、安全及设计反证项没有因小模型、局部实验、负面结果、Books已有覆盖或中心争议排除；14923/15042/15183中心桥不采用，SparsityDepth/Muon/beam只采用有效受限子命题，14825 Table9平均toxicity不冒ASR，TTRL numeric gate不冒完整安全，HYDRA均值语义链不混随机采样，WorldDrive保留部署latent forecast/critic。14833原先稿门无原件已仅定点撤销并补必要Source/实际owner/写后验收，未扩发现波。

日期保留15569另实际定点核[官方Mamba-3 Part1](https://goombalab.github.io/blog/2026/mamba3-part1/)原HTML首段d-front-matter：title为Mamba-3 Part1、published明确March 16, 2026，正文Paper指向2603.15569；此是具体dated同家族机制说明信号，与14833无论文先发依据不同。保留首公开/重大修订关系请求是安全终态，不以当前Blog证明原论文精确首次公开，也不扩读PartII或版本史。MoDA/ClawWorm同样不计这34候选，不将日期夹证当所有作者先稿不存在。

来源实际范围为14 Daily入口的本日有限切片、四窄主题Submitted buffer start0/max150 ascending到41/43/18/46（130跨主题唯一只作发现），官方相关月title LGskip1400/DC100/CL700/CV1800/show100有界20完整AB后停止；错CL1100/CV1200不计，不扫描Weekly/全分类。当前14源表已按补充自然日实际入口/停点更新，不用旧09→09窗口表冒新覆盖。GooglePubs/MetaPublication/Seed缺5/MiMoBlog/MiniMax历史slice/arXiv延迟公告及旧具名正文版本日期请求均精确隔离；不能用于正面证据、Books或全网无遗漏，外部保留本身不冒普通未读。原窗口、原0候选与连续§4有效正文保持。

其余明确排除按来源/主题/理由分层抽检：本reader已实际完整题摘校准14712系统框架/展望、15523语言领域匹配、15164科学idea/引用venue代理；实际OpenAI WorkerBench有限主文工资/使用估算，及Google March页2两项SpeciesNet03/06与Bayesian03/04窗外卡。Google医疗应用暂缓范围与Bayesian窗外理由分开；原09→09的具名负侧及7关闭仅按root既有实际限定抽核复用。未将130元数据、全部月页标题、机构全部研究或全部历史排除项宣称全量逐篇/全附件独读；有重要信号者已恢复为候选或必要保留请求，不由分层样本授全量真值。

本轮实际再次运行当前V3校验通过，限定README/本独核git diff --check无输出；先前实际只读检查确认34唯一行=17整合+14NC+3暂缓、56本地引用无missing、原连续§4 677字符逐字保持。这些仅接口/一致性支持，DAY依据是上述实际语义复核及有效分层证据，不由脚本PASS代替。当前Report状态/§5/§6仍待作者或root同步本通过结论，全年分子由root单独更新；本人未改Report/Books/LS/索引，未stage、commit、push。不授实现核验、实验复现、生产/物理安全、全Coverage或所有中心Evidence证明。

## 10. 授权恢复后的局部复核（resume_review17_18）

14833本人注一次真实同步后，本人实际最终定点读Ch17 871–878；resume_review17_18完整474–500/867–877非writer POST身份、范围和限定结果准确、邻family未覆盖，最后本人注回读局部通过，可由root释放Ch17该family窄锁。不递归改注，不授DAY。

14833非writer本人实际完整顺读Ch17 474–500 mHC carry几何→新484/486冻结mixer pair rescue→正交约束及867–877本人875/邻注，逐字回对SUP_ABLATE_RESCUE两PRE与有效Source，分布KL非正确、相似非互换/剪枝、实验路由条件非部署建议、费用/回退与既有几何分责正确，actualPOST局部通过。唯一本人注待一次同步真实resume_review17_18完整回读身份/范围后最后定点读回，不授DAY。

15228本人注一次同步后，本人实际最终定点读Ch23 1688–1695；resume_review17_18真实完整256–284/1682–1695非writer POST身份、范围和受限结果准确，邻family未覆盖，最终本人注回读局部通过，可由root释放该Ch23 family窄锁。不再递归改注，不授DAY。

15228/HYDRA非writer本人实际完整顺读Ch23 256–284连续feature/UniCom→新268/270串行bottleneck→离散表示及1682–1695本人1692/邻注，逐字回对已更新SUP_HYDRA两段PRE与有效必要Source，确定性均值语义链/随机潜变量分开、channel非token压缩与三consumer协议/反退/全费用和旧双表示回退准确，actualPOST局部通过。本人注只待同步真实resume_review17_18完整POST身份/范围后最后定点读回，不重读同Source，不授DAY/全Books。

14833/Ablate and Rescue本人实际当前abs/history、exact-v1 §3.1–3.4/§4.1–4.3/Table1/§5与本日原AB及DOI身份字段定点通过：v1 submitted03/16 05:24:44UTC、arxiv.content/findable registered03/17 04:24:36UTC，按同批官方常规最早公告/公开上界夹证为BJT03/17首次arXiv日级推断，非submitted当公开日、非registered当准确公开时刻；无实际具体先稿依据，撤销旧14833日期隔离，仅改此既有误判，不授所有作者先稿不存在。成对zero/rescue使用缓存原activation且冻结原mixer，KL恢复只测输出分布、非事实正确或自然路由可删流；781M单模型/Dolma/AdamW+Muon、65/21919知识检查通过、表1不对称恢复与CKA一般可逆不变性错误隔离均已核。2+1+2=5，有限干预接口与相似性误用边界深入，支持具体准入而非小模型关闭。actualCh17 402–509完整替换/交换→残差路由→mHC carry→正交约束已读，soleMODEL-TRANSFORMER-LAYER frozen-mixer pair rescue差额成立；SUP_ABLATE_RESCUE两段逐字PRE正式通过，不采CKA错误数学保证、不授剪枝/全任务能力保真或完整预算；未写未POST、不授DAY，候选最终数由作者归并不预支。

14948本人注同步后，本人实际最终定点读Ch25 1725–1733；真实resume_review17_18完整958–985/1723–1731非writer POST身份、范围和受限结果准确、邻family未覆盖，最后本人注回读局部通过，可由root释放该Ch25 family窄锁。不再递归改注验收，不授DAY。

切回18独立重读当前AGENTS、研究/Report合同、统一prompt、完整ROADMAP、来源使用/每日/arXiv主题、LS恢复路由及本日README与SUP_SOURCE_STOP当前/历史停点，只接本日具名事项。15228/HYDRA首段PRE更新后本人实际最终读回：带均值方差bottleneck建模潜变量，Sem-ViT取均值投影确定性特征、随机采样不直接送语义层，符合已核Eq2/4/5与clean-latent原证；其余有效Source/owner/第二段PRE不重读，现两段逐字PRE整体正式通过。未写未POST、不授DAY。

14948/WorldDrive非writer本人实际完整顺读Ch25 958–985训练期privileged/删除整个预测接口→新970/972候选teacher→部署forecast/critic→Pixels/closed-loop及1723–1731本人1729/邻注，逐字回对SUP_REMAINING_OWNER_PRE两段与有效独立必要Source，具体consumer差额与费用、反退、oracle ceiling/authority和回退正确，actualPOST局部通过。本人注仅待同步真实resume_review17_18完整回读身份/范围后最后定点读回，不授物理安全/全Books/DAY。

14833旧日期隔离需纠正：本独核先前“具体先稿信号”的表述未附实际原稿URL/公开日期，作者现确认无原件，不能由HF模型artifact早发推论文早发，也不继承09时刻门。root当前abs/html与本日AB/history/DOI定点回查未见该具体信号；本轮只恢复此已有具名family的同批日级夹证与必要Source/owner/PRE，不扩发现或无差别版本比较，最终日期/证据裁决另记，不预先冻结33数量。

15228/HYDRA本人实际exact-v1 PDF必要§2/Eq1–11、§3/Fig4–7/Tables1–4与B/D.1/D.2/Table6；root已读必要余证有效复用，串行Gen-ViT→GSB→Sem-ViT容量分责受限Source通过，2+2+2=6。Eq2有随机z，Eq4/5语义输入却是均值μ投影的Hbn，理解读取clean deterministic latent；已向root请求仅澄清首段逐字PRE，不把随机样本直接写成语义消费者输入。actualCh23 215–275/296–339/349–370完整native→连续/UniCom→离散及Q/K–V分工/容量tradeoff已读，串行bottleneck具体分支差额成立、唯一MULTIMODAL-REPRESENTATION。两段PRE其余边界局部通过：C64有限/C≥256生成失效、12+12局部操作点、理解共同训练前期较慢、三能力不同协议、tokenizer两阶段与全模型三阶段都计费，300M/7B/100M限制不外推；不授无压缩/可逆、无冲突或全部baseline总预算公平。首段澄清更新后待最终定点回读，未授逐字PRE整体通过或actualPOST/DAY。

14948/WorldDrive本人实际[exact-v1](https://arxiv.org/html/2603.14948v1)§3.1–3.4/Eq1–7、§4.1–4.5/Tables1–7与关键预算/反侧；Source与2+2+2=6通过。训练按候选trajectory条件由冻结TA-DiT提供future target，query decoder从当前scene/候选直接预测latent，部署移除重生成器但保留forecast→critic，不把预测升级真实可达未来。16A100/batch32→8RTX3090/batch256/50epochs→FAR10epochs/冻结planner、A800平均53ms对不同PWM850ms全计费且不授预算匹配或tail SLO。Oracle best6只作ceiling，TTC94.3低于94.7、视频FVD131.7差于DriveWM122.7保留；NAVSIM非反应式与v2反应式pseudo simulation及nuScenes开放循环分开，不授物理驾驶安全。本人实际Ch25 357–375/945–989完整training-only塑形→Pixels/真实feedback与Ch26 439–474相关teacher/predicted-change消费者交接：具体teacher rollout→部署latent forecast→critic差额成立；SUP_REMAINING_OWNER_PRE第二节两段逐字稿唯一MULTIMODAL-WORLD-MODELS PRE通过，当前插入为968后/970 Pixels前。尚未写入、不授POST或DAY，root另行协调窄锁。

15432/Gym-V本人实际[exact-v1](https://arxiv.org/html/2603.15432v1)§3.1–3.5、§4.1–4.3/Figs4–6/Table4必要Source通过，3+2+2=7保留。底层dynamics不变而rules/caption/history wrapper改变学习曲线，适用于Qwen2.5VL7B、12single-turn/4multi-turn三算法的有限研究；recent3/5实际为此前2/4对observation/action，Minesweeper无rules更高和Geometry→Algorithmic−1.1/FrozenLake→2048−2.7保留。字幕引入state信息不授像素感知能力提高，wrapper/API公开描述不等已核实现或全部奖励保真；作者同预算声明未补全实际设备/precision/batch/seed/训练总费。179/202及10/11类别口径冲突不用于库存分母，仅采用明确16环境实验。actualCh66 220–269（尤其230–261）与4198–4207完整scaffold干预邻接已读，rules可见性/history混杂、完整subject/protocol adapter非中性及独立scaffold intervention实际已有覆盖，唯一PLATFORM-EVALUATION-SYSTEM具体NC通过；不把接口标准化当新增RL算法、不因NC降分、不授普遍正transfer/安全或DAY。

本轮压缩恢复再次独立重读AGENTS、研究/Report合同、统一prompt、完整ROADMAP、来源使用/每日及arXiv主题边界、LS当前恢复路由和本日完整停点。只接当日具名单篇，不恢复宽列表队列；旧暂停段不覆盖当前授权恢复，不授DAY。

14938/FARDrive本人实际[exact-v1](https://arxiv.org/html/2603.14938v1)§3.1–3.4、§4.1–4.3/Tables1–3必要原证；随机history horizon→逐步将当前generated latent与GT混合→后续整段mixed history自条件、frame VAE/history KV/固定control feature cache分责均受限Source通过，2+2+2=6不降分。AR1/3steps与AR16/30steps不能直接因果比较；8训练帧到229视觉rollout不证明真实闭环驾驶。Table3 H200六view576×1024每迭代1step .84s/FID25.94对20steps3.36s/FID11.92，20steps关KV8.15s却FVD80.53优于82.78保留，NPU型号/precision/request batch/concurrency/SLO及匹配总训练费未披露。actualCh25完整688–694真实历史→自产history/分别扰动/生成回流及723–759因果少步→self-rollout→真实观测reconcile已实际读；唯一MULTIMODAL-WORLD-MODELS具体训练人口、错误反馈、限定horizon与费用责任已有覆盖NC通过，不宣称现文含本精确blend公式或任意OOD纠错，不以成熟组合排除候选，不授artifact/复现或DAY。

独立切回本18重读AGENTS、研究/Report合同、统一prompt、ROADMAP、来源使用/每日/arXiv主题边界及最新本日checkpoint、SUP_SOURCE_STOP。15195/15590必要Source、PRE、actualPOST及本人末注最终读回按未变身份/精确版本/命题有效复用，不重读相同核心/正文；本轮只own独核记录，不写Books、报告、LS或索引，不stage/commit/push。

14825作者新增Table9 notes已本人实际定点更新后回读SUP_EVIDENCE_TITLE_COMPLEMENT首两段：C.3/Table9攻击后Perspective/Detoxify平均toxicity口径、约56–78残余与表头ASR冲突限定准确，局部PASS。复用此前必要Source/actualCh23具体NoChange，不把新增notes认作新安全证书或ASR数字，不重复附件。

15059在恢复后root新窄锁下已作者实际写入；本人非writer实际顺读Ch28 561–585完整whitening→modulation order→新570→两侧geometry/幅度控制邻接，及1861–1875本人1869和15195邻注。回对有效root必要Source及已正式核过SUP_BOOKS_NEW_PRE一段，正文逐字一致，loss下界/无偏有限p矩/β=0/joint求和/liminf而非parameter convergence、严格更快与缺秩recipe隔离、费用与旧路径保持，局部actualPOST PASS。本人注目前仍待作者同步真实非writer身份与范围，最终更新后定点回读尚待，不授DAY或复现。

15279/LOOM root恢复后正式确认必要Source限定通过，有效复用其暂停前实际exact-v1 §3.1–3.3、§4.1–4.2/Tables1–3与B/C/D/G必要原证及其保存的反侧，不重读相同核心。本人实际Ch24 239–286端点配对的完整population prox→learned forward bridge邻接与SUP_LOOM_PRE两段逐字稿：有限训练集的跨batch持久permutation是当前具体差额，唯一MULTIMODAL-GENERATIVE-PARADIGMS；cache/配对identity、tie不等最终映射固定、小batch次优/固定noise过拟合、条件source marginal、OT-CFM部分更优和总训练费用均保持。受限Source复用、actual唯一owner与两段逐字PRE正式PASS；不采stationary optimal/唯一或tie-final映射/免费预算/条件生成保证。尚未实际写入，POST未发生，不预支完成或释放root窄锁。

15059唯一本人注1869更新后再次实际定点顺读1865–1873，与15195邻注分开；真实resume_review17_18非writer actualPOST身份/561–585与1861–1875范围准确，未扩大Source/理论采用边界。最终末注回读局部PASS，已通知root可释放该family的Ch28窄锁，不授DAY。

本次切18重新独立重读适用合同/统一入口/ROADMAP、来源使用/每日/arXiv及当前恢复checkpoint、本日SUP_SOURCE_STOP；仅处理本日具名接口。15279/LOOM已作者在root窄锁实际写入，本人非writer实际顺读Ch24 252–276完整离线网格/多步forecast→population prox→新262/264→learned forward bridge及2429–2437本人2435/邻注。回对已正式通过的逐字PRE与root有效限定Source，新两段完全一致、持久配对状态不冒充population最优/固定tie mapping，条件source偏置、费用、OT-CFM反侧与旧路径保持，actualPOST局部通过。本人注仍待作者同步真实resume_review17_18身份/完整范围后最终定点回读，当前不释放root锁，不授DAY、artifact或复现。

LOOM本人2435注同步后本人实际定点顺读Ch24 2431–2438，再核唯一family的真实非writer身份、252–276及2429–2437范围与邻注分开，最终末注局部PASS，可由root释放该窄锁；不重读相同Source/PRE，不授DAY。

14851/AutoMoT本人实际[exact-v1](https://arxiv.org/html/2603.14851v1)§3.1–3.3/Eq3–5、§4.1–4.4/Tables4–5必要原证及actualCh26 922–947完整Fast-Slow→SaiVLA→AR-VLA接口，Source与唯一MULTIMODAL-EMBODIED-VLA具体已有覆盖NC局部通过，2+2+2=6不因NC降分。冻结UE低频per-layer KV、AE当前KV联合读取及0.5–1秒训练错位支持有限staleness实例，现正文已经实际承载频率/状态身份/训练部署staleness/费用/controller责任；不把KV concat或有限错位当通用recipe另写。同步.322/.38s对异步.326/.05s、fine-tune语义反退、CARLA闭环与nuScenes开放循环分开，不授实路安全/总预算因果净加速；8A100仅训练不补推理设备、未核artifact/复现或DAY。

14892/PromPrune本人实际[exact-v1](https://arxiv.org/html/2603.14892v1)§3.1–3.4、§4.1–4.3/Tables1–6及B/C必要反侧，Source与2+1+2=5局部通过。固定总token预算由单图谱entropy分saliency/coverage、先saliency后剩余池DPP，不是动态总长度；700 GPT4o分组关联非逐图语义真值，1000图校准/μ/τ与crop失配、selector费用均限定。Table4局部93.6→96.1不授无损；SQA的FPS/FL优于DPP、同320预算402.7ms慢于Div388.5/Vis321.1反侧保留。actualCh23 584–634完整固定预算→content/redundancy分配→selector与保留层/DPP代理边界已读，唯一MULTIMODAL-REPRESENTATION的稳定分责与失败链已有覆盖NC通过，不宣称现文载有本精确谱entropy公式/μ/τ或普遍最优；不凭NC改准入/降分，不授artifact/复现或DAY。
