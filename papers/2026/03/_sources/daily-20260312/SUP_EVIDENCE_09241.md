# 2603.09241 — RAE-NWM：预测表示与像素解码的闭环分责

作者mar12_model_continue，2026-10-09；实际[exact-v1](https://arxiv.org/html/2603.09241v1) §3–6、Tables1–4/A1–2必要原证。完整题摘/窄准入和日期复用batch3/本日独核；owning arxiv.content/findable registeredMar11UTC02:08:47与公告下界同BJT03-11。currentv2同题摘，无withdraw/具体纠错；未见具名先稿，不比较全部版本/附件/图数/实现。精度、推理batch/并发/生产SLO与训练seed方差本必要披露Not Disclosed；不复现实验。

**2+2+2=6，因具体长期gap深入。** 增量是dense foundation representation中的action-conditioned连续转移与不用pixel re-encode的rollout/规划接口，跨表示—预测—planner边界，不因DINO名称或更小模型计分。Owner **MULTIMODAL-WORLD-MODELS/Ch25**；actual latent dynamics局部与180–238 action/schema交接、597–618 latent cost局部、Ch23/24开篇已读。旧正文虽有latent transition和planning距离非真值，但未承载此fixed encoder/decoder、dense patch空间自反馈/decoder仅显示的具体分工；不在Ch23重复dynamics。

§3 probe frozen各encoder，仅A的1×1biasfree+空间broadcast的action B拟未来latent，训练/测试trajectory分开、Huber，globalR²跨batch/spatial/channel flatten；持久appearance、latent方差与representation scale会影响R²，未matched no-action/identity不认证因果作用或“最适合物理”。不采用图中精确数。

§4冻结DINOv2和RAEdecoder，16²patch×768、context4，CDiT-B12×768及浅宽DDT2×2048；预测flow velocity，action=[ux,uy,yaw]与horizon经Fourier/MLP，t驱动sigmoid gate调action注入。t是flow时间而不是物理预测horizon k；不把gate与kinematic causality合并。每interval新Gaussian、Euler50步，clean predicted tokens进入sliding window，下游CEM直接算DINO goal距离；decoder只作可视化/pixelmetric。学习t-gate不保跨域单调/固定coarse-tofine，更高维不是无压缩原信息。

§5/A：SACSoN/RECON/SCAND训练split union、heldouttrajectory，Habitat MP3D1000轨迹另训；50epochs/batch96/twoA80080GB≈2days。T1直接4/16s预测与图中16s顺序4fps人口分开；T2 CEM每iteration120candidates、各8steps rollout，RECONATE1.36/RPE.37差于NWM1.13/.35，短期texture与长期structure有取舍。HabitatSR78.95优于OneStepWM72.67而SPL63.58低69.10；成功是stop距goal≤1m/mean8mepisode，不授机器人真实安全。表文Table4/实际Table3错引不移数。T4gate对照SACSoNATE/RPE支持本条件；removeDDT反退说明representation/backbone共同变化，350M vs1B也非matched。DINOmetric共享训练表征不是独立物理几何真值，LPIPS/FID不证明action consequence；真实因果/碰撞未测不授。

全部dense encoder/token驻留、widehead、多interval50ODE×CEM120候选、轨迹评分、训练/调参及必要decode成本付费，较小backbone不等完整更快。高频texture受损、长rollout与wrongaction仍需观测纠正。当前无必要external，剩普通独核/落稿待办。

## 逐字 PRE

拟在Ch25「Latent dynamics」中基础式与收益说明后、下一分支前插入一段，原latent/interface论证不动：

> Latent rollout 还要决定是否每步经过像素解码再编码。一个受限导航分支冻结视觉 foundation encoder 与配对 decoder，在 dense patch 表示中学习 action 和 horizon 条件下的连续转移，并让预测 token 直接成为下一步的历史；decoder 只负责显示和像素评价，planner 直接消费预测表示与 goal 表示的距离。预测网络中的生成时间与物理 horizon 是两个条件，前者可调节 action 注入强度，却不证明后者的物理后果。[有限导航对照](https://arxiv.org/html/2603.09241v1)支持这项接口分工，但较高线性 probe 分数或同 encoder 的距离不认证因果动力学、可达性或安全；高频纹理与短期轨迹仍可退步，仿真成功率提高也伴路径效率反退。Dense 状态、宽预测 head、多步求解与多候选规划均付费；表示、action 标定或规划成本失配时，应保留原 VAE dynamics、真实观测刷新与已验收 simulator，而不是从较小 backbone 推出免费或无损预测。<!-- source-family:SF-2026-ARXIV-2603-09241 -->

末注拟为：`SF-2026-ARXIV-2603-09241` — Daily `2026-03-12`补查；[RAE-NWM exact-v1](https://arxiv.org/html/2603.09241v1) §3–6/Tables1–4/A1–2。2+2+2=6，dense latent rollout/decoder/planner分责gap深入；不采probe因果、DINO真值或普遍安全/速度，RECON和SPL反侧及全部候选求解费用保留。未核图像点数、代码或复现；Source/PRE待独立复核，未写Books。

## 本次真实 Gate 状态

reviewer必要Source/date/6分/当前owner逐字PRE通过；root授单段及自身注窄锁，作者已实际写Ch25 248并顺读235–262。root非作者实际235–262完整正文/邻接核对POST通过，锁释放；本人章末注已同步真实状态。 未核实现或复现，不授日级验收；本项普通待办只剩授权后的Report同步。
