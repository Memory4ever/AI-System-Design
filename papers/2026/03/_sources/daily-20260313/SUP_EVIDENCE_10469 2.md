# 10469 DepthCache：跨帧merge状态、region restore与reinit的Source/PRE

仅补Mar12 BJT自然日，第二包完整exact-v1 AB、独立窄准入与日级arxiv夹证复用。官方 https://arxiv.org/html/2603.10469v1，`SUP_CORE_10469.raw/txt`及manifest/result GET200、197896bytes、UTC2026-10-09T16:01:43.014245。作者实际完整III-A–D/Eq1–4、IV-A–D/TablesI–IV及V直接限制；图只正文/caption不认证pixels/曲线精确点值/实际视频。无代码运行、复现、全外部引用或无关附件。

## 新增命题与实际评分

固定单帧uniform prune/merge会损空间证据或跨帧突变→本文将depth region/protection、跨帧progressive merge、region restore与phase-aware全局reinit组成独立frontend→改变视觉压缩状态如何进入action conditioning并在新几何变化时恢复。这不是Kmeans/ToMe/near-field常识本身。拟`2+2+2=6`：重要压缩-恢复接口2、当前sensor与跨帧压缩/action-chunk门的边界2、可复用两级失效/预算资格2。真实Ch26状态/控制gap已比较，必要深入完成；拟两段整合，待非作者Source/PRE与root窄写，不提前formal/POST/DAY。

## 实际方法与尚未认证的实现边界

III-B1 N5 warmup保持standardforward，跨heads/Nframes聚合cross-attention，以mean+std选semantic P_att；depth梯度阈值选P_edge，union P。P只init/reinit更新，不是每帧新目标真值；attention不是calibrated task-importance概率。

III-B2只对unprotected patches按depth Kmeans K3，mean-depth线性映射rmin→rmax，protected r0。无保证近物一定重要/远物无信息；dmax=dmin退化分母与空protection集合处理未披露。III-B3各region cosine bipartite greedy配对，top相似pairs按W5窗口逐步达到targetmerge count，size-weighted averaging不等下游Transformer/action semantics无损或无偏；pair topology“relatively stable”不是严格frame correspondence，也不能据方法名把旧tokenfeatures/KV永久缓存。Eq2只写min(t−t0,W)，reset后time/size/pairs需共同绑定，当前不补唯一artifact实现。

两层失效分开：patch sliding depth变化超过eps的nonstatic比例>gamma→**该region恢复full tokens**，再收敛后从头merge；III-B4 **只在gripper没有carry object**时看旧P_att平均depth与init差>δreinit→重新warmup、刷新P、重partition、重启progressive merge。carry判定来源/阈值与actual反馈未详，不能称depth触发穷尽动态目标变化；同depth平面移动/appearance变化可能漏（审阅者推断），但另region restore仍存在，不能把全局reinit门误说成全部局部恢复都关闭。

III-C辅助wrist view两state：从**predicted action chunk**的gripper aperture稳定+end-effector显著运动进入Merge；开闭transition且低motion进入FullView。这是预测趋势门，不是当前机器人已真实抓住物体的测量、无延迟证明或权限。未写intermediate组合/fallback/实际grasp-detector的完整确定机，不能自行补造。III-D512双camera tokens→约300steady是受限配置，不代表所有模型或全episode固定ratio。

## 对照、预算、直接反侧

IV-A LIBERO4 suites/40tasks×100episodes，π0.5 3.3B(SigLIP/Gemma/Flow)、OpenVLA7B(SigLIP+DINO/Llama2 AR)、GR00T2.2B(Eagle/DiT)，HF checkpoints且均LIBERO finetuned，没有exactrevision/精度/完整finetuning预算。单RTX4090 24GB；latency定义image observation→action output的wallclock episode平均，非sensor acquisition→actuator/尾延迟SLO。N5/K3/W5与caption rmax.7/eta.2已具体，不补edge/eps/gamma/δ/rmin数值；depth获取/warmup/attention/聚类/配对/restore/I/O/动作解码费用应一同验收，不从lower tokens推净所有component费用。

TableI原OpenVLA平均76.7→75.7（**−1.0pp**），π0.5 97.9→97.6、GR00T93.1→92.9；因此“all less1%”不能按严格小于照录，前者正是1.0pp四舍五入。speedup1.21/1.28/1.07，retained78.9/68.2/87.5%跨模型不同，局部任务有正/负。SP-VLA由原publication引用且动态ratio，不是本作者matching全部实现；ToSA和FastV质量/ratio/实现路径不同，不授同ρ同budget所有pruning都劣。没有seed/repeat/CI、完整walltime分解，不授显著/因果独占。

实机PIPER6DoF/twoRealSenseD435直接stereo depth，π0.5，三core各20trial：20/20→20/20、18/20→17/20、17/20→15/20，合55/60→52/60；191→143ms仅所定义平均infer。15trial sorting15/15→13/15、time28.6→22.1；人为推cube2–3cm recovery11/15→12/15、17.4→13.7。各表time成功/失败人口未细说明、不是固定时限throughput/精确同成功率速度收益，不能把小样本comparable签安全或无需回归。

