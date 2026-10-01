# 2604.24921v1 Libra-VLA：混合动作空间的有界机制核

状态：04/29 V3 作者侧标准必要证据，待非作者 source→actual-owner 核；不写共享 Books，不是日期或日级 Gate。

## 身份与贡献

- [官方 exact-v1](https://arxiv.org/html/2604.24921v1)题名 *Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System*；[v1 身份页](https://arxiv.org/abs/2604.24921v1)及本日官方公告批链待与独立更早公开例外核对。`submitted` 不能单独当首公开。
- 原有 VLA 可以用离散 action token、连续 diffusion/flow head 或快慢两级异步 controller；这里值得审的非同义分支是让**低频语义 planner 先产生可执行的粗离散方向序列**，高频 action refiner 再以每步粗 token 为条件预测连续细动作，二者不是各自预测完整动作再平均。若它成立，action schema 要同时标注粗意图的 codebook/量化粒度、planner horizon、细动作解码与对应 observation freshness；不是只取论文 benchmark 排名或两模块名字。

## 必要原文、对照与停止边界

- §2.1–2.2 承认已有 temporal hierarchy、dual system、HybridVLA 并非首创粗细/混合概念；作者区别点为 action-space 内串行条件化而非平行算术融合，以及下一宏动作序列的预测 intent buffer。§3.1–3.3 用离散 `aᶜ` 作方向锚、连续 `aᶠ` 作局部修正；训练先以真实粗 token 做 teacher forcing，planner 达阈值后改用它预测的 token，属于有身份的 train/inference exposure 切换，不是独立 safety repair。
- §3.4 的 FIFO 在空时由当前 observation 一次产生 `M×H_chunk` 粗 token，之后 `M−1` 个细控制步仅消费队列，planner 暂不重算；这减少慢 VLM 调用，也使后续环境改变时旧粗意图可能仍在 buffer。§5 Limitations 明言所有预测意图顺序消费，尚无动态验证/失效重规划；不能把 intent buffer 当执行授权、开放世界稳定器或无 stale-action 风险机制，低层 controller/safety envelope 仍独立。
- §4.3 Table 3 的同框架消融：monolithic Libra-Base 平均 88.3、只加视觉 encoder 87.0、粗细 Refiner 95.1、完整 97.2；支持本 setup 的串行表示分支有独立增量，也显示“多 encoder 即改善”不成立。Table 4 在无/有附加 encoder 两组中，`N=10` 分别 95.1/97.2 优于 `N=2` 的 92.3/79.0 与 `N=100` 的 83.9/93.9，但只试四个 bin 配置，同数据/模型；`N=10` 是本实验工作点，不能证明一般倒 U 连续曲线或“恰在两模块学习难度均衡”的测量事实，论文未直接量化每模块的可比 learning difficulty。
- Table 5 curriculum 的平均 success 97.2 对纯 teacher forcing 96.0、从头仅预测 token 95.5，说明切换能减本 setup 的 exposure mismatch，但没有隔离阈值/额外训练或长期漂移。Table 6 `M=2→5` 时 RTX4090 所测平均模型 inference latency `122→104ms`，平均成功率 `97.2→95.3`；对 monolithic 220ms 的百分比属于异构架构/调用频率共同差异，不是单独 FIFO 的因果收益，也没有 tail、jitter、真实控制周期违约率。真实 AgiBot G1 实验是三项受控任务、人工监督与急停，不等于无监督开放世界物理安全。

## owner 与拟处置

- [ROADMAP](../../../../../ROADMAP.md) `MULTIMODAL-EMBODIED-VLA` 的 [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)已分账离散 codec vs 连续 head、action chunk identity、快慢异步执行的 deadline/stale/cancellation 与低层 commit；还有 gaze token→action head 这一不同来源的上游监督分支。它暂未明确描述**粗离散动作自身作为高频连续动作的串行条件**，以及量化粒度、teacher-forcing 切换与 intent buffer 的耦合。可作窄 Books gap 提案，但须非作者验证这不是已有叙述的简单换名，且不能复制论文架构细节为普遍配方。
- 作者侧拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6/9`、Standard。受限机制可信、`N=10` 与硬件成绩不外推；当前处置待非作者判 `Integrate` 窄条件分支或 `No Change — Existing Coverage`。最小可写命题若获准：在离散/连续二择之外，粗离散意图可作细连续 proposal 的条件，但须绑定 codebook、observation、horizon 和 teacher→predicted exposure；异步缓冲带来的 stale action 由独立 controller 验收，收益与成功率一起测且保单头/同步 fallback。未获锁和真实写后核前不计整合。

最小同行核：官方 §2.1–2.2、§3.1–3.4、§4.3 Tables 3–6、§5 Limitations 与 Ch26 离散/连续段、action chunk identity 和异步 deadline 段；不需扫完整机器人引用史或项目页后续版本。
