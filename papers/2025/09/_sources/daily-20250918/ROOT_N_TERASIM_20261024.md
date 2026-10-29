# 13164 TeraSim-World：首次决定准入的有限事实

作者456明确尚未开始CORE/Methods且无请求在途，root本轮明确接受**最小决定N**，不接日期/评分/标准必要或owner。原完整v1/current题摘复用，不第三AB；不是完整Source自行签收/正式候选或Books结论。

## 原件和实际范围

[Exact-v1](https://arxiv.org/html/2509.13164v1)的[raw](ROOT_NCORE_TERASIM_13164_20261024.raw)/[request](ROOT_NCORE_TERASIM_13164_20261024.request.json)，GET 2026-10-24T07:51:57.777370Z～07:51:58.782645Z，200/exit0，109987B，SHA256 `9d196e02e7b0847ed4e2f8f6a7daf79b968b7ab4e90951bd2ea5ab472e5bd9b6`。首次实际完整读III/IV-A–C/TI/F2–3必要文字、V-A–C/整TII/直接F4–6文字caption和VI，决定事实已足。不看曲线/视频像素，不核代码、外部TeraSim/Cosmos论文全部方法或实际仿真/复现；本次材料边界只这份稿。

## 不是只有平台名称串接

原文具体给出trajectory到sensor生成的中间消费者：从地图road/lane/crosswalk和各agent时序位置构造3D线条/cuboid场景，以声明的六相机intrinsic/extrinsic逐帧投影成HDMap视频，作为现成Cosmos的控制输入。另从同一地点StreetView取得各view静态环境描述，明确忽略原图交通参与者，避免将历史照片中的动态对象与模拟agent混在一个条件来源。

生成顺序也具体：先用front-view HDMap与prompt交Cosmos-Transfer1-7B-Sample-AV，生成front视频；再把该生成结果作为cleanvideo条件、连同其它view的HDMap/各view prompt交Single2Multiview模型。这里从前级传的是**生成的观察条件**，不是新增真实相机证据；trajectory、相机几何、静态文字和前级视频分担不同控制资格，不能由text-only location名称获得一致运动。

这种绑定的可核接口使本项存在潜在主线增量：**只生成背景外观或仅模拟轨迹，无法让多相机生成器消费同一traffic event → 以相机标定投影的时序HDMap为公共布局控制，并将静态地点条件与agent运动来源分离 → 需要分别验轨迹控制、多view一致性和真实场景/下游闭环，而非只验照片风格。** 这不是宣称发明ControlNet/多view attention、TeraSim的NADE或Cosmos新architecture，也不以“安全关键/全球”声望准入；具体的是已有agent simulator到生成sensor的输入合同与先front后多view的依赖。

## 潜力不代表以下结论已经成立

III/IV所称strong consistency/任意地点互通尚无独立量化验证。VI明确large-scale dataset和closed-loop AV testing是future；当前V仅AnnArbor一roundabout、Mcity两类例和全球五个代表场景的文字/示例，不给系统成功/失败分母、轨迹误差、多view几何一致指标、训练/下游安全收益或与CARLA配对公平控制。不能由作者说“closely follows”或看起来真实签可控世界模型/真实安全。

Cosmos ControlNet/zero-linear、cleanvideo/view-indicator/cross-view attention等机制来自所用模型，不算本稿新发明；NADE/crashstats/denseRL也指向前TeraSim，不能据本稿集成文字把统计代表性当已核新定理。OSM格式转换、TomTom速度比→Greenshields密度是派生估计而非当时真实traffic distribution；StreetView capture age、pose与live traffic/模拟时钟不自动同一观测时刻。

六view StreetView heading/FOV拟匹配RDS-HQ，不使历史全景图成为车载真实新视角；模拟cuboid也不锁定生成像素中的完整物体身份/碰撞几何。front120frames/24FPS/704x1280与surround六view各57frames/24FPS/576x1024分别披露，完整裁剪/时间对应未闭，不默造120→57同步recipe或把“24FPS输出”当生成速度/实时deadline。

全部地图/API、StreetView和VLM制备、traffic/对抗模拟、HDMap渲染、多级扩散和生成视频驻留/独立几何与真实闭环验收都付费；所用大模型/RDS预训成本不因管线自动化免费。本文没有完整硬件/precision/生成时延/成功率分母或净费用，不采用cost-effective/可替代实路测试作为已证收益。条件不可靠时保冻结地图/轨迹、可重放传统sensor renderer与真实采集/独立控制，不给生成图像现实authority。

## 交接

root只提出**存在值得核验的具体agent→sensor控制合同，潜在P而非仅组件名组合**，未自签P/评分/日门或完整Evidence。Socrates唯一另一角色回上述决定域实际采用/校准，认可后再按其本日职责核日期、原拟三分与必要差额；本包已读且有效域可复用，不为了“标准必要”重读同一III/IV/V。Helmholtz只复用闭合的最小N角色链，不第三此原域。若认定本合同仍不构成新设计/条件，应给具名增量不足理由，不因未有完整实验或安全保证而关闭潜在贡献。

当前无root GET/exec在途；未核可选图/代码/外部实现不列必要材料阻塞，不扩大整站/全Cosmos研究，也不把本包当日报完成。
