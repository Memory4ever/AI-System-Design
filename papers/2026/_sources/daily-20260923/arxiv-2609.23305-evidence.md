# `2609.23305v1` — 固定控制频率不意味着固定动作进度

- 来源：[arXiv exact-v1 HTML](https://arxiv.org/html/2609.23305v1)、[摘要与版本](https://arxiv.org/abs/2609.23305)，访问：2026-09-23。官方 09-22 `cs.RO /new` 公告属于本窗 09-23 08:00 北京时间；`Submitted 20 Sep` 不是公开时刻。当前摘要页为 v1，未见撤回标记；未核实作者项目页是否曾更早公开同一正文。
- 原问题与旧方案：one-step policy 直接输出固定控制时间索引的 action chunk，简单、低延迟，能在静态或时间分配不敏感的任务使用；移动目标拦截或限时复原却要求在相同 20 Hz 接口下调整 chunk 内每段动作的进度。增快模型 forward 并不自动让它知道何时加快接近、何时停留抓取。
- 机制与状态所有权：§III-A–F 把动作表示为进度索引的曲线 `Q(s)` 和从固定执行时间 `u` 到进度 `s` 的单调时钟 `φ(u)`，用 `a_h=Q(φ(u_h))` 解码。单调正增量保证顺序，不保证物理可行性。曲线与时钟由同一 observation/latent 一次预测；示教的归一化动作变化定义训练期进度锚点，decoded-action drifting 加两项对齐损失共同训练。`Q,φ` 不是唯一可识别的运动因果分解，clock 是每个 chunk 的临时状态，不是全任务 phase。policy 只提出动作；短前缀执行与下一次观测/安全控制仍属于 controller。
- 对照与评价：§IV 用两步观测、`224×224` RGB、16-action horizon、每次执行 8 步再重规划；四项真实任务共 300 trial，所有比较 policy 在 Jetson AGX Thor 上以 20 Hz 控制，作者给出 25 ms 平均 policy 推理时间。输送带固定 `16 m/min` 的 matched fixed-clock 对照为 79/100 杯，完整方案 91/100；这个对照同时改变可学习 clock 与其对齐目标，只支持联合表示，不隔离 clock head 的单独效果。Transport/Square 的同架构消融表明对齐有任务依赖，Square 最终五 checkpoint 平均值低于 uniform-clock+MSE 对照。真实任务的 Wilson 区间只反映 trial-level 不确定性，没有训练 seed 方差；论文没有生产尾时延/SLO。代码和配置写为将发布，未见可锁定提交，也未声称复现。
- 证明与未证明：作者实验支持在所列设备、数据、任务下显式 chunk 内执行节奏有价值；不证明 action space 变大、同一时钟对应语义任务进度、任意速度/手型有效，或 deadline/safety 保证。等价曲线-时钟参数化、归一化敏感性、缺失动作模式、观察延迟与 actuator 误差仍可能失败。固定时间索引方案在简单、可预测或训练数据不足时仍合理。
- Books Decision：`MULTIMODAL-EMBODIED-VLA` Ch26，在“动作生成速度与物理执行 deadline”主线增加 chunk 内时间分配这一层；不是把论文方法写成 VLA 必选架构。评分拟为 Design Delta 2、System Reach 1、Durability 2，合计 5/9；独立来源/写后复核尚待完成，不因此提前标记 Daily Complete。
