# 10712 FutureVLA：单篇独立 Source / 评分 / owner / PRE

复核者：mar13_admission_review，非准备者；准备者 mar13_supplement，Books writer 由 root 协调。仅 Daily 2026-03-13 的补充窗口 2026-03-12 BJT。实际启动重读 AGENTS、当前 Research/Report/Sources 使用说明与 Daily/arXiv 范围、Prompt、完整 ROADMAP、本日 README 停点及 LEARNING_STATE 本日路由；Books 判断另读 Project Context / Learning Philosophy / Writing Guide。未载异日候选，未改原窗口、候选、评分或 §4 前缀。

本 ID 完整题摘准入与 §23 日级日期证据有效复用，提交时间不作公开时间。本次实际回读完整 v1 题摘身份 FutureVLA: Joint Visuomotor Prediction for Vision-Language-Action Model、Xiaoxu Xu 等十作者，缓存显示唯一 v1、无 Comments/venue/撤回/纠错标记；只认实际可见范围，不遍历版本或全网无早稿证明。

## 实际必要原证与边界

实际读 [准备包](./SUP_EVIDENCE_10712.md) 后回到 [exact-v1 原响应](./SUP_CORE_10712.raw)，独立解析实际 §3.1–3.2 / Eq1–7、AppA1 架构、§4.1 与完整主 Tables1–3、§4.3 与完整 Tables4–5、AppA2 预算、完整 Tables7/10/12/13、AppA4 limitations 与 A6 实机设置。另实际读对应精确文本 Table13 后的 reconstruction-target 解释，核“strictly necessary”的越界位置。图只用正文/caption，不核曲线/像素/精确图加速或物理相关性；Table6/8/9/11/14/15、额外定性样本、代码和旧模型不展开，不依其数字支撑采用。

[Manifest](./SUP_CORE_10712_MANIFEST_RESULT.json) 实际 final URL 为 `https://arxiv.org/html/2603.10712v1`，GET200、377346 bytes、2026-10-10T03:09:11.810752Z，身份一致。支持与关键反侧已足，两段采用不要求所有 world-model 附件。

### 机制可支持什么

- 冻结 WAN2.2 3D-VAE 编码17连续224×224帧，4N+1格式，1960×48 tokens；两层 encoder 后均分980 visual/980 motor。Visual 重建第一帧392×48 latent，QueryPool 再经 decoder；motor 预测16-action chunk，并以 motor Q 查询 visual K/V、经 learned scalar gate 条件化，重复三次。两组分开的是直接监督目标，前端同读完整未来 clip，不能证明 visual 只含当前/静态信息或 motor 纯物理 dynamics，也未认证跨流梯度隔离。
- §3.2 冻结预训练 teacher，从 future clip 提取 motor target；当前 observation+instruction 的 VLA 经 Transformer adapter 拟合该 target，同时动作监督。未来信息是训练期特权 target，不是部署的真实未来观测或执行授权。AppA2 预训练 OXE+LIBERO 15.6M frames、batch256/LR1e-5/warmup5000、约三天×16A100；后训 Qwen3-VL-4B、两类 action heads、alignment β cosine 衰减。没有补出未披露的 adapter removal/部署 shape、后训总费用、实时 deadline 或零未来监督成本。
- Eq1 第二行覆盖同一 M′，第三行两项仍为该 M′，与正文/AppA 所述 original motor + gated attended 不一致；Eq5 插值 τX+(1−τ)ε 与随后 ε−X target 的时间方向亦需实现约定。两段只采用正文/AppA 一致的条件化分工，不声称精确 gate/Flow Matching recipe 已可执行；这两个符号资格不全盘否定有限任务实证。

### 直接评价怎样收窄采用

