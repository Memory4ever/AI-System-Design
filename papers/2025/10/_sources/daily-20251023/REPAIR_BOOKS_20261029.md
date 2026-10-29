# 本日实际 Books 比较

仅记录实际读到的正文论证，不以主题标签或论文名充覆盖。尚在拟稿的精确差额仍普通工作；唯一reader的PRE/actualPOST另见本日canonical。未改State/索引。

## 已有覆盖与仅报告：writer实际比较

| 家族 | 实际owner与正文位置 | 覆盖的具体采用论点与本次边界 |
| --- | --- | --- |
| 18821 SSP | TRAIN-DATA / Ch27 `可验证数据也要保持 Policy-relative Sweet Spot`、`Verifier-backed Synthetic Curriculum 需要双重权威` | 已分开来源/可执行规格、当前solver成功/方差、可解性与难度及独立verifier；局部重建/判别任务不认证开放现实正确。RAG资格过滤与LLMjudge正是这些合同的局部实例，不将teacher或文档一致变成唯一gold。 |
| 18544 SLICE | INFER-SCHEDULING / Ch56 `SLO-aware Admission`与`Iteration Scheduling` | 实际已有累计输出期限不等逐token间隔、TTFT/进度包络与TBT分开，以及quota/debt不承诺wall-clock等待。SLICE的一秒周期mask不能授硬TPOT；不增加一份算法recipe。 |
| 18525 SPEQ | INFER-TENSORRT-LLM / Ch49在线变精度父表示段、投机FPGA dataflow段 | 已分开同父bit表示/各档位kernel与质量、全部decode/control费用，并把target acceptance交Ch48。SPEQ具体浮点转换只报告局部硬件方案，BF16近似/同KV未闭不新增exactness。 |
| 18480 DLM | MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 `Parallel Progress 与 Active Compute 是两条独立成本轴` | sole reader R16已实际核两连续段：低QPS token并行与高QPS跨request参数摊销、总K与质量运行点/真实roofline分账。有效层复用，不改书。 |
| 18003 BadScientist | PLATFORM-EVALUATION-SYSTEM / Ch66 `Self-report、Behavior Probe 与 Deployment Outcome 是三种证据`，Ch81诊断与计算guard段为交接 | 已明确自述/真实决策/外部effect分离，正确诊断未必限制下一计算。review concern与accept score冲突只局部新证据，不授所有reviewer失败或AI生成即造假，不再改书。 |
| 18477 LAFA | AGENT-WORKFLOW / Ch81状态机语义的Plan-execute优化段 | 已有结果cache、dependency-aware executor优化只读/调度，不能跳precondition/effect或用依赖误判批准并发。LAFA跨subquery复用不新增隐私executor机制；DP/encryption在backend，20query/operation count不认证语义或privacy，不改书。 |
| 18798 WebSeer | TRAIN-GRPO / Ch33 ChatR1参照改写/终奖段 | 已明确训练可见human/teacher改写参照不取得线上真实意图/faithfulness权限，额外工具与judge成本须全计。WebSeer用gold反馈反思是这项训练特权分责的局部验证，不当部署自证。 |
| 18476 SToM | AGENT-MULTI-AGENT / Ch82 `Behavioral belief 不等于 authenticated identity` | 已把有限history的partner行为预测与身份/外部规则分开，latent或标签不证明真实多种意图；SToM有限hypothesis entropy不是心智校准，不为新名称重写。 |
| 18032 OptAgent | AGENT-MULTI-AGENT / Ch82动态topology修复段、peer evidence-ledger段 | 已允许改边/插critic/串行副作用，拓扑按process failure而非更密图，保审计非truth、版本/迁移/回退与全部budget。OptAgent verbal feedback/乘性edge update不授参数RL或全局最优，不增加重复机制。 |
| 18825 Graph mask | MODEL-SELF-ATTENTION / Ch14 `稀疏连接可以跨层补全可达性，但不能免费替代内容路由`及block-skip统计/执行段 | 已明确最终可达不等单层内容路由/数值等价，密度与硬件shape/selection成本不直接授加速。virtual节点/局部mask的受限图实例不新增普遍LLM机制；严格理论条件不搬给任意softmax。 |
| 18148 Attention Rules | WORLDVIEW-REPRESENTATION / Ch5信息可读与因果使用段、局部规则诊断段 | 已把可读feature、规则/SAE局部解释与真实activation干预/留出行为分开。top激活vs随机零值的规则F1不授全层faithfulness；正文/附录样本口径冲突只保限制，不改书。 |
| 18315 Sorting | WORLDVIEW-REPRESENTATION / Ch5逐层cosine/CKA/probe与任务表现段 | 已分开表征几何、指定读出器能力与实际行为，probe/几何更好不认证真实使用或能力同比提高。475个小排序模型提供局部反证，softmax前QK不改名注意概率，不新增世界状态主张。 |
| 18135 World-in-World | MULTIMODAL-WORLD-MODELS / Ch25 `Imagined rollout`、`Open-loop imagination vs closed-loop correction` | 实际已有候选model内部reward/risk并会被planner利用漏洞、执行首项后真实observe重规划；更高视频质量不是控制/接触效用。不同viewpoint接口与训练预算仅报告局部，非统一物理simulator。 |
| 18313 OmniNWM | MULTIMODAL-WORLD-MODELS / Ch25 `从 RGB Rollout 到 Projective 4D Predictive State`及`Imagined rollout` | 已明确appearance/depth等联合分支误差相关、自己预测给自己评分不是独立物理真值，learned reward/想象成功无提交权限；不为panorama/occupancy换场景重复。 |
| 18795 ProCLIP | MULTIMODAL-REPRESENTATION / Ch23连续图文encoder兼容目标段、`对齐不是把向量拉近这么简单` | 已有旧CLIP软关系teacher/各scale职责、新目标适配后逐分类/检索consumer验收，冻结producer也不冻结consumer坐标。两阶段LLM embedding/EMA方案是局部替代，62.5vs74.5不能说无损保留；不新增普适recipe。 |
| 18165 Saber | MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 `用跨步分布不稳定性分配 Revision Budget` | 已按相邻step分布变化提出重开、区分永久lock及可撤销状态、保阈值/oscillation/cache失效和全费。Saber adaptive confidence/回退是受限代理实例，不由至少remask1批准终止。 |
| 18457 VFM-VAE | MULTIMODAL-REPRESENTATION / Ch23连续codec为生成器提供可学习邻域的PAE段、连续表示三consumer段 | 已有冻结视觉prior补细节、压latent、扰动decoded一致性只proxy，重构/语义/下游生成共同验收；干净CKNNA不能预测所有生成不是新三门原则。teacher变更和多loss仅报告，不为新codec名改书。 |
| 18744 Diffusion Buffer | MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 recurrent-depth wavefront段、统一成本模型 | 已明确多个暂定latent交错推进、每轮前进不等每对象只一次计算，前位晚改会级联、活跃驻留和总求值计费。本次音频延迟/质量取舍是局部证据，未采用未读BC-UNet细节，不称首次buffer机制。 |
| 18716 SSD | INFER-KV-CACHE / Ch45跨层dense/sparse角色段、head-aware复用段、KVCompose段 | 已实际区分head角色/原位置/每head预算和索引刷新，global/local只是校准分布配置而非未来有效性证明；layout规则不授identity/质量。SSD图像head实测是局部新验证，不把CFG-MSE相关当语义因果。 |
| 18353 Diffusion-DRO | MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 `生成后训练：轨迹概率、反馈与信用分配` | 已有expert/current-policy在线discriminator、trajectory/local surrogate非真实terminal objective、proxy reward不消hacking、两模型/online负例全费。具体参数化局部取舍不改变已承载的概率/反馈权限，不重复改书。 |
| 18725 SemiLoRA | TRAIN-LORA / Ch30输入相关adapter库检索段、MCIT/ProtoAda原型路由段 | 已实际分开伪domain/prototype与实际adapter选择、encoder/统计人口/目标协议及行为验收，冻结centroid也不冻结竞争。句级伪标/centroid替分类器是局部验证；general/news全域baseline更强，不新增“域越细越好”。 |
| 18291 GeoDiff | MULTIMODAL-WORLD-MODELS / Ch25几何生成后修订RGB-DN段、`从 RGB Rollout 到 Projective 4D Predictive State` | 已明确光流/深度/法线一致性与原几何距离只内部proxy、非真实米制观测，consumer与几何/相机须分验。已知pose photometric可更好而AbsRel更差支撑这条分责，不给生成深度真实尺度保证。 |
| 18113 Dark Patterns | PLATFORM-EVALUATION-SYSTEM / Ch66 `Response Rate、条件质量与无条件质量不能互相替代`、Agent安全harness可解性段 | 已明确不行动/原样返回可虚高safety而未交任务，固定分母/实际response、真实goal与副作用分验。EF early-exit/interaction paralysis是局部实证，不用低DPSR授防御。 |
| 18491 Crucible | 仅报告；相关已读Ch66 `Observed Capability 与 Elicitation Ceiling 必须分开` | potential由固定probe、normalization、权重、搜索器与预算产生，不是算法内在标量；现有正文已分自然分数、可诱发最好行为、监督识别上限及适配开销。逻辑+Bayes用于ABR/调度的有限实现不建立独立普适可调性量尺，不为场景流程再改书。 |

