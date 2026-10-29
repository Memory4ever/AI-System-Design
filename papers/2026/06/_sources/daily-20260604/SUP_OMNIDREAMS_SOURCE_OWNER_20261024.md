# OmniDreams 03159 必要Source / actualowner / 最小两段PRE

作者supp_20260604_author。R45完整exact-v1题摘/准入/Jun03联合日证/当前notice层复用，不第三；当前v3仅资源comments不自判实质修订。正式拟2+2+2=6：状态化sensor-generation的chunk时钟与policy/显式simulator交接跨模型/环境控制接口，属于可复用机制；不按NVIDIA/实时标题/WAM参数加分。因具体长期gap深入所采用域，待首次独核正式评分。

[exact-v1 HTML](https://arxiv.org/html/2606.03159v1) HTMLfirst；[剥标保mathannotation完整TEXT](2606.03159v1.fulltext.txt)实际fetch exit0、123175字元原输出另保存末换行，不含tooltruncation。必要实际读§2.2/3.1/4.2–4.3/5.1–5.3/6完整/9.4完整。支持与直接反侧足即停；未读全部数据量/各perceptualscore、§7完整WAM、§8fixer、图像像素/代码或复现，不采WAM胜出/onefifth参数或完整训练recipe，不扩附件。

## 必要支持及关键反侧

§2.2地图是预构建city-level HDmap，动态object检测跟踪10FPS插值30FPS，按相机内外参投影到world-scenario条件；驾驶动作进入ego/actor轨迹。它不是模型自行发现真实物理state；检测/标定/插值错误和map支持均进入生成条件。text主要控制环境外观，不改几何不等所有生成确实遵守；Qwen2.5VLcaption本身不是额外事实传感器。

§3.1首RGB作为cleanlatent，text经Cosmostextencoder/crossattention，结构地图/agent轨迹经小MLP controltokens与visualtokens合入causalbackbone，memorycache存自产历史。协议准确说是给定显式simulator状态/轨迹后生成sensor，不夸所有动态状态均由worldmodel独立推进。§4.2 diffusionforcing先在RDS无worldcontrol转causal、后RDS-HQ-1M加control；causalmask/Flexattention和每帧独立noisetime支撑按过去条件生成，非物理因果证书。§4.3 selfrollout两步[1000,450]、只随机step反传且前帧KVdetach、fixedwindow限制，DMD learnedfakescore/frozenrealscore是分布训练代理；声称eliminatecompoundingerrors强于实际，原文承认仍shiftingartifact并以更长teacher续训。58K高质难视频蒸馏、teacher/score与rollout费用不因两步取消；不采用其复杂度口号为任意历史质量上界。

§5.1 localwindow SV6latent24RGB、MV8latent32RGB，staticshape/preallocatedKV、首次lazyCUDAgraph、后续复用；KVupdate另线程不是零费用/不需完成可见性。LightVAE/LightTAE或MVpixelshuffle改变codec/条件成本，shape依赖graph不能任意重用。§5.2 view→time→spatial轴分别影响attention，16GPU4cam按V4T4HW1，不把单帧FPS当任意multicam资源。§5.3 GB300/704×1280/twostep，SV8RGBchunk/MV16RGBchunk；Tabletotal**排除**KVupdate因异步，effectiveFPS=chunkframes/totaltime，每camera口径，不是完整gRPC/所有simulator/policy/排队/维护/首chunk开销之deadline。precision、全部run并发/seedCI及端到端SLO未披露；不补数字或声称已测实机。本PRE只保有限条件和全部费用，不采用FPS倍率。

§6核心：rank0 gRPC接受renderrequest，经NCCL通知其余ranks，gather后JPEG返回；将服务与policy/traffic/physics分开无需统一rankruntime。RDMA或gRPC只协调+NCCLbulk是future，不能称已无JPEG损耗/网络开销。session以首frame/map/新ID绑定preallocatedKV、renderer/graph状态，后续只传newtrajectory/prompt，避免把autoregressive视频当无状态任意帧render。并发rollout需区分ID/顺序；原文没有完整failure/retry/lease protocol，不由session命名授隔离与故障恢复保证。

§6.4 MV16/SV8帧chunk对应VAE压缩；ego/actor每帧pose须请求前已知，中途改trajectory会使整chunk失效。postfetch可让policy/traffic在新视觉缺失时先走整chunk，之后视频在逻辑过去，要求能处理滞后图像与时间重排；这是考虑的另一策略，非本文AlpaSim实际选项。实际prefetch在chunk边界先policy/traffic多步预测/controller/physics轨迹层接口，commit到下chunk，插值到每frame时间，再按逻辑捕获时刻注入返回帧。原型保序策略不是逐frame即时新policy反馈、真实动作可撤销或所有race已证；必须比较实际控制反馈周期与chunk合同。

§9.4两sensorrenderer swap：AlpaSim/traffic/physics/sceneinitial固定，4policy配置（WAM、Alpamayo1.5四/二/一camera）不是完全不同独立backbone人口。NuRec需3DGS、Omni需seed+worldmap，交集501scene并排除WAM训练，20s/533ms重规划；incident仅ego距对应GTtrajectory4m内才count，限制被测风险人口。总体AllIncidents排名保留不证明每个incident类/每条scene一致，也不通过NuRec代理传递为真实世界认证；FVD随offpath更稳定只说明visualdistribution，不证真实物理响应/碰撞安全。文本“faithfulproxyrealworld”须收窄，不采用。作者同时承认generativerenderer比重建renderer更多compute；数据/地图和track/caption、预训练/适配/teacher蒸馏、所有kernel/cache、JPEG/RPC/网络/等待与policy/physics/traffic、重跑/回归均计费。

## actualowner / 完整锚 / 原两段PRE

唯一MULTIMODAL-WORLD-MODELS Ch25。三Bookscontext/ROADMAP已读，actual相关Stateownership、Controlflow完整组和WorldModel/AgentMemory完整下组已实际读；Ch24/26开篇职责已核。现有AR少步、rollinghistory、actioncommit和各owner分责不等于本项**sensorrenderer session绑定、chunk内pose预提交与pre/post-fetch图像时滞/事件时间合同**；不是泛视频更真或又加state术语。旧simulator和现有AR主线保留，实际sourcefamily/title未见已整合，不因相同主题NC；未核完整其他无关章节或全章所有note。

拟只以下Controlflow最后完整短段之后、WorldModel与AgentMemory真H2前两段+本人注；无新授/未写，不预I/DAY。

完整上锚：

关键 commit boundary 发生在 action 执行前。imagined branches 可随时删除；已执行 action 只能补偿，不能 rollback。这个差别把第24章的 token revision 问题提升为真实副作用治理。

拟增两段：

当 world model 被接成闭环的 sensor renderer，控制时钟还必须服从生成器的状态边界，而不只是一次调用返回若干图片。一条[分块仿真接口](https://arxiv.org/html/2606.03159v1#S6)为每条 rollout 建立 session，将首帧、地图与预分配的历史 KV 绑定到同一 ID；后续请求只补轨迹和 prompt，不能任意重排帧或把另一次 rollout 的 cache 接续进来。模型消费 simulator 提供的地图、ego/actor pose 和动作轨迹，再生成对应相机观测；它拥有派生视觉历史，不因此接管显式交通/物理状态或真实环境真值。

视频 chunk 内所有帧的轨迹须在请求开始时已知，因此一种 pre-fetch 合同让 policy、交通和 controller 在 chunk 边界先产生并提交多步轨迹，按帧时刻插值后送入 renderer，再将返回帧按其逻辑捕获时间注入事件流。中途改轨迹会使整段条件失效，不能一边即时重规划、一边继续消费旧 chunk；另一种 post-fetch 路径须让 policy 接受滞后图像，并额外处理时间倒序，不是同一个反馈预算。缩短 chunk 或改用同步高保真 simulator 仍是重要分支。少步生成、静态 KV、异步维护与多 GPU 只减少部分执行费用，不能取消网络/编解码、cache 就绪、排队和控制周期；GB300 的 chunk FPS 也不是闭环 deadline。作者在 501 场景、20 秒、533ms 重规划且 incident 限定距录制轨迹 4m 内的对照中保持策略总体排名，只支持该受限代理；不证明远离录制轨迹的动力学、所有事件排序或真实驾驶安全。地图/时间/动作支持、session 连续性或全链费用不合格时，保留原 observation、显式 simulator 和短 horizon 反馈，不让生成画面提交物理事实。<!-- source-family:SF-2026-ARXIV-2606-03159 -->

完整下锚（真H2与完整首段）：

## World Model 与 Agent Memory 的边界

Agent Memory 保存任务历史、事实、偏好、策略经验或 artifact provenance；World Model 估计环境如何随 action 演化。二者都需要检索和更新，但 correctness 不同：

本人trueH2注拟：

- `SF-2026-ARXIV-2606-03159`：Daily2026-06-04补Jun03；exact-v1 §2.2/3.1/4.2–4.3/5.1–5.3/6/9.4必要，2+2+2=6具体sensor-renderer session/chunk边界差额深入。保simulator提供状态/模型仅派生观察、pre/post-fetch不同反馈预算、cache时序/全费与501场景20s/533ms/4m近录制轨迹人口，排名非真实世界/安全保证；少步/GB300 FPS非全链deadline。未核图像像素/代码、全部WAM/fixer或复现；待首次Source/正式评分/actualowner/PRE与新授，不预I/DAY。

