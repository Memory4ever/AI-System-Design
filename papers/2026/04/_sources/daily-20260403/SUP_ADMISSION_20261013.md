# 2026-04-03 source omission supplement：首批准入校准

## 2026-10-13 fresh reader 实际停点：额度暂停，非日级验收

复核者：`apr03_finish_reader`（非报告作者、非 Books writer）。已完整重读当日 AGENTS、Prompt、研究/Report 合同、每日来源及 arXiv 主题路由、ROADMAP 与本日最小路由；只处理本日既有11普通项，不扩发现、日期或附件。root 最新指令要求立即暂停，因此下列记录覆盖“reader仍在执行”的旧停点，不覆盖此前31真实 POST 或其他有效层。**本日报仍进行中；本轮未执行 DAY/完成态 FINAL，不授整日验收。**

### 本 reader 已实际核对的精确原稿

以下原文均为 `https://arxiv.org/html/2604.<ID>v1`，直接打开必要 HTML 正文；作者 packet 只用作路由，不当正文替代物。未复现实验、未核实现，也不授全篇/全附件已读。

| ID | 实际支持与反侧读取 | 独立判断与采用边界 |
| --- | --- | --- |
| 00799 | §3.2–3.4/4.1–4.3、Tables1–4 | 2+2+2=6，限定准入/标准 Source 通过。真实多视图 pose 不一致与 semantic identity 分责值得保留；self-paste/no-change 仍高于 chance 且有 selection bias，不能证明所有3D推理失败或 artifact 全排除。**纠错：实际手工筛选/人评为615 pairs，不是作者 packet 的6151。** §3.3 bbox扩大20%与Table4/末文生成default5%不一致，不自行合并成统一default。 |
| 00829 | §3.1–3.2/4.1–4.4/5/6，Tables7–10 | 2+2+2=6，限定准入/标准 Source 通过。frozen teacher 读取 student multimodal K/V、来源选择 teacher signal 的资格可采用；teacher 不是独立原语言输出真值。uniform/selective 的α/T共变，不能只归因选择器；OCR/DocVQA/部分语言任务仍退步，训练双塔费用仍计入。 |
| 00903 | §3.3/4.1–4.3/5.1–5.3、Tables4/9/10 | 拟2+2+2=6，安全受影响内容深入 Source 通过，完整题摘准入层见下段。authorized personalization 与公开生成 output linkability 是具体威胁边界；PGD照片是私有训练变量，不是公开照片保护或DP。质量指标退步、stage/joint局部收益及held-out retrieval仍可高关联必须保留；不授不可关联/生产隐私保证，也不统一正文与表格ρ。 |
| 00913 | §3.4/4.1–4.3/5.1、Table5 | 2+2+2=6，限定准入/标准 Source 通过。跨depiction测量与加/换文字 input-policy 分责是具体评价盲点；D2收益不推出T1收益。TextOnly不是同一跨depiction输入资格，CKA/attention不能证明信息不可恢复或encoder瓶颈因果。 |
| 01151 | §3.1–3.3/4.1–4.4、Table1及39 matched局部分析说明 | 拟2+2+2=6，安全受影响内容深入 Source 通过，完整题摘准入层见下段。群体聚合与observer/label人口需绑定；指令标签、4项未执行剔除、不同round提取、Transfer方向反转与privileged observer缺口均实际可见。AUROC不是阈值安全gate，schematic heatmap非像素/因果定位，adaptive攻击未测。 |
| 01161 | §3–4、AppendixA/B、Tables1–4 | 拟2+2+2=6，必要标准 Source 内容通过，完整题摘准入层见下段。context-dependent stop与有效reasoning预算值得保留；same-prefix最后50token重采样支持有限行为差额，不证明质量变化全由verification缩短。Subtask分摊token不是同单题budget，Kimi多turn及Olmo Instruct长输入存在更长反侧，prefill费用仍需记账。 |

