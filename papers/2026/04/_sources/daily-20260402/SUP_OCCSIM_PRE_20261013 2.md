# OccSim28887 受限 owner PRE（未授锁、未写 Books）

Source5由screen准备、resume reader实际独核；只采静态occupancy的ego-warp→completion接口，不采用一般traffic dynamics、persistent-map或安全保证。Owner `MULTIMODAL-WORLD-MODELS` / Ch25；窄范围一段与本人静态末注。日期独立普通层仍须闭合，PRE不授候选或Integration。

## 当前完整局部与拟段

这种结构先验增加了传感器、时钟同步、参数识别和 model-mismatch 风险。自运动不可观测或模型误差占主导时，单体学习模型仍可能更合适；安全关键路径也仍需 simulator、规则模型或 hybrid residual 的独立校验。

静态occupancy的观察生成还可把这条分解落实成补全问题：在已知、受限的平面ego motion下，先将上一时刻latent刚体传播到下一坐标系，再用几何可见性与训练期随机遮蔽形成不完整条件，由生成器补全下一latent；waypoint也须在同一目标坐标系对齐，不能让简单复制冒充长期变化预测。这里学习的是warp与可见条件下的静态场景补全，不是一般交通动力学；latent旋转与插值不保证无损，分布相似也不证明同一个未见场景身份一直被保存。[OccSim的有限对照](https://arxiv.org/html/2603.28887v1)仅在给定静态AE空间、平面运动与训练人口中支持该接口，随机mask、token条件与辅助loss共同变化，不能独归一个组件；动态layout仍由另一路生成和规则运动驱动。AE、warp、补全训练/采样与长rollout校验都付费，条件旋转失配、遮挡历史不足或质量回归时，保留真实重观测、显式静态地图或已验simulator，缩短horizon，而非由长期FID批准物理行动。<!-- source-family:SF-2026-ARXIV-2603-28887 -->

同一分解原则还可以从“已知自运动”推广到可复用 dynamics module：让 actuated agent 与 background environment 分别持有自己的 transition state 和版本，再由显式 latent interface 组合交互。这样替换 agent 时可以冻结背景模块，避免把不变环境一起重训；但模块边界必须由动力学责任而不是视觉分割决定，interface 才拥有跨模块 effect 的组合语义。

## 拟本人末注（仅在写入时当前末尾追加）

- `SF-2026-ARXIV-2603-28887` — Daily 2026-04-02补04-01自然日；[exact-v1](https://arxiv.org/html/2603.28887v1) §3.1–3.3/4.1–4.3/6.1/10，2+1+2=5。只采静态ego-warp→visibility/masked-completion分责；Eq2 conditioning mask与complement loss范围不闭、τ²非exponential，不照录recipe。平面/AE/插值依赖、辅助组件联变、distributional fidelity非persistent scene identity、dynamic规则层与全部费用近文；未核实现/复现或物理安全。
