# 当天必要证据与 Books 比较（进行中）

最终状态：root完整实际读六部分、重跑V3与Books/本日限定diff检查，日级语义通过并授权完成。本日58冻结、38POST/7覆盖/12报告/1暂缓，普通待办0；下列进行中标题和时间段为过程原证。最终评分又定点纠正09591与09214为2+1+2=5：前者两初始化/精度混杂的长度局部反侧，后者URR/HCC局部VLM sensor；原新增可复用但不是长期通用foundation，非因Only降分。不改58准入/已核标准审阅/Books或原负面限制，旧6分以当前README最终表及本段为准。

作者：feb12_independent；独立准入与必要证据校准：root。仅记录真实已读位置，普通未读继续，不自授整日完成。日期原字段见 V3_DATE_BOUND_FIELDS.md；下述四项 v1 submitted 均在官方 Mon14–Tue14 EST 批次，DOI在本窗登记，推定公开区间下界为2026-02-11T09:00+08，上界为逐项registered加一秒。不声称登记即发布时间。

当前停点以文末“最终逐ID停点”为准：58唯一家族冻结、38整合POST/7已有覆盖/12仅报告/1暂缓；必要原源、日期与owner处置均已非作者独立核到各自安全终态，全部窄锁释放，普通待办0。六项局部评分修复不改变准入或处置。只剩最终六部分机器检查与root整日验收，作者不授完成；下方按时间保留的“待授/working”段落是过程原证而非当前队列。

## [FlexMARL v1](https://arxiv.org/html/2602.09578v1)

评分拟定2+2+3=7，深入完成必要原文：§3–4、§8.1–8.2/Table2、§8.6–8.7、§9。准入是 microbatch 到齐便算梯度、缓存累加，但 global batch 完整后才 optimizer update 与统一 policy-version 同步；不是一般异步 rollout 原则，也不是 stale fully-async 更新。Experience table 带 policy_version、sample_id={input_id}_{turns}_{trajectory_id}、generated flag/value/ref；梯度计算与未完 rollout 重叠。Hierarchical agent-centric LB 与 on-demand 绑定补充吞吐。

评价：48 nodes、每node16 commercial NPU/64GB/HCCS；Qwen2.5-14B multi-agent与14B/32B conversational、私有电商数据；长度8192、GRPO lr1e-6 Adam、batch64/micro16，precision Not Disclosed。Table2 MA MASRL914.4s/DistRL293.8/MARTI174.1/Flex126.1，7.3x是对朴素MASRL；CA438.6/130/112.8/78.8。平均约1.4x对MARTI，不写7.3x对SOTA。去LB吞吐下降19.8–25.5%；去micro-async MA E2E+103.2%、CA+57.5%。混合32B/14B与至15agent的有限扩展不授任意硬件扩展。

关键限制：作者断言同步on-policy，但没有独立任务质量/收敛实测；不能从吞吐证明数值等价或生产质量。Reviewer推导条件是同一global population、完成group reward/normalizer及冻结policy下，分块提前计算才不改objective；跨块不完整优势不可提前定值。§9单buffer权重、PID/rank及STRICT_PACK只给披露NPU实现，不普遍外推。未运行代码、未复现。

Books 比较：已实际读 Ch33 §RL Recipe与§Rollout服务化（1100–1225）：已有policy epoch、trajectory gate、异步服务和group identity，却未承载“gradient compute提前、optimizer commit仍同步”的具体分界。拟在服务化开头邻接增加窄机制段，owner TRAIN-GRPO；Ch32/Ch34交接尚需读完再写，root必要source→owner与具体写锁未授。

## [KVFetcher v1](https://arxiv.org/html/2602.09725v1)

评分拟定2+2+3=7；深入必要原文§3.1–3.3、§5.1–5.3、§6。v1事件页题名 Efficient Remote Prefix Fetching with GPU-native Media ASICs；保留作者系统名KVFetcher，不混后发KVCodec元数据。量化后的整数KV按token/frame与three-layer chunk组织、离线H265无损编码；lossless仅针对量化值，不对原BF16无损。读取用闲置NVDEC而非SM解码；waiting_for_KV独立队列使fetch尚未完成不挡non-reuse请求；完成后下一iteration进入running。Profile lookup按上一chunk测得bandwidth选择已编码resolution，降低传输/解码pipeline bubbles，不改量化精度；frame-wise恢复到pagedKV。

评价：A10080GB(5NVDEC)/H2096GB(7)/L2048GB(3)，LWM7B1M/Yi34B200k/Llama3-70B128k，2/2/4高端或2/4/8 L20；1–40Gbps，默认H20/Yi34B/16Gbps；L-eval3–200k、LVeval16–256k、LongBenchV2 13–167k；non-reuse 0.2req/s、40kreuse阈值、FCFS。作者平均TTFT改善13.63x对fullprefill、3.51x对rawreuse、1.52x对CacheGen。Layout消融给量化之外interframe2.2x、intraframe累计2.96x；同网络jitter adaptive TTFT5.2s比fixedresolution约20%低。7chunks decode+restore峰400MB只是该恢复buffer开销，不是全部KV。

反侧：纯decode吞吐4L20/2H20/2A100为27K/67K/47K tok/s，是CacheGen0.3x/1.34x/0.88x，ASIC并非各卡更快。GQA较小KV和NVDEC数量减少机会。§6 NVENC在线编码过慢，不能授PD migration/故障恢复可行；全部fetchKV预分配会因HBM预算挡non-reuse，故“无SM竞争”不等“完全无干扰”。localoffload是futurework。质量只限披露量化和任务，无生产SLO、未复现。

Books 比较：Ch45实际§Disaggregated KV Compression（1230–1250）已有service-awarecodec与joint costs；§lossless codec（660–662）已有量化唯一lossy原则。未覆盖NVDEC offline-prefix路径及compute隔离不消HBM admission。拟在codec service合同旁增加两段hardware-path条件分支，owner INFER-KV-CACHE；Ch44/46开篇交接已读，root必要source→owner与写锁未授。

## [Sci-VLA v1](https://arxiv.org/html/2602.09430v1)

root已实际核§3.2、§4.1、§4.2.3与结论，窄准入通过；2+1+3=6标准完成。原子π0/π0.5/π0-fast各自finetune后冻结；检索下一skill demo起始joint pose，LLM读当前joint/camera/next-task/targetpose，生成restricted controller-template过渡代码；在固定平均demo时长T后打断原子skill，执行释放/安全放置/姿态恢复，再恢复下一原子VLA。改变的是 skill terminal→next initial distribution bridge，不采用化学发现及科学成绩。

反侧：有些关闭盖子的baseline本来成功，因为上一步terminal匹配下一初态；不能说所有sequencing必须bridge。仅每sequence20trials，排除了代码generation/network bug，因此不是全部请求端到端成功率；内部原子精度失败也不由桥接修复。unsafe code/collision、regen latency和网络依赖保留，无formal safety或任意组合保证。未复现。

Books 比较：Ch26 §Next-skill Readiness Contract（901–937）真实承载postcondition≠next readiness、gate/repair/abort和downstream residual训练，但“无需重训冻结skill，插入demo-init controller bridge后resume”尚未显式承载。拟在readiness contract首两段后加窄替代分支，保留已有gate与residual，owner MULTIMODAL-EMBODIED-VLA。邻章25/27开篇已读；待rootsource→owner与具体锁，不以主题相同宣称已有覆盖。

## [AWM v1](https://arxiv.org/html/2602.10090v1)

root实际核§3.3.1、Table6/7、B.2和Limitations，窄准入通过；2+1+3=6，因reward具体gap作受影响深入比较。SQL/MCP、1000合成环境及runtime error修复不计贡献。拟采用DB-diff verifier的idempotent false-negative（目标已成立，必要无op却没有预期变化）与wrong-entity false-positive（发生了形式匹配变化但错误对象）的具体反例；LLM结合trajectory/state校正code verifier仅是互补sensor，不授语义真值。

Table6 Qwen3 4/8/14B比较LLM/code/augmented；hybrid多数指标改善但4B MCP与LLMonly同为6.70，不写每项严格胜出。GPT5judge约$1.80/trainstep最多1024samples；runtime max5次异常selfrepair只保证可执行尝试。Table7只4B：训练/评估history-limit对齐时limited64.50/22.57/43.89/6.70 vsfull55.35/15.92/36.33/6.15；未对齐limited61.85/9.35/15.11/5.03 vsfull56.80/16.10/33.09/6.15，截断并非免费/普遍更好。只训练526/1000环境，合成跨域结果不授真实环境correct transitions或生产oracle。

Books 比较：Ch33已有outcome hardgate、环境transition权责、judgeproxy但未给DB差分两种反向误判，也未给history-limit改变policy observation的训练部署对齐。拟在reward/environment段追加反例支撑的窄解释，owner TRAIN-GRPO（reward population & deployment context）。Ch84只是消费EvalSpec不重造rewardowner；待rootsource→owner与锁。

## [AgentCgroup v1](https://arxiv.org/html/2602.09345v1)

2+2+2=6标准必要证据完成：§3.1–3.4、§5–7。144 task-runs=111GLM4.7Flash与33Haiku4.5，后者是前者task subset；跨模型仅33共享task。表征机Ultra9 285K/24core/128GB/Ubuntu24.04/Linux6.15.11，每秒采样，无resource limit；工具返回计dispatch+execution+collect，initialization不含image pull。98.5%burst是Haiku，不是GLM（67.3%）；1.8x nondeterminism仅同task三run，不证明历史预测均无用。增量是tool-call child cgroup在agent parent budget下隔离burst、memory.high throttle/freeze优先于毁掉context的kill，BPF memcg/sched_ext作在kernel反应。

§6仅Ultra7 258V/4core/16GB/patched6.19rc5、三条trace 50倍重放；高优先dask421MB、两低优先github3.py406MB，memory.high=400MB。1100MB预算下baseline1LOW OOM，BPF全部完成；1300MB预算HIGH allocation P95 70.97→50.14ms（29%），不是live agent E2E/P95。Prototype依赖未upstream memcg RFC，初始化/大image/retry积累仍未解决。未实跑。Books待比较 Ch84 sandbox resource管理具体段，不授生产多租户隔离或通用微秒SLO。

## [ELPO v1](https://arxiv.org/html/2602.09598v1)

2+2+3=7，必要深入§4.1–4.4/Eq6–12、§5.3、§6.2、Limitations、Appendix A/E/F/G/H。BEL保留failed-prefix采suffix，任一成功向后、全部失败向前；仅O(logK) anchors，非token成本保证。Entropy-gap挑一failedtrajectory与adaptive1–3 suffix占原Ntotal16；内部children reward平均作branch比较，leaf normalization沿sharednode平均作trajectory credit，lambda混合；只critical suffix放宽负adv lower clip，正adv upper unchanged。

8A100、Qwen2.5-7BInst/Qwen3-4BInst，SFT3K五epoch+RL30K一epoch，batch128/mini16/context20k/KL0，precision Not Disclosed。全baselines同16 rollout计数不等总generated tokens/compute，tree分支也计一条。Table1 4B AIME25/Math500低于Demy。Appendix E GT仍固定policy/decoder Pass@keval recoverability代理，Hit@1 66.8%，稀少成功或有限budget false-negative能让定位移位；只确定性code/calculator，未验web/GUI；单earliest不涵盖多错交互。F表显示各移除降低AIME24，而叙述声称移除ELC略改善AIME24，与表矛盾；不采用该句或稳定性保证。机制可窄采用经验branch-credit，不采用真first-error或硬不可恢复。Ch33已有token credit/entropy branch与FaithRL前缀重采，但二分经验定位→局部lowerclip尚待具体Books比较/非作者。

## [Where-to-Unmask v1](https://arxiv.org/html/2602.09501v1)

2+1+3=6标准必要证据完成，追加读Appendix B/C.1。§2.2/PiRank、§3.1–3.7、§4.1–4.8/Table1–2。Gt-Margin=Pgold−maxPother是需要GT的oracle，不可线上用；greedy每步一token、fixedL用于比较order。LLaDA8B/Dream7B经dataset LoRA；§3 GSM256与C.1 GSM128有冲突，保留两值、不授同一统一length配置。Oracle LLaDA GSM.845/Sudoku.995不可作部署结果。

训练另一个LLaDA8B LoRA+MLP planner，输入prompt+argmax填充hypothesis+maskedstate，oracle生成rank以stochastic rank-conditioned masking构造训练states，PiRank relaxedNDCG训练；token predictor不改，部署前半planner后半Margin。Table2 learned GSM.705vsMargin.605、Math.285vs.180，但Sudoku.085<.110；全程planner和去hypothesis均更差。额外planner forward、GT/rank采集与训练成本，不授无成本oracle复现或多token并行性能。Books待Ch24 where/what解耦论点比较。

## [Laplacian Mechanism v1](https://arxiv.org/html/2602.09297v1)

2+1+3=6，标准机制/有限评价完成；geometry论证与configuration必要段仍待补。§2/Eq3将部分heads PV改V−PV，Wo允许更新符号，混合heads不增trainable params但未授无算力成本；直接控制偏离contextual mean，而不是把attention替换成普遍收缩。§3 ViT-B/DeiT3、same recipe/drop-path，Table2 bestk依dataset，ImageNet非随k单调。561M GPT2style/10heads，11.2B FineWebEdu+midtraining+SFT；GSM/HumanEval为pass@10，其他zero-shot不可混。全10L HumanEval10.98低于baseline12.80，7L GSM21.99低于22.29；平均改善不等每项。§4geometry分析来自vision classifier，NTC理想及原因是conjecture，不能授LLM能力几何因果或语言token都应collapse。Books待Ch14实际平均/variance机制比較。

## [Architectural Pitfalls of RCA Agents v1](https://arxiv.org/html/2602.09937v1)

2+2+2=6标准核心完成；§3/4.1–4.3、§5.1–5.3、§6。1675runs=335task×5model，Opus4.5分析+人核binary诊断，多labels百分比相加>100%；相关共享framework不独自证明architecture唯一因果。具体可采用§5.2：Executor回code+完整output/errors；Controller给完整analysis、旧output片段与goal，纠正summary-only opaque interface。