上述6项仅是 reader 的贡献/必要 Source 裁决；公开日期链沿用已有效的本日日期层，**本 reader 暂停前未另实际读回 EXTRA7/1152注册投影，不能将其冒称本 reader 新独核。** 已将799/829/903/913/1151具体结果直接告知作者/root；本表保存1161的真实结果供恢复。Books owner具体差额/PRE均尚未由本 reader 完成，不授锁、未写书。

层级补充：799/829/913的完整v1题摘已在实际HTML结果中读到；903/1151/1161本 reader已实际读取上述必要方法、评价和反侧，但暂停前未另完整读回其matching题摘。故这三项记录只是足以支持表中窄命题的正文 Source 独核，不代替尚未有效完成的完整题摘准入校准；若既有准入未通过，恢复只补读这三条现存题摘，而不重新深审已有效的正文。不能据本表直接批量加6个正式候选或称全部准入/日期门通过。

### 暂停时仍未闭合的普通集合

- 00519：本 reader 尚未打开其必要原稿，作者拟EX不是本 reader通过。
- 00923：已实际读题摘、Methodology部分及Results/Sequential/Limitations原文；尚未完整闭合实验配置/embedding-head与k口径，普通必要复核待续，不授Source通过。
- 00938：已实际读§3.2–3.5/4.1–4.5/AppendixB.1–B.3，看到remain近似与实际798/800、786/800、representation球及Eq12 gap常数边界；**Alg1尚未实际读到**，必要Source/采用与Books尚待，不自补定理或宣判全部radius无效。
- 01152：已实际读§3.5–3.6/4.1–4.3及Tables1/3/4。sampled-span投影与冻结旧path不推出mixed-route零遗忘，chat floor=.20及routed退步是实际设计反侧；本 reader未签作者EX，也未准入评分。下一步只比较Ch30具体已有论点后裁决是否构成需要收录的设计修正，再定点补缺失必要位置；不全篇重审。
- 01170：已实际读§3.2–3.4/4.1–4.4及Tables2–4、AppendixA/B。score-before-update/reset、完整随机算法LTT、iid/fixed outer/同policy前提及λ0未定义、累计标签与真实正确性、OOD超δ均已核；Table5机制对照尚未实际读，正式采用/Source与Books仍待，不授on-policy实验或任意OOD risk保证。
- 15具名EX的分层题摘抽检/必要安全否侧：本 reader尚未开始，不能冒15全量通过，恢复仍用SUP_REMAINING_AB最小路由。
- QUEST：本 reader只读既有日期出口packet，未实际核author C71/BibTeX、exact PDF/forum/API原证；日期隔离出口独核仍待，不冒贡献EX或Apr02新首发。

没有新的外部HOLD；以上是暂停的普通工作。此前31真实Books非writer POST继续有效，不重审。尚可执行的作者Report同步、6项owner差额/PRE及必要写后复核、上述剩余Source/EX/QUEST、全六部分DAY和完成态FINAL均未被本表预支。**遵守用户/root额度暂停：仅保存停点并结束，不接04-04或任何其它日期，待用户明确恢复。**

## 最新有限停止 / 当前实际出口

当前实际更新：正式35新增/总97＝31 actual Books＋2仅报告＋2中心D。RFM/RELISH/Omni/QAsk、Dynin/DisCo和ViewScaling/OmniVoice/SCT/Ego十个最新单段root实际nonwriter POST已通过且窄锁全部释放，回执同各PRE，正式报告已同步。其余11ordinary与15具名EX独核尚未结，发现保持STOP，不把作者core已读当root Source通过。日期上界EXTRA6两行/EXTRA7九行是定点owned公开状态投影，与MM下界组合而非注册独自证明first-public；后九不是9个准入。下段18仅上一快照履历。

