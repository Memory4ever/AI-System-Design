# Jan14 KALE / MAESTRO 独立必要复核 delta8（2026-10-08）

复核者：review_jan15_delta（非作者）。仅 root 授权07430 /07208，未重开其他论文。压缩恢复后已重读 AGENTS、当前 Research / Report 合同、Prompt、ROADMAP、每日来源及本日路由/停点，Books 判断前重读项目背景/学习方法/写作指南与实际目标邻接。仍仅 BJT Jan13 完整自然日补充窗；保留原17、原窗口/分数。未改 Books、Report、LS、索引，未 stage / commit / push，不授 DAY。

## 身份 / 准入 / 必要原证

两项完整题摘均实际读本日 increment-abstracts-1/2/3/4/5-20261007.json 的对应行。07430新增KG与gold-answer共同构造训练rationale、以有/无rationale分布对齐的特权训练分支；07208新增completed-response context→逐response奖励强调→组优势训练另一个controller的结构链。两项均通过实际贡献准入，不从主题映射、成熟KL/GRPO或机构名称倒推。

两项独判均2+1+2=5。07430标准审阅；07208因确认具体长期差额，深入受影响的scalarization/credit/更新身份，而非扩整篇附件。原件分别 increment-necessary-core-2601.07430v1-20261008.json（§3–5/限制）、increment-necessary-core-2601.07208v1-20261008.json（§3–5/限制）。原必要字段中的附录observations不当原证；07208另实际读官方 exact-v1 C4–C5、E1–E4并保存 [必要附录原文](./increment-independent-delta8-maestro-appendix-20261008.json)。第一次标题定位notfound已由真实标题恢复，不作为材料缺失或通过证据。未核artifact/复现/完整理论。

复用本日已核正常公告/ID日期界定，结合 increment-date-bounds-rest-20261007.json 两行：07430 Updated Jan13 02:17:00Z → registered04:02:40Z，07208 02:04:37Z →03:57:24Z；均只归BJTJan13，不以Submitted或注册单证、不追公开秒数。独立轻读当前官方abs：07430 current v1；07208 current v2 / Apr12 / ACL2026 Main，页面未见具体撤回/纠错说明；不比较全版本、不由v2自动授重要修订。本次采用exact-v1。

## 07430 KALE — 5 / 具体 Existing PASS

原文§4训练rationale由question和gold-answer实体共同查KG并交GPT4o生成；§4.2没有rationale的p更新，带rationale的q固定为target，印刷目标为KL(p||q)。这支持特权context内化的有限实例，不认证生成rationale为truth。印刷xinp包含answer，后文却称only instruction/query，不能暗删answer后授完整训练/推理recipe；bounded BFS将不可达设∞所需的∞−∞条件未闭合，不采用A* admissibility证明或完整搜索实现。

§5采用6个7–32B模型、8QA、<32B的8A100与32B的16A100设置；主表与KI/KA移除对照支持该人口内局部结果，但分别改变监督内容与objective，不能授某原理唯一因果。known&incorrect由另一次fact-check操作定义，不证明模型真的拥有可调用latent truth；硬匹配、structuredQA/KG availability、KG搜索/GPT4o/teacher logits/训练与能力保留评价全费均保。

实际顺读 books/part-04-training-system/29-sft.md:478–551完整邻接。488特权teacher target需差分/verified acceptance；500–515有无context在同一prefix对齐、softtarget与KL方向/token reduction；517–538永久/周期冻结target、teacher identity与state/费用/行为验收，具体承载拟长期采用判断。这里只说采用链已覆盖，不说正文已有KALE A*、gold-answer路径或精确训练数据实现。无需新增正文/Book锁。

## 07208 MAESTRO — 5 / Ch31 单段最小 PRE PASS

§3与E1–E2明示读取完整prompt+完成response后的terminal hidden h；linear head产生categorical奖励强调动作，每response采自己的a/对应scalarization。§3.2缓存(h,a,A)，周期以组优势训练Conductor。E4给周期更新/temperature/minprob，C4–C5说明response reward与group归一化，但未完整说明每个a如何映射w(h,a)。本次仅采用角色/状态链，不照拼full recipe，不采用h是sufficient statistics、bi-level/Pareto最优、普遍防vanishing或counter-hacking保证。组均值中心化本身不证明score-weighted meta梯度为零；不同response不同criterion weights也会改变组内score可比性，不能假定仍是同一固定测量尺。

§4五reward channels、两个8B backbones、7bench与外部judge三次majority属于对应评价，不是事实truth或统计seed充分性。§5表示层对照OPUS first=last12.6，不能签terminal层普遍优胜或模型“self-perception”；异步/熵局部对照不证明所有时效稳定。Table2 ToMBench+6.7%、Web+4%、SS-GEN−20.1%是任务依赖时间，不签零开销。head/full-sequence readout、buffer/refresh、reward/probes/judge及actor训练费、channel偏差和有限8B适用域须近文保留。

Actual owner books/part-04-training-system/31-rlhf.md:197–280完整邻接已读：220–224按group历史调整权重，237–257按channel bottleneck及format对象聚合，259–272另为gradient-space controller。尚无同prompt每条completed-response终态→各自奖励强调→scalarized优势→另head及缓存更新的分支；不是用同义state/control词重写已有群体历史聚合。唯一owner为TRAIN-RLHF /Ch31，不在Ch33重复GRPO公式。

最小采用范围：在当前257的format分责之后、259的gradient-space标题之前加一短段，先保固定权重在criterion同尺度/优先级稳定时合理；再说明terminal response条件化聚合及另controller的实际输入/更新身份。把completed-response context、actor/controller revision、criterion normalization和buffer更新周期作为奖励测量身份；这是独立推导的工程约束，不冒称原文已有完整字段协议。近文保逐response尺子变化、proxy误设不能由adaptive weights修复、全费与回退固定权重/分项结果。不需要新标题、整套算法、理论或第二owner。仅 root 可授作者这单段及自身末注锁；实际写后须另POST，PRE不计actual integration。

## 停点

07430具体Existing终判可同步；07208结构级窄PRE已通知root协调锁，Books尚未写，本记录不授POST/正式整合或DAY。准备内容与机器通过不等整日验收；其他可执行工作由当日主流程路由。

### 07208 actual POST（后续，覆盖上段历史待写状态）

root授Ch31单段/自身注窄锁，作者实际写后，本复核者独立读正文259、完整248–282邻接及自身末注1374。实际结构为format对象分责→完成response条件化奖励→gradient-space controller，保留原有效段落/交接；固定权重共存、full-response非生成前控制、权重映射未闭合、跨response测量尺/proxy、全费/局部负侧和回退均在正文近邻。保存controller/channel/buffer/cadence明写为工程约束，未假托原文已提供完整协议；未采Pareto/vanishing/truth/hard-gate保证。自身注正确保精确v1及必要E/C原文、当前身份/日期界，待POST字段由作者据此同步。actual POST PASS，已通知root释放这项Ch31窄锁；现在可计1实际整合，不授DAY或实现核验。后续root另授07212/07224必要独判，独立处理。
