# AB10五项含糊事实：一次决定性core（待非作者准入校准）

固定本日窗口，不扩池。root对discovery完整题摘只提出五个含糊准入事实；本轮FETCH_AB10_ONCE于2026-10-05T21:25:10～12Z取得各exact-v1 abs/current Comments/HTML，实际题摘与下列决定位置已读。3窄IN5、1潜力/date hold、1成熟组合EX为作者拟判断，不记安全终态或Books，停止初筛补读；准入通过后才继续必要评价/owner，不默认审全文。HTML200仅是取得，不是全篇已读；没有运行artifact或复现。

## 22983 CC-BOS：保留窄受控安全/测量潜力，家族日期未授

[v1](https://arxiv.org/html/2602.22983v1) blocks21–41/77–97/168–190已读，未读无关攻击示例/全部search伪码。classical Chinese+已有策略维度+fruit-fly优化本身是成熟组合，不能只凭100%ASR准入。决定性增量是**同classical-language响应的翻译前后测量与output-defense比较**：Table6去翻译90 vs加翻译100是测量pipeline改变，不能倒称模型更有害或评价更真实；Table9同一raw输出guard与translatedoutput guard下DeepSeek36→26、Gemini24→22，mixed input+translatedoutput对照又有变化。已有现代语言对齐/原语guard够用的判断→原受限语言变体中测量和guard可见性不同→需分别验raw/transformed输入与真实harmful标签，不让英文规范化自动替原文真值。此窄经验反侧若落窗，拟2+1+2=5；不是经典中文普遍优于其他语言或FOA独创新原语。

Table12同攻击设置英文/现代中文/古文82/86/100为有限对照，unknownpretraining/alignment数据分布不支持“High Capability-Low Alignment”因果保证。50AdvBench/100CLAS/60StrongREJECT-small、6API模型、DeepSeek-Chat攻/译和GPT4ojudge＋manual；平均target queries不是attack/translate/judge/人审总代价，各baseline预算不完全同。二stage翻译可改变含义，规范化本身未经独立faithfulness验收。防御与指标测试原件/译文双保留，不提供利用步骤或用promotionalASR签安全无效。

current Comments明确ICLR2026Poster；官方OpenReview同题同9作者摘要PDF已定点找到：[正式论文](https://openreview.net/pdf/6c74df58b713d1884aca9fb94ef5dbb5e6aeb929.pdf)。搜索相对“7months”不是确切pdate，不能据此定某天首公开；仅称存在conference family身份信号，本窗arXiv区间不能替家族firstpublic/重要新增事件。两次同题primary限定搜索停止，没有可核forum/pdate；不扩查ICLR全部。当前未进确定候选/Books；重开需同identity官方public date（或此前正文公开上界）及如早公开，本窗有实质新事件的依据。技术必要源有效但不是safe。Submitted02/26 13:25:35Z，sameIDregistered02/27 02:59:37Z，仅arXiv事件09:00～10:59:38+08。

## 23024 InCoM：窄IN5，真实v1不采用发现稿real-world声明

[v1](https://arxiv.org/html/2602.23024v1) blocks27–57/76–81一次已读。固定scale感知与base→arm单向条件不能同时表达阶段注意和双向协调；实际新增：历史action增量/当前globalfeature驱动三scale权重，base/arm各自flow decoder在每层以trajectory summary互换信息而stopgradient阻断跨路反传。不是“encoder+flow”名字套装；会改变**是否共享输出头、单向层次还是分路前向互条件**选择。Table4 full83.8、固定多scale78.2、single-scale64.3以及更换decoder75.9是受限机制对照。拟2+1+2=5，继续必要预算/反侧与Ch26实际owner，不授权安全/coordination最优。

训练kinematic增量标签不是intent真值；base/arm静止时Eq3归一化/zero support需明确，softaffinity不是真实物理对应，stopgradient不保证共享条件函数全冻结。DCFM替densehead改变architecture/objective不独立证明双向stopgradient唯一原因，轨迹summary/多scale计算和交互仍付费。发现题摘称实机验证，**exact-v1完整摘要没有该句、原结果段集中ManiSkill-HAB**，该discovery→v1差异只撤真实硬件采用，不复扫其余初筛或默认比v2–v7。原v1titleWhole-Body亦与currenttitle略异，采用精确v1。currentv2Apr27～v7Sep28窗外，不默认revisiondiff。

Submitted02/26 14:03:58Z/registered02/27 03:00:38Z，事件09:00～11:00:39+08；必要具体family旧事件未见，不以Submitted直接公开。

### 23024 必要审阅与 actual owner（2026-10-06）

feb28_vla_last7非原packet作者实际核精确v1 §3.2–3.5/4/A、blocks27–57/62–81/89–101。Fetch7DoFarm/torso/2DoFbase；13Daction中11jointincrements走PD、2linear/angularbase，normalized[-1,1]不是安全界。三层sparse3D/DINOv2、历史action+globalCLS产生scalegate、kinematic增量弱目标/KL/entropy=.1，静止support与Eq3归一化实现未披露，不把它当intent真值。dualflow每层summarytoken前向互读，cross-read state sg截另一分支grad不冻结sharedψ/本分支；decoder替densehead改变架构+objective，75.9 vs83.8不授sg唯一因果；fixedscale78.2/singlescale64.3支持受测scale选择。DARM positionalsoftaffinity/OT不是真实geometry correspondence，不重复推导本次不采用的细式。

模拟三scenario/PPOopenclose+SACpickplace每task1000success demo，100ksteps/B64/Adam1e-4/warm1000/cosine100k，λscale1/λalign.01；evaltrial数/seedCI/hardware/precision/完整端到端时延未充分披露。AC-DiT原paperprivileged直接引用非同population，π0 RGBonly+大预训练另表，不授公平head唯一原因；SetTableopenfridge87.3低于90.7/90，其他人口pickall仍低；初始target不可见、对象落下、尺寸误估碰撞和grasp-slip是直接反侧。exact-v1无实机采用，discovery题摘称实机已撤，不比窗外v2–v7。score2+1+2=5保留，Ch26已有MoPA分query/branchexchange但未含dynamic尺度与summary前向互条件/sg后sharedencoder梯度边界；只深入这一差额，窄融Perception分流节。费用、sim/输入人口及旧fixed/shared/单向decoder-controller回退近文。原Submitted14:03:58Z/registered03:00:38Z、本窗09:00～11:00:39+08与current/家族未变事实复用本日原证。正文/完整邻接/自身末注实际顺读；root非写入者actual POST通过，本项终态，非日级Gate，未核artifact/复现。

## 23029 WISER：窄经验条件IN5，不授advertised分支独立概率

2026-10-06 后续必要Evidence/Books（`feb28_ch76_ch36_finish`）：原v1 blocks32–53/58–61/67–76/96–101直接核samecandidate verifier输入、Eq8/9、Table3core对照、threshold/iteration及失败侧；保原准入、未把Eq8当独立概率或校准confidence。2+1+2=5，窄Evidence通过；actualCh76 representation/admission已有但缺文本/编辑图双proposal共享verifier与非单调预算选择，窄I写284、完整邻接262–294、末注1284，root 非写入者已实际核正文、完整邻接与自身末注，POST通过。BAGEL/Qwen2.5VL7/GPT4o/CLIP/H20/K50/一轮/.7仅作者设置，额外调用与shared错误计价；未核实现/复现，日期采用上文原值policy+registered区间、不默认diff窗外revision。

[v1](https://arxiv.org/html/2602.23029v1) blocks32–53/68–76/96–101一次已读。retrieve/verify/refine与双路生成都是成熟原则；具体受控增量是**编辑后文本与编辑后图像检索的固定similarity混合可比单路更差，而shared candidate verifier/低confidence门控反复检索的效果与阈值非单调、追加iteration收益递减**，改变何时开双路/何时付refine成本的具体选择，不凭CIR领域45%/57%headline。70同editor单T2I接近CIReVL、同core组件替换与fixedfusion扫描提供必要准入依据，75阈值过高回落/97两路都误与局部条件遗漏保反侧。拟2+1+2=5，继续必要configuration及actualCh76 owner比较；不把所有reranking称新机制。

Eq5对candidate的verifier只读同ref/instruction/image，未给branch特有证据。相同candidate两路c的独立性未证，Eq8sum/lexicaltie不授权独立likelihood融合或calibrated可靠性；branch最高yes probability也不是真值/不确定性校准。双路遗漏目标时refine只能改proposal，不能从无reference创造truth；同VLMcaption/reflection可放大共同错误。较大32B verifier退步、不一定thinking可靠；maxiteration与threshold增加GPU/外部调用费，0.5GPUh/1%无统一production成本分母。潜力与数值可信度分开，不由这些限制自动EX或整项D。

Submitted02/26 14:11:10Z/registered02/27 03:00:45Z，事件09:00～11:00:46+08。current CommentsCVPR2026，版本Mar2/7/24窗外，不默认diff；本轮未发现撤回/重要纠错说明。

## 23058 GeoWorld：几何prediction接口窄IN5；GRL惩罚子命题隔离

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；Poincaré映射/action predictor坐标目标接口；Eq17恒零与GRL归因隔离。2+1+2=5，Ch25自身末注1286；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：blocks30–80/385–399；Poincaré映射与action predictor的坐标/目标接口；Eq17三角恒零与GRL归因隔离、视频非物理闭环。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

[v1](https://arxiv.org/html/2602.23058v1) blocks30–80/385–399一次已读。不是JEPA+RL字样组合：将Euclidean encoder状态作为原点tangent经exp map进Poincareball，action-conditioned next-state predictor按hyperbolic距离做teacherforced与两步rollout训练，改变**latent error metric/curvature与长horizon训练接口**。Table5原v1的SFT(hyperbolic)/GRL(Euclidean)/GRL(hyperbolic)分开报告，horizon7/8与短horizon差异可继续核验，拟2+1+2=5。非实体物理系统验证，CrossTask/COINvideo labeledaction不是任意robottransition oracle；branching几何prior不等实际层次truth。

必要直接反侧：Eq17 `max(d(x,z)−d(x,y)−d(y,z),0)`在合法同metric的三个点上由三角不等式恒为零，故不能作为非零geodesic一致性约束/trajectory变直证明；Eq18与β改变的Table4结果无法按该writtenpenalty归因。41/53预测target距离低也不保证整条path是可行动geodesic；15将maxnegativecost写minpositivecost没有保负号，不直接当等式。**隔离这两个GRL/几何保证子命题**，不认证artifactbug或全paper无价值；独立representation/longhorizon经验分支仍待必要方法对照/owner。足够此小恒等式即止，不遍历全部hyperbolic/RL背景或proof。

Submitted02/26 14:42:53Z/registered02/27 03:01:27Z，事件09:00～11:01:28+08。v1/current CommentsCVPR2026；currentv2May17窗外，没有重要纠错说明，版本号不触发diff。

## 23079 SALA：成熟组合EX，停止不评分/Books

[v1](https://arxiv.org/html/2602.23079v1) blocks19–40/77–88一次已读。全文题摘潜在隐私信号已定点核：metadata/web候选、经典stylo指标＋LLM比较、embedding/keyword数据库复用、reflection-guided改写vsdirectparaphrase。原方法就是这些成熟组合；受限新闻作者匹配/同框架guidedrewrite分数未给新的独立attack-generalization、evaluationoracle或privacy预算/失败条件，不能只将“deterministic工具解释”重命名为新authority机制。79 guard对任务表述不同的观察无matching/样本受控试验，不能凭这条一般风险话语升级为独立新安全反证；英语news与representationbias限制也未形成新控制设计。明确项目相关但**具体增量门槛未达**，不是因为未开源/昂贵/新闻题材排除。

Table8 targeted0.827→.561/openworld.156→.012与embedding相似只支持作者改写实验，不证明semantic内容全保或privacy认证；82“near-random”未定候选分母，不能无条件照录。本轮不进一步查全部攻击案例/训练预算/owner。日期不影响EX，Submitted02/26 15:05:13Z与metadata上界可留原值，不额外创建必要日期请求，raw保留。未见撤回或重要纠错说明。

## 停止

准入校准待root；23024/23029/23058拟进入必要证据，不因本次局部读数授完成。22983只因具体family日期信号保留，非原文访问受阻；23079EX不评分。35safe与未冻结总候选状态不变。仅定点源事实及risk排除，未遍历全部613库存/228切片。

2026-10-06 root非作者一次准入原段独核：23024 blocks27/28/37/40/45/47/76/79；23029 35/36/47/53/70/75/97；23058 35/41/53/55/56/76/80/390–392及74–79/393–399。三项窄IN5通过，仅授具体准入，未授日期/必要标准Evidence/owner/Books完成。23058 Eq17三角不等式下恒0实际核到，不采用GRL保证归因，不由此推全经验无效。
