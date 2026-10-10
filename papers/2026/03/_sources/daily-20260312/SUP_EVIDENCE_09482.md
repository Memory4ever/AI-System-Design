# 2603.09482 — StyleVLA exact-v1

本日SUP_EXACT_BATCH3/ADMISSION_BATCH3的完整AB、current无撤回与官方公告lower/owning findable upper同2026-03-11的日期夹证复用。v1唯一版本。[精确v1](https://arxiv.org/html/2603.09482v1)实际读II-D/Eq6–12、III-A2/III-B1/TableIII–VI、IV；2+1+2=5，具体auxiliary train/deploy差额深入。报告不能照摘要写deploy continuous head：MLP regression head仅训练，推理仍LLM结构化trajectory tokens。

CE之外，response pooled hidden state经MLP回归x/y/v/a/heading，regression与内部kinematic consistency作辅助训练，uncertainty weights调两loss。kinematic式只按恒heading/acceleration短步推下一位置，不是完整vehicle dynamics/碰撞constraint。TableIV同Qwen2.5VL7B/50k/3秒horizon，CE→REG→PIKC的ADE1.47→1.21→1.17，PSR29.00→32.08→33.19，支持受限auxiliary收益。PSR定义ADE<1米，不是实际驾驶安全成功；Score按success/reach/error/kinematic固定权重，未直接测人类style接受度。III机器RTX4090/24GB，QLoRA4bit/bf16训练，FPV40k/1000test、BEV50k/2000；fine-tuned与zero-shot不同监督，且不少对照不输出v/a或根本不生成，不授普遍压倒闭源。FPV KCE .11反而高于Gemini3Pro .06，不能写所有物理指标胜出。1.92/2.13秒mean不授实时tail/deadline；batch/concurrency/完整token长度/seedsCI Not Disclosed。未核实现/复现。

Books拟整合owner MULTIMODAL-EMBODIED-VLA。实际读Ch26 Action representation442–480、Reflection1440–1458与Evaluation986–1018，及Ch25/27开篇交接；现有语言辅助目标不覆盖“训练continuous head、部署token”的接口分离。逐字PRE插入“### Trajectory / waypoint”首段之后：

> 连续轨迹监督也不一定意味着部署时使用连续 action head：可以在 token 解码训练旁增加一个回归位置、速度、加速度与 heading 的辅助 head，用相邻预测的一致性塑形 shared representation，部署仍由原 token head 输出轨迹。[有限对照](https://arxiv.org/html/2603.09482v1#S2.SS4)支持这一训练分支，但内部运动学一致不认证障碍、接触或真实动力学，按 ADE 阈值定义的 planning success 也不等于闭环安全。它增加 auxiliary 参数、训练和 loss 权重选择成本，原直接连续 head 或 token-only 路线仍有各自适用域；辅助目标冲突、物理可达性或 deadline 不合格时，回退较短轨迹和已验 controller，而不让 training-only head 取得部署动作提交权。

reviewer已实际Source/date/5分与逐字PRE通过；root授本批Ch26窄锁后已按逐字文字写入Trajectory首段后，保留原接触prefix与全部邻接。锁写后立即释放；root非writer已实际顺读正文/完整邻接及本人末注，actualPOST PASS。必要Source与Books整合完成，未核artifact/复现，不授日级Gate。
