# 2603.08862 — APPLV exact-v1

本日SUP_EXACT_BATCH4/ADMISSION_BATCH4及独核AB/date夹证复用，2026-03-11公开/current无撤回；[v1](https://arxiv.org/html/2603.08862v1)必要§IV–VI/训练与真实TableII实际读。2+2+2=6，planner参数接口深入，不借MPC成熟性加分。

输入不是自然RGB-only：720beam LiDAR、globalpath及footprint渲染topdown pseudo-image，Qwen2.5VL3B最后4层hidden＋DPT＋历史/velocity条件回归φ；φ含速度限制、costweights、horizon及inflation，经典planner再出(v,ω)。Visual frozen、language LoRA r64/α128＋history/head，expert/APPLR labels MSE后TD3；policy输出参数不等保留原planner每项safety。1000attempt/environment、0.5sec采样，困难/运动filter和停滞/转圈保留10%使约30k/planner人口有选择偏差。BARN300train/300test/四planner支持有限移植，不同SL/RL及budget不得混为唯一VLM因果。

TableII Jackal＋Hokuyo两course各3次：DWA SL0/6→RL1/6，TEB两者2/6，MPPI/DDP6/6，不可写全部planner真机均安全成功。Costmap/localization扭曲使DWA/TEB仍失败，直接LiDAR/history路径亦不授全环境保证。现实remote5070Ti，训练A100；.41s/5070、.47/3080、.27/5090为作者平均推理，不是sensor→network→planner尾deadline。5500样本以上结果不单调，非普遍scaling。§VI“maintaining safety assurances”只作者结论，未证明可变inflation/速度边界不会弱化保障。完整precision、TD3与LoRA全生命周期预算、seedsCI、RTT/concurrency/SLO ND，未运行代码。

owner MULTIMODAL-EMBODIED-VLA。实际Ch26层级139–154和VLM-conditioned controller163–175、Ch25/27交接；已有高层terminalcost权重不直接提交动作，但未显式处理把速度/障碍inflation这样的planner安全相关参数交给VLM。逐字PRE插入“VLM负责场景和语言grounding，专用policy/controller负责动作”首段后、floating-base pose段前：

> 高层也可以不输出 waypoint 或 action，而根据观察与历史回归 classical planner 的速度上限、代价权重、horizon 或 obstacle inflation，再由原 planner 生成短动作。这样复用已有规划器，却把参数范围与修订带入控制契约；尤其速度和 inflation 会改变原安全余量，不能从“仍用 classical planner”推导原保障原样继承。[有限导航对照](https://arxiv.org/html/2603.08862v1#S5)中，costmap 与定位失真仍使部分 planner 失败，平均模型推理时延也未覆盖通信和规划 deadline。渲染、历史、标注/训练、参数验证与低层规划均付费；host 应保留受限参数范围、planner revision 和拒绝记录，几何、参数或时序不可信时恢复已验固定参数、重新定位或停机，模型只拥有 tuning proposal，不拥有 safety envelope 的改写权。

reviewer已实际打开必要v1及具体owner局部，Source/date/6分与逐字PRE通过；root授Ch26指定单段及本人末注窄锁，已按逐字拟文＋对应SF marker写入VLM-conditioned首段后、floating-base前。作者实际完整邻接及自身末注顺读，锁释放，root非writer实际顺读Ch26完整158–180邻接及2093本人注，actualPOST PASS。必要Source与Books整合完成，未核artifact/复现，不授日级Gate。
