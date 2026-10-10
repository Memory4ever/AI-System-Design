# 2603.09163 — SPAN-Nav exact-v1

本日SUP_EXACT_BATCH3/ADMISSION_BATCH3完整AB/current无撤回与独核2026-03-11夹证复用；v1唯一版本。[精确v1](https://arxiv.org/html/2603.09163v1)actual III/IV、V必要annotation、VI-A–D/TableI–IV、VII；2+2+2=6，compression consumer与train/infer gap深入。

VQ-VAE occupancy encoderdecoder先train，后丢discretequantization用continuous latent→singlehidden token；RGB预测occupancylatent，再将该latent投影回VLM actionreason，AH MLP预测ego x/y/theta。不是显式语言CoT的因果证明。StageI action看GToccupancy，StageII看selfpredicted，只有有GT时才occ loss；不把GTteacher当部署observedgeometry。7.08M多任务/4.2Mocc，真实FrodoBot occ是DepthAnything3重建proxy，32H100约768GPUh。实机GO2四camera→remote4090→onboardcontroller，仅定性展示，完整precision/RTTtail/通信loss/trialCI/部署并发SLO ND。

TableIV同data：无StageII IoU58.04 vs58.11近似，但HomeSR56.8 vs90.9、Commercial67.3vs91.0，正文相应数56.6/68.1不一致，本包采用table不合并。无CoT IoU60.71高于58.11但SR81.3/85.2低于90.9/91.0，重建好不等action好。离散45.03/80.3/80.0支持有限表示对照，不授普遍quantization失效；MetaUrban unseenPointNav92低于UrbanVLA97，不全SOTA。one vs150tokens FPS26%作者局部测量不等端到端成本，未读曲线像素不额外定数。各benchmark不同successprotocol，proxy geometry不认证collisionfree。

owner MULTIMODAL-EMBODIED-VLA。实际Ch26PrivilegedTeacher93–112、actiongradient250–284、压缩1245–1253，Ch25/27交接已读。现有原理覆盖表示非metric/压缩须action验收，但未承载GT→selfpredicted consumer训练变化及occupancy质量相同action大退。逐字PRE插入PrivilegedTeacher末段HAIC之前：

> 几何监督也可保留为部署时的预测接口：先把 occupancy 压成 continuous spatial latent，让 RGB 模型预测它，再把该 latent 接回 trajectory head。若训练动作只消费 ground-truth occupancy，部署却消费预测结果，重建指标相近也不能消除消费者失配；应另用 self-predicted 条件训练和闭环动作验收。[有限导航对照](https://arxiv.org/html/2603.09163v1#S6.SS4)中，去掉这个阶段几乎不改 occupancy IoU，却显著降低导航成功，另一个变体的重建更好而动作更差。单 token 因而只是一种任务相关压缩，不恢复真实障碍或允许通行。occupancy 标注/重建、双阶段训练、额外预测和远程控制均付费；几何或通信不可信时，回退显式 state estimator、较短 waypoint 与已验 controller，不能由辅助表示分数签发物理安全。

reviewer已实际Source/date/6分与逐字PRE通过；root授本批Ch26窄锁后已按逐字文字写入PrivilegedTeacher marker后、HAIC前，保留原段。锁写后立即释放；root非writer已实际顺读正文/完整邻接及本人末注，actualPOST PASS。必要Source与Books整合完成，未核artifact/复现，不授日级Gate。
