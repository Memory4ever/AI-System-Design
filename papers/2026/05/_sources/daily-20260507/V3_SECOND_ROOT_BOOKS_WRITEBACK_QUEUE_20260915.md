# 2026-05-07 第二轮 Root Books 写回队列

作者侧只形成命题级队列；root 已于 2026-09-15 按目标章节顺序合并 7 项正文增量，避免论文列表式追加。当前仍需新的独立语义终审。

## 2605.04346 — Covariance-Aware Goodness for Scalable Forward-Forward Learning

- Owner：`TRAIN-PRETRAINING`
- Target：`books/part-04-training-system/28-pretraining.md`
- Primary：https://arxiv.org/html/2605.04346v1
- Semantic delta：在 Ch28 activation-memory/optimization 主线中加入受限分支：全局 BP → block-local objective → 可配置 gradient horizon；明确 block boundary、局部 readout/FAL、内存收益、跨层协同损失和 LLM 外推边界。
- Evidence boundary：证据限 CNN/VGG、监督分类与作者硬件；局部目标依赖标签、readout 和特征统计，未证明可扩展到 Transformer/LLM 预训练、跨设备通信或与 BP 等价。
## 2605.04413 — Counterfactual identifiability beyond global monotonicity: non-monotone triangular structural causal models

- Owner：`MULTIMODAL-WORLD-MODELS`
- Target：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`
- Primary：https://arxiv.org/html/2605.04413v1
- Semantic delta：在 Ch25 counterfactual contract 段加入 non-monotone triangular 分支：global monotonicity → mechanism-wise invertibility + context-independent inverse transport；保留 Push 边界、cyclic/latent/vision 未覆盖和 simulator fallback。
- Evidence boundary：只覆盖共享顺序 triangular SCM、mechanism-wise invertibility、低轨迹 state-based 环境；不处理 cyclic SCM、图像 world model、深 latent causal discovery，也不证明真实机器人因果变量完备。
## 2605.04470 — CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies

- Owner：`MULTIMODAL-EMBODIED-VLA`
- Target：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`
- Primary：https://arxiv.org/html/2605.04470v1
- Semantic delta：在 Ch26 online post-training 分支加入 counterfactual proxy → grounded residual correction → EMA constraint；强调同一 visited-state distribution、harness revision、proxy bias/rare-event variance 和真实环境 fallback。
- Evidence boundary：counterfactual proxy 仍依赖 future evaluator，grounded residual 受稀有事件和 simulator realism 限制；EMA 自蒸馏可能保留错误，单一 driving suite 不证明真实道路安全或通用 VLA post-training。
## 2605.04525 — HDFlow: Hierarchical Diffusion-Flow Planning for Long-horizon Tasks

- Owner：`MULTIMODAL-EMBODIED-VLA`
- Target：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`
- Primary：https://arxiv.org/html/2605.04525v1
- Semantic delta：在 Ch26 hierarchical controller 主线中加入 high-level diffusion subgoal → projected latent target → low-level rectified-flow trajectory → MPC/inverse-dynamics handoff；保留数据、表示、延迟和安全 fallback。
- Evidence boundary：依赖带成功/失败标记的 demonstration、RSSM 表示与 inverse dynamics；真实样本和 trial 数有限，未证明开放世界安全、任意 embodiment 迁移或 end-to-end latency SLO。
## 2605.04647 — ReflectDrive-2: Reinforcement-Learning-Aligned Self-Editing for Discrete Diffusion Driving

- Owner：`MULTIMODAL-EMBODIED-VLA`
- Target：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`
- Primary：https://arxiv.org/html/2605.04647v1
- Semantic delta：在 Ch26 action-token/correction 段加入 draft → selective rewrite → invalidate/recompute mutable action state → reverify/commit；说明 RL credit 必须覆盖完整 rollout，并限定 NAVSIM/Thor/oracle 证据。
- Evidence boundary：固定分辨率 BEV token 限制精度，RL reward 是 proxy，未在更高保真 simulator 验证；编辑扰动集中纵向/横向误差，31.8ms 平均延迟不证明尾延迟或安全闭环。
## 2605.04980 — Conceptors for Semantic Steering

- Owner：`MODEL-SAMPLING`
- Target：`books/part-02-model/20-sampling.md`
- Primary：https://arxiv.org/html/2605.04980v1
- Semantic delta：在 Ch20 trajectory feedback/hidden-state control 后加入 vector → subspace projection 的替代分支；把 quota 限定为 layer sensor，区分 interpolation/replacement 强度、degenerate-output 风险与外部 verifier。
- Evidence boundary：只测三种较小 instruction model、三个英文概念、单层 intervention、有限 contrastive pairs 与自动 classifier；Boolean composition 依赖子空间 overlap，不证明行为正确或生产安全。
## 2605.05172 — When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning

- Owner：`MULTIMODAL-EMBODIED-VLA`
- Target：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`
- Primary：https://arxiv.org/html/2605.05172v1
- Semantic delta：在 Ch26 online RL 段加入 BC baseline Q state + learnable RL Q state + per-state gate；明确冻结/更新 owner、估计误差、支持的 policy class、robot wear 风险与 safety fallback。
- Evidence boundary：需要 BC policy 暴露 action likelihood 与 entropy；soft-optimality、Q estimation 和 critic calibration 可能失准，尚不支持 diffusion/flow policy，Q gate 也不替代 physical safety envelope。
