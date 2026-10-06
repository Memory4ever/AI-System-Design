# OnFly 2603.10682v1：必要Source/actual owner/最小PRE ready

仅2026-03-12 BJT补充自然日。完整v1题摘/准入有效复用（独核§19）；日级arxiv公开夹证复用§23的42项及SUP_DATE3_10682原字段，不以Submitted当公开。官方v1同五作者、唯一v1，无具名venue/撤回/纠错信号，不扩版本史。

实际原件 https://arxiv.org/html/2603.10682v1 ，SUP_CORE_10682.raw/txt、MANIFEST/RESULT为GET200、187038bytes、UTC2026-10-10T02:31:41.418141。实际读III problem/IV-A全部双actor与memory维护、选择、serialization；IV-B Eq1/refine/gating/local planner、IV-C task queue/D部署；V-A–E完整setup/TablesI–IV/realworld及VI（258–1587）。支持与关键反侧足够；不要求全部照片、视频、代码或复现，不扩成熟FastPlanner/AWQ引用。

## 新增与评分

一个推理流同时给即时目标与长horizon进度，长history更新与两类频率互相阻塞→本稿让目标producer以当前RGB-D/pose和共享ViT feature输出pixel目标，独立低频monitor以first/key/latest记忆输出CONTINUE/STOP/LOST；两者独立KV上下文，STOP消费到task queue，LOST先停后回最后normal heading，semantic/geometry refinement后目标才交local planner。新增是带具体消费方的双状态/缓存更新接口，不把“异步”“KVcache”“ESDF/AWQ”名称或UAV领域指标单独算贡献。

拟 **1+2+2=5**：本地producer/monitor及keyframe序列实现D1，实际monitor→任务推进/恢复与目标→geometry/controller两条消费边界R2，可复用的状态、token顺序与物理验收分账D2。现Ch26快慢缓存论证尚不承载该独立完成监控消费者，受影响差额触发必要深入；不是自动把localplanner或真实飞行称重要机制D2/多层R3。

IV-A目标包包含pixel/depth_t/cached f_t/pose_t，previous3Dgoal经当前pose重投影作为history cue；monitor异步，固定三status。IV-C写stable STOP才推进队列，但稳定确认次数/时钟/旧结果跨subtask作废规则Not Disclosed，不能补造状态授时协议。每分支有独立prompt/memory/KV，sharedViT避免重复视觉编码，不等GPU无竞争或零拷贝实现已核。

Hybrid Memory的pool按translation/rotation候选与feature cosine去重，几何最近L内选重复；固定S路程segment sticky winner，保持上一Q最长有效prefix、追加/补未用pool项，最后按chronological sort，输入[first,Q,latest]。**保留prefix后排序不是逐步最终token-prefix不变证明**：未用较早pool项插入已保留keyframe之间会改变排序前缀；只采用有界keyframe更新分支，cache复用须对最终序列核有效prefix。未查token位置/attention实现、重复frame首尾、缓存命中率或invalidate代码，不授等同全量fresh attention。

IV-B相似mask保原pixel所属connected region，在该region∩depth-clearance可行集合中找最近pixel；depth>Dmax跳过本地refine。交集为空没有定义此处fallback，feature相似也不保错误原pixel具有正确指令语义；投影depth mask dilation不是全世界collision certificate。bearing乘Gaussian缩forward range后回odometry；FastPlanner保持local ESDF与动态限制、yaw penalty。既有controller负责实际动作，没有把finiteclearance与模型标签当环境真值。

## 完整关键评价与反侧

仿真UE4.27十scene/150tasks，object40%/precise40%/long20%；pairedimage Qwen3-VL235B生成指令并人工核。各baseline同Qwen3-VL4B-AWQ、13900K/4090/64GB，TypeFly另YOLOE，stop接口改造保留，不当原baseline未改。速度/加速度.6、yaw.4rad/s，Dmax7m、S4、monitor每2s、sim90×60°720p，thresholdSR5m、episode70s、每episode三次。CR碰撞即终止；SR要最终停对且无碰撞，OSR只需途中到过，FT至完成口径不能替tail/SLO。

