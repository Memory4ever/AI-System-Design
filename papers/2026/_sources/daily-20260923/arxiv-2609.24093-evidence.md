# `2609.24093v1` — 跨手型示教应迁移接触结构，而非关节轨迹

- 来源：[arXiv exact-v1 HTML](https://arxiv.org/html/2609.24093v1)；访问：2026-09-23。官方 09-22 `cs.RO /new` 公告批次落本窗 09-23 08:00 北京时间；摘要页 `Submitted 21 Sep` 与首公公告分开保存。若作者仓库能证实更早公开了同一正文，再按真实首发日回拨。
- 旧方案及新约束：示教的 joint angles / fingertip positions 与目标机器人手型兼容时，直接运动学 retarget 简单；多指手的形态、自由度和接触区域不同，纯运动轨迹重放还缺失力和动态可行性。Ch26 已说明跨 embodiment 的目标/控制器分权，但此前未具体说明 contact-rich 技能究竟迁移什么。
- 机制与所有权：论文 §3.2–3.4 用模拟 MANO 手和共享 residual RL 对人类 motion capture 做 physics refinement，生成接触/力注释；按“哪块指面在何时接触哪个物体表面”的序列约束目标手姿，而非复制源手关节；目标手的 residual policy 再修复动力学。Contact proposal 来自经模拟恢复的示教；retargeter 提出手型相关的可行轨迹；真实控制器与传感反馈仍拥有物理 action commit。换手型仍需目标手配置与机器人侧 residual policy 训练，不能称零适配。
- 评价：§4.1–4.3 分别测物理重建、100 条轨迹的 retarget 对照、四种手型与四项真实双手任务；接触、关节限位、抖动与闭环成功分测。作者报告无需实机训练数据的四项硬件执行，但不能推出通用 VLA/world-model 或任意接触安全性。表中 high-iteration contact retarget 仅约 5.5 frame/s，远慢于部分几何基线，是离线数据转换而非控制周期的实时算子；不能只保留成功率增益而删除计算代价。代码链接是可用 artifact 入口，此次未锁定 commit，也未复现硬件实验。
- 失败/共存边界：模拟 contact/force 错误、物体几何偏差、目标手不可达、控制反馈延迟都会让“表面对应”与实际稳定抓取分离。精密接触、触觉缺失或安全关键操作仍要真实 sensor、safety envelope 和人工接管；简单 gripper 任务或同构手型继续可用直接 kinematic retarget。
- Books Decision：`MULTIMODAL-EMBODIED-VLA` Ch26，在已有 latent goal 跨本体路线之后补 contact-rich 分支；Ch25 的模拟环境只提供候选状态，不拥有真实动作。受限证据不支持“所有 VLA 必须采用 contact anchor”。
