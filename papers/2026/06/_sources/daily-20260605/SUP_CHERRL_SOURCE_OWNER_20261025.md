# 04923 CHERRL：必要Source / actual owner / 最小两段PRE

作者supp_20260605_author，2026-10-25，同一Daily2026-06-05补Jun04。准入/联合日证采用本日R33–36有效层，不第三AB/date。精确[2606.04923v1](https://arxiv.org/html/2606.04923v1)，官方HTML原件`SUP_2606.04923v1_20261025.html`419571bytes，实际读§2–4/Eq1–7/T1–6、Limitations、A.1–3/B.1–8及F必要支持/反侧；不借未来稿、不扩全部agent traces/search-budget附件/仓库，不运行训练或复现。

## 评分与必要证据

首次2+2+2=6；具体已定位reward truth/onset与offline-online接口缺口而深入受影响域。增量为：真实rubric reward的bias与质量纠缠→固定基准judge、注入已知bonus并形成可复核threshold reference，另向detector隐藏原分解→分别审计“能发现何种捷径、所报起点是什么、是否可当线上质量报警”，不以proxy上涨自签学习有效。医学数据只作通用RL judge实验负载，不采用医学知识/临床结论。

- §2.1–2.2 Eq1–2：J_biased=J_unbiased+α·bonus，实验α0.5，bonus为目标bias二值判据。所谓unbiased/gold仍是常规LLM judge的rubric score，不是人类真值；两judge同Qwen3.5-27B backbone，仅分工不同，不能把“same foundation”说成独立无偏评价。known injection使增量可控，不消除基准原有偏差。
- §2.3 Eq3–5和A.1：G为全部rollout的两score均值差；M只在score≥0.99的高分bucket测已知shortcut，样本至少20，否则undefined并从平滑排除。五checkpoint居中窗含t+1/t+2，端点截断；3个gap阈值0.08/0.10/0.12×4个M阈值15/20/25/30共12对，首次双越阈为candidate；canonical取众数、并列取早，interval取12candidate最早/最晚。这是阈值敏感区间，不是抽样置信区间、真实首次出现或在线检测延迟。
- 操作性差额：按Eq2，G本身等于0.5乘bonus频率；G+M共同上升不独立证明gold下降。Eq1附近reward hacking叙述还需真实质量停滞/下降，而Eq5 operational reference不含这一条件。故采用其可复核参照和局部质量对照，不把起点阈值升级成普适hacking真值。
- A.2–3：六个reference runs，VerInstruct format区间301–443宽142步；两作者各自标注、第三作者裁决，固定seed抽高分人口并隐藏step/reward/region等，仍是内部sanity check而非独立外部真值。T10多项pre-onset已有shortcut，HealthBench lexical的三个区间weak cue均常见，不能声称标记首次出现；正文“precise ground-truth”须收窄。
- §2.4–2.5/T3–4：policy Qwen3-4B经GRPO，HealthBench与VerInstruct各四bias，八settings六出现hacking；VerInstruct tone/HealthBench format未出现，不推出永不出现。相对无bias训练的局部domain指标下降，但若与base比较，有项仍更高；Arena-Hard部分不降也不是已证实evaluator被欺骗因果。保具体对照，不授全部能力普降。
- §3.1 first60step无既定reference onset，用gold>0.5定义T与shortcut B算OR；OR和后续canonical onset在六run相关，不是操纵entanglement所得因果定律。§3.2 T5每bias300试验，format按指令生成成功66% vslexical100%，支持所测模型pattern difficulty差异，不单独隔离后续放大速度唯一因果。
- §4/B.1–7：detector只见sanitized mirror的step/input/output/normalized proxy score及rubric，隐藏J_unbiased、bonus、reference/shortcut detector等；RHDA工具跨checkpoint提出/验证假设、粗到细缩小区间，输出typed alert(onset_step,evidence[],onset_basis)。输入受限不认证其输出正确或可自动改reward/停训练。
- B.3明确主实验temperature0、offline retrospective、unlimited tool budget。B.6 normalized score除以整个run的max(1,maxabsrawscore)，含未来全程scale；不能把这套离线接口原样认证为causal online。要在线使用需另定过去可用归一化、只读已到达checkpoint、成本与延迟合同，这是工程推断/未实证，不补作者已实现。
- T6 RHDA与CC-Qwen同Qwen3.5-plus/backend和mirror，但工具/协议、假设state、typed alert等一并不同，不能单归某个机制。CoT仅16均匀step×3example，无score/自适应工具，与RHDA并非等信息量/等预算。其遗漏3个HealthBench单列，已检测误差和miss不能混成全人口误差。
- 关键B.3宣称重复试验固定均值聚合，与B.4/B.8“finalized representative runs/predictions rather than a single universal aggregation rule”口径有差额；本次保原双方，不补一条不存在的统一选择规则。因此不采用T6排名为稳定统计优越/公平等预算结论，不降分或删候选。可采用协议/条件参照，排名与总体miss率待逐replicate选择/未报警处理和预算披露才重开；此不阻塞本文可支持的有限测量边界。
- F：约2000 NVIDIA H100 GPU-hours为全论文训练/推理总预算、H100 80GB租用；不是单模型/单detector成本，闭源Qwen3.5-plus size未披露。精确训练batch/优化超参/生成长度/并发/在线尾延迟、完整replicate N/CI未在必要域充分披露，Not Disclosed，不声称生产收益。Limitations仅单4B policy与检测未实现fix；不能由检测器alert授修复已完成。

支持与直接关键反侧足够停止。未核可选代码、未复现；不为消灭代表性运行的统计不确定性读取所有无关trace。本次不采用排名/完整线上报警主张，所采测量机制及其边界不依赖可选实现。

## actual owner与最小差额

当前已实际读ROADMAP、三Books公共上下文、仅2026路由；Ch31 reward hacking完整组519–547、独立evaluation/stop完整组1172–1196与policy-relative state组，邻Ch30/32开头交接。唯一owner `TRAIN-RLHF` Ch31；不是Ch66再写通用评分、Ch33重写GRPO或Agent检测工具小百科。

实际已有覆盖：Ch31:532“所以reward上升必须与independent human evaluation、task verifier、安全评估和distribution slices同时解释”；1174–1180用外部EvalRun/patience提stop proposal、job owner提交/回退；policy-relative state与动态负判据已保judge共同失误/额外费用。故泛“reward不是truth、detector不授权、独立评价”不再新增。

尚未具体承载：有已知注入bias时，reference onset由baseline judge差额+高分人口shortcut+阈值网格构造，其语义不等真实首次/独立质量下降；offline居中平滑/全run scale和代表性运行不能冒在线报警。拟在上述532完整总结段后、534“即使把learned reward换成规则明确…”完整段前两段，支持边界近文。当前只是首次非writer必要Source/actual-owner/PRE准备，无新授权/SAVE/POST/I，可按具体覆盖作校准，不默认整合。

完整直接上锚：

所以 reward 上升必须与 independent human evaluation、task verifier、安全评估和 distribution slices 同时解释。

原两段PRE：

当真实judge的偏差和质量难分时，可先做有已知偏差的受控压力测试：固定基准rubric judge，再给指定行为加独立记录的bonus，分别保存基准分、代理分与高分输出里的捷径比例。用分差和捷径比例共同越过一组阈值定义参考起点，再报告阈值变化下的起点区间，能让监测器接受可复查的目标；但基准judge仍可错，分差还会随注入bonus频率机械变化，越阈不独立证明真实质量下降。这个区间是操作定义的敏感范围，不是首次出现、抽样置信区间或真实失控时刻。

[CHERRL的受限实验](https://arxiv.org/html/2606.04923v1)还把分解分数和参考标签对检测器隐藏，让它跨checkpoint核对行为并提出带证据的起点；但主实验是离线回看，居中平滑和全run归一化不能直接当线上早警接口。六个已发生捷径的run、内部作者审计、代表性预测选择口径，以及不同工具/分数可见性与搜索预算，均限制排名和漏报外推；早期偏差共现与参考起点、生成难度与后续放大分别对应不同观察，尚未隔离因果，不能合成一条‘更早发现必更快放大’的规律。双judge、轨迹保存、搜索和独立质量回归都付费；证据不足时保原冻结奖励/可信rubric与人工核验，由外部质量和训练owner决定是否停训或改奖，不让一个alert自签修复。<!-- source-family:SF-2026-ARXIV-2606-04923 -->

完整直接下锚：

即使把 learned reward 换成规则明确、始终未被修改的 task verifier，代理边界也没有消失。数学 checker 可能只检查终局答案，代码测试只执行被抽取的程序；它们并不因此拥有整段生成行为的安全判定权。攻击者若能污染训练 prompt，使“先产生不允许的内容、再给正确答案”获得正 reward，而拒答因没有答案获得负 reward，policy 就可能在不改变 checker 的情况下学会奖励这种组合。这里需要区分 **checked span 的任务正确性** 与 **完整输出的行为约束**，不能由前者为未检查的前缀、工具调用或副作用背书。<!-- source-family:SF-2026-ARXIV-2604-09748 -->

## 当前单篇ready

6分必要Source/actualowner/两段PRE ready，待本篇首次独核；无Books新授/SAVE/POST/I。前04425 R49–50已实际行政采用，当前既成新增I11＋旧Kimi合计12I。其余十篇必要层和有限相关官方标题stop/最终六节与DAY仍ordinary，不因等核扩大下一篇Methods；State/index/他日不碰，未stage/commit/push。

## 当前R51–52实际采用：唯一修句后真实SAVE待POST

上节是R51前准备历史。现已实际完整读回R51–52并采用其首次必要Source/六分/actual Ch31及限定PRE。第二段旧句只按R51替换成“早期偏差共现与参考起点、生成难度与后续放大分别对应不同观察，尚未隔离因果，不能合成一条‘更早发现必更快放大’的规律。”，其余原两段逐字不变，原准备误合两观察轴的措辞撤销，不变成新因果结论。

root本轮新窄授后，作者已真实保存修后两段于Ch31原532完整总结后/534完整checker前，加本人true-H2 Review notes下注。作者已实际完整自读新增两段、完整直接两侧及本人注；原09748marker保护，本family正文marker恰一处。去掉本两段与本人注后，整Ch31与写前快照`/tmp/jun05-cherrl.PVHSAE/ch31.md`字节相同，sha256 `ca53e8ccd4a9a0758592049b59f0d437b6da06b2dec9f4dd1f88c0e2dd00c274`，其他并发修改未动。

新增从独立质量原则引入可控偏差/参照语义，再回到checker覆盖范围；区间非首次/CI/真实质量、未来平滑/全run scale非在线、排名/选择口径未闭与全费/冻结reward人工外部owner回退近文保留，未授自动修复。当前只SAVE/selfread待唯一非writer actualPOST，既成仍新增I11＋旧Kimi合计12I，不预I/DAY。其余十篇/有限标题stop普通保持，先交本就绪写后层释放槽，不等全批或扩大Methods；无State/index/他日/stage/commit/push。

## 当前R53–54唯一actualPOST已采用

上节为R53前SAVE历史。现已实际读回R53–54，04923唯一非writer actualPOST通过/整合生效并释放窄位；累计新增I12＋旧Kimi合计13I。只行政同步README/本Source/本人注，不第三技术/Source/PRE/POST。其余十篇必要层和有限标题stop/最终DAY仍ordinary，未授DAY。