当前机器层：97候选行、229本地引用存在、原62整行及连续原§4逐字冻结、V3与限定unstaged diff检查通过；只证明接口与冻结，不授Source/日级验收。最后普通Source集合为00519/00799/00829/00903/00923/00938/01151/01152/01161/01170，其中519/1152作者拟EX须非作者实际裁决；SUP_REMAINING_AB另15具名EX分层校准未结，不冒全量负侧通过。QUEST精确forum日期出口独核另待本日SUP_QUEST_DATE_EXIT，SafeReAct反证出口已通过。root已fresh委派`apr03_finish_reader`仅接该最小集合/QUEST出口，他直接逐项给作者与root；作者保存此停点后结束当前turn，收到明确结果再followup本日，不空转或换日。Books锁仍由root协调且现全部释放，31处有效POST不重做；最终root只接真实DAY/FINAL。用户停止边界只收尾04-03，整体验收后暂停；剩余ordinary不转外部HOLD。

### Fresh reader 最小路由（现有有效层复用，不新发现）

启动按当前AGENTS完整加载适用合同/每日源与arXiv主题路由/ROADMAP/本日停点，只读本日。旧62/连续原§4冻结；本轮35正式家族逐项必要Source、31真实PRE/POST和两仅报告/两D均有root实际独核回执，引用各现存packet即可，不无差别重读。当前report仍进行中，reader先完成下表实际原证必要裁决，具体Source可单篇返回；作者才申请owner差额/窄PRE，root控制锁/actualPOST。最终六部分ready再DAY与一次完成态FINAL，不把机器通过当日级验收。

下表均已有作者必要原证读到具体停止，拟6/7或EX只作者判断，非新完成收据。精确原稿全部 `https://arxiv.org/html/2604.<ID>v1`，原题摘身份在现有 `SUP_EXACT_V1_AB_1/2/3_20261013.json` 或 `SUP_EARLY_AB_1/2_20261013.json` 的matching entry。方法/反侧按原章节最小读取，不读无关proof/附录/code；packet是路由与作者采用范围，不替原证。

| 剩余ID / 本地作者packet | 原稿最小支持＋直接反侧位置 | 待非作者裁决的窄范围 |
| --- | --- | --- |
| 00519 / SUP_SEVENTH_CORE | §4.1–4.4/5.2–5.4、Table7/必要A5–A6 | learnability/reference加diffusion guidance/repulsion的成熟组合是否有实际新增成立条件；作者拟EX，不因CNN负载排 |
| 00799 / SUP_NINTH_CORE | §3.2–3.4/4.1–4.3 | 三view换pose/局部几何与identity分责；self-paste/no-change仍高chance/selection与inpaint残余，拟6不授全部3D失败 |
| 00829 / SUP_NINTH_CORE | §3.1–3.2/4.1–4.3、Tables7–10 | frozen text-query teacher读取student multimodal K/V；来源选择KD与α共变/OCR退步，拟6不授全部知识保留 |
| 00903 / SUP_NINTH_CORE | §3.3/4.1–4.3/5.1–5.3、Tables4/9/10 | 授权个性化私照PGD/FT循环与公开生成FR observer；quality退/held-out仍关联、ρ不统一，安全深入拟6 |
| 00913 / SUP_NINTH_CORE | §3.4/4.2–4.3/5.1、Table5 | 跨depiction与加入/替换description人口；任务反退/CKA非信息损失，拟6非家具标签EX |
| 00923 / SUP_TENTH_CORE | Methodology/Results/Limitations | front/rear层选择含embedding/head、k不计两者；sequential反退与预算，拟6不借脑区类比 |
| 00938 / SUP_TENTH_CORE | §3.2–3.5/Alg1/4.1–4.3及必要B.1–B.3 | frozen upstream/top-r QP/真实repair停止；linearized remain非全margin、表示ball非tokens、Eq12不自补，纠错深入拟6 |
| 01151 / SUP_TENTH_CORE | §3.1–3.3/4/Table1/4.4 | collective activation features、instruction labels/不同round/transfer反转、observer缺口与adaptive未测；安全深入拟6 |
| 01152 / SUP_TENTH_CORE | §3.2/3.5–3.6/4.1–4.3、Tables1/3/4 | sampled output-span SVD＋router成熟组合；独占旧path非mixed-route零遗忘，作者拟EX，保明确重开命题 |
| 01161 / SUP_ELEVENTH_CORE | §3–4/必要A/B | context依赖stop/firstcandidate/verification代理；same-prefix resample与非匹配budget/个别长生成反侧，拟6 |
| 01170 / SUP_ELEVENTH_CORE | §3.2–3.4/4/Tables2–5及必要A/B | score-beforeupdate/reset与LTT完整算法/iid边界；λ0未定义、OOD/error label/全費，不授任意shift risk，拟7深入 |

