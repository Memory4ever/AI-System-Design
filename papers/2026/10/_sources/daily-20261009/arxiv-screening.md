# 2026-10-09 arXiv主题发现与准入

执行者：supplement_20260311；仅owner本文件，正式报告由supplement_20260312维护，Books/共享索引由root协调。窗口仅北京时间2026-10-08完整自然日；2026-03-11已完成并停止写，不用于本日候选或分母。2026-10-09约13:15执行；已fresh完整重读AGENTS、研究/Report合同、Prompt、ROADMAP及来源使用/Daily/arXiv/recovery，未加载Weekly组。

## 当前漏斗与停止

首包4项官方完整题摘实际读完，可准入；root已独立AB校准同四项（见[independent-review](independent-review.md)），本包不重复计跨源家族，不授必要Source/Books完成，不采用摘要性能数字。当前页均v1且未见撤回说明，不遍历完整版本史。官方公开归属来自[DC Oct8列表](https://arxiv.org/list/cs.DC/recent)日期组，不把Submitted Oct7或Recent首Oct9当Oct8。

实际官方DC列表20行起Oct9，132行起Oct8，共22条、编号13–34；作者已读完此日期组的标题，329行遇Oct7停止，不遍历旧日。CL当前[skip144/show100](https://arxiv.org/list/cs.CL/recent?show=100&skip=144)确认20行Oct8组、118条，实际标题浏览到编号173（2610.09671），不是118条完整题摘；剩余仅有界查漏线索，不自动完整AB/全文。

root两篇必要Source委派已逐篇完成并交接，随后依授权续原query分页；本记录固定真实停止点，不重读四项已校准AB。本轮最终检查时间2026-10-09 13:59:50北京时间（时钟实核，不作公开筛选条件）：系统/多模态/Agent查询均到Oct6提交边界停止；模型初次超时后缩到Oct7提交段有限恢复，start0/50/100已读至结果末端。官方分类宽标题只发现，不自动逐项AB队列。

## 主题查询执行与真实分页

API使用`https://export.arxiv.org/api/query`，均`start=0&max_results=50&sortBy=submittedDate&sortOrder=descending`；时间条件仅14日发现上界，`published`字段仍是Submitted元数据，不证明本窗first-public。精确查询如下：

```text
(ti:transformer OR ti:"language model" OR ti:"foundation model" OR ti:MoE OR ti:"post-training" OR ti:reasoning) AND submittedDate:[202609250000 TO 202610072359]
(ti:inference OR ti:serving OR ti:offload OR ti:"expert parallel" OR ti:GPU OR ti:kernel) AND (cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG) AND submittedDate:[202609250000 TO 202610072359]
(ti:"world model" OR ti:VLA OR ti:multimodal OR ti:"video generation" OR ti:"audio generation" OR ti:"vision-language") AND submittedDate:[202609250000 TO 202610072359]
(ti:agent OR ti:RAG OR ti:retrieval OR ti:"tool use" OR ti:memory) AND (cat:cs.CL OR cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.LG) AND submittedDate:[202609250000 TO 202610072359]
```

网页查询入口不可达；最初curl正文解析失败不计有效读取。修正后系统/多模态/Agent三查询首50身份、提交日与标题已读；14日返回量244/770/1390不去重、不作本日分母。系统首50在index16遇2610.09111（Oct6）即题摘选择边界，前一项2610.09250，后续响应虽存在不形成旧日队列。多模态start50第一项2610.09217（Oct6）停止，不需读后49；Agent start50 index0–39的Oct7标题已实际读，末项2610.09240，index40的2610.09237（Oct6）停止，不续start100。

模型14日query18秒超时，不记零；只将同query下界改为202610070000，25秒有限重试成功，总101，start0/50各50标题已读，start100唯一末项2610.09274（Oct7 01:13 submitted，Hardware-aware Calibrated Clustered Attention for Efficient Visual Geometric Transformers）已actual读，结果末端停止。该收窄只恢复Oct7提交段，不保证完整24小时公开召回；Oct7 cutoff后提交的109xx/108xx与延迟编号106xx仍可能Oct9公告，必须用官方组隔离，不能因Submitted收进Oct8。以上API只题名发现，不是完整AB筛选或候选分母。

## 首批准入（仅AB）

| 官方精确v1 | 原约束→实际新增→可能改变选择 | 日期/当前信号/状态 |
| --- | --- | --- |
| [MemFerry / Fast and Memory Efficient Offload Training Framework with Hybrid XPU Computation](https://arxiv.org/abs/2610.09657v1) | 传统offload仅CPU更新且GPU利用/重叠受限→GPU经DHA读取host中层参数、forward调度同时搬其余参数，backward再驻留；shadow模型统一分区、梯度DHA调度与scale-up多路径→重选训练计算位置/驻留与通信的取舍。 | DC Oct8组19；current仅v1，无撤回信号；具体潜力准入，不授实测收益/实现或全面正确。 |
| [CoMoE / Democratizing MoE inference on commodity GPUs with CoMoE](https://arxiv.org/abs/2610.09424v1) | 弱PCIe/host介导无P2P的MoE通信瓶颈→host单写共享token后multicast、staging中的token粒度combine替全局同步→重选dispatch与同步粒度，非硬件成本比例本身准入。 | DC Oct8组21；current仅v1，无撤回信号；具体潜力准入，不授privacy或普遍消除stall。 |
| [vLLM-Omni Technical Report: A Unified Serving Runtime for Omni-Modality Generation](https://arxiv.org/abs/2610.09307v1) | 单文本decode-loop不能统一异构生成阶段/长会话→orchestrator admission/stage推进/流输出分派与专门engine replicas、connector重载荷data-plane及session control分责→重选服务runtime的请求、数据和会话状态接口。 | root DC Oct8原件及本作者DC #22（213行）已核，完整current AB已读、仅v1无撤回；具体潜力准入，不授API兼容/夜间CI等生产保证。 |
| [Expert Coupling in MoE Pretraining: Reducing All-to-All Overhead with Correlated Placement and Token Shuffling](https://arxiv.org/abs/2610.09372v1) | EP按固定布局多次dispatch同token→已测router跨/内层相关性提议expert共置、每GPU单发token及attention reduce-scatter中预测下一层位置→不改router/expert而重选通信/布局，不因加速数值入池。 | root DC Oct8原件及本作者DC #32（307行）已核，完整current AB已读、仅v1无撤回；具体潜力准入，摘要相关性不授prediction可靠度/完整通信语义。 |

四项完整题摘读取入口为current官方/abs精确版本链；必要Source逐项由获授作者独立记录，不由本筛选表授完成。需报告作者在日期/身份去重及必要证据之后按拟采用命题评分，不从机构/性能数字反推分数或Books差额。

## 新增四项完整AB准入（root独校准通过）

本人实际读current精确v1完整标题/Abstract及已有当前说明；不读全文。均未见当前撤回标记，不遍历全版本史。root随后独立actual四份完整AB，按下列具体增量通过准入；四家族与首包4去重后不同，当前共8完整AB准入，不是所有query命中的候选数，未授8项必要Source/Books完成。

| 材料与实际AB位置 | 具体增量→改变选择（仅潜力） | 日期/状态 |
| --- | --- | --- |
| [Reproducible LLM Inference Benchmarking: A Sequential Isolation Protocol for Regression Testing](https://arxiv.org/abs/2610.09778v1)，AB16–19完整；首次输出截断后已单项补齐 | 无控制系统状态使重复推理测量漂移→sequential isolation提出稳定回归参考，并随concurrency定位tail transition→重新选择性能回归的基线/状态与并发人口，不以CV改善或成本数字准入，不外推生产流量。 | [PF列表](https://arxiv.org/list/cs.PF/recent)58行Oct8组、60行#5；date=2026-10-08确认；具体评价盲区潜力，未评分/Source。 |
| [Your Prompt Should Do More: Effects of Retrieval Instructions in Embedding Models](https://arxiv.org/abs/2610.10508v1)，AB16–17完整 | prompted embedding对query-side distractors不能稳从instruction→用该干扰评价并在fine-tuning加入query distractor→重选instruction-following检索的评价/数据控制；题摘训练假说不是已证唯一因果。 | 原CL skip144/show100 Oct8 #146官方组已核；date=2026-10-08；具体潜力，未评分/Source。 |
| [PHRBench: A Behavioral Evaluation of Post-Hallucination Reasoning in LLMs](https://arxiv.org/abs/2610.10455v1)，AB16–19完整 | 只看终态正确掩盖hallucinated premise后续行为→受控假前提轨迹分别看compliance/avoidance/correction与最终答对→重选过程恢复和outcome的分测，不把4820任务库存或相关预测视因果。 | 原CL Oct8 #147官方组已核；date=2026-10-08；具体潜力，未评分/Source。 |
| [Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation of Four Mechanisms Across Two Corpora](https://arxiv.org/abs/2610.10170v1)，AB16–18完整 | context heading收益可能只是prepend改变embedding、hierarchy gate漏证据→chunk匹配与合法shuffled-heading placebo/first-stage recall对照→重新选择结构检索归因与门控；QASPER只是RAG人口，不由论文领域词变Science应用，不授局部效应普遍性。 | [IR列表](https://arxiv.org/list/cs.IR/recent)201行Oct8组、203行#20；date=2026-10-08确认；具体潜力，未评分/Source。 |

## 明确标题层范围外与待核线索

- DC Oct8编号17（2610.09713），官方完整原题“Rendezvous under Variable Disorientation:The Algorithmic Power of Fixed Unit Distance”（172行）：讨论定向失衡下移动实体rendezvous与单位距离算法，非模型驱动Agent或训练/推理执行机制；标题层范围外关闭，不称其一般分布式理论无价值。
- DC Oct8编号18（2610.09659），官方完整原题“Communication-Aware Qubit Placement and Automatic Node-Count Allocation for Distributed State-Vector Simulation”（181行）：分布式state-vector量子模拟qubit布置/节点数，不是foundation模型计算/通信贡献；标题层范围外关闭。
- DC Oct8编号20（[2610.09512v1](https://arxiv.org/abs/2610.09512v1)），官方完整title/AB已实际读（web cache miss后curl官方原HTML恢复）：针对graph连接/非平衡mass的distributed quadratically regularized OT提出solver-free projection、局部penalty与AP-ADMM理论，AB仅泛称ML应用，未提出模型学习/表示/训练执行关系。具体范围EX，不因ADMM或理论标签排除，不须全文绕补关系。
- DC Oct8编号13（[LOCAA2610.10487v1](https://arxiv.org/abs/2610.10487v1)），官方完整title/AB已实际读（同恢复）：仅tool-integrated LLM+guidance+memory搜索科学模拟数据compressor EB，在三个科学应用上减少试验，没有新模型/Agent机制或可核主线failure边界。暂缓Science应用具体EX，不采用试验减少数字。
- DC Oct8编号15（[2610.10148v1](https://arxiv.org/abs/2610.10148v1)），官方完整title/AB已实际读（同恢复）：云tenant bottom-up SCI与provider报告残差分配、idle/embodied carbon问责愿景，无基础模型/训练/推理workload或机制关系；通用云会计不是AI平台贡献，具体范围EX，不称残差方法无价值。
- DC Oct8编号16（[HPC-MQBench2610.09786v1](https://arxiv.org/abs/2610.09786v1)），AB16–18已完整读：Slurm自建Kafka单broker实验的delivery qualification与auditable config selection，明确非独立分配因果、multi-broker未来；没有模型/训练/推理系统增量，只可通用测量类比，具体范围EX。四项不为无关准入日期/全文另建队列，Oct8归属可复用DC原组。
- CL首组10533、10426、10332、10232、10179及10508/10455已转下文实际AB，不再记未读；其余CL页面宽标题不自动队列。

当前可执行工作：限定主题query与有界Oct8相关标题查漏、具名含糊完整AB/日期与准入分解。首包即交报告作者/复核者，校准后只展开受影响集合；不声明全分类/全站Coverage、0遗漏或整日完成。

## 模型query四项具名机制线索的AB决定

这是已执行query标题中的具体机制/评价命题，不是对101条全量AB。四份精确v1完整title/AB已实际读，当前页无撤回标记；贡献潜力清楚且官方日期已定点核完，未评分/Source，不将Submitted当公开。完整范围如下，交独立准入：

| 材料（官方AB实际位置） | 实际增量→改变的选择 | 状态 |
| --- | --- | --- |
| [Executing Causal Structure Learning with Linear-Attention Transformers2610.10395v1](https://arxiv.org/abs/2610.10395v1)，16–19完整 | 只会因果答案不等执行算法→固定权重block保存graph及multiplier复现连续优化update，准确算法执行和准确因果恢复分测→重选Transformer可执行算子/state充分性；普通训练学该executor仍开放，不授learnability。 | 明确模型机制/理论潜力；官方LG Oct8组#338确认2026-10-08，非Science应用。 |
| [ResidualQuant2610.10381v1](https://arxiv.org/abs/2610.10381v1)，16–19完整 | loop共享参数但KV随loop扩张→末loop KV作reference，其余低精度residual，least-square/rotation/loopwise precision→重选跨loop状态表示与重建；不按理论bytes或吞吐数字准入。 | 明确cache机制潜力；官方LG Oct8组#342确认2026-10-08。 |
| [OnlineQAT2610.09346v1](https://arxiv.org/abs/2610.09346v1)，16–18完整 | fixed completion恢复漏量化student自产prefix→blockQAT初始化后以冻结FPteacher在student访问状态给reverseKL信号→重选低bit恢复人口；成熟OPD在该失配的受限新验证可核，不授唯一因果/2bit普遍收益。 | 明确恢复边界潜力；官方CL skip144/show100 Oct8组#189确认2026-10-08（只targetdate，不扩大标题全读声明）。 |
| [Layerwise Error Attribution2610.09877v1](https://arxiv.org/abs/2610.09877v1)，16–18完整 | budget分配组合爆炸/坏校准→分离propagated/local perturbation的概率误差分析及separable score无需solver→重选mixedbit allocation/calibration鲁棒性；DRUNet及diffusion是量化方法人口，非暂缓科学应用，未经必要源不授概率保证。 | 明确量化机制/理论潜力；官方LG skip324/show100 Oct8组#401确认2026-10-08。 |

定点日期恢复真实入口：LG recent初次show2000响应25秒截断，但已完整目标Oct8 header/10395#338/10381#342字段，不借截断称完整列表；随即缩至[skip324/show100](https://arxiv.org/list/cs.LG/recent?skip=324&show=100)，完整响应核09877#401、09679#420。CL仅以原skip144/show100同组定点核09346#189，未把其后标题全量计已读。

## 其余已具名查漏线索的完整AB（准入独校准通过，Source另行逐项）

仅围绕已读题名中具体latent更新/训练预算/诊断控制/上下文删减与首组五个命名线索，非全API命中逐项；下列9份完整题摘已实际读，当前精确v1无撤回标记。5个CL首组公开日复用已实际标题的Oct8组；其余4只定点恢复日期，不追精确时刻。

| 材料及完整AB位置 | 原文实际增量→改变选择 | 日期/决定 |
| --- | --- | --- |
| [PaTh / Think Before You Paint2610.09876v1](https://arxiv.org/abs/2610.09876v1)，16–19完整 | frozen diffusion不修视觉约束错误→小recursive thinker在每denoise内更新latent、经ControlNet引导，无symbolic target/solver，且注入错误恢复反側→重选pixel推理和sampler纠错接口，不以10M或题摘成功率准入。 | 官方AI skip302/show100 Oct8 header下目标ID实际确认2026-10-08；机制/有效性边界潜力。 |
| [CERO2610.09679v1](https://arxiv.org/abs/2610.09679v1)，16–19完整 | per-update预算不管整个horizon→concave exposure surrogate/Fenchel supporting slope及shared budget price控制prompt admission/revisit/round groups，组大小固定→重选RL训练全周期budget pacing，不授surrogate=真实学习收益。 | 官方LG Oct8#420/date2026-10-08，明确潜力。 |
| [The Attribution Blind Spot2610.09493v1](https://arxiv.org/abs/2610.09493v1)，官方完整title/AB（webmiss后curl恢复） | match文本不等依赖来源→pairedstate magnitude诊断vs有符号PC1 equalnorm控制，并分trainingexposure与行为sourcechoice→重选诊断与干预方向/核泄漏证据；OLMo曝光检测不显著不能当不存在。 | 官方AI skip302/show100 Oct8 header下目标ID实际确认2026-10-08；明确主线反证潜力。 |
| [EntroPrefill2610.09757v1](https://arxiv.org/abs/2610.09757v1)，官方完整title/AB（同恢复） | attention集中不能认证删context→sinkisolatedGQA pooling+discardedmass约束，head删除包络/自适应observer/条件perturbation，反例拒浅观测未来无条件保证→重选midprefill准入与物理page/transfer分账。 | 理论机制/边界潜力清楚，无实测不自动EX；2026-10-08日级夹证（下段），不授条件保证成立。 |
| [EngramEdit2610.10533v1](https://arxiv.org/abs/2610.10533v1)，16–19完整 | frozenbackbone的ngrammemory共享更新伤旁事实→多表达target memory匹配、joint共享embedding更新及重用频率惩罚→重选memory edit locality/表达覆盖，不授nearperfect或能力保持。 | 原CL Oct8首组已核；明确潜力，未授formal独立更新。 |
| [CoTrace2610.10426v1](https://arxiv.org/abs/2610.10426v1)，15–18完整 | harness搜索轨迹混作replay漏runtime依赖→组件分promotion、verified harnessmatchedSFT与freshonlineRL的routing/curriculum→重选数据/执行人口，不授题摘foreignscaffold唯一因果。 | 原CL Oct8首组已核；明确机制/边界潜力。 |
| [Task-Progress Distillation2610.10332v1](https://arxiv.org/abs/2610.10332v1)，16–19完整 | 完整teacher reasoning未必利小agent→compactstage-actionpair监督与admissiblejointscore/harness，stage益处随示教量消失→重选蒸馏内容与数据预算条件；小模型/负面不EX。 | 原CL Oct8首组已核；明确受限机制/反证潜力。 |
| [LLM Persuasion Is in the Eye of the Evaluation2610.10232v1](https://arxiv.org/abs/2610.10232v1)，16–20完整 | 单persuasionrank混任务与拒绝→同15models共享setup的9评价弱一致、ability与willingness分离→重选能力/规范行为人口与跨task外推，不授refusal唯一因果。 | 原CL Oct8首组已核；具体评价盲区潜力，不研究健康应用。 |
| [Beyond Outcome Rewards2610.10179v1](https://arxiv.org/abs/2610.10179v1)，16–18完整；必要[HTML intro91–102](https://arxiv.org/html/2610.10179v1)实际定点补齐 | AB泛称新signal/路由不足，最小intro核到同observations的passagecoverage/CovDep/answer-match × scalar/localquerytokencredit及preservedactionalignment控制→重选信号身份与credit支持集的联合比较；不只因关联RAG收，准入事实清楚即停。 | 原CL Oct8首组已核；具体机制/有效性边界潜力，非全Source完成。 |

EntroPrefill日级恢复：精确v1 Submitted=Oct7 09:44:59UTC不能直接作公开日；[arXiv原始公开规则](https://info.arxiv.org/help/availability.html)说明ID在公告时才分配，Tuesday14:00–Wednesday14:00 Eastern批次最早Wednesday20:00，即2026-10-08北京时间（当日EDT）。[DataCite官方原始记录](https://api.datacite.org/dois/10.48550/arXiv.2610.09757)标题/DOI/已公开arxivID匹配、state=findable、registered=Oct8 02:41:24UTC（BJT10:41），作为已公告ID的上界；上下界均落Oct8，按日级夹证确认，不把registered/Updated单独作first-public。LG当前Oct8段skip324/424/524/624及Oct9段0/100/200/300的定点ID检索均未见本ID（624含Oct7header即停止目标恢复、不扩旧日），保留该列表缺失而不据此EX。show200与首show2000截断不作完整列表证据；未追精确firstpublic时刻、全文或作者历年材料。

当前明确AB漏斗：25唯一精确v1完整题摘＝首8已root独校准准入＋新增13经review_mar11_continue完整题摘独校准准入通过＋4具体AB范围EX（reviewer已独读通过）；另2标题层EX独校准，不混入AB分母。新增13公开日均有官方组或同日夹证（EntroPrefill）支持，root已独立定点确认09757日级夹证；具体独立范围见dc-core-review.md，准入不授Source或Books完成。未新query、不追14日更早页；其余宽命中不自动排队，不冒充全分类召回。本人本轮普通发现/AB/日期操作已结束，候选必要Source和Books状态由各自材料记录与正式报告维护，不授DAY。
