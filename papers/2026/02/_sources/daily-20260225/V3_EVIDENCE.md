# 02/25 当前必要证据笔记

本文件为本日作者实际必要源审阅与owner比较的工作入口；正文/候选处置完成后由README引用。不是独立验收收据。所有实验均作者报告，未核实现、未复现；正文下载本身不算审阅完成。

### 当前非作者结论（34/34 项；替代各段保留的 PRE 时点待核描述）

root 已实际必要原源与 owner 核34/34：18581/18649/18674/18679/18690/18694/18721/18739/18749 九项仅报告；18583/18600/18613/18700/18733/18746 六项具体已有覆盖；18628/18633/18639/18658/18671/18711/18724 七项中心争议终态、不正面 Books。18639 A.8 的吸收步骤需要未给出的 ε≤d，不能说作者已经提供此假设；d=0 不能吸收正 ε。因此隔离原 theorem，保留 reward-free transition、PCA-tail floor/local MPC 的条件经验，不以“仅报告”掩盖中心 bound 冲突。

18568 Ch54、18571/18702 Ch78、18584 Ch27、18582 Ch31、18645 Ch33、18647/18695 Ch24、18710 Ch66、18734 Ch76、18742 Ch26、18745 Ch23 十二项作者窄写已完成；root 实际正文、完整邻接与自身末注 POST 均通过，窄锁全部释放。最终三项实际位置为 Ch76 431–451/自身末注1549、Ch26 583–614/自身末注1924、Ch23 572–598/自身末注1295（后续其他作者插入可能移动行号；source-family 身份不变）。下面仍有先前提出增量时的 PRE 描述，只为保留审阅历史，均由本段实际终态替代，不是尚待原源/Books待办。未核实现/复现，不等于本日六部分验收。

## 2602.18581v1 — 更新门控，不是无目标学习保证

