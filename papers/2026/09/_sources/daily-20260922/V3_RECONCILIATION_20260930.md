# 09/22 V3 当前作者接续

作者：sep22_resume_v3。范围仅 `[2026-09-21T09:00:00+08:00,2026-09-22T09:00:00+08:00)`；本文件接续既有 `arxiv-recovery-20260927.md`，不是第二份完成收据。AGENTS、研究/Report V3合同、统一Prompt、来源说明/每日/按需和arXiv主题、ROADMAP、本日README与三份旧账本及最新恢复§7均已读。保护已有staged/dirty，不stage/commit/push。

## 实际队列与复用边界

发现身份1746=1003 New+183 Cross-only+560 Replacement-only。旧68中67个v1归09/21，只保留原证据；旧09/23的38个家族均归本日。42项工作池=38+H-Spec1+NSP/SPLASH/SPECTRA3，还不是最终分母。09/23作者apr29_close拥有对方README，本作者迁入有效表/证据后通知其移除旧候选；旧`papers/2026/_sources/daily-20260923/`附件保留，不整段复用旧Complete。

普通待办：5 Date Hold、2理论、1版本正确性、Cross22547/23570及具名重要revision信号；13机构有限恢复（含MiMo工具PR）；三项Books写入与必要新增判断；最后非作者全positive/风险negative及其他分层抽核。普通未读不写外部受阻。

## 09/30实际原始证据推进

