# 12252 必要 Source 与具体 owner 差额

作者 root。精确 [v1 HTML](https://arxiv.org/html/2603.12252v1)，本日`SUP_CORE_12252.raw/.txt`。实际读 §4.2.1–4.2.4 Eq4–11、§5.1 Table1的训练人口和反侧、§5.2 Tables2–3/成本解释、§6，以及AppendixC的实际评价说明、D1–2和E1/E3直接训练边界。不是全图、全PDF或全附录复核；未核代码/复现。首批准入与日期门复用，v2–4窗外不自动比较。

## 机制与不采用

原静态MLLM条件限制→固定prefixP上反复把前一步连续hidden state当embedding输入，取末位置h_tau→DiT条件与训练监督联合改变。关键是**tau reasoning index与flow t不同**：Eq5在一个tau下有完整flow轨迹；部署仅递归h再以末态生成，不反复解码所有中间图。h_ref从groundtruth文本+输入图得到，L2只末tau开启，不是运行时事实查询或可验证的逻辑证明。两stage先各tau图像flow监督，再仅末态loss/中间forward no-grad并短训；共享MLLM/DiT LoRA仍更新，不保证保住旧轨迹。借用Flow/latent-CoT成熟原则不计Durability3。

QwenImageEdit2511，MLLM+DiT联合rank32 LoRA、LR1e-4、5epochs、512²合成任务图。92.1是task-specific均值不是unified；unified Table1在Maze32 52低于66，VSP4 98低于99，VSP-Super24 100高于97但32 80低于84，不授全任务支配。原文本行拆分曾误读为Maze16/TSP4，mar14_supplement实际Table1独核纠正，不采用该错误列定位。Maze消融支持所测组合，更多latent轮次和不同resolution费用不是同总compute/普遍scaling证明。D2过多terminal训练使中间步骤稀疏，E3中间语义loss反而退步；手动tau/高质量中间label仍必要。

AppendixC只给评价prompts/qualitative例，未充分披露独立parser、validity/optimality verifier/CI；不据生成红线或92.1签算法正确性。AppendixB Sudoku Eq13的行列和约束不是唯一性充分条件，本轮不采用该式，也不把其算法标签当实际实现校验。人工分解/teacher数据、联合适配、latent求值和完整末态denoise均付费；hardware/precision/batch与训练/推理总成本未由本轮量测，online concurrency/SLO无采用。与WorldModel/action-controller不是同一种状态，输出仍需任务独立验证。

## Owner / 评分 / PRE

`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。2+2+2=6标准最低；条件状态/推理与denoise双时钟的具体长期接口缺口定点深入。实际读Ch24 prototype负CFG→pooled-modulation及前后reference分支完整局部，Ch23表示边界与Ch25 observed/imagined入口；已有条件选择与sampler history不等新的MLLM latent递归/终态监督。拟在“guidance还应区分条件进入网络的接口”之前插两段，非root必要Source/PRE通过后root写，不另扩Agent或WorldModel owner：

条件也不必由 prompt 一次编码后始终固定。复杂指令可先在固定 prompt/image prefix 上递归更新连续 hidden state：把前一步状态直接作为下一次模型输入，而不先生成离散中间文本；联合训练条件 encoder 与 DiT，并用分步图像目标和只作用于末态的文本参照，使推理状态成为可学习的条件接口。这里推理轮次 `τ` 与 denoising time `t` 是两条不同轴：训练可监督各推理轮次对应的完整生成轨迹，部署则先更新 latent 条件，再解码末态，不是让每个去噪步都重新生成一幅中间图。末态与参考 hidden state 接近，也不证明逻辑成立或得到了外部事实。

[受限联合训练](https://arxiv.org/html/2603.12252v1#S4)先监督中间和末态，再缩短第二阶段、只对末态传播训练信号；参数仍会更新，不能把中间 no-grad 误写成旧推理链被永久冻结。过多末态训练会损伤中间轨迹，给每一步加语义监督也可能退步；合成任务的专训均值不等统一模型或通用视觉推理能力，部分统一任务仍落后对照。分步标签、teacher/人工构造、联合适配、额外 latent 求值与最终完整 denoising 都有成本，应分别验收质量、独立约束正确性与总预算。标签、latent深度或行为回归不稳时，保留静态条件、显式计划/已验收指导和外部任务验证，不让流畅图像或不可见的“思考”自行取得发布权。

尚未独立PRE、写入或POST，不授本日完成。