精确原源：[v1 PDF](https://arxiv.org/pdf/2602.18581v1)，本地`V3_2602.18581v1.pdf`。官方v1 abs只有一个v1且Submitted20Feb19:39:56UTC，原DataCite Registered24Feb03:42:55UTC。PDF第1页实际封面Dated February24,2026/边栏v1，已渲染核对；HTML同一内容桥但署August24异常，不用它承担封面日期。必要正文p6～11（§IV.A～H及V），PDF文本与HTML已核同一门控/covariance/continuous控制机制。

快状态是对称零对角W的tanh recurrent+noise；两个window诊断是低velocity与低prototype，stress为badness及plastic-rent/update-cost的EWMA。越on threshold才开有限commit，off threshold重armed、refractory避免立刻重复，低改善早abort并forced-shortprobe防永久停止。更新目标是demeaned covariance，随后固定spectral radius；不用该归一化就不能把bounded matrix norm归因于gate。连续plasticity保留其余组件的作者对照仍稳定但持续变化；只支持这一toy定义下的episodic更新相对持续更新的组织差异，gating强制分段本身并不是有用知识习得或自然涌现的证明。

必要反侧：理论里的irreversibility未在toy实现；没有外部任务正确性、OOD适应效用、多seed不确定性或参数敏感面。p11仍把stable nontrivial structure条件与open-ended intelligence列为open question。不得采用objective-free必然优于optimization、具有可学习性保证、W模长稳定证明认知/语义稳定；“armed/action可见前后时段”不是随机timestep对照完全等价。可支持设计命题仅为：塑性更新频率与快状态动力学分账、noise transient不能直接触发结构修改，收益仍须任务/参数控制验收。root 已实际 PDF p6–11 与 WORLDVIEW-WHY-MODELS-LEARN Ch4:93–140/409–424；固定rho与门控属成熟稳定化，这个组织案例不新增可证明的学习机制，判仅报告。不因toy或没有LLM任务自动排除，保留候选及反侧。

## 2602.18568v1 — Capacity-for-bandwidth的条件硬件分支

原源：[v1 HTML](https://arxiv.org/html/2602.18568v1)，`V3_NATIVE_core18568.txt`；实际读§II～IV/VI～IX。低batch dense decode若weights+KV近全占容量，每token可读带宽/容量比成为约束；传统扩HBM stack常同时买更多容量。提案参数化ranks/banks/subarray容量并保shoreline bandwidth，chiplet memory-compute-network解耦与on-chip buffer吸收层间计算/带宽不平衡。更少容量不是白送带宽：高BW/Cap每GB成本更高、batch/sequence feasible域更窄，横向增加CU之后activation broadcast成为强扩展瓶颈；不能把长context与高batch都当低latency最佳点。

性能归因：§II是实测H100 motivation，4H100 FP8 Llama70B、batch32、16k prefill/2k decode/vLLM+Dynamo与PyTorch2.2 standalone kernel；§VI是SystemC/HLS N16→N2投影、RTL部分layer功能校验+calibrated symbolic event模型，后者非全模型真实numerical output。§VIII ISO-TDP对照则W4/A16、fullTP、Llama3 70B/405B等，与§II FP8 profiler不能拼同协议。§IX在RPU内部拆HBM-CO/provision/decoupling，memory-customization仅约2.1×latency部分，不应把完整45×归给HBM-CO。cost/energy分析依赖模型、scaling、wire/TSV和封装假设，未制造芯片、无线上SLO或精度质量保证。只支持将BW/Cap作为容量可行性之后的硬件参数与低batch分支，不采用“已部署最快”宣传。

实际owner比较：INFER-GPU-MEMORY Ch54已有memory hierarchy/实际HBM budget及减少表示/提高利用率/扩层级，缺固定interface下容量可调及与batch/sequence feasible-domain的分支。相邻Ch53承serving topology、Ch55承PD workload break-even；本命题不接管PD或compiler owner。root 实际必要源与owner PRE通过，授自身窄锁；已在容量budget后窄写两段及自身末注，作者顺读邻接/正文/末注、diff-check通过，非作者POST待核。

## 2602.18571v1 — 有观测工具不等于执行会先观测

原源：[v1 HTML](https://arxiv.org/html/2602.18571v1)，`V3_NATIVE_core18571.txt`；实际§4.1～4.3/5.4～5.5/6.2～6.3.3/7。工具会原子构建/启动test/等待debug port/attach/break，subAgent只inspect/control/breakpoint/read，没有edit；main通过runtime query收value/stack/location。Java实验再把edit权限延迟到至少一次debug调用，改的是执行可达性，不是更多提示。等base model main/sub同模型，baseline/direct-tools/subAgent/tool-limit四配置；Java directtools可下降（Sonnet75.7→64.5），subAgent78.0，gated85.5；Java call近99%才有更高观测。Python语言上调用与收益不同，不能把Java rigidgate推广所有bug。

对照/代价：subtrajectory25step cap，tokens分main/sub；调用至少一次不保证有有效runtime证据。失败sample50中18 build/attach、17正确诊断但main错修、8复杂multi-session、4API、3静态回答，not universalfailureprevalence。正文§7未计debuggercompute，buildable测试前提/仅两语言一benchmark及强制workflow可能妨碍简单bug。采用“暴露tool、实际采用、产生证据、据证行动、最终验证”五层，不将called once作为已诊断或修复保证。root 实际必要源与AGENT-TOOL-CALLING Ch78:213–232/548–573比较：已有调用收益及证据Gate，但缺可达性前置条件≠有效诊断分支；PRE通过授自身窄锁。utility admission后窄写两段与自身末注，作者实际顺读邻接/正文/末注、diff-check通过，非作者POST待核。

## 2602.18583v1 — 条件类别读取不等于生成或校准保证

原源：[v1 HTML](https://arxiv.org/html/2602.18583v1)，复用`exact-v1-bodies/2602.18583v1.html`并当前v1 abs轻量核信号；实际§3.1～3.4/4.1～4.2、Tables2～5/数据定义。冻结decoder backbone、每metric LoRA与trace-field prompt、preflight单token类别映射，final-position读取class logits并只在class集合归一化；一次forward消除自回归judge解码，但input attention仍随长度增长。直接single-token base与finetuned head对照表明output长度约束不创造评价能力。

数据/配置：promptinjection~2k synthetic Safe-Guard、context adherence~5k 4.4k/0.6k、BFCLv4被重标为tool-quality、tone~4.5k/PII内部数据；GPT4.1 ChainPoll3次平均。F1只这些metriclabel人口，不是工具真实执行或输出事实真值。A100/H100各长度table端到端queryforward+classification；约1250token的150ms对GPTAPI3s只是异后端含evaluator方法的作者条件比较，precision/batch/concurrency/设备资源与全面cost未披露，QPS宣传不采用。

数学收窄：受限softmax CE的normalizer抵消，不对集合外logits提供相对概率抑制梯度，不能采用原文“忽略otherlogits会让无关词概率negligible”的因果表述。runtime是显式取class subset，single-token/argmax确定性也不证明置信校准。当前Ch66 2152～2158整段、前后邻接及末注4631已实际读取，承载metric-specific LoRA/head、focused trace、classprobability normalize、artifact identity、sharedbackbone的干扰/漂移及非天然校准/非真值限制。root 实际 §3.1–3.4/4.1–4.2、数据定义及直接base对照、owner2146–2168通过具体已有覆盖 No Change；不以旧V2.1标签判覆盖。

## 2602.18584v1 — 目标梯度子空间是选择几何，不是逆Hessian恢复

原源：[v1 HTML](https://arxiv.org/html/2602.18584v1)，`V3_NATIVE_core18584.txt`；实际§2.2/3.2–3.3/4/5.1–5.5、AppendixA及E.3必要假设。5%候选pool LoRA warmup一epoch后，对小目标集合梯度SVD，候选梯度投影后cosine，按各目标max选择topk。target eigenspace不必axis aligned，对角缩放不保存旋转耦合，但projector只留方向，既不保curvature eigenvalue也不等inverse-Hessian influence。Eq12/E.3依赖正eigengap和residual/proxy mismatch ε/γ，正文“warmup低loss就保证恢复”不是此条件定理推出；有限验证梯度/经验Fisher不天然等真实H。

对照与边界：Llama2-7B/Llama3.2-3B/Qwen2.5-1.5B、270k instructionpool、MMLU/TydiQA/BBH、三seed；选取方法同5%与finetune预算，Full100%不等数据/compute。fewshot demo既targetselection又evaluation ICL，非未指定分布的通用改善。作者LESS4checkpoint/8192dim对GIST1checkpoint/低rank150/9/50，singleA10080GB的约4×时间和350×存储节约主要来自checkpoint数和dimension变更，不是同几何单模块因果。rank/epoch反侧：后epoch变差、全rank不必最好；方向cosine丢magnitude/token粒度，target bias/漂移未消除。拟TRAIN-DATA Ch27:1069 OPUS后补“learned target subspace vs optimizer-state geometry”的窄分支，现有834逆curvature/sketch不承此有意改选择对象。尚未请求锁或改书。

## 2602.18582v1 — 行为奖励的变量接口决定可表达性

原源：[v1 HTML](https://arxiv.org/html/2602.18582v1)，`V3_NATIVE_core18582.txt`；实际§3–5/6及AppendixB.3。已有taskreward与低层subgoal pseudo-reward之外，LLM分别生成rL(s,o,a)、rH(o_prev,s,o)，低层policy先通过subgoal门槛才进入高层组合，最后另验taskfeasible及behavior alignment。一个相同s/a不能区分先前option的flat接口无法表达交替/持续规则；B.3反例只比较给定state未augment的flat，不证明包含history的flat reward普遍不如hierarchical。rewardgenerator变量权限不是编译正确性或语义faithfulness证明。

GPT4o每配置8candidate×3trial，Flat同两层training但prompt去option字段，Task5trial；PPO低层/DQN高层，三simulateddomain已给固定options/termination，Kitchen固定lowpolicy。先compile/permitted-variable filter，再train/threshold，完整失败funnel须独立保留。Table1行为均值只tasksuccess候选，Figure6任务分母是syntactically valid候选，不能把成功人口76.92%直接写成每次生成成功率；接口更丰富与prompt可表达性共同改变对照，不是纯HRL算法优势。30人分两域视频blindrating仅对应样本，未提供真实开放Agent安全。核“语言→可执行reward代码的state/option/history签名”与taskfeasibility/behavior不同Gate为窄长期命题。实际Ch31:909–915已有自动rewardproposal/competence-aware gate，但未承载变量签名决定表达/先subgoal后highlevel的消费对象与成功人口分母，拟TRAIN-RLHF此处两段窄整合，root核前不写。

## 2602.18628v1 — 中心 non-interference 保证争议

原源：[v1 HTML](https://arxiv.org/html/2602.18628v1)，`V3_NATIVE_core18628.txt`；实际§3–4/5.3–5.5/6/8与AppendixB/C。frozenbackbone外bank Ab/Bb可训练，Fθ(z)吐topk logits，Gφ以firstpass hidden选z，secondpass才finaloutput。95%Gaussianellipsoid sampled256anchors后锁的是Fθ(anchor) MSE Eq13，λlock/λsep加普通loss，不是全region hardconstraint。三个断点：finiteanchors零loss不能推出连续region全点相同；bank可在F固定时改变effectiveΔW；Gφ/input→z变化也未锁。§3.5“bank改就必改field”与所给独立参数关系冲突，§6.1把weightedpenalty称zero-tolerance不能弥补。

Mistral7B Alpaca→CodeAlpaca两task PPL rounded4.35→4.35仅局部作者表现，缺多seed/不确定性；separateLoRA也0forgetting，额外两次forward及323Mbank不等单rank8预算。Figure5的validationPPL2.49与Table3数值口径也不同，不能合并。root 实际Eq3–6/13、§3.5/6.1、B/C独核中心争议终态通过：不删候选/不降分，不采用provablenoninterference、immutablecapability或roll-back等软件类比保证，不进入Books。重开需覆盖全region的函数界、显式冻结/验证bank与coordinate-map保留的实际契约或修正原claim。已有Ch30:630–632承“frozen旧参数项≠旧任务函数保持”，不需用争议稿正面补引用。

## 2602.18613v1 — 固定证据池隔离 selection，不认证 retrieval

原源：[v1 HTML](https://arxiv.org/html/2602.18613v1)，`V3_NATIVE_core18613.txt`；实际§2–4/Table2–3/Figure3。345 MultiNews clusters每组固定8个600char文档、400char summaryfirstsentence作query，全部ranker共用deterministicshuffle，K3～6；BM25/MMR λ.7/Random与Llama3.1-8B/Qwen2.5-7B/GPT5mini。单次shuffle只控制共享输入，不是orderrobustness验收；APIdefault与opensourcetemp0不是同sampling。10000pairedbootstrap与lexicalJaccard/summaryrecall、MiniLMsemanticproxy支持固定人群内模型异质redundancy取舍，不是完整truth/证据充分性。GPT更重复、Llama某K更分散，LLM并非普遍更diverse；更高coverage仍不证明answer收益，未测reader和真实candidate-recall或端到端成本。

实际现有AGENT-RAG Ch76:438–440已具体承载固定pool排序 vs真实candidatepool recall；454–488承coverage/redundancy/evidenceauthority与setutility不等truth。因此本稿三模型新闻slice的局部验证不新增必要正文。root actual §2.1–2.4/结果负侧及具体owner独核：已有覆盖通过，不照录模型排行。

## 2602.18600v1 — 路径正确需拆 visual/structure/objective/format

原源：[v1 HTML](https://arxiv.org/html/2602.18600v1)，`V3_NATIVE_core18600.txt`；实际§2–4.2及AppendixG/H。328map的topology/attributes由Gemini3Flash+deterministic/manualQC，196800query来自有限16400OD而非独立样本；无约束image/edge/table混合拆视觉恢复，与weightedconstraint/edge+vertex拆规划目标。EMA有transfermarker要求，100errorcase中实际路径正确但missmarker也算错，不能由总低EMA推全部规划失败。Dijkstra及合并cost reference依赖表和weight定义，不是真实旅游utility，PMA最长prefix也非完整可行性。

15VLM单场景：dense Metro image加table可比table-only更差，稀疏Travel方向可不同；原文interference/OCR解释非唯一causalmechanism。Thinking模型/分辨率变化并非纯计算预算matched，100errorcase是先排generationcollapse后的错误人口非所有请求prevalence；最短路径碰巧满足weightedobjective可混准确率。只采用诊断矩阵：structuredoracle+samegoal→感知前端/表输入/目标计算/格式证据分账；未测动态环境/生产SLO，费用/precision/重复run不完整披露。root actual必要方法/反侧/过滤及PLATFORM-EVALUATION-SYSTEM Ch66:4052–4078/939–961独核已有覆盖通过，不将路线应用本身整合。

## 2602.18633v1 — private reward channel 的边界仍须定点核

原源：[v1 HTML](https://arxiv.org/html/2602.18633v1)，`V3_NATIVE_core18633.txt`；已读§3–6及AppendixD必要隐私分析。公开prompt+Qwen2.5-3B生成，privatecorpus只进入similarityrewardaggregate，不直接LM输入；s维privatevote向量加σc√s噪声，每T调用composition，训练PPO后输出属于postprocessing前提。AppendixD使用absolute≤c假设，但Fig2仅min(sim,c)上clip；structured两dataset额外Jaccard/turncountKL如何同sensitivity/noisechannel计入不明确。需必要定点核及非作者判，可支持conditionalboundedchannel而不能当前先签全实现DP。

同generator/embedding、2k或QMSum700生成数据对AugPE10iterations；GPT2对DPFT一般更低，BERTsmall改causalmode与原pretrain不同。ε1/2/4/∞局部结果，私有语料公开模拟；gpt4o promptadherence阈值gate不是真实privacyoracle。去promptgateembedding更高但downstream差，PubMed正文与QMSum Table3caption冲突不采用精确dataset归因；AugPE多样性/FID某slice更好。WildChat8A100200step约40GPUh+生成1 vsAugPE100只有作者所列，rewardembedding/judge费用未全包含。必要AppendixC实际999–1005未补range/channel。root 实际Fig2/§4.2/AppendixD独核中心实现DP保证争议终态通过，score6候选不删除，不正面Books；重开需signed range/双clip及全部private reward channel accounting。不据“eyesoff”绕过存在的评分服务原文本访问。

## 2602.18639v1 — 背景不变性是条件经验，不授 reward-free 普遍规划界

原源：[v1 HTML](https://arxiv.org/html/2602.18639v1)，`V3_NATIVE_core18639.txt`；实际§3/4/5.1–5.6/6及必要A.8。冻结DINOv2/SimDINO/iBOT patchencoder后训练32dim projection+transition，pairwise latentdistance对learned nextlatentdistance，无reward项；标准VICReg可能保留主背景方差，提案PCA tail variance floor允许dominant PC不设floor。主PC与nuisance相关是场景条件，未知静态线索不应被一律删掉；公式currentbatch PCA与Implementation165一次PCA不同，currentbatch basis的offdiag covariance本已为零，不采用其额外spread因果。

MuJoCo PointMaze固定transition、50起终点、六类背景/distractor，DINO-WM同horizon但batch32/384dim vs本稿batch20/32dim，DR40%训练样本覆盖有限扰动。NC本稿.78低于DINO .80/DR.82，部分场景DR更高；latent降维与regularizer未全部单因果隔离。SimDINO整体低于DINO，足够informativeencoder为前提；复杂操作/长horizon仍future，不用toy直接排除。理论Theorem4.1 ε-approximate且bounded表示，原bound却无ε；A.8行721–724将ε吸收到d需要未提供的ε≤d(z,z')，零distance无法吸收正ε，不授原普遍零差异规划界。只可采用背景控制与预测/控制表示的受限经验关系。实际Ch25:950–966已有可规划表示可识别条件、1027–1035 transition-vsappearance/静态线索反侧，未直接承PCA tail例；保留有限机制经验但隔离中心theorem，root已必要源/反侧独核中心争议暂缓通过，不进入Books。

## 2602.18645v1 — 选择集合与最终回答使用不同 conditional credit

原源：[v1 HTML](https://arxiv.org/html/2602.18645v1)，`V3_NATIVE_core18645.txt`；实际§3/4及关键Table3/Limitations、A与E。Qwen3-4B同模型两prompt角色：controller读full时序+已选segment/答案决定continue/accept，reasoner只读当前segment回答。训练G=6 interaction轨迹，每最终segment N=6独立reasoner重采；correctness均值给controller整轨迹所有角色tokens，reasoner只给终轮tokens且按correctness方差选一个group。可支持固定集合的消费者可靠性与上游选择credit分责；平均correctness不是单独真值/因果证据，variance选组改变学习人口。A15/18已给σ<ε时advantage=0；只全组σ=0的选组分布退路未明确，不授标准clipped GRPO或无偏保证。root必要源/actual Ch33 owner PRE通过，获锁写两段及末注；作者实际完整邻接已顺读，非作者POST待核。

六univariate任务各自LoRA SFT后fullparameter一epochRL，4H100；八次evaluationrun是采样重复非八trainingseed。Table3只ECG/RCW，w/o reliability改变nested资源/信号，不是同总预算单因果；移controller/fullinput、controller-only与myopic更新亦改变条件。SleepQA TimeMaster+RL显著更高；usage bin低coverage高accuracy是难度/策略混杂，不能推删更多segment必提高正确。额外6×6rollout、迭代推理与encode成本未有完整端到端同预算账。实际Ch33:1471–1513已有conditional hierarchy/strategy N×M但不承consumer最终集合nested均值credit与variance单组更新；拟此处两段最小差额，只采用conditional接口不复制领域榜，root必要源/owner PRE待核。

## 2602.18647v1 — 噪声层级采样改变 effective emphasis

原源：[v1 HTML](https://arxiv.org/html/2602.18647v1)，`V3_NATIVE_core18647.txt`；实际§2–6/8及D。Gaussian I-MMSE只连Bayes MMSE/σ³与entropy slope，当前learned denoising MSE包含模型误差，不是已获得真实entropy。按σ bin FIFO+EMA/最低count/warmup/refresh，lowσ gate后targetρ，以π∝ρ/w构sampler；w固定却πw改变期望有效目标，不授原objective无偏等价。训练数据不新增forward但仍支付buffer/插值/刷新与估计失准；fullpath最小mass未显式保证，零/罕见bin更新可停，不能臆造exploration契约。

EDM U-Net/optimizer/augmentation/EMA同recipe，continuous只π变，discrete w=1 main与fullEDM transfer同时w不同须分账；FID/SeiFID及kEx-to-baseline-target不是wallclock。FFHQ2.56差于EDM2.53、MNIST/Fashion速度1.0，部分收益1.4–1.5在CIFAR，不是普遍2.8；processedexample整数表与正文1.5–2.8亦不采用精确全局倍数。NFE同Heun的grid只图例质量，Eq19额外σ因子与training u定义不同，不拼为同坐标保证。scheduler超参/模型proxy与非Gaussian迁移是边界，precision/硬件/多seed/完整总成本Not Disclosed。实际Ch24:123–132已有schedule/sampling/parameterization共同定义目标，拟补online loss-proxy bin allocation与fixedw≠fixedeffectiveobjective的窄分支，待root PRE，不正面entropy测量或最优配置保证。

## 2602.18649v1 — 轨迹方向低维不等最终矩阵可压缩

原源：[v1 HTML](https://arxiv.org/html/2602.18649v1)，`V3_NATIVE_core18649.txt`；实际§2/3.1–3.4/4/5/7。模97三任务sharedtrunk/三head、3尺度315k～2.2M/5WD共15conditions；trajectorycheckpoints做全参数PCA vs每矩阵ΔW截SVD与padded跨矩阵SVD，不是同矩阵population/rank。Trunk-only重建保finalembedding/head，五轨迹PC可高accuracy但矩阵rank64显著退步，只支持所测结构中低维学习方向≠每矩阵lowrank。需要保存完整N维basis与init/heads，不授只有五系数的成品模型压缩；Figure3只effectiveparameter不完整storage预算。

核心局部表达争议：§3.4描述在final weight vector中移除taskloss gradientcovariance eigenvectors，却把此称activation-space circuit（418–420/425），不能由parameter干预认同activation子空间；taskselectivity也不证明唯一/全部circuit。无自然语言/大LLM/新任务加入验收，generalcontinuallearning与safety皆猜测，noformalfoundation。单conditionseed/uncertainty/硬件/完整cost未披露。实际Ch30:73/119–121已有LoRA不等事后SVD及低维训练方向不授最终weight rank/通用Transformer子空间，188–196有最小Frobenius≠任务质量；拟仅报告受限观察，不为“holographic”包装扩书，root待核。

## 2602.18658v1 — 理论 delta 混合与实际 factor 混合不相同

原源：[v1 HTML](https://arxiv.org/html/2602.18658v1)，`V3_NATIVE_core18658.txt`；实际§3.1–3.5/4.1–4.5及必要B/F。global FedIT 与独立local taskvector先convexmerge；λ=(b−c)/(a+b−2c)由联合Gaussian posterior covariance trace proxy推，LMC basin/smooth/HessianLipschitz及crosscov PSD且≤两marginal为条件，clippedgradientcorrelation+inverse diagonalFisher仅经验近似；upperbound更小不是实际loss必降，denominator退化及diagFisher零项未给全实现契约。Gaussian非退化support与proof bounded basin也不授无条件LLM保证。

必要中心桥：Eq3/8–18使用composed delta θ=B A；AppendixB1153–1160却明确实际Fisher与merge分别在A/B，乘积额外cross terms而不是Eq3，所以不能把同一theory的bound签给实际artifact。ViT400FedIT+300Local对600federated，Llama3.2-3B50+300对600，沟通成本少不等总训练少；client1000/500、训练同Dirichlet测试分布，额外30sample Fisher及5.92h训练之外.46h λ计算，FLAN1.18h/6.83h，不是免费privacy/personalization。实际Ch30:620–632已有factor坐标≠有效delta/乘积协方差及dense-delta回退，拟中心保证争议终态、不正面Books；经验局部merge收益保留，root待核，不遍历全proof。

## 2602.18671v1 — 原始 logit 跨步 energy 不是已识别的 AR joint energy

原源：[v1 HTML](https://arxiv.org/html/2602.18671v1)，`V3_NATIVE_core18671.txt`；实际§3–5.2/Limitations及必要A.1–A.3/B。Eq8以prefix i−1的selected rawlogit减prefix i的logsumexp，另用marginalenergy及scaledΔE，对exactanswer span pooling评价。任意每prefix统一shift c(prefix)不改任何softmax/AR joint，却改变ΔE by c(prev)−c(current)；A.1构造单depth JEM后其partition相等，不证明不同depth构造等于同一AR joint。A.3把跨步两rawenergy视为相同并要求0缺约束；CE不是未优化概率chain cancellation，已规范化AR conditionals自然定义consistent joint。拟中心“必须0/非零意味着joint错或幻觉”保证争议，不正面Books；fixedcheckpoint proxy的经验相关不因此自动归零。

受限三模型人工数值offset的syntheticarithmetic不是自然幻觉发生率；real任务中AUROC是ordering不是置信校准或低FPRreleasegate，不同任务/模型pooling异质且有近chance反侧。Base/instruct不同，noextra classifier但exactspan用Mistral7B辅助extract+最多5次retry，invalid/NOANSWER排除，success约87–94%不是所有请求；punctuation/开头tokens误报。需完整checkpoint/rawlogit读取身份、span与过滤人口、成本，不采普遍training-free reliability。root必要理论独核待办，不扩大wholeproof或补训练实验。

## 2602.18674v1 — Uniform random 局部保持不等 adversarial worst case

原源：[v1 HTML](https://arxiv.org/html/2602.18674v1)，`V3_NATIVE_core18674.txt`；实际§2/3定义与Theorem3.1、§4.1结构/4.2必要条件及§5；parent既有Theorem4.2必要proof独核复用。Feedforward ReLU+单Heaviside binaryoutput，activation cell≤nfaces，uniformsphere radiusr perturbation的classunchanged≥1−n exp(−a(x)²d/(2r²))；a是离unioncellfaces边界的距离，不是verified正确类别margin。Lebesguemeasurezero边界不限制测试分布集中附近；维度收益还依赖n、a、r联动，a缩小或bound负可vacuous。最坏方向可在a<r穿界，randomrare不授对抗安全；r<a则cell恒定亦不证明分类正确。

没有training/benchmark配置，纯定理不凭无实验排除；不外推attention、CNN或LLM tokenattack。现PLATFORM-SECURITY Ch72风险主体/验证链不拥有ReLU球帽几何，本结果也未新增平台控制/威胁界。拟仅报告条件理论，不为随机罕见性扩安全书；root必要源/owner终态核待办。

## 2602.18679v1 — 小 attention 的 ICL forecasting 诊断，不是科学 FM 普遍机制

原源：[v1 HTML](https://arxiv.org/html/2602.18679v1)，`V3_NATIVE_core18679.txt`；实际正文40–110（无section）及AppendixB/C/D/E。两层singlehead、d256/dk128/V100/C512，quantizedunivariate ODE train→不同system OOD，100不同系统pair训练重复；AdamW50ksteps，每1000只一个randomvalidationbatch。OOD双下降不等训练loss作OODgate。按TestOOD大量contexts聚合k-gram conditional operator，对GT fullyobservedUlam谱/不变分布比较；attentionrollout stablerank与Lorenz96dimension相关是诊断，不是内部latentdim真值或因果证明唯一Perron-Frobenius程序。

meanregression弱基线、未给同预算nonattention/组件干预，OODcontext是实际推断支持不是完全无信息zero-shot。GToperatorpartition选entropy heuristic、manifolddim使用5–50percentile距离与幂律拟合，是估计而非真实dynamicD；tokenquantization/scale和有限512history限制可辨状态，样本systempair不是100同taskseed。未测开放LLM/长期真实预测/完整费用。实际WORLDVIEW-LLM-INTELLIGENCE Ch8:82–105已有固定θ/context更新与“内部估计算法需机制证据，存在构造≠训练选择”边界；仅报告这个有限经验ICL线索，不重开science领域或新章，root待核。

## 2602.18690v1 — 空间邻接的预测约束不授真实机器人或生物必然性

原源：[v1 HTML](https://arxiv.org/html/2602.18690v1)，`V3_NATIVE_core18690.txt`；实际正文36–409，方法133–174、三实验175–268及直接限制362–401。Amari recurrent field的7×7 lateral convolution与1×1 input/output保持像素拓扑，前四channel以motor scalar乘法门控；先看3帧，再blind rollout。32×32弹道、120×45 planar double-pendulum是简单2D physics环境；“real physics”是从learned世界模型回到该物理环境，不认证真实机器人/sim-to-real。冻结worldmodel训练policy仍支付 separately trained catchpredictor与真实physics监督，不是无真实数据。

10seeds/100episodes、neuralfield13k/50k vsVAE-LSTM850k/1.7M且后者分两阶段各10kepoch，较少参数不等同总训练/计算匹配。pixelMSE相似而catchrate不同及centroid跳跃支持受测表示/控制误差诊断，不隔离topology、局部连接、门控和训练recipe单因果。局部依赖的传播半径也不自动限制signed reconstruction/多峰场的centroid jump，本文只实测threshold>3pixels；Rchannelselectivity而Cchannel不显著不授完整body schema/生物必然。作者明确需ConvLSTM等结构对照、遮挡碰撞与3D仍future；precision/完整compute预算Not Disclosed。拟仅报告受限空间表示案例，不凭2D排除，也不借生物类比给Books普遍保证；owner差额独核待办。

## 2602.18695v1 — 学习中间顺序要保终点接口并防 schedule 自退化

原源：[v1 HTML](https://arxiv.org/html/2602.18695v1)，`V3_NATIVE_core18695.txt`；实际§3/5/6、D.5.2 1331–1350与E1524–1573。固定L辅助位置[D]→[M]→token，contract成可变序列；以data-dependent Kumaraswamy CDF的hazard决定插入/揭示次序，F(0)=0/F(1)=1保持理论终点，训练φ见clean z1而部署generator θ只见partial xt。REINFORCE双样本leave-one-out加directloss gradient联合更新，不可只detach整份目标。理论CDF端点不认证有限τ-leaping、nucleus/confidence选择的实际终态精确性；近似rate积分和mask输出须另验。

关键反侧D.5.2：联合优化可把事件推到端点以压低rate-weighted loss，而非学得更好顺序；混合CDF线性prior和每位置tε=.01/δ=.01软hinge防该退化，非硬全区间保证。Stargraph端点向junction的任务有有利局部顺序，固定unmask b=1比全自由稳定，sharedbackbone在hard明显更差；相同80k训练/500采样steps但auxtransformer及每例两中间样本额外付费。50ksteps/2048batch/1024steps另一生成实验只作机制压力测试，不收领域science：nucleus/confidence改变diversity/uniqueness，最优参数预算比较不是完全同协议；p=1某项质量几乎相同。硬件/precision/训练seed与端到端成本未完整披露。实际Ch24:1108–1114承rate/destination与固定mask hazard，尚未承data-dependent target-path联合学习的degeneracy/endpoint责任，拟该处窄两段；root PRE待核。

## 2602.18700v1 — 可学的 action-hook 信号是行为取证而非授权证书

原源：[v1 HTML](https://arxiv.org/html/2602.18700v1)，`V3_NATIVE_core18700.txt`；实际§3/4/Impact/A/B/C必要段。先Check含所需动作的eligibletrajectory，最多min(floor(R全量),eligible)选取；保原pair但插入hook action/observation并给prompt secretphrase。保留原pair不证明运行state/副作用不变；选用已有actionspace不等授权。Detection以同prompt truekey/clean/shamkey的hookfrequency差和paired t统计，支持所测训练继承信号，不证明唯一数据来源、许可违法或不可伪造。C把n=NQ独立同Bernoulli/大样本normal作假设，不将“suffices”当小n非渐近FPR保证；固定“OK!”sham不能覆盖任意自然key语义。

MATH1000/SimpleQA2000/SWE-Smith2000正确trajectory过滤，QwenCoder3/7/14B与Llama8B、2epochs/batch8/32768/8H800，R.05；sourcebase能力与fine-tuned对照分开。3B-SWE及Llama contextual近chance反侧，entropy/actionboundary相关不证明归因；DeCoMa/LLM paraphrase/summary三攻击不等适应性删除hook/key或故意伪造训练。Aux30B注入10～30min、检测N×Q三条件、额外执行turn/cost都付费，未有完整尾延迟预算。实际Ch72:191–193已承trigger/target继承、行为取证非原文本水印、误归因/未知学生与provenance权限边界，拟具体已有覆盖；actioncarrier是此受限实例，不为headline扩认证，root待核。

## 2602.18702v1 — 独立片段可回答不等于本次取证的边际价值

原源：[v1 HTML](https://arxiv.org/html/2602.18702v1)，`V3_NATIVE_core18702.txt`；实际§3.1–3.5/4.1–4.6/5，尤其175–193与548–632。coarse64frames×16tokens，groundaction以coarse frameindex转秒后fine16×64接历史。最后片段单独问同policy、对GT答错才−.1 penalty，并仅最终全trajectory答对时激活groundreward；有label用lastIoU+overlap，而非完整多片段coverage。独立lastclip answerability是consumer可用性proxy，不是同prefix直接答/随机clip的counterfactual，不能认证新clip对原轨迹有用、内部faithfulness或对所有错误给探索惩罚。

Qwen2.5-VL7B/rank128 LoRA、group8/batch32/max3turn/2H800，8195label与42549无groundlabel但仍有QA answer，two-stage RL没有SFT不等无监督。Video-MME/LongVideoBench val/MLVU MC dev、无字幕；HR8倍视觉token上限，解析失败改sampling重试3次，额外证据/GTchecker/训练和decode成本需分账。去pseudo整体53.6→52.9，不照录普遍胜出；独立InternVL3.5-38B仅lastclip、32×256，medium反侧54.5低55.3，不同选片人口/长度未全预算匹配。先groundlabel coldstart防groundaction消失，IoUhard单独训练可崩，混合reward非一项因果。实际Ch78:226–228已有同prefix调用增益与randomclip反事实，235–249已有按需video取证；尚缺lastview独立可用性与边际增益不同责任这一局部分支，拟counterfactual之后两段，不授安全/真实因果。root PRE待核。

## 2602.18694v1 — 宏动作、上下文与搜索预算不是独立的 token 压缩收益

原源：[v1 HTML](https://arxiv.org/html/2602.18694v1)，现有 `exact-v1-bodies/2602.18694v1.html`；实际§4 125–194、§5 195–199/555–585、A.1必要缓存与A.2配置。RQ-VAE把observation+macro-action编码成多depth code，同一时间sum embeddings进入temporaltrunk，depth MLP逐层采样，避免把context C展开C×D但depth求值不消失。mask全部longreturn与当前/下步shortreturn，保historyshortreturn；因此code不以当前realizedreturn择编码，不是无reward训练。cached topcandidate+MCTS/P-UCT用learnedfuture/return，不是真实belief或支持集外探索保证；A.1 967–974平均decodedobservation与top10%缓存限制多模态/稀有未来覆盖。

 poolednoiseMuJoCo0/2.5/5三seed模型vsdataset-specific CQL/IQL及引用旧paper数字，Adroit人工mask目标坐标；非真实robot/LLM证据。固定C改L同时改实际history C×L与branching，固定primitivehorizon vsmacrodepth也须分账；D3局部增益D5略退，partialobscontext与depth共同有latency增长。RTX5090/i9作者单run约6h，decisionlatency32candidates/horizon9随context1→12约.09→.35秒，不能签生产SLO/免费并行。拟仅报告受限宏动作/上下文/搜索recipe与局部压力，保留3seed及tradeoff，不把既有RQ/MCTS组合改称新的完整state安全控制；owner独核待办。

## 2602.18710v1 — 同 estimand 与执行合规仍不固定分析 pipeline

原源：[v1 HTML](https://arxiv.org/html/2602.18710v1)，`V3_NATIVE_core18710.txt`；实际§3–5 75–170。固定dataset/hypothesis/estimand，而ReAct Python/shell/fileagent仍选择清洗、缺失值、协变量、函数、estimator/SE；五persona中两项明确confirmation-seeking/p-hacking，不把差异全部视为无意识偏见。四模型T1/max250messages或60min，4946run→3303审计合规人口；按model/persona排除18～48%/强CS57%，不能用合规后supportrate替全请求成功或原数据真值。LLM fulltranscript auditor读toolreceipt比只报告更可核，但Sonnet4.5也作为analyst之一，“distinct”不是所有格独立模型，作者抽样人审无数量/比例披露；少于1%方向错误事后纠正，audit不完备。

结果支持固定task也有persona相关pipeline/裁决分散；相同estimand不消除surveyweight、outlier或clusterSE的选择。选保守/激进pipeline可造成selective reporting，但统计association/有限三task不证明任意persona的因果行为规则或所有有效分析可互换。旧soccer记忆/污染明确，METR“unlikely训练出现”仅作者推断非实际data audit，ANES复杂构造需规范identity。约30compliant/cell与同sample audit、sampling/模型预算不能合并独立humantruth；ensemble/auditor/paypertool成本需保留。实际Ch66:94–108已有EvalSpec人口、scorer/uncertainty，但未承“固定estimand与执行合规后仍有分析规范自由度，必须交代spec选择与survivor分母”的具体分支，拟两段窄整合，不纳领域结论，root PRE待核。

## 2602.18711v1 — attention-guided 特征的定义桥存在中心退化

原源：[v1 HTML](https://arxiv.org/html/2602.18711v1)，`V3_NATIVE_core18711.txt`；实际§3.2–3.3 151–209、§4/5关键反侧、A/B。LURE真/合成hallucinatedcaption pair提取layerdifference后SVD，按HIScomplement软缩projector编辑MLP，不新增部署权重；pair统计方向非唯一hallucination因果subspace，editedsupport须重测。关键断点Eq3定义softmax(QKᵀ)V即attentionoutput J×D，却Eq159称J×J attentionmap；若按通常row-normalized attentionmap解释，168沿key平均每row恒为1/J，所谓positionalimportance退化uniformmean，不能支持核心attention-guided pool超出ordinary hiddenmean的增量。HIS histogram丢位置且KL需support/smoothing，原必要段没有完整normalizedcomplement契约，不能补实现。

作者500COCO/CHAIR、MME、24image/60question LLaVABench GPT4V，三重复但采样训练身份不全，k/layer/beam模型不同且best选择偏置需分账；Colour与detailedness反侧、rank32BLEU低、alllayer未全胜。noinferenceextrahead不等offline pairattention/SVD/hyperparam搜索免费，hardware/precision完整cost未披露。核心定义退化未解决，拟中心机制争议终态，不降分删候选、不正面Books；重开需精确实际attention tensor/aggregation轴、非退化对照与全部score规范。经验objecthallucination结果按所测checkpoint保留，不授knowledge保持/视觉真值，root定点独核待办。

## 2602.18724v1 — 带噪预测差额与动态 potential 不自动继承 metric/shaping 保证

原源：[v1 HTML](https://arxiv.org/html/2602.18724v1)，`V3_NATIVE_core18724.txt`；实际§3.1–3.3、实验§4及必要A.2–A.4。Eq5/6 用独立预测 reward 样本的绝对差，learned transition 加 Wasserstein 项。Gaussian predictor 有正 σ floor，即使同 s/a，两次独立样本的预期绝对差仍正；避免零尺度不证明任务相关 metric 的自距为零。训练132的 target 是 multistep return，不是 theorem Bellman 的 immediate reward；A.3 678–680 明确要求无偏 immediate reward 与真实 transition，这些条件未由 learned artifact 验证。不把 value bound 当有限训练已获得的保证。

Eq12/13 potential 实际读当前 action、随 batch 的平均 reward/nextlatent 与更新 target 网络；A.4 的静态 state-potential 证明不能自动签给这个非固定 Φ(s) 接口。Theorem3.3 的 expected-pair diameter 不等 worstcase diameter，A.2 对下一步 coupling 的平均还须相应分布条件。三个训练seed、MetaWorld像素稀疏任务/1M steps与Maze十seed100k覆盖支持受测经验，不证明所有距离/最优policy不变；Box-close 与组件反侧保留，variance/predictor/target-network及bonus均付费，完整硬件/精度/总预算不全。拟中心保证争议终态、不正面 Books，保留 reward/transition预测与探索的局部结果；重开需精确 coupling/self-distance、reward对象及 static/augmented potential 契约，root 定点核待办。

## 2602.18733v1 — prior-aware 条件复述信号仍不是训练成员证书

原源：[v1 HTML](https://arxiv.org/html/2602.18733v1)，`V3_NATIVE_core18733.txt`；实际§3/4及Limitations。要求 continuation 条件概率越门槛，同时相对 prefix-prior 平均概率的比率越门槛，防常见短语因高概率被误称记忆。Eq3/Definition3 与114–129的 MC 无偏依赖明确定义、归一的同一 prefix 人口；131/实际实验的 dataset prefixes 不自动等同模型生成 prefix 分布，有限样本不能直接宣称真实全词表 marginal。需将实际 denominator 记为其 probe 人口，不补未披露样本/长度律。

受控小GPT2与350训练模型、exact/near-duplicate注入及50实体频率桶支持局部相关；counterfactual去exact不消除所有语义/近重复。大模型 CommonCrawl/Pile近似语料与 SATML1000样本不是实际训练成员真值。m随4/50token改变，n由常见语句校准，不是低FPR安全threshold；exactcopy也提高prior导致比率缓升、无法充分区分大量常见duplicates，249明确保留。额外logprob读取、many-prefix denominator与controlled训练付费。actual Ch72 285–305已有低loss对照、generic-subject/commonprior、条件关联≠membership及语义家族血缘；拟具体已有覆盖，不为更换ratio传感器扩书，root判断待核。

## 2602.18734v1 — 历史 reader 成功率训练 reranker，非因果 document credit

原源：[v1 HTML](https://arxiv.org/html/2602.18734v1)，`V3_NATIVE_core18734.txt`；实际§3.1–3.4/4.1–4.4/Limitations及A Algorithm1。Reranker 先选 topK，generator 的答案包含 GT 给 binary success，历史平滑document success-probability 形成 pairwise hinge ordering target，并交替更新两者。实际371训练 K=1，减轻单次多文档credit混杂，不能笼统说本实验所有共选文档同reward；部署 K3/7 却转为多文档消费。历史值还混入 query/context、exposure与变动 generator，不是文档独立因果utility。原文151承不严格GRPO，Eq11简化policygradient，不授完整clipped optimizer契约。

BGE-reranker-v2-m3/Llama3-Instruct8B、两者LoRA、LR5e−5/1e−5、temperature.7；只有PopQA训练，其余四任务evaluation，初期另用Llama3 coarse doc标签；所以反馈pipeline收益不归一项“peer cooperation”。ASQA/指标及文档数量反侧保留，没有order-shuffle控制就不授排列不敏感；额外generator rollout、历史状态、标签/两模块训练及pool刷新成本未完整匹配。actual Ch76 434–445有离线teacher reader-utility与shared retriever/reranker，但不承自更新 reader 的历史成功标签与 K1→Kmulti 消费差额。拟 UAE reader-utility 后两段窄整合：冻结/版本化consumer与历史统计人口，成功标签非独立credit；请求 root 必要源/最小差额 PRE，不先写 Books。

## 2602.18739v1 — physical 条件攻击是白盒受限分支，非真实驾驶风险率

原源：[v1 HTML](https://arxiv.org/html/2602.18739v1)，`V3_NATIVE_core18739.txt`；实际§4/5.1–5.3/6与必要Supplement评委标准。DriveDreamer/2白盒物理condition梯度，用clean reference branch的diffusion-loss threshold管理阶段，再以SDXL-inpainting目标/SSCD语义方向攻击HDMap与3D box。条件名叫physical不等硬物理约束，τ门槛不证明data-manifold、连续轨迹或安全；两阶段/EMA均非保证，也不把正文反序t下min索引擅自改成精确first-visit实现。

nuScenes700/150，前者从头官方recipe、后者发布checkpoint，25diffusionsteps/448×256/100生成每实验。GPT5与20驾驶经历人评至少两人每片的三axis平均>.5为ASR；评委“不确定”可打.6，no-risk.2，分数不是真实道路risk或内部causalfaithfulness。并非只visual judge：实际276–277/346–353有800frames/100videos合成augmentation的FCOS3D检测下降及ST-P3/VAD相关open-loop三秒轨迹指标。必须保留这份有限downstream证据，但openloop collision%不授闭环部署频率；human/GPT差异未隔离唯一appearance-bias机制，clean/attacked训练与完整重复/预算未全披露。白盒access、reference branch、target生成及backprop付费。拟仅报告有限condition-channel攻击及fidelity≠downstream作用案例，不因驾驶领域排除，也不从成熟diffusion攻击包装扩Books；root必要源/owner终态判断待办。

## 2602.18742v1 — IDM 标签须核 video–action 一致，回放相似非安全证书

原源：[v1 HTML](https://arxiv.org/html/2602.18742v1)，`V3_NATIVE_core18742.txt`；实际§3/4.1–4.3与A/B必要配置。生成视频→IDM pseudoaction→simulator replay，再由冻结V-JEPA2+.crossattention probe比较两video运动，real demonstration/replay正pair、时间错位/跨episode负pair训练分类器。分类score筛样或Best-of-N最大值；验的是 action标签与视觉运动的受限一致性，不是真实环境完全可执行性、任务成功或physics证明。V2V复用action还依赖object identity/shape不变与calibration；probe负例覆盖不认证所有接触/动作误差。

ActionNet3k/30k subset、GR00T N1.5、60ksteps/batch512、前50k全样后10kcurated/真实与合成1:1，fine-tune各任务steps调优；ALLEX三任务各24trial/48realdemo包含有限真机证据，不是只有simulation。sim24tasks各50trial，articulated任务VideoCon39.0、DreamGenBench40.7与本40.3，非全slice领先。probe最高50epoch、视频生成/IDM/simreplay/Nsamples及额外visualaugmentation均付费；固定prefilter10k不等equal retained set/完整compute。IDM失败、sim-to-real或classifier失准时回真实labels/直接BC，不授motionmatch安全。actual Ch26 583–612有derivedlabelprovenance与appearance复用身份，但缺“伪action回simulator→与生成video的运动一致性核标签”训练admission。此处两段窄分支已落实，root实际必要源/owner PRE及写后完整邻接/自身末注POST通过、锁释放；不接管Ch25 world-transition或runtimecontroller权限。

## 2602.18745v1 — 可 render 的 IR 对齐不等 parse 成功或真实几何完全恢复

原源：[v1 HTML](https://arxiv.org/html/2602.18745v1)，`V3_NATIVE_core18745.txt`；实际§3.1–3.2/4.1/4.3–4.5、B/C及I。symbolic predicates/proofseed→metric/text/code realization→semantic/coordinate检查→deterministic rendering；从image先预测plotting IR再reason/answer，使entity/segment/annotation可单独核，不只是geometry合成配方。semanticvalidator与Instructor/Coder都实际GPT-OSS120B，“独立语言模型”文字不等独立model family或真值authority；coder不读trace/answer减泄露但不证明完全无信息泄露。数值constraint检查/parse/renderclarity与语义真实性不同gate。

264705symbolic→35297seed→18176保留，10510semantic/4171coordinate/2017execution/423visual拒；Qwen两7B LoRA128/2epochs/bf16，GRPO4samples只format+answer，greedy评估和224resize须保。code/caption/none相同输入对照支持这套supervision局部改善，但length/总训练cost未全匹配；Testmini219parse/49nonparse的solve37.9/36.7%相近，189含annotation子集正确43/84与错误16/105有相关不证明唯一因果，segmentF1不覆盖circle/allmetricsemantic。平面Euclid/教科书图像、LLMhallucination与高reject、未广跨backbone是直接限制；生成验证render、IRtokens/训练都付费。actual Ch23 572–604已有caption辅助与多目标alignment，却不承“可render scene IR的结构/annotation vs syntax验收”。拟caption分支后两段窄分支，只representation owner，不纳geometry排行榜；root PRE/锁待办。

## 2602.18746v1 — region marker 是重读 proposal，不是新增视觉事实

原源：[v1 HTML](https://arxiv.org/html/2602.18746v1)，`V3_NATIVE_core18746.txt`；实际§3/4/5.3、B/D效率与E限制。反思关键词→Molmo7B point→SAM2.1 marker原图→再读；GT teacher correctivefeedback转firstperson供SFT，训练保留teacher严格增分/最终10分/GT一致的人口，OCR/Chart关键词还来自GT。这不是模型无外部正确答案自行产生internalfaithfulness；部署selfvalidation终止不认证独立groundtruth，定位模型/segmentation也会错。

Qwen2.5VL7B LoRA32α128/3epochs/2H100；同dataset单轮QA、wotool和trajectorymixture对照能拆部分训练和观察作用，但额外视觉/turn预算不等matchedcausal；ρ1纯纠错反退、.75局部最好不授普遍比例。MMVet3.73s/112.58token只是作者局部效率，Molmo/SAM调用完整资源与precision/重复未全披露。Abstract数学无法spatialground、flowers组合属性退为泛检测，marker不验证这些命题。actual Ch23 537–551已有未决claim观察与marker回读、定位proposal非新增证据/selfconfirm非正确性；Ch80 278–293拆retry/re-grounding/critique。拟已有覆盖，只报告这个有限训反思recipe，不为“closedloop”扩书；root终态待核。

## 2602.18749v1 — loss 变化训练选样器，不认证 learnability 或推理路径真值

原源：[v1 HTML](https://arxiv.org/html/2602.18749v1)，`V3_NATIVE_core18749.txt`；实际IV-A/B、V必要Assumptions/Theorem与VI配置/消融/通信反侧。两方向DPO-like loss把server/client的整串likelihood对比作为偏好，角色方向不自动认证较好/正确reasoning，非真正path结构对齐。Eq5/6跨轮/批比较不同所选样本及count的exp(loss)总和，reward同时混入更新、人口/量与query，不能当单样本causal learning gain；训练ExploitNet预测共同reward、ExploreNet拟residual不等校准uncertainty或真实UCB保证。>.5阈值/首轮cluster与movingconsumer需版本绑定。

5500MC/3client各1000train500test、1000public、≤5round、不同模型1–5epoch、8A800/三run均值，fourheterogeneous configs与现family命名原文混写，不自行造checkpoint。通信3.87–6.71MB并非最少(FedMKT更低)，不等训练/公共teacher query/filter10epoch的净效率；某hyperparameter和server暂退，去filter同时改所有public人口，不是同tokens因果。V192刻意把selector在bounded-variance分析下等同随机，且强凸化/二阶Lipschitz/界domain及τ'=1才rate简化，条件theorem不证明这套自适应LLMartifact收敛，不追全部proof。actual Ch27 148–172已承版本化data-control/历史loss predictor与heldout独立，成熟DPO+banditproxy组合不新增可验证learnability条件，拟仅报告有限双向蒸馏case；保经验不因federated自动排除，root终态待核。

## 2602.18721v1 — 声学证据驱动 pseudo-label 校正，迭代仍会积累错标

原源：[v1 HTML](https://arxiv.org/html/2602.18721v1)，`V3_NATIVE_core18721.txt`；实际§3/4.2–4.6/5。每轮ASR给有/无label生成hypothesis，audioLLM在有label的audio+hypothesis→GT上训练，再校正unlabelaudio；rule-CER/length/重复/digit gate或label训binaryWERfilter后喂ASR。文字纠错能流畅但未得声学证据，原audio对textonly有限对照支持groundedlabel质量，不认证LLM真值/beam普遍最好/所有正确发音。Corrector与ASR两者更新及filter改变接受人口，不能由完整loop收益归单机制。

WhisperLargev3/VoxtralMini3B/DeBERTaBase、QLoRA4bit/rank16、5epoch/batch128/8A100、5runs/3iterations，四语音语料按sourcefile/meeting分割；textnormalization删punctuation/filler，WER非全语义/安全。同Earnings21audio前后次序test6.34相同，beam3test更好beam5unlabel更好，不授任意modalorder/greedy绝对差；主loop第二轮后退，epoch/LRdecay只缓解，moreiteration不单调更好。模型filter过拟合有限label，rule可拒绝真correct大量改动；额外corrector训练、全量decode/beam/过滤无端到端matchedcost。拟仅报告有限声学co-trainingcase及反侧，不从成熟self-training+音频条件组合扩Books；原Ch27:151–164已要求teacher/student modality/verifierlineage，但具体声学供证关系仍由root定点判断，不自动EX。
