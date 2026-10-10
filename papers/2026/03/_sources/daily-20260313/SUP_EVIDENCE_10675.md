# Cybo-Waiter 2603.10675v1：最小必要Source/actual Ch26/PRE ready

仅Mar12 BJT补充日；完整v1题摘/准入/日级date有效复用，八作者、唯一v1、无具名venue/撤回/纠错标记；SubmittedMar11T11:41:32Z、SUP_DATE3_10675.raw registeredMar12T02:07:13Z与正常公告下界夹Mar12，不用Updated。

官方 https://arxiv.org/html/2603.10675v1 ，SUP_CORE_10675.raw/txt和MANIFEST/RESULT实际GET200/194640bytes/UTC2026-10-10T02:27:29.161718。实际读III-A/B完整typed schema/所有条件ref grounding、III-C完整Eq4–6/uncertain/VLM辅助、III-D所有失败反馈/timeout/retry/plan更新、III-E执行接口/gait/MPC分责、IV全setup/TablesI–II/V及完整JSON示例（331–1670）。未核代码/所有motion clips/图片或复现，不扩全部references；支持与直接反侧足够即停。

## 新增接口，不借成熟模块加分

原skill contract只给object/geometry并交controller→本稿将每predicate绑定key/grounded args/comparator/value/consecutive stable_frames，分别把precondition readiness与success completion交给geometry supervisor，失败predicate/continuous diagnostics回planner，并以timeout/maxretry决定局部修正或改未完成计划。新增不是SAM3/RGB-D/VLM/JSON/MPC/RL组合名，也不把debounce/feedback原则独立当突破；是可复查的计划条件、连续观测验收和恢复消费接口。

拟 **1+2+2=5**：typed condition/status局部实现D1、实际planner→grounding/supervisor→controller/replanning责任接口R2、条件人口/连续证据与恢复消费分账可复用D2。新gap触发必要受影响深入，已读核心及安全边界；不借人形robot规模抬D2/Reach3。若非准备者判断仅既有配置则只改具体受影响采用命题/评分，不从工作量反推结论。

III-C sat(p,t)=prod last n eval，Ready/Done分别AND不同predicate集；安全/feasibility在执行过程中作为invariant，失败暂停/请求恢复。VLM semantic boolean仅辅助，可靠geometry优先、冲突重新观测/grounding而非直接宣成功。III-D blocked/failed/uncertain触发；maxretry耗尽才请求更新remaining plan，保已完成subtask并更新symbolref。III-E RL lower-body与upper-body MPC分责、precondition不满足转locomotion调整；没有把VLM动作指令当controller事实。

## 必要反侧与费用

连续n帧只压瞬态false positive，不证明n独立观测/传感器新鲜、校准正确、predicate实现涵盖全部collision/contact或物理safety。φ key→具体几何计算/阈值、confidence/uncertain触发、weight/采样频率与unknown处理完整实现Not Disclosed；不能擅补n/时间/成功规则。JSON示例destination为container而SUPPORTED_BY support为table_1（ref未在target/destination同字段定义），n3/n10、timeout30/maxretry2只是该例，不是所有任务默认；可解析监控不认证goal-intent一致或本例已实际运行成功，不用改原示例替作者修协议。

UnitreeG1/Dex3-1/headRGB-D，RTX5080工作站跑SAM3/planner/supervisor，onboard Unitree computer跑lowcontroller；不是全onboard大模型。T1“尽量跟Being-0定义”5task×10，各Fetch9→9/Deliver8→8/Grasp8→10/Placebasket6→9/Coffee6→8；外部Being0预算/实现不匹配不授唯一归因。T2每task10，对照关闭整个supervisor：Tidy5→7/Sort6→8/Drink7→9，是bundled monitor/geometry/recovery差额，不单独识别stable_frames/多对象/重规划每项效应，未披露CI/重复独立seed。JSON谓词窗口n不是该10trial统计分母。

MPC objective/低层约束完整数值、policy训练预算/12clip与sim domainrandomization细节、机器人near-miss/强制接管/最坏偏差、图像频率/obsage/online latency/concurrency/SLO、precision/全部token调用与功耗Not Disclosed。不授碰撞/平衡始终安全、开放任务泛化或所有grounding正确。SAM3多对象、深度反投影/过滤、VLM plan及semantic复核、回看/重seg、RLskill训练、MPC与retry都计费；超时budget不是闭环deadline证书。

## actual owner与逐字最小PRE

ROADMAP唯一MULTIMODAL-EMBODIED-VLA Ch26。实际完整1549–1561的ActionPrecondition authority+SkillSchema geometric contract及Reviewnotes标题邻接，另27–36模型准确率与近失/控制验收已顺读。现文具体有skill先给对象/相对位姿/接触可达/motiontemplate→perception实例化→controller，但未承载predicate集按连续帧分别给Ready/Done、失败实例+diagnostics/uncertain与remaining plan恢复预算的接口。不是简单“robot evaluation”主题差额；Ch78仅泛tool-effect消费，Ch66实验协议handoff，不分双owner。

拟在SkillSchema现有两完整段之后/Reviewnotes之前增两段（待非准备者实际核，未经锁不写）：

几何契约还可以把动作前提与完成条件显式分开：高层计划为每项条件声明 predicate key、对象引用、比较关系、目标值与连续帧窗口；perception 将目标、目的地与条件引用全部落到同一 object-centric workspace，geometry supervisor 再分别计算 Ready 与 Done。一个瞬时条件通过不批准步骤推进，窗口内各帧均满足才交给执行层；失败时返回具体 predicate/grounded arguments 与连续诊断，而不是只让 VLM 给整步一个成功标签。低置信或几何与语义复核冲突时重新观测、grounding；局部修正与完整改计划分别消费 timeout/retry budget，改计划保留已完成步骤并更新对象引用。

[Cybo-Waiter 的有限实机对照](https://arxiv.org/html/2603.10675v1)支持这条监控接口，但关闭整个 supervisor 的组合消融不识别连续窗口、几何或恢复各自的唯一收益；同一错误几何连续通过也不成为真实接触或安全证据。JSON 结构可验证不等于目标语义已闭合，示例目的地与 support 引用、窗口长度和 unknown 规则仍需任务 owner 明确；VLM 辅助不能取代低层约束与真实环境结果。多对象分割、深度与诊断、重观测/重规划、skill/MPC 求值和训练均付费，十次任务成功不授 deadline、near-miss 或全任务安全。对象身份、时序、接触或恢复预算失配时，暂停推进并保留显式 controller/人工接管与可核验的原 skill，不让连续 proxy 帧自行批准 physical commit。

准备者无Books写。本包ready请求root非准备者Source/score/actual owner/PRE裁；如整合仅请求这两段与自身note窄锁，实际非writer POST仍需写后发生。不提前formal或DAY；普通未读motion artifact不外部化。

最新正式终态：root必要Source/评分/actual owner/PRE通过后实际窄写Ch26两段，非writer本准备者actual POST见SUP_POST_10675.md通过；root实际核正文/回执并将本人末注同步PASS、释放局部锁。本日formal第42项，1+2+2=5深入完成/整合，非DAY；上文保留准备时提案不作未完路由。
