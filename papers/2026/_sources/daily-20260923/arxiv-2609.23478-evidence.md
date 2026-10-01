# 2609.23478v1 定点证据审阅：Latent Action 的代数指标不能认证时间结构

- 身份：Di Wen 等，*Algebraic Consistency Alone Does Not Certify Temporal Structure in Latent Action Models*，[官方摘要和版本史](https://arxiv.org/abs/2609.23478)、[精确 v1 HTML](https://arxiv.org/html/2609.23478v1)。访问日 2026-09-23；官方 `cs.CV/recent` 的 2026-09-22 公告批次落入本日报 09-23 08:00 北京时间，`v1 Submitted` 09-20 09:03:21 UTC 是投稿字段，不替代公开时间；页面未见 withdrawn。未发现更早的作者 primary 首发，但若后来证实，应回拨 owner。
- Owner：`MULTIMODAL-EMBODIED-VLA` Ch26 的 latent action 与行动证据；Ch25 已有“代数 surrogate 不等于物理/规划可用”的上层原则，只作 handoff。非作者独立复核认为本篇改变 Ch26 原句暗示的认证强度；V2 评分 Design Delta 2 + System Reach 2 + Durability 3 = 7。

## 问题、机制与旧方案边界

Action-labelled 机器人轨迹昂贵，从 action-free 视频两帧推断 latent transition 再预训练策略是合理的低标签路线；加性与可逆性损失让 latent 更规整，也能衡量模型是否遵守自己设定的代数目标。争议出在把低 additivity/reversibility error 进一步解释为“已经学到真实时间后继或可执行动作”。在加性 decoder 的重构目标下，`dec(z_ab)≈φ(b)-φ(a)`；任意三帧的 feature 差分都会望远镜相消，不需要真实时间顺序。Proposition 1 只给 decoded-space 残差上界 3ε/2ε；code-space 上界还要 decoder 线性、满列秩。归一化比率可能被近零分母放大，非线性或量化 decoder 不能直接继承该定理。

状态所有权由此必须区分：表征训练器可以优化代数约束，但 evaluator 不能把它的自有 loss 当作外部 action/temporal 证书；真实 successor pairing、action labels 与环境 outcome 才拥有后者的判定权。更强的评价合同先用 architecture-matched、已训练但无代数约束的 reconstruction baseline，随后破坏时序配对后**重新训练**各 arm，保持数据与模型预算可比，再以 action-content probe、任务闭环结果（该论文仅 LIBERO 仿真）及多 seed 不确定性核验。只在固定模型上重排评估三元组不足以替代重训控制。

## 实验、trade-off 与未证明

- §IV-A–F：五源域、三 seed 的结构实验显示普通重构已贡献相对未训练 anchor 的大部分误差下降；destroyed-pair retrain 后 constrained error 虽上升，仍在各域低于 real-pair unconstrained。模拟例子中 controllable 与 nuisance feature 差分都可把代数误差压到近零，但只有前者编码动作。这说明指标不可识别，而非证明所有 latent action 表示无效。
- §IV-G/H：作者自建、与 released system 不同的 LIBERO 仿真 pipeline 以相同 policy architecture/优化/rollout 协议比较，13 seed、每任务 50 episode。低代数误差与 action-code 线性可解码度、最终 success 不呈单调关系；效果受 seed budget 影响。该结果不能直接评价任何已发布系统或真实机器人，也不能说破坏配对通常更好，或代数约束普遍损害策略。
- 代价是需要 architecture-matched 对照、破坏配对重训、动作标注 probe 与闭环 rollout；在只开发表征而无 action labels 时，代数指标仍可作为内部训练诊断，但不能升级成“已学到时序动作”的发布证书。旧方法与新审计是不同证据层，不是替代训练方案。

## Disposition

非作者准入/全文证据复核通过；Ch26 已将“supervision 使表示同时保留任务语义与动力学约束”收窄为条件命题，并在旧方案→约束变化处补入上述评价差分，写后独立语义复核通过。作为本窗受限实验性证据，不外推跨 embodiment、真实物理安全或生产控制收益。