Bank有限mitigation四model共41任务（§5.1prompt干预为Claude70task，不能混人口）；GPTmini perfect0→2/41、Gemini1→3、Solar2→3。每步token+24.8%(68K→85K)、steps−22.1%(11.9→9.2)、总token−1.6%、时间−22.3%，不能说通信免费。Prompt broadens探索但解释幻觉不降，未证明任何prompt永不可修复。persistent kernel memory watcher阈值重启只消披露baseline OOM（Bank2/41scenarios），restart不等原状态恢复。其余domain与别framework、人工classifier独立一致性未验证；硬件/precision Not Disclosed。Books待Ch82实际artifact/evidence handoff；不会因RCA领域指标本身准入。


## 首批必要证据补足与当前 Books 差额（2026-10-04T09:35:25+08:00）

四项实际写入并经root非作者POST通过：TRAIN-GRPO L552（AWM两向差分错误）、L1222（Flex提前梯度/global commit）、L1224（history对齐），INFER-KV-CACHE L1241/1243，MULTIMODAL-EMBODIED-VLA L919/921；各末注已同步POST通过，不授日级Gate，三文件锁已释放。

09501补B：单A100；token/planner分别LoRA，planner另全参数MLP，Sudoku2epoch、其他5epoch，batch2/accum4、lr2e-4、PiRank k30。无端到端timing/精度披露，不能称低开销。Ch24 L278–308已读：已有schedule/content标签分权、influence/confidence order与position-temperature，不等GT-correct-vs-wrong margin oracle及单独planner前半/后半fallback。拟增加窄替代分支，await source→owner/lock。

09297补§4.2–4.7/5/6/8、B.2：ANOVA的withinseq/withinclass/betweenclass及图像分类NC关联不是语言模型因果证明；§6 diffusion analogy依signed参数/局部线性解释，任意learned V/Wo不授单调variance下降。§8明确SSL理想几何未知，NTC非universallyoptimal。Ch14 L92–120公式为PV及路由不等贡献，未承载V−PV作为可混head的偏差接口。拟在平均读取之后一段及直接限制，不移MHA owner。

ELPO比较：Ch33 L205–250已有PRL suffix-logratio、PRPO独立PRM、entropy-hint树credit及FaithRL sentence-verifier重采；未有有限Pass@k二分经验error boundary→critical suffix的lower-clip控制。拟紧邻FaithRL新增两段，保留有限采样/无真error oracle、额外预算和F表文矛盾，不采宽理论。root必要 source→owner/窄锁待授。

AgentCgroup比较：Ch84 L462–480 workspace生命周期/权限已覆盖，L594–612平台harness并非tool child cgroup resource反应；需要区别agent parent预算与短时tool burst的child调度、memory.high/freeze先于kill。拟Scheduling开头两段；patched kernel/50倍3trace而非liveE2E限制邻近，未授Production。

RCA Books拟已有覆盖：Ch82 L412–417 ordered evidence DAG、raw-message回读与conflict fallback，以及L270–272明确诊断需完整trace/typed evidence，已承载opaque summary不够和长消息成本。新Bank界面案例支持此边界，不改变这条长期规则；不为其领域成绩增加正文。请root核具体coverage而非主题映射。

## [On the Optimal Reasoning Length v1](https://arxiv.org/html/2602.09591v1)

2+1+3=6，标准必要证据完成，实际§3.1–3.2.2、A.1–A.4、B.4、D.1–D.2。Qwen3-1.7B-Base与R1Distill1.5B，两初始能力不构成同模型反事实：长度惩罚强度改变policy，Base在受测范围长者较好，Distill出现中间峰。Mode accuracy、answer entropy/mode share区分中心与离散度，但仍关联，不能授overthinking唯一几何/因果。DAPO17K、KL0、8GPU×72h（型号Not Disclosed）、batch64×16rollout、train8K/16K；分别BF16+TIS/FP16无TIS，初始cap超限<5%不是全训练截断率；模型与recipe不同不因果鉴定“reasoning已有/未有”。AIME/AMC64sample、Math50016sample，temp.6/topP.95，meanaccuracy非pass@64。

直接反侧：D.1同576GPUh非单纯同steps支持窄非单调，但不是所有调参全费用；64K仍大量>32K也>64K，不能完全排除truncation。A.4有同配置ALP第一次diverge后restart成功，只报告成功run，不授稳定性。GFPO实际16→8最短过滤未复现短化，早期logging只计算filtered长度是假短趋势，失败长回答排除的解释为作者假设，不能授所有GFPO无效。Books拟仅报告/已有覆盖：Ch33 L796–820已有hardcap、显式成本和prior的成立条件及必要步骤误税；本项仅两初始化/不同精度的局部证据，不足改成阶段识别规则或通用length阈值，采用局部新反例留本日报，待root比较。

## [PABU v1](https://arxiv.org/html/2602.09138v1)

2+2+2=6，标准完成：§3.1–3.3、4.1–4.5、5、B.1核心环境条件、B.2–4/B.6–8。Belief保存不可变goal/最近obs，attempted actions仅当前progress stage，学习保留旧obs、progress及action；available actions从obs parse，不认证物理可执行；进度文本不是Bayesian probability/严格Markov。训练successfulAgentTraj-L去关键动作判outcome、LLM+人核progress/retention，对noncritical步骤标签换下个critical action，训练label位置不授任意部署skip可达。

6776轨迹128392decisions，trainH100或GH200，evali5-9600K32GB/RTX3090，Ubuntu22.04，precision/seed Not Disclosed；8B主，1B组件。主81%vsATLAS65.4是相对23.9%，ATLASstep未披露，26.9%步骤改善相对AgentEvol13→9.5；部分WT/MV/ALF低于其对照，open模型数据从旧论文未reproduce。ALF Table2 progress-aug84.5→PABU90.0，inputtoken1,015,571→502,426但output15,042→25,869，非所有成本下降；掩context训练/评估一起改变模型，非仅inference消融。离线覆盖/未见失败与lossyabstract limits保留。Ch75 L534–544有可恢复执行state/时机，L364–388goal pruning，未有progress-conditioned action reset/obs retention的联合学习；拟两段，source→owner/lock待授。

## [AgentAuditor v1](https://arxiv.org/html/2602.09341v1)

2+2+2=6，标准完成：§4.1–4.3、5.1–5.3/Eq8、6.1–6.6/Table1–5、7、B.1。步骤语义embedding/τ合并EMAcentroid→reasoningtree，对CDP共享prefix和有限branch窗口judge，仅decision-critical evidence，仍给supportsets因此非消除popular cues；confidence gate commit/defer beamK不是真值/校准概率。GT筛majoritywrong-minoritycorrect构造branch preference；Eq8仍standard DPO，新增是训练人口，不给成熟DPO评分。

4bench/5MAS；3agents3rounds，upstreamgeneration保持；8A100，LoRA16/alpha32/dropout.05，temp.7/topP.95、epoch1–3/lrsweep，三seed均值未提供普遍置信界，precision/contextlength Not Disclosed。B.1明确Llama3.1-8B/3.2-3B，主简写Llama3，不混版本。Majoritycorrect MV100/minoritycorrect MV0是构造分母，不是自然任务普遍率；少数正确仍65.35/81.82，MaJC也有97.28/91.67低于MV。审计973tokensvsjudge1762/solver2046不含完整candidate生成/训练。无beam退步提供受限支持，文中“proving”不授任意commit安全。Ch82 L591–624已有minority override校准与act/defer，但未有语义CDP局部审计+陷阱人口训练；拟判别接口窄分支，待root核。

## [Rethinking Global Text Conditioning v1](https://arxiv.org/html/2602.09268v1)

2+1+3=6，标准完成：§3–5、6.1–6.3/Table1–4、AppH/J及B策略定义。PooledCLIP进入modulation、T5序列attention条件不同；其effect在FLUX短prompt10与长77子集不同，HiDream/FLUXKontext有inactive情形。修改y(p,t)+w[y(p+,t)−y(p−,t)]是MLPmodulation接口，不是finaloutputCFG；dynamic是layer-dependent而非timestep schedule。高scale会忽略原prompt，不授语义disentangle或通用视觉准确性。

T2I128Parti2images/prompt；count70/hand200；自动COCO5K，三人偏好majority；Table2aesthetic/complexitywin但relevance/defect可低于50，Table4smoothness反退。CLIPfreeCOSMOS先500K自产数据4Ktrain，CausVid1KtrainMLP，故适配非trainingfree；硬件/precision/总端到端成本Not Disclosed，现成pooled接口才有限低额外路径。AppH明确不解决T2Icorrespondence，hyperparams需校准。Ch24 L164–172有CFG/capacitygapguidance，未区分pooled modulation正负方向与attention语义；拟一机制/一限制段，source→owner锁待授。

## 决定准入的三个含糊核心：定点核验已停止