## 子命题争议精确隔离

18638 LSA：2+1+2=5，R14合法重参数化/可达性与优化区别可保；Ch14线性ICL/TD构造已明确全局minimum存在不证训练可达。中心NP-hard归约结构未保留的争议单列，不进Books正面定理，重开需作者合法结构归约。

18680多teacher MI：2+1+2=5，Gaussian conditional NLL工程代理可保；Ch29表示MSE/真实行为不同、Visual Information Gain/CIG并不自动是真实互信息已有具体正文。连续entropy Bayes bound的缩放反例未解，中心普遍保证暂缓，不让已读工程域消失，也不将普通Books比较伪成外部H。

## 需具体新增稿的差额（普通进行中）

AdCo已经R15→W7→R18实际整合。Batch A三项TokenCake/CAD/R2BC完整PRE已交。

后续拟稿仅实际差额：APT（pixel熵quadtree先于encoder的变长patch与dense grid回映）；Hydra（member轴与head轴/共享MLP的不同合同）；LRP（守恒、函数等价不变性和指定干预三义务不同的算术反例）；CovMatch（跨模态cross-covariance与各边缘feature约束不互代）；MENTOR（teacher工具集合而非完整trace、答案/执行三奖励的权限）；ICD（当前answer与跨request异步teacher/demo pool写入）；LDDM（连续latent/token双channel联合或先latent后token采样）；PlannedDiffusion（AR语义计划与异步隔离span/同步cache）；MoT-VLA（冻结generalist与domain expert经mask交互、运动hidden而非逐token文字成为动作条件）。均未默认已整合，实际完整PRE/必要反侧和owner/邻接仍按日内依次落实，不占全章。
