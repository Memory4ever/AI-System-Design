# Visual Injection 29418限定owner判断

原[精确v1](https://arxiv.org/html/2603.29418v1)Source6/正常日门复用；不读攻击代码/有害target或重跑机制。作者actual Ch72 16–42/75–90：外部image/模型输出不继承主体权限，trigger visual/semantic邻域分别测action propagation和benign utility；prob/像素sensor不是release证明，跨步读实际effect而不是standalone偏移，视觉attention高分/干预又不签语义恶意或功能保持。

拟采用仅是这些已有具体边界：source image中小pixel变化/clean画面不获可信来源资格；生成目标的文本响应不是下游action真实effect，sensor和效用必须配对验证。具体NC **PLATFORM-SECURITY / Ch72**，不是声称latent/text-image攻击构造及全部机制已写书。该构造仅作为受限压力观察保报告，不采用新recipe/危害实现或全防御结论；当前没有提出新的可复用判准/防守接口替换上述边界，局部优化目标与数据配置不需追加安全段。

真实评分 `2+2+2=6` 保留，来自source-image到生成consumer的受限跨模态取舍，不因NC降分。必须保四API snapshot/seedCI/hardware/费用未披露、surrogate白盒而非零access、caption/VQA人口各100、扩1000仅三个模型、Claude hard7/2低成功反侧。Hard文字称exact但实际semantic score>.3、soft以victim目标caption作reference，循环性不升级tokenexact；Table5 hardASR与AvgSim不同，full.339低于去text.348/去update.351，不宣唯一双对齐因果。全部制备/优化/模型求值/独立检查计费，未核代码/复现/真实行动。

交reader独核上述限定采用层。若认为source图像→consumer分责本身有新的长期差额，只重开这一owner理由，不重Source/日期，也不靠安全标签免去本材料判断。