TableIV去depth partition Avg97.6→79.4、去progressive→81、去dualprotect→90.3/speed1.48且ρ55.6、去reinit→92.8/ρ72.5、去aux→97.8（**更高**）/speed1.06/ρ88。多个对照也改变ρ，支持受测完整接口质量/资源取舍，不是所有模块安全/必要因果证明。Fig5只正文/caption，.3–.7 localplateau与default.7不授全模型safezone或已知最优；预测action gate不会消灭实际反馈滞后。

V明示不加速action decode/Flow denoising，Amdahl上界与3架构/单臂适用范围保留。depth误差/无纹理/薄结构/透明反光、相机变化与同depth目标变化可破保护或触发（工程推断，非稿内已实测所有failure）；空间压缩更不保碰撞或grasp稳定。可回退fulltokens、关闭aux merging、重新观察/缩短chunk、经验证controller。

## actual唯一owner与差额

唯一 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。此前本日10340已实际读的47–115真实观察/表示/几何handoff与536–558state/freshness有效复用；本项实际770–818从placement/quantization全预算到language/metaaction压缩、端到端deadline/async proposal完整局部。现动作/语义缓存说明boundedstaleness，但不承载本稿**protection/topology/window→region restore与conditioned global reinit**以及predictedchunk wrist compression对象；CGVD初始raw图补景又与token aggregation不同。原sensor/controller职责沿用，不计为本稿自带新安全机制。Ch23通用表征compression只handoff，Ch45KVcache不是本item merge状态owner，不另开多章节。

拟在Ch26 `Quantization、Placement 与 Frequency` 两段及2602.13052 marker**之后**、`从语言推理到One-step Meta-action`标题**之前**两段，使视觉frontend压缩先接共同控制预算再转语言/action压缩，不打断fast/slow/AR-VLA新旧缓存链。仅请求root两段窄锁，作者不写Books。

### 逐字PRE（非作者校正后root已窄写）

视觉 token 压缩也可带有跨帧状态，而不是每一帧独立按同一比例删减。一条受限分支在 warmup 中分别积累任务 attention 和 depth edges，把 union 作为 protection，其余 patches 按 depth region 分配 merge 比例；配对与目标压缩量在若干帧内逐步生效，让当前 action conditioning 逐渐转入压缩视图。Depth 这里是运行时压缩的外部结构 prior，不要求原 policy 新学一条深度输入通路；近场或高 attention 仍不自动等于全部真实任务证据，聚合均值也不保下游动作语义无损。

恢复需要区分两个层级：局部 depth 变化使 region 回到 full tokens，重新收敛后再逐步合并；旧 semantic protection 中各 patch 相对初始化 depth 的变化绝对值之均值，则在未搬运物体的条件下触发全局 warmup、保护集合刷新和重新分区。辅助 wrist view 从预测 action chunk 的夹爪与运动趋势选择压缩或 full view，只管理感知预算，不证明实际抓持、消除反馈滞后或授执行权限。[DepthCache 的有限4090/双RGBD对照](https://arxiv.org/html/2603.10469v1)支持这种速度—质量分支，但实机core成功55/60降至52/60、sorting也有成功退步；推理平均耗时不等完整控制deadline。Depth、camera、instruction、protection、merge topology/window和reset应与当前观察绑定，warmup、深度、配对/恢复及原action解码都计费；深度失准、同depth变化漏触发、压缩质量或时限失配时，应恢复full tokens、关闭辅助压缩并重观测/缩短chunk，保留原policy与独立controller，不让保护分数或预测动作签发物理安全。<!-- source-family:SF-2026-ARXIV-2603-10469 -->

## 精确停点

Source/actual owner/校正PRE已通过，root已窄写Ch26两段及本人末注；下列实际非writer POST通过，待root仅同步本人末注并放锁后formal。强unbiased/task-token全保、安全plateau、temporal lag消除及普遍同质量吞吐不采用。不是整日报完成，不因无实现运行转为外部材料受阻。

## 实际非writer POST（mar13_supplement）

直接顺读当前Ch26 760–838完整局部，从domain-gap交接、placement/frequency预算两原段与2602.13052 marker，经过新784/786两段，到One-step Meta-action、固定控制频率、完整deadline/异步prefix与continuation相邻链；本人2129末注完整实读，不仅核proposal/diff。回对本日精确v1 III-B的region restore、III-B4/Eq4、III-C预测action-chunk两态门与IV-C TablesII–III全部必要行；其余已通过III-A–D/IV-A–D/V必要Source与actual owner/PRE独核有效复用。

新正文明确Eq4为旧P_att每个patch相对初始化depth变化的绝对值之均值，不是abs(mean depth difference)；region full-token恢复、仅未搬运时global reinit与predicted wrist gate没有混并，也没有把预测aperture当实际抓持反馈。正文保留core55/60→52/60与sorting15/15→13/15负侧，平均infer非完整deadline，保护/merge非语义无损、全部frontend/decoder费用与原policy/controller退路均近文；没有采用temporal lag消除或物理安全。前后原placement与language/meta-action推理链完整，本人末注正确限必要Source/适用边界、未授复现/代码/DAY。实际非writer POST通过；作者没有写Books，root只需同步本人末注PASS/释放窄锁，随后本日formal6分深入整合。
## root末注同步与正式状态

root已同步本人Review note为实际非writer POST通过并释放本两段窄锁；作者直接回读当前Ch26对应完整末注确认。Source/校正PRE/actual窄写/非writer POST层均通过，Report正式同步受限整合，不授日报DAY；不重复已核原件，也不写共享Books。
