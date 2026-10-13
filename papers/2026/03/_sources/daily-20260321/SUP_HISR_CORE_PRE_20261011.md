# HISR18683：必要 Source / actual sole owner / 最小 PRE

准备者resume_mar18，仅本03-21补BJT03-20自然日。精确[2603.18683v1](https://arxiv.org/html/2603.18683v1)；完整题摘/准入和官方日级夹证复用SUP_FIRST_ADMISSION。Submitted ACL2026 Jan5是投稿，不是同稿已公开证明；不追全venue或旧版。拟2+2+2=6，给segment outcome拟合→future-conditioned重权→当前policy更新的具体训练接口，而非旧segment或teacher幅度原则新分。未非准备者PASS/锁/Books/safe/DAY。

## 必要实际 Source 及关键反侧

实际§3.1–3.3/Eqs1–9、§4.1–4.6/Tables1–2、Limitations与A/B/C必要配置已读；支持和直接反侧足够即停，不遍全部cases/prompts/附件。成功expert轨迹SFT只对thought/action计算loss，reference每task10rollouts并过滤错格式/重复；GPT4o按subgoal对连续turns分段。参考模型末segment hidden接2层SiLU MLP，以(sum r_i−terminal R)^2训练；只有sum约束不能识别唯一segment贡献，任意两段加c减c仍同loss，不授因果或真实progress。

Hindsight模型用完整已发生trajectory的observations及前/后actions重建当前action，policy只读当前prefix可见信息。Eq5–6用两密度之比的长度归一log均值再exp，beta.3；段内将各turn ratio相加，乘SPRM分数后归一；Eq8再加grounding executable0/1，PPO/GAE消费。Ratio>1只能说明未来条件下更易预测，不证明action推动成功：未来描述重复该action、或错误动作让失败观察可预测，也可提高分数。段内sum会偏向更多turns，不因actiontoken长度归一而消除segment长度偏好；SPRM未有非负约束、Eq7未披露norm类型或zero-vector guard及segment→turn/token exact分配，不照抄为bounded recipe。Table2 r=(.069,.118,.132,.681)、z=(.127,.392,.286,.195)，L1归一乘积≈(.03885,.20506,.16737,.58872)与表him相符，但不能据此自动把正文未指定norm当完整实现已核。训练未来可见不意味着部署actor可读取未来；两个模型的可见信息/冻结版本必须分账。只采用这个有限调制接口，不授中心“accurately reflects how each segment propels outcome”。

必要配置：Llama3.2-3B-Instruct、8H20/vLLM/fastchat。三dataset SFT3epochs/batch32,24,32各LR；collect温度.7，后SPRM/hindsight各1epoch，LoRAr8 PPO、KL.01/gamma.99/lambda.95、critic1e−4/policy1e−5；测试T0。Table3 ALFWorld2851/134、Virtual4920/247、Web1938/200，maxturn40/40/10，Web0–1属性price匹配是softscore而非二元全任务success。GPT4o不分段Web89.3%、ALF11.5%、Virtual16.9；Web本法即w/oSPR，不能以其证明segment优于turn。SR精度/最大token、总PPO更新/生成预算、完整batch/concurrency、seed/CI、端到端GPU-time或SLO未披露；SPRM/hindsight训练、10rollouts、GPT分段、双模型评分、critic/环境及独立测试均付费，不是无标注/无teacher费用。

Table1直接反侧：ALF PICK83.3<SPA95.8/w/oHIM87.5；HEAT65.2<SPA87、w/oHIM78.3、w/oSPR78.3、w/oAGS78.3，HIM或分段不是各类单调提升。Web69.1=w/oSPR，w/oHIM63.7=w/oBOTH63.7不授互独单项充分性；平均83.6/59.1/69.1仅所测人口。C明确PE/SFT/RFT和多数RL baselines来自既有论文，DPO代码重跑，但未全same-budget实现；不能把所有收益唯一归调制或发布“全对照公平”。Limitations承认hindsight frozen→policy变化失配、SPRM后段强prior未完全纠正；segment比例和分数变化只是模型归因，不是独立因果评价。必要访问完整，无真实external blocker，不因这些反侧EX/降分/假NC。

## actual sole owner / 具体差额

TRAIN-GRPO/[Ch33](../../../../../books/part-04-training-system/33-grpo.md)。实际完整784–812 privilegedteacher/reset与832–860 segment→value→continuation credit；前后31/32/34开篇及Ch32 ratio交接已读。现已有teacher正乘子不翻outcome sign、语义segment和恢复前/后continuation估计，但没有**仅terminal-sum训练SPRM，再用未来可见的hindsight/current density ratio按turn聚合调制segment奖励**。这不同于已授因果的continuation分支，不能假NC或以PPO名字新分；Ch32继续拥有GAE/PPO优化公式，本章只拥有信用来源/边界。拟在Ch33现844原segment机制/成本之后、846“前述milestone分支…”之前一段＋自身静态源注，不改任何旧family。

## 一段逐字 PRE（未写）

Segment reward 还可以先由终局总分拟合，再用已经发生的未来信息调节，而不执行新的 continuation 对照。一条[受限训练分支](https://arxiv.org/html/2603.18683v1)让分段器按 subgoal 冻结连续 turns，以各段分数之和拟合 episode outcome；另训练 hindsight 模型，在完整轨迹中重建当前 action，再将它与只读当前 prefix 的 policy 的长度归一 likelihood ratio 聚合到段内，重权原分数后交给优化器。这提供更密的信用代理，不识别唯一贡献：总分拟合存在多种分解，未来条件更易预测某动作也不证明该动作导致成功，段内相加还可能偏爱更多 turns。Actor 的部署可见信息不能借用 hindsight 的未来权限，分段、两个模型的版本、权重和归一化须随训练目标保存；动作可执行性与最终成功另行验收，不能由调制分数自签。局部任务与去模块对照有反退，冻结 hindsight 也会随 policy 改变失配；分段器、轨迹收集、额外模型训练/评分、critic 与环境交互都付费。代理或恢复边界不可靠时，保留原 terminal reward、可信 milestone 与已验证的 continuation 分支，不由“知道后来发生什么”宣称因果 credit 或普遍更稳。<!-- source-family:SF-2026-ARXIV-2603-18683 -->

## 静态源注 PRE（未写）

- `SF-2026-ARXIV-2603-18683` — [HISR exact-v1](https://arxiv.org/html/2603.18683v1)必要§3/Eqs1–9、§4/Tables1–2、Limitations与A/B/C配置/对照；仅采用terminal-sum segment拟合与future-conditioned/prefix-only两密度调制的训练分责。sum不识别贡献、ratio非因果/段长偏好、norm/zero guard未闭合、Web等价turn、任务反退与冻结失配保留；不授准确credit、普遍稳定/全费公平或部署未来信息，未核实现/复现。

## root 非准备者必要 Source / owner / PRE 复核

实际精确v1§3.1–3.3/Eqs1–9、Table1/2、§4.4–4.6、Limitations及A/B/C必要配置与对照；实际 Ch33完整828–872的segment/value、milestone与continuation论证，Ch32/34交接复用本轮已读。总分loss不能识别唯一分解，Eq5–7未来密度并非因果贡献、sum turn仍有长度偏好，Web本法等w/oSPR与HEAT65.2低于多个对照均已实际回证；冻结失配与外部baseline费用限定充分。sole TRAIN-GRPO只接信用信号来源，PPO优化仍归Ch32，不复制新算法或授未来部署权限。原6分不变，有限 Source/PRE 通过，可写原一段及自身静态注，未授 POST/DAY。

## 获锁后的实际窄写（待非writer POST）

作者按root唯一Ch33窄锁落实原一段与静态源注；新正文846、自身注3206。实际顺读完整834–864（segment/value→hindsight有限代理→milestone→continuation）及尾七行本人/邻注，逐字回有效原PRE与必要Source一致；marker/注各唯一，限定diffcheck空。未改其他family，未授未来部署信息、因果credit或完整更新recipe；仍待root一次非writer actualPOST，不先计安全整合或DAY。

## root 实际非 writer POST

实际顺读 Ch33完整834–864和末七行本人源注，回对有效原 PRE/Source：segment/value信用与仅总分拟合的hindsight代理有明确分责，接回milestone及真实continuation对照不混作因果证明。不可识别分解、未来权限、段长偏好、反退、冻结失配、全费用与旧信号退路近文完整；正文与静态注各唯一，限定diffcheck空。actualPOST通过，释放该 Ch33 锁，可同步整合；本日来源/筛选余项和最终 DAY 尚未授予。