日期复用：后九ID在 `SUP_DATACITE_BOUNDS_EXTRA7_20261013.json`、1152在原27，client/state/registered/matchingURL原值可实际读；官方MM04不可backdate给Apr02下界＋owned公开状态给同日上界，不以Submitted/created/registered单独认证，已知更早正式全文反证仍优先。519明确EX时不为不影响处置的日期另立请求；若实质重开才恢复必要日期。新688/733两投影在EXTRA6，原557/1001分别原27/EXTRA，有效链不重复。

15具名贡献前EX分层校准入口只 `SUP_REMAINING_AB_20261013.md`：00086HIVE、00222riskCI、00239PLtaxonomy、00422SHARPEN、00442EVOM、00696TTA-Vid、00842Pare、00853MotionGrounder、00920GPTNL、00947randomlanguagephysics、00969DLWM、00977FPDRL、01142DDPG+boundedES、01195ORBIT、01212YC-Bench；完整v1题摘在上述EARLY/EXACT matching entry，不以作者简记代替实际题摘。按来源/主题/排除理由抽检且明确样本、未检查范围；纠错/安全/设计反证信号须实际核受影响内容，共同错误仅重开相关集合，不把15变新增全类队列。

QUEST仅看现有 `SUP_QUEST_DATE_EXIT_20261013.md` 的确切author primary C71/BibTeX与forum `HkztQWZfl2` / exact OpenReview PDF identity和API403；不得串C72邻居、不绕挑战、搜索7个月不作精确日期。精确first-public日无法恢复则安全日期隔离，不评4月2新首发、不扩2025/2026全部revision。SafeReAct已root实际NeurIPS2025反证出口复用。

发现仍四query220槽/186身份、主题前缀129标题槽，68完整v1题摘；作者必要core在SUP_THIRD～ELEVENTH各packet已到具体采用/EX/日期隔离，停止其它附件。root未核项不继承PASS。现正式18新增/总80：14 actual Books POST通过并释放，RSP/OCR两仅报告，CircuitProbe/TAC两中心争议不Books；后两owned日期已root独核。四最新Integration回执同PRE_THIRD_FOURTH；FLB/speech Source/PRE通过且已实写，actual POST待核，暂不计formal14。QMask/CI/Refusal Source已过，PRE_QMASK_CI_REFUSAL待授；FGR Source过待owner。其余各批独核仍ordinary，外部HOLD不变；本report/原62/连续原§4冻结检查通过，不自授DAY/Complete。下列早阶段记录只保留履历，不覆盖本最新停点。

作者：`supp_apr03_20261013`。补窗仅 2026-04-02 北京时间自然日；原 62 家族、评分/日期/窗口及连续 §4 冻结，基线见 `baseline-before-supplement-20261013.md`。旧完成/独核不替代本轮。

## 实际发现范围与停止

