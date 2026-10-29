# 本日新增正式项必要证据与 Books 比较

writer Popper。日期层复用 sole reader R3 的28精确身份合法联合日，均2025-10-14；原件与字段不重命名为实际公告时刻。以下只有实际完成的读取层，不预签reader/Books。

## 11012 COCO-Tree v1

准入沿旧完整AB/校准层。2+1+2=5，标准必要读本日 `REPAIR_CORE_11012.html` §3.1–3.3、§4.1–4.3、§4.4成本与数据差异、§4.5–4.6及Limitations；未读全附件/图像素/代码、未复现。caption先分M实体，再按S分支/L深度由LLM递归生成entailed concepts，以LLM语言yes概率与VLM视觉yes概率加权评分，再greedy/beam选路径和原VLM分数融合。实体分解/概念图是模型生成的条件，不是原图事实；Table6 judge entailment不证明faithful真实推理或因果解释。

Llama3.1-8B、temperature0、M2/S3/L3；EqBench2500测试，调参1000 disjoint EqBench-Light，ColorSwap另用train；七VLM/四bench与小样本200复刻CECE比较不能外推全任务。语言侧改善的image选择收益较弱，更多分支/深度收益饱和，失真概念和高置信误感知可自强化。§4.4写O(M*S*L)与Limitations的breadth-tree指数成本有张力，不补成严格复杂度证明；不采低资源/净加速。全部LLM生成、节点VLM评分、搜索/缓存与回归计费；硬件SKU/precision/端到端时延和重复seed不在上述必要域披露。

owner拟MULTIMODAL-REPRESENTATION Ch23。实际已读开篇L47–51空间关系可读/消费者失用诊断、L198显式region回灌与grounding非事实；这些不承载caption-entailment树的分解/视觉双评分与路径融合。拟新增长期命题只这一条件化接口，非整框架摘要；完整邻接/PRE尚普通。

## 11016 InstructUE v1

2+1+2=5，标准必要复用旧最低门并实际从 `SUP_CORE_INSTRUCTUE.raw` 读§3.1–3.3/§4.1–4.4与Table2/3相关完整人口和原件AppA配置（首输出截断不当全读）。f(X,I)条件化表示、末USER token读出，AR答案学习与用户/文本contrastive共同训练，downstream labels再调instruction token的class-prototype对比目标。该label使用不等无监督指令去噪、通用零样本或不需标签。

Qwen2.5-0.5B/gte-base，UserQA200M；六场景各1M、linear probe拟合/评估各半且不重合。Table2手写指令在Ant Forest、Purchasing Power、Food Preference等不必优于Universal；Table3 AvgPooling在部分场景数值更好，与正文“consistent degradation”冲突不能照录全胜。t-SNE分群不是去噪或业务因果。多源编码、合成/预训、标签/提示优化与重编码全部计费；公开必要域无独立seed CI、隐私隔离证明或完整服务成本。128 PPU是原配置口径，不改造GPU SKU。

owner拟AGENT-RAG Ch76的检索表示消费者，而非token lookup Ch12。已实际读Ch76开篇、L160–178附近latent响应/双向表示及多阶段query/candidate条件读出；仍须对照条件指令优化的具体差额再决定，不凭主题匹配No Change。未写Books/未PRE。

## 11031 LogiNumSynth v1

2+1+2=5。实际读取本日partial HTML已经完整到达的§2形式表示/规则和自然语言转换、§3.1–3.4、§4相关过程/答案对比和Table5结果、AppB限制/F1配置。传输448664/799621，未授整页/全部F实现完成。Facts/Rules/Query先在形式world上产生DAG/gold，控制逻辑depth/规则条件数与数值表达类型，再模板化/LLM润色；只合取/蕴含、常数/检索/线性运算和二项聚合，不是一般现实逻辑truth。过程评分由Qwen3-8B结构化提取，替代正确路径可算正确，长/交错引用仍会错；answer高不代表理由可读或忠实。

29模型/四难度加极难；SFT只Llama3.2-1B与Qwen3-1.7B/LoRA，不能外推大模型或一般能力。调用API默认配置、开源模型3090/4090、temperature.3/top_p.8/top_k20，不与API模型当同预算。生成/规则求解、润色、过程提取、训练及外部任务核验全计费；输出长度/训练完整seed CI与端到端成本不在已读域明确，Not Disclosed。owner拟TRAIN-DATA Ch27的可控难度数据生产，现开篇collection定义不足以替代formal-gold→language-proxy双身份；完整owner/邻接待核，不整合模型排名/通用性能。

## 11062 Stronger Together / AT-GRPO v1

2+2+2=6。实际读`REPAIR_CORE_11062.html` §4.1完整Alg1/Eq4/三个算法小节、§4.2、§5.1/§5.2角色共享反侧/§5.3完整Table3和Limitations。不同role/turn/history使普通same-question组不可比，原算法每个当前(e,i,t)观察分K支采样，组内算advantage并保留全组，执行最高reward分支继续环境；不把hash(e,i,t)本身当内容身份检查/全历史相同证明。团队加本地reward，不推无偏counterfactual credit。