- **NSP 2609.22755v1**：本轮curl实际取得834474-byte、19页PDF（`/private/tmp/sep22-nsp-v1.pdf`，临时缓存不是永久依据），pypdf实际读pp.5–13 §3.3–6.4。确认nested aligned power-of-two SP tree、token budget/proxy planner、phase issue order、group-uniform save/remat、input/reverse all-to-all保持loss identity。§6明确省略GPU型号；mixed precision未给dtype。保留此前评价/反例，不把64GPU normalized结果写成具体型号或独立复现。需要root非作者证据复核及Ch36实际写入。
- **SPECTRA 2609.24847v1**：本轮actual HTML §4.1–4.4已读，20tiles=14accel+4memory+processor+I/O；same-prompt matched target-only到spec实际完成长度；vector/systolic反事实及Table2资源代价；Jetson引用文献latency，不是同硬件实测。需要继续核完整HTML的精度字段；若确未披露，写Not Disclosed，不把未读变Not Disclosed。
- **CKDA 2609.24797v1**：完整摘要、§3–6/Theorem1–5实际读。旧“必须真实LM scale才收理论”误门槛撤销：单位key、signed channel gate[-1,1]与β[0,2]组合令实数DPR1 transition产生旋转/复特征值，同时non-expansive；单layer有限SO(3)子群tracking及S5 finite-reachability反证有精确前提。WFAs扩展需要β>2、polynomial precision/exact algebraic arithmetic，不在稳定范围内。1.3B/100B-token结果接近bounded KDA而非普胜，GRU在周期任务仍更好。拟新增6=2+1+3，owner MODEL-LONG-CONTEXT，待非作者准入校准与必要Books差异。
- **Exactness 2609.24942v1**：完整摘要、§2.3、§5.2–5.3及§9实际读。作者明确criterion不是定理，未证明OOD必要性；连续分析限unbounded-output regression，关系分析限free per-entity parameters；文章自己承认normalized MLP、binding/indirection、symmetry等反例。不能把所有OOD泛化必须exact写入Books。准入时潜在改变表达/OOD解释仍存在，待按窄争议终态作候选处置，不能省工暗删。
- **MPS 2609.22991v1**：完整摘要、§3环境/axes、§4.3、§5、§6.2已读：单M2Ultra192GB/macOS27，fp32/fp16，11PyTorch版本2.4.1–2.14；bmm systematic sweep，CPUfloat64为oracle，CUDA只control（arange也错误）；inclusive numel>=2^32 guard会误阻正确大tensor，设备侧切块view的大storage offset没测。官方[Issue197636](https://github.com/pytorch/pytorch/issues/197636)于09/19已公开核心stride/large-output错误与实例，不是本窗初次发现。论文新增input-wrap/跨版本/guard预算是否构成重要证据事件与首次issue日期继续定点核。
- **Cross22547/23570**：actual v1完整摘要已读，潜在贡献明确，不以Cross标签拒绝。22547 paired simultaneous confidence bands与条件kernel异质性修正pass@k crossover解释；23570先用executable outcome核oracle-history usefulness，再考察memory系统是否交付。版本v1提交字段仅作身份，不能冒充公开；需要官方公告/首公开定点确认与必要机制评价。
- **MiMo-Code PR2456/2463/2455**：GitHub API实际核`created_at=09-21T10:37:32Z/16:43:55Z/09:19:39Z`，均本日。全文body实际读：per-agent/step FIFO仅read/grep/glob重叠、跨agent不共享gate；生成完前buffer最多16/第17取消整未执行批，non-read failure/invalid call级联取消；persisted结果不重放/主actor拥有checkpoint/status。作者测试声明不是本地复现。需对现有Ch78/81/84具体合同检查，release时间不能取代PR首公。

## 仍需执行

### 日期停点有限终态（09/30本轮实际检查）

- 22125：完整题摘与[TyDe官方日程](https://tydeworkshop.org/2026)实际读到Aug27 fullpaper同题、作者、PDF与video；足以表明更早公开报告，PDF精确首次上线未知，故不作为本窗firstpublic候选，保留真实早期owner恢复线索；重开需要Aug27报告/PDF正式公开档案，不再追submitted。
- 22195：[OpenKedge官方页](https://www.openkedge.io/paper/persistent-cognitive-identity/situated-identity-test)核心命题/当前结果实际读，未给首次发布日期；官方SITBench repo全文入口与release API实际检查为空数组。当前页/commit日期不能锁首次公众可见，Date Hold终态隔离，不评分不写Books。接受作者发布时间/可信网页归档后仅重开本family。
- 22819/24144/24812：复用既有精确commit内容与时间（workingpaper/pairedrollout反例/MSI权限EvalSpec），本輪逐repo GitHub releases API均实际返回空数组；未获得published_at或正式公告。finite两种原始入口耗尽，保留3项Date Hold终态，不以commit或created_at填时钟，不用它们支撑Books/positive/零遗漏。重开需作者官方公告、可信归档或release公开时间；24144须同时辨别核心方案与后续gradient证据的重要事件。

以上5项日期条件缺失已隔离，不再是未读普通队列，也不是日期Evidence/Coverage通过。尚未读理论/版本/revision不因此隔离。

### 追加必要源实读：SPLASH / SPECTRA / CKDA

SPLASH本轮exact-v1 HTML §4–8.5实际重读：co-selection 512观测/16component/page固定写入；GQA meanquery、centroid只等价平均logit，page ranking近似；per-plane cap放弃某些global top-k改变quality。§7 single-writer、program完成才推进horizon、step开始latch保证不读未提交页；不能推广到多writer任意GC。§8.1明确全部serving结果来自OpenHBF+Vidur Blackwell measured kernels；Llama3-8/70B、Mixtral8x22B、DeepSeek67B、Qwen3235B，BF16weights/KV、128K/512K/1M、B1–128 TP1–8、16Kwindow、10%budget；accuracy仅Llama3.1-8B/positional pages，co-selection单独验证，performance和quality不是同一多模型实测。§8.3 48needle/64K/10% dense.86、Quest.62、SPLASH.50；§8.5 WA1.15未测，uniform wear与30min retention是寿命假设，不是5年硬件保证。作者评分6=2+2+2，因具体Ch54缺口深入核；拟仅写query-driven page translation/commit horizon/per-plane质量代价。

SPECTRA本轮§3.1–3.2 actual重读：同8×8PE/64MAC，通过control/memory indexing切M1 vector与M>1 systolic，不换bitstream；64-bankweight+8-bankinput/psum/output，tile count/MNKshard与reduce/multicast pipeline recipe离线由FPGA-profiledcostmodel选择。全文precision/FP32/bit定点检查：§2的32-bit weight只用于AI roofline推导，§4原型/实验并未锁定MACdtype/量化/累加精度，记Not Disclosed，不把128-bitNoC位宽当计算精度。§4 matched target-only同prompt生成到spec实际长度，第一8轮和完整length-sweep分开；资源LUT/FF明显增加，Jetson latency来自引用而非同硬件matched。评分5=2+1+2，因Ch49实际缺口深入核。

CKDA AppendixE/G.2实际读：理论[-1,1]含0/endpoint，实际signed gate为sign(r)×[e^-5+(1-e^-5)|r|]，在a0不连续且detach sign/abs零subgradient；FP32logmagnitude，integerparityscan把cumulative signs吸收到q/k，最终state/gradient同sign还原；GVA value-head-specific signs要扩q/k。kernelbenchmark排除projection/optimizer/finalstate，H100BF16、16heads128、32768logicaltokens/20warmup50timed×4；PyTorchgauge是不同allocation/fusion参考不能当匹配消融。state tracking训练选best3seeds，exact datatype理论不等于BF16无限长度正确。拟Ch22在写入几何/时间惯性前加短分支：signed coordinate reflection+Householder打开stable旋转，但仍有singlehead spectral/S5条件边界；通用regular/WFA扩张β>2不同。

1. 核理论/日期/Cross/Revision与机构有限队列，保留具体关闭与安全隔离理由；不重扫Weekly或整日无关列表。
2. 迁入38有效表/证据；修正24969原错误“09/23commit早于arXiv”及所有09/23clock句，日期改变不否定机制。
3. 新增Books采用前读写作/学习上下文与owner邻段，向root申请精确窄锁，实际写后交非作者。
4. 全日普通0及非作者Gate通过后才Complete。当前未完成。

### 本窗撤回：2609.16639v2 的正面采用链清理

本轮实际读取[官方精确v2](https://arxiv.org/abs/2609.16639v2)：Comments明示所有作者未一致同意，history `v2 Mon,21Sep2026 09:26:35UTC (1KB)(withdrawn)`；此撤回事件由本窗Tue22 Replacement公告公开，不评分、不留候选。仓库定点搜索发现 Ch29 曾单独采用其“Self-revision连接SFT与on-policy”段，旧恢复记录“无采用链”已失效。root授权Ch29该段窄锁后，实际删除小标题及唯一由此稿支持的正面机制段；保留前面的privileged evidence、teacher/student occupancy、其他有效来源及后面的context distillation。没有该family的Review notes混合证据。官方列出的v3提交为09/22 05:52:45UTC（本窗后）；不凭v3存在恢复本窗正面采用，交真实后续日作者定点判断。

三项新Books已实际落地：Ch36 Attention Workload Pool后的nested-SP分支；Ch54 Persistent Near-memory后的query/page/commit-horizon分支；Ch49 FILCO后的same-PE vector/systolic与profiled-recipe分支。采用边界分别保留greedy-tail预算不可行反例、HBF simulation与needle质量反证、未披露MAC dtype和非matched Jetson对照；等待root写后非作者核。

### CKDA与Exactness终态推进

root独立必要源与Ch22 owner对读后授权CKDA窄写；本轮实际在“写入几何与时间惯性”前写入三段signed reflection→real rotation分支，明确列状态记法、unit-key/β[0,2]/signedgate条件、homogeneous nonexpansive不保证forcing下总state有界、representation不保证learnability、A5随机训练和GRU反例、hybrid Attention混杂、β>2 WFA理论属于不同条件。评分6=2+1+3，深入完成，Books实际整合等待写后核。

Exactness补读§3.6/4.5/9/AppendixA.4后，root认可5=2+1+2的深入争议终态：Criterion的一般OOD必要性未证；A.4给的是误差上界，不能反推实际误差非零/必随组合增长。范围内的MLP/绑定例子不证明所有模型都须exact。保留当窗候选、争议/暂缓，不正面采用或写Books。重开需明确任务与误差含义的必要性证明或可匹配的反证，不能靠增大scale、补另一个宣传实例解决。

### 最新有限队列证据（覆盖前面的过程性待办，不继承完成标签）

root已对NSP Ch36、SPLASH Ch54、SPECTRA Ch49实际新增段以及Ch29撤回删除作非作者写后检查，全部通过，窄锁释放。CKDA已写Ch22:473起三段，root实际文字写后亦通过。机构13入口在本日报§2逐条恢复可核停止点，保留动态目录/日级时钟隔离；不再把这些入口写成未读普通工作。MPS 22991 的5=2+1+2重要修订深入/仅报告校准已获root支持，但不把此校准当作全日Evidence复核。

**22547v1**：完整题摘、[exact-v1](https://arxiv.org/html/2609.22547v1)§3–6/8及B.4证明实际读。固定K、iid prompt、正方差条件下pointwise CLT，Gaussian multiplier同prompt共享系数保留跨k covariance；同一曲线“某k显著不同”不等于crossover，须早段lower>0和晚段upper<0。DeepScaleR与R1-distill-Qwen1.5B的1060prompt、每题128答、T.6/top-p.95，对新32K预算first-cross CI11–61；截断7.8/.7为实测；按假定概率修复截断的敏感性分析是反事实，非观测部署结果。conditional kernel在同p、异q下也异质，held-out answer halves不替代新prompt验证。拟6=2+1+3，Ch66 pass@k层之后加paired simultaneous-band分支，普通待非作者准入/Books窄锁。Cross在官方Tue22列表可核，v1 Fri18 20:03:44UTC过cutoff只辅助身份，不以投稿字段填时钟。

**23570v1**：完整题摘、[exact-v1](https://arxiv.org/html/2609.23570v1)§3.1–3.4、4.3–4.4、5–6实际读。记录构造不读取target gold，但offline oracle筛选确用gold outcome、4seed平均outcome与reference Deepseek-v4-flash最佳memory-combination选择（base<1且正收益），属于有利选择不是部署可获监督。五个solver转移CI均跨0；11/12 memory系统不优于off，单项+2也CI跨0；42% retrieval pairings在memory-off已4/4成功，是headroom限制而非oracle ceiling。即使固定同记录，仍有25.7% target pair受损；内容属性/粗stage标签和词面anchor的kappa .32/.24/.35不提供强因果定位。拟5=2+1+2，Ch77 component matrix后补“verified useful是reference solver条件下的关系”，ordinary等非作者/窄锁。官方Tue22 Cross可核，v1 Sun20提交不是发布时刻。

**MiMo-Code tool-flow family**：[2456](https://github.com/XiaomiMiMo/MiMo-Code/pull/2456) gate.ts全文141行、[2463](https://github.com/XiaomiMiMo/MiMo-Code/pull/2463) gate/processor/flooding.ts全文109行及body实际读。step/agent FIFO只让read/grep/glob同组并行；edit/write/MCP均为barrier，但guest内部执行与跨agent不共享gate。finish前整批buffer，17th取消provider和全部未执行调用；EOF/error无finish也不执行，progress事件不等于tool执行。非read失败/invalid name标失败并取消queued/late，普通read失败豁免；optout flag可禁flood/cascade，不能写无条件安全。完成调用的效果并未rollback，receipt提醒retrySafe=false，执行排序不是事务。[2455](https://github.com/XiaomiMiMo/MiMo-Code/pull/2455)完成结果不重放/main actor checkpoint已经Ch84覆盖，与09/21已审session failure-state family定点去重，不另增独立机制分母。2456初次+2463重要修正同family拟6=2+2+2，Ch78 partial-record合同后补whole-batch admission与step-local ordering；待非作者准入/窄锁。

**2602.13718v2**：[当前精确v2](https://arxiv.org/html/2602.13718v2)完整题摘、§III–V/TableI–IV实际读。同MeanFlow checkpoint通过r=t diagonal额外instantaneous field训练与fullinterval平均场共用网络；global jump→ReNoise `alpha*eta+(1-alpha)*coarse`→local diagonal velocity不新增模型。RoboMimic同checkpoint每任务100episode，plain1/2/4/16NFE为78/78/72/60，noRN24、2stepReflow58、ReflowRN82、ours95/95.5；不是单纯多步更好。attenuation(1-alpha)不证明re-noise分布等于training marginal；fixedinterval传播界不是NFE指数定理。real Thor同300demo/encoder/controller/backbone，PPID69/80、EP53/80，CT43/63对照0；WM182/300是得分不是Bernoulli。19ms在action features ready后，排除95ms视觉camera，不是8x整loop；Transport82低于STEP86/DDIM88，不能全任务优胜。拟重要revision、深入完成，Ch24组合正则器后新增受限global/local flow sampling分支，待非作者/窄锁，不重复评分family。

### 其余具名重要revision已实际必要源读到停止

- [2606.08151v4](https://arxiv.org/html/2606.08151v4)§3/5 Tables3–7：50 SWE-Bench file instance，BM25top50→Qwen3.6rerank，Hit@1 .78vs.58、MRR .790vs.634，但R@10 .714vs.716，修正不是recall提升；模拟utility、parseable和小样本RepoBench不证明patch success。应保留重要纠错、仅报告/现有Ch76具体覆盖判断，不能无声排除。
- [2608.28021v2](https://arxiv.org/html/2608.28021v2)§III-E/F、IV-B TableII、limits：prescriptive分类52insecure/33secure/15functional，与独立49/41/10仅75%一致；999 size matched pool的3.50x对比仍非prompt-matched任务归因，functional类密度仍高于human，幅度/分层解释对分类敏感，非方向反转。响应执行unsafe指令不等于模型默认偏好，须保留prompt-class correction影响，不写通用安全结论。
- [2601.15322v3](https://arxiv.org/html/2601.15322v3)§1/3.1–3.4与表/结论：v3 intended arguments评价不等于v2实际names-only；binary faithfulness fixture非grounding；portfolio fixture被排除，21config4705run的r=-.11仍混旧fixture，不能推“过程与结果独立”。需报告纠错和版本层，不用整合未经匹配的相关性结论。
- [2606.22419v3](https://arxiv.org/html/2606.22419v3)§5当前probe：engine1.8.0 Sep15先修LIMIT pushdown、optional/multiple type(r)、comma CREATE孤点；Sep21验证degree20k1.1ms与1k1.3ms及null/create正确。算法/实验未变，但旧workaround不再是当前必需；版本验证重要性限定，不把Sep15 fix本身首次归本窗。
- [2603.16859v3](https://arxiv.org/pdf/2603.16859v3)23页PDF通过web实际读pp1–9/§§3–4.4/Tables2–5。prefix-boundedquery不是实际stream latency；128gold-positive条件下Cov=Rm/128、Quality只TP nonempty、Joint乘积使漏回答0但FP仍另由when precision惩罚。GPT4o cond76.5 Cov30.47 Joint23.31 vsVita49.93/88.28/44.08是不同coverage质量权衡，不是通用榜。cascade visual-only也非native omni等硬件；三固定judge留一family rank shift≤1，individual rank shift最多5/pair MAE17–28，不能消除偏置；shuffled-reference AUC只是有限construct检查。必要证据已可得，curl局部PDF不完整不使用、不写外部材料受阻；Ch66 reach/coverage/conditional quality链已有具体覆盖，待终审确认。

轻量元数据终止：15795v2官方Comments明示title typo且manuscript unchanged；09646v2仅AgentX参考ID/DOI/URL更正且results unchanged，不是重要机制，候选前关闭不评分。12748v2官方摘要确为撤回传播因果解释非论文withdrawn，history Fri18 10:22UTC不能单独锁replacement公开；目标Tue22恢复未命中，有限archive入口已尝试后日期隔离，不用其支持本日候选或Book。只接受官方公告archive/可靠公开范围后恢复归属和必要纠错，不扩周/月。

### OpenAI本窗漏项局部纠正

本輪实际获取[官方News RSS](https://openai.com/news/rss.xml)，1238项仅作时间过滤入口而非全年审阅队列。逐项解析原`pubDate`，以UTC `[2026-09-21T01:00:00Z,2026-09-22T01:00:00Z)`过滤得到以下5条，已纠正旧09/23机构记录漏项；旧零命中判断不再复用。

- [Priorities and principles for effective third party assessments](https://openai.com/index/priorities-principles-third-party-assessments/)：`Tue, 22 Sep 2026 00:00:00 GMT`→09/22 08BJT。核心§Priority areas/Principles/Road ahead完整实读：提出预注册claim范围、比例grey-box access、独立性/利益冲突、editorial independence与redaction、launch-agnostic长期检查；并明确非单次launch批准、没有单一第三方能覆盖全部风险。未给新的可执行检测/评估机制、阈值、比较协议或实证结果；这是对既有评估原则的机构治理提案，贡献前关闭、不评分，不把访问承诺或原则当作已实现安全保证。具安全信号，交root风险negative有限校准。
- [Building standards for the next phase of AI](https://openai.com/index/building-standards-next-phase-ai/)：`Mon, 21 Sep 2026 10:00:00 GMT`→09/21 18BJT。完整核心§RSI/International standards/两建议/US lead实际读：倡议国际公共机构协作、共同测量/事件汇报和human review标准，仍是拟议方向，正文明确不是许可或mandatory prerelease approval；没有新公布的可执行标准、测量阈值或实现证据。贡献前关闭，不将所链接早期研究当作本窗新机制。
- [Higgsfield AI ships new video features in a day with GPT-6 Astra](https://openai.com/index/higgsfield-from-prompt-to-production-with-astra/)：`Mon, 21 Sep 2026 12:00:00 GMT`→09/21 20BJT。核心两节完整读：客户对广告变体生成/一工程师一天发功能的声明，归因长任务规划及协作，但未披露新的模型/Agent机制、可比基线、执行配置或测量协议。应用与效率故事不足以改变系统设计选择，贡献前关闭不评分。
- [Advisory Group on Mathematics and Artificial Intelligence](https://openai.com/index/advisory-group-on-mathematics-and-ai)：同`Mon, 21 Sep 2026 12:00:00 GMT`→20BJT；标题明确数学研究咨询计划，当前AI for Science暂缓，不作为系统候选。
- [Expanding OpenAI Academy with new learning paths](https://openai.com/index/expanding-openai-academy-with-new-learning-paths)：`Mon, 21 Sep 2026 07:00:00 GMT`→15BJT；标题明确教育学习入口发布，非模型/系统机制，贡献前关闭。

本轮另按root定点请求完成June9的非作者Books写后：FuseFSS Ch72两段和BUDDY Ch49 early-exit之后两段实际文字及前后衔接均通过，已回报root；仅核指定正文，不重开日期或重复全篇原文，也不计为本日候选。

### 四个新增分支实际写入

sep21非作者必要源/actual owner核均通过，root批准四窄锁。本轮实写22547 Ch66:1403–1405、23570 Ch77:1150–1152、13718v2 Ch24:357–359、MiMo Ch78:88–90，均为两段机制/边界，唯一SF，scoped diffcheck通过；已交sep21核实际文字与前后衔接，未把必要源核当实际写后。23570纠正42%为memory-off已4/4成功的pairing比例，strip/random不证明唯一instruction pollution原因。当前42实际整合/8已有覆盖/2仅报告/1争议=53，最终冻结与日级复核尚待具名修订及四项写后完成。

root定点请求的June9 Rosetta Ch77:329–331、CAR Ch69:201–203、Aliyun Ch33:1101–1103两段及前后衔接实际写后PASS已回报root；Rosetta已纠正source writer/target reader角色，CAR保same-policy null与total-not-direct，Aliyun保resource precondition与任务outcome分责；轨迹/清理receipt→admission属于工程建议，不当作者已实现系统。仅限定非作者支持，不改June文件、不扩大本日分母。

四处新增实际write-after均获sep21 PASS。按独立反馈实际修正22547“实测截断率/假定概率修复敏感性反事实”、23570“四seed平均outcome在候选memory combinations择最佳”而非挑seed、HybridFlow“默认初始噪声或fresh variant”边界；MiMo实际两段无须修改。28021v2 TableII functional两类密度均>human，已纠正Report/本笔记原“方向相反”为“幅度与分类解释敏感，非方向反转”，Only裁决PASS。22419v3风险negative必要§5及日期/版本语义获sep21 PASS；08151/15322长期命题由具体owner承载，保留E，但版本事实仅报告，不新增Books；16859 E和MPS深入Only有限核亦已通过。

日级分层抽核局部重开22109共享LR非中性、22101 extreme-value margin、22098 parent-conditioned tree survival/without-replacement residual、22135 probe-best≠steer-best四条具体排除理由，sep21正在准入/actual owner校准，不自动计入候选、不扩大1746发现范围。旧§7.7“除22419无已采用正文”已被实际定点命中12748 Ch84:925–927纠正：既有段只承载共同substrate/波次不证明传播、缺read log不能推消费、缺outcome不能推效用，符合v2撤回因果解释，保留其有效合同而非新增v2正面采用。v2日期Hold不变；request≠delivery/causal use，收到官方replacement archive后定点重开。当前普通工作为四条局部筛选校准及最终日Gate，不再是已完成的具名revision/四项写后。

## 有限七项重开：必要源 → actual owner（09/30恢复）

上述过程停点现由非作者[日Gate §4](V3_SEP21_DAILY_GATE_20260922.md)覆盖：同一19具名分层样本局部重开七条，23551/22100/22091亦已具体准入；不是新增发现扫描，不因成本降分或删除。原53有效结果保留；最终候选尚未冻结。以下是作者必要证据，不是独立通过或写锁。

### R22098 TreeSpark — INFER-SPECULATIVE-DECODING

[exact-v1](https://arxiv.org/html/2609.22098v1)完整题摘、§3.1–3.5/Proposition1、§4/Algorithm2、§5.1–5.5与§6实际读。一个block backbone加parent-specific低秩Markov项；树边的接受率须拟合在ancestors-accepted条件人口，all-edges混入不可到达父节点，在held-out该人口ECE .059→.0105。路径乘积是预算估计，不是把独立事件假设当定理。采样兄弟必须依次从排除先前样本的q重归一化抽取，target按相同抽取顺序执行min(1,p/q)与正部残余；slot在看见抽样token前决定接纳，不允许按token值删改/重排，才满足其lossless命题。deterministic top-k反例TV .46，对比真抽样.047/target有限抽样.066；不是任意树验证都exact。

固定预算/温度/模型对照区分parent条件头和校准，Qwen3-4/8/14B、block7、BF16/SDPA、H200三次matched target-only（KV缓存）；A100 recompute双方cache-free，不混两种AR。§4 A10040GB、4B、512prefix成本模型与churn simulation分开；simulation排drafter和prefill，不当生产goodput。same-GPU交错A/B的bs16 sampled树慢于chain，fallback选代码相同chain；校准随modelpair/hardware更换，greedy训练标签到sampling拒绝率仍有未隔离mismatch。得分6=2+2+2，确认长期gap故深入。actual Ch48:220–238仅一般prefix-survival/容量，700–712仅一般残余整形，缺上述条件人口+树draw-order合同。拟在“Verify Length”既有profile/旧block尾部限制之后、37532 binding之前窄两段，保留chain/no-spec fallback；等sep21 source→owner与root锁。

### R22101 Context Poisoning — MODEL-LONG-CONTEXT

[exact-v1](https://arxiv.org/html/2609.22101v1)完整题摘、§3定理/命题、AppendixA证明、C/D及F完整关键设置/表14–15/限制实际读。定理只在单decisive evidence logit≤γ、iid Gaussian distractor varianceσ²、固定softmax温度τ、attention mass低于ρ时decoder正确率≤a0的faithful条件下，有accuracy上界 a0+(1−a0)Φ((γ+τlog((1−ρ)/ρ))/σ)^N；在该抽象内要容许固定高accuracy，γ需Ω(σ√logN)。N是有效tail-competitive干扰项，非raw token数；真实模型的Gaussian/独立性诊断不成立，通用无关filler的Llama有限测试100%正确，不能宣称长窗口必败。gate命题仍是上界而非改善保证。

F固定100QA×7长度、GPT4.1-2025-04-14、T0/top1/max64、BM25 dev选K、proxy tokenizer，同prompt/order/一次生成，不加quote阶段。512K固定K16 recall .79、EM .59vsraw.57，paired CI[-.06,+.10]；扩K192 recall .93、EM.64、Δ.07 CI[0,.14]/McNemar .092，仍有限/边缘，不能普遍显著。检索hit子集改善不是整体收益。Ch22:109已有linear/isotropic-Gaussian associative top1 vsTAM的读取合同，非softmax faithful-decoder定理，缺effective distractor与recall-miss抵消干扰收益。拟其后、容量测试总结前窄两段，理论假设和gate反例同正文；6=2+1+3，因长期gap深入；等peer/窄锁。

### R22109 Shared Learning Rate — TRAIN-RLHF

[exact-v1](https://arxiv.org/html/2609.22109v1)完整题摘、§2–6、Scope与AppendixA/B实际读。Qwen2.5 1.5B/7B GSM8K、LoRA32、AdamW/clip1、top5%/512rollouts×3轮1536steps、4090下arm×4rate区别dense/selective对rate反应；raw梯度相差15.5倍不代表实际更新，归一化parameter displacement在已测LoRA仅2.2%差，不能外推所有权重/optimizer state。frozen是冻结scoring modelθ0，不是冻结每轮token集合；rollout仍来自当前student，仅切直接评分反馈，不切所有on-policy依赖。TV n12两rate interaction3.79pp CI[.29,7.30]，不是所有selector相同；entropy不复现，MATH小样本不复现不等于零效应。FullFT fp32master/A80080GB更大rate依赖，但无frozen对照且hardware baseline不同；不拼成同条件机制证明。

endpoint n3 Random的5.4pp p.097、Full的1.8pp p.26均不称确定差异/等价；rank没有全逆转，posthoc uncorrected统计描述。arm×rate不是已完成公平per-arm tuning（缺独立tuningholdout和匹配搜索预算）；rescoring频率观察unpaired也不作因果。Ch31:718–743一般policy/反馈、941–945既有prefix兼容及LR预算匹配，未承载“同一数值LR不保证比较中性”的闭环selector诊断。拟22600 token-position段之后、23740轨迹段前两段；6=3+1+2，因纠正设计控制且长期gap深入；等peer/窄锁。

### R22135 Read-Best — MULTIMODAL-REPRESENTATION

[exact-v1](https://arxiv.org/html/2609.22135v1)完整题摘、§III/§V/VI/VIII actual读。source whitening/linearprobe和raw target-neutral centroid→去top2PC→unit direction不同；注入α||h_layer||v，paired相同norm/random方向、5seed layer扫图区分读出准确率和干预效力，不能把probe最大层当最佳控制层。三模型Qwen2.5Omni7B/Phi4Multimodal3.8B/MiniCPMo4.5峰gap7/10/9，但r .45/.55/.36不满足预注册r<.30，采用gap≥5条件；不用“低相关”偷换成功标准。logit-lens H1失败，Hthreshold解释MiniCPM失败，非统一因果理论。

干预主要输出文本，T.7/top-p.9/max80；text30/audio100/image102，GPT5.5 judge text150校正仍非human真值。joy在Qwen/Phi显著但MiniCPM多层mapped注入Δ.022 CI[-.064,.122]；anger跨judge弱，不普遍跨模态可控、不外推70B/语言。hardware/precision Not Disclosed；成本是层扫/方向校准/额外judge与offmanifold/OOD监测，未测serving收益。Ch23:743–749一般跨分支matched干预与probe≠语义，不承载within-model read-best/steer-best层选择差额。拟26411 marker之后、30210几何指标分支之前窄两段；5=2+1+2，确认长期gap深入；等peer/窄锁。

### R23551 Paragraph Boundaries — MODEL-POSITION-ENCODING

[exact-v1](https://arxiv.org/html/2609.23551v1)完整题摘、§3.1–3.4、§4.3、§5.1–5.3、§7与AppendixB.2/C实际读。paragraph/sentence/token三坐标各占RoPE channel，p1-only fake merge/split保持token序列和其距离不变；rand_axial同架构/频段/训练预算/密度，random标签每训练step重采样。仅线性距离residualization不足排除非线性混杂，核心估计在每个精确token distance内对比paragraph位移，再pair-count加权，≥2000pairs/cell，旧distance bins足以翻转WikiText符号不能继承。random轴亦compression，因此“有压缩”不证明真层级；Code/Wiki的real-minus-random depth CI排0，但OpenWebText[-.059,+.093]不排0，不称3corpus全胜。depth不等于可稳定识别minimum位置，更不是Riemannian度量或已识别内容机制。

8层/8头/d512/context1024、batch16、AdamW、5000step/三seed，hardware/dtype Not Disclosed。document-cluster bootstrap2000只刻画固定corpus内抽样，跨3corpus顺序描述性；flat相比hrope在Wiki/OWT有小validation-loss成本，n3方向证据最低sign p=.125，未测下游/serving。Ch13:145–175现RoPE单轴相对距离，177–182连续二维坐标身份，没有文本相同token但层级坐标不同及matched-random反证。拟RoPE极简例之后、连续二维小节前两段“reading-order坐标不唯一决定结构→固定token/精确距离+random轴验收”，不承诺推荐hRoPE或大模型增益。5=2+1+2，长期gap深入；待peer/窄锁。

### R22100 AdaMem — AGENT-RAG

[exact-v1](https://arxiv.org/html/2609.22100v1)完整题摘、Method全段、Experiments关键配置/表1/消融、AppendixA/B/C/D实际读。同query-passage forward得到固定candidate <MEM> bank与<RERANK>分数，pool标准化后a=Bsoftmax(score/τ)，largest-remainder保整数总预算B，m=0省略，取每篇前m个state再project给decoder；不是在线预算增加，也非单纯shared encoder。score detach使allocator不可直接由answer梯度训练，rank MSE teacher和generation .1mix共同训练；连续分配只对假定log utility最优，reversewaterfill是高温一阶近似，nearest整数rounding不证明真实answerutility最优。固定bank生成发生在allocation之前，不能称compressor计算随m成比例下降。

Llama3.2-1B compressor/Mistral7B decoderLoRA64，128token/querypassage截断、25retrieved；196916训练经goldalias+teacher目标过滤，eval六集不筛（4×2000+948+1609）。OSCAR同queryconditioning/训练data-hyperparameter-stage与预算，差额allocation；其他baseline不同压缩率不合并。BF16/FA2，eval分8A10080GB，latency单A100。Table4同16x192.4ms/56.4GB vsOSCAR156.1ms/39.6GB，64x152.9/44.4 vs142.9/38.7；更贵的candidatebank是明确反证。Table1 substringmatch可奖励列举/unsupported答案，judge非truth，bootstrap SD非trainingseed不确定性；不宣称4x通用同质量。Ch76:593–648一般controller/retain-compress-bypass缺固定budget passage allocation/候选bank成本。拟controller末后、Iterative Stop小节前两段，保uniform/raw/bypass与source指针可回取为工程推断，不把compressedstate当support authority。6=2+2+2，长期gap深入；等peer/窄锁。

### R22091 Prospective Term — AGENT-MEMORY

[exact-v1](https://arxiv.org/html/2609.22091v1)完整题摘、§3/3.1、§4.1–4.3、§5/6实际读。explicit dated/condition ledger保action/触发/链接，resolved记录而不删；offline链接在query时由日期/condition matcher判断open且fire，给linkedrecord乘cos×(1+Wb)，b∈{0,1}，其他四salience分量实验关闭。no query LLM不等于零计算/零维护；乘法使cos0仍0、负cos不一定升分，不能把“relevance sovereign”写成任意rank/安全定理。小W有救不回深埋条目的ceiling，floor或大W可改rank同时改变tradeoff；salience是rank，不是删除或执行权限。

singleuser curated markdown+bge-micro-v2/384dimension，48LLM-authored blindblueprints/175tasks（pilot5另列），hard22positives来自11blueprints，easy74、resolved53；oracleledger使这是完美抽取上界，抽取层尚未构建。primaryhard/easy相对gate在发现absolutegate问题后posthoc换，LLM措辞/embedder可能相关，6例单reviewer自然性抽核非human真值。hardR5 .955、negativefalseboost0仅该集合；heldoutparaphrase13/16fires→hardR5 .818；不能把17–29%定义下比例当用户真实base rate。误ledger和missedtrigger回普通similarity，真实resolved检测未由oracle实验证明；禁止把retrieval提示当外部action授权。Ch77:193–210介入controller和215后cue关联未承载dated+resolved explicitledger离线链接/零LLM arithmetic rank；15405仅tailtrace不算正文覆盖。拟主动干预小节末、预算关联回忆前两段，工程生命周期/来源/权限沿已有owner，不主张作者已实现生产抽取。5=2+1+2，具体长期gap深入；待peer/窄锁。

七项必要证据现均已读到拟采用命题的支持/关键反证停止点，拟具体I须经非作者源→owner及root窄锁才写；尚未有七项源PASS/实际写后。最终分母须包含真实准入而不取决于写书数量。

**七项执行更新**：sep21 source→owner通过22098/22101后，root授权指定两段窄锁，actual Ch48:243/245、Ch22:111/113已写，sep21实际文字及前后衔接写后PASS；只采用其上述受限机制，不承诺生产或普遍正确性。22109/22135 necessary source→actual owner也已PASS，已向root申请22600后/26411后两段锁；22135禁把26x多层vs单层对照当纯层位置收益，仅按单层扫描论证。23551/22100/22091源→owner仍普通peer待办；不重复53有效结果。README当前准入60（7本窗官方身份可核）、尚未冻结、普通待办不归外部阻塞；机械格式修正后校验PASS，不代替日Gate。

**最终闭环（10/01，覆盖以上过程停点）**：七项必要源→actual owner及实际两段写后全部sep21 PASS。root授权余5指定两段窄锁已按当前文件落实：22109 Ch31:945/947（22600后/23740前）、22135 Ch23:753/755（26411后/30210前）、23551 Ch13:176/178（RoPE例后/连续2D前）、22100 Ch76:649/651（controller末/Iterative Stop前）、22091 Ch77:212/214（主动controller末/关联回忆前）。每项unique SF marker为1，scoped diffcheck通过，未更改其他日期既有段；Ada bank cap的可行性验收明确是工程要求而非作者连续proof。sep21实际文字与前后衔接逐项通过，首2实际PASS与原53有效结果保留；所有七条误漏普通工作已闭合。Report六部分已同步并冻结最终60家族：54深入/5标准/1争议，49实际I/8E/2Only/1D。sep21已直接核最终变化包、分母与全部普通0，独立Gate最终通过（见其最后一节），不重审未变53；正式日报同步完成及§6后复跑机械。没有新增发现或另造平行账本，隔离DateHold/来源局限/中心争议维持原重开条件，不支撑正面采用或无遗漏；未stage/commit/push。