四主题 arXiv API 以 submittedDate `202603311800–202604011800` 作为**线索**范围（不是公开日期），MODEL/AGENT/MULTIMODAL 起点0各返回35，RUNTIME返回31且已到total31；总136槽/122身份。前三入口 total65/82/42，尚未将剩余条目作题摘审阅；宽返回含医学/领域应用，不变成全类关闭队列。各 query、完整返回题摘、版本字段保存 `SUP_QUERY_*_20261013.json`；本阶段只对下列具名材料实际阅读完整题摘，不称136均已语义初筛。

Qwen动态40项实际恢复到字段；04-02唯一 `qwen3.6`，`extra.date=2026-04-02T04:00:00+08:00`。同一发布事件原04-02已具体贡献前关闭：`../daily-20260402/v3-reopen-notes.md` 的到期来源SRC-QWEN行，厂商受限能力结果及 `preserve_thinking` 默认false API事实，没有新训练/架构因果机制；具名复用，不再进入候选。Hunyuan EN全部9/9元数据已恢复，仅目录不含04-02，不扩大到作者全部未列稿。Seed页面40起片取得，必要窗口目录停止尚可继续；普通待办不HOLD。

## 首批潜力（未经独立校准，不评分/计新增确定）

| family / 精确材料 | 实际新增命题与受影响选择 | 本轮日期/重复门 |
| --- | --- | --- |
| [DRKL 2604.00223v1](https://arxiv.org/abs/2604.00223v1) | RKL mode-seeking不是单纯词表大小问题→目标/非目标梯度分账并修改非目标监督→蒸馏质量与输出多样性可能需要联合目标；这是原文增量而非泛化为任何teacher/student配置。 | v1题摘已实际读；Submitted Mar31不是Apr02公开日。原04-02未见正式family，待首次公告门，不先评分。 |
| [Learning to Shuffle 2604.00260v1](https://arxiv.org/abs/2604.00260v1) | 任意epoch排列收敛不意味着排列常数等价→block reshuffle降低prefix-gradient方差、paired reversal消二阶order项→训练数据顺序的方差/步长敏感性选择可能需收窄。 | v1题摘已读；不因理论/小实验排除；必要公开日与理论假设仍待后续门。 |
| [Asymmetric Actor-Critic 2604.00304v1](https://arxiv.org/abs/2604.00304v1) | 黑盒actor不可重训、单次interaction不可重试→小critic在同条trajectory内监看/干预→可能将事后反思换为本轮action监督；是否超出成熟actor+critic组合，须决定性core定点核。 | v1题摘已读，潜力不是确定准入；拟定点core解决组合误收风险，公开日期待核。 |
| [In-training Probe 2604.01025v1](https://arxiv.org/abs/2604.01025v1) | PPL与下游成功不同步且生成式evaluation贵→用checkpoint内部表示预测pass@1、早期probe预测后期checkpoint→可作训练监测sensor分支；不让probe获得release权。 | v1题摘已读；潜力不由1h→3min数字或Ch66可映决定，公开日期待核。 |
| [Secure Forgetting 2604.00430v1](https://arxiv.org/abs/2604.00430v1) | 原文称自然语言unlearning与对抗查询能隐私遗忘→需核究竟改参数、prompt还是Agent state及observer→安全采用边界可能受影响。 | v1题摘已读；安全声明须必要core，不因“已有遗忘章”关闭；公开日期门仍未过。 |
| [Anthropic RSP v3.1 / Roadmap Apr02事件](https://www.anthropic.com/responsible-scaling-policy) | 官方Apr02日志把AI R&D阈值明确为aggregate capability progress，而非研究员productivity；并明确自愿暂停开发不受强制触发限定。另Roadmap公告两个goal状态变化。→阈值估计对象及政策义务/自愿措施需要分账。 | 官方原始Apr02日值按当前自然日规则，不再追09:00边界；旧本日报§5仅因旧精确窗口隔离，未采用/未评分。拟读精确v3.1及redline受影响句；现current Roadmap已有May/Jul修改，不能倒灌。 |

## 代表性负侧

| family | 具体初判与完整题摘边界 |
| --- | --- |
| [2604.00725v1 Historical Newspaper OCR](https://arxiv.org/abs/2604.00725v1) | v1题摘需完整核后裁决；不能把已抓v2的后发题摘当v1。所见标题是OCR encoder比较，不因SSM/Transformer关键词自动入选；如具体长度/表示替代条件存在则重开，不预先EX。 |
| [2604.00469v1 MS lesions](https://arxiv.org/abs/2604.00469v1) | 明确医学影像病灶分割，使用U-net/Transformer并非形成模型/系统机制；按ROADMAP暂缓AI for Science范围关闭，不经Ch23/Ch66类比重入。 |
| [2604.01169v1 ADA](https://arxiv.org/abs/2604.01169v1) | 题摘有理论distribution alignment，但原文目标/证据是atomic/Boltzmann及molecular/protein实验；不因domain-agnostic自述把Science领域模拟对齐自动升到VLA/world dynamics。请独核其范围出口，若确有直接形成模型主线机制则纠正。 |
| Qwen3.6 Apr02事件 | 具名复用原04-02具体关闭，不重数。 |

## 下一具体事项

root校准上述潜力、范围负侧和日期出口；作者继续机构本窗字段与有界相关标题查漏。校准前不写Books、不把任何API published/submitted或DOI-created当first-public。随后只推进已确认本窗/未重复的必要单项，不把初筛潜力变全篇阅读队列。

## 当前停点（覆盖上面的首批阶段性数字/待办）

发现已停止，实际最终有限发现与14源停点见SUP_SOURCE_STOP。四主题完整分页220槽186身份；宽主题prefix129标题槽只查漏，不转全类关闭；实际63 pinned-v1+首批另5=68完整题摘。root已实际首批v1题摘校准DRKL/Shuffle/Probe潜力，纠正OCR不能按领域标签EX，MS7T局部segmentation具体EX，ADA只Science当前暂缓无基础生成桥不收。日期上下界独核见SUP_DATE_RULE/真实27投影，不把日期投影计候选。

DRKL/Shuffle/Probe必要Source已root通过；RSP5分仅报告单family两关联事件已root独核并入正式表/增量§4。DRKL Ch29逐字PRE及窄锁已root通过，作者写后局部实际顺读，root nonwriter POST已通过且锁释放，回执见SUP_BOOKS_PRE_DRKL；Shuffle/Probe仅申请各owner PRE未写。AAC窄核心拟EX及SecureForget同v1原证EX交root，不自签；OCRparagraph/length实际读到收益和直接反侧即止，拟5分精确对照另交独核。普通可执行归并、必要Source/Books/DAY不改外部HOLD，不声称全日完成。

上述历史停点已推进：Shuffle/Probe实际PRE/POST通过；AAC成熟verbal critique/revision+干预SFT、SecureForget成熟DPO prompt/memory目标分层、Gemma首发仅variant/模态/既有MoE事实均root原证贡献前关闭，SecureNL utility与Code baseline已正确分开。OCR5分标准/仅报告root actual Tables6/7反側通过。Source A/B七项root必要原证与唯一owner逐字PRE、10月13 actual非writer POST全部通过：00001Ch27/00004Ch22、00028纠正LQ1 Decode归Ch44（Ch43没写）、00821Ch49、00208Ch66、00770/00072Ch72。连同首批三项Books，目前正式新增12=10真实Integration+RSP/OCR仅报告2，总74；所有这批窄锁释放。

第三～六批必要Source ready但尚未root通过的层不自签：SUP_THIRD_CORE_DECISIONS、SUP_FOURTH_CORE、SUP_FIFTH_CORE、SUP_SIXTH_CORE；00012更早NeurIPS2025全文日期出口经root独核，不按Apr02first-public评分。有限余项尚有普通必要core和具体Books/DAY，不当外部HOLD。下一具体源项00445/00455/00489/00519决定性core，无新发现或跨日队列。