T1 SPF→ours SR26.4→67.8/CR42.7→2.7/FT39.2→27.1；T2 SPF+planner→ours SR43.2→67.8，**OSR80.3→78.1反退**，CR4.7→2.7、FT50.2→27.1。T3 noDual SR48.6/FT44.1、noVerify SR63.7/CR3.2、noPlanner SR35.8/CR37.5；其为指定bundle removal，不分sharedencoder/独立KV/prompt/async各因果。time/sliding memory OSR78.4/79.5都高于hybrid78.1，hybrid优SR/FT不能写全指标单调。Qwen2B CR2.6低于4B2.7，30B略高SR但FT29.2长于27.1。没有CI/独立seed/按任务类型失败分布，不外推精确差或通用安全。

T4 OrinNX perstep baseline3.83/7.47s→Edge.81/1.98→Hybrid.81/1.15（decision/monitor），只所测平均分支时延，未披露尾延迟、concurrency、fullsensor→PX4deadline、power；6.50×是monitor对Transformers baseline非新增memory独效，1.98→1.15另看。实机customquadrotor OrinNX16GB/Mid360LiDAR/D435640×480/PX4四任务展示，无全任务trial denominator/near-miss/最坏停止偏差；不把仿真150tasks三次搬到实机。AWQ/FP16ViT、TensorRT/CUDAgraph是已有部署组合，memorypool/geometry/重规划、VLM两分支与planner全部计费。

## actual owner与逐字两段PRE

ROADMAP唯一MULTIMODAL-EMBODIED-VLA Ch26；实际完整Fast-Slow 902–918及前Streaming 881–900、后ActionChunk 919–936邻接已读。现文慢read-only表示供快action expert、episode/instruction/history/generation刷新与controller权限具体已有；AR-VLA另区分动作FIFO与视觉block。未具体承载**独立历史monitor状态消费task progression/LOST恢复、共享视觉但不共享两推理KV、keyframe序列的有效prefix**。不声称已有内容被新稿替代。Ch45只拥有generic cache有效prefix、Ch78通用tool effect，Ch66评价分母，保持本Ch26唯一owner。

拟在AR-VLA两完整段之后、Action Chunk标题前窄增两段（准备者不写Books；待非准备者实际核/协调）：

快慢接口还可以把完成监控与目标生成分开，而不只是缓存慢语义给快 action head。当前观测、depth、pose与共享视觉feature供目标分支提出pixel goal，另一低频分支用first/key/latest轨迹记忆判断CONTINUE、STOP或LOST；两分支保持各自prompt与KV上下文，STOP交任务队列推进，LOST先停再按最后正常heading提出恢复。Keyframe pool去重、分段sticky选择和有限记忆更新减少整段历史重编码，但缓存只能复用最终输入中真正未改变的prefix，不能由“先保留、再按时间排序”推断每步cache永久有效。目标还需在局部相似region内按depth clearance修正、经bearing降速与local planner交controller，监控标签本身不批准physical commit。

[OnFly的有限对照](https://arxiv.org/html/2603.10682v1)将途中到过目标的OSR与正确停止的SR分开；加planner基线与其他记忆分支仍有更高OSR，组合消融不能识别每个cache/监控模块独效。错目标的feature相似、空可行集合或长距离跳过refinement不成为正确语义或安全证据；最终prefix、subtask/status新鲜度与稳定STOP规则仍需运行时验收。Orin上的分支平均时延与四项实机展示不授sensor-to-actuation deadline、零碰撞或普遍开放环境安全；两次推理、编码/缓存维护、geometry与planner全部付费。状态迟到、target失配或控制预算不足时，刷新观测、重建有效cache并保留同步短步、原local controller与人工接管，不让旧monitor或模型恢复提案自行推动物理执行。

准备者到此支持+直接反侧足够即停止，尚无非准备者Source/PRE/实际POST或正式候选计入。没有Books/State/index写、stage/commit/push；Optional artifact未读不称外部受阻。

最新正式终态：root实际必要Source/owner/PRE通过并窄写Ch26两段，本准备者非Books writer实际POST见SUP_POST_10682.md；root实际核回执/正文、本人注节号修正与POST PASS、局部锁释放。1+2+2=5深入完成/整合，本日formal第44项；上文只保准备时提案，非DAY。