Qwen3-1.7B/8B no-thinking、单8H100、K4/T4、alpha1；SA代码/数学single-turn而MAS多轮/工具与角色不同，不署纯协作同费因果。角色共享数学局部可胜、swapped-policy大退步支持身份敏感，不支持通用角色专化。所有分支reward/环境执行、未选样本、更新/多模型驻留及回归计费，precision/完整token成本/独立CI在必要域未披露。CPU sandbox是作者设置，不授任意真实工具安全。owner拟TRAIN-GRPO Ch33组定义与树采样，不复制系统pool正文到本章；实际group owner缺额/邻接尚待具体比较。

## 11210 Discursive Circuits v1

2+1+2=5。实际读partial原件中完整§2.1–2.3/§3实现与metric/§3.1–3.3、Limitations直接域；末附件截断不冒全读。替换connective并由GPT4o-mini生成反事实continuation，取clean/corrupt状态作一阶edge-attribution patching，按平均绝对edge分筛circuit。单GPT2-medium先在heldout CuDR微调到约80%正确；32采样discovery/validation、五次重采样，稀有关系/过相似continuation被过滤。恢复normalized logit difference不是自然话语能力或全model压缩证据，也不证明circuit唯一；分母近零/错答人口需保留，边重叠与域内faithfulness无相关反侧(r=-.007)不藏。跨框架需手工relation映射，SDRT较难；40人工valid只指示性。未核全部映射/图像素/代码/复现，不授0.2%可部署算量或普遍层功能定律。owner拟WORLDVIEW-REPRESENTATION Ch5，采用对照构造/局部归因和功能交叠测量边界，实际正文比较待继续。

## 11302 Detection TCO v1

1+2+2=5，因数字口径具体冲突对受影响域深入。实际读§3全部费用/式3–9、§4完整配置/抽样、§5.1原人口及§6费用解读。只采用固定前置标注/训练与每次inference成本、类别taxonomy/质量分母共同决定break-even这一条件命题。1000 COCO/200新类、YOLOv8m固定COCO taxonomy与Gemini开放新类不等同目标；新类YOLO0不证明不能适配。105/200却写52.3%、100k时$25/(100k*.685)却写$.00050，§6切换91.2/68.5到89.7/72.8等准确率，不能照采55M/286倍或绝对CCD。API/免费额度只是本稿历史假设，不作当前报价。T4/FP16/batch16属于YOLO，API硬件不披露；冷启动、标注/训练和长期维护不得重复摊销，图像与object成功单位也需一致。

Books拟已有覆盖：PLATFORM-COST Ch70实际L215–240已明确同质量functional unit、完整lifecycle/分摊、unit cost/demand volume/quality-SLO/marginal value分账；L268–280 ROI不只GPU。本文数据未建立可复用的额外阈值，采用范围不超既有该具体论证，因此不为新论文名加段。需reader核这项具体NoChange，不自签。

## 11307 FOSSIL v1

2+1+2=5。实际读本日HTML §3、§4.1–4.5、Table1/2、§5.1–5.2相关反侧、§5.3及Limitations。语言反馈embedding与instruction/observation/action共同形成序列条件；辅助MSE预测下一反馈但**预测token不回灌**。CNN同步训练、SentenceBERT冻结、Llama2仅参考结构而非预训权重；backbone约90M与总模块约146M不混。BabyAI-XGen像素局部观察，BFS及随机替换planner动作构造optimal/suboptimal，oracle用特权state/goal生成语言与标量反馈，不是自然人评或部署可取得真实反馈。

语言不普遍优于scalar，未见空间位置泛化较弱，组合也非每项更好；模态/反馈改变了信息条件，不能把收益纯归为语言表达或普遍stitching机制。主线只采用次优动作的条件消费与辅助预测/在线反馈的分责。反馈/特权标注、全部轨迹、训练与闭环评估计费，真实物理/人类反馈成本未证；不采安全/通用机器人/端到端效率。owner拟MULTIMODAL-EMBODIED-VLA Ch26，需具体消费位而不是借TRAIN-SFT另写通用loss。

## 11370 Rollout Routing Replay v1

2+2+2=6。实际读HTML完整§3.1–3.3、§4.1–4.3公式4–9及prefix接口、§5.1–5.2/完整Table1。只重放rollout选出的expert mask，training logits在同mask中重新softmax，保router梯度但不使gating weight/activation/输出概率相等；这也改变训练当前router自由选择路径。prefix mask与KV共同缓存须绑定同prefix/模型/路由身份，不能由文本一样签当前权重可复用。§3 k3估计公式方向标签与采样基准需谨慎，不采其绝对KL作完整分布证据。