[ADORA 2602.10019v1](https://arxiv.org/html/2602.10019v1) §3.2 Eq4–8实际新增为 success-length/difficulty 条件下的 group 权重 heuristic：依当轮成功/失败长度及成功率乘共同 advantage 系数；“dynamic”指每轮按 rollout 重算，不是另有 utility estimator。根据信号定义未辨识新的 utility 可靠性条件，关闭贡献；不采用“token-independent 所以无偏原目标”的桥接。改变 query weighting 与依 rollout 取权重均需重新定义目标，不能以 token 维度恒定证明原目标无偏。root 已独立实际核此错误信号和原增量，关闭通过；不泛化所有 dynamic curriculum 无效，日期无需为不改变处置另请求。

[AARM 2602.09433v1](https://arxiv.org/html/2602.09433v1) opening/V-E/VI-C/VII-B R1–R6/conclusion：policy infrastructure 被假设可信，model/content/framework 不可信；kernel syscall 只能见低层边界，不能自动解释 TLS payload/高层 intent。五种 decision、dependency pause、default-deny timeout、身份/新鲜度与 signed receipt 是 normative 组合 spec；原文未给出新的 enforcement、兼容性或不可绕过的证明边界，因此关闭贡献。不是因“没有实现”排除 spec/theory，也不是因 security 词触发全文；root 实际核 R1–R6 与安全 claims 的证据角色，关闭通过。得到判断后停止无关附件。

## [BiasScope 2602.09383v1](https://arxiv.org/html/2602.09383v1)

窄准入经 root 独立核通过，2+1+2=5，标准审阅核心已读 §2.2–2.3、§3.1、§4.1/Table5–6 与必要 limits。Teacher 变换 rejected answer，保留 outcome 的目标经过有限 GPT-OSS-120B check；self-explanation→teacher hypothesis→去重→JudgeBench 增错筛选不是真实因果发现。七模型 greedy/random position，RewardBench 发现/JudgeBench 验证、最多四迭代；未声称新50种label或50%榜本身是增量。

采用的评价反侧是 Table6 length-matched truncation：多bias误判仍平均 +2.2pp，而纯 length 对照 −2.5pp，因此不能仅由 response length 解释此局部差异。标签检查只随机三组，原始40/610有误label(6.6%)、变换157/1838(8.5%)，不是每条原标签不变；truncate可能改变内容/语义，发现及验证筛选也不是自然人口因果估计。保留有限结论，不授受测judge全场景安全或 truly causal bias 分类。root 已实际核 Table6/§4.1直接反侧，普通 Books owner 比较待执行；不再读全H/50bias附件。

## [n-Musketeers 2602.09173v1](https://arxiv.org/pdf/2602.09173v1)

2+2+2=6，标准必要证据完成。HTML标compiled August24与精确PDF标compiled February11不同，故采用固定v1 PDF必要方法/评价而不自动继承重编译HTML；官方abs仅一个v1，完整题摘身份相同，无现成撤回/纠正标记。实际PDF §3/4.1–4.4/6（P2–6，L260–927）支持：各冻结专家own tokenizer最后层pooled hidden，经维度投影至512、Perceiver latent queries crossattention+FFN+近零output投影作policy softprefix；专家无decode不等无专家forward成本。Qwen2.5-3B-Instruct LoRA8，GRPO group8/KL.04/effectivebatch32/lr1e-4，ReasonGym500steps/GSM233，单H200，3seed均值与std，generation128tokens与8query/8heads；precision Not Disclosed。同生成预算不等总算力，hardrouter只执行top1而本项全专家，其对照不是完整router设计空间。

Table1 default arithmetic75.26±5.62 vs single52.34±1.78，但Logic82.81<96.88、GSM61.59<64.32，generalist GSM41.02±29.01；无需多专家的环境有干扰且波动大。§4.3 reward/attention entropy时间相关与capacity preference混杂，不证明真实任务动态分工因果。§4.4 firsttoken75.13±1.12近lasttoken75.26±5.62，shallowlayer更差；原文据此提出粗/近prompt-invariant模型signature已可能足够，而非已因果证明静态偏好是全部收益来源。§6不以效率为目标。只采用隐藏表示接口与“更选择性权重不授分工”边界，Books owner比较待执行。

## [RFID-MoE 2602.09316v1](https://arxiv.org/html/2602.09316v1)

2+1+2=5，标准必要证据完成 §3.1–3.4/Alg1、§4/Table2–5及结论。对expert按routingfreq分组，共享低秩basis；allocation把normalized activationfreq与squaredsingular谱的effective rank线性融合，而非frequency直接等重要性。K_g=max(1,floor(K_total*C_g/sumC))保留小组最低rank，但不能由该表达授全预算精确守恒。稀疏one-hot P的列按count归一、共享group，η残差投回weight；PᵀP=I只保证低维latent度量，不能授任意全维残差/语义保真或lossless压缩。只压expert up/gate，calibration WikiText1024samples，每四expert一组，η原参数3%挤占A/B预算；8A100，precision及端到端latency Not Disclosed。

四类MoE模型zero-shot LM harness：受测rank/freq融合多数优于统一/单维度分配，但个别任务低于MoBE或原model；Qwen30B60%压缩avg.64<original.66，不授无损。WikiText/C4 calibration分别改变下游PPL，α/ξ最佳随ratio变化；稀疏projection效率/残差收益不是实际GPU部署吞吐验证。大235B有限PPL支持不授全任务能力。Books owner MODEL-MOE 的具体低秩rankallocation比较待执行，不采用“information density=真实expert知识重要性”。

## [VLM-UQBench 2602.09214v1](https://arxiv.org/html/2602.09214v1)

2+1+3=6，标准核心 §3.1–3.3、4.1–4.3/Table2–5及limits，另定点A.1标签/A.2 oracle、B.4–5强度校准，C.1–2只必要定义/范围（不遍历全部图）。VizWiz各150模态subset由阈值+三expert review；grounded ambiguity60amb/80unamb；CLEVR scenegraph正确clean→perturb后错误定义其hallucination，是任务答案翻转而非真实视觉推理的因果分类。四VLM（Kosmos2、QwenVL、LLaVA、GPT4omini），9既有UQ方法，greedy0或temp.7采10，其他LMPolygraph protocol，硬件/precision/全调用cost Not Disclosed，闭源缺logit项记缺失。

采用的反侧：group-level明显歧义AUROC/F1不移交为instance-level微小语义变换下risk calibration；URR只计uncertainty是否上升，HCC是ΔU与答案翻转point-biserial相关，均非calibrated风险概率。Blur在Qwen属性任务64.7%翻转，而对应UQ敏感/相关弱且模型依赖；crossmodal perturbation可能改变GT，作者明确不将其纳入hallucination同标签比较。B.4人为选能看见artifact但人仍认出object的强度，强弱两端会trivial/noanswer，不能授一般鲁棒性。小curated core主观性、人工强度heuristic保留；需要部署按模态/扰动验证，而非从entropy alone授可靠abstention。Books具体owner/覆盖待比较。

## [Timing and Memory Telemetry 2602.09369v1](https://arxiv.org/html/2602.09369v1)

2+2+2=6，标准核心§3–7，必要§11 observability。采用具体反侧：CUDA scalar/VDF、tensor GEMM与memory-hard/hash三类probe观测不同资源争用，random CHAL HBM vs pinnedhost访问能给statistical residency线索，不能以一般GPU utilization counter合并成可信execution proof。两阶段freshnonce/BLAKE2mask+Argon2id访问；数值drift fingerprint只能class，不标识单device，同类GPU outsourcing在其threatmodel允许，原文也承认不是securebinding。host/device全不可信案例不提供cryptographic attestation，challenger时间/合法dataset正确性与挑战响应仍条件性假定。

Python/CUDA12.4、T4/H100；hash/VDF T4同TinyLlama1.1/约2GB、Qwen2.5-7B约9GB及Llama2 FP16约12GB争用，GEMM H100 FP16mul/FP32accum/Freivalds5。H100 CHAL60GB、hot/cold550samples冷访问差>350ms，明确强制HBM或pinnedhost placement，非真实adversarial逃避实验。noncontinuous uniform120s、10min overhead观测；nominalPoW2^24与Figure2^13各自保留。连续probe抢计算/带宽，residency自身HBM占用很大：低dutycycle低power不等低memory/全负载无干扰。没有正式threshold/tests、FP/FN未量化、远端network与privacy时序泄露/同类offload/调度规避需校准；不授counterless生产合规检测。未复现。Books具体owner比较待执行。

## [LaPha 2602.09375v1](https://arxiv.org/html/2602.09375v1)

2+2+2=6，标准核心§2.1–2.4、3.1–3.6/Table1–2、5，必要A.1search/A.2valuegradient/A.3/A.5配置。Meanpool dialogueprefix hidden、减root/√H并exp映射到Poincareball，依当前树verified-success leaves定义V=droot/(droot+dnearestgoal)；linear-sigmoid valuehead回归此target，MCTS用value+likelihood初始化、terminal outcome才backup，近latent聚类prune供固定simulation下探索。不把几何distance当语义真值/真实进度oracle，训练有成功leaf才能构target，filter成功率(0,.8]与tree reward跨度>.01改变采样人口。

Eq7边reward为Vj−Vi，但§2.4 scalarR沿root→leaf聚合且同Adv共享tokens，reviewer推导为Vleaf−Vroot望远镜，不能由“dense”名称授逐step-local credit；该rollout-dependent/frozen条件未给一般PBRS policy-invariance证明，标准PBRS成熟原则不计分。Table2同model/rollout/优化几何消融Poincare30.0/26.7/79.6 vsEuclid13.3/10/70.5支持受限几何接口，不鉴定内部语义进度。sg128提高有限math成绩但额外search/tool预算，1.5B Olympiad38低于ToRL44、MATH/Gaokao个别也不优；A.2 backbonejoint76.4vsstopgrad67.2是其配置。Table1从base蓝字不授公平RL全预算对照。

Qwen2.5/Math1.5B/7B，SFT混合Glaive/OpenR1/NuminaTIR两epoch、RL DAPO17K；main4epoch与A.5 YAML8epoch冲突，不统一；BF16/TF32、depth6/breadth6/sim24/prune8、prompt3072/completion1024/temp.7/p.8/k20、16独立生成均值；硬件、seeds/uncertainty、全E2Ecost Not Disclosed。只采用几何value/search与nearestgoal有限条件，不授普遍长horizon优势或无额外model所以免费。Books比较待执行。

## [Refusal Vector Fingerprint 2602.09434v1](https://arxiv.org/html/2602.09434v1)

2+2+2=6，标准核心§3–7，具体安全/provenance反侧读C.1/C.3/D.3（不采用B未验证ZKP）。Harmful/harmless最后token centroid差、每layer归一再选中间层平均，得到whitebox家族方向与512bitSimHash；不是拒绝率行为黑盒probe。10K balanced prompt（AdvBench/JailbreakBench vs Alpaca/ShareGPT），C.3中间90%层/BF16；硬件、全调用budget、seeds Not Disclosed。七base模型2B–70B，家族识别报告76 derivative/6family而初始setup七base，比较表另外48cases；分母分开，不合成一个全局准确率。数据为HF likes排序至Sep2024的有限人口而非真实未知API。

Table1 quant/adapters/SFT/merge大多保留方向，但SFT最低.681、merge.669，叙述标准derivatives全>.8或fine-tune全>.9不符表，不采用；pruning.295、distill.568不能外推普适heritage检测。D.3仅两alignment-breaking variant .4746/.5020，相对八independent模型近零仍有限可分，但不是targeted擦除安全测试。主top1 100%是closedset，τ=.2为样本内gap建议、无外部open-set校准；blackbox的secret elicitation FSR不是相同任务，不能把52/58对100作等价鲁棒性胜负。§7明确针对拒绝subspace旋转攻击未测，ZKP/escrow只是拟议路径而非已实现绑定。采用whitebox安全行为几何作有限provenance线索，不授API归属证明或安全tamper必检；Books比较待执行。

## [Align-TI 2602.09483v1](https://arxiv.org/html/2602.09483v1)

2+2+2=6，标准必要§3–4/Table4–8、B.1/B.6、E.5/Table18、F。IVA选instruction-to-vision attention跨query变化最大的IRS层，将teacher attention聚合作visual token KL权重；不是attention权重直接证明视觉因果贡献。TPA在GT prefix上采student next-token alternatives，再对各one-step conditional distribution做teacher KL；ribbonmask让candidate仅看共同GTprefix、互不看彼此，在expanded sequence一次teacher/studentforward计算。d=4不等全|V|²真实覆盖或完整长horizon onpolicy，候选/teacher仍有support限制。

Teacher Qwen2-7B/Qwen3-8B、student.5/1.5/.6/1.7B，SigLIP-B14/两层MLP；teacher8A100 LLaVA558K/665K，student16H20 1.2Mcaption+2.4Mmixed，fullfinetune一epoch/lr2e-5/batch128，precision/seeds Not Disclosed。Table5 avg64.3→66.7、TPA66.4，SQA IVA58.0<baseline59.0且combined60.7<TPA61.0，非单组件每任务严格win。Table4训练355h→509h(~1.4x)，memory70.6→75.6GiB；E.5同样时间扩Vanilla至1.5epoch533h只有65.3，提供限定budget反侧但不是所有distill方法全费用控制。IVA额外很小不授TPA免费。仅image-text，不授video/continuousaction转移；不采用粗跨模型TTFT宣传为本机制速度因果。Books具体owner比较待执行。

## [SchröMind 2602.09528v1](https://arxiv.org/html/2602.09528v1)

2+1+2=5，标准必要§2.1–2.4/3.1–3.3/Table1–2/4，固定activation steering方向改为unpaired hallucinated/factual activation分布的conditional bridge：perhead logistic classifier选topH，Gaussian-mixture potential近似SB/EOT，selectedhead按当前位置/时间drift+noise修正，image/object两种分布分别fit再合并。新增是input-dependent非统一向量接口，不采用“truth manifold”语义真值或数学transport最优等视觉事实保证。

LLaVA1.5-7B/Qwen2.5VL7B，1500activation sample筛head，POPE27K balancedyes/no三dataset/三采样，MME14维；head数具体取值、Gaussian mixture数/steps/ε、训练分割、硬件/precision/重复seed与总E2Ecost Not Disclosed。ICT据officialcode复现；Table1 GQA random89.23/89.22低于ICT89.3/89.49，Table2 MSCOCO randomF1 85.68<ICT85.84；不能称universally superior/no能力代价。Combined也有MSCOCO adversarial87.33低于object-only87.5，synergy并非每格最优。没有运行开销/能力保持充分对照，结论“without increasing computational cost”不采用，drift求值和noise本身有执行条件。有限object hallucination实证不授高风险部署或全部输出faithfulness；Books比较待执行。

## [SAKE 2602.09517v1](https://arxiv.org/html/2602.09517v1)

2+2+2=6，必要§3.1–3.2、4.1–4.2.3、5.1–5.2/Table1–2、6.1–6.3/Table3及limits实际读。固定gold文档的受控pre-search reasoning长度比较支持编码位置边界，而非证明唯一attention因果。SAKE保持原交错history，同时把外部文档另按新到旧堆在question/旧reasoning之前：causalmask让这一副本文档不看旧推理，原交错slot仍存在。Repeat只将新文档原位重复、StackOnly删除交错视图，受限MuSiQue对照支持双视图而非所有重复token都有收益。

Qwen3-4BThinking/30B-A3BThinking/QwQ32B；wiki语料Hotpot66K/2Wiki56K/MuSiQue101K/FRAMES25K，Qwen3Embedding.6B top5/最多10次 vsStandardRAG一次top10；GAIA在线搜GPT4.1mini。temp.6/p.95/k20/minp0；文本4096tokens/step总30K、GAIA8192/step总50K，RAG总16K不同预算不能直接归因整个流程。F1与FRAMES/GAIA judge accuracy分开；硬件、precision、seeds、总E2Ecost Not Disclosed。GAIA QwQ Level3 SAKE8.33低于Search16.7、Hotpot4B RAG48.6高于SAKE47.1，不授普遍超RAG。文档复制增加context；重新插入prefix可能改变已有KV可复用性是reviewer推断，不声称作者实现已测。不会保证检索文档真值/不被注入或所有旧推理偏差消失。

## 第二批真实 owner 差额停点（待独立核）

- 09173：Ch82 L274–334 latent contract、StateBridge已生成hidden-suffix闭式对齐、XKV jointcache都有具体读取接口；尚未承载冻结专家各自无decode forward→learnedPerceiver softprefix→RLpolicy。拟在latent分支后增加两段，不采用动态分工因果，更多专家无decode仍算全部forward。
- 09316：Ch21 L786–813已有frequency/precision与qualitysensitivity分账；尚未承载frequency+effective rank分配压缩rank、sharedbasis+sparse latent残差。拟两段局部分支，PᵀP不授全维lossless、不宣称E2E加速。
- 09369：Ch72 L122–138已有physical fingerprint需trustedpath/attestation与adversarytier；尚未承载不信任host时用分资源challenge观測争用/统计residency而非deviceproof。拟此处两段，CHAL占HBM且同类offload允许，不能授远端绑定。
- 09434：Ch59 L78–90 byte/behavior integrity、L348–354 privatebehaviorproof及L110–116adapter weightsensor实际读。拒绝方向需whitebox，不像signature/digest/privateproof具绑定；拟在behaviorproof后两段家族provenance sensor，阈值closedset/targetederase未验放正文，不让统计sensor有promotionauthority。
- 09483：Ch29 L230–248 densityweightedrepresentation、L624–635onpolicy state mismatch实际读；尚未承载instruction跨query变化选teacher视觉KL权重、GTprefix局部alternative的一步conditional KL/ribbonmask。拟在onpolicy说明后两段接口分支，明确不是完整onpolicy/不免费。
- 09528：Ch23 L840–856 existingconstantsteering/readvscontrol实际读；尚未承载unpaired hallucination/factual distribution conditional drift/noise代替constantheadvector。拟两段输入条件干预分支，不采用formalSB语义真值/无成本/全任务更好。
- 09214：拟已有覆盖/仅报告局部新反侧。Ch66 L551–580 slice/选择偏差、595–616 hiddenregime/semanticneighborhood/jointUQ已明确sensor并非概率与部署验收；本项instance perturbation下URR/HCC不校准与有限VLM反例可留报告，不强造新概率接口。待root判断具体覆盖。
- 09383：拟仅报告局部新反侧。Ch66 L580格式/语义控制、L2317–2325 lengthdeconfounding及L271–295judgeartifact/safetytruth已承载实际判断条件；Table6残余2.2pp和有限labelcheck没有新通用biascontroller，不为50bias新榜造diff。待root核具体覆盖/处置。

## [TDAR/BACD 2602.09555v1](https://arxiv.org/html/2602.09555v1)

2+2+2=6，标准核心§3.1–3.2/Alg1、4.1–4.2/Table1、5.1–5.3、6.1–6.3/Table2–4及B/C/D必要配置实际读。BACD用当前block已unmask置信度均值clip到[τl,τh]，初始τh，空集合仍放最高conf一token；bounded是阈值界，不是correctness/recoverability保证。TCCF生成到`</think>`替换为检查指令，从B16切B1，第二段再生成，不自动定位/修复第一段真实错。Progressive B4→64额外SFT stage，固定smallblock直接解码不是同训练人口。

Qwen3-8BBase 50B CPT+B3B长CoTSFT每阶段3epoch，选B16；同recipe AR但目标不同；LMDeploy/H200、temp1、无topP/K、max30K。Main TPF=generatedtokens/forward不是墙钟；D同单H200 BS1–32测BACD TPS195→1675，只此受测configuration，无precision/SLO/E2E训练预算与uncertainty披露。Table1 BACD在AIME25/LCB/GPQA小反退；Table2无upper Math83.6>83.4；Table4全B1准确率更高，mixed更快并非质量更好。Table4含重复critic生成，Table1/4相同配置部分值不一，不合成单统一成绩；不采用stable performance lower bound。只采用block-local阈值history及不同role/blocksize采样接口，Books待比较。

## [BG-MCTS 2602.09574v1](https://arxiv.org/html/2602.09574v1)

2+2+2=6，核心§3.1–3.5/Eq2–7/Alg1、4.1–4.2/Table1–2、5–6/Table3及C预算定义实际读。剩余outputtoken比例ρ同时衰减PUCT探索、增加经验answerdepth归一completion bias，virtual generative child以mean+λρvariance跟既有branch竞争。新增是把widening变成统一选择与剩余预算联动，而非generalMCTS原则；PRM方差不是calibratedepistemic。无answer时用maxdepth，深不等更接近正确，budget循环生成后才检查可越过名义B。

Llama3.1-8B/Qwen2.5-7B/GenPRM7B，MATH500+AIME24/25，B10K/20K/30K，k2/c√2/κλ1，LightEval与regexgold；hardware/precision/seed/lengthfullcap/端到端cost Not Disclosed，tables均值两run。Outputtokens不包含input/PRM调用，不能授APIcosthardcap。Table2去exploit Llama10/30K和Qwen30K反好，组合非每cell最优；多数收益局部不是三组件普遍互补。LiteSearch表每instance独立cap/earlystop，图把surplusredistribute另人口，不合并；ABMCTSfullnode vs其他stepnode差异，scalaronlyPRM不复原原反馈条件。Treeanswered覆盖更低可同时answerednodeprecision更高，不混run/node分母；rewardnearbinary局部limits保留。Books待比较。

## [Blind Denoising 2602.09639v1](https://arxiv.org/html/2602.09639v1)

2+1+3=6，采用有限理论适用边界；实际§3.1–3.7、4.1、4.2必要对照、G.3，必要B.3–B.4证明路径。Blind population MSE denoiser对noise posterior边缘化，误差多一个noiselevel estimation项；可从高ambient/低intrinsic维单样本估计noise不等任意图像都可。A1 bounded support/A2 metriccover k²≪d/A3 weighted population L2学习误差，noiseprior覆盖/constantstep exponentialEuler与特定at条件必须保留；D_X依不可得support projection，仅suggestive perceptual不是FID/真实语义距离。常步结论不外推maskedlanguage/任意nonblind差模型。

重要不用的冲突：Corollary当前HTML写σ0≈ε/R，B.4初始化误差为R²/(2σ0²)，小σ0与其小误差要求不衔接；§3.6正文编号3.10而appendix仍3.6/3.3。只采用noiseestimation误差分账/条件，不采用该完整参数处方或一般收敛保证。B.3 posteriorconcentration条件化而非生产观测证书。13M vanillaUNet、CelebA/LSUN、4H100/24或34h、batch512/lr.001/1000epoch，盲/非盲同architectureexceptconditioning；训练prior1/√σ与分析σ^-3不同，empirical a_t.2σhat与证明.5σ²不同。PSNR近同与匹配seed/noise视觉示例、noise-estimator两sample轨迹不足证明唯一DDPM失败原因/高维场景SOTA；precision/repeatedtraining/FID/E2Ecost Not Disclosed。只采用明确适用条件，Books待比较。

## [Partitioned Entropy 2602.09651v1](https://arxiv.org/html/2602.09651v1)

2+1+2=5，标准核心§4.1–4.4/5.1–5.3/6、B/C必要定义配置实际读。不是统一CFG新算法：对非穷尽semantic class二分归一，conditional/reference重建差累计likelihoodratio，track posteriorentropy以诊断不同distinction的noise时窗。B实际强制prior.5不是真实classpopulation，unconditional近似complement，guidedexpectation后变crossentropy；不把曲线直接解释为正确语义/普遍该时刻commit。Gaussian有限equiprobable/isotropic/highdimension假设只理论背景，不采用任意model phase-transition定理。

EDM2XS/ImageNet512 stochasticDDIM NFE64/EDM σ.002–80/ρ7，highlight3000其余300samples；SD1.5/LAION5B NFE100/400samples。Guidancegrid每设置50K、FID/FD-DINOv2选择不同interval且precision/recall不同，不把最优质量榜合成单最佳。Modelconditionalcalibration/近似complement误差、prompt改动非单属性及SD细节能力限制均明示；hardware/precision/seeds/全grid成本 Not Disclosed。Estimator本身增加两branch读数/采样，不能称无费用guidancegate。只采用specificdistinction测量接口，Books待比较。

## [ScaleNet TTA 2602.09719v1](https://arxiv.org/html/2602.09719v1)

2+2+2=6，核心§3.1–3.3/Eq3–19、4.1–4.4/Table1–2实际读。每query freshLoRAQ/Vr4α16，prompt NLL K≤5steps，discard恢复base；first/lastmeanpooledhidden+stepK→128MLP两个perlayer非负lrscales，gold仅训练ScaleNet post-adaptanswerloss，训练截断Hessian二阶。新增不是LoRA/TTA一般原则，而是sample-specificlayer/QV/step学习更新幅度与reset。Eq2 q(y|x)∝q(x) under C不由Bayes成立，不采用；非负scale与metatraining也不保证任意prompt/answergradient内积正或单调conditional收益。

每dataset/model30Ktrain/300test，BF16，ScaleNetAdamW1e-4/baseTTA.01 vsfixedbaseline.05，未对齐base全lr搜索；hardware/seeds/端到端adaptationlatency Not Disclosed。Llama3.2-3B/Qwen3-4B variants及Llama3.3-70B/Qwen3-32B，XSum/SQuAD/NQ/AdaptEval。NLL下降不等生成质量；Table2LlamaNQ .2766→.2398/.2507、70B1step .2327→.2237反退；maxgen64/32/256限制，domain-tailored不同任务迁移未授。不采用layercontrol“必要”的普适措辞，额外反向/optimizer/ScaleNet资产与prompt安全需另验。Books待比较。

## [Size–Fidelity Paradox 2602.09789v1](https://arxiv.org/html/2602.09789v1)

2+1+3=6，标准核心§3、4.1–4.3/Table1–2、5.1–5.2、6.1/Table3、7实际读。Compressedcontinuousmemory→固定Llama3-8BInstdecoder，联合prefixreconstruction+continuationobjective；Qwen3.6–32B/Llama3.2 1–90B三压缩4/16/64，同claimedrecipe，不授相同FLOPs/hiddengeometry。FaithEval/ConflictQA counterfactual与DeepSeekR1生成结构QA，topic/relation/role/modifier七维及不可答项，给出BLEU/重建loss与counterfactualfaithfulness可反向的局部证据。

Table2非随每个size单调，0.6B→4B可进步；90B16x FaithEval.55 vsLlama3B.73，不能跨family用Qwen4B.71作纯scale因果。Fixed.6B训练postpeakrank/entropy与QA相关仍有共同训练进度混杂，r/p不证明“semanticcapacity唯一罪魁/causalcreativitytrap”。Table3更换decoder仅.6/4/8compressor不含90B，跨familyparagraph自矛盾“Qwenfamily”“Llamafamily”，以table具体Qwen population为准，不采universal表示内生根因。4.44Mreconstruction/598FaithEval/1431Conflict/449Fineweb×20QA、decoderQA能力与自动题标偏差需保留；硬件/precision/seed/完整training/latency ND。实际作为consumer-compatiblepairedfaithfulness反证，不把全compression都不该scale；Books待比较。

## 第二批必要 primary 定位（支持与反侧，不是独立核完成）

以下行号是2026-10-04当前web提取行，精确版本URL与§/Table/Alg才是稳定定位。09316/09369原HTML还在`exact-v1-bodies/2602.<id>v1.html`；其余下列项没有本日body cache，不把作者notes称为primary。

| 精确材料 | 拟采用支持位置 | 必要直接反侧 |
| --- | --- | --- |
| [09173v1 PDF](https://arxiv.org/pdf/2602.09173v1) | P2 L274–365 §3冻专家forward/Perceiver/softprefix | P4 L525–558 Table1；P5 L745–850 §4.3–4.4，capacity偏好未分辨/first-token近似；P6 §6效率非目标 |
| [09316v1](https://arxiv.org/html/2602.09316v1) | L119–280 §3.1–3.4 rank分配/latent残差 | L281起配置/Table2、L303起Table3–5 calibration/α/ξ；不授全维lossless/E2E加速 |
| [09214v1](https://arxiv.org/html/2602.09214v1) | L180起URR/HCC定义，§4.2 Tables2–5 | L285 crossmodal改变GT、L286起64.7%局部反例，B.4–5人为强度；非risk calibration |
| [09369v1](https://arxiv.org/html/2602.09369v1) | L187–218 §5 CHAL two-phase/class fingerprint | L97–104非proof；L207同class offload允许；L257–260强制hot/cold60GB；L527起§11观测边界 |
| [09375v1](https://arxiv.org/html/2602.09375v1) | §2.1–2.4 root/nearest-success potential/Eq7/scalar return | L202起§3.3同预算几何消融，L186–188过滤人口；main4epoch/A.5 YAML8不统一，差分聚合望远镜非stepcredit |
| [09434v1](https://arxiv.org/html/2602.09434v1) | L105起§3.2–3.4 whitebox拒绝方向/SimHash | L144起Table1/5.3 closedset；L230起§7；L358–366 D.3只有两alignment attack非targeted擦除 |
| [09483v1](https://arxiv.org/html/2602.09483v1) | L106起§3.1–3.2；L459起B.6 Alg1 ribbonmask | L200–219 Table4–5成本/单任务反退；L592起E.5 matchedtime及F限制 |
| [09528v1](https://arxiv.org/html/2602.09528v1) | L85起§2.3–2.4 conditionaldrift/head fitting | L115–157 Table1/2/4反退与缺配置，L160无成本不采用 |
| [09555v1](https://arxiv.org/html/2602.09555v1) | L131–175 BACD Alg1/TCCF | L185–207 Table1、L267–300 Table2–4；D只单H200TPS。固定v1 PDF题名同HTML Advancing Block Diffusion Language Models for Test-Time Scaling，P0 preprint Feb11，abs家族题名不同不继承最新版机制 |
| [09574v1](https://arxiv.org/html/2602.09574v1) | L116起§3.1–3.5/Alg1 budget联动selection/widening | L256–270 Table2；L396起C budget population，§6 reward限；后验预算检查非hardcap |
| [09639v1](https://arxiv.org/html/2602.09639v1) | L158起§3.1 posterior；L205–240 A1–3/error分账 | L264起supportprojection/Corollary；L624–629 B.4初始KL R²/(2σ0²)，不桥接小σ0完整recipe |
| [09651v1](https://arxiv.org/html/2602.09651v1) | L122起partition，L186–245 tracking/guidance | L246起limits；L458–480 B强制prior.5/conditionalapprox；曲线非新安全sampler |
| [09719v1](https://arxiv.org/html/2602.09719v1) | L105–224 §3 ScaleNet/QV/reset/firstorder | L225–230配置；L252起Table2/§4.4 NQ反退；Eq2 Bayes桥接不采用 |
| [09789v1](https://arxiv.org/html/2602.09789v1) | §3–4/Table1–2 L93–176 pairedfaithfulness | L177–203 rank相关；L212–225 Table3实际Qwen且仅.6/4/8；§7，不授size唯一因果 |

当前working而非frozen：首批13已处置，第二批16必要core已准备（含BiasScope/SAKE），另16普通core未完，09080日期单隔离，09629准入事实未定。所有来源与日期尚未收束；不得称45工作项均已确定落窗。未获共享Books锁。

## [SAKED 2602.09825v1](https://arxiv.org/html/2602.09825v1)

2+1+2=5，标准必要§3.1–3.5/Alg1、4.1–4.6/Table1–5、A.1–2、B.2/Table7与C限已读。CHSS按selected visual heads一致性、CLSS=1−邻layer token distribution JSD、CTSS=1−邻token visualattention JSD，加权KSS逐token挑正负layer logits contrast，再与原prob加权并限制原top20。不同邻token未必同entity，visualattention entropy/max与一致性只是signal；不采用“唯一hallucination根因/最stable就真”的桥接。

7B-scale五backbones、单48GB NVIDIA GPU（型号/precision ND），deterministic无sampling，参数topk/p/temperature均1，beam5；CHAIR500COCO2014 max512，AMBER64，POPE/MME10。Table1 InstructBLIP Ci14.0不如greedy13.3；POPE Intern.9027低于greedy.9074/MiniGPT.7639低于Deco.7714；AMBER QwenCHAIR3.8高于greedy3.7。Table4去CHSS QwenCi7.0优于full7.6、去CTSS InternCs30.2优于30.4，不授所有component普遍win；同LLaVA full Table1/4/5为11.6/11.0/11.6而未披露统一原因，不合并。B.2 Intern语言质量各项低于Deco，averageBLEU3/4亦不最优；词面指标非真实fluency。C说明CTSS短序列作用小，candidate layers/α/β需model-specific调；读所有layer/head注意力与unembedding的额外latency/HBM/完整成本/seed ND，不授trainingfree等无计算成本。拟只采用stability-conditioned layercontrast的限定接口；Books普通比较待执行，不自授新增diff。

## [Code2World 2602.09856v1](https://arxiv.org/html/2602.09856v1)

2+2+2=6，标准核心§3–5/Table1–3、A.1–2、B.1/Alg1、D.3.1–3.2必要reward rubric已实际读。新增GUI action-conditioned next-screen以self-contained HTML+确定browser render替代纯pixel，固定root坐标/SVG/semanticimageplaceholder；目标不是运行真实Android应用。GPT5 screenshot→HTML→SigLIP.9门槛/最多1次visual修订后不合格丢弃，筛选影响人口。Qwen3VL8B先codeSFT再renderedsemantic/action-consistency双judge reward，单visualreward的Table3 identifiability79.12→78.85反退，不能由视觉像素近授transition正确。

8H20×96GB；冻结vision/projector，全LM SFT2epoch/batch64/lr2e-5/cutoff24576；RL G4/temp1/batch16/lr1e-6/KL.01/prompt24576/response8192/equal两reward；precision/seed/总训练latency ND。Judge奖励与评价同Qwen3VL8Btemp.1/max1024（temp.1并不证明严格deterministic），placeholder忽略照片纹理只核结构/语义标签，action rubric是VLM自评非真实状态oracle。Table1对zero-shot通用code/image模型不同训练人口，OOD若干GPT5/Gemini视觉/逻辑项更优，不授普遍轻模型越大模型。AndroidControl-High Table2 SR是offline single-step，不冒充完整task成功；AndroidWorld116task/20app在线 Gemini41.4→50.9是9.5pp，Naive simulator仅+1.2pp，SFT47.5/单reward49.2或50.1/combined50.9，但没有全费用同budget/independentjudge可靠性证明。Propose K→simulate→select增加候选生成/HTML/render/judge成本，K/onlinehorizon/端到端延迟/失败预算未披露；预测screen变化不授hiddenappstate/外部sideeffect与permission认证。采用renderable结构替代分支及visualreward≠action consistency反侧，Books owner比较待执行。

## [MVISTA-4D 2602.09878v1](https://arxiv.org/html/2602.09878v1)

2+2+2=6，必要§4.1–4.4、5.1–5.2/Table1–4、A实现/相关B–D、H/I实际读。采用几何对应限制的deformable epipolar crossview、localRGBD融合与trajectory-level TCN-VAE条件；执行时先生成text-only固定future，再优化随机trajectorylatent100次generator反传匹配future、TCNdecode并pointbased residualIDM修正。latentcondition reconstruction只训练且推理弃，不称直接actionhead、真实可达性/逆动力学唯一解。

WAN2.2TI2V5B、全block微调AdamW1e-5/1000warmup、frozenTCNVAE、前50epoch actiondrop0后升.5，geometrysampling/localattention额外成本；train hardware/precision/总epoch/seed/完整latency ND。RLBench8K/RoboTwin10K轨迹各10task、real14tasks，camera数量正文16与B12不同原值保留；训练2–3view，主结果default两passmaskedcompletion/3view，对照至多2view“where applicable同WAN”不授全compute/view公平。100episode平均非CI；T3 latent优化RLBench72.6vsActHead72.5、Robo43.0vs42.5小效应未鉴定普遍必要。T4 PutOrange63<66；T1PSNR/SSIM不每项优。

H给drawer错误拉向、contactnear-miss：highlevelfuture合理不等geometry/contact足够执行；I明示多步优化增latency、camera/kinematics calibration偏移影响动作。C实际real6task先核predictedvideo错误即计failure，再decode/interpolate/execute；i9/RTX4090是采集机、200Hz是teleoperation，不冒充模型推理闭环频率。采用生成future→低维trajectory反推→residual修正的条件分支，不授safe/realtime/controlguarantee；Books普通比较待执行。

## [BagelVLA 2602.09849v1](https://arxiv.org/pdf/2602.09849v1)

2+2+2=6，标准必要PDF P4–12 §3.1–3.5/§4.1–4.3与P18–19 A/B文字/D实际读；HTML不可用，官方export精确v1完整40,045,985字节有限恢复于`/tmp/feb12-bagel.4KnUEi/2602.09849v1-export.pdf`，不把此前2MB部分下载当完整原源。采用的新增分界是双flow-matching的action expert可读初始图像噪声步骤的KV而不等待fully-denoised未来图；RFG令初态为N(current-frame latent,I)，action仍多步去噪，single-step只指image-conditioning。Complete先完整预测后action、Joint同步两路径、Single-step固定最初context三种方案是具体控制条件，不授预测图真实可达性。理解/生成各7B与action2B专家，未来全图并非动作执行的必要产物；关于背景聚焦/中间OOD是作者假设而非唯一根因证明。

Table4 Calvin single-view、每种10K trainsteps、image50/action10去噪、单A800每chunk计时20次：Complete6.04s/2.480、Joint2.90s/2.038、Single1.23s/3.345、RFG1.23s/3.600；同受测条件支持路径/latency局部取舍而不授所有VLA更优。主Table1 two/three-view与fulltrain不同不合并该消融；主真实basic的PutFlowers35低于π0 40/VPP50，planningaccuracy显著高于任务SR保留fine-control缺口。主1.2s/chunk RTX5090、chunk48对应40Hz是动作输出摊销，72Hz另异步旧image/context复用，不是每秒72次新视觉反馈或完整请求latency。

D lr1e-5/FSDP：pretrain64A800 batch约1600/20Ksteps；Calvin8A800 batch192/30Ksteps/chunk10，无proprio；RoboTwin8A800 batch128/60Ksteps/chunk16每3步采样horizon48；real32A800 batch512/50Ksteps/chunk24。Main叙述实时chunk48与D real24未统一，precision/seeds/CI/fulltrain cost ND。§3.5与C.1的QA2.98M/2.56M、self-collected75K/4.5K及publicrobot分组数量不同，保留冲突，不授一致人口/全compute公平。只是采用partial-forecast-context→action条件替代分支，不采用planning必然正确或formal safety；Books普通比较待执行。

## [AdaTSQ 2602.09883v1](https://arxiv.org/html/2602.09883v1)

2+1+2=5，标准必要§3.1–3.3、§4.1–4.4/Table1–4实际读。拟采用temporal activation allocation与staticweight calibration分责：gradient-squared Fisher指导层/时步3/4/8精度，beam筛非支配(bit-average,MSEsum)后只保留距origin最近有限M条，最终小batch生成质量挑方案；不是全空间最优Pareto保证。Budget是layer/timestep平均bit，非parameter/FLOP加权或真实费用hardcap。Weights不按时步重复保存，用Fisher时间softmax加权ΣαXXᵀ校准；equivalent√α features是校准接口，GPTQ成熟原则本身不算增量。

FluxDev50steps/Schnell4/ZImage10/Wan2.1-1.3B25，GenEval与VBench不同评估；Table1 FluxDev4/4 total.6183低于FP.6667；Table2 Wan4/4 imaging.5626低于FP.6055、motion.951低于.9558；不能采用正文“allmetrics faithful/virtuallyindistinguishable”。Table3仅FluxDev3/3消融fulltotal.527>uniformcalib.466，但ColorAttribute.290低于Fisher-only.4191，非每component/任务严格互补。Baselines“optimal settings”没有明确全搜索/校准预算一致；calibration样本/全质量选优调用数、precision beyond requestedbits、重复seed/uncertainty及实际runtime kernel/throughput ND。

§4.4单A10080GB搜索约4分钟不含披露不明的最终全质量筛选/部署代价；Table4 modelsize/FLOPs是理论值，无实测latency或吞吐。正文80%3bit/10%4bit/10%8bit按字面平均3.6bit，与声称3.1bit不符，不采用其5.16x精确物理成本换算；weightsstatic3bit模型尺寸另与activation平均分账。时间敏感校准可有限采用，不授edge可部署/内存与compute同步5x或新最优精度定律；Books普通比较待执行。

最新普通停点：working45仍未冻结，首批13已处置；第二批21必要core已准备（16+SAKED/Code2World/MVISTA/BagelVLA/AdaTSQ），普通11未完。09080日期保留、09629准入含糊事实另记，不计作确定落窗家族。root新核09316/09369/09434/09528必要source通过；尚未授其Books差额/写锁，其他有效POST不重审。

## [Routing, Cascades, and User Choice 2602.09902v1](https://arxiv.org/html/2602.09902v1)

2+2+2=6，必要§3.1–3.3、4.1/4.2 Theorem1–4、5/6 Proposition1–2、7限制及C.3/C.4采用部分实际读。唯一provider/twomodel/唯一user、p固定iidBernoulli、已知route/cascade/value、stationaryabandon、subscription用户无每call价：provider minimize expectedcompute+Pabandon，user maximize VS−cumulative latency，因此costper-success排名与用户t/p排名可不同。新边界不是通用routing成本原则，而是失败后用户是否继续由route内生决定；不采用“现实所有cascade无用”。

采用§6窄反例：原两model净值Vp−t>0，若P≤min(c1/p1,c2/p2)，把双方t抬到Vp之上会让q=1；此时只付c_i+P(1−p_i)≤c_i/p_i，可比原最佳成本而用户价值恶化。这是模型内存在性/充分条件，不是观察到厂商throttle或P高于阈值一般免疫。无真实用户实验/估计P，task feedback可使p变化、隐藏route/多人/付费API均未覆盖，hardware/precision/performancebench不适用。C.3第一分式U1−U2展开符号与直接代数相反、mixedcase首式漏s等排版/代数错误不采用；只采用可直接由§3闭式与上述不等式核出的有限命题，不授全部threshold证明正确。Books普通比较待执行。

## [Pre-Generation Success Probes 2602.09924v1](https://arxiv.org/html/2602.09924v1)

2+1+3=6，必要§3.1–3.3/Table1–2、4.1–4.4、5.1–5.5配置/反侧实际读。相同post-instruction activation线性probe分别预测humanIRT、MCmean success、greedy/Maj@5或codePass@5，后三者不是同标签/概率。Bestlayer/position/α按validation选择并Plattscale，不授AUROC=风险校准。采用有限反侧：GPTOSS20B low→high任务accuracy.866→.920，平均probeAUROC.78→.64；Table4 MATH.848→.855却提高、AIME.731→.375下降，不能称每任务单调。更多CoT可能改变linearaccessibility，不证明难度信息丢失、唯一根因或nonlinear不可恢复。

MC Qwen50rollout/GPTOSS5，binaryMaj5；各dataset独立训练不做跨域transfer。vLLM GPTOSS max131072/temp1、R1Qwen7B32768/.6、Math3000/.7、Coder4096/.2；hardware/precision/seeds/CI、probe前向/HBM/全训练筛选cost ND。Routing只基于outputtokens×Fireworks挂牌估值，不含读多modelactivations/input/latency，不能授生产费用节省。§4.1cascade模型1.5→7与Fig3/§4.2的7→GPTmedium不一致；MATH“$15vs28=70%”算术不符且Table8high40/router10.35(accuracy.917<.920)/28.37(.930)不同值，AIME/GSM费用也不统一，不采用17–70%保证。采用policy-specificlabel/受限linearprobe反证，不采用精确costfrontier或普适预知成功；Books普通比较待执行。

最新普通停点更新：第二批23必要core准备，普通9未完；8项限定necessary source经root实际核通过，Books差额不继承通过，无当前共享写锁。

## [VersaViT 2602.09934v1](https://arxiv.org/html/2602.09934v1)

2+1+3=6，必要§3/4.1–4.3/5.1–5.3 Tables2–8、8.1–8.2/9.1–9.3/12实际读。只采用MLLM视觉骨干的表示边界，不纳入下游depth/segmentation领域应用：同Qwen2VL骨干Table4继续VQA/caption使VQA64.8→66.1但NYU RMSE.541→.557、ADEmIoU33.6→32.0；单global language-alignment改善不认证densefeature保留。多粒度监督可在该配置改善共同backbone，不是“task heads天然隔离gradient冲突”证明。

具体训练三任务alternatebatch累计完才统一更新，DepthAnythingV2伪depth/SAM+caption伪mask，所有backbone/head/LLM解冻；3.1视觉Qwen2与trainingLLMQwen3-1.7B，VQA评价另8B，两者不混。BF16/AdamW/ZeRO2，VQA percard8/max896、dense32/532或560，不同dataset重采同steps。独立reviewer实际§5.1纠正配置：caption alignment为128H20/batch1024/lr1e-3/1epoch；joint visionencoder/projector/textdecoder lr1e-5、其他1e-4，另1epoch；joint硬件不能由上阶段推定，seed/fullcost ND。9.3的128H20/5epochs仅额外depthFT不当联合主配置。Table7 35M-caption baseline不能全排除数据分布/伪标签与监督差异；Table5 lossweights各任务最佳不同；Table2 MMBench/AI2D小反退，Table3仍低于DINOv3部分dense项，不授通用best encoder。固定dense与dynamicVQA resolution可能任务bias明确保留；采用语义/dense兼容性需分别测的有限反侧，Books比较待执行。

## [ESTAR 2602.10004v1](https://arxiv.org/html/2602.10004v1)

2+2+2=6，必要§3/4.1–4.3/5.1–5.4/6.1–6.3 Tables1–2、A.1–A.2/A.5实际读。新增mid-CoT自主stop proposal经外部LightGBM接受，训练fullanswer一致性SFT+goldverified截断/GRPO、按新轨迹更新classifier；部署没有gold，ρ≥.9仅sensor不是correctness证书。SFT前5处matchedprefix且错误原轨迹加goldhint生成correctedtrace，训练人口已改变。Top20answerbucket/累计winner/slopecurvature的局部稳定，不等posterior所有answer无未来翻转；Theorem3.1期望tailvariation未知，不是可在线精确算证书，A.1一个answer-logprob局部plateau不能上界全分布未来变化，无formal/calibrated guarantee采用。

Qwen3-8B主，Classifier closedUSMLEtrain/openDeepScaleR；CoT temp.6/k20/p.95/repetition1.2，forcedanswergreedy，SFT明确MATH500而同MATH500评价未给分离说明，不采用其无污染普遍generalization。SFT8GPU/lr2e-5，RLbatch256/G16/39steps；GPU型号/precision/seed/CI/E2Elatency ND。Table2 AIME3788比Lite3045更长、JAMA56.10低于FT57.2，模型收益非每任务双赢；A.5阈值.99→.8准确77.53→73.76且coverage升说明实在质量/退出取舍。A.2的early-stop-answer logprob等特征可能需生成answerbranch，正文宣称online-top20未给全branch成本，不采用廉价无额外调用/CoT缩短等于墙钟加速。MedicalQA只作受测人口，不采用医学应用结论；拟采用proposal/gate接口及一致性≠真值边界，Books待比较。

当前普通剩7：10021/10044/10097/10098/10099/10104/10109；第二批25必要core准备但独立source/Books/逐项日期仍未全收束。09629含糊准入另定点，09080日期保留，不以待办数作已冻结分母。

## [DRIFT 2602.10021v1](https://arxiv.org/html/2602.10021v1)

2+2+2=6，标准必要§3.1–3.5/4.1 Tables1–3/6、A.2 filtering/A.3、C.1与D relevant反侧实际读。采用query-conditioned分chunk知识LM→CPS末层hidden→3layerprojector→reasoningprefix接口；预训练decoder冻结全context重建8x，第二阶段仍冻结只重建question evidence32x，最后QA才更新reasoner。Bucket按input-length上界固定输出预算，不是已测实际query信息量自适应；query-aware内容选择不等数量适应/真实事实清洗。8K训练chunk外长文分开编码后按原序拼接，未显式核跨chunk联合encoder关系。

主Qwen2.5-3B+Mistral7Bv.2/另Qwen7/14，LoRA16/32/.05 lr1e-4/batch128；hardware/precision/epoch/seed/CI、parallelchunks concurrency/256K TTFT完整runtime ND，因此不采用7x端到端普遍速度。T1仅512–1024重建BLEU/ROUGE非counterfactual事实保持；T2 L-EvalQA/LoCoMo多项低于vanilla，32→128某些任务反退，T3没各stage等更新预算不授必要因果。Qwen72B既生成过滤DocumentQAevidence又评估准确，自评evidence不授外部真值。D generalcapability雷达caption明确placeholder、KL曲线增大不能证明specialized reasoning/faithful，不采用无遗忘与新推理因果。只采用可审计的query-conditioned latent训练权限/消费边界，Books普通比较待执行。

## [Optimistic World Models 2602.10044v1](https://arxiv.org/html/2602.10044v1)

2+2+2=6，必要§3.1–3.2/4.1–4.2.2 Eq4–10、5/6、A.1/A.2 Tables2–5/A.4实际读。RBMLE是成熟原则不计增量；具体新实现把imagination trajectory的advantage乘transition logprob并加modelentropy，反向改变world dynamics，而非只改actor或UCB calibratedconfidence set。Replaylikelihood仍保留，optimism是训练偏置，不是预测真实性/实际可达性认证。Tabular渐近条件α→0且tα→∞不覆盖constantα=1e-4的神经POMDP；gradient-based convergence原文列未来工作，不授最优策略/ regret界。

Dreamer/STORM同其base hyperparams，modelentropy3e-6/3e-4；每实验单A100，timing另RTX4090 MsPacman五seed138vs115min（20%更久）与178vs170，不能称免费。Atari100K=400Kframes、DMCproprio500Ksteps/vision1M，O-Dreamer10seed其余5seed、20evalepisode/checkpoint、SEM曲线smooth3，precision/fullarchitecture/全部训练latency ND。A.2 Dreamer Breakout/BankHeist、STORMPong/Seaquest等反退，O-STORMFreeway mean6.38但IQM/median0不授稳定探索成功；α.1或η.03崩坏。仅采用偏置world-transition训练的可控替代分支与过度optimism边界，不把行业所有wm必须乐观化；Books普通比较待执行。

普通剩5：10097/10098/10099/10104/10109；第二批27 necessarycore已准备，尚未独立核的必要命题/Books尾部继续，source与日期未冻结。

## 第二批独立必要源与实际窄写（整日仍进行中）

root实际独立核8项09173/09316/09214/09369/09375/09434/09483/09528及六项09555/09574/09639/09651/09719/09789必要支持/反侧，限定范围通过，不等Books与日期通过。六具体owner差额亦已核并授锁，实际写两段+末注：09316 Ch21 L807/809/1002；09369 Ch72 L134/136/4113；09434 Ch59 L354/356/417；09528 Ch23 L856/858/1159；09173 Ch82 L340/342/1285；09483 Ch29 L637/639/1248。作者实际顺读各前后、scoped diffcheck通过，root POST待验，锁仍持六文件；不自授完成，其他有效11POST复用。

## [Step-resolved data attribution 2602.10097v1](https://arxiv.org/html/2602.10097v1)

2+2+2=6，必要§2/3/Eq2–15/Alg1、§4、§5与D.1/D.2配置实际读。对共享loop-body把总gradient按每次参数使用拆成φ_t，TracIn总training-gradient与testφ_t内积形成step轨迹；对teststeps求和恢复body总TracIn，不含非共享前后层，也不是逐step实际因果credit。CountSketch/TensorSketch在forwardactivation/backpropdelta上按参数tensor独立hash，无需materialize每example全gradient；concat后为αm而非单m，保存仍随example/loop/tensor数增加。Eq11 z/z′符号和Alg返回形状省α不照录为执行配方；hash无偏/variance假设不授因果必要性。

GPT-style135.1M τ32、seq128 FP32，singleA6000 48GB batch4→40、m2048/48tensor是对约100Mbody梯度~1000x维数缩小，不是整个运行内存1000x；相对SDI误差.0388±.003/TracIn.022±.0052为10sketch随机trial，不是十独立训练。Timing额外2.55s/checkpoint对inference baseline不等训练backward低开销。D.1 synthetic随机token只核fidelity，默认m8192与main2048分账。Parity代理alternating100%、实际test93%不能全域faithful；Sudoku晚期energy与difficulty相关不授halt判据，正文τ64与captionτ32饱和不统一。§5明确momentum/adaptiveoptimizer仅gradient-similarity、truncatedBPTT令早step零是graph构造，dense train×test/fullBPTT仍昂贵；reweight/remove行为、sharedfeature混杂均未证。只采用step-resolved测量/张量sketch接口，非训练数据删改authority或真实progress因果；Books待比较。

## [VLA-JEPA 2602.10098v1](https://arxiv.org/html/2602.10098v1)

2+2+2=6，必要§3.1–3.3、4.1–4.5 Tables1–4、5及A.1–2/B任务配置实际读。Qwen3VL2B仅初始observation+lang生成learnedlatent（8future×3token），冻VJEPA2作futurestatetarget，worldmodel causal跨time/步内双向以teacherforced过去state+latent预测next，actionhead再消费latent/proprio；未来label训练不等future输入泄露，但teacherforcedhistory也不能称全预测自回归部署正确。Deterministicencoder令KL自动消失的ELBO桥接不采用，Eq5差分未明范数不照录为执行loss；latentmotion与attention集中不证明控制语义/唯一旧方法failurecause。

8A100、每卡32/global256、VLMlr1e-5/world+head1e-4；SSv2约220Khuman+Droid76K预训50Ksteps，Libero2K30K、real100demo/3task20K；冻结targetencoder其余更新，16layer12head1024actionDiT、horizon7/FM4denoise。precision/seeds/CI/latency/fullcost ND。LIBERO每task50episode，spatial低于多个对照；Simpler human移除平均相等/Google反更好，而LIBEROPlus79.5→62.9有限支持扰动鲁棒性，非人video普遍动作物理知识来源。Baselines机器人人口/预算不同，不授同compute因果。T4仅直接LiberoFT T4/8/16平均94.8/96.1/95.5，非horizon越长越好；Table3 noise66.3低于π0/其他、camera低于π0Fast。Real每task10trials且banana50%与π0.5相同，OODgeneralization作者承认不如π0.5，peachgeometry反侧；重复grasp来源是作者假设。只采用初态latent监督与teacher-forcedtransition/action消费分界，不授真实可达性、安全闭环或无需机器人行动数据；Books待比较。

普通剩3：10099/10104/10109；第二批29必要core准备但未全部非作者source/Books/逐项日期收束。09629含糊准入与09080日期保留独立，working45未冻结；本日来源尾部继续，不扩大旧库存。

## [RJF 2602.10099v1](https://arxiv.org/html/2602.10099v1)

2+1+3=6，必要§2–3/Alg1–2、4.1–4.3 Tables1–3、5.1–5.3 Tables4–5、B.1–B.3实际读。采用明确几何接口：单位化representation/data与noise，SLERP训练路径、预测velocity投影tangent、exponential-map采样且重新归一，sinc²((1−t)Ω)给不同时间/端点pair加权。Riemannian FM成熟原则不加分，具体representation-path/采样/权重组合及同小模型路径反侧可核。LayerNorm的近恒norm不证明全部语义只在角度；单image angularloss能下降不鉴定fullpopulation capacity不存在，不采用唯一geometric rootcause。

ImageNet256、LightingDiT B/L/XL/RAEdecoder、Adam2e-4/β.9/.95/noWD/clip1/EMA.9995、80epoch/batch1024、50step/50Kimages；硬件/precision/seed/CI/训练与sampler总成本 ND。Table3 EFM24.32/SN21.99/RFM7.06/RJF6.77，同epochs有限支持trajectory比仅endpoint归一重要，Jacobi只是.29局部变化；200epoch4.95无guidance/3.37有guidance不混80。Table1B6.77与prose6.93，21.64/24.21/24.32不同baseline数字不统一；XL4.28→3.62是.66不是prose1.19。Table2RJFrecall.52落后多种方案，不授普遍更语义忠实/SOTA。Table4widthscaledDH仍改善且只.13，不排除capacity共存；Table5SigLIP/MAE局部改善不证明各自严格sphere。§5.3 radius27.7FID7.79而45FID6.77，decoder幅度敏感是新接口反侧，非全语义norm无用。

B的Jacobi公式作为作者weight启发保留，不授任意方向endpoint-error等价：alonggeodesic与orthogonal扰动的Jacobian不同，单sinc标量未覆盖所有切向分量；trainpathdata0/noise1而Alg2noiseinitial与t_i定义未闭合，不照录执行recipe。采用representation geometry/proposal与decoder radius分别校准，非formal收敛/唯一根因或免费generation；Books待比较。

## [Olaf-World 2602.10104v1](https://arxiv.org/html/2602.10104v1)

2+2+2=6，必要§3.1–3.2/Eq1–5、4.1–4.5 Tables1–4、A.1–A.3、B.1–B.2/C.1–C.2及F实际读。新接口为latentaction sequence均值经MLP，与冻结VJEPA2每frame pooled feature差的均值方向做cosine；该difference望远镜=(sK−s0)/K，不能称保存完整顺序/所有细粒度动作credit。Inverseencoder读x0:i+1允许未来transitionlabel，但没有真实actionlabel；冻LAM的每帧latent作WM AdaLN timestep条件，再训练action→latentadapter+LoRA用于具体控制。A证明只给reconstruction的context-dependent bijection非辨识，diagonalGaussian KL精确剩signedpermutation（退化isotropic例外），不是任意rotation都保βVAE或alignment证明唯一physicalaction。

MiraData3Drender/CityWalking；MIND1st/3rd共同8navigation/cameraaction，latent32/window16/λ.02；LAM16blocks1024/16heads，VJEPA2Giant384，8H200 batch32 AdamW2.5e-5/WD.01 β2e-4/100epoch146K约4.5days；SkyReels1.3B540p97frames压缩4，WM4H200 batch4/card/10Ksteps5e-5，LoRA16adapt1e-4。precision/seed/CI/adapt全steps/推理cost ND。Probe在源domain验证checkpoint再跨域，Table1F1与prototype相似度仅可读性不是因果控制；Table4full3rd→1st.5904低于nonorm.5934，不写所有grid最佳。

Table2 matchedbackbone/data/LoRAsteps有限支持RPE，但0/1video视觉质量/temporal多项低于AdaWorld；data3→5或rank32非单调，zero-shot4cases质例不授普遍。C2以ViPE重建pose+Sim3alignment算RPE，不是真实hiddenstate/sideeffect实测；OOD50初态仅appearanceshift。F明示singleeffect混camera/ego/other/environment，contact-rich与physics/planning是未来工作；同物理action不同cameraobservableeffect仍可能混淆。只采用共享effectreference减少局部coordinate任意性，不授真实控制因果/robot跨embodiment或physicsruletransfer；Books待比较。

普通剩1：10109必要反侧/config未完；第二批31必要core已准备，working45未冻结，来源/日期/Books普通尾部仍继续。

## [ST4VLA 2602.10109v1](https://arxiv.org/html/2602.10109v1)

2+2+2=6，必要§2.1–2.2/§3.1–3.5/Tables1–4、A PSS、B.1–B.2/C.1–C.5 Tables5–10、D.1–D.3与E.5 failure实际读。采用空间prompt+latent读取与梯度写权的联合接口：Qwen2.5VL3B的groundinghidden→8.7MB queryingTransformer固定queries→DiT/DINOv2 actionexpert；action梯度回VLM乘.5衰减，保留groundingSFT。新增不是dualarchitecture本身，而是同空间标签人口下prompt/read与可更新能力保留的具体边界/局部反侧。PSS只在最后层q2048²/固定64batch测两gradient矩阵列空间，trace(P1P2)/minrank对G→−G不变；nested不同rank也可1，不授loss梯度同向/全VLM无冲突或PSS1必identicalsubspace。PSS升.25→.42与success相关不能唯一因果。

16A100 Simpler actionbatch16/grounding4/50Ksteps约2.5epoch、chunk16；LIBERO8A100 batch128/chunk8/30Ksteps20h独立suite各500trials；pretrain3M数据约2.3Mspatial、多种web+robot，sim244K、real1K/6h/23object5container等人口分开。Hardware预训/precision/LR/seeds/CI/fulltraincost/推理latency ND。Table1同Qwen与C8双backbone的有限对照支持接口，不证明所有backbone无capacityconfound；groundingpretrain增数据/steps未给全预算反事实。B1延长100K曲线不授无限训练ceiling，C9 0.5M均值低于0M，不采用新scale law或criticalmass定理。

C2ground/action1:1或1:5 grounding更好但action退步；1:10非每指标最优（1:15 Widow71.8>71.7），co-training不是所有任务必兼容。C5default77.9高于随机padding58.5支持promptsemantics有限区别，但Box Widow75.8>default73.2，fixedprompt非普遍optimal；也没有对每种gradientfactor独立必要消融，不把整组合收益归于.5。LIBEROspatial98<vanilla98.8/π0KI98且goal低于π0，不授每taskbest。Real300rollouts各≥50slice且slice可重叠/每trial至3attempt，不是300×8独立task；sensor/container错误与incorrectgrasp仍存在，depth/proprio改善是future。多步骤plan实际学自22hsegmented轨迹不授无监督规划/安全control。只采用空间读接口/回传梯度与co-training比例分账及PSS非方向可靠性，不授formal安全或空间先验必须；Books待比较。

普通必要core全部32已准备（加首批13为working45），不等全部独立source/Books/日期。09080日期单保留、09629准入事实含糊未关闭；来源发现停点未冻结。六Books实际写后仍待rootPOST，作者不自标整日完成。

最新POST停点覆盖上述早期待验：root实际读六项两段、完整邻接与末注，09316/09369/09434/09528/09173/09483非作者POST通过；六末注已同步，六锁已释放。累计17项实际BooksPOST有效，非日级Gate。当前无共享锁；本日45 working necessarycore已准备，source独立未核尾部、日期/owner/来源/成稿继续，未freeze。

## 官方发布入口贡献关闭（日期不另强求）

[Seedance2.0 launch](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0/) 原文L23–124已读：支持text/image/audio/video references、editing、joint AV架构名称与能力demo，但未披露新增factorization、训练目标、采样或受控物理一致性机制。有限专家评测与宣传“真实物理”不是模型可控/正确性新边界，故本项目贡献关闭；保留detail/multi-subject/audio distortion限制，不因四模态/新榜收录。官方日期仅2026-02-12，未核时区/时刻；既贡献明确关闭，不为不影响处置的日期另建请求。后来2026-04技术报告不倒灌本launch。

[GLM5 launch](https://z.ai/blog/glm-5) 官方可读搜索全文core已核：355B→744B/32B→40B、23T→28.5T、复用DSA，以及Slime“异步RL基础设施”标签和成绩。未说明本launch相对已公开方法的具体异步机制、陈旧更新条件或新兼容边界，规模/组合/排名本身不足；贡献关闭而非授通用大模型无贡献。当前精确open返回0行不以此记零命中，已实际读同官方indexed core；后发2602.15763技术报告不继承为本launch原增量。2026-02-12 date-only未核公开时刻，关闭不另追日期。

[Google throughput scheduling Blog](https://research.google/blog/scheduling-in-a-changing-world-maximizing-throughput-with-time-varying-capacity/) 核心已读：未来capacity已知，online未知的是job arrivals；restarts损失已有进展，不是checkpoint/resume。原SPAA2025论文的unit-weight1/2与一般capacity1/11理论重释，Blog未提出新的大模型执行/训练/推理机制或适用边界，既非本窗论文首公开也非重要机制修订，关闭；不能因“cloud scheduling”联到主线便计新增。保留其理论条件，不泛化真实未知capacity生产SLO或原算法无学术价值。

## [Four-Checkpoint Framework 2602.09629v1](https://arxiv.org/html/2602.09629v1)：定点准入关闭

实际读完整题摘、§9.3–9.4/Table6–8、§10.2与§11.2必要限制，root独立实际核§9.3–9.4及10.2首表后关闭通过。新增四级severity taxonomy的binary ASR只取level3指示，WASR则平均level/3；两者不同estimand，“52.7%对22.6%”不能授真实旧binary evaluator在同一response漏判的2.3x安全反证。Classifier仅见harm category而非original request，Sonnet同时作target/judge，150条跨judge一致76.6%、100条人工一致91%仍有限。Table7归纳既有refusal-then-explain等泄漏类型；partial actionable leak的重要性不被否认，但本稿未给改变现有设计的受控新盲区。CP3/4叠加输入framing，blackbox指标不能定位真实内部output-stage防线因果。保留安全反证和真实原文，不采用其taxonomy/线性重权为新可靠性条件；日期不再为不影响关闭而追加。此项一直不含在working45中，不因关闭人为减候选数。


## 2026-10-04T11:58+08:00 当前停点（覆盖早期待授叙述）

19项实际BooksPOST已通过：09719 Ch30正文659/662与末注869，09639 Ch24正文212/214与204–222完整邻接及末注1874均获root实际POST，已同步、锁释放。没有共享写锁；不是整日Gate。另17必要源独立定位见[V3_REMAINING_PRIMARY_ANCHORS.md](./V3_REMAINING_PRIMARY_ANCHORS.md)，没有重复首批已通过的身份/必要证据。

来源有限补检已停止，实际范围见[V3_SOURCE_SCOPE.md](./V3_SOURCE_SCOPE.md)；新20完整题摘见[V3_BOUND_TITLE_FULL_AB.md](./V3_BOUND_TITLE_FULL_AB.md)，root实际读原文校准13窄增量继续、7关闭。关闭10024/09801/09270/09621/09413/09805/09552，理由分别track汇总/暂缓科学域/社会统计/backend组合/datafree层缩放未新增可靠性/成熟分账与局部ranking/未给instruction-history-turn受控新边界；不是因局部、小模型或域内实验一律拒。新13为09448/09616/09229/09764/09170/09276/09331/09394/09842/09891/09983/10058/09533，未评分或授落窗。总working58未冻结，原45 necessarycore已准备，新13普通必要审阅继续。

09394已实际定点读§2.3/3.1–3.3/7.1–7.3/E.1–E.3，root已独立核必要原源：采用endpoint-only testing的条件理论，仅报告（2+1+3=6）；真实contractive Markov抽象模型而非仅操作类比，但Def2.4全文trajectory可观测与Def3.8/T3.9只观测R的测试下界未桥接。温度mixing/permutation另需假设，语义多对一不自动证明严格收缩。GSM只width/objective-mismatch例证，contraction/inspection仅synthetic。普遍全轨迹训练归因/critic原因/无限样本不可能主张明确隔离，不进入Books，重开须同一可观测域的下界或LLM真实抽象/收缩证据，不继续所有inspectionproof。


## [ADPO 2602.09533v1](https://arxiv.org/html/2602.09533v1)

2+1+3=6，标准必要§4–6/Eq7–31、Table2–5、A/B/C定义与证明、E配置/Table10–11实际读。新机制是prefix-wise BT假设下将segment logratio-margin的logsigmoid求和，token length μ与feedback length μ′分开；static EOSpadding与adaptive固定m等分改变比较单位。seq pair偏好继承给各prefix并非逐step真实正确性监督；异长度ordinalsegment也不是同语义对齐。m=1恢复DPO，但m256不是唯一正确细度，Table3小m的Llama/GemmaGSM与QwenMATH可反退，m512亦可低于256；不是所有更细更好。

理论不采用“任意原reward相同KL最优”：C允许f(x,y< i)的prefixshift，它在不同winner/loser前缀不自动抵消；A Eq33–36其实先定义canonical r°后得到loss，不能把它与原r*同偏好等同。B Eq62–65只证明sum energy全局Boltzmann等于全序列energy，未证明Eq11–12的逐条件归一乘积等于该全局Boltzmann（通常还缺未来partition/value），不授Cor2或Theorem1的sequence reward invariance。只采用明确新局部目标与反馈权限，不照录普适理论。

四H100，TRL/LoRA16/AdamW，math3epoch GSM8K训练/8shot GSM与4shotMATH500；DPO/ADPOlr2e-5，c系4e-5；contrast估64samples/topP.5，conversation PairRM1epoch。precision/batch/maxlength、真实seeds/training cost/latency ND，Table10 std无具体独立run数，不补种子。GemmaMATH生成895→2192token并非“略长”或免费质量，selectgranularity/beta不同search人口不授全compute同预算； Table3细度反侧与Table4有限judge评价独立保留。必要支持HTML L145–174/228–263，直接反侧 L271–283/499–538/610–639；root必要命题已实际独立核通过，owner TRAIN-DPO具体Books差额待比较。


## [Complexity–Diversity 2602.09448v1](https://arxiv.org/html/2602.09448v1)

2+1+2=5，标准必要§3–6/Table5–8、C配置与F13误差人口实际读。同8K MS MARCO docs、相同Q/doc下Paraphrase vsDiverse更改query格式/内容，Novel受益而2Wiki反退，是可采用的生成retriever训练数据多样性≠普遍质量边界；温度0与few-shot .7的主表不同生成配置，不把全baseline收益单独归因diversity。两retriever FP16/InfoNCE batch128、AdamW至100epoch、每500step按MSMARCO dev选checkpoint；LR先humanlabels搜索再统一，不等所有synthetic方法独立最优或同总训练/生成成本，hardware/seed/CI/fullcost ND。

Table7每condition Pearson n=4个dataset，14condition/56点共享四个CW值，不是56独立任务；12/14显著而非全14。CW是unique non-stopwords length>1词数，反映lexicalproxy不是controlled intrinsic reasoning complexity。Table5 Novel gains与2Wiki hurts允许窄取舍；不采用CW7/10通用阈值、复杂度唯一根因或真正语义labelnoise已证。F13的455/522(87.2%)只取Q3胜Q1败子集，Q1胜Q3仍187/4345；净335局部错书段变化，不证明全数据表层overfit唯一成因。训练query多不等coverage，文档数/总pair量及earlystop分别计费。root必要source已实际核通过；Books AGENT-RAG具体已有coverage/局部证据比较待执行；support L123–153/239–291，直接反側L293–357/432–453/510–522，不遍历后续全榜。

## [Argus 2602.09616v1](https://arxiv.org/html/2602.09616v1)

2+2+2=6，标准必要§3.1–3.2/4/5/6/7/8、D.2–D.3已实际读。RPS是Wikipedia首段实体、Wikidata一跳相关query、排除query直接邻居的800竞争池、固定topk的hit经验均值，不是实际corpus/query人口的校准失败概率。各retriever单独拟合embedding→RPS，NER同surface重复mention取最低predscore，τ.3标记后BM25检索两条首段KB。Expansion每entity×KB多view，synthesis汇总为单额外view；保留原文并不保证新view无语义变化/外证真值，也不保证index全部误风险消除。

八retriever，BRIGHT10/ImpliRet2/RAR7任务，nDCG5/10；同target模型诊断/索引/排序，synthesis Qwen3-30B-Instruct2507，hardware/precision/seeds/CI/全offline与online成本ND。Table2 Jina ImpliRet synthesis17.9→16.4反退、Expansion20.8；两增强形式并非互换免费。未给等index膨胀的随机/全entity增强控制，不授“低RPS选择唯一收益原因”；关联E.1也非因果。固定KB与threshold依域限制保留，有限RPS支持索引前诊断/增强接口而非安全概率。support L143–160/182–214/482–531，counter L225–277。owner AGENT-RAG具体差额待比较/独立source待核。

## [Embedding Magnitude 2602.09229v1](https://arxiv.org/html/2602.09229v1)

2+1+3=6，标准必要§2.4/3/4.1–4.2/5/6、B配置、F1–2与K/N/O定点已实际读。2×2独立保留query/doc norm；固定非零query的正norm只改变score scale不改变该次排名，doc norm才可能改变排名，但在InfoNCE训练中query norm改变temperature/梯度。新证据是同训练population的分权消融与scratch/FT异向；成熟dot-vs-cos algebra不单独计分。Learn γ虽可插值，sigmoid有限参数不精确取0/1，不能授安全默认或可训练校准保证。

三BERT检索器/MSMARCO81795，主三seed0/42/1337；B两GPU每卡128/effective256，正文batch128保留层级；LR只cos sweep后统一，best dev checkpoint不等同总训练预算，型号/precision/全latencyND。T1 Contriever DL20 Dot56.32<Cos57.25，聚合优不等每bench；T2 scratch Dot/QNorm广退。T5 RetroSTS Dot.750>.749，与“norm必益对称任务”普遍原则不符；partial asymmetry违背对称要求但Dot仍对称，故对称本身不推出幅度无用。T6单向CLIP损失更改训练目标且双向退步，Cohen-d相关/去pony后相关不授唯一因果，O最佳DNorm的叙述与主QNorm偏好保留不合并。只采训练/推理norm作用分账及条件反侧，不采普适task-symmetry规律/无成本能力。support L228–267/304–333；counter L275–281/340–417/474–523/1023–1027/1054–1083；owner AGENT-RAG待比较与独立核。

## [BITS 2602.09764v1](https://arxiv.org/html/2602.09764v1)

2+1+3=6，标准必要§3/4/5.1–5.3与A reset/bit数/soft-target反侧已实际读。Teacher EMA hard-threshold target→student逐bit BCE，L2-normalized prebinary logits covariance logdet regularizer，optional每10epoch同时投影head重置；binary是训练agreement channel，最终backbone仍连续，不是交付256bit语义完全表示。Eq4互信息是解释目标，连续logdet不是离散H(Z)精确估计，学生看到X2不只Z2，不能授已证明优化原MI或独立真实semantic factors。

ViTB16 scratch ImageNet1K100epoch、batch256、256headbits、共同SimDINO框架/aug；hardware/precision/seeds/CI/运行budget与latencyND。Table3同discrete head BCE43.44vsCos36.34支持逐bit目标边界，而非离散化本身即可。A Table9 reset1低于10、Table11 512bits39.32低于25643.05；softτ.1接近hard，不能授硬化必优/bit越多越好。covariance effective rank不等真实factor因果，未测DINOv2/3 patchobjective兼容，不外推所有foundation encoder。support L125–169/170–205；counter L210–218/340–360；owner WORLDVIEW-REPRESENTATION/MULTIMODAL-REPRESENTATION待具体比较与独立核。

## 最新实际停点：22 POST，日期轻检完整，普通必要尾部2

root实际POST通过09533 Ch34 L158/160/513、09517 Ch76 L432/434/1469、09825 Ch23 L1002/1004/1175，末注已同步，三锁释放；共22实际整合POST（原45占21，新13 ADPO占1），不是日级Gate。BagelVLA已有覆盖Ch26 L312–319 latent future-KV，Code2World已有覆盖Ch25 L991/1000 provisional executable-delta，09448已有覆盖Ch27 L242–251 quality/集合diversity/proxy反退，root实际核具体正文通过，局部新反侧保留本报告。原45必要source现17/17独立通过，见ROOT_REMAINING_REVIEW.md，09934仅修配置，不重审附件。原45共27 owner已处置（21整合+6报告/覆盖），余18具体owner比较；新13 ADPO整合、09448覆盖、09394仅报告三项已处置，余10 owner。working58未freeze，不把这些过程计数当完整日期/日Gate。

新13精确abs v1均200、history/最终DOI身份相符、现成信号轻查与各自BJT包络保存V3_DATE_BOUND_FIELDS.md；全部包络下界02-11 09:00，上界登记+1sec落当日10:57:45～11:19:10，独立日期Gate待验。新13前6必要source已root过；09331/09276/09170亦已独立核限缩命题，以下作者标准必要审阅完成，09891/10058已准备交root；剩普通必要2项09842/09983正在定点核心，不扩发现。

## [FLARE 2602.09170v1](https://arxiv.org/html/2602.09170v1)

2+1+3=6，实际§3/Alg1、§4.1–4.2、§5/6、A单步、D/E/G必要反侧。只采用固定非参数随机性时，Laplace参数协方差的单步JΣJᵀ pushforward及随机跨层子网/JVP近似sensor，不授全路径calibrated epistemic。Alg1一次sample子网与描述每步sample不混；G1 cross=GΣJᵀ和leading variance同阶，posterior concentration不自动相对消失，main17/G29符号/矩阵与state依赖未闭合，不照录完整递推。

FiLM residual MLP合成grid/sine/chirp/damped；sine prose8330 vsTable4218参数、chirp72496/sub4412、600steps/b512或256，hardware/precision/fullcost/seed ND。Gap-closure式方向与正收益叙述冲突、Damped85/76.2不统一。G2 20trajectory/S128与Table3 N80不同population，Table4 p=.9993/1.0与one-sided小pprose相反；只保留小模型局部cross数值影响，不采用精确p/任意scale negligible。完整variance/真实epistemic归因中心隔离，重开须一致递推含state Jacobian/sharedθ cross与相对误差条件及可核同人口统计，不深追全proof。root必要source范围通过；Books普通比较待执行。支持§3 L160–259/E591–594，反侧G617–724/§5，非所有附件认证。

## [Effective Reasoning Chains 2602.09276v1](https://arxiv.org/html/2602.09276v1)

2+1+2=5，实际§2.1–3/4 Tables1–3、A1/B必要配置。LoRA rank/module sweep至共同accuracy阈值是操作性capacity proxy，不是全参数真实minimum维数；14strategy ID–accuracy相关.75/.93不授压缩因果、UAT或跨任务定律。1B/4B阈值24.3/63不同，不能用不同model的LoRA参数值推规模更压缩；filler可降低proxy而略增分，2/4/8 distractor proxy非单调，参数位置/优化预算也参与proxy。

Gemma1B8000steps/4B6000、LR搜索1e-2～1e-6/b8，硬件/precision/seeds/完整sweep成本ND。教师生成并正确过滤6.2–7.5K不同population；14样式的size相关不显著不能证明无混杂，Gemini teacher与Gemma27B亦不统一。扫多LoRA结构不是免费selection。支持§2/3 L85–161，直接反侧§4.2–4.4/Table3 L200–251/A1/B366–369；root必要source通过，仅采用受限测量诊断，Books具体比较待执行。

## [Counterfactual credit 2602.09331v1](https://arxiv.org/html/2602.09331v1)

2+2+2=6，实际§3/4 Tables1–3/7、§5与A开销。每条最多10 regex算术/句子span替换placeholder后测原生成answer的teacher-forced概率drop，minmax映至[.5,4]乘group advantage；未覆盖token权1/answer1.5。Placeholder可能OOD，answer dependency不证明正确性、真实causal step或oracle删除；负adv同样被重权，不能只解释为奖励正确span。

Qwen/Llama≤3B LoRA32/α32、GSM7473train/1319test、500step/b16/acc4/G8/lr2.5e-5/temp.6/p.95、三seed。只有Qwen2.5最终p.002，另两.112/.125，随机权Qwen85.8略高vanilla85.6，不能由方向反转授真实因果。MBPP250 CF51.3<54.2，算术regex域限制与answer-sink解释分别为配置/作者假设。A单L40S405→535/403→578/412→715min（32–74%），额外forward费用真实；缓存命中<1%，其他优化多futurework，precision/完整预算控制ND。root必要source通过；support§3 L158–229/counter§4.4/5 L358–388/A435–456，Books具体比较待执行。

## [Stemphonic 2602.09891v1](https://arxiv.org/html/2602.09891v1)

2+2+2=6，必要§2/3、4.1–4.4、5/6与Tables1–3已实际读。每stem独立batch item，同mix随机subset成group，同group训练/推理共用初始高维noise，不加cross-stem attention；可变集合并行与原逐stem顺序路径的替代接口。训练仅半group用left-out submix做condition，noise共享不是整batch iid，也不是推理时简单相同seed即可匹配joint训练。活动控制是-60dB二值16dim condition而非真实harmonic一致性证明。

1B DiT/T5XXL/VAE64dim12Hz/44.1kHz、32s394frame、effective16Kseconds/bperGPU1024sec、AdamW1e-4、30Ksteps8A10080GB三日；先20Khourmix再400hourmix/~6stems、单A100推理Euler32/CFG3仅steps3–28。precision/seed/uncertainty/fullpretraincostND，评估Moises1488/Mus964mix由LLM+手核tag，FAD/CLAP非独立真synchronization。Table1 Musmix C1.05差于B .91；训练活动控制反退，Table2 onepass质量可差于Kpass，twopass质量/时延tradeoff；具体秒数不外推任意K/hardware。作者解释K/2人口bias未因果鉴定。support§3 L81–106/4 L109–139，counterTables1–3/§5 L140–176；仅采用共享noise/group interface，无跨领域语义coupling普遍证明。source/Books独立待核。

## [Disentangled Music Representation 2602.10058v1](https://arxiv.org/html/2602.10058v1)

2+1+3=6，必要§2.1–2.4、3/4/5 Tables1–5实际读。单embedding vsconcat新probe性能差绝对值Δ是互补可读信息诊断，不是直接估计mutual information或无confound因果；global/timed两个分支名称不认证timbre/structure真正解耦。Table5 SS-VQ structure任务 .311/.318与tempo.478差，AFTER双策略仍tempo.382；去augmentation/adv各有反向切片，表示解耦也不自动移交decoder可控性。

三官方模型default配置retrain同Slakh145h/非鼓stem90/10，embedding1024 vs16 vs6/12明显不同，不授等capacity或default全最优。SynTheory受控音高/时间/乐器，MPE36hMAESTRO→MusicNet、SLP earlystop/MLP512，阈值validation选并trackmean；hardware/precision/seeds/CI/完整训练与decoder成本ND。小Δ也可能两probe都弱，绝对差含退步，因此不当独立性证书；作者decoder/controller/perceptual输出评测仍future。只采用cross-branch leakage的测量反侧，不采用音乐应用结果或representation→control必然桥接。support§2 L74–109/3 L123–134，counterTable5/§4/5 L135–162；source/Books独立待核。

## [Step-Size Stability 2602.09842v1](https://arxiv.org/html/2602.09842v1)

2+1+3=6，标准必要§3 Theorems3–4/A1–2、§4 Lemmas5–7与NGN额外lower-model条件、§5.1–5.2/limits已实际读。新stability index δ=f_current−prox-surrogate_min把名义α与effective step分开：同state/sample下SPS/NGN/SPP δ≤SGD，SPS受interpolationσ²+lower-bound underestimate分账，凸lower-model条件才桥接suboptimality；nonnegative不自动使NGN square-root model全域lower bound。不是“更大LR总更好”或Adam/momentum保证。

ResNet20/CIFAR10 20epoch/α.01–100，warmup100steps；三seed同初始化不同dataordering，D≈50来自实际位移不是已知distance-to-optimum。Linear regression n50/d10/b5，target噪声与b25改变σ²，C=-2可失SPS优势；同steps通过epoch调整，不把batch增大当所有optimizer更稳定。HW/precision/完整grid成本ND；proxy曲线支持非凸局部观察，不能移交凸定理/通用LLM优化recipe。SPP subproblem额外solve成本与限定结构保留。support§3 L138–203/4L228–294，counter§4.3 L270–275/§5 L324–377/limitsL86–88；不为标准审阅遍历全appendix proof，source/Books独立待核。

## [Coupled Diffusion Inference 2602.09983v1](https://arxiv.org/html/2602.09983v1)

2+1+3=6，必要§3/Eq9–24、§4/T1、§5与C实现条件已实际读。已知codebook Gaussian-mixture解析score，以Tweedie denoised factor的乘法reconstruction energy联合guide多个diffusion chain，再restart/renoise；实际是未知factor条件推断，不是多个现实感知模型学到语义解耦。DPS conditional-score只是近似，similarity energy exp不可归一仍可作gradient，不能称真实posterior精确采样/新probability guarantee。

随机bipolar D1000、200trials、100iteration、correct-factor c/K不是全部factor精确成功；Optuna各variant单独在D1000/K3/n50 validation选9参数，guidance clip、温度、ρ/R/T另有预算/尺度。HW/precision/seed/CI/E2E cost与Optuna全部budgetND；同iteration非全算力相同，ALS pseudoinverse费用不同。Gaussian在T1强噪大幅落后，ODE/SDE优势依energy，更多T无单调趋势，restart独立成功公式1−p^R与p被称correctprob及沿前次state相关不闭合。C线性β范围.1–20与离散1−β平方根时钟未明确DT换算，不照抄可执行recipe。仅采用known-factor priors通过denoised-product约束耦合的条件接口，不授真实视觉semantic decomposition/理论capacity或免费跨模态保证。support§3 L152–223/counter§4 L224–277/C383–446；source/Books独立待核。

最新停点：working58未冻结；限定必要原源58/58均经非作者独立核，作者普通必要证据未读0，日期轻检均准备而DateGate未授。实际Books POST累计26，最新09616/09229 Ch76、09842 Ch28、10097 Ch27正文/邻接/末注通过并同步，锁释放；不重复前22有效POST。原45 owner余10（09375/09651/09878/09883/09902/09924/10004/10044/10099/10104），新13余4（09764/09331/09891/09983），合计14普通owner待办。09574/10098/10021已有覆盖，09789/10109/09934/09555/10058/09276仅报告，均已root核具体处置。09170最终Books处置为暂缓/中心审阅争议：单步JΣJᵀ sensor的限定源已核，不认证sharedθ全路径递推/真实epistemic；不进入Books，重开要求一致state-Jacobian/sharedθ-cross递推及同人口相对误差证据。本窗可隔离终态，不冒充完整Evidence保证。当前Ch25仅10044、Ch24仅09891/10099已获窄锁，正在落实；无新发现查询。

## 最终逐ID停点：58冻结，38 POST，普通0

最终评分校准：root发现共同误理由，仅纠正09789/09924/09934/10058/09983/09394的Durability 3→2，均为2+1+2=5。它们原增量分别是固定consumer压缩反侧、policy-specific线性probe、同骨干paired consumer反侧、probe leakage测量、已知解析codebook的DPS条件接口和endpoint-only条件测试；这些有限新证据可复用，但不足成为长期通用认知基础。不是因Only处置降分；准入58、原证/反侧、已完成标准审阅和Books终态均保留。下方/上方旧6分为过程记录，以本段与当前README最终表为准；09842等具体理论机制不一刀切改分。

root实际核全部日期字段与官方排程，58唯一家族冻结（45原准入+13新增），38整合/7已有覆盖/12仅报告/1暂缓，全部owner处置已核；38整合正文/完整邻接/末注实际POST通过，全部窄锁释放。普通必要原源/owner/修改/POST待办均0；剩六部分成稿、机器检查与整日独立Gate，作者不能自标完成。来源补检已停止，不扩新材料。

计数纠正原证：作者曾以58个paper heading去除09629得57，漏掉inline记录的09394；root逐ID确认58 heading=45原准入+12新增heading+关闭09629，另有新增inline09394。因此最终58=38+7+12+1；09394保留限定endpoint-only仅报告，09629保留关闭原证但不入候选。旧45→44/58→57算术推论无效，不用排版结构改变准入或日期。

最后9 POST均已同步：09764 Ch5、09375 Ch79、09331 Ch33、09883 Ch49；09878 Ch26、10104 Ch25、09651 Ch24、10004/09902 Ch56。09170最终暂缓中心sharedθ全路径递推争议，不混Only；必要单步sensor源已核但不进入Books、不授完整Evidence保证。09394限定终点可观测测试下界只报告，全轨迹归因claim隔离；中心重开条件保留各项证据。

MiniMax精确链接恢复：M2.5 launch https://www.minimax.io/news/minimax-m25 的关闭仅指其launch原核心；[中文Forge](https://minimax.cn/blog/forge-scalable-agent-rl)根实际读L64–66为2026-02-12 date-only且§3.1有WindowedFIFO具体机制，不能与launch标签贡献关闭合并。中文news标Feb13、英文blog标Feb14；整天不完全落窗，缺最早正文公开时刻/完整包络，作为单独日期终态保留，不采用、不入Books、不计58，取得只重开本family。本稿可读，不称正文不可访问或普通未读已审通过，也不倒灌后发详细技术报告。
