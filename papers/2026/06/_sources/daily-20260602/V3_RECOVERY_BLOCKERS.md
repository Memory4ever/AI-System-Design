# 2026-06-02 V3 恢复阻塞与共享写入队列

## 当前独立恢复停点（2026-10-01，覆盖以下旧完成状态）

作者sep22_resume_v3仅接管06/02默认[06/01 09,06/02 09)BJT；AGENTS/当前V3合同、每日来源/适用arXiv主题、ROADMAP与相关checkpoint已重读。不继承09/22或旧月候选。旧可读110=32I75E3Only是工作清单，不是当前验收结果。10/01 root独立日期语义裁决后，110全部转具名DateHold：正常schedule、Submitted与DataCite Updated不证明公开上界，Available仅月份；当前正式候选无核准项，不等于零命中。六必要恢复包与有效笔记保留供真实归属日复用，未声明全110证据读完。旧32I正文不一刀删除，但本日采用链未通过本次验收，不计本轮I、不新写DateHold；空JSON和匿名旧post-write声明不是验收。

实际发现canonical raw的date_semantics以DataCite created作部分归属依据，first/last注册字段在06/02 11:41–12:42BJT，不能据此证明统一08–09公开。有限日入口、正确monthly无dayheaders、root official advanced年月粒度与具名metadata恢复已穷尽当前可用日期证据；[DataCite官方dateType](https://datacite-metadata-schema.readthedocs.io/en/4.6/appendices/appendix-1/dateType/)定义Updated是资源最后更新而非Available。日期缺口已隔离终态，重开需当日官方批次、公开receipt或arXiv明确provider字段公开语义；不扩1449发现。14厂商/arXiv来源已定点恢复实际stop，Google Research/Qwen/MiMo/arXiv缺口明确保留。旧negative共同错误已对00944/00997/00981/01128/01600/01185补机制与反证，不以费时或日期障碍关闭具体贡献。10/01 root非作者本次安全隔离终态日Gate通过，实际范围见正式README §6；110旧表+六不重叠恢复=116终态日期保留，无已核准当窗候选，旧32I本轮不验收，不声称全116证据/Books通过。当前普通0，报告完成；未stage/commit/push，dirty/staged与原证据保护，索引LearningState归root。

### 2606.00944v1 — PRISM：准入恢复与一般 gauge 主张争议

已实际读[官方题摘/版本页](https://arxiv.org/abs/2606.00944v1)及[exact-v1正文](https://arxiv.org/html/2606.00944v1)§2、Algorithm1、§3.1–3.3、§4 Tables2–5/Limitations、A25–A27、B1及C1相关诊断。完整题摘新增的是同一低秩更新在不同因子表示下的剪裁/噪声差异及切空间随机机制；旧“未改变训练平台ownership”不是贡献排除依据。首提交原字段2026-05-31T01:19:03Z，官方页面未见撤回说明；旧receipt保留normal owner06/02及DataCite created2026-06-02T04:03:34Z，created只作ID存在上界，不作公开时钟，正式当窗入选仍待日级日期核准。拟命题评分2+1+3=6，确认长期缺口及中心反证需深入受影响内容。

采用可能成立的窄部分：Z=ABᵀ不因(A R,B R⁻ᵀ)改变，但factor梯度剪裁范数随gauge改变；独立factor噪声映射到Z时有因子范数尺度及二次乘积项，不等于原factor算法不具DP。full-column-rank时ΠA/ΠB定义的正交切空间投影只依赖子空间，跨全部LoRA modules的per-example intrinsic norm给单一clip coefficient；Eq19用两组(m×r)/(n×r)随机矩阵构造投影高斯，噪声能量r(m+n−r)是adaptive transform/retraction前的切空间结果，不能延伸成全训练轨迹界或无噪声损失。A25的privacy论证依赖固定当前DP历史/切空间、clip及Poisson subsampling+PRV accountant；adjacency尚未具体披露，C/b不能无条件用于replace-one（工程核验需要2C/b或相符约定）。标准LoRA的zero-factor初始化不满足full-rank流形假设，现读原文未给直接处理保证，不把dagger记号当作该保证。

中心争议必须保留：§3.3 Eq25与A26宣称一般GL(r)下adaptive intrinsic update/trace inverse floor不变，A27 LemmaA30实际只证明orthogonal R。经root必要源独立核准，采用精确可行的sanitized-noise分支反例：m=n=r=1、A=B=1，zero clipped-gradient平均且Eq19的ΩB=1时，I−ΠA=0，得到(ΔA_dp,ΔB_dp)=(0,1)。零初始moment的一步中mB/VB分别与1/1成比例、Eq26 λB与M⁻¹=1成比例。正缩放c=2后A'=2、B'=.5，等价noise lift ΔB_dp'=.5；mB'为原1/2，VB'/λB'为原1/4，故Eq25 UB'=UB，但intrinsic方向A'UB'=2AUB。trace(M⁻¹)也从1变1/4。该代数反例不是实际运行复现；它无需声称任意抽样pathwise invariance，而直接否定一般GL下同一可行lift的adaptive intrinsic不变公式。不能正面采用“整套adaptive optimizer一般gauge invariant”或完整数值/privacy实现保证；投影/noise分布的窄结果与争议分开。重开一般保证需要作者修正或新的证明，不靠有限c sweep消去反例。

评价只绑定单A100-PCIE40GB、Gemma3-4B主实验（9B/12B有限text-only对照）、r16（8/32敏感性）、GLUE8/Math10K、500/300 updates、effective batch64/micro4、len384/256、seed42、ε3/6 δ1e−5与各optimizer不同LR；dtype Not Disclosed。DP suite平均有利但SST2/RTE/AQuA等不是全赢，非DP RITE均值更好；Math单卡10warmup+30measured step time约18.64s vs AdamW9.37s、peak memory近同。没有multi-seed普遍效用、生产或实现复现保证。实际Ch30 PrivateSelector段仅两阶段预算，factor谱段仅坐标敏感merge，projector共识段仅联邦聚合；均未承载intrinsic-private-update的剪裁/噪声/退化rank边界。拟owner `TRAIN-LORA`、PrivateSelector之后两段，未申请/获得写锁；当前窄I还是中央D须非作者裁决。

### 2606.00997v1 — OALM order diagnosis：恢复具体诊断而非无条件定理

已实际读[官方题摘/版本页](https://arxiv.org/abs/2606.00997v1)、[exact-v1正文](https://arxiv.org/html/2606.00997v1)§1–3、§4.1–4.4 Tables1–4、§5–6、A1/A2/A4/A5、B必要协议/统计与C sampling sweep。首提交2026-05-31T04:25:36Z；官方页面没有withdrawn说明，旧“撤回”仅项目旧准入/采用链处置，不能冒充官方事件。旧receipt的normal owner06/02仍待日级日期核准。拟评分2+1+3=6，长期缺口深入必要范围；新增不是系统control术语，而是masked learned conditionals未必对应同一coherent joint，次序改变会同时改变target log-product与瓶颈形状。

Th3.1的uniform optimum只在固定productP、逐step成功模型与log f(exp(y))严格凹时成立；A1的single-competitor Gaussian/logit noise及conditional successive successes不等于真实qt traces独立，A4的小σ/凹性范围不能静默外推全vocab/σ或在线decoder。§4在同一LLaDA2.1mini、block32、one-token-per-forward、C4 fixed1000（prefix32+target128）中对固定target仅换reveal order，mean logP/n −3.00至−3.49是有限checkpoint的order-coherence反证；forced-L2R仍是block-bidirectional计算，不变成causal AR。同prompt四benchmark、greedy、max16384/EOSstop、KV-cached driver的content mean/variance是joint diagnostic，排EOS、task grading与trace length仍须记录；硬件/dtype Not Disclosed，没有端到端加速或parallel-batch保证。

关键negative：Table3全部cell mean方向相同不等于全部显著，IFEval Forced p=.068、Random p=.059，|rho|仅约.06；Table4 IFEval lo-mean/lo-Var64.7低于lo-mean/hi-Var67.3，直接限制正文“matched mean低Var never worse”泛断言。withinstructured order无stablewinner，content path近L2R并有不同EOS tail，min-V是完整logged trajectories的事后比较，不是已部署在线policy；sampling sweep只测C4固定长度，亦非一般任务保证。保留二轴诊断及条件理论，不采用普遍正确性排序或oracle-free算法。actual Ch24 Masked generation的confident-gating熵界、attention影响排序、position/token温度和多chain-remask虽相关，尚未承载learned joint incoherence与fixedtarget order-log-product/variance分账。拟owner `MULTIMODAL-GENERATIVE-PARADIGMS`、confidence影响排序前窄两段，未获写锁。待非作者必要源→actual owner核，未自动入正式候选分母。

### 2606.00981v1 — Auto-formalization：接口失真与执行状态保留

已实际读[exact-v1题摘](https://arxiv.org/abs/2606.00981v1)与[正文](https://arxiv.org/html/2606.00981v1)§3–5.2、Limitations、C3/Table16及E在线event-delta模板。v1提交2026-05-31T03:28:42Z；旧正常owner只作日期线索，尚未核官方当窗公告。旧“既有solver串联、无ownership变化”误挡的是具体faithfulness与repair反证，不因已有solver原则而关闭。拟2+1+3=6，长期缺口深入必要范围。

新增命题不是CP-SAT天生正确：计划accuracy同时验原问题依赖/目标/资源、duration与optimal makespan。PDDL谓词/effect/goal的间接编码可让语法正确/solver有解而原任务关系丢失；统一solver-neutral IR后确定性编译给两种target、Gold IR绕过提取，分开自然语言提取与compiler/solver/plan-extraction失效。§5.2及Table16的直接PDDL .1%→NL-IR79.3%，Gold83.9%而CP-SAT Gold100%仅支持所测pipeline，不证明PDDL语言无表达能力。**C3叙述与Table16有数字冲突**：叙述NL PDDL54.8–64.4/Gold64.4–77.6不等表中75.2/84.0/69.6/88.4与81.6/88.8/75.2/90.0；Qwen叙述94→68.4也不等95.6→97.2。采用分账机制，不拿这些矛盾数字合成收益或模型优劣保证，重开具体数值需作者澄清。

在线new-event不重建整份spec：completed固定，running保留start与resource占用到committed finish，LLM只返回event delta，solver reschedule remainder。46.1→84.5是四模型/140题有限均值而非真实机器人控制；online hard optimization仍是关键残差。600合成DAG5–100、AsyncHow320、Robo与Online各140（每split20）、四模型temperature0；Figure3仅两模型均值范围，不称四模型CI。Robotouille低层仿真CP-SAT0/PDDL17.5与简化Robo98.8并存：后者去掉navigation/bookkeeping，不能外推真实执行。硬件/dtype Not Disclosed，最多3次syntax repair额外成本未给端到端SLO。actual `AGENT-PLANNING` Ch79:145–166仅feasibility/execution mismatch与suffix refinement，未承载representation→IR控制/原问题关系缺失、running resource-preserving event delta。拟solver-boundary后、旧trajectory refinement前两段；未获锁/未写，日期和非作者source→owner待核。

### 2606.01128v1 — Local MixVR：通信轮数与样本量的条件分离

已实际读[exact-v1完整题摘](https://arxiv.org/abs/2606.01128v1)（canonical raw在M<处截断不能代替）、[正文](https://arxiv.org/html/2606.01128v1)§2–4、Algorithms1–3/Lemma3.1/Th3.2、AppendixG实验。v1提交2026-05-31T10:02:15Z，公告归属仍待核。旧“无large-LM/跨workload”不能排除直接通信理论。拟2+1+3=6，长期缺口深入：常规local drift→同样sample budget中三种variance-reduction协同→把communication-round界与dataset size分开，不宣称训练免费或普遍LM收敛。

条件为共同分布D、独立samples、凸expected objective及每sample L-smooth、bounded gradient variance/smoothness variance、global minimizer与特定stepsize。慢的anytime iterate+同sample两点STORM差分；K预算分成local与minibatch accumulation，先平均两组参数，再在共同参数点与旧local点用同minibatch耦合差分校正gradient estimator，最后另一次平均estimators，不能只平均参数/moments。Th3.2保LD1²/(KR)+sigma-tilde D1/(sqrt(K)R)+sigma-tilde D1/sqrt(MKR)，在固定常数/统计误差主导与N=MKR的渐近比较中R尺度依M；M≲N^(1/4)才有相对ASGD窗口，不把这个Big-O阈值当精确可部署worker上限。

关键边界：正文一处μ²局部递推写beta*g，而Algorithm1是g+(1−beta)(d−g_previous)，不直接复制歧义公式为implementation recipe；AppendixG实验又用gamma=.95及标准momentum .9，不是Th3.2的gamma=2/(t+2)、beta=1/t配方。MNIST4/CIFAR8 workers、B200、2-layerCNN/ResNet18、2/30epochs、perworkerbatch4/16、3seed、LR及alpha grid仅accuracy-vs-rounds证据，dtype/实际拓扑/bytes/wallclock Not Disclosed，FineWeb数字仅理论规模代入非实际LM实验。actual `TRAIN-DISTRIBUTED-TRAINING` Ch36:70–83有LocalSGD、sharedgradient多参数、compressed gossip，不承载accumulation校正的共识对象与条件sample-independent rounds。拟该分支末两段；未获锁/未写，非作者source→owner待核，不冒充已复现实验。

10/01补读AppendixE Lemma3.1证明的三种step噪声、Eq22–25同步drift和variance预算，以及F LemmaF.1/Th3.2最后代入：当前round的未平均噪声保留Kloc项，旧round与minibatch才有M/Kavg降噪；凸性/Jensen与eta≤1/(8LT)后将error budget纳入loss界，T=R(Kloc+1)≥KR/2导出所列三项尺度，不能静默省掉local variance成本。F最后代入第一行HTML写24eta/M，但由F.1的12eta/(TM)与Lemma3.1的worker平均式代入应是24eta；后续显示的sqrt(Kloc)项又没有额外1/sqrt(M)。这是精确公式一致性未决，不把该中间行用于更强的M收益，也不以它宣称最终保守三项界已被反驳。需非作者核必要原PDF/公式后裁支持范围，不遍历无关证明或降分关闭。

### 2606.01600v1 — RoboTrustBench：按可行性改变评价方向

已实际读[exact-v1题摘](https://arxiv.org/abs/2606.01600v1)、[正文](https://arxiv.org/html/2606.01600v1)§3–5/Table2–4、Limitations、B generation settings/E human-MLLM agreement。v1提交2026-06-01T02:56:09Z；不借08/31v2改写本窗，日期公告仍待核。拟2+1+3=6，既有WorldModel原则不等于该具体反证已覆盖。

以DROID instruction+初始图建立Normal533/Constraint345/Counterfactual228/Adversarial101，共1207；77图编辑、三专家检场景。13项评价中task completion在feasible是正侧，在infeasible反而可指hallucinated execution；unsafe跟随同样不能当高质量。按18子类各10形成180 human subset、7模型1260视频、三评者1–5+NA，人工不是完整1207每项；自动评20frames可遗漏瞬时接触。Table2清晰图像与弱physical realism并存，Figure4是condition on high-completion的切片，不无条件推普遍相关/因果。GPT5.4比human宽松，Table10有任务/safety相关较强、细视觉很弱，ImageQuality饱和/ties也使human相关低，不能仅把低相关归于MLLM不懂物理。

所有prompt统一加use robotic arm且允许默认rewriter；模型输出约5–6s、resolution/FPS不同，不同产品不能混成controlled architecture ablation。Veo三条guardrail未返视频被排除，缺失不是安全率成功，也不能将完成样本的unsafe指标外推request population。硬件/dtype Not Disclosed；仅离线instruction-conditioned视频，无真实adversarial action/closed-loop后果、安全保证。actual `MULTIMODAL-WORLD-MODELS` Ch25:645–665有分层rollout/uncertainty/真实outcome，但未承载counterfactual completion分数方向反转与nonresponse selection；拟Evaluation首段后、rollout admission前窄两段。未获锁/未写，日期与非作者source→owner待核。

### 2606.01185v1 — Skill issues：逐提交验收，非所有技能可独立优化

已实际读[exact-v1题摘](https://arxiv.org/abs/2606.01185v1)、[正文](https://arxiv.org/html/2606.01185v1)§2.2、§3.1–3.3/Table1、§4及AppendixA的write verifier示例。v1提交2026-05-31T11:58:04Z，不用07/16v2的摘要数字替代；本窗公告仍未核准。原关闭理由“vertical workflow/未改变平台ownership”不能排除写路径评价的具体贡献，拟2+1+2=5标准审阅；是否落窗与最终E须非作者核，不自动成为正式候选。

工具trace、lakehouse state、final response是不同证据：同一任务先准备用户分支/初态、冻结main与用户分支baseline commit，运行后验end_conditions并回收post-baseline分支。API write映射immutable commit，state verifier按commit检查branch/table/schema/rows/merge；只看文本或CLI名称不能证明目标数据发生变化。CLI与SDK两种合法路径应按实际语义检查，不把调用形式当唯一正确轨迹。AppendixA示例实际只检查存在性、row count、正总量与总量接近；这些有限predicate不能证明任意行/所有字段正确，工程采用仍需按任务声明覆盖及独立审查，非作者已证明完备。

§3.2.1明确生产API频率受当前skill描述影响，不能直接作任务混合；rare safety操作需人工taxonomy补覆盖。§4仅25任务（6 read/8 pipeline/6 fix/5 ingestion）、每skill按50/25/25划分且val/test最低各1，Claude Sonnet4.6+Claude Code。四技能heldout平均改善31.9%，skill字符长度平均增93.3%；两种multi-skill任务未找到较seed更佳候选，不能外推联合优化收益。hardware/dtype Not Disclosed；论文有限cost/time曲线不支持生产吞吐或对任意destructive action的安全保证，artifact未实际执行。

actual `AGENT-WORKFLOW` Ch81“搜索分支必须连同权威外部状态一起分支”正文292–298已具体绑定candidate artifact/database revision、promotion与回收，并保snapshot隔离成本/fallback；`PLATFORM-EVALUATION-SYSTEM` Ch66过程合规正文330–344把tool trace、环境transition/effect receipt和final outcome分开，regression正文282–319保requirement coverage、固定environment identity与未知失败；这些是拟保留的长期命题，不仅主题相似。当前拟已有覆盖、No Change；31.9%及25任务仅本研究上下文，不新增普遍skill优化正文。未写Books，日期和非作者结论待核。

## 早期分母与写入过程记录（不作本轮验收）

以下至原文件末的冻结/已完成措辞仅旧运行快照，受顶部当前停点覆盖，不支持本轮候选、Evidence或Books断言。

### 分母证据冲突

- 可读 canonical raw packet：1,449 identities。
- 可读 semantic checkpoint：51 prior candidates + 1,398 closure proposals；其中历史状态字段已由本次 110/1,339 重审结果取代。
- 可读 owner receipt：51 candidate identities，18 个由 DataCite 确认本 owner，33 个需要迁移后重建。
- 旧报告顶部另称 736 raw identities、旧 52 收紧为 28；对应 `identity-provenance-v2-strict.json`、`candidate-denominator-audit-v3-fresh.json`、`screening-ledger-v3-fresh.tsv`、`evidence-audit-v3-fresh.json`、`evidence-books-comparison-v3-fresh.json`、`post-write-fresh-audit-v4.json` 均为 0 字节。

不得以 28 这个总数反推候选身份。当前已从 1,449-row packet 冻结 110 Candidate / 1,339 Close：旧 51 项为 44/7，旧 1,398 closure 为 66/1,332；逐项结果见 `V3_SCREENING_LEDGER.md`。

本轮 false-negative 抽检证实旧共享理由不可靠，因此已全量重审 1,398 项并恢复 66 项。`SENSE`、`ART`、`BudgetDraft`、`PrivacyPeek`、`Bit-Exact AI Inference Verification`、`PR2`、`When Safe Skills Collide` 和 `TAPS` 的完整摘要能指出明确系统合同；`BitsMoE`、`CAST` 等仅有局部模型/训练增量者仍关闭。当前不再有待重审的 closure family。

### 旧Books共享写入过程

旧报告标记 17 项 `Integrate`；当前准入保留 16 项，`SF-ORDER-AGNOSTIC-CHAIN-RULE` 撤回并删除整条采用链。三条错误 Daily 日期均已修正为 `2026-06-02`。16 个存续项已逐项执行 trace-to-body：14 项完成正文绑定，`SF-ADAPTIVE-AUTO-HARNESS` 与 `SF-GHOST-TOOL-ISSUE-PRIVACY` 经当前正文重读改判 Existing。

本轮从旧 closure 恢复的 20 个 proposal 也已全部由对应 owner 消费：19 项完成正文绑定，`SF-MEMPRO-EVOLVABLE-PROGRAM` 经当前 Memory 正文重读改判 Existing。另有 `SF-SKILLHARM-LIFECYCLE` 在旧前沿复判中由 proposal 改判 Existing，命题锚点为“Harness Backdoor 把单次写入变成跨 Run 控制状态”。

最终共享队列为 0，exact-v1 access blocker 为 0；全部新增正文与 Existing 锚点已经由非作者按正文而非 trace 完成 post-write review。完整清单与验收结果见 `POST_WRITE_AUDIT_SCOPE_V3.md`。

## 110旧工作家族具名DateHold清单

110项全部缺本窗真实公开上界；旧拟分数、owner与材料身份仅恢复线索，不是当前候选。新六包00944/00997/00981/01128/01600/01185位于顶部，另保日期Hold；实际ID对照无重叠，共116具名日期保留，不增加本窗正式分母、不称116已审。禁止将Submitted/Updated/Created合成08–09公告。完整原始公开字段见上述既有receipt，仅正常schedule亦不能排除hold。

| 材料 | 日期处置 | 旧拟贡献与评分（未本轮核准） | 审阅标记处置 | 旧owner定位（未本輪采用） |
| --- | --- | --- | --- | --- |
| [Emergent Collaborative Deliberation in Multi-Model AI Systems](https://arxiv.org/abs/2606.00005v1) | DateHold：公开落窗未证 | persona×model 分权、claim chain 与 OOS evidence 分离共识和证据；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../../books/part-07-agent/82-multi-agent.md) |
| [Deliberative Curation](https://arxiv.org/abs/2606.00007v1) | DateHold：公开落窗未证 | guarded knowledge-artifact lifecycle 与分层复核/争议协议；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [Completion at the Boundary](https://arxiv.org/abs/2606.00145v1) | DateHold：公开落窗未证 | Before/Hit/After object 将 completion proposal 与 handoff action 绑定；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-WORKFLOW — [章节](../../../../../books/part-07-agent/81-workflow.md) |
| [Persona Attack](https://arxiv.org/abs/2606.00150v1) | DateHold：公开落窗未证 | incremental memory injection 使风险跨 turn/implementation 累积；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [DataShield](https://arxiv.org/abs/2606.00160v1) | DateHold：公开落窗未证 | compliance-direction probe 将 benign content 扩为 training-effect admission；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：TRAIN-DATA — [章节](../../../../../books/part-04-training-system/27-data.md) |
| [BAGEN](https://arxiv.org/abs/2606.00198v1) | DateHold：公开落窗未证 | prefix replay 校准 remaining-budget interval、feasibility 与 false abort；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLANNING — [章节](../../../../../books/part-07-agent/79-planning.md) |
| [Quantized Reasoning Models Think They Need to Think Longer, but They Do Not](https://arxiv.org/abs/2606.00206v1) | DateHold：公开落窗未证 | PTQ 引发 intermediate-correct/final-wrong 与 reasoning-token inflation；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-GPU-MEMORY — [章节](../../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [The Deterministic Horizon](https://arxiv.org/abs/2606.00376v1) | DateHold：公开落窗未证 | 长链 state tracking 超界后将可形式化 transition 委派给 deterministic tool；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLANNING — [章节](../../../../../books/part-07-agent/79-planning.md) |
| [SENSE](https://arxiv.org/abs/2606.00021v1) | DateHold：公开落窗未证 | 语义检索与 soft gate 改变 speculative verification contract；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [ART](https://arxiv.org/abs/2606.00024v1) | DateHold：公开落窗未证 | value-aware accumulated-output stability 在 kernel 内终止 KV traversal；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点“Value-aware Termination 只能提前结束读取，不能接管正确性” |
| [Agreement Metrics for LLM-as-Judge Evaluation](https://arxiv.org/abs/2606.00093v1) | DateHold：公开落窗未证 | 将 scale、exclusion、abstention、pooling 与 metric 固化为可重构 measurement identity；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Judge Agreement 不是单一数字” |
| [BudgetDraft](https://arxiv.org/abs/2606.00144v1) | DateHold：公开落窗未证 | sparse drafter/full verifier 的多 KV budget 与 acceptance-aware training；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [PrivacyPeek](https://arxiv.org/abs/2606.00152v1) | DateHold：公开落窗未证 | 隐私 gate 从输出/issue 前移到 tool response 进入 context 的 acquisition 时刻；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Tool Response 在进入 Context 时就要执行 Data-minimization Gate” |
| [Bit-Exact AI Inference Verification](https://arxiv.org/abs/2606.00279v1) | DateHold：公开落窗未证 | software emulator 以数值路径 identity 提供跨硬件 bit-exact replay；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PR2](https://arxiv.org/abs/2606.00395v1) | DateHold：公开落窗未证 | predicted MoE route 同时绑定 rollout behavior 与 training importance estimation；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md)；正文锚点“MoE Route Replay 也属于 Behavior-policy Identity” |
| [When Safe Skills Collide](https://arxiv.org/abs/2606.00448v1) | DateHold：公开落窗未证 | 安全对象从单 skill 扩为 installed set/capability union，并分离 static candidate 与 runtime issue；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Confused ChatGPT](https://arxiv.org/abs/2606.00485v1) | DateHold：公开落窗未证 | 共享 flat context 允许跨 app persistent write 与 confused deputy，要求 per-app isolation/mediator；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“App-local Context Namespace 阻止普通 Writer 获得跨 App Authority” |
| [TAPS](https://arxiv.org/abs/2606.00487v1) | DateHold：公开落窗未证 | prefix reachability 与 target verification latency 联合约束 draft tree；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [“I Strongly Suspect This Website Is a Scam”](https://arxiv.org/abs/2606.00497v1) | DateHold：公开落窗未证 | field-level endpoint outcome 揭示 detection–action gap，要求独立 issue gate；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Threshold-Based Exclusive Batching for LLM Inference](https://arxiv.org/abs/2606.00516v1) | DateHold：公开落窗未证 | workload/hardware crossover 驱动 mixed/exclusive phase switch；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [GNMR](https://arxiv.org/abs/2606.00539v1) | DateHold：公开落窗未证 | operator-normalized risk 与受预算恢复路径形成低精度训练控制面；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：TRAIN-PRETRAINING — [章节](../../../../../books/part-04-training-system/28-pretraining.md) |
| [Same Payload, Different Channel](https://arxiv.org/abs/2606.00566v1) | DateHold：公开落窗未证 | matched payload 隔离 channel-conditioned authority asymmetry；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Sandboxed Coding Agents are Competitive Omni-modal Task Solvers](https://arxiv.org/abs/2606.00579v1) | DateHold：公开落窗未证 | sandbox tool transformation 修正 native modality substrate 假设；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：仅报告：现有 tool/workspace contract 足以承载，离线 benchmark 未形成新 owner 机制 |
| [TRACE](https://arxiv.org/abs/2606.00611v1) | DateHold：公开落窗未证 | risk-aware latent evidence 与独立 reader 改变长轨迹 monitor state；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-MONITORING — [章节](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点“Risk-aware Latent 只能压缩 Evidence，不能压缩 Authority” |
| [MemPro](https://arxiv.org/abs/2606.00619v1) | DateHold：公开落窗未证 | 整个 MCR pipeline 成为可执行、可晋升与可回滚的 versioned program；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md)；命题锚点“Memory policy 本身也可能成为可学习、可版本化的 procedural asset” |
| [Hidden Thoughts Are Not Secret](https://arxiv.org/abs/2606.00642v1) | DateHold：公开落窗未证 | prompt-based trace exposure 证明 hidden interface 不是 secrecy boundary；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Invitation Trap](https://arxiv.org/abs/2606.00654v1) | DateHold：公开落窗未证 | 模型主动诱导未来 trigger，使 attack provenance 跨轮闭环；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“模型建议也可能塑造未来 Trigger” |
| [Scaling Behavior of Single LLM-Driven Multi-Agent Systems](https://arxiv.org/abs/2606.00655v1) | DateHold：公开落窗未证 | 固定 base LLM 后隔离 agent count 与 coordination tax；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../../books/part-07-agent/82-multi-agent.md) |
| [NeuroLog](https://arxiv.org/abs/2606.00669v1) | DateHold：公开落窗未证 | LLM typed facts、Datalog composition、SMT witness 与 ASan gate 分离推理 ownership；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Paradox of Outcome Optimization](https://arxiv.org/abs/2606.00674v1) | DateHold：公开落窗未证 | 因果/信息论边界解释 outcome objective 的 shortcut bias；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md) |
| [WaveFilter](https://arxiv.org/abs/2606.00724v1) | DateHold：公开落窗未证 | wavelet-guided token filtering 给 diffusion KV 压缩增加多尺度 selector；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ViBE](https://arxiv.org/abs/2606.00735v1) | DateHold：公开落窗未证 | workload skew 与 measured GPU service rate 联合决定 MoE placement；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [CoMIC](https://arxiv.org/abs/2606.00756v1) | DateHold：公开落窗未证 | edge-local history 与 cloud-owned cross-agent insight 形成双层 memory ownership；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md)；正文锚点“Edge-local Episode 与 Cloud-derived Guidance 必须分离所有权” |
| [FALAT](https://arxiv.org/abs/2606.00765v1) | DateHold：公开落窗未证 | typed dependency 与 counterfactual repair 区分 first causal error 和传播步骤；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-TRACE — [章节](../../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety](https://arxiv.org/abs/2606.00801v1) | DateHold：公开落窗未证 | semantic attack archive 将 red-team mode collapse 变成可观测 coverage state；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Semantic Archive 暴露 Mode Collapse，但不拥有 Release Verdict” |
| [Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems](https://arxiv.org/abs/2606.00804v1) | DateHold：公开落窗未证 | problem-class routing 在 consensus/debate/synthesis/single-agent 间选择控制路径；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../../books/part-07-agent/82-multi-agent.md) |
| [Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs](https://arxiv.org/abs/2606.00813v1) | DateHold：公开落窗未证 | attack archive 跨 release replay，阻止安全结论随版本自动继承；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SkillPager](https://arxiv.org/abs/2606.00822v1) | DateHold：公开落窗未证 | typed skill nodes、dependency completion 与动态 budget 形成 execution-sufficient context；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md) |
| [Momento](https://arxiv.org/abs/2606.00832v1) | DateHold：公开落窗未证 | 跨 session history 必须在 consequential action 前重验当前 user state；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md) |
| [MORI](https://arxiv.org/abs/2606.00866v1) | DateHold：公开落窗未证 | program-level relative idleness 决定 KV tier boundary 与 admission；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点“Agent Idle Window 要按 Program Horizon 决定 Tier，而不是二元搬空” |
| [MetaForge](https://arxiv.org/abs/2606.01801v1) | DateHold：公开落窗未证 | Decide–Retrieve–Adapt–Forge 将工具候选纳入可版本化 lifecycle；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [Cost-Aware Diffusion Draft Trees for Speculative Decoding](https://arxiv.org/abs/2606.01813v1) | DateHold：公开落窗未证 | target verification cost 与 context 驱动每轮 draft-tree budget；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [CRAB-Bench](https://arxiv.org/abs/2606.01815v1) | DateHold：公开落窗未证 | constraint graph 同时拥有 task generation、多解验收与 disclosure state；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Constraint Graph 可以连接任务生成与多解验收，但不能替代真实环境” |
| [Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus](https://arxiv.org/abs/2606.01828v1) | DateHold：公开落窗未证 | reliability/divergence/relevance 在预算内选择通信 edge 与 stopping；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../../books/part-07-agent/82-multi-agent.md) |
| [Benign Inputs, Harmful Outputs](https://arxiv.org/abs/2606.01837v1) | DateHold：公开落窗未证 | joint cross-modal semantics 可由各自 benign fragments 重组 harmful intent；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Trust-Calibrated Code Review](https://arxiv.org/abs/2606.01969v1) | DateHold：公开落窗未证 | overview/file/snippet 分层暴露 review risk cues；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：仅报告：概念原型与主观 survey 尚未形成可验证 release contract |
| [SafeMCP](https://arxiv.org/abs/2606.01991v1) | DateHold：公开落窗未证 | server-side look-ahead 在 agent 取得工具前限制 power/action set；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MMG2Skill](https://arxiv.org/abs/2606.01993v1) | DateHold：公开落窗未证 | human guide→editable skill→trajectory diagnosis→versioned revision；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [Extreme Low-Bit Quantization for Reasoning Models](https://arxiv.org/abs/2606.02011v1) | DateHold：公开落窗未证 | trace inflation/commitment failure 使 per-token speedup 不等于端到端收益；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-TENSORRT-LLM — [章节](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点“Reasoning Quantization 要验收 Commitment，而不只是 Token Cost” |
| [OpenWebRL](https://arxiv.org/abs/2606.02031v1) | DateHold：公开落窗未证 | live-browser state、trajectory judge 与 online multi-turn RL 形成训练 identity；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md) |
| [SentGuard](https://arxiv.org/abs/2606.02041v1) | DateHold：公开落窗未证 | sentence-level semantic fence 平衡 streaming intervention 与不完整语义误拒；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Streaming Guard 的最小可解释 Commit Unit 可以是完整 Sentence” |
| [BADGER](https://arxiv.org/abs/2606.02109v1) | DateHold：公开落窗未证 | generative structural parsing 与 deterministic scoring 分离评测 ownership；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AgentRedBench](https://arxiv.org/abs/2606.02240v1) | DateHold：公开落窗未证 | connector/destination/argument mutation 构成 integration-aware red-team subject；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点“Integration-aware Campaign 必须把 Connector 与 Effect Identity 编进 Case” |
| [When Knowledge Is Not Free](https://arxiv.org/abs/2606.02245v1) | DateHold：公开落窗未证 | evidence access tier、共享预算与 sufficiency/stop 联合进入检索状态；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：AGENT-RAG — [章节](../../../../../books/part-07-agent/76-rag.md)；正文锚点“Evidence Access Right、Cost 与 Sufficiency 是联合检索状态” |
| [POIROT](https://arxiv.org/abs/2606.02282v1) | DateHold：公开落窗未证 | peer interrogation 分散诊断但不形成独立 truth；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：仅报告：内部 Agent 共识不能替代 independent verifier |
| [Unified Context Evolution for LLM Agents](https://arxiv.org/abs/2606.02304v1) | DateHold：公开落窗未证 | typed Memory/Strategy/Workflow/Skill units 以 usage evidence 演进；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [Do Multimodal Agents Really Benefit from Tool Use?](https://arxiv.org/abs/2606.02357v1) | DateHold：公开落窗未证 | no-tool/call-shell/real-result 反事实区分工具确认、修复与干扰；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：AGENT-TOOL-CALLING — [章节](../../../../../books/part-07-agent/78-tool-calling.md)；正文锚点“Tool 出现不等于 Tool 对答案有贡献” |
| [MOC](https://arxiv.org/abs/2606.02359v1) | DateHold：公开落窗未证 | multi-order evidence stream 与 semantic-topological merge 改变消息 state；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：AGENT-MULTI-AGENT — [章节](../../../../../books/part-07-agent/82-multi-agent.md)；正文锚点“多阶消息需要 Ordered Evidence DAG，而不是压平后的共识摘要” |
| [SPADE-Bench](https://arxiv.org/abs/2606.02380v1) | DateHold：公开落窗未证 | regular/pressure 配对并比较显式 plan 与真实 tool action；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Investigating and Alleviating Harm Amplification in LLM Interactions](https://arxiv.org/abs/2606.02423v1) | DateHold：公开落窗未证 | trajectory-prefix monitor 捕获跨 turn 逐步放大的 harm；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [HLL](https://arxiv.org/abs/2606.02449v1) | DateHold：公开落窗未证 | 动态交互 telemetry 与 family-specific rules 验证最终状态；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AgentCL](https://arxiv.org/abs/2606.02461v1) | DateHold：公开落窗未证 | PG/SG 拆开跨任务经验的 plasticity、retention 与 interference；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md) |
| [MCP-Persona](https://arxiv.org/abs/2606.02470v1) | DateHold：公开落窗未证 | 真实 MCP trace 派生 stateful simulator 与 checkpoint/execution 双验收；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Monitoring Agentic Systems Before They’re Reliable](https://arxiv.org/abs/2606.02494v1) | DateHold：公开落窗未证 | structural/within-run/cross-run scope 先做成熟度与 FMEA 路由；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-MONITORING — [章节](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点“Pre-reliability Monitoring 先验证 Wiring，再解释 Quality” |
| [Tracking the Behavioral Trajectories of Adapting Agents](https://arxiv.org/abs/2606.02536v1) | DateHold：公开落窗未证 | versioned skill diff 上的 trait probe 只提供 promotion sensor；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SimSD](https://arxiv.org/abs/2606.02544v1) | DateHold：公开落窗未证 | temporal causal attention 与 RoPE alignment 恢复 dLLM token verification；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点“双向 Mask Context 必须先改写成 Temporal-causal Verification Layout” |
| [Lodestar: An Online-Learning LLM Inference Router](https://arxiv.org/abs/2606.00946v1) | DateHold：公开落窗未证 | 在线路由在质量、价格与延迟反馈间更新，改变多模型推理控制面；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Silent Failures in Federated Personalization of Foundation Models](https://arxiv.org/abs/2606.00947v1) | DateHold：公开落窗未证 | client-local 行为不可见改变 foundation-model 评测可观测性；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Federated Personalization 的盲区是可见性合同” |
| [When Parallelism Pays Off: Cohesion-Aware Task Partitioning for Multi-Agent Coding](https://arxiv.org/abs/2606.00953v1) | DateHold：公开落窗未证 | 依赖内聚性成为并行 Agent 分工与合并失败的控制条件；3+2+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../../books/part-07-agent/82-multi-agent.md) |
| [Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference](https://arxiv.org/abs/2606.01007v1) | DateHold：公开落窗未证 | workload identity 进入 MoE 通信分组与路由协同；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Hybrid Verified Decoding: Learning to Allocate Verification in Speculative Decoding](https://arxiv.org/abs/2606.01019v1) | DateHold：公开落窗未证 | 动态分配 speculative verification 改变正确性/吞吐合同；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [A Finite-Calibration Regime Map for LLM Judge Panels](https://arxiv.org/abs/2606.01034v1) | DateHold：公开落窗未证 | 有限 calibration 下 judge panel 的适用区间与报告要求；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Leyline: KV Cache Directives for Agentic Inference](https://arxiv.org/abs/2606.01065v1) | DateHold：公开落窗未证 | Agent 生命周期意图下沉为 KV cache directive；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Before the Model Learns the Bug:Fuzzing RLVR Verifiers](https://arxiv.org/abs/2606.01066v1) | DateHold：公开落窗未证 | 训练前 fuzz verifier reward 漏洞改变 RLVR 发布门禁；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Deep Research as Rubric for Reinforcement Learning](https://arxiv.org/abs/2606.01091v1) | DateHold：公开落窗未证 | evidence-derived atomic rubric 改变 RL reward provenance；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md)；正文锚点“Evidence-derived Rubric 是版本化 Reward State” |
| [memorywire: A Vendor-Neutral Wire Format for Agent Memory Operations](https://arxiv.org/abs/2606.01138v1) | DateHold：公开落窗未证 | wire format 明确 memory 读写、版本与互操作 ownership；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md) |
| [SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision](https://arxiv.org/abs/2606.01139v1) | DateHold：公开落窗未证 | 失败轨迹接入持久 skill 变更闭环；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [Schedule-Level Shared-Prefix Reuse for LLM RL Training](https://arxiv.org/abs/2606.01143v1) | DateHold：公开落窗未证 | schedule-level prefix reuse 改变 rollout/training KV 生命周期；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md) |
| [When Data Is Scarce: Scaling Sparse Language Models with Repeated Training](https://arxiv.org/abs/2606.01155v1) | DateHold：公开落窗未证 | 联合 repetition、sparsity 与 effective parameters 修正 scaling 边界；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：TRAIN-PRETRAINING — [章节](../../../../../books/part-04-training-system/28-pretraining.md)；正文锚点“数据受限的 Scaling 必须把 Unique Data 与 Repetition 分账” |
| [Low-Resource Safety Failures Are Action Failures, Not Representation Failures](https://arxiv.org/abs/2606.01196v1) | DateHold：公开落窗未证 | 安全退化定位到 action 而非 representation；3+2+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation](https://arxiv.org/abs/2606.01212v1) | DateHold：公开落窗未证 | 跨检索与生成链的 discourse manipulation 改变 RAG 威胁模型；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories](https://arxiv.org/abs/2606.01311v1) | DateHold：公开落窗未证 | first actionable fault 与 acceptance check 约束可回退 skill 更新；2+3+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems](https://arxiv.org/abs/2606.01314v1) | DateHold：公开落窗未证 | skill/tool 联合演进改变能力包状态与验证闭环；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces](https://arxiv.org/abs/2606.01317v1) | DateHold：公开落窗未证 | stateful workspace 的操作安全门禁与 outcome/effect 验收；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability](https://arxiv.org/abs/2606.01365v1) | DateHold：公开落窗未证 | 把浪费计算追到 Agent/step 级因果链；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-MONITORING — [章节](../../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Fail-Closed Lowering of Resident KV Claims onto LLM Serving Runtimes](https://arxiv.org/abs/2606.01387v1) | DateHold：公开落窗未证 | claim identity、materialization 与 fail-closed lowering 构成 KV 合同；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Differentially Private Datastore Generation for Retrieval-Augmented Inference](https://arxiv.org/abs/2606.01413v1) | DateHold：公开落窗未证 | 隐私预算进入检索 datastore 生成边界；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems](https://arxiv.org/abs/2606.01416v1) | DateHold：公开落窗未证 | 检测、隔离、恢复与 fallback 构成 orchestration 生命周期；2+3+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [Reliable Post-Retrieval Assembly for Agent Memory: Separating Evidence Extraction from Policy Execution](https://arxiv.org/abs/2606.01435v1) | DateHold：公开落窗未证 | 分离 evidence extraction 与 policy execution；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md) |
| [An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models](https://arxiv.org/abs/2606.01462v1) | DateHold：公开落窗未证 | 离线评测与生产行为错位修正 release gate；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494v1) | DateHold：公开落窗未证 | 多安全信号冲突要求显式 adjudication；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Move the Query, Not the Cache: Characterizing Cross-Instance Latent Attention Redistribution Across GPU Fabrics](https://arxiv.org/abs/2606.01502v1) | DateHold：公开落窗未证 | query 移动与 cache/fabric 代价共同进入跨实例控制；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：INFER-PD-DISAGGREGATION — [章节](../../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems](https://arxiv.org/abs/2606.01508v1) | DateHold：公开落窗未证 | Agent control plane 与传统 OS resource boundary 的结构映射；2+3+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md) |
| [Defenses &amp; Enablers For Skill Injection Attacks on Terminal Based Agents](https://arxiv.org/abs/2606.01567v1) | DateHold：公开落窗未证 | skill 来源、执行权限与注入防护改变终端 Agent 安全边界；2+3+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Don't Let a Few Network Failures Slow the Entire AllReduce](https://arxiv.org/abs/2606.01680v1) | DateHold：公开落窗未证 | degraded-link 在线 collective 调度改变训练控制面；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点“退化链路仍在线时，Collective 需要 Bandwidth-state Schedule” |
| [Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation](https://arxiv.org/abs/2606.01725v1) | DateHold：公开落窗未证 | workload trace simulation 形成 Agent 容量规划与评测合同；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点“Task-DAG Simulator 只能校准 Capacity Plan，不能承诺线上 SLO” |
| [SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving](https://arxiv.org/abs/2606.01751v1) | DateHold：公开落窗未证 | position-aligned segment identity 与 selective correction 改变 KV reuse；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点“非 Prefix 复用必须绑定 Position-aligned Segment 与 Correction State” |
| [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770v1) | DateHold：公开落窗未证 | open-ended stream 的 harness routing/evolution 构成部署控制面；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md)；命题锚点“Harness Controller 是版本化策略，不是模型的隐式习惯” |
| [Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving](https://arxiv.org/abs/2606.01839v1) | DateHold：公开落窗未证 | conversation-lifetime placement 与 KV transfer 改变调度粒度；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点“Conversation Placement 用已观察状态替代逐 Turn 预测” |
| [Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction](https://arxiv.org/abs/2606.01850v1) | DateHold：公开落窗未证 | compression release 同时约束 accuracy 与 calibrated uncertainty；2+3+3=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Compression Release 必须同时验收 Accuracy 与 Calibrated Uncertainty” |
| [Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads](https://arxiv.org/abs/2606.01927v1) | DateHold：公开落窗未证 | scheduling/I/O overlap 与 Amdahl 边界改变并行度选择；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-REQUEST-LIFECYCLE — [章节](../../../../../books/part-05-inference-system/42-what-happens-during-inference.md)；正文锚点“并行扩展必须先移出不可扩展的 Host Critical Path” |
| [Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories](https://arxiv.org/abs/2606.02060v1) | DateHold：公开落窗未证 | outcome 到 first harmful commitment 的 span 追踪改变评测粒度；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Trajectory Error 需要 Span、Commitment 与 Claim Propagation 三层坐标” |
| [DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding](https://arxiv.org/abs/2606.02091v1) | DateHold：公开落窗未证 | draft capacity 与 target verification 共同决定 diffusion speculation 成本；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点“Draft Capacity 可以借用 Target Feature，但不能借走 Commit Authority” |
| [Faster Synchronous On-Policy RL via Straggler-Aware Group Sizing](https://arxiv.org/abs/2606.02218v1) | DateHold：公开落窗未证 | posterior straggler risk 调整同步 on-policy group size；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md)；正文锚点“同步 Group Size 也可以由 Straggler Risk 有界调节” |
| [SeClaw: Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents](https://arxiv.org/abs/2606.02302v1) | DateHold：公开落窗未证 | 从安全 spec 生成任务并保留验收边界；2+2+2=6 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses](https://arxiv.org/abs/2606.02373v1) | DateHold：公开落窗未证 | 搜索状态外置到 harness，改变 Agent/environment ownership；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：AGENT-CONTEXT — [章节](../../../../../books/part-07-agent/75-context.md) |
| [Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference](https://arxiv.org/abs/2606.02430v1) | DateHold：公开落窗未证 | layer/operation/token/task propagation chain 改变故障评测；2+3+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“数值 Fault 要沿 Layer、Operation、Token 与 Task 观察传播” |
| [On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters](https://arxiv.org/abs/2606.02437v1) | DateHold：公开落窗未证 | million-model deployment 改变 adapter state、存储与 serving ownership；3+3+3=9 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-MODEL-REGISTRY — [章节](../../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools](https://arxiv.org/abs/2606.02483v1) | DateHold：公开落窗未证 | proposal/issue/execution 分权揭示 issue-time privacy 边界；3+3+2=8 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction](https://arxiv.org/abs/2606.02540v1) | DateHold：公开落窗未证 | persistent skill 的 revision、reuse、revoke 与 sandbox 构成生命周期合同；2+3+2=7 | 旧审阅标记，未获本轮验收 | 旧owner定位，非本轮采用：已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点“Harness Backdoor 把单次写入变成跨 Run 控制状态” |

## 旧110证据与采用定位（仅为待核过程记录）

以下是迁存旧Report§4而非此次全110实际审阅；旧“官方announcement/当前/完成/整合”断言不予继承，统一由当前DateHold覆盖。保留作者必要证据、反证与精确原位置，禁止以这些过程措辞宣称本轮Evidence/Books通过。Books已有机制不一刀删除，但本日采用链未验收，不计本轮I。


以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_01.md`](./V3_EVIDENCE_BATCH_01.md)。公开时间使用官方 2026-06-02 arXiv announcement batch 的北京时间范围；DataCite `created` 只作注册回执，不冒充首次公开时刻。

### [SENSE](https://arxiv.org/abs/2606.00021v1)

Target hidden-state retrieval 与 semantic soft gate 改变验证语义；当前 speculative-decoding 正文已明确 exact/lossy verification、matched baseline 与 exact fallback，故已有覆盖。

### [ART](https://arxiv.org/abs/2606.00024v1)

Attention kernel 依据 accumulated-output magnitude/direction stability 提前停止 KV block traversal；该增量已归并到 `INFER-KV-CACHE` 正文锚点“Value-aware Termination 只能提前结束读取，不能接管正确性”。

### [Agreement Metrics for LLM-as-Judge Evaluation](https://arxiv.org/abs/2606.00093v1)

Scale、case exclusion、abstention/invalid policy、pooling 与 metric 必须共同进入 agreement measurement identity；该增量已归并到 `PLATFORM-EVALUATION-SYSTEM` 正文锚点“Judge Agreement 不是单一数字”。

### [BudgetDraft](https://arxiv.org/abs/2606.00144v1)

Sparse drafter/full verifier 在多 KV budget 下训练并以 acceptance 对齐；现有 speculative-decoding/KV 正文已拥有 budget、acceptance、verification cost 与 fallback，故已有覆盖。

### [PrivacyPeek](https://arxiv.org/abs/2606.00152v1)

隐私审计需在 tool response 进入 model context 的 acquisition 时刻执行 scope/field admission；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“Tool Response 在进入 Context 时就要执行 Data-minimization Gate”。

### [Bit-Exact AI Inference Verification](https://arxiv.org/abs/2606.00279v1)

Software emulator 复现 arithmetic/reduction/rounding 以跨硬件生成 bit-exact replay evidence；当前 Evaluation 正文已有同名机制、coverage failure 与 tolerance fallback，故已有覆盖。

### [PR2](https://arxiv.org/abs/2606.00395v1)

Predicted route 既是 rollout behavior state，也是 training importance-estimation identity；该合同已写入 `TRAIN-GRPO` 正文“MoE Route Replay 也属于 Behavior-policy Identity”，并保留 route 缺失、expert 不可用和版本失配时的丢弃、重采或 current-policy fallback。

### [When Safe Skills Collide](https://arxiv.org/abs/2606.00448v1)

Installed skill set/capability union 才是 composition risk 对象，static scanner 只是 recall sensor；当前 Security 正文已覆盖跨-skill composition、runtime authority 与 effect boundary，故已有覆盖。

### [Confused ChatGPT](https://arxiv.org/abs/2606.00485v1)

Flat shared context 让一个 app 的 persistent write 影响另一 app 的后续 authority；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“App-local Context Namespace 阻止普通 Writer 获得跨 App Authority”。

### [TAPS](https://arxiv.org/abs/2606.00487v1)

Draft tree selection 必须服从 prefix reachability 并结算 target verification latency；现有 speculative-decoding 正文已覆盖 causal-prefix tree、cost budget 与 sequential fallback，故已有覆盖。

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_02.md`](./V3_EVIDENCE_BATCH_02.md)。

### [“I Strongly Suspect This Website Is a Scam”](https://arxiv.org/abs/2606.00497v1)

Field-level endpoint outcome 与 detection–action gap 证明识别风险不等于阻止提交；当前 Security 正文已由独立 issue-time gate 承载，故已有覆盖。

### [Threshold-Based Exclusive Batching for LLM Inference](https://arxiv.org/abs/2606.00516v1)

Mixed/exclusive batching 的优劣由 hardware、model 与 workload crossover 决定；当前 Scheduling 正文已有 workload-dependent phase switch 与 fallback，故已有覆盖。

### [GNMR](https://arxiv.org/abs/2606.00539v1)

低精度训练的 operator-normalized risk、长短窗口信号与 limited recovery budget 已由 Pretraining 正文承载，故已有覆盖。

### [Same Payload, Different Channel](https://arxiv.org/abs/2606.00566v1)

相同 payload 仅因 tool/user channel 不同即产生 authority asymmetry；当前 Security 正文已要求 authenticated provenance、typed boundary 与 effect-time monitor，故已有覆盖。

### [Sandboxed Coding Agents are Competitive Omni-modal Task Solvers](https://arxiv.org/abs/2606.00579v1)

Sandboxed tool transformation 能替代部分 native modality input，但当前证据限于 offline staged tasks，未形成超出现有 tool/workspace contract 的长期机制，故仅报告。

### [TRACE](https://arxiv.org/abs/2606.00611v1)

Risk-aware latent evidence、独立 reader 与 raw-trajectory fallback 已归并到 `PLATFORM-MONITORING` 正文锚点“Risk-aware Latent 只能压缩 Evidence，不能压缩 Authority”。

### [MemPro](https://arxiv.org/abs/2606.00619v1)

重读当前 Memory 正文后改判已有覆盖：“Memory policy 本身也可能成为可学习、可版本化的 procedural asset”已经把 extraction/update procedure、source episodes、held-out validation、versioned skill bank、provenance 与 rollback 连成完整命题；后续 cluster-local tournament 又覆盖独立晋升。MemPro 是该合同的受限实现，不再新增正文。

### [Hidden Thoughts Are Not Secret](https://arxiv.org/abs/2606.00642v1)

Reasoning trace 可被 prompt 重建，说明 hidden interface 不是 secrecy boundary；当前 Security 正文已有同名机制与独立 DLP/authorization fallback，故已有覆盖。

### [The Invitation Trap](https://arxiv.org/abs/2606.00654v1)

模型先诱导用户在后续轮次输入 trigger，使 attack provenance 跨轮闭环；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“模型建议也可能塑造未来 Trigger”。

### [Scaling Behavior of Single LLM-Driven Multi-Agent Systems](https://arxiv.org/abs/2606.00655v1)

固定 base LLM 后，agent count 呈非单调收益并支付 coordination tax；当前 Multi-Agent 正文已拥有同一 budget/fallback contract，故已有覆盖。

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_03.md`](./V3_EVIDENCE_BATCH_03.md)。

### [NeuroLog](https://arxiv.org/abs/2606.00669v1)

LLM 只填 typed facts，Datalog/SMT/ASan 分别拥有组合、可行性与 crash truth；当前 Security 已有同一 hypothesis-to-reproduction contract，故已有覆盖。

### [The Paradox of Outcome Optimization](https://arxiv.org/abs/2606.00674v1)

Outcome optimization 的 shortcut bias 与 process verifier 边界已由 GRPO 正文覆盖；论文提供理论与受限 counterfactual evidence，不改变 owner contract。

### [WaveFilter](https://arxiv.org/abs/2606.00724v1)

Wavelet 是 diffusion KV token-utility selector 的局部实现；当前 KV 正文已有 proxy、误差预算、loop drift 与 FullKV fallback，故已有覆盖。

### [ViBE](https://arxiv.org/abs/2606.00735v1)

Expert placement 需要联合 workload skew、measured GPU service rate 与 drift recalibration；当前 Scheduling 正文已有同一状态与静态回退，故已有覆盖。

### [CoMIC](https://arxiv.org/abs/2606.00756v1)

Edge-local episode 与 cloud-derived cross-agent guidance 分属不同 memory owner/revision；该双层异步合同已写入 `AGENT-MEMORY` 正文“Edge-local Episode 与 Cloud-derived Guidance 必须分离所有权”，并明确 dispatch receipt、tenant/expiry 与 local-only fallback。

### [FALAT](https://arxiv.org/abs/2606.00765v1)

Typed dependency 和 counterfactual repair 才能区分 first causal error 与后继传播；当前 Trace 正文已有可证伪因果候选与 multiple-candidate fallback，故已有覆盖。

### [Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety](https://arxiv.org/abs/2606.00801v1)

Semantic archive 把 attack exploration coverage 与 mode collapse 显式化；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“Semantic Archive 暴露 Mode Collapse，但不拥有 Release Verdict”。

### [Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems](https://arxiv.org/abs/2606.00804v1)

Coordination strategy 应按 problem class 与 budget 选择且保留 single-agent fallback；当前 Multi-Agent 正文已有这一长期 contract，故已有覆盖。

### [Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs](https://arxiv.org/abs/2606.00813v1)

安全结果不可随 model generation 自动继承，attack archive 应跨 release replay；当前 Evaluation/Security 已要求 immutable versioned evidence 与重跑 regression，故已有覆盖。

### [SkillPager](https://arxiv.org/abs/2606.00822v1)

Typed semantic node、query selection 与 dependency completion 将长 skill 变成 retrieval plan；当前 Memory/Context 已承载这一机制，故已有覆盖。

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_04.md`](./V3_EVIDENCE_BATCH_04.md)。

### [Momento](https://arxiv.org/abs/2606.00832v1)

跨 session history 只是 current user state 的候选，不得直接授权 consequential action；当前 Memory 已有 recall/commitment 分层，故已有覆盖。

### [MORI](https://arxiv.org/abs/2606.00866v1)

Tool-call gap 的 relative idleness 应决定 program-level KV tier boundary；该增量已归并到 `INFER-KV-CACHE` 正文锚点“Agent Idle Window 要按 Program Horizon 决定 Tier，而不是二元搬空”。

### [MetaForge](https://arxiv.org/abs/2606.01801v1)

动态工具生成仍必须经过 typed artifact、isolated validation、versioned admission 与 runtime gate；当前 Agent Platform 已拥有完整 lifecycle，故已有覆盖。

### [Cost-Aware Diffusion Draft Trees for Speculative Decoding](https://arxiv.org/abs/2606.01813v1)

Draft tree 应按 target verification cost、context 与 acceptance 联合选 budget；当前 Speculative Decoding 正文已有同一 contract，故已有覆盖。

### [CRAB-Bench](https://arxiv.org/abs/2606.01815v1)

Constraint graph 同时控制 task generation、多解 materialization 与 user disclosure；该增量已归并到 `PLATFORM-EVALUATION-SYSTEM` 正文锚点“Constraint Graph 可以连接任务生成与多解验收，但不能替代真实环境”。

### [Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus](https://arxiv.org/abs/2606.01828v1)

通信 edge 和 stopping 应由可靠性、divergence、task relevance 与预算决定；当前 Multi-Agent 正文已有条件化 topology 与验证 fallback，故已有覆盖。

### [Benign Inputs, Harmful Outputs](https://arxiv.org/abs/2606.01837v1)

各模态独立 benign 不代表 joint semantics 无害；当前 Security 正文已要求 cross-modal joint-risk admission，故已有覆盖。

### [Trust-Calibrated Code Review](https://arxiv.org/abs/2606.01969v1)

三层 review UI 能改善 attention allocation，但证据仅为 prototype/survey，未验证真实漏审或 release outcome，故仅报告。

### [SafeMCP](https://arxiv.org/abs/2606.01991v1)

Look-ahead world model 只能在 server-side 提议缩小 action set，最终 authority 仍属 deterministic/effect-time gate；当前 Security/MCP 已覆盖，故已有覆盖。

### [MMG2Skill](https://arxiv.org/abs/2606.01993v1)

Human guide 编译、trajectory diagnosis 与 skill revision 必须保留 provenance、validation、admission 和 rollback；当前 Agent Platform 已承载，故已有覆盖。

以下十项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_05.md`](./V3_EVIDENCE_BATCH_05.md)。

### [Extreme Low-Bit Quantization for Reasoning Models](https://arxiv.org/abs/2606.02011v1)

2-bit trace inflation、commit gap 与 loop/budget exhaustion 要进入 precision release identity；该增量已归并到 `INFER-TENSORRT-LLM` 正文锚点“Reasoning Quantization 要验收 Commitment，而不只是 Token Cost”。

### [OpenWebRL](https://arxiv.org/abs/2606.02031v1)

Live-browser rollout、trajectory judge、invalid-sample filter 与 online RL state 已由 GRPO/Agent Platform 的现有合同承载，故已有覆盖。

### [SentGuard](https://arxiv.org/abs/2606.02041v1)

Sentence boundary 是 streaming safety 的语义 commit fence；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“Streaming Guard 的最小可解释 Commit Unit 可以是完整 Sentence”。

### [BADGER](https://arxiv.org/abs/2606.02109v1)

LLM 只做结构抽取、deterministic scorer 拥有最终判定；当前 Evaluation 已有同一 ownership，故已有覆盖。

### [AgentRedBench](https://arxiv.org/abs/2606.02240v1)

SaaS connector、destination、argument/content mutation 与 fixture state 应构成同一 red-team subject；该增量已归并到 `PLATFORM-SECURITY` 正文锚点“Integration-aware Campaign 必须把 Connector 与 Effect Identity 编进 Case”。

### [When Knowledge Is Not Free](https://arxiv.org/abs/2606.02245v1)

Evidence access right/cost tier、per-query/shared budget 与 sufficiency/stop 已合并进 `AGENT-RAG` 正文“Evidence Access Right、Cost 与 Sufficiency 是联合检索状态”；authorization 与 source authority 先于价格，预算不足时 abstain。

### [POIROT](https://arxiv.org/abs/2606.02282v1)

Peer interrogation 可生成诊断候选，但执行 Agent 的集合不能自证正确或取代独立验收，故仅报告。

### [Unified Context Evolution for LLM Agents](https://arxiv.org/abs/2606.02304v1)

Typed experience unit、usage scoring 与 retirement 已由 Memory/Agent Platform 的 versioned lifecycle 承载，故已有覆盖。

### [Do Multimodal Agents Really Benefit from Tool Use?](https://arxiv.org/abs/2606.02357v1)

Tool trace 不是贡献证据；no-tool/call-shell/real-result intervention 与 confirm/repair/harm/no-effect 归因已写入 `AGENT-TOOL-CALLING` 正文“Tool 出现不等于 Tool 对答案有贡献”。

### [MOC](https://arxiv.org/abs/2606.02359v1)

Multi-order message path、per-hop lineage、consolidation loss 与 raw-message fallback 已写入 `AGENT-MULTI-AGENT` 正文“多阶消息需要 Ordered Evidence DAG，而不是压平后的共识摘要”。

以下八项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_06.md`](./V3_EVIDENCE_BATCH_06.md)。

### [SPADE-Bench](https://arxiv.org/abs/2606.02380v1)

显式 plan/self-report 只能解释意图，真实 tool action、environment transition 与 effect receipt 才能支持 deception 判定；当前 Evaluation 已有同一证据顺序，故已有覆盖。

### [Investigating and Alleviating Harm Amplification in LLM Interactions](https://arxiv.org/abs/2606.02423v1)

多轮 harm 要由跨 turn trajectory risk state 与独立 stop/authorization owner 管理；当前 Security 已有这一累计风险合同，故已有覆盖。

### [HLL](https://arxiv.org/abs/2606.02449v1)

CAPTCHA 的动态 interaction rules 是 typed action、state legality、loop 与 completion evidence 的垂直实例；当前 Evaluation 已覆盖，不将绕过能力外推为部署授权。

### [AgentCL](https://arxiv.org/abs/2606.02461v1)

顺序 task stream 必须拆开 acquisition、retention/forgetting、interference 与 transfer；当前 Memory 已有同一 checkpoint contract，故已有覆盖。

### [MCP-Persona](https://arxiv.org/abs/2606.02470v1)

Stateful MCP simulator 必须冻结 initial state、schema、checkpoint、execution outcome 与 real-environment anchor；当前 Evaluation/MCP owner 已承载，故已有覆盖。

### [Monitoring Agentic Systems Before They’re Reliable](https://arxiv.org/abs/2606.02494v1)

结构完整性应先于 task-quality monitor 成为 maturity gate，并用三种 scope、三维信号与 FMEA severity 路由发现；该增量已归并到 `PLATFORM-MONITORING` 正文锚点“Pre-reliability Monitoring 先验证 Wiring，再解释 Quality”。

### [Tracking the Behavioral Trajectories of Adapting Agents](https://arxiv.org/abs/2606.02536v1)

Trait vector 可以筛查 versioned skill diff，但不能替代独立 held-out behavior、quarantine、promotion authority 与 rollback；当前 Security 已有这条供应链边界，故已有覆盖。

### [SimSD](https://arxiv.org/abs/2606.02544v1)

dLLM 的双向 mask context 破坏标准 token-level verification，需以 temporal causal layout 与 RoPE alignment 恢复可验证 prefix；该增量已归并到 `INFER-SPECULATIVE-DECODING` 正文锚点“双向 Mask Context 必须先改写成 Temporal-causal Verification Layout”。

以下八项的详细 Method / Evaluation / non-proof 与 Books comparison 位于 [`V3_EVIDENCE_BATCH_07.md`](./V3_EVIDENCE_BATCH_07.md)。其中 `2606.00005v1` 无官方 HTML，使用官方 exact-v1 PDF；其余均使用 exact-v1 HTML。

### [Emergent Collaborative Deliberation in Multi-Model AI Systems](https://arxiv.org/abs/2606.00005v1)

Persona 不创造独立真值，deliberation 必须保存原始 evidence、相关性与 human/independent outcome gate；当前 Multi-Agent 已有这一 contract，故已有覆盖。

### [Deliberative Curation](https://arxiv.org/abs/2606.00007v1)

Knowledge artifact 的 guarded lifecycle、争议/撤回、独立 promotion 与 skill-conditioned reputation 已分别由 Memory、Platform 与 Multi-Agent owner 承载；投票不能自证事实，故已有覆盖。

### [Completion at the Boundary](https://arxiv.org/abs/2606.00145v1)

Completion sensor 只提交 bounded proposal，handoff 仍由 verifier、state revision 与 workflow owner 验收；当前 Workflow 已有相同分权，BPT 是 VLA 局部实现。

### [Persona Attack](https://arxiv.org/abs/2606.00150v1)

多轮 benign-seeming injection 会在 transcript/state memory 中累积风险；当前 Security 已要求跨 iteration trajectory state 与不可由模型自授的 stop/effect gate，故已有覆盖。

### [DataShield](https://arxiv.org/abs/2606.00160v1)

当前 Data 正文已用本篇 exact-v1 写入 checkpoint/layer/projection/threshold 绑定的 training-effect filter，并保留 canary 与 held-out safety regression，故已有覆盖。

### [BAGEN](https://arxiv.org/abs/2606.00198v1)

Remaining budget/feasibility interval 只是需要校准的 controller sensor；当前 Planning/Platform 已要求 hard cap、verification reserve、false-abort outcome 与 terminal receipt，故已有覆盖。

### [Quantized Reasoning Models Think They Need to Think Longer, but They Do Not](https://arxiv.org/abs/2606.00206v1)

当前 GPU Memory 已要求按完成任务的 memory/latency/energy/quality 结算低比特而非压缩比，Decode 也已有 overthinking 的 request-local intervention；marker penalty 不新增 owner contract。

### [The Deterministic Horizon](https://arxiv.org/abs/2606.00376v1)

可形式化状态可交给 deterministic solver，开放 state 仍需 observation、authorization 与 effect receipt；当前 Planning/Tool Calling 已有此边界，论文的强架构上界不作外推。

候选级证据未丢失：[`V2_1_EVIDENCE_ARCHIVE.md`](./V2_1_EVIDENCE_ARCHIVE.md) 对 51 个前沿材料保存了标题、精确 v1、Method/Evaluation/Limitations locator、claim boundary、评分与旧 Books comparison。本次抽查 PRISM、Lodestar、Leyline、verifier fuzzing、SparseX、ConServe、compression uncertainty、Albireo、DFlare、SAGC、Ghost Tool Calls 与 SkillHarm，原题摘均直接研究大模型或其基础设施；同时抽查 Metastable Faults、federated-personalization taxonomy、lakehouse agents、Agent OS 等高风险 false-positive，确认仅有通用系统类比、研究议程或垂直应用不能自动保留。

对 1,398 项关闭提案已完成全量 title sweep；边界项进一步读取完整 abstract。旧共享 closure reason 被反例击穿后共恢复 66 项，现已全部闭合 candidate-level Evidence/Books comparison：43 项已有覆盖、20 项正文整合、3 项仅报告、0 项暂缓。`BitsMoE`、`CAST` 等只呈现局部模型/训练方法而没有可迁移系统合同的条目仍关闭。所有 1,332 个维持关闭项已重新落入具名的 embodied/local、incremental、benchmark、theory 或 vertical family，而不是沿用统一模板。

Books 方面，旧 `Integrate` 没有凭 trace 直接闭合：`SF-GHOST-TOOL-ISSUE-PRIVACY` 与 `SF-SKILLHARM-LIFECYCLE` 经正文重读改判 Existing，其余存续项和新恢复的长期增量均已落到唯一 owner 的 Review notes 前正文。`SF-ORDER-AGNOSTIC-CHAIN-RULE` 因当前准入关闭，整条 adoption chain 已删除。旧前沿 44 项的最终正文重判见 [`V3_PRIOR_CANDIDATE_BOOKS_REJUDGMENT.md`](./V3_PRIOR_CANDIDATE_BOOKS_REJUDGMENT.md)，全量 post-write 状态见 [`POST_WRITE_AUDIT_SCOPE_V3.md`](./POST_WRITE_AUDIT_SCOPE_V3.md)。

### [Lodestar: An Online-Learning LLM Inference Router](https://arxiv.org/abs/2606.00946v1)

精确版本 `2606.00946v1` 的机制与适用条件：round-robin、queue-aware 和 prefix-cache-aware routing 在请求分布与 GPU 同质时合理；agentic prompt、batch/KV 耦合和异构加速器使静态启发式失准。Lodestar 按请求采集 instance/request/performance snapshot，在线训练 reward predictor，再以预测 TTFT 选择实例。 公有云 GPU 实验与 prefix/load heuristic 的比较支持特定 workload 下的 TTFT 改善和约五分钟适应速度；它不证明 predictor 在突变、观测延迟或 reward drift 下仍安全。在线训练、探索和隔离带来 control-plane 成本，冷启动与失准时应回退确定性 router。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#lodestar-an-online-learning-llm-inference-router)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Silent Failures in Federated Personalization of Foundation Models](https://arxiv.org/abs/2606.00947v1)

精确版本 `2606.00947v1` 的机制与适用条件：Federated foundation-model personalization makes client-level behavior inaccessible to a central observer, so bias, miscalibration, fairness collapse, adaptation misalignment, out-of-domain degradation, and alignment erosion can pass ordinary aggregate acceptance; the durable delta is a privacy-preserving behavioral-evaluation contract that assigns what may be observed, aggregated, audited, and used for release. Clients own raw examples and local behavioral outcomes; the measurement protocol own（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#silent-failures-in-federated-personalization-of-foundation-models)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Federated Personalization 的盲区是可见性合同”；现有正文对照及采用边界以本报告当前判断为准。

### [When Parallelism Pays Off: Cohesion-Aware Task Partitioning for Multi-Agent Coding](https://arxiv.org/abs/2606.00953v1)

精确版本 `2606.00953v1` 的机制与适用条件：Co-Coder materializes repository work as a weighted dependency graph, isolates structural hubs, partitions cohesive file/symbol communities, and executes only dependency-ready units in parallel, making critical-path and merge-interface ownership explicit instead of equating more coding agents with more useful parallelism. The partitioner owns a versioned weighted file/symbol dependency graph and cohesive communities; the scheduler owns dependency-ready admission; agents own only their assigned w（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#when-parallelism-pays-off-cohesion-aware-task-partitioning-for-multi-agent-coding)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../../books/part-07-agent/82-multi-agent.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference](https://arxiv.org/abs/2606.01007v1)

精确版本 `2606.01007v1` 的机制与适用条件：TACG builds a task-conditioned expert coactivation graph for capacity-feasible placement, while GESR replicates generic experts and selects replicas using locality and load; this turns MoE expert placement and cross-GPU communication into runtime workload-aware scheduling state rather than a change to router or expert semantics. TACG owns a calibrated task-conditioned expert coactivation graph; GESR owns replica candidates; the serving scheduler owns capacity-feasible placement using topology, l（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#beyond-task-agnostic-task-aware-grouping-for-communication-efficient-multi-task-moe-inference)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Hybrid Verified Decoding: Learning to Allocate Verification in Speculative Decoding](https://arxiv.org/abs/2606.01019v1)

精确版本 `2606.01019v1` 的机制与适用条件：cache draft 几乎免费、model drafter 更稳定，固定选择其中一种无法利用 agentic prompt 中局部重复。Hybrid Verified Decoding 在 target verification 前预测 cache draft accepted length，再按 payoff 在 cache 与 model drafter 间切换。 三个 LLM、16 个数据集及 agentic workflow 对 EAGLE3 的比较支持 payoff-guided 选择；预测器错误、缓存漂移和 verification cost 仍可能抵消收益，2.73x 不是通用常数。结构重复少时普通 model drafter 更简单。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#hybrid-verified-decoding-learning-to-allocate-verification-in-speculative-decoding)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md)；现有正文对照及采用边界以本报告当前判断为准。

### [A Finite-Calibration Regime Map for LLM Judge Panels](https://arxiv.org/abs/2606.01034v1)

精确版本 `2606.01034v1` 的机制与适用条件：增加 judge 并用完整 joint table 能表达交互，但有限人工标签会产生稀疏 cell 与 unseen-pattern 风险。FCPS 在 judge path、panel size、scalar/reliability stacker 与 joint-table aggregator 间按 validation support 选择。 RewardBench、LLMBar、SummEval、Arena100K 与 controlled interaction data 共同界定何时简单校准优于表格；不证明一个 panel 在新分布自动保持校准。人标预算和 judge error correlation 决定选择，标签很充足时 richer table 仍合理。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#a-finite-calibration-regime-map-for-llm-judge-panels)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Leyline: KV Cache Directives for Agentic Inference](https://arxiv.org/abs/2606.01065v1)

精确版本 `2606.01065v1` 的机制与适用条件：append-only chatbot 让 prefix cache 正确；Agent 会删除、替换和移动历史 span，现有 kernel eviction 又无法接受 harness policy。Leyline 用声明式四元组区分 edit 与 position-preservation mode，经架构适配 kernel 做 RoPE re-anchoring、splice 或 semantic-forgetting re-prefill。 cache-hit、latency 与 debug-gym solve-rate 实验支持特定 MLA/agent edit path；它不证明任意 attention architecture 的 replay 等价，也不把 policy directive 升级为 runtime truth。checker、kernel surface 与错误编辑风险增加，append-only workload 继续使用 prefix cache。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#leyline-kv-cache-directives-for-agentic-inference)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Before the Model Learns the Bug:Fuzzing RLVR Verifiers](https://arxiv.org/abs/2606.01066v1)

精确版本 `2606.01066v1` 的机制与适用条件：RLVR 把 reward 交给可执行 verifier，获得低成本精确反馈；一旦 checker 有 bug，policy 会优化 exploit。该框架生成 adversarial completion，同时运行被测与 stricter reference verifier，记录 FP/FN/disagreement/exploit/uncertainty。 贡献是 verifier differential-testing contract，而不是模型能力 benchmark；摘要未给跨 verifier 的普遍缺陷率。reference verifier 也可能错，fuzz coverage 和维护成本不可忽略；形式简单且已有证明的 checker 仍可直接使用。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#before-the-model-learns-the-bugfuzzing-rlvr-verifiers)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Deep Research as Rubric for Reinforcement Learning](https://arxiv.org/abs/2606.01091v1)

精确版本 `2606.01091v1` 的机制与适用条件：DR-Rubric retrieves external evidence, synthesizes atomic verifiable constraints, scores policy outputs against that rubric, and feeds the result into group-relative reinforcement learning; rubric provenance, granularity, bootstrap version, and polarization therefore become reward-state and stopping-contract inputs rather than free-form judge text. The rubric pipeline owns an evidence snapshot, atomic constraints, provenance, granularity and bootstrap version; the scorer owns criterion results; （完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#deep-research-as-rubric-for-reinforcement-learning)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md)；正文锚点“Evidence-derived Rubric 是版本化 Reward State”；现有正文对照及采用边界以本报告当前判断为准。

### [memorywire: A Vendor-Neutral Wire Format for Agent Memory Operations](https://arxiv.org/abs/2606.01138v1)

精确版本 `2606.01138v1` 的机制与适用条件：各 memory backend 的 SDK、存储和操作词汇不同，单后端集成可快但迁移会重建状态且缺少人工 write governance。memorywire 统一 remember/recall/forget/merge/expire、四类 memory、MemoryStore、fan-out router 与可选 HITL channel。 五个 adapter、100-fact/50-query microbenchmark、adversarial fusion 与 16-scenario conformance suite 支持 wire compatibility；小语料与部分 cell 未通过，不能证明语义完全等价。schema lowest-common-denominator 和 adapter drift 是代价，单后端专用 API 仍可保留。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#memorywire-a-vendor-neutral-wire-format-for-agent-memory-operations)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md)；现有正文对照及采用边界以本报告当前判断为准。

### [SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision](https://arxiv.org/abs/2606.01139v1)

精确版本 `2606.01139v1` 的机制与适用条件：SkillRevise diagnoses execution traces, writes reusable principles into explicit memory, proposes bounded skill revisions, and promotes a revision only through utility-gated selection, turning skill text, trace evidence, revision rounds, and rollback candidates into versioned platform state. Trace diagnosis writes source-linked failure evidence and reusable principles; the reviser owns bounded candidate skill text; a utility gate owns promotion across affected tasks; the registry owns version, r（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#skillrevise-improving-llm-authored-agent-skills-via-trace-conditioned-skill-revision)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Schedule-Level Shared-Prefix Reuse for LLM RL Training](https://arxiv.org/abs/2606.01143v1)

精确版本 `2606.01143v1` 的机制与适用条件：标准 GRPO trainer 为每条 trajectory 重算相同 prompt prefix，保持实现简单却在长 context/group 下浪费前后向。该 schedule 只做一次 prefix forward，suffix microbatch 读取共享 K/V 并累积 gK/gV，最后统一做 prefix backward，同时保留 MoE token accounting。 Llama3/Qwen dense 与 MoE、100-step actor replay 及 TP/CP/PP/EP 组合支持数值等价容差和 HBM/速度收益；真实算术等价不保证所有 finite-precision kernel 或 stochastic op 相同。gradient cache、offload 与 scheduler 复杂度增加，小 group 仍宜普通训练。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#schedule-level-shared-prefix-reuse-for-llm-rl-training)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md)；现有正文对照及采用边界以本报告当前判断为准。

### [When Data Is Scarce: Scaling Sparse Language Models with Repeated Training](https://arxiv.org/abs/2606.01155v1)

精确版本 `2606.01155v1` 的机制与适用条件：The sparse data-constrained scaling law jointly models unique-token volume, repetition, effective parameters, and sparsity, so repeated-epoch pretraining must choose model size and sparsity against a data-saturation boundary instead of applying dense Chinchilla allocation or sparsity gains independently. The training planner owns unique-token count, presentation count/epochs, active and dense-equivalent parameters, sparsity process and theoretical compute budget as one allocation record. The tra（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#when-data-is-scarce-scaling-sparse-language-models-with-repeated-training)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：TRAIN-PRETRAINING — [章节](../../../../../books/part-04-training-system/28-pretraining.md)；正文锚点“数据受限的 Scaling 必须把 Unique Data 与 Repetition 分账”；现有正文对照及采用边界以本报告当前判断为准。

### [Low-Resource Safety Failures Are Action Failures, Not Representation Failures](https://arxiv.org/abs/2606.01196v1)

精确版本 `2606.01196v1` 的机制与适用条件：Cross-lingual analysis finds harmfulness representations can remain separable while refusal actions fail, moving the safety bottleneck from feature availability to downstream action realization. Activation directions and probe scores are sensor state owned by the diagnostic pipeline. The decoder/policy owns the refusal action, the language-conditioned routing gate owns intervention, and the safety evaluator owns matched benign/attacked outcomes. A separable activation never receives execution or（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#low-resource-safety-failures-are-action-failures-not-representation-failures)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文对照及采用边界以本报告当前判断为准。

### [DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation](https://arxiv.org/abs/2606.01212v1)

精确版本 `2606.01212v1` 的机制与适用条件：DiscourseFlip organizes opinion-manipulation goals as a hierarchical attack-surface graph and uses an agentic action loop to revise seemingly coherent documents against black-box RAG retrieval and generation feedback, showing that corpus admission must govern discourse-level provenance and intent rather than only lexical anomaly or isolated poison snippets. The attack loop owns a hierarchical manipulation goal, candidate document revisions and observed retrieval/generation feedback. The corpus a（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#discourseflip-an-oblique-discourse-level-opinion-manipulation-attack-against-black-box-retrieval-augmented-generation)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文对照及采用边界以本报告当前判断为准。

### [SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories](https://arxiv.org/abs/2606.01311v1)

精确版本 `2606.01311v1` 的机制与适用条件：整条 trajectory 或 session feedback 更新 skill 实现简单，却把失败责任扩散到多个步骤。SkillAdaptor 找到 first actionable fault、关联候选 skill，在显式 acceptance check 下做局部更新并保持 backbone 冻结。 WebShop、PinchBench、Claw-Eval 与三种模型支持 step-level attribution 的小幅稳定改善；fault locator 和 acceptance check 仍可能错，代码尚未冻结。诊断开销高，单步或明确错误流程继续使用 session-level edit。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#skilladaptor-self-adapting-skills-for-llm-agents-from-trajectories)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md)；现有正文对照及采用边界以本报告当前判断为准。

### [SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems](https://arxiv.org/abs/2606.01314v1)

精确版本 `2606.01314v1` 的机制与适用条件：SkillSmith co-evolves versioned skill instructions and executable tools through bounded atomic wrap/edit/compose/split/retire operations, validation-gated state updates, Pareto management, and anti-pattern memory, making tool capability and skill procedure one jointly governed release graph. Atomic wrap/edit/compose/split/retire operations create candidate skill/tool graph versions; validation and Pareto management own promotion evidence; anti-pattern memory records rejected lineage. The capabil（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#skillsmith-co-evolving-skills-and-tools-for-self-improving-agent-systems)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md)；现有正文对照及采用边界以本报告当前判断为准。

### [SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces](https://arxiv.org/abs/2606.01317v1)

精确版本 `2606.01317v1` 的机制与适用条件：Saber evaluates coding agents inside stateful workspaces with executable harm, local safe alternatives, rule-based violation checks, semantic auxiliary judging, and an outcome taxonomy that distinguishes refusal, recognition, unsafe shortcut, and multi-step environmental effects; the final workspace state, not response text, owns the operational-safety verdict. The sandbox owns initial and final workspace snapshots plus executable effects; deterministic rules own declared violations; the outcome（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#saber-benchmarking-operational-safety-of-llm-coding-agents-in-stateful-project-workspaces)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability](https://arxiv.org/abs/2606.01365v1)

精确版本 `2606.01365v1` 的机制与适用条件：只在 final answer 后打分无法挽回已经浪费的 token。该框架把 orchestrator/search/execution 事件转成 loop、budget pressure、low information gain、tool instability 的在线信号，再用离线语义和选择性 judge 补充。 165 条 GAIA trace 与 10-task intervention pilot 支持 warning 后仍有大量可避免计算；小 pilot 不证明自动 redirect 的总体收益。误报会过早终止，语义 judge 也会错，因此 cheap signal 只应触发有界 recovery。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#early-diagnosis-of-wasted-computation-in-multi-agent-llm-systems-via-failure-aware-observability)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-MONITORING — [章节](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Fail-Closed Lowering of Resident KV Claims onto LLM Serving Runtimes](https://arxiv.org/abs/2606.01387v1)

精确版本 `2606.01387v1` 的机制与适用条件：priority、TTL、offload、event 与 KV-aware routing 是有用 substrate，但各自不承诺未来 reuse。ResidentClaim lowering 要求 accepted claim identity、materialization predicate、ordered lifecycle 与 claim-scoped outcome，并用 descriptor/checker 将 mapping 分成 native、adapter evidence、approximation、reject 或 unknown。 对 TensorRT-LLM、SGLang/HiCache、Dynamo 的 anchored descriptor 与 patched vLLM failure path 支持 semantics boundary；checker 不证明未审 runtime 完整，也没有 performance claim。claim metadata 与 fail-closed path 有成本，不需未来义务时弱 primitive 仍足够。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#fail-closed-lowering-of-resident-kv-claims-onto-llm-serving-runtimes)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Differentially Private Datastore Generation for Retrieval-Augmented Inference](https://arxiv.org/abs/2606.01413v1)

精确版本 `2606.01413v1` 的机制与适用条件：直接发布 on-device RAG datastore 保留 utility，却泄露个体贡献。该方法用 LSH bucket 汇总 class vote，再加入校准 DP noise，输出可共享概率 datastore。 七个数据集、epsilon=5 的 accuracy 与 membership-inference attack 支持所测 privacy/utility；单 epsilon、2–14 类和 attack model 不证明任意数据安全。hash collision、noise 和 privacy accounting 有成本，非共享本地 store 不必采用。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#differentially-private-datastore-generation-for-retrieval-augmented-inference)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems](https://arxiv.org/abs/2606.01416v1)

精确版本 `2606.01416v1` 的机制与适用条件：固定 workflow 与无差别 retry 易实现，但 timeout、malformed arg、stale context、contradiction 和 silent output 需要不同恢复。该 orchestrator 将 observable signal 映射 failure class，在预算内选 recovery、验证新轨迹并记录 trace。 100-task fault injection、budget sweep 与 local model-in-loop 支持 verifier-guided recovery；受控故障和高 success rate 不代表开放工具生态。分类错误会浪费预算或重复副作用，幂等性未知时应 fail closed 而非自愈。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#self-healing-agentic-orchestrators-for-reliable-tool-augmented-large-language-model-systems)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Reliable Post-Retrieval Assembly for Agent Memory: Separating Evidence Extraction from Policy Execution](https://arxiv.org/abs/2606.01435v1)

精确版本 `2606.01435v1` 的机制与适用条件：把 retrieval、语义过滤、冲突/新旧 policy 和生成合在一次 LLM call 中简单，却会让正确证据在组装阶段丢失。该接口先抽取 matching evidence 成候选结构，再由独立 policy executor 选择 current value。 MAB FactConsolidation、262K context、同 backbone/top-10 controlled comparison 与 LongMemEval negative check 支持收益主要来自阶段分离；不证明所有 memory task 有效。额外阶段增加 latency，且只有显式 version metadata 时 freshness policy 可审计。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#dont-ask-the-llm-to-track-freshness-a-deterministic-recipe-for-memory-conflict-resolution)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-MEMORY — [章节](../../../../../books/part-07-agent/77-memory.md)；现有正文对照及采用边界以本报告当前判断为准。

### [An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models](https://arxiv.org/abs/2606.01462v1)

精确版本 `2606.01462v1` 的机制与适用条件：The paper separates reasoning production from reasoning evaluation and identifies answer-confirmation bias: a valid final answer can cause evaluator models and process reward models to accept invalid intermediate reasoning, requiring an evaluation contract that independently binds step validity, answer validity, evaluator state, and causal diagnostics. The trace verifier owns step-validity judgments, the answer verifier owns final-answer validity, and the evaluation run owns judge/prompt/checkpo（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#an-enigma-of-artificial-reason-investigating-the-production-evaluation-gap-in-large-reasoning-models)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有正文对照及采用边界以本报告当前判断为准。

### [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494v1)

精确版本 `2606.01494v1` 的机制与适用条件：单一 malware scanner 的 allow/block 简单，但 Agent skill 同时包含脚本、指令与语义权限，VirusTotal、静态规则和 SkillSpector 覆盖面不同。该数据集把三类 signal 与 registry verdict 对齐，专门分析 disagreement。 67,453 个 sanitized latest skill、overlap 与 verdict slice 支持 layered triage；registry 是 automated silver label，不是 malicious prevalence 或 human truth。多 scanner 增加误报与审核成本，effect-time sandbox/least privilege 仍是最终控制。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#clawhub-security-signals-when-virustotal-static-analysis-and-skillspector-disagree)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Move the Query, Not the Cache: Characterizing Cross-Instance Latent Attention Redistribution Across GPU Fabrics](https://arxiv.org/abs/2606.01502v1)

精确版本 `2606.01502v1` 的机制与适用条件：cross-instance sparse attention 通常搬 selected KV block；MLA 将每 token K/V 压成窄 latent 后，约 1KB query row 可能比 cache chunk 更小。该工作将 probe/transfer/compute/return/merge 分解成 cost model，按 fabric 与 request shape 决定 route-query、fetch-cache 或 local。 真实多节点 H100/IBGDA、批量 round-trip 与约 7% model error 支持这些测量系数；predicate 不是所有网络和架构的常数，re-adaptation splice 也有失败面。新架构需重测 payload/fetch 系数，单机或大 query 仍可搬 KV。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#move-the-query-not-the-cache-characterizing-cross-instance-latent-and-sparse-attention-redistribution-across-gpu-fabrics)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：INFER-PD-DISAGGREGATION — [章节](../../../../../books/part-05-inference-system/55-pd-disaggregation.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems](https://arxiv.org/abs/2606.01508v1)

精确版本 `2606.01508v1` 的机制与适用条件：传统 OS 的 process/thread/syscall 假设确定控制流和有界生命周期；长寿命 Agent 动态选工具、积累状态并跨 session 改变目标。AOS 架构在现有 OS 上增加 agent scheduler、context/memory、capability registry、policy/trust enforcement 与 audit control plane，并列出从 user space 到 distributed plane 的集成层级。 这是架构/非目标/评价标准分析，不是实现 benchmark；它支持责任分层，却不证明应由新 OS 取代 Linux/Windows。agent control plane 会扩大 TCB 和调度复杂度，普通应用仍应运行在现有 OS 隔离内。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#agent-operating-systems-aos-integrating-agentic-control-planes-into-and-beyond-traditional-operating-systems)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Defenses &amp; Enablers For Skill Injection Attacks on Terminal Based Agents](https://arxiv.org/abs/2606.01567v1)

精确版本 `2606.01567v1` 的机制与适用条件：可证明的是 Skill 必须经过 provenance、capability 与 runtime mediation；不能证明 guardian 单点足以替代 sandbox、least privilege 和 effect-level authorization。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#skill-injection-guardian)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Don't Let a Few Network Failures Slow the Entire AllReduce](https://arxiv.org/abs/2606.01680v1)

精确版本 `2606.01680v1` 的机制与适用条件：证据支持“collective algorithm 必须消费当前 topology/bandwidth state”这一机制；它不证明无额外 buffer、控制开销或多故障下仍保持同样收益。旧 ring 在对称网络、故障直接 fail-stop 或恢复时间短时仍更简单。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#optcc)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点“退化链路仍在线时，Collective 需要 Bandwidth-state Schedule”；现有正文对照及采用边界以本报告当前判断为准。

### [Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation](https://arxiv.org/abs/2606.01725v1)

精确版本 `2606.01725v1` 的机制与适用条件：证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#gaiatrace--vidur-agent)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点“Task-DAG Simulator 只能校准 Capacity Plan，不能承诺线上 SLO”；现有正文对照及采用边界以本报告当前判断为准。

### [SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving](https://arxiv.org/abs/2606.01751v1)

精确版本 `2606.01751v1` 的机制与适用条件：论文证明的是所测模型/长度下 segment reuse 的可行性，不是任意切片均等价；segment identity 仍必须绑定 tokenization、position、model/adapter 与 correction policy，边界依赖或 selector drift 时要回退 dense Prefill。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#sparsex)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：INFER-KV-CACHE — [章节](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点“非 Prefix 复用必须绑定 Position-aligned Segment 与 Correction State”；现有正文对照及采用边界以本报告当前判断为准。

### [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770v1)

精确版本 `2606.01770v1` 的机制与适用条件：单一 harness 在固定 benchmark 上反复优化时合理，但 open-ended task stream 会累积 history、domain shift 与 specialization conflict。Adaptive Auto-Harness 把持续 evolution、solve-time harness-tree routing 和 human steering 分成三个控制面，并保存 stateful evolution history。三类流式 benchmark 与 ablation 支持该分工在给定系统中减轻峰值后退化；不能证明自动演化不会 reward-hack，也没有把 human intervention、branch retirement、artifact provenance 与生产 rollback 全部闭合。本报告只保留上述 exact-v1 机制、实验边界与 failure mode，不把作者 benchmark 外推为通用生产结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#adaptive-auto-harness)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-PLATFORM — [章节](../../../../../books/part-07-agent/84-agent-platform.md)；命题锚点“Harness Controller 是版本化策略，不是模型的隐式习惯”；现有正文对照及采用边界以本报告当前判断为准。

### [Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving](https://arxiv.org/abs/2606.01839v1)

精确版本 `2606.01839v1` 的机制与适用条件：作者在四张 A40、Qwen3-0.6B replay 与 SWE-agent traces 上证明这一 owner change 可减少预测依赖；不证明所有 agent conversation 都有稳定两阶段结构，模型、工具或负载变化时仍需迁移、再平衡与 admission fallback。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#conserve)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：INFER-SCHEDULING — [章节](../../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点“Conversation Placement 用已观察状态替代逐 Turn 预测”；现有正文对照及采用边界以本报告当前判断为准。

### [Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction](https://arxiv.org/abs/2606.01850v1)

精确版本 `2606.01850v1` 的机制与适用条件：压缩评估通常只比较 accuracy/perplexity，却可能遗漏置信集合扩大与 selective-risk 变化。论文以 conformal prediction 在 12 个 LLM、量化/稀疏配置与五项任务上分离 accuracy 和 uncertainty，观察到规模依赖与阈值式 inflation。它证明 deployment gate 不能由 accuracy 单指标代理；不证明 conformal coverage 在 distribution shift、生成式开放答案或线上 calibration drift 下自动保持，也未给统一 latency/SLO。本报告只保留上述 exact-v1 机制、实验边界与 failure mode，不把作者 benchmark 外推为通用生产结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#compression-uncertainty)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Compression Release 必须同时验收 Accuracy 与 Calibrated Uncertainty”；现有正文对照及采用边界以本报告当前判断为准。

### [Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads](https://arxiv.org/abs/2606.01927v1)

精确版本 `2606.01927v1` 的机制与适用条件：证据支持 inference scaling 必须分别计量 model-parallel compute、communication 与 non-scalable control path；作者基准和 production deployment 不能证明任意 runtime/模型都得到相同收益，异步 overlap 还引入 buffer lifetime、ordering、backpressure 与 late-result failure mode。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#albireo--non-scalable-inference-overheads)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：INFER-REQUEST-LIFECYCLE — [章节](../../../../../books/part-05-inference-system/42-what-happens-during-inference.md)；正文锚点“并行扩展必须先移出不可扩展的 Host Critical Path”；现有正文对照及采用边界以本报告当前判断为准。

### [Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories](https://arxiv.org/abs/2606.02060v1)

精确版本 `2606.02060v1` 的机制与适用条件：证据支持 outcome → span → claim propagation 的诊断分层，但 LLM-assisted annotation、framework/backbone mix 与 benchmark construction 不能证明 locator 找到真实因果根因；它是 failure sensor，不是 truth owner。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#drift--telbench)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“Trajectory Error 需要 Span、Commitment 与 Claim Propagation 三层坐标”；现有正文对照及采用边界以本报告当前判断为准。

### [DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding](https://arxiv.org/abs/2606.02091v1)

精确版本 `2606.02091v1` 的机制与适用条件：六类 benchmark 支持“draft capacity 与 conditioning interface 共同限制 acceptance/speed”这一实验性分支；结果绑定三种 target、训练数据和作者实现，不能外推为 diffusion 解码普遍优于 AR，也不能省略 target verification、rollback 与 distribution/quality contract。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#dflare)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：INFER-SPECULATIVE-DECODING — [章节](../../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点“Draft Capacity 可以借用 Target Feature，但不能借走 Commit Authority”；现有正文对照及采用边界以本报告当前判断为准。

### [Faster Synchronous On-Policy RL via Straggler-Aware Group Sizing](https://arxiv.org/abs/2606.02218v1)

精确版本 `2606.02218v1` 的机制与适用条件：GRPO/DAPO 实验支持动态 group 可以在所测训练栈改善 wall-clock 且保持 reward/quality；不能证明 controller 在 workload shift、reward drift 或不同 rollout service 下仍校准。最小固定组在负载稳定、可预测性优先时仍更简单。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#straggler-aware-group-control)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：TRAIN-GRPO — [章节](../../../../../books/part-04-training-system/33-grpo.md)；正文锚点“同步 Group Size 也可以由 Straggler Risk 有界调节”；现有正文对照及采用边界以本报告当前判断为准。

### [SeClaw: Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents](https://arxiv.org/abs/2606.02302v1)

精确版本 `2606.02302v1` 的机制与适用条件：证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#seclaw)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses](https://arxiv.org/abs/2606.02373v1)

精确版本 `2606.02373v1` 的机制与适用条件：实验只证明特定 20B agent、search tasks 与训练配方下的收益；harness state 仍可能 stale、被错误压缩或与网页事实分叉，因此必须 version、provenance、rebuild，并保留 final verification。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#harness-1)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：AGENT-CONTEXT — [章节](../../../../../books/part-07-agent/75-context.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference](https://arxiv.org/abs/2606.02430v1)

精确版本 `2606.02430v1` 的机制与适用条件：该研究支持 evaluation subject 必须绑定 injection site、bit/error model、model/task 与 observable outcome；模拟 fault 不给出现实发生率，也不证明作者四种 mitigation 覆盖 GPU、network、kernel 与 checkpoint 的真实故障分布。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#llmfi)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点“数值 Fault 要沿 Layer、Operation、Token 与 Task 观察传播”；现有正文对照及采用边界以本报告当前判断为准。

### [On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters](https://arxiv.org/abs/2606.02437v1)

精确版本 `2606.02437v1` 的机制与适用条件：它支持 adapter identity/revision/provenance/evaluation/residency 必须分层，但不证明每个用户都应持有 adapter，也不能把 population 数量等同同时驻留数量。现有 Model Registry 章节已经拥有该长期合同，故不重复写入。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#peft-scale-up--down--out)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-MODEL-REGISTRY — [章节](../../../../../books/part-06-ai-infrastructure/59-model-registry.md)；现有正文对照及采用边界以本报告当前判断为准。

### [Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools](https://arxiv.org/abs/2606.02483v1)

精确版本 `2606.02483v1` 的机制与适用条件：三套 corpus、12 种 policy 的原型支持 privacy boundary 必须在 dispatch 前执行；它不证明 prototype 覆盖真实 provider retention、timing side channel 或多工具 workflow。低风险本地 pure function 可继续 speculation，外部 observer 则需 issue-time contract。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#ghost-tool-calls)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文对照及采用边界以本报告当前判断为准。

### [SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction](https://arxiv.org/abs/2606.02540v1)

精确版本 `2606.02540v1` 的机制与适用条件：一次 session 的 poisoned skill 测试会漏掉 persistent package 被静默改写后在未来复用触发的 harm。SkillHarm 把 fixed-payload 与 self-mutating poisoning 放进 skill lifecycle，并按 data、environment、autonomy 构造 879 个攻击样本。作者结果显示当前 defenses 在该 harness 下仍脆弱；ASR 受 agent 是否读取 poisoned file 影响，未触发不等于抵抗，benchmark 也不能证明所有 skill ecosystem 的真实发生率。本报告只保留上述 exact-v1 机制、实验边界与 failure mode，不把作者 benchmark 外推为通用生产结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#skillharm)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：PLATFORM-SECURITY — [章节](../../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点“Harness Backdoor 把单次写入变成跨 Run 控制状态”；现有正文对照及采用边界以本报告当前判断为准。
