# AR-VLA 2603.10126v1：必要Source与Ch26窄差额PRE

仅2026-03-13自然日补查；first-public Mar12 BJT与首10独立题摘准入复用，原候选/日期/评分冻结。维持2+2+3=7，不以补审成本重算。必要机制与teacher-forcing/部署反側要求深入。作者只写本日原证/Report，不写Books；以下拟文尚无独立Source/PRE或写锁/POST。

## 实际阅读范围与原件

官方精确v1 [HTML](https://arxiv.org/html/2603.10126v1)原件`SUP_CORE_10126.raw`，TXT只作定位。实际完整读III-A–D方法、IV-A–D四实验段及Tables I–IV，Appendix架构/超参/采集与评价rubric/Limitations，直接对回HTML公式、表与必要Fig6/8 caption；不宣称读无关参考文献或artifact实现。必要两图原件请求记录`SUP_10126_FIG_MANIFEST_RESULT.json`另保留，数字不靠抽象段推断。本包采用以下接口、有限控制对照与反侧，不采用未核执行代码或“精确无损”承诺。

## 方法：实际可支持的机制

III-A Eq2将动作串以过去action/proprio与最近VL条件建模；III-B动作是连续Δpose/关节向量，经linear projection每时间步一token、deterministic head回归下一action。不是把动作改成离散NLL token；“conditional likelihood”类比不证明本文实现了categorical likelihood。

HKV有两个生命周期：action/proprio K/V为逐token滚动FIFO；VL为single-slot整块refreshable prefix，新图处理完成后替换VL块，**并不因此清空过去action history**。III-D控制和感知为独立线程；旧action hidden states可已受此前VL条件影响，不将保留cache等同新观测下全量重算的exactness。

DTR把VL key的RoPE索引设为图像**capture-time** n，把action key索引设为executed-action timestep n，当前query索引m；value不旋转。III-B Eq3–5使位置项依赖m−n，对同一unrotated内容共同移时不改变相对旋转；这不是attention只取决于时间、不是墙钟新鲜度/几何正确性或安全证明。传感时刻与编码完成时刻必须分开，不能把迟到图在publish时重标成fresh。FIFO窗口与VL刷新也不是一个TTL。

Phase1 action-only预训练；Phase2以真实过去和未来动作teacher forcing作跨模态对齐。每个future-token query独立随机遮蔽部分past history，避免仅复制专家history。Appendix generalist过去16、causal train8、test20、mask .6；specialist train20/test30、mask .5。用确定性过去动作训练并不自动暴露部署自产动作分布。论文后段明示OOD动作进入KV会形成反馈回路，随机mask只缓解、不保证恢复。

## 必要评价、预算与反侧

Generalist采用PaliGemma3B＋300M expert（18层、hidden1024/MLP4096），BridgeV2；作者的FAST*为改造成同规模独立expert的reproduction，FM*为Bridge版本π0.5*，不是原发布checkpoint的完全同配方对照。Table I共96 SIMPLER trials，四task平均AR61.5、FAST*49.0、FM*51.0，block20.8与FAST*持平、eggplant95.8与FM*持平，SpatialVLA eggplant100；不能宣告每任务最优。Table II PushT DP65.20/.957胜AR60.40/.920，ALOHA human insertion ACT20.00胜AR12.67；有限跨任务收益不授普遍优势。

Table IV是本拟文的决定性部署反侧：mask0 validation error2.7比mask.6的4.2更低，闭环SR却0对61.5；mask1的2.9/SR28.1也不最优。故监督误差不能代替自产history闭环回归，.6仅作者有限配置。FIFO history1/5/10/20/40对应36.5/50.0/59.4/61.5/**59.4**，40反退，不采用文字所称单调提升。Static positional SR3.1/noPos29.2与DTR61.5支持此模型的时间锚差额，不证明全部替代位置机制数学错误。Phase1去除同时间37.5、双时间54.2 vs61.5，但额外action数据/计算没有完全分账，不能唯一归因HKV。

Table III AR action-forward28.86ms、VLM69.56ms/4、effective total/action46.25ms。两线程隐藏stall不证明真实同卡无竞争或sensor→actuation p95/hard deadline；WidowX实际控制5Hz、每4action刷新VL，没有部署硬件、precision、并发/尾时延。平均jerk7.89/max39.83是有限成功trajectory测量，不授安全或全任务smoothness。不能把29ms模型forward改叫34.6Hz实机闭环。

实机WidowX固定相机到各baseline简单任务3/3成功再做4layout×3trial挑战、200步/40s timeout。Appendix C给逐task milestones .25/.5/.75/1，取trial达到最高stage；主文称89%“success”的量不能直接采用为binary全任务成功率。PushT2有240 human trajectories；Stack3有16 teleop demonstrations及partial-stage评分。成对当前视觉相似的构造支持为何要保留history，但不采用无误memory或物理安全。

Phase1 action-only20k steps/batch1024、约2h单A6000；Phase2 30k/batch512、AdamW LR5e−5，generalist BF16；specialist200k/batch8、FP32。Appendix“冻结VLM backbone”与后续aux FAST训练/knowledge insulation表述有层级歧义，采用的是action loss梯度隔离而不是已核所有VLM参数永久冻结。完整数据人口、训练总硬件/成本、deployment precision与repeated seeds/CI：未披露或不完整。Action预训、VL对齐、masking、cache存储/刷新、两线程同步和closed-loop回归均应计费。

## 实际owner比较与窄差额

唯一owner `MULTIMODAL-EMBODIED-VLA` / Ch26。实际完整顺读当前Ch26 832–910（contact feedback→streaming→fast/slow→chunk time contract），特别HKV现有相邻论点：Reflex分instruction/observation-FIFO/flow-suffix并承认固定输入exactness不覆盖异步；fast/slow已有observation/episode/refresh身份、训练staleness、缓存不是永久真值；SaiVLA段是训练HB缓存与runtime刷新分账。另读536–618状态/latentmemory，TempoFit是历史pre-RoPE K/V检索再注入当前K/V，不是本文action自回归FIFO与VL单slot刷新。没有本文两类状态分别更新、capture-time anchor以及teacher-forced低误差/自产history闭环崩坏的具体桥。

差额不是再写异步或KV优势：是**刷新语义block不抹去动作因果历史，而图像key时间锚仍保留采集时刻；闭环须独立验证自产history分布**。适合现fast/slow小节SaiVLA段之后、Action Chunk标题之前追加两段。现章节的episode/instruction失效与controller授权规则继续有效；新段不取消它们。开始拟文前已完整加载ROADMAP/ProjectContext/LearningPhilosophy/WritingGuide与当前相关checkpoint。此PRE尚待非作者直接核原件与actual owner，不可提前计Books。

## 拟逐字PRE（两段＋本人来源注，待许可）

> 动作自回归还可以给两个缓存状态不同的更新边界：连续action/proprio每步形成一个token，K/V在有限FIFO中滚动；视觉语言条件只占一个可替换block，新帧编码完成时替换该block，而不因一次视觉刷新抹去动作历史。为避免迟到图像在发布时被误当新鲜状态，可把视觉key的位置锚设为图像采集时的action-step，动作key保留实际执行step，当前query读取两者的相对年龄；RoPE只提供这一相对时间编码，不证明场景仍有效或缓存等同fresh全量重算。Episode、instruction、标定与policy失配仍按前述身份规则重建，controller继续拥有动作提交权。<!-- source-family:SF-2026-ARXIV-2603-10126 -->
>
> 保留自产action history也扩大了错误反馈环：teacher forcing下更低的动作误差，不保证运行时出错后的KV仍可用于控制。[AR-VLA的有限对照](https://arxiv.org/html/2603.10126v1)中，不遮蔽history的验证误差更低却闭环失败，延长FIFO也不单调提高任务成功；随机遮蔽只能缓解对示教history的依赖，不签发OOD恢复。Action预训练、跨模态对齐、缓存/刷新与线程同步、真实闭环回归都要计费，单次action forward时延不能替代sensor→actuation deadline，也不能把阶段进度分数叫完整成功率。动作history偏离、旧视觉超出训练支持或刷新迟到时，应缩短历史/重新观察、回退同步短horizon policy与已验证低层controller，而不是用相对年龄或低离线误差批准物理执行。

建议本人末注仅记录exact-v1方法/必要TablesI–IV/App接口和上述限定、最终校准分数与深入、Source/PRE/实际writer/POST身份，不复制实验数字为新benchmark，不影响相邻其他来源。未有lock、writer、POST或DAY。

## 必要图像与独核后补记

实际视觉直接核200图6/8：图6纵轴task complete rate，主文89与partial-stage rubric不能改读binary；图8 PushT2 AR66.7 vsDP44，Stack3 H4 43.8低于FM56.3，H40 81.2较高。这是不同task人口，与SIMPLER H40反退并存，不能合成普遍history单调。上述具体数值仅保留本包，拟Books不采用。

独立reviewer直接核方法/表/App、两图及现Ch26后，两段Source/PRE通过；精确owner已校正。其建议新增命题评分2+2+2=6，不借成熟RoPE或teacherforcing mismatch抬Durability3，必要深入不减少。初拟7仍保留为过程快照，最终待root裁定；尚无作者Books写入或POST/DAY。
