# 后续五项必要证据与具体owner比较

五项必要证据/实际owner已root非作者核：21480 Ch70具体Existing；21652 centralDisputed安全隔离（Table1/2有限经验仍报告、不采用中心等价/fastrefresh、不Books、不以Only抹去争议）；21492 Ch27正文166/邻接158–175/own1546、21496 Ch72正文52/邻接45–60/own4266、21655 Ch33正文598/邻接590–607/own2907均PRE/实际POST通过、窄锁释放。下列保留实际源/控制/写前差额与作者待裁建议，以上终态为准；均未核代码/复现，非日级Gate。Blocks编号不是文件行，V3_BLOCKS_<ID>.md保留实际原源。

## 21480 Both Ends Count! Just How Good are LLM Agents at Text-to-“Big SQL”? — 2+2+2=6

[v1](https://arxiv.org/html/2602.21480v1) blocks22–86/117–124：query-only VES不计生成、tool/schema/check或engine运行失败成本；VES*/VCES引入end-to-end时间/费用及正确性权重，CVQ=C/p还要求重复尝试成功率/成本稳定，不是实际Agent retry保障。Extra columns人工projection协议不是所有SQL语义等价；Eq34集合记法与文字相反，不采用该字面oracle。

BIRD仅8题，选所有原模型EX≥.85，后续GPT5.2例外；TPC-H四题1/17/18/21按Claude4.5失败挑选，不是总体排名。Jan2026三模型API，BIRD AWS m5.xlarge/us-east1；TPC-H EMR r5b.xlarge master/core、32 cores、gp3 128GB。AppendixE SF1指标50次，跨SF10/100/1000另执行已生成SQL，不能将50次自动转给各scale。Run_query后停止，无无限repair；scale使语义正确却昂贵/不成执行的计划暴露出来，不证明模型质量普遍次序。No memorization check failure不证明未记忆。API precision等Not Disclosed，SQL/工具成本之外排队SLO未测。

拟具体已有覆盖PLATFORM-COST Ch70实际86–121/162–181：完整trajectory计context/device/tool/network/idle/coordination，cost_per_good_request按quality/SLO结果、失败与无进展不算有效利用率，已承载“SQL正确不能替总workflow成本、有效完成分母与失败成本”的主命题。该有限SQL验证不新增通用成本原语，拟Existing而非为BigSQL名加段；CVQ独立重试假设仅报告。

## 21492 GradAlign: Gradient-Aligned Data Selection for LLM Reinforcement Learning — 2+2+2=6，选择接口具体gap深入

[v1](https://arxiv.org/html/2602.21492v1) blocks38–83/84–140：在可信heldout validation上重新on-policy rollout得到平均GRPO gradient，对训练候选梯度作cosine排名，按top25%或5%选样；每10update重算避免旧policy support/importance variance。原问题不是仅挑适中passrate：50%候选reward替Bernoulli(.5)仍看似适中，alignment在作者步骤0/50/100选中噪声17.8/37.1/29.9% vs accuracy-greedy81.8/85.3/87.1%；mixed-domain Countdown目标只在目标验证/测试，不是所有领域质量提高。

Theorem4.1 binaryreward、on-policy、未normalize且忽略clip/KL的score-function期望可支持局部方向；Theorem4.2实际group随机均值/std与梯度有关，不能从逐组乘正随机因子推出期望vector保持方向/accuracy unbiased。隔离这个认证命题，不自动隔离Table1/2有限经验。Qwen3-8BBase（MMLU另1.5BMath）、judgeQwen2.5-72BInstruct；matched learningsteps不等matchedcompute。总体固定100步test average45.7对44.4/44.6/45.3，单任务反退，未见统计重复保证。AMC22 val/AMC23+AIME test分账支持不直接训练val；Table6best checkpoint按test挑不能当heldout选择，采用fixedstep数据。Gradient两seed Pearson随kv32/.30、128/.49、512/.79只显示估计噪声，非排名稳定证书。额外validation/candidate rollout、backward与梯度memory未披露端到端墙钟费用/hardware/precision，不照录modest成本。

TRAIN-DATA Ch27实际148–165已有embedding/loss/gradient/validation信号与boundedmixture、heldout、delay/leakage/cursor；但无“heldout target gradient与候选更新方向匹配，噪声中间passrate不能代表有用”的具体选择分支。拟在data-control-plane后单窄段：target/validation/policy/samplingbudget身份，cosine只是当前局部proxy，错误/分布偏validation也会误选，新增完整scoring成本与static/accuracy基线回退；不搬Theorem4.2/无偏accuracy保证。请求root实际owner/PRE决定。

## 21496 Beyond Refusal: Probing Limits of Agentic Self-Correction for Semantic Sensitive Information — 2+2+2=6

[v1](https://arxiv.org/html/2602.21496v1) blocks29–45/52–78/105–113：Evaluator读原query+draft，Editor只读draft+critique，最多3轮/检测clean停止。成熟selfrefine loop不计增量；采用同Qwen3-8B thinkingon/off的有限风险方向改变与迭代非单调反侧：raw SemSI84% vs74%，加loop42% vs47%；utility同表4.61vs4.03，但Table1 Qwen4.54不同，避免精准合并。Llama70B步骤2occur16.5%后步骤3升19%，更长loop不是安全单调。GPT5 vsGemma的rewrite/truncate差异不隔离架构、training、capacity，不能授普遍scale threshold/emergent law；10qualifiedresponse/model的人注不提供总体推断。

NoProtection→loop均值降低主要混入initprompt效应，prompt-only控制55%→51%才是迭代额外均值，个别无改善/反退。GPT5 LLMjudge的人注400responses同GPT5人口，agreement不是所有模型敏感信息真值或开放域calibration；88qualified GPT5样本0%false也非全输出0/epistemic calibration。AppendixC105删词例子还可能删掉解释misinformation的有用context。返回budget-exhausted draft不能认证clean，modelversion/precision/hardware/totalcalls/token/latency未完整披露，角色可以同模型且共享盲区，guardclassifier target不同不能由低F1授所有guard无效。

PLATFORM-SECURITY Ch72实际47–51最小披露/抽象泄漏，251–258已有rewrite/privacy-utility、生成改事实/新线索与非DP；633–635已有pipeline次序/同人口效用与外部enforcement，尚无“同model thinking风险方向依赖是否有编辑约束+更多轮风险可反升”的具体反侧。拟47–51附近单窄段：reasoning不是单调privacy提升，检测/编辑/预算停止非truthauthority，分别验raw/同prompt/loop与utility/context preservation，费用与deterministicrelease/不发布fallback；不推荐安全医疗内容、不授规模定律/零false/通用guard失效。请求PRE或Existing裁决。

## 21652 Sparsity Induction for Accurate Post-Training Pruning of Large Language Models — 2+1+2=5

[v1](https://arxiv.org/html/2602.21652v1) blocks6/27–53/56–66。拟claim等价channel scale+shift预适配稀疏/absorb+fastcachedHessian；核心接口尚不一致：Eq3应W*S与S^-1(X−δ)配套，而Eq10/11按DX缓存score并非此前同scale；固定mask/δ0时纯等价scale的Wanda |W*S|*norm(X/S)消掉scale，不能据此认证Wanda importance改变。Eq5从输出channel初始化而Eq3输入channel需清楚映射，Eq8 exp(−αsum norm)最小化鼓励norm增大，不证明低rank/feature sparsity。这里只核拟采用核心，不遍历其他公式。

Table1/2真实OPT/LLaMA finite经验不能由上述问题自动认伪：128C4×2048tokens calibration、RTXA6000/1–5epochs，attention/MLPlinear剪枝、embedding/head保持dense；不少SI平均accuracy或PPL反退（50%SparseGPT LLaMA1/2 7B等），不采用consistent胜出。Table3的15.27vs345.91s是128samples/batch1 Wanda refresh，Table4 2:4 Wanda与SI均251ms/dense312ms，SI不是额外runtime加速；precision/输入输出形状/concurrency/SLO不全。函数等价折叠跨非线性/shift路径也无完整实现材料，不能认证全architecture无overhead。

INFER-TENSORRT-LLM Ch49实际493–513已pattern/冻结artifact/kernel admission、目标混合/曲率近似、scale自由度、quality反退及离线恢复成本。现有可支持的经验只是既有范式有限验证，不制造Books差额。拟OnlyReport保Table1/2有限结果，同时明确equivalence/fastrefresh关键命题争议；若root认为等价适配是中心且未留独立新增经验，则centralDisputed终态无Books。重开需要同参数坐标完整实现/目标及对应matchedbenchmark，不全附件。

## 21655 CCCaption: Dual-Reward Reinforcement Learning for Complete and Correct Image Captioning — 2+2+2=6，reward支持域具体gap深入

[v1](https://arxiv.org/html/2602.21655v1) blocks26–57/78–101：imagefacts分母与captionfacts分母分开，前者用多MLLM生成的视觉问题、只给caption答题作为completenessproxy，后者从caption拆subquery再给image打grounding分作为correctnessproxy。两个方向的有限对照有真实取舍；querycosines方差/tsne覆盖不证明全部imagefacts、query库错/漏真值与同模型judge会共同错。Eq51初始化1−mean＋每epoch variance再normalize没有完整参数规则，不采用确定实现配方/采样无偏或所有hard题低概率。

Qwen3VL2B训练与correctnessjudge同名、completenessQwen2.5VL3B、H100、20epochs/GRPO5rollouts/5queries+max5subqueries/α.05，baseline/token/precision完整总budget与统计重复NotDisclosed。Table5 samebase无Corr OCRHall81.93低于base82.32、无Comp OCRPrism40.45低于50.16；双reward83.09/55.34支持有限tradeoff。ChartQA correctness-only68.11优于combined66.72，双reward非各metric最优；withoutDynamic OCRHall83.92也高于83.09。训练步曲线不是端到端节时，CapRL3B不同base与2B不能独立归因correctness。CapArena/Prism/Hall均MLLMproxy，不授caption完整/真值。

TRAIN-GRPO Ch33实际585–606已有verifier spec/多rewardscale/独立heldout；Ch23actual586–595已有captionproposal不可图像替身，但没有明确image→caption coverage与caption→image grounding两个不同采样人口/denominator的reward接口。拟Ch33 verifiable/learned reward边界单窄段：imagequery coverage和captionatomicgrounding责任分开、原图/query/judge/source身份与额外calls、sampling改变目标、judge共盲区及独立image/quality Gate；Table5非双reward所有维度优胜，固定queries/单目标配matchedcalibration回退。不照抄query公式实现/完整coverage或training speed。请求root PRE/Existing判断。