- T4 WidowX GT guidance 均值62.5→71.9，OT54.2→63.6；OT Carrot58.3→54.2反退。T5 baseline62.5→仅多帧motor58.4→分开双监督65.6→加入JVG71.9。**无JVG的双监督本身已超过 baseline**；JVG从(c)到(d)同时带条件化/交互，不能把整包差额归给 scalar gate 单项。StackCube在(c)37.5→(d)29.2反退。
- T13 last-frame68.8、first-frame71.9；逐任务 first/last 为83.3/75、75/75、29.2/29.2、100/95.8，仅两项提高、两项持平，不证明第一帧在任意任务严格必要，也不验证 pure motor intent。原文“strictly necessary”隔离，不进入 PRE。
- 完整主 T1/T2/T3 有局部正结果，但 T2 StackCube GT29.2/OT25低于GR00T-N1.5 57；T1 Google VM GT Pick92.3低Villa-X98.7、OT Drawer55.6低π0 72.6。T7 Google GT VM Pick97.6→92.3、VA Drawer61.9→52.4，OT VA Drawer40.2→31.7。平均提高不写“所有任务一致提高”。
- T10 所测 Franka 四任务 GT48.3→70/OT33.3→51.7，有限实机成功可保；A6 300 trajectories/每任务75、5Hz、去static zero-action frames，并不披露可据以补造的 evaluation trials/seed/CI、完整闭环时延或安全力矩保证。A4 直接承认白板接触等仅视觉约束可能不足，应加入 tactile/force-torque feedback。机器人有 torque/force sensing 不证明本模型充分使用且验收过这些信号。
- T12 3D-VAE训练step3.28s、VQGAN3.53s，是训练步费用/不同codec对照，不是控制时延或3D单一因果收益。完整 teacher 训练/forward、future视频/动作标签、visual重建、adapter/后训和 runtime VLA/action head/controller 仍付费。精确总训练/推理费用未由必要位置建立；不因不足而要求全附件或改低分。

Source：上述有限双目标/条件化/teacher→student接口与局部任务证据通过；pure physics、因果解耦、第一帧严格必要、精确公式实现、所有任务优势或通用安全不通过、不采用。

## 评分、实际 owner 与具体差额

**1+2+2=5 成立**：D1为局部双目标条件化训练实现，不借成熟 gate/cross-attention/distillation 抬分；R2为实际 future-clip producer→current-observation VLA 与动作监督的训练责任交接；Durability2为具体 reconstruction target / future特权资格及消融改变“只加多帧”和“如何选监督”的稳定边界。不是因 VLA 名称、SOTA或 owner 联想准入。实际长期差额触发受影响内容必要深入，已完成所需，不扩全证明或全表。

实际顺读 [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 101–120 完整 training-only privileged 3D teacher 局部；272–295 的 pose bottleneck、加性 action-facing 重建两段、forward/inverse 两阶段完整两段、导航 dynamic-region 两段与相邻分支。较宽读取曾截断，272–295 已再次定点完整读取。现文已有 privileged target→student、future reconstruction≠real action；但加性分支拥有组合重建先验，forward/inverse分支拥有无动作视频预训练/适配，导航分支拥有光流选择动态区域，均未承载本稿 **first-frame visual target 与16-action chunk两路监督、motor查询visual、冻结整段futureclip teacher→当前VLA target及T4/T5局部负侧**。因此不是主题相似即NC，也不把一般 teacher≠truth当全部差额。

唯一 owner `MULTIMODAL-EMBODIED-VLA` Ch26。实际读 [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 入口，保留环境转移/observed-belief-imagined责任；另读 [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 与 Ch27 入口，只交接表示/训练数据，不新增 owner。放在 forward/inverse 完整段后、导航 dynamic-region 前，可承接“无动作标注”与“有动作标注”的不同监督分支，保留旧机制/控制权与回退。

## PRE 最小修改及当前结论

已向作者/root指出三处，仅修拟文不改 source：

1. “视觉组只回归第一帧的 latent” → “视觉组的重建目标是第一帧的 latent”。直接 target 分工不等 action-loss 梯度完全不进入 visual。
2. “分开重建与动作监督、再条件化才提高所测均值” → “分开重建与动作监督提高所测均值，再条件化进一步提高均值”。T5(c)65.6本已超过 baseline62.5。
3. “gate 的 StackCube 对照” → “加入条件化的 StackCube 对照”。(c)→(d)是JVG整包对照，不能单因果归给scalar gate。

其余双段机制、训练期未来资格、共享前端限制、费用、接触反馈/controller与BC/原policy回退均可采用；成本与回退为工程判断，不称原文实现自动安全。限定 Source / 5分 / 实际 owner-gap 通过；两段 PRE **按以上修改后通过**。当前不授未经检查的实际写入或 POST，也不授本日 DAY。只写本文件，不改 Books/Report/State/共享 ledger。
