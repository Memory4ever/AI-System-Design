# AutoWorld：动态监督与下游消费的局部差额

仅恢复04-02既存2603.28963家族；exact-v1题为Scaling，不采用v2 Learning摘要/数字。必要Source与normal资格复用STOP §9.51/61；root另实际打开精确v1 §3.2–3.3、§4.1及完整§4.4/Table3，当前Ch25 184–223完整交接。2+1+2=5；具体长期缺口深入受影响机制，不重扫附件或实现。现有ego因子化与OccSim静态补全并未承载动态change加权目标到agent-specific消费者的双层验收。

## 唯一owner与位置

`MULTIMODAL-WORLD-MODELS`，Ch25。接在OccSim静态warp-completion完整段后、原“同一分解原则还可以…”模块化段前；只一段及本人章末静态来源注，不改旧论证/markers。需非写入者PRE和实际POST后才同步整合。

~~~~markdown
从静态补全转向动态预测时，监督人口也必须改变：非语义occupancy中的静态体积占多数，均匀损失可能弱化少量却影响行为的变化。一个分支先补偿ego motion，在两时刻共同有效的voxel中提取occupancy变化，再下采样成latent权重，强化这些位置的预测监督；把权重均值归一为1只控制尺度，不证明仍在优化原均匀风险。预测的未来latent随后提供逐时刻条件与跨时刻摘要，交给另一个负责agent-specific轨迹的生成器；occupancy预测、agent身份/运动时序与真实行动因此仍分别验收。[AutoWorld的受限对照](https://arxiv.org/html/2603.28963v1)支持动态重权的局部收益，但语义监督基线的动态IoU、realism与轨迹误差仍更好，场景预测更准不能直接认证动作更准。遮挡、warp和传感器变化也可触发change，不能把它等同真实物体运动标签；免去world阶段的语义/轨迹人工标签不免下游运动监督、LiDAR/pose、VAE、双生成及完整验证成本。支持域或消费者质量失配时，保留语义监督、较短horizon或已验simulator/真实重观测，不让预测场景或局部榜单取得物理状态与控制权。<!-- source-family:SF-2026-ARXIV-2603-28963 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-28963` — Daily2026-04-02补04-01；[AutoWorld Scaling exact-v1](https://arxiv.org/html/2603.28963v1) §3.2–3.3/§4.1/§4.4 Table3，2+1+2=5，动态change监督→future occupancy→局部/全局motion条件的差额深入。保validmask/ego warp、非无偏目标/非motion真标签、无agent identity；IID8×4且去DPP，MA dynamicIoU .71/RMM .7618/minADE1.4334仍弱于semantic .73/.7651/1.4081。WOSAC1s历史/8s10Hz/32rollout/1Hz replan限定；均值/局部指标非真实安全。world免相关人工标签非全部pipeline无监督/免费，保制备/训练/双采样/校验费；未核代码、复现或完整DPP recipe，不倒灌v2。
~~~~
