# 2604.25416v1 Biased Dreams：本日作者有限证据审阅

仅按 [官方 exact-v1 HTML](https://arxiv.org/html/2604.25416v1) 的 §2.2–2.3、§4、§5.1–5.3、§6 和现有 Ch25 邻段审此 family；不把旧日报 `deep_complete` 或 8 分当 V3 Gate。日期归属仍由本日 arXiv 公告联合链负责；页首 `28 Apr` 本身非首公开证明，若有更早独立正式正文须重开。

## 可迁移问题与受限机制

World Model 规划常用 latent transition ensemble 的**单步分歧**代表 epistemic uncertainty，再以低分歧支持更长 imagined rollout。但这只对模型彼此是否同意敏感；若 RSSM 从 OOD 起点被 recurrent latent dynamics 拉回训练密集的 attractor，ensemble 可以迅速一致，而同一 action sequence 对应的真实环境 body state 已偏离。于是 `latent uncertainty ↓` 与 `physical discrepancy ↑` 可同存，prior rollout 的 reward 还可能相对 simulator 系统性偏高。这个反证把本书原有“长 horizon 放大误差／要测 uncertainty”收紧为“**uncertainty proxy 自身也须按 rollout horizon 与真实状态／奖励校准**”，不能仅把高低 uncertainty 当执行许可。

作者测 RSSM 与仅替换类别 latent 的 Cat-RSSM，在 4 个 DMC Suite 任务、5 seeds、训练 1M 环境步下，取 50-step rollout（先 3 步 posterior warm-up）。`M=5` 个单步 latent predictor 用 geometric Jensen–Shannon divergence 测分歧；真实误差由同起点同 action sequence 的 simulator 状态与模型 physical decoder 输出计算 body-position L1。§5.1 的 OOD 起点由人工设成物理有效但罕见；Cartpole Swingup 无 OOD 起点。Fig4 比较 ID/OOD：OOD 初始分歧高，随后接近 ID 水平，physical error 却持续较高；Fig5 对相同 action sequence 比 predicted vs simulator reward，prior 乐观，posterior refresh 更接近。PCA 流场图只用于可视化 attractor，不是可证明的全维吸引域定理。

## 反证与范围

- 物理 PE 对照使用 MuJoCo HalfCheetah，而 latent RSSM 主实验用 DMC 四任务，ID/OOD 的选法也不同；故不能说受控实验已隔离“latent 架构相对物理模型必然失败”的唯一原因。§6 明说 attractor 因果机制的形式分析留待未来。RSSM/Cat-RSSM 的一致受限现象仍成立。
- Physical decoder 是额外联合训练的观测投影、且作者承认其重建质量不好；body-position L1 因此是有偏测量通道。对同 action 的 simulator 奖励差提供另一种更直接校验，但也未证明全部 latent 变量的误差结构。
- 只测这两类 RSSM、四个 DMC 任务、五 seeds 和 50-step open-loop；不能推成一切 World Model、其它 uncertainty estimator 或真实机器人必失效，也不能声称短 horizon uncertainty 无用。论文未提供已验证的修复算法或形式安全阈值。

## Score、owner 与最小 Books 提案

建议 `Design Delta 3 + System Reach 2 + Durability 3 = 8`，Deep；保留有限风险纠错，非安全标签泛化。真正 owner 为 [Ch25 Imagined rollout 与 latent dynamics](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：目前正文已有 `error_H ≠ H × one_step_error`、真实 observation refresh、重建好不等于 control-sufficient 等总原则，**但未明确**“ensemble 在自己被吸回支持域后也会自信，从而同低分歧掩盖真实误差/乐观 reward”这一特定选择失效。若 root 非作者 source→actual-owner 复核确认，最小 patch 应只在 Ch25 `Imagined rollout` 或其 latent dynamics 后补一段：在每个 horizon 评估 ensemble 分歧与同 action 真实 transition/reward 的联合校准；低 disagreement 不自动批准长 rollout 或动作提交，失配时缩短 horizon、强制 observation refresh、退回可核 simulator/真实环境。不要把 RSSM attractor 写成 universal theorem，也不要把作者未验证的 latent restructuring 当已交付回退。Ch66 可链接评测对象但不成为第二个知识 owner。

本作者未动 Books、正式 V3 日报或共享 checkpoint。此项 Books 和日期仍待独立 Gate；普通可执行项继续推进。
