# Oct23 Daily — SOURCE_WORLD2

仅 Oct22 BJT；本批四个已准入家族 29329 PAL / 30125 PhysiCalWorld / 30136 AW-0 / 29088 CausalWM。已重读当前 AGENTS、Research/Report 合同、Prompt、每日来源/arXiv恢复与ROADMAP，State仅本日路由；不扩发现/其他日期。原完整题摘/正式分/官方New-Cross日期关联复用ARXIV有效层：PAL2+1+2=5，PhysiCalWorld2+1+2=5，AW-02+2+2=6，CausalWM3+1+2=6（设计反证受影响深入）。本作者只准备必要Source/actualowner/具体NC或精确PRE，org非作者独核，root唯一Books/Report/State writer；未写未POST，不授DAY。

四份exact-v1 HTML文字原件已保存为source-world2-2610.{ID}.txt，缓存不等已读，以下逐篇记录实际必要域。

## W1 — 2610.29329 PAL；2+1+2=5；Ch26 小 gap

日期/身份复用：exact-v1，Oct22 cs.RO New[28]，无本窗受影响版本cue。必要原件：[HTML文字](source-world2-2610.29329.txt)，[exact-v1](https://arxiv.org/html/2610.29329v1)。实际读 §4.1–4.3、§5.1–5.3/关键表、§6限制、B.1/B.2、C.2监督来源与D.1真实数据处理；未核实现/复现，不遍完整任务视频/示例。

旧约束→增量→选择：历史检索每次临执行再推subtask易丢短暂线索；PAL把已出现的未来相关证据提前写成顺序subtask_list，与短visualbuffer和eventlist分开，再由当前VLM选择条目交低层VLA。所谓executable是自然语言子任务可被低层消费，不是已执行代码、分支程序或真实effect收据。

必要证据与直接反侧：
- §4.2新event/subtask/currenttask三输出；信息不足允许空更新。新subtask非空则清旧event，任一新memoryupdate清visualbuffer，否则累积后固定frame下采样。这些清理会失去证据，不能把压缩当无损/永久事实；subtask_list顺序append明确不支持conditionalbranch（§6）。
- Stage1按teacher稀疏边界的中点扩展空/非空标签，**启发式timing不是实际证据充分性oracle**。Stage2在训练observations上滚动自身memory状态，不是另采机器人自由控制轨迹：非coordinate文本必须exactmatchreference，coordinate<10pixels，重复/错误各自置空，迟至banddeadline仍缺则整rollout失败。通过者才自标注；失败fallback原监督/部分task始终原标签，不能叫无外部监督、真实任务成功自验证或全状态分布已匹配。
- 模拟annotation含simulator oracle event与taskrules，真机label由gripper/静止粗界+GPT5.6Sol视频细标、去stationary并将action重写指向nextretainedobservation；部署不提供oraclegate。UpdateGate消融却使用环境groundtruth80%slot，不能把其结果当可部署低费替代。stage1Only过写、sparse漏写，两阶段改善仅该训练标签人口；所有消融同hierarchymemory，未单独控制每个representation的唯一因果。
- RoboMME16tasks groupmean56.05 vsFrame44.51，但只4/16逐task最高；same low-level MemER VLA，不代表high-level训练/全部预算对齐。FrankaResearch3真机4tasks各10episodes×3repeats，PAL60.83/MemER45.00/Frame28.33，VideoUnmask同100，不授全任务普胜或安全/长程deadline。
- Qwen3VL4B+LoRA33M，frozenvision/aligner；8A800、bf16、ZeRO2，stage1约8.9h、模拟stage2约5.5h（178855rows），realcyclic15blocks约.7h且参考label仍参与。relabel/verifier/重复非空/upweight、VLM查询、memory和真实控制/回归全费；没有完整控制端到端latency/并发tail SLO，不用更小context签加速。

actualowner：完整读Ch26 episode-memory定义/历史control审计/readgate，以及predictive write-before-loss二完整段+RePlanMem二完整段、hierarchicalsubgoal两段。现有keyframe提前保留和write/read/control分责充分；小差额是将瞬态证据**提前转为未来子任务**而非仅存图、写入时机与内容监督分开，同时清理旧memory的失败边界。Ch77通用记忆不另复制机器人控制机制。

精确位：Ch26 SF-2606-20092 marker后、SF-2610-22556 surprise写门首段前。直接前完整正文：
> 预测性写入减少关键证据丢失，却引入阈值误判、annotation dependence、有限容量和错误记忆累积；写得过多会退化为 dense history，写得过少仍会漏掉因果线索。短 horizon 或写入信号未校准时，固定窗口、周期采样或人工定义 milestone 仍更可控。论文证据不提供物理安全保证，memory 不确定、时间戳冲突或 observation identity 不一致时，controller 必须刷新观测、降级或交还人工。

逐字 PRE：
> 瞬态证据还可以在消失前先转成未来子任务，而不只保存供日后检索的图像：让流式视觉与事件状态提出顺序 subtask list，执行时再选当前条目交给低层策略。列表可被消费不等动作已执行，也不是能表达任意条件分支的程序；新条目后清旧事件或视觉 buffer，还可能提前丢掉后来仍需的证据。[PAL 的受限分支](https://arxiv.org/html/2610.29329v1#S4)同时监督写入内容与近似时机，再在自身生成的 memory 状态上用参考标签将错误、重复更新置空，缺失必需更新而超时的轨迹则不用于自标注；这是带特权标签的训练修正，不是部署真值或完整机器人状态分布已对齐。标注、反复自标注/训练、每次视觉推理和实际控制验收均计费，较短 context 不证明完整实时收益。未来条件、列表或时机失准时保原观察、固定里程碑/窗口及重新规划，仍由独立 controller 决定真实动作，不让已写计划代替完成证据。

直接后完整正文：
> 写入信号不一定来自另一个语义标注器，也可以利用policy对同一未来的修订：上个chunk已执行H步后，将其剩余K−H动作与新观察下pre-write chunk的前K−H动作对齐，再把动作差、方向/夹爪变化及visual feature差按task历史校准成surprise percentile。统计只用本query之前的数据、部署时冻结；它提示“值得重看”，不证明发生了语义事件，预测错误也会产生峰值。Event与write仍分开：从此前小窗口和FIFO内容中聚类，仅选未被memory代表的新簇，可能零写入或一次多写；mask只用于比较，不能改写存给policy的原始图像。

org 非作者必要Source/actualowner/PRE已通过；W1近似联合target/错误重复置空/缺必需更新超时整轨迹不自标注的修词已同步本PRE。root实际保存后，org已实际顺读完整新增、直接完整两侧和本人末注，非writer POST通过；作者仅行政同步有效消息，不重审或授DAY。

## W2 — 2610.30125 PhysiCalWorld；2+1+2=5；Ch25 小 gap

身份/日证有效层复用：exact-v1；Oct22 cs.RO New[68]、cs.AI Cross[210]、cs.CV Cross[138]。必要原件：[HTML文字](source-world2-2610.30125.txt)、[exact-v1](https://arxiv.org/html/2610.30125v1)。实际读§3.1–3.3/Eq4–7、§4全部主实验/表1–3/4.3 OOD与§5限制，A.2 context encoder及主干配置、A.3全部训练/推理伪码、A.4 CEM直接消费；未核实现/复现，不遍其余图片与附录。

旧约束→增量→选择：同外观不能辨质量/阻尼，单体短history会把不同scene dynamics平均化；从**同动力学组另一episode**采action–observation prompt，以未来latent预测共同训练context encoder，压成一份scene descriptor，在固定动力学下跨候选/rollout复用。不要求物理数值标签，但仍要求准确的same-physics grouping、探索和训练，不是从任意视频零成本辨识真实参数。

证据及反侧：
- §3.1 descriptor是learned-query池化的附加条件；A.2 DINO分支广播到spatial/temporal位置后作channel拼接，LeWM与每步192维latent拼接，不是增加attention序列token；A.2固定12frame→64维，视觉keypoint与动作联合编码后4层8head transformer；主干DINO-WM/LeWM均K=3，不照录为通用最优recipe。训练预测与prompt从samegroup不同episode抽取，防止prompt直接携带target future；teacherforce causal predictor，context与predictor共同梯度。无physics labels≠无数据结构监督。
- Test先在当前scene采随机/任务无关交互，**须有揭示动力学的接触或运动**；descriptor先算一次，后跨CEM候选复用。CEM以final-latent到goal MSE评分、在环境执行整段计划，latent距离低不证明真实可达/碰撞安全；交互本身可能有副作用，部署探索授权是项目工程约束，不是论文提供安全保证。
- 四模拟环境135train配置/15test配置，每配置5episode，共75；planning同75。对照LongHistory/ContextPrefix/label-trained EstimatedPhysics/GT-inference PrivilegedPhysics应分开，最后者不是同信息预算baseline或数学上界。描述无标签不代表胜过有特权：Reacher SR61.3低于Estimated69.3，BeerPong SR80低于ContextPrefix82.7，FetchSlide SR56低于Estimated69.3；视觉指标与planning不互代。稀疏碰撞线索会让全rawprefix保留更多可消费信息。
- OOD只Reacher第一joint damping超训练范围、另一joint固定，指标openloop视觉；不能授任意物理因素组合或实机OOD。PushT descriptor余弦随CoM相关不证明唯一恢复真实参数。
- §5明确samephysics分组野外难、prompt信息质量依赖、**episode内stationary**；physics改变须新取证/失效旧descriptor，不由可cache签永久有效。采集、编码、joint训练、全部候选rollout/CEM与真实动作验收均计费；单token较便宜不证明包含探索的端到端实时/SLO。

actualowner：Ch25“把已知自运动…因子化”完整段链与QWM静态spec条件两完整段已读；Ch26跨trial绳索context两侧已读。既有已知spec/解析ego不拥有**未知且固定scene动力学由独立interaction clip压缩成可复用predictor条件**这条接口；Ch26 policy历史不复制，唯一Ch25小gap。
精确位：Ch25完整QWM反侧段后、OccSim“静态occupancy…”完整段前。直接前完整正文：
> 显式条件化增加规格解析、归一、异质采样和 reward-scale状态，并把训练支持域变成迁移边界。[QWM的必要对照](https://arxiv.org/html/2604.08780v1)将同一形态向量提供给 model-free policy，支持 learned dynamics的受限迁移分支；但 held-out Go1/ANYmal-D 的插值成功与重型 B2 的失败同时存在，不能说任意本体零适配或 universal physics。作者选定两本体的实机运行不授物理安全、唯一因果或无模型失配。规格错误、未知接触/负载或训练域外时，应重校准并恢复本体专用模型、可信 simulator/解析残差路径与短 horizon真实反馈；单本体、规格缺失或隐式辨识已足够时，原 monolithic dynamics 仍合理，动作提交继续由第26章 controller验收。

逐字 PRE：
> 物性未知但在同一场景中固定时，还可以先用有接触或运动的交互片段取证，把动作—观察响应压成一份 descriptor，作为未来 predictor 的附加条件；同动力学组中不同 episode 的 prompt 与预测目标共同训练，避免提示直接泄露该目标的未来。[PhysiCalWorld 的受限对照](https://arxiv.org/html/2610.30125v1#S3)无需物理数值标签，却仍依赖正确分组、有信息的探索和 stationary dynamics；learned token 不是唯一物理参数或已验世界真值。固定条件下可跨 rollout 与候选规划复用，但稀疏碰撞时完整 raw context 仍可能更好，较准画面也不保证较高规划成功。采集、编码、联合训练与全部候选/真实验收均计费，不由单 token 签完整实时收益；场景物性改变、提示无信息或真实反馈失配时，应失效旧 descriptor、重新取证并保留显式标定、较完整 history 或可信 simulator，真实动作仍由独立 controller 验收。

直接后完整正文：
> 静态occupancy的观察生成还可把这条分解落实成补全问题：在已知、受限的平面ego motion下，先将上一时刻latent刚体传播到下一坐标系，再用几何可见性与训练期随机遮蔽形成不完整条件，由生成器补全下一latent；waypoint也须在同一目标坐标系对齐，不能让简单复制冒充长期变化预测。这里学习的是warp与可见条件下的静态场景补全，不是一般交通动力学；latent旋转与插值不保证无损，分布相似也不证明同一个未见场景身份一直被保存。[OccSim的有限对照](https://arxiv.org/html/2603.28887v1)仅在给定静态AE空间、平面运动与训练人口中支持该接口，随机mask、token条件与辅助loss共同变化，不能独归一个组件；动态layout仍由另一路生成和规则运动驱动。AE、warp、补全训练/采样与长rollout校验都付费，条件旋转失配、遮挡历史不足或质量回归时，保留真实重观测、显式静态地图或已验simulator，缩短horizon，而非由长期FID批准物理行动。

org 非作者必要Source/actualowner/原PRE已通过；A.2 descriptor是channel拼接而非新增序列token的作者bullet已同步。root实际保存后，org已实际顺读完整新增、直接完整两侧和本人末注，非writer POST通过；作者仅行政同步有效消息，不重审或授DAY。

## W3 — 2610.30136 AW-0；2+2+2=6；Ch26 小 gap

身份/日证有效层复用：exact-v1，Oct22 cs.RO New[69]。原件：[HTML文字](source-world2-2610.30136.txt)、[exact-v1](https://arxiv.org/html/2610.30136v1)。实际读§2.1–2.4全部/Eq1–6、§3.1–3.3主要对照/表1–4、A模型/训练/计时全部、F.1/F.2具体代码错误、H全部失败说明、I全部混合执行伪码、J直接比较范围/渠道人口、K程序标签静态检查/skill准入关键条件、L全部限制；未遍图像/所有task与库定义，未核实现/复现。

旧约束→增量→选择：外层代码planner与内部WAM分离会串行等待；AW-0把masked code/video/action各自expert以code→video→action的blockcausal attention接进同一去噪。默认code只是subtask条件，**不执行**；另可让同次生成的code通过gate后占用本阶段，否则用direct chunk。已有语言联合生成不等这份结构化程序的两种消费责任。

必要证据/直接反侧：
- 模态内双向、模态间单向；不是三路对称“相互修正”。Code用独立吸收mask、video/action独立连续噪声；code canvas128、4step confidence揭示，video额外mixture采样/截断batch归一权重，不称准确importance无偏目标或generative-law等价。训练memory旧标注slice按概率换自产slice，episode reset，不能叫完整执行事实。
- 自动标注先每task抽episode、Gemini+Claude协调抽库，再冻结50skills（23YAM/27human）重标缓存；语法/API/参数/词汇检查不执行。2913.2h数据仍有human单view复制三slot，未获得三独立观测；joint48H100、taskposttrain100demo等全部费，same downstreamdemo不等所有预训/compute匹配。
- 真机8task×3trainingseeds×16rollout/task报rubric score71.1不是binary全成功71.1。Joint比AR均值71.1/54.5但ReplaceLightbulb75<79.2；RTX5090完整inference包含视觉/联合去噪/video decode/actionpostprocess .23 vs .55s，却比nocode .19s更慢；不授传感器—执行器deadline/tail或物理安全。
- RoboTwin50task×50rollout clean/random default80.8/20.6，hybrid63.1/29.2；hybrid另用CaP采demonstrations，与default不同trainingpipeline，故不能全归仲裁或code执行。有效性gate不估code相对action的优势，clean退步重要；realhybrid只YAM towel一task90.6 vs84.4，不授dexterous/全部task。
- I完整alg：stage/dependency/compile/whitelist/nonvacuous及失败重复gate；code attempted就discard同轮action，即使exception也等下一轮fresh观察再plan，不能把旧chunk接续当安全rollback。**无exception即把stage记done**并不验证物理postcondition；F语法parse87.5%/helpercalls29.2%、参数extraentries/注释换行可使合适skill仍不可执行，H几何碰撞/滑脱/接触丢失直接说明有效syntax非成功。
- L明确不从自身互动在线学习，安全/任意skill发现与持续自改进均非本稿已验证。标注、库/接口、三expert训练/驻留、所有候选推理、感知/primitive执行与真实回归全费。

actualowner：Ch26现World-action model完整joint接口/UniW(A)M路由两段、SUAVE、UniWALM两完整段与hierarchical subgoal责任已实际读。联合语言规划、memory/fresh/control边界已有；唯一差额是**同程序既作内部video/action条件、又可选择交外部primitive消费**，必须不同验收，尤其attempted不等成功/noexception不等物理done。不向Ch78复制通用工具事务。
精确位：Ch26完整UniWALM反侧段及其marker后、“显式 rollout 保留…”完整段前。直接前完整正文：
> 有限同 subset 消融支持语言共训的边际作用，主结果却还改变 FMC、LoRA 或 anchor；memory 消融的30K与100K训练不能直接相减归因，episode置信区间也非训练重复。更关键的反例是文字计数已到目标、完成 channel 晚一步，实际仍多按一次：summary 正确、memory 更新与物理完成须分别验收。语言 expert、文字/anchor 驻留与更新、联合训练及动作采样都付费，少了独立 planner 不等免费或高频 deadline 已满足；控制时钟、summary 或动作失配时，保留外部可追溯记录/独立完成检查、短 chunk/direct policy 与真实重观测，不让可读意图或 done 预测替 controller 提交动作。

逐字 PRE：
> 同一结构化程序还可以有两种消费者：在 code→video→action 的条件路径中与未来和动作共同去噪，默认只给动作模型提供 subtask；另在重规划点经阶段、依赖、语法与 primitive 白名单检查，才尝试交给外部技能执行。[AW-0 的受限分支](https://arxiv.org/html/2610.30136v1#S2)由此把内部计划与代码执行分开，联合生成不证明二者语义或物理后果等价。原混合算法尝试代码后即丢弃同轮动作，异常须新观测再规划；无异常就记录阶段完成也不是独立物理 postcondition。有效语法不估计它是否优于被替换动作，模拟混合配置的分布外改善同时伴干净场景退步，且另改示教采集；真机混合仅一项 YAM 任务，不推广任意手型。程序标注/技能库、三路训练与推理、感知及 primitive 执行都计费，局部完整模型计时不签控制 deadline。代码参数、接触或优势无法验收时，保留不执行代码的 direct chunk、fresh 观察与独立 controller/停止接管，不以生成计划或未抛异常批准真实完成。

直接后完整正文：
> 显式 rollout 保留可观察的中间未来，适合人审和诊断，却把多步 video denoising 放进 action critical path；joint generation 允许 future state 与 action 共同建模，但两条生成路径的误差会相互耦合。Direct-policy 分支直接产生 action，延迟更低，却容易在移除未来画面时把 predictive dynamics 一并丢掉。中间路线是在训练期用真实 future observation 或 frozen dynamics teacher 塑造 latent state，在部署时只做一次 current-observation / stochastic-future prefill，把 layer-wise KV 与 compact dynamics registers 暴露给 action denoiser，而不 materialize future video。

org 非作者必要Source/actualowner/原逐字PRE已通过，无修词；root已具名通知实际保存，org actualPOST队列中，未预签。

## W4 — 2610.29088 Causal World Models under Physical Parameter Shifts；3+1+2=6；Ch25 具体设计反证

身份/日证复用：exact-v1，Oct22 cs.LG New[53]、cs.RO Cross[73]。原件：[HTML文字](source-world2-2610.29088.txt)、[exact-v1](https://arxiv.org/html/2610.29088v1)。实际读§2、§4.1–4.4/Eq1–12全部、§5.1–5.6全部主设置/表1–5/指标定义、§6限制、A组件来源全表及B.1/B.2基线/评价协议；B2末任务表仅必要主文结论不采全部子项，未核实现/复现。具体OOD输入伤害/结构机理深入，不为“causal”名义授高分。

旧约束→增量→选择：删除shortcut输入与使用真实但窗外的物理参数是两个设计问题。固定同finger-local routing下，mass进入普通MLP/recurrent可伤害外推；显式mass-affine惯性/bias加knownPD路径才把已知mass转为稳定正面输入效用。故“把已知spec送入模型”须另与相同family无mass/训练均值mass比较，不只比绝对预测分。

必要机理/反侧：
- Synthetic pairedintervention按output归一响应阈值估mask后冻结，与dense/random等edgecount/oracle共享architecture/loss；OODRMSE1.769→.697 vsrandom1.604/oracle.694只支持该shortcut合成环境，不授机器人学得因果图。Robot是**人工fingerlocal路由**，3指独立parameters/共有objectcontext，objectMLP不直接读mass；依赖结构所有三mechanism固定。
- Eq5/6惯性由state-dependent PSD项按非负mass系数加和+正definite floor，bias亦massaffine；这能保非负mass下矩阵正定，不证明与真实惯性/能量/Coriolis一致。加速度因求逆非mass-affine。torque和contactresidual不直接读mass；learnedtorque有学习scale，knownPD用真实simulatorcontroller/physical units及固定训练scale，二者是整体配置变化，不能把跨family差额唯一归为PD。独立bias/inertia的energy-consistency和匹配torque对照是futurework，非已证。
- CausalWorld pushing/picking×5seed，trainlight归一区间[0,.4]与OODheavy[.6,1]，两者仍在平台spaceA；12mass中9可变。每150步250Hz仅.6s，100step共享forecast .4s且RWM另读32history；不授长期闭环/未知mass辨识/真实迁移。
- Same varying-mass轨迹，actual/fixedmean PD初始化/minibatch匹配、同候选grid各自IDvalidation选；fixedmass不等环境真的固定。150step表3 knownPD实际mass .727 vs均值输入 .609；10/10run改善但two task per seed共享流，不独立20人群，signp仅indicative。learnedtorque .734/.733几无massbenefit，MLP实际-.803 vs无mass .721、只在已拟合model替testmass为mean则.717，分别是重训控制与推理诊断，不能混为同一操作。
- 100step表4 learnedtorque actual .755/fixed .768，strongRWM无mass .752，差额小，不说PD/causal模型全面最优；knownPD .746<no-massRWM .752却massbenefit +.071。RWM实际mass 8-step训练horizon -.648、50horizon -.540 vs各无mass .718/.752，故可用参数并非自动可用信息。pairgain先逐run再median，不等两个median差或百分比。
- spaceA→B/PETS式ensemble的表5另有50steptransition/筛objectmovement≥5mm/每domain单独动作池/独立intervention额外数据，score用source mean不是表4testmean R2；只是prediction非PETS MPC/control，同信息预算也非全成立，不拿该表拼机器人mass统一涨分。
- 原证据只knownmass/knowncontroller+state与有限两task，decomposition/coefficient/residual/one+multistep训练、仿真/paired controls/全部rollout均费。未评uncertainmass/longdeploy/downstreamcontrol/physicsdeadline，不能用positive definite或mask授真实安全/因果发现。

actualowner：完整读Ch25 factorization 265–273（ego已知传播/风险/QWM spec两段）及本章输入channel/parameter误差consumer两段、multi-intervention共同mechanism两段。已有“不唯一辨识/输入校准/完整费用”不拥有这份**已知真实参数仍可伤害、同family输入效用和绝对精度分验、mask选择不决定外推函数**的反证。只增一段，唯一Ch25，不复制Ch26控制章节。
精确位：Ch25 ego factorization结构先验风险完整段后、“若没有可信的解析传播器…”QWM首段前。不与W2后QWM位冲突。直接前完整正文：
> 这种结构先验增加了传感器、时钟同步、参数识别和 model-mismatch 风险。自运动不可观测或模型误差占主导时，单体学习模型仍可能更合适；安全关键路径也仍需 simulator、规则模型或 hybrid residual 的独立校验。

逐字 PRE：
> 选对依赖输入仍未决定如何外推它：删除不相关 shortcut 可以去掉一条错误路径，但真实质量超出训练范围时不能简单删掉，直接送给 MLP 或 recurrent predictor 也可能显著伤害预测。[有限 link-mass 对照](https://arxiv.org/html/2610.29088v1#S4)固定 finger-local 路由，将质量显式放入惯性与 bias 的仿射系数，并让已知 PD 负责作用路径、残差不直接读质量；同 family 的真实质量与训练均值输入控制显示受限正收益，却不保证最高绝对预测精度，learned-torque 分支的质量效用又近乎消失。因此参数可得、同机制下的输入效用与不同整套配置的精度应分别验收，不能把稀疏图或正定矩阵当外推与能量正确的证明。已知质量、controller、仿真与配对训练/rollout 都有成本，证据仅两任务的短预测而非长期控制；参数不确定、接触或支持域失配时保留无参数/均值输入对照、原完整 predictor 与可信 simulator/短 horizon 真实反馈，不由较好预测批准物理执行。

直接后完整正文：
> 若没有可信的解析传播器，但机器人质量、肢长和关节构型在部署前已知，也不必全靠运动历史把它们重新辨识。一条不同于解析 ego 分解的分支将这些 engineering specifications 编成静态条件，分别进入 observation encoder 和每一步 learned recurrent dynamics；真实 observation 仍更新 posterior，想象 rollout 才使用 prior，policy消费其 latent。这把可预先声明的本体条件与运行中的动态估计分责，不证明隐状态已经统计独立，也不让规格书替代摩擦、执行器背隙或真实传感反馈。跨本体训练的 reward 范围可以逐本体用分位数/EMA归一，但该尺度状态不是不同 reward 语义等价的证书。

非作者必要Source/actualowner/PRE待org；root未保存，未POST。

作者停点：四项必要Source/actualowner/精确完整两侧与PRE均齐，已逐篇交org非作者核；root唯一Books/Report/State写者。本批不扩发现、其他日期或新Source；W4独核/后续实际POST由具名消息续记，不由作者代授DAY。
