# 有限cs.LG补口：贡献准入待独立校准

原first2000停止14997，未穿过本窗身份段，不作为覆盖完成；仅取官方`/list/cs.LG/2026-02?skip=2000&show=2000`，当前响应跨过20162–21206，57个未在原156题摘中的标题作为有限查漏。不是其余2000条或整个cs.LG的题摘队列。执行UTC见V3_FETCH_lg-window-title.json。当前列表题目可为后版；采用的题摘严格v1，20730后版题目不同但同ID不多计家族。

20个含糊/潜在贡献/安全signal标题已实际完整读v1题摘，实际原文包V3_LG_NEW_ABSTRACTS.md 1–128（各ID独立标题）。摘要不能计必要方法审阅。本表未授root独立准入通过或评分；once项仅补一次决定准入的具体核心，IN只进入必要命题证据层。

| ID | 拟准入 | 实际增量/具体退出依据 |
| --- | --- | --- |
| 20307 | once | 已有ICL不能仅换time-series就入；题摘重构pretraining输入/输出关系，需一次确认是否有可迁移新因子化/heldout-task机制，非普通few-shot模板data augmentation。 |
| 20329 | EX | SCM mapping drift/intervention生成可控shift、classifier退步后恢复为成熟合成移位实现；未给新识别条件/大模型机制或旧评价反证。 |
| 20370 | IN | equivariance仅universal approximation不知size-rate→同规模ReLU/DeepSets/Sumformer/Transformer定量表达界→改变硬编码对称性损失表达能力的判断；限equivariant目标类。 |
| 20396 | IN | 观察multivariate attribution可能引入collider/suppression→因果context干预Shapley并给消除该偏差理论→须分开association与采用已知SCM的归因；非科学域结果。 |
| 20403 | EX | online Wasserstein DRO saddlegame+piecewiseconcave budgetallocation是一般稳健序贯优化；题摘未建立神经模型学习/训练执行的新直接条件，不因optimizer owner关联而收。 |
| 20418 | once，安全signal | GNN模型提取后embedding与label双输出signature可能新增verification机制；“first/robust/noauxiliary”本身不足，核一次具体signature/反侧条件能否跨出GNN子图工程组合。 |
| 20419 | IN，安全signal | model-extraction ownership从相似headline变MI相似度+实际threshold理论条件→可核验证据权限，不先授任意model所有权证书。 |
| 20467 | IN | 直接移除weight的saliency→同时最优邻接bias扰动再定义importance→改变稀疏移除/补偿误差的选择；小FC实验不必排除。 |
| 20549 | IN | diffusion prior缺归一化证据→利用posterior reverse过程time-marginal中间samples估evidence→改变多prior选择/不匹配诊断与采样预算；不采用blackhole科学结果。 |
| 20567 | IN | directed mixing仅收敛不足→stationary imbalance与spectral gap联合进入finite-iteration稳定/泛化与早停→改变有向通信拓扑/stepsize取舍；条件理论非任意LLM保证。 |
| 20593 | IN，安全signal | train honest-but-curious仍可infer-stage feature poison→无需训练时植入trigger的新信任边界→核training/inference权限及label辅助条件，非把VFL privacy措辞签为隔离。 |
| 20629 | IN | 数学judge平均分遮蔽rubric人口→course/expert双rubric和人审对照揭示系统性inflation→改变judge校准reference条件，非仅增加题目。 |
| 20698 | IN | user级污染与good-batch内部异质/污染分层→高维SoS及两级误差下界/上界→改变聚合证据中的batch averaging与异质不可消除项；限mean估计假设，不借泛Federated关联。 |
| 20730 | EX | 离线warm-up/DPO+Mamba+heuristic bootstrapping用于TSP/CVRP，题摘只有成熟模块组合与memory/throughput优势，未指出新成立条件/可比反证。 |
| 20758 | IN | opaque posterior GAN换likelihood需重训→Langevin unfold可在推理设定likelihood参数→新增模块化采样/条件漂移适用机制，限posterior问题，不授physics truth。 |
| 20804 | IN | benchmark成功被当作history/协调推理→reactive/memory对照和temporal influence探针37场景揭示同步耦合替代解释→修改评价能力归因条件，非MARL主题映射。 |
| 20921 | IN | discrete/continuous ResNet泛化界假设不连通→flowmap与deep-layer limit得到depth-uniform/structure dependent界→核模型深度的泛化解释，不授任意Transformer。 |
| 20971 | IN | robust interpolation不等robust generalization→robust loss Rademacher/Lipschitz与扰动radius共同条件→改变平滑/容量设计结论，MNIST只是局部验证。 |
| 21020 | IN | imitation measure匹配被当低exploitability→exact matching仍失败/一般hardness，dominant strategy或best-response continuity下恢复界→核多交互policy匹配与均衡边界，不涉及经典机器人拼模块。 |
| 21191 | EX | Gaussian-smoothed halfspace agnostic SQ complexity与L1 polynomial逼近度下界，尚无改变当前foundation模型形成/执行机制的直接链；不因通用learning理论名称自动准入。 |

负样本分层：SCM synthetic drift、一般DRO、NCO模块组合、受限SQ半空间理论均保完整题摘；模型提取及triggerless安全signal即使最终EX也须独立核。其余37个明确领域/传统优化标题在官方raw留存，待下段逐身份具体理由，不以整类机器学习排除。

## 其余37标题范围关闭（无所见纠错/安全signal）

完整题目与同ID定位保留V3_ARXIV_LG_LIST2.raw的list-title；此层不评分、不宣称完整摘要/全文已读。以下按具体题目切片理由，不因机构或分类排除；若后续出现直接机制/安全纠错证据只重开受影响家族。

