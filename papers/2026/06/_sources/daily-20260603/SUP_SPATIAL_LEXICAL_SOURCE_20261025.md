# 01914：视觉信息可读与语言选项干扰

## 范围、版本和首次必要审阅

仅06-03补Jun02自然日，AGENTS、当前Research/Report合同、Daily来源/Prompt已重读，ROADMAP/三Books上下文与实际Ch23/邻22–24交接按本日加载。R62完整题摘/Jun02联合日证有效复用，不重GET日证或搬旧日期。[精确v1](https://arxiv.org/html/2606.01914v1)及[当前事件页](https://arxiv.org/abs/2606.01914)实际打开；v1 Jun01、v2 Aug31，所见无撤回/勘误，当前EMNLP状态不倒填v1贡献。已读§3–6/T1–2、D完整推理/解析、J完整probe控制、K.1–2/K.6–7、L.1训练/偏好构造；未看图像素、全K层曲线/所有prompt、代码或复现。支持与直接反侧足即停。

正式拟2+2+2=6，而非R62题摘暂拟7：实际新增是视觉consumer可用信息与LLM侧选项干扰的诊断/干预界，不是所有视觉错误的归因翻转；跨视觉表示、语言消费与训练scope选择，长期稳定但不是通用基础定理。不因已有覆盖/后续工作量改分，也不动任何旧正式候选字段。

## 核心支持与必要反证

三合成集各2000场景、四空间label；选项作全部2/6/24排列，sample-wise robust要求所有排列均正确，不是普通prompt均准确率。55个BSTF case来自7个模型，故意选binary robust=1且新增空间选项使ternary跌至少80pp；九模型全面观察与55高脆弱case诊断不是同一人口，另两模型未过此阈值不等无bias。无关词替换保持同模板/排列负担，选项空间语义效应仍可能含tokenization/词频差异，不授完整唯一语义因果。

视觉attention只是两例选后可视化，不能据ROI相近证明完整grounding。J每模型从正确行取800平衡训练、按scene分隔于错误eval行，线性probe real/blank分别重取特征并重新训练；峰层macro .998 vs .137是probe诊断，不是base自然使用或信息充分性的证明。Blank同时改变全部图像内容，不将其变成精确语义信息量的反事实下界。

双向last-token整state替换能修/破选项答案，只定位选后人口中的决策相关状态，不映完整circuit或单一知识。K再从空间错、三个无关词对照均对的严格条目每case选首30，按同批平均activation差排top-K，added-option位置清零；同K随机基线有固定seed，但非能量/分布匹配，且best layer/K同人口选择不独立holdout。小case模型仅2–3case，重复排列不变独立scene；不把稀疏杠杆当唯一因果通道或部署安全patch。

L.1另一合成对象对scene-group 80/10/10，单object pair不等仅一张图；81,600训练pair、10,200验证/测试pair、标签和选项顺序平衡，响应是letter而非自由rationale。vision/projector冻结，只LLM attention/MLP LoRA（r8/a16/dropout.05），每模型3seed、一epoch、AdamW3e-5/effective batch16，监测letter KL和各方向退步早停。模型权重BF16，普通SDPA/干预eager，greedy最多8新token；解析失败回首步合法letter logits，不能称原生成文本全合法。GPU/并发/完整时延未披，不补SLO。

T2更强four-way robust常改善，但Qwen2-VL2B/7B、InternVL2-1B若干public binary切片有反退，binary基线近满分也可跌；不授全任务无损。冻结视觉后LoRA有效不唯一证明原错误只在语言侧、更不证明没有新视觉关系学习，作者自己承认修复非唯一机制证据。全部排列/反事实forward、probe训练/选层、activation驻留/干预、LoRA与跨任务质量回归均付费；不复制完整DPO教程或推荐永久清零。

## actual owner与原单段PRE提案

唯一 `MULTIMODAL-REPRESENTATION` Ch23。实际现开头“视觉答错还应分开…”完整段已有probe可读不等使用/不能只升级encoder，且限定局部attribute；音频06854的差分读出不是空间选项干预。具体缺口是同图/同题下选项语义扰动如何引出language consumer诊断，以及受限双向state/稀疏干预与冻结视觉的适配能支持到哪里。只补一段，不在Ch33重写DPO或新建circuit章节；若独核认为旧具体机制已完整承载，可NC，不为diff强加。

拟放在现Ch23完整2610-29241诊断段之后、完整“即使都保留为文本，也应按任务关系选择局部性…”段之前，保原段及marker：

> 可读信息与消费失败之间，还可加入同图、同题的选项扰动：二元判断稳定正确，加入错误空间词后却总选新项，并不自动说明视觉 encoder 丢了关系。保持选项排列负担，再以无关词、去图 probe 和双向 hidden-state 替换分别检查词面干扰、可读性与决策相关性；稀疏通道干预只给局部杠杆，不映完整 circuit 或唯一因果。[受限空间诊断](https://arxiv.org/html/2606.01914v1#S5)使用故意挑出的高脆弱人口，选层/选通道也可能过拟合；冻结视觉后仅适配语言侧能够修复部分错误，仍不证明视觉接口已经充分或新知识未被学入。更严格的全排列通过率不是普通准确率，部分公共任务切片仍反退；全部对照、probe、驻留、适配与质量回归计费。证据、干预或预算失配时，保留原图、原模型和独立关系核验，不仅凭attention图或一次修复就决定扩encoder、永久剪通道或签发空间正确性。<!-- source-family:SF-2026-ARXIV-2606-01914 -->

本人true-H2注待首次必要/score/actual-owner/PRE与root fresh窄授后再真实写。本项未I/POST/DAY，下一01600未必要；不能从本包存在预减日级/候选计数。
