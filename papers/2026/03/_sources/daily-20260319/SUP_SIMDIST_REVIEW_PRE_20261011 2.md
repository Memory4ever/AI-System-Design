# SimDist 2603.15759：必要原证、唯一 owner 与最小 PRE（待 root 独立裁决）

准备者 resume_review17_18；本次仅03-19补03-18自然日。root具名授权准备本 packet，不写 Books、Report、LS、索引或脚本，不stage/commit/push。准备者不能自行授 Source/PRE PASS、actualPOST 或 DAY；本文件是待复核提案，不是完成收据。

## 1. 身份、投入与实际阅读范围

[Simulation Distillation exact-v1 HTML](https://arxiv.org/html/2603.15759v1)，Jacob Levy 等九作者；复用本日已独立校准的准入/公开日夹证，Submitted 03/16不是first public。SUP_LATER_ADMISSION原评分2+2+3=7不因处置变化调整。当前[官方 abs](https://arxiv.org/abs/2603.15759)显示May12 v2/RSS2026，无本次已见具体撤回/勘误信号；只作轻量状态检查，不展开新版、会史或代码。

本人实际独读v1完整题摘、III–IV/Eqs1–3/Algorithm1、V-A–E/TableI、VI限制及A/Algorithm2、B/TablesII–III、C/TablesIV–IX、D/TableX的必要方法、实施配置与直接反侧。只采用图4–7文字说明与正文明确数字，不冒图内全部曲线、逐点/视觉验证、代码或实验复现。初次过宽的Books关键词输出被截断，未用该输出认证覆盖；随后实际完整局部顺读如下§4。

## 2. 可支持的机制与不可外推的桥

III/Eq1、IV-A/Eq2/A/Alg2：模拟器提供privileged状态，PPO expert及中间checkpoints与连续短窗action噪声共同产生成功、失败与恢复人口。各访问状态的reward来自模拟器，value target来自expert critic；只有未加噪expert动作参加BC。不是所有扰动动作都克隆，也不是证明PPO critic为真实或新域最优价值。Eq2联合latent预测、reward、value及受限BC，不据其T/T+1记号补造精确执行recipe。

IV-B/Eq3/Alg1：真实域保留编码器E、历史编码C、reward R、value V与base policy π，只更新latent dynamics f；以同一冻结E产生未来观测target，短窗预测误差监督更新后，由MPPI重新采样/排序候选并闭环再采集。baseline SimDist没有部署value bootstrapping，但仍消费预付的模拟价值；SimDist+BC另外更新π的示教变体不能混作“所有实验均只f”。冻结target保住latent坐标，不证明其仍充分感知新域或目标/价值序仍有效，更不证明新动力学下Vsim等于Vreal。只有任务评价与感知语义仍适用、主要差异在可辨识局部动力学时，这个更新面分责才有条件成立。

IV-C：仅最新exteroception配proprio/action历史，causal action-conditioned chunk一次forward及sequence reward/value heads服务大批候选，不是取消历史、因果mask或将生成latent认证为物理状态。采样仍要调用模型多批/多solver iterations；50Hz设定不是尾延迟、最坏deadline或controller安全证明。以上拟稿只保职责分工，不补全未读图结构/全部实现。

## 3. 关键评价、反侧与完整费用

V-A/B及B/C：UR5e两装配任务，3×224RGB+关节、64latent、H=T=5/5Hz；100k模拟trajectories，约36%在附录实为optimal动作比例，不能当完整expert轨迹占比。每任务20teleop示教，baseline SimDist无示教变体与+BC区分；每20episode更新f，model-free每episode更新，RLPD/IQL使用sparse reward且MLP无action chunk，SGFT虽转sim value也不是全架构/预算matched。不能把全部差额唯一归因于冻结或world-model更新。

Go2两terrain任务，height-map+proprio、12joint targets、H=T=25、RTX4090M laptop/50Hz。主文“100M trajectories”与C的4096×25000约100M data points不同，采用附录transition口径；55.7%是未扰动expert动作。专家训练490M simulation steps，数据生成约7h、world-model预训练约28h/单RTX4500Ada，不能把15–30min采集headline当全部训练或实际适应墙钟。C明确Foam32.1min、Slope35.7min真实数据；不照录“所有任务15–30min”。两epoch/b512/约369k梯度步与训练Adam披露不替真实finetune完整optimizer/updates/seed预算。

V/Fig4 caption与C/TableIX：装配success每点20trials；quadruped每speed5trials×3speeds=15，不是15独立training runs。Slope最终14/15、Foam15/15仅受测人口；Foam慢速pretrained已3/5，不能概称零样本全失败。Foam RLPD因训练中destabilize未报告，不填为0也不据此证明SimDist安全。实际MPPI manipulation250+100 policy candidates/3iterations，quadruped450+22/8iterations；完整前后processing、控制反馈、重复/精度、library版本、concurrency及最坏SLO仍未齐。

V-D仅同初态两条teleop轨迹的value曲线和一条held-out slip轨迹latent loss .076→.019，不认证所有候选的return calibration、latent充分性、跨任务value或真实可达性。V-E/TableI/D是模拟消融：同量expert-only明显较差、MLP R/V较差支持分布/接口分支；reconstruction却使quadruped22.78→23.34更好，50%data22.73近全量，保留反侧，不宣告重建或缩数据一概失败。1080固定模拟参数组合每个仅一episode不是训练seed/实机泛化，latent loss改善与真实成功仍须分别验收。VI明确single-task/high-fidelity simulator，不能外推新目标、多任务/开放域。真实示教、采集/重置、全部expert训练、混合数据/渲染、模型训练/更新、MPPI搜索和独立控制验收都计费；无复现、无普遍因果、样本/墙钟/物理安全保证。

## 4. 实际 owner 与具体差额

sole owner拟 `MULTIMODAL-WORLD-MODELS`，Ch25。本人完整实际读181–209（typed action→ego factorization→agent/background模块→共享encoder漂移→Goal开头）、370–441（预测/梯度更新→uncertainty/rollout→continual组件诊断/replay→persistent状态）、602–671（state authority→latent cost/query closure→scene memory）；Ch24首22行/Ch26首22行和998–1074相关控制权交接实际读。Ch26负责action schema/controller/安全提交，不另写第二份更新机制。

Ch25现191–205已承载已知ego与residual分责、agent/background dynamics module复用和冻结expert仍受共享encoder漂移影响；420–428承载actor与transition/reward/value逐组件遗忘/回放。不完整承载“同任务sim预付E/C/R/V/baseπ→真实只f监督短窗→固定评价head重新MPPI”的更新责任及不能把sim value当新域真值。它不是一般模块冻结或actor遗忘NC。提案为最小两段，放现205 shared-encoder反侧之后、207 Goal/Planner Cost标题之前；前后latent语义→更新面→goal/cost分责连续。保留既有单体、replay、真实controller退路，不创建结构候选。

## 5. 最小逐字 PRE（仅提案，未写/未授锁）

root 非准备者独核：exact-v1完整题摘、III–IV/Eqs1–3/Algorithm1、V/TableI与VI、A/Algorithm2、B和C必要配置/反侧已实际读取；A未扰动expert动作BC、C 100M data points/490M expert steps、32.1/35.7min实机数据、Foam预训3/5与RLPD不报告均保留，未授全部图内曲线、代码或复现。实际Ch25 181–216、410–433、608–636及既有任务/表示漂移交接，确认现有冻结模块/逐组件遗忘不具体承载sim预付评价head后真实只f监督更新再MPPI。2+2+3=7、sole MULTIMODAL-WORLD-MODELS及下列原两段/静态注通过，根节点仅own此窄写；作者或准备者不得因此自行授actualPOST或DAY。

同一任务从模拟器转向真实环境时，有限交互也可先改变更新面，而不把表示、评价与策略一起重学：在模拟器中混合专家、中间策略和连续短窗的动作扰动，以特权状态提供reward和expert value监督；只有未扰动专家动作参与行为克隆。真实域固定observation与history编码器、reward/value heads和base policy，仅用真实观测编码出的未来latent监督更新dynamics，再由MPPI按候选预测奖励与终端价值重新规划。这样把长程任务评价预付给模拟训练，把在线参数更新限于短窗预测；它不是无需模拟价值，也不把低预测损失直接当成物理行动成功。<!-- source-family:SF-2026-ARXIV-2603-15759 -->

这条分支要求冻结的感知与任务评价仍适用：latent坐标不漂移不等于新域状态已被充分观察，模拟器的expert value也不自动成为改变动力学后的真实价值。[受限装配与四足对照](https://arxiv.org/html/2603.15759v1)只覆盖单任务、高保真模拟器及有限实机采集；对照同时改变奖励、动作表示与更新频率，重建目标还有任务反益，不能授普遍稳定改善或全部预算优势。专家/混合数据预训、真实采集/重置、动力学更新、候选搜索与控制反馈均付费，声明控制频率不证明最坏deadline或安全。感知、目标评价或预测支持失配时，应重新校准相应组件并保留单体/真实数据适配、短horizon反馈与可信controller；只更新dynamics是条件分支，不是所有sim-to-real任务的默认保证。

### 拟静态来源注

- `SF-2026-ARXIV-2603-15759` — Daily `2026-03-19`补03/18自然日；[exact-v1](https://arxiv.org/html/2603.15759v1) III–V/Eqs1–3/Alg1/TableI、VI及A–D直接配置/反侧。2+2+3=7；仅采用冻结E/C/R/V/baseπ、真实监督更新f再规划的受限更新面分责。sim价值/表示迁移前提、同预算非同架构、单任务/有限实机与重建反益、全部预训/采集/搜索成本保留；未核代码、实验复现、最坏控制deadline或物理安全。

## 6. 待独立裁决的精确事项

请root作为nonpreparer核必要原证、上述actualowner差额及逐字两段/静态注；采用范围不含sim价值普遍不变/最优、无限off-policy泛化、所有系统只需短horizon ID、stable monotonic/no-safety-event或实时成本保证。尚无Source/PRE PASS，未授写锁/未写/无actualPOST，不计safe或DAY。若该条件化职责链不获支持，保留7分与原反侧，按具体NC或中心暂缓重新裁决，不能因为审阅投入或现章主题相似排除/降分。

## 7. 实际写后局部复核（覆盖§6的历史待办状态）

root已作为非准备者完成必要Source/actualowner/原两段PRE独立通过（§5），并获窄范围实际写入。resume_review17_18为本packet准备者但不是Books写入者，恢复后本19实际重新加载适用合同/ROADMAP/每日来源/README/STOP及本日独核，复用本人必要原证与root有效独核，不重复全文。

本人实际非writer完整顺读当前Ch25 191–225：ego/residual与模块复用→共享encoder漂移/MetaWorld反侧→新207/209两段→Goal/Planner Cost及typed transition交接；另完整1733–1741源注邻接，自身15759静态注为1741，非其他family的1739。正文两段及自身注逐字回对§5原PRE/静态注一致，冻结E/C/R/V/baseπ与真实只f监督再MPPI、sim value/latent充分性迁移前提、重建任务反益、全部训练/采集/候选搜索/反馈成本和短horizon/controller退路均未丢失，未增加普遍性能、物理真值、最坏deadline或安全保证。scoped Books diff定位本family仅两段及自身静态注，既有/并发其他family改动不作本项复核；本章限定diff-check无输出。一次实际完整局部/自身及邻注actualPOST正式通过，root可释放Ch25该family窄锁并由报告作者正常归并实际整合；不改Books注身份、不写Report/LS、不授本日DAY。