| ID | 标题级具体理由 |
| --- | --- |
| 20175 | Tensor-network辅助TSP优化，非foundation训练/生成或执行机制。 |
| 20194 | FedAvg用于bridge deterioration CTMC hazard，是领域预测应用。 |
| 20199 | regional partition/metaheuristic ensemble用于imbalanced多类分类，未指基础模型机制。 |
| 20210 | Any-to-Any crystal建模的科学领域生成；ROADMAP科学应用暂缓。 |
| 20224 | LLM/ConvexTopics检索anti-aging文献，科学文献应用。 |
| 20232 | neural wavefunction molecular orbital学习用于coupledcluster，科学域研究。 |
| 20271 | delivery delay multi-task预测，物流领域regression。 |
| 20306 | cardiac mechanics surrogate与geometricaugmentation，科学/医疗模拟应用。 |
| 20399 | physics simulation lift geometric pretraining，科学模拟路线非通用生成机制论点。 |
| 20404 | active MDP model estimation统一探索，是传统MDP估计路线，不是模型驱动LLM规划。 |
| 20442 | sparse EHR unknown-missingness imputation，医疗数据填补应用。 |
| 20449 | proteinLM comparative inference，protein科学学习路线暂缓；不凭LM字样引入。 |
| 20468 | graphcontrast crossscale timeseries anomaly detection，未指foundation机制。 |
| 20527 | apprenticeship学习student pedagogicalstrategy，教学策略领域建模。 |
| 20530 | prototype/cooccurrence mixedemotion识别，传统领域分类模块。 |
| 20557 | symbolicregression equation generativespace，科学方程发现非本主线生成模型。 |
| 20573 | GNN molecularregression architecturebenchmark，科学应用排行榜。 |
| 20578 | online nonmonotone DR-submodular凸域最大化upperlinearizability，传统组合优化非直接模型训练机制。 |
| 20643 | GPT+RL urbanmobility trajectory，是交通领域应用。 |
| 20651 | sparse Bayesian functional regionselection，传统统计函数估计路线。 |
| 20671 | gradientboosting federated bike demandforecast，城市需求预测应用。 |
| 20677 | urban spatiotemporal foundationmodel，标题领域泛化未指跨任务基础机制；urban建模范围外。 |
| 20714 | CFD piano-key-weir geometric surrogate benchmark，科学流体模拟应用。 |
| 20729 | fuzzyguided robustsafeRL，传统fuzzy controller组合，不以safe词收。 |
| 20782 | EV energydemand FLforecast，能源领域预测。 |
| 20809 | AlphaZero regretguided searchcontrol，传统gamelearnedsearch非LLM驱动规划。 |
| 20932 | EEG2Text hierarchy decoding，脑信号专域解码评价。 |
| 20947 | binaryclassifier Wilson KDE confidencebound，统计二分类估计未指foundation calibration新条件。 |
| 20974 | multifidelity surrogate spatialtrustweight，科学代理模拟路线。 |
| 21043 | channel-head绑定TSimputation，专域填补模型模块。 |
| 21046 | prototype/MCTSbrainnetwork disorderdiagnosis，医疗分类应用。 |
| 21072 | offdynamics offlineRL localdomainadaptation，传统RL动力学迁移非foundation/vla接口。 |
| 21078 | proxyguided federated semisupervised，一般半监督FL模板无题名直接新基础模型机制。 |
| 21092 | GNN topology activationpattern，graph-specific结构诊断未指foundation表示条件。 |
| 21104 | ski-rental unknownquality distributionprediction，经典在线算法路线。 |
| 21168 | sequential counterfactual temporalclinical inference，医疗时序因果应用。 |
| 20344 | fragment-based分子self-supervised embedding，科学molecularrepresentation应用。 |

核对：标题关闭37身份，57新标题=20完整AB+37明确标题范围退出；漏列20344已实际raw13725–13745恢复完整题目并补分子领域理由，不用计数代替实际阅读。

root实际独立20完整v1AB准入校准通过：20329/20403/20730/21191 EX，20307/20418 once；20698在once核心确认mean aggregation直接改变哪个模型/平台聚合判断，不因user/batch词强挂Federated。其余明确潜在IN进入必要命题证据，不授headline/theorem普遍成立。Registered全20原值保原文包，v1 Submitted均晚于prior-slot cutoff（最早20307为02/23T19:48:47Z），当前sameID Registered精度上界均在02/26 09前；Updated/Created不作公开字段。

root actual一次核心终态：20307 V3_CORE_2602.20307.txt413–620 Alg1随机same-task IO concat/原input，成熟ICL模板未新成立对照EX；20698 txt292–490 unknownboundedcov P的rawmean双级污染，没有实际gradient/model聚合桥，通用robuststatistics不足直挂当前主线EX。20418 txt795–1125/1490–1567/1688–1735保持潜在贡献2+2+2=6候选，中心Eq1 top2−top1的ReLU恒0不能签boundarygap，root定点确认Disputed终态，不自补符号/不入Books。拟经验verification只保局部来源身份，不授所有权低误报；重开需一致boundaryscore定义/实现及ownership误报验证。日期明确落窗后三者不追加附录。

来源停点纠正：月目录先primary再cross，不可只用整个页面maxID作跨分类覆盖。LGskip2000包含primary末24286后cross重新00002并停14472；仅定点补skip4000剩余672cross标题本窗主题，非重开已校准20或读整类摘要。CL全1936的primary/cross均已跨窗；CV首2000仅primary至22819，补skip2000的末662用于本窗cross相关标题。csAI实际首页primary1068至24288、cross只至05670，补skip2000穿本窗。未冻结候选，不用可恢复普通coverage缺口冒充external终态。
