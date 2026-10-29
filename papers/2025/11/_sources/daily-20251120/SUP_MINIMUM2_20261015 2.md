# Nov20 窄主题四个最低域实际提案

## 1. 本轮必要范围

作者Noether。只接`SUP_ARXIV_NARROW_20261015.md`四minimum的具体决定事实，非四篇标准Evidence/全文。实际原件`SUP_WEB_MINIMUM2_20261015.raw`及后续tail，采用精确v1；ReflexGrad晚v4新标题/触发规则不回填。此包作者提案3窄P/1C尚待Ohm核，不授日期或并入通过数，首14的12P2C保持。

## 2. ReflexGrad 14584：拟窄P，有限反馈接口不授causal/convergence

实际§4.1–4.5 L230–392、必要6.1/6.3 L514–609。TODO状态需TextGrad进展与轻LM比较前后observation都判完成才推进；反思取working最近5项和当前经验，进入后续textual-gradient上下文，policy经LLM semantic merge更新，最近gradient也给反思上下文。这是原v1明示的任务状态/两反馈消费耦合，不只画三角色图，拟保局部设计潜力。

原Fig1称三步merge、每5步/失败反思，正文Eq11每步merge，不能照录唯一严格schedule；merge仍LLM而非deterministic优先合并，双LM不是独立因果真值，r<=0标签亦不等每个中间动作真实失败。原9环境/2trial的few-shot aggregate对照不等计算/条件，23/23 alignment不证明因果/普遍无loop或stable convergence；有实际Table2三种ablated构造，但预算/seed/人口不足以授一般保证。只保反馈/状态接口，未用晚v4进展门、134任务/十seed/计算匹配或强causal归因。不是因LLM merge或组合本身排除真实局部控制变化。

## 3. SAM-Fed 14302：拟窄P，teacher/student动态监督人口

实际Server/Client/Alg1 L81–135及结论必要169，原server LoRA适配teacher并广播其权重与public labeled数据；client先有监督训练，再每像素比较teacher/client。相同label用共识且weight1，不同则选最大softmax confidence一方/权重也取其最大值，进入weighted CE。冷启动teacher与随后local适应的监督选择关系有具体潜力，不只是医疗数据上SAM+FL改名，拟窄P。

这是可错置信/共识控制，不是calibration或真实标签；双模型同意也会共同错，confidence不跨模型自动可比。原L111写SAM只单次推理，L114/Alg1又说每训练iteration双方预测，确切refresh/caching费用有冲突，不照录无重复teacher费或完整recipe。结论称global/client双向KD，但所读最小域没有完整展开双向global更新，不能因“dual”签全机制已核。只保具体pseudo-label消费规则，不采用临床效用/隐私或泛LLM收益，也不因这些反侧自动关闭潜力。

## 4. DevPiolt 14227：拟具体C

实际§3.3 L176–184及阈值分析必要243–244。score对device/field/value概率加预设权，再对actions平均；复杂candidate/数值属性阈值降10%、上级device低置信整条不展示、最后融合first-token confidence与平均，选0.7取exposure/acceptance折中。已辨清具体规则，不由confidence标签直接当新安全门，也不因IoT应用标题C。

该必要域是常见分层confidence过滤/曝光取舍的任务化heuristics，未辨明新的校准机制、执行/权限保证或足以改变主线结论的独立反证；pretrain/SFT/DPO和推荐指标不能替此增量，拟C。自然语言/启发式控制不是天然无价值，本项关闭只针对这个实际增量。原acceptance只曝光人口，不能签全部任务质量或操作安全；不为未知日继续请求、也不展开全用户/在线实验。

## 5. LGSID 14221：拟窄P，编码约束与强保证分开

实际Method L117–180，尤其HGIT155–180。first layer用经纬/行政/类别/brand加权特征MiniBatchKMeans定组，再以组内LLM embedding均值作第一codebook；后层才在embedding residual上学欧氏聚类、recon loss及cluster-use KL。固定外部属性分区与后续残差几何不由同一学得codebook拥有，这个编码/consumer分工有潜力，拟窄P，不把所有推荐应用纳主线或因推荐领域自动C。

RM/G-DPO强解释不采用：Eq3是distance rank正权，Eq4展示只含`-p*log sigmoid(r)`的正项，不是完整binary CE，也未在该域闭合rank概率/负项，不能从这式认证地理排序或目标well-posed；Eq6是reward差的policy/reference对照而非普通token logprob DPO，Eq7又有距离排斥项，未授语义保持/概率校准。只留固定属性首层/learned残差的构造假设，不把缺监督对照变C，也不采整个优化配方正确性或真实地理truth。重读边界若显示需更多决定事实，只重相关式/规则，不扩全部工业实验。

## 6. 原件与交接

请root转Ohm实际最低域：3窄P/1具体C为作者当前提案，尚未通过。ReflexGrad具体schedule/归因、SAM-Fed单次与每轮teacher冲突、LGSID强优化保证的数学口径都保原反侧；不由本域签完整Evidence或Books。其它minimum（LIT/Video/Kandinsky）尚普通，本包不预签。Objects本人note admin已真实保存待root单差额闭合；SAM3/S2ST不重，97/132不含Nov20，无普通消息/stage/commit/push。
