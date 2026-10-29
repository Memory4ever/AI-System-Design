# ANIRA08864：必要Source/owner/PRE请求

Understanding Dynamic Compute Allocation in Recurrent Transformers，精确2602.08864v1，2+1+2=5。root完整AB/日期已通过。anira-core.json实际完整§3–6；anira-direct.txt为官方A.2配置、A.4/5直接反侧与A.8.1–3必要测量人口。只围绕early/online信息资格、冻结状态与allocation不认证算法泛化深入，不修一般proof/不读全附件。

§3 prelude/shared recurrent/coda，E浅层一次depth categorical；O每步中间表示条件halt概率，剩余mass形成depth分布，D收尾。CE只answer，KL(q||exponential prior)全token，−entropy+log(b)Edepth，b=1仅负熵不是depth penalty。静态训练展开D，已退出token passthrough冻结，KV仍可被其他active tokens读取；decode过去token只存到exit深度d*，请求d读min(d,d*)。这是定义改变后的执行语义，不是删除token或恢复full-D原计算。E训练ST Gumbel/inference mode，O逆CDF/ST训练，§3.2.3 inference median-CDF .5；A.5又称main exclusive mode、图caption写E而标题O。此默认规则与统一Pareto宣传冲突隔离，正文不采用具体哪个默认取得数字，需作者统一阈值协议后重开该保证。

§4 execution=sum active token-step vs decision=head调用分账，decider约8%params，不授系统wall time。O模拟E论证依赖identity recurrent/expressivity假设，非全训练普遍优越。§5 MANO L3–16、BREVO N3–30、CLRS移除trace合并为23tasks，PCFG3b LANO与parser代理；算法answer mean actualdepth vs语言token expected depth不同分母。D MANO14其他6，1/1prelude/coda；5.1M/13.7M synthetic模型、AdamW250kstep单A100约7h，E小验证grid选LR/gamma/b后复用O，precision/重复CI/SLO未披露。

§6.1/T1 synthetic expected-depth parser correlation E/O expansion .666/.456等，不等真实语言难度或internal执行因果。§6.2/Fig3 unseen size含interpolation sharp下降；A.4所有4模型MANO超train L仍明显退步，O较缓不是algorithmic generalization保证。§6.4/T2回归控graph N：E多structural hub、O多DFS/frontier；A.8只correct samples且E26,641样本/210,640tokens、O1,718/14,046，信息人口不等；用expected depth连续目标而主算法actualdepth。相关/筛correct人口不能授唯一内部算法追踪，保作者解释为hypothesis。

§6.6八层recurrentLlama约5B Nemotron math fine-tune，4×A10080GB/day，b32/len4096/lr2e-5/gamma.1。GSM-Symbolic main/p1/p2 fixed8 acc46.26/23.54/5.80，E45.70/24.06/5.80 mean6.060/6.004/5.982，O43.68/23.02/5.08 mean4.108/4.105/4.001；更难未多算，O各split有质量下降，不授同质量省算/通用难度解释。depth/D只recurrent执行/KV proxy，不包含prelude/coda/head/sparse dispatch、训练staticD或生产TTFT。

actual MODEL-TRANSFORMER-LAYER Ch17 531–565：停止先验段解释深路径训练机会，08220段是two-axis mask+reach混合/targetprivilege；尚未具体比较cheap early structural cue与online执行state的决策身份、discrete frozen-token KV语义及allocation跟难度≠generalization。Ch16/18入口actual重读。唯一Ch17，拟紧接08220末段559之后/双时间尺度标题前一段；不另写Ch66/Ch45。尚未root必要Source/PRE或锁，未写Books。

拟文：停止器还要声明它在何时拥有何种信息。便宜的浅层预测器可以一次决定每个位置的深度，逐步停止器则读取已经付费得到的中间状态再决定继续；二者的决策调用费用与实际活跃token-step须分账。采用离散退出时，已退出位置可冻结在该深度，让其他位置继续读取其KV；请求更深轮次只读取该位置最深已缓存状态。这保留退出语义而非完整深度的原计算，也不是把退出token从历史中删除。受控递归实验中，早期分配更关联结构线索，线上停止更关联执行状态，但相关分析只来自已答对人口；分配随算法复杂度增加也仍会在未见长度失效，自然语言更难切片甚至没有多分深度。故应把决策身份、freeze/cache规则、训练与部署停止口径、质量和长度泛化共同版本化，不能用depth/D认证完整加速或把“多算”当正确性。停止头、静态训练展开与稀疏执行都付费，缺少可靠停点或质量回归时回退统一预算与独立任务验证。

拟链接exact-v1#S6；自身末注保median/mode冲突、correct人口、自然math反侧与完整系统费用未证。请求root实际Source/owner/PRE及Ch17窄锁。
