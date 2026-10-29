# DreamPlan 16860：必要证据与离线想象偏好接口

准备者resume_mar17；只本19已准入家族，不扩发现/附件或下一日。启动实际重读AGENTS、研究/Report合同、统一prompt、ROADMAP、Daily/arXiv来源说明及本19README、SUP_SOURCE_STOP与LS路由。分数维持SUP_LATER_ADMISSION的2+2+2=6；核心及直接反侧支持下面拟采用接口，具体差额需深入比较。未授Books锁、未写未POST，不计safe/DAY。

## 身份与必要Source停止

[DreamPlan: Efficient Reinforcement Fine-Tuning of Vision-Language Planners via Video World Models](https://arxiv.org/html/2603.16860v1)，exact-v1。完整题摘复用SUP_AB_16860，当前官方abs header/Comments/history实际核无撤回/勘误信号，只有v1。日级归属沿SUP_LATER_METADATA 1062–1101已有夹证：arxiv.content findable created/registered均UTC03/18；Submitted UTC03/17 17:59是投稿字段，不单独充当公开日；不重建精确发布时间或迁日。

实际必要HTML §III-A–C/Eqs1–5与§IV-A–D/TablesI–III、§V。方法HTML L83–132，评价硬件/执行/人口L141–176及最终对照L177–196；支持和关键反侧已够，只读必要正文，不扩references、project artifacts、代码、全部图像点值/视频、复现或版本diff。

### 模型与行动真实接口

§III-A以当前/目标图分别检测的keypoints作离散抓取/放置候选，没有跨图显式点匹配。§IV-A2由SAM2分割（目标mask离线预标、当前首次人工框初始化后传播）与Farthest Point Sampling给候选，planner另选机械臂；像素点unproject至3D，固定抓取→搬运→释放→归位primitive及插值执行。不是VLM直接学连续低层控制或无需人工/标定。论文实机双Franka FR3、D435i 960×540@30Hz，Cartesian pose control30Hz，局部32GB RTX5090 workstation。

§III-B先执行零样本planner的探索动作取得真实action/outcome，再把机械臂运动渲染成action video，经ControlNet残差条件驱动冻结CogVideoX-5B backbone；生成白背景object-only视频以聚焦变形。Eq2–4明确条件支路与noise loss，生成更像图像仍不是已校准真实动力学。§III-B“several hundred action sequences/~4 hours”与§IV-A2总2056 trajectories粒度关系未解释，不合成同一精确人口或采样效率主张。探索数据次优不等无限动作支持，也不能用想象替代最初实采。

§III-C单次video inference约一分钟，因此先对真实数据的observation/goal pair采样K候选并生成预测outcomes，由GPT-4o比较生成图与目标选best为positive，池内其余为negative；预制偏好后policy update不再生成视频。这是离线想象反馈进入planner参数的接口，非每step在线world-model policy gradient，也非模型本身获得执行权。有限Qwen3-VL8B实验中部署直接planner forward、不再逐候选video/GPT-4o搜索；单次planner输出仍须经过上述primitive与真实观测。Eq5写log-sigmoid的log-likelihood差，没有明确通常ORPO的完整odds/SFT组合与minimize/maximize实现；只采用pair构造/消费分工，不采该式为通用ORPO可执行配方或无偏RL保证。

### 评价、直接反侧与未证明

§IV-A3每任务10次随机初始化trial，**每次一个action primitive**，分值{0,.5,1}含有意义进展；T1的平均score不是纯二元success rate，也不是长序列闭环success/safety。Qwen3-VL8B base三任务.20/.10/.70、adapted .60/.35/.85，均值.33→.60；作者其他大/商业zero-shot对照不匹配训练预算，不由该差额证明单一module因果或普遍physical grounding。没有训练seed/置信区间、judge一致性或模型排序对真实结果的完整校准。

T2同action conditioning、最终object crop区域PSNR24.70→26.25仅支持局部重建目标；full-scene/crop改变预测任务，视觉相似或qualitative像真不授稳定/因果动力学与独立verifier资格。§IV-B1 baselines文本动作vs本方法rendered action，条件接口及专门适配共同变化，不能把全部差额归因ControlNet。

T3 explicit verification N4/N8平均score.48/.50，时间926.32/2605.56s、TFLOPs7.82e4/1.56e5；部署DreamPlan .60/1.12s/15.14。此表比较online候选video+GPT-4o搜索与预先adapted单planner，节省的是**部署决策路径**，不等相同总训练/人工/采集预算，且不认证控制deadline或完整机器人wall-clock。K训练值、完整pair人口、优化超参/训练资源与所有judge/API计费未披露，不由32GB机器叙述补造precision/batch/SLO。world model错误与GPT-4o视觉偏好可共享偏差，池内best也可能全错；没有独立real-ranking验证则不能把chosen叫真实可行/成功。保留初始真实采集/重置、mask/标定/render、基座/条件支路训练、K候选全部生成、judge、pair制造/planner更新及真实行为回归全部费用。

## actual owner 与具体差额

实际Ch25 352–402（重点362–390）顺读：Imagined rollout通用model-bias、RaWMPC 370的风险数据/伪标签proposal但部署仍MPC；VLAW372的真实成功BC＋imagined success与迭代更新；374–376 global forward/local Jacobian分工；378–390目标回写dynamics/分歧synthetic权重等。它们均未承载**探索实采→action-rendered object-only预测→预制候选排序pairs→离线planner更新→部署不再video搜索**这一计算前移接口，因此不是泛主题NC。sole `MULTIMODAL-WORLD-MODELS`，拟Ch25 VLAW372后一段、global forward/local梯度374之前。Ch24入口、Ch26 1–29/995–1038完整control/online-critical dream交接、Ch79入口及Ch34 pair/objective责任相关150–165已实际读；动作执行归Ch26、通用偏好目标归Ch34、抽象计划归Ch79，不复写第二owner。

## 最小逐字PRE（待root非准备者独核/窄锁）

root 非准备者已实际读取 exact-v1 必要 III-A–C/Eqs1–5、IV-A–D/TablesI–III 与直接反侧，并顺读 Ch25 352–391 及已有 RaWMPC/VLAW、前后向分工。SOURCE/PRE PASS：只采用计算前移与 pairs 消费接口，保留单 primitive/部分分值分母、真实探索/控制依赖及全费用，不采 Eq5 为完整 ORPO 配方、物理安全或匹配预算优势。root 已窄写 Ch25 一段及静态源注；正文仅规范中英文空格并将“成功真值”明晰为“真实动作成功标签”，不改变核验命题。actual POST 由非 writer 读取实际正文、完整邻接与自身源注后另行确认；未计 safe/DAY。

昂贵的视频想象也可以前移成离线偏好，而不是驻留每个部署决策。一条[受限变形物体分支](https://arxiv.org/html/2603.16860v1)先执行零样本planner的探索动作，用真实action/outcome训练读取机械臂运动渲染的object-only视频预测器；再从同一观测与目标采样候选动作，生成各自outcome，由外部视觉judge比较目标并选池内优者，冻结为偏好pairs后更新planner，更新时不再生成视频。部署省去的是逐候选video与judge搜索，不是最初实采、训练或完整动作控制；已有mask、像素到三维与固定primitive仍属于执行条件。生成模型与judge可以共同偏离真实结果，池内chosen不是动作成功真值，object-crop PSNR也不证明候选排序已校准。有限实机证据每次只执行一个primitive、平均score包含部分进展，不授长序列闭环安全或普遍收益；部署单forward时间更不等匹配总预算或控制deadline。真实探索与重置、渲染/分割、视频模型、全部候选和judge、pairs与planner训练均计费；真实排序、支持范围或净费用回归时，保留可靠真实动作监督、短想象与显式候选核验，动作仍经独立controller及真实环境反馈，不让离线偏好自签物理grounding。<!-- source-family:SF-2026-ARXIV-2603-16860 -->

静态源注：`SF-2026-ARXIV-2603-16860` — [DreamPlan exact-v1](https://arxiv.org/html/2603.16860v1) §III-A–C/Eqs1–5、§IV-A–D/TablesI–III与§V。仅采用真实探索训练action-video预测、预制想象偏好与部署移除逐候选搜索的有限接口；judge/model共同偏差、单primitive/部分进展分母与全费用近文，未采用Eq5通用ORPO配方、实采人口口径或稳定/安全保证，未核artifact、全部图像点值/视频或复现。

## root窄写后非writer actualPOST（resume_mar17，2026-10-11）

本人实际顺读Ch25 360–386完整Imagined rollout局部（新正文374）及1738–1748自身静态注/相邻WorldDrive、WorldCam、SimDist注，并回对已读必要exact-v1原证与root SOURCE/PRE裁决。新正文除已声明中英文空格规范与“真实动作成功标签”消歧外，与原PRE采用命题一致；VLAW真实/想象样本分工→离线视频排序pairs/部署计算前移→global forward/local Jacobian交接连贯，未混为同一更新接口。探索实采、action-rendered object-only条件、judge与model共同偏差、单primitive/部分进展分母、PSNR非ranking校准、完整费用及独立controller/真实结果边界近文；不授Eq5完整ORPO、真实物理grounding或匹配全预算性能。自身源注范围/未核边界准确且无验收人员身份循环。一次局部actualPOST PASS，可由root接纳并释放该family窄锁；无Books改写、额外Source/附件或本日DAY宣称。