Qwen3-30B-A3B base/SFT，verl/Megatron/SGLang；batch256×8、prompt2048/response30720，dynamic sampling只保部分正确组。mini_step8 lr1e-6与mini_step1 lr3e-6不同；每五步评测后取各项best step，非同checkpoint/固定预算最终分。TIS+R3可低于R3，残余mismatch仍有，不能证明route是唯一成因或完全稳定。实际硬件/precision在必要域Not Disclosed，全部route存传/缓存/复算、未用rollout与选择评测付费。owner校TRAIN-GRPO Ch33：实际L2119–2127已有route作为behavior identity/冻结路由与staleness/不可用回退，但没有“固定mask、重算train gate”与prefix缓存的双状态消费分工，拟窄增，不照搬到Ch36或改MoE基本模型章。

## 11414 Uncertainty-aware TBAC v1

2+1+2=5，授权风险按受影响内容深入。实际读§III–V完整policy/resource-risk/uncertainty tuple、两个use case及§VII/VIII。resource manifest给静态risk，LLM合成tool/transaction权限并估uncertainty，risk或uncertainty超阈值就人审，否则mint短期capability；PEP另验token。示例数值是假设，不是实验。MCdropout/ensemble/stochastic disagreement只是可选估计提议，§V又让LLM自述不确定性，不能等同校准概率或独立安全判断。语法检查不足以授权；缓存tuple还需manifest/identity/有效期，不由“相同任务”跳过重新授权。

Books提案仅报告：研究提出双轴gate，但校准/动态risk/注入防护都列future，未证明其自动approve门可采用；现有PLATFORM-SECURITY主体/独立授权及纵深防御不应被未验证judge替代。保留新提案和失败路径的报告价值，不删候选/降分，不将尚未验证的autoapproval改成长期可靠配方。未运行token服务或代码，没有部署/安全保证。

后续实际owner比较纠正上述初提案：reader R16指出“未实现”本身不排除长期proposal；writer已完整读Ch72 Safe-commit/certificate与Tool Boundary、邻章交接。原all-world证书/独立IAM不承载risk和epistemic分别触发升级、再由短capability/PEP执行的具体双轴接口，故PRE08 I25改为窄整合提案；明确未实现/未校准和未来注入测试，不采可靠autoapprove。不是降分/删反侧，也不是修好原安全结论后采用；实际PRE/SAVE/POST以canonical后续层为准。

## 11498 ReLook v1

2+2+2=6。旧最低/安全强反侧有效；本轮另实际读完整§2.1–2.4、§3.1–3.4及Table1/2、§3.5/3.6，补标准层。policy tokens有GRPO advantage、critic feedback tokens mask并可另蒸馏；三时刻render截图只为视觉评分条件，valid-render约束不验交互语义/全部安全。critic-only accept-improving+最多10次resample不是自然质量单调；critic-free仍最多三轮selfedit。Qwen7B/Llama8B、3000任务、去重和多个子集、三seed、temp1/top_p.7；独立Gemini judge不等human truth，原稿human-study新做/继承冲突保持。WebRL FullStack可低于base，不能照录strict全胜；64GPU训练与4H20 policy/8H20 critic单并发100query的推理角色分开。§3.5 123.04→18.03只是移除critic/截图路径、非所有费用或同质量保证。训练/全部拒绝与重采、render/feedback/蒸馏、搜索选择与闭环验收均计费。

owner AGENT-REFLECTION Ch80：已有独立feedback、比较器与介入价值，不覆盖训练阶段按视觉proxy择优轨迹、部署撤critic后消费资格变化，拟窄增并保human来源冲突，不为单调宣称背书。

## 11660 ManiAgent v1

2+1+2=5，数据标签/执行风险受影响域深入。旧SUP_MANI_MINIMUM及独核§18必要完整复用；本轮实际从本日HTML读§III-D及§IV-F完整数据采集、15cm成功proxy/scene reset规则，其他框架与性能不扩采。任务prompt exact match后按object index/当前坐标重绑cache，真实新任务评测关闭cache，不能用该真实成功率证明缓存数据路径。450/551有效、19.5h/15次人工restore/每约46min，手动恢复与模型训练合格是不同人口；CogACT normal execution不证同count同预算等human quality。

owner TRAIN-DATA Ch27。实际collection协议/自动采集段已有一般筛选/provenance，但“任务完成率→缓存自动采集proxy→有效示教/人工恢复人口”仍须具体对照正文再判。只数据资格与周期完整成本，不采通用新MAS/物理安全/无人采集。尚待writer实际owner比较，不用普通待办改终态。

后续实际owner比较更新：Ch27 L501完整Seed2Scale段已明确collector/target/judge独立lineage、binary-success admission与success内quality分层、失败探索/reset/人工审核全费和独立success sensor。与L100的通过终态非全过程正确共同承载本次采用的数据资格/全周期成本命题。ManiAgent的cache执行资格不在本次长期采用范围，不以Ch27改写动作缓存协议；原450/551/15次restore作为本例直接反侧留报告。因此提案**已有覆盖 TRAIN-DATA Ch27**，具体承载为该完整Seed2Scale及原生交互标签段，不另写框架/末note。待reader核该NoChange，不靠主题相似关闭。
