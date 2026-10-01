# What Matters in Designing World Action Models — 2026-09-23 定点证据

- Source Family：`SF-2026-ARXIV-2609-24048`。
- Primary：[arXiv 版本记录](https://arxiv.org/abs/2609.24048)、[exact-v1 HTML](https://arxiv.org/html/2609.24048v1)。`cs.RO/recent` 的 2026-09-22 官方公告批次包含该 v1，属本窗；09-21 投稿字段不是公开时刻。未见撤稿；未找到更早原始发布，但这不是穷尽性证明。
- 准入与评分：Ch26 已有 explicit rollout、joint generation、direct latent policy 三分支，但尚缺把 future→action 读取通路、时间先验存放位置、auxiliary world objective 时序分开的受控评价合同。Design Delta 3、System Reach 2、Durability 2，合计 7。Owner `MULTIMODAL-EMBODIED-VLA` Ch26；Ch25 保留通用状态转移原则，不复制这项控制策略证据。
- 机制与状态：§III-B 比较六种 video/action dependency、八种 latent、四类训练目标。预测的 future 只拥有 provisional imagination；action head 读取它时才构成部署推理通路；controller/environment 仍分别拥有 action commit/transition truth。Frozen inter-frame encoder 与 policy-trunk temporal modeling 是不同时间先验位置，不能只靠视频可视化质量互换。
- 关键对照：§IV-A 中 Joint/Uncond、Bidirectional/Action-to-Video 的 matched structural pairs 在 separately trained policy 间比较，不能单独作 inference 因果证明；作者再固定已训练 policy 扰动 future latent。强内容噪声下 action change <1%、成功率变化小，时间顺序颠倒则动作与成功率下降，LIBERO-Plus OOD 更明显。结论只覆盖其两 future slot、扰动方式及训练配置，不能说真实未来画面内容对所有 WAM 无用。
- 表示与目标：§IV-B 的 inter-frame latent 在 RoboCasa-GR1 ID 优于 framewise，而 LIBERO-Plus OOD 顺序反转；linear probes、时间错配支持“固定时间先验可能脆弱”的解释，但未识别普遍因果机制。§IV-C 中 BC-only 是该 ID 设置的最强分支；BC+VG 在 LIBERO-Plus OOD 从 77.96% 到 81.22%，早期合训全部目标低于 BC+VG；先 BC+VG 训练 80% 再加入 dynamics 目标达到 83.15%。这不是通用训练日程、所有域的收益或单独目标的纯因果效应。
- Evaluation 与未证明：§III-A/IV-D 的 DROID 是真实机器人采集数据的 held-out **离线动作预测** MSE/L1/Accuracy，不是实机闭环 success/safety。仿真为 RoboCasa-GR1、LIBERO、LIBERO-Plus；作者 §V 自认模型、数据、训练预算中等规模，大规模跨 embodiment、真实闭环、延迟及安全均未证明。性能数须绑定该 benchmark、具体 variant 和训练配置；硬件、precision、部署并发与 SLO 未披露，不能写普遍效率结论。
- Books：Ch26 的 World-action model 段新加一小节，沿已有三分支后承接“怎样验证未来通路被用到”的问题，保留 direct VLA、显式 rollout、真实 controller 的共存边界。独立证据审阅者 `sep23_independent` 已核准入、日期、对照、证据范围；Books 写后复核通过，回指前述 latent prefill / Future-KV 的过渡句已澄清。
