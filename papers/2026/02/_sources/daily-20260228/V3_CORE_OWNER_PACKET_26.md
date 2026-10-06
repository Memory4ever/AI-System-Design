# 第二十六包：AIQI必要缺段恢复与两个早期once-core停点

没有Books lease；35safe不变。只恢复三个同identity既有待办，不扩标题池、来源或版本比较。PDF原件已保存，数学/图示相关页实际读取；PDF恢复不代表全证明或实验复现。

## 23242 AIQI：拟2+1+3=6，Ch79模型式lookahead之外的条件分支

[精确v1 PDF](https://arxiv.org/pdf/2602.23242v1)已于本轮2026-10-05T22:44Z附近定点取得；HTML giant转换段缺失关键aligned数学，因此只恢复PDF pp3–7，p6已render并实际视觉核验。原[HTML](https://arxiv.org/html/2602.23242v1)完整题摘、方法/声明已读且与PDF此采用链一致；current-v4摘要新增Self-AIXI等内容不授v1，不默认比较全部revision。

旧general-RL最优性分析依赖显式environment model；本稿直接对history/action条件化的离散return distribution作Bayesian mixture、按期望return选择行动，不用模拟未来环境。有限A/O/R、reward[0,1]、gamma∈(0,1)，H-step return离散到M级；N≥H周期augmentation分成N个phase predictors，只有已观察到完整H-step reward后才能给该phase补return。n=t mod N的条件保证输入不用未来reward，N−H留出的buffer支持有限counterfactual轨迹。正探索概率tau、fixed tie-break与phase身份都属于方法，不等普通Q表或任意值网络。

pp4–6必要理论条件已读：grain-of-truth要求每个phase mixture包含该AIQI策略本身的真实conditional return predictor且有正prior；reflective-oracle-computable类给自指闭包，不是可在有限硬件部署的computability。Th4.6需tau≤epsilon(1−gamma)/10、M≥10/[epsilon(1−gamma)]、H=H(eta)且eta≤epsilon(1−gamma)/10、N≥H+log_gamma(epsilon/5)。中心主文由one-step gap与counterfactual TV收敛拼接给limsup value gap≤epsilon、nu^pi-a.s.；只采用 **这些条件下理想on-policy无需显式world-model的替代分析**，不声称全部附录lemma或所有proof已独核，不给sample complexity/finite-time wall或一般LLM保证。

直接反侧p7：若数据由historic pi'产生，predictor估的是该旧policy return，最大化该值不等自己后续策略值。Th4.10在含computable variable-order Markov类、H≥2等条件给存在性反例：即使某self-optimizing policy存在，AIQI也不必epsilon-self-optimizing。保留这一采用边界，不把反例扩成所有off-policy算法无效。硬件/precision/吞吐/SLO不适用于本次理想理论采用命题；有限近似程序和附录实验不是本段的证明，不按headline授它们部署最优性。

actual `AGENT-PLANNING` Ch79 42–85完整状态/transition/lookahead邻接实际读，185–219完整search/teacher/controller邻接此前已读。现有model-based候选验证、full-action探索和reactive fallback，未说明 **直接return预测在自身policy/完整history/grain-of-truth条件下构成非world-model分支，而旧日志return不能授新policy最优**。拟在model-based lookahead交接处极短条件段；Ch25不重复environment dynamics，Ch33不把理论return混成实际GRPO credit。条件不可核时保普通reactive policy、显式model/search与真实rollout评价。root若判现有分支已经具体覆盖可Existing，不以AIXI/AIQI名称制造gap。

原v1 Submitted2026-02-26T17:21:16Z；本轮原始V3_THEME_0/1 DataCite同DOI实际registered2026-02-27T03:06:03Z、created03:06:02Z，两字段分开。公告下界结合registered秒精度+1sec给arXiv事件02/27 09:00～11:06:04+08。current UAI2026及后续v2–v4为窗外线索，无具体撤回标记，不凭后来摘要授v1。

## 22519 Mathematical Theory of Agency and Intelligence：once决定拟窄IN5，须root准入

HTML v1确404；[原v1 PDF](https://arxiv.org/pdf/2602.22519v1)定点恢复，仅pp2–3/6–10/15–17实际读，p6图caption已render视觉核验。一次事实决定停止，不补量子/生物解释或全部形式推导。拟贡献只为 **frozen policy的扰动监测，interaction统计先于reward、并受表示/分箱与基线稳定性限制**，不是新intelligence定义、MI normalization本身或IDT命名。

P=MI(S,A;S')/[H(S)+H(A)+H(S')]的.5上界是所写非负Shannon entropy代数界，不赋予“intrinsic intelligence”真值。DeltaH=H(S'|S,A)−H(S,A|S')=H(S')−H(S,A)，不能由它直接归因environment vsagent故障；MI非causal intervention证明。p6 Figure2 caption明确闭控制loop是future work，不采用p10“resolves open-loop fragility”或已能自适应恢复。严格agency必须<.5也不由定义成立：独立公平bits S,A且S'=(S,A)，H(A|S)>0、MI(A;S'|S)>0而P=.5；不据此断言所有paper无价值。

决定性有限经验p7/15–16：HalfCheetah-v4 frozen SAC2M/PPO1.5Msteps、11/10seeds、50Ksteps/run、8种外力/重力/observation/action noise；window300/stride50，3σ相同baseline阈值但IDT为四信号union，reward仅单信号，不能把89.3 vs44%唯一归因P或称equal false-alarm budget。5seeds因baseline不稳排除，p7/p16却又写168trials/n21seed，人口冲突不采用其精确统计优势。三equal-width bins/bodypart grouping得信号，四bins估计不可靠、quantile bins扁平无用，是具体estimator条件而非通用interaction information保证。

LLM：Llama3.1-8B/Ollama、三teacher、约4574turn/34conditions、AzureT4、4096context/max150tokens、normalT.7 vsT.1。fixed注入contradiction/topic/nonsequitur约40词、baseline30turn；不能以这些明显synthetic shifts授自然semantic drift召回。P与cosine的29/34=85%一致性更高却semantic项44%的括号仍写29/34，数字冲突不采用精确比率；token frequencies没有完整说明联合采样/对齐，不能称所估MI就是因果coupling。precision/完整wall与false-alarm长期预算ND，teacher APIs/监测/分箱校准均付费。由此只保表示依赖的sensor/control分责与负侧，不授zerooverhead、intelligence划界或自主控制已落地。

actual `PLATFORM-MONITORING` Ch67 18–46/265–299完整邻接实际读，已有sensor identity、统计信号不能认证变化原因/质量、threshold/variance成本与独立policy权限。若root确认该受控扰动/分箱失效条件有准入价值，拟具体Existing优先：sensor proxy≠task correctness、监测不授控制都已覆盖；是否还缺interaction triples的具体表示分箱条件由root actual裁决，不先写书。

Submitted2026-02-26T01:26:21Z，原V3_THEME_0实际registered02/27T02:48:16Z、created02:48:15Z；arXiv区间02/27 09:00～10:48:17+08。current-v2 March8无此窗revision授权，无论准入不比较其正文。

## 22240 Task-based parallel code：once决定拟窄IN5，但日期尚未授

[v1](https://arxiv.org/html/2602.22240v1)完整题摘与必要blocks51–72实际读，决定到这里停止。具体反侧：先作包括hard在人为修复，才测strong/weak scaling，non-executable计zero；Qwen HPX pi代码将up128任务共用global RNG、争用导致理论embarrassingly-parallel工作仍不伸缩；OpenMP把task和loop parallel混用是额外错配。新可选条件是 **固定repair人口后的correctness与scaling仍分验、runtime语义错误不能由compile/pass@1关闭**，不是HPC应用名或新benchmark大小。仅此具体受限负侧拟IN5待root校准，模型泛化排名/PCGQS普遍质量不采用，必要方法/owner在日期授予后续，不继续全实验。

双socketEPYC7742、core-bound最多128threads、固定128tasks、GCC13.3/OpenMP4.5/HPX1.11；原57称24/48/96是odd core counts有措辞错误，不照录为奇数cores。v1 Submitted2026-02-24T09:49:10Z，sameDOI registered2026-02-27T02:41:48Z只给上界，不能因在本窗登记就把早submission改成本窗首公开。Workshop2026 comment不等publication。尚缺原公开下界/实际首次公告，精确保留日期，不列确定候选、正面Books或无遗漏。可接受同identity首次公告/原正文公开时间界，重开只此ID；不扩扫其他日期或默认revision。

2026-10-06 root非作者22519必要PDF方法/冻结RL协议、3bins/W300/stride50与分母冲突实际核验，窄IN5（2+1+2）通过，不授causal agency或精确AUROC。新执行者非旧packet作者实际核Ch67 18–46与265–299，窄sensor/control/表示依赖边界已有具体覆盖，标准E落本日报，不写Books、不复用whole-paper理论。23242实际Ch79段87、完整78–105及自身末注560已root非写入者POST通过，窄锁释放；是实际一段I，不授日级完成。
