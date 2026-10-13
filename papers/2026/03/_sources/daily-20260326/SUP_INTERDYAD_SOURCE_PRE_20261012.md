# InterDyad necessary Source / Ch24 PRE

作者supp_mar26_fresh；仅03-25补充自然日。2603.23132v1，2+1+2=5及公开日期已独立准入通过，不重开日期或附件。当前为必要Source/PRE准备，未获新Books锁、未写或POST。

## 必要原证及直接反侧

实际读[exact-v1](https://arxiv.org/html/2603.23132v1) §3.1–3.4/Eq1–7、§4.1–4.4/Table1–2、§5。仅采用音频语境→逐帧query→预训练motion latent→spatial injection这条中间监督接口，并分开最终唇同步；冻结Qwen3-Omni还读首帧与text，不是audio-only或已有互动因果oracle。motion encoder输入先mask嘴，人物mask约束注入位置；不能由此保证identity完全解耦或绝无跨人物泄漏。RoDG由双轨VAD及嘴部Gaussian提议局部audio CFG，继承既有guidance而非新发明。

§1 77–79称先Injector后MetaQuery，§4.2 172–173实际训练叙述却先alignment6000步12h，再Injector/audio CA10000步2天；训练顺序口径冲突保留，不交付完整recipe。Wan2.1-I2V14B/Wan-Animate encoder/81帧chunk/9-image context；700k筛选clips(720P/25FPS/3–10s)，100随机测试。原文未披露GPU、precision、batch、seed重复、线上concurrency/latency或SLO；训练时长不能外推总费净节省。主T1 identity分数低于InfiniteTalk，作者“动态更多导致识别困难”仅解释，非控制归因。T2移除Injector与MLLPredictor均损局部代理，但训练/容量预算不等价未隔离唯一MLLM语义因果；DI-Sync与训练encoder同Qwen3-Omni，固定0.5s shift，DI-Sali只量眼区总运动，不能证明社会合宜/causality。侧脸20例为qualitative，普通Sync指标作者承认不可靠，未逐视频独审；仅双人，不支持3+turn-taking。足够支持受限训练接口及指标分责，不支持宣传的严格解耦/普适正确/实时。

## actual owner gap / 原锚

sole MULTIMODAL-GENERATIVE-PARADIGMS，Ch24。实际完整306–324：capacity negative→content/context reference→18600 learned null音视频参照→velocity EMA→referencepopulation→safety分支；以及Ch23/25开篇交接。18600已有跨模态null与两/三支求值合同，但不承载逐帧query映motion prior、非发声反应与局部唇guidance分责。拟在18600完整原段之后、下一“guidance reference也可以来自同一采样轨迹的历史”之前插入两段，不移动原段、不新增收纳节。下两段逐字PRE，需reader Source/具体差额/PRE独核及root窄锁后才写。

## PRE paragraph 1

音视频同步之外，对话中的非发声反应还可拥有独立的中间监督接口，而不把点头、转头当作嘴部同步的副产物。一条受限双人分支先从嘴部被遮住的参考视频提取 motion latent，再让冻结多模态编码器读取双轨音频、首帧和文本，以逐声学帧对齐的可训练 queries 与时间 connector 预测该 latent；训练同时约束 latent 逐点误差与时间差分，之后由人物空间 mask 将预测条件注入视频生成。它将“何时产生哪种反应”与最终外观、发声渲染分开，但参考 latent 仍是学得的代理，空间 mask 不认证彻底的身份解耦或社会反应正确性。<!-- source-family:SF-2026-ARXIV-2603-23132 -->

## PRE paragraph 2

这条条件桥还可按双轨 VAD 提议当前发声者，只在其嘴部附近提高 audio guidance；局部唇约束与非发声 motion 条件不是同一质量对象。[必要方法及反侧](https://arxiv.org/html/2603.23132v1#S3)中，身份指标仍落后一个基线，去模块消融只支持有限代理收益；同一多模态模型提取的时序事件、固定延迟补偿与总运动强度不证明互动因果或合宜性，极侧脸的唇效果也只作局部定性展示。原文训练阶段顺序口径尚不一致，不照录完整 recipe；motion/语境编码、query/connector训练、人物定位与额外 guidance 全部计费，未披露硬件、precision、batch与端到端延迟，不由局部结果外推实时或多人保证。条件失配、质量或净费用不合适时，保留参考视频直接驱动、普通双轨条件生成与独立唇/身份验收。

## 自身静态证据注 PRE

SF-2026-ARXIV-2603-23132 — [InterDyad exact-v1](https://arxiv.org/html/2603.23132v1)，必要§3–5/Eq1–7/T1–2；仅采用逐帧query→motion prior的条件桥及唇/互动指标分责，保训练顺序冲突、同模型评价/固定延迟代理、身份反退与双人/侧脸定性边界；未核实现或复现实验。
