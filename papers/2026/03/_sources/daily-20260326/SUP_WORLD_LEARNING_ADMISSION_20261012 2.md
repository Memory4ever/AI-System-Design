# 03-26 World/Learning有限准入

对应 SUP_WORLD_LEARNING_ABSTRACT_DATE_20261012.json 十二完整exact-v1题摘；官方流程最早25BJT＋同ID/findable25上界日级夹逼均成立；不把官网Submitted显示作为公开证明。全为潜力候选，评分对象只拟证的新命题，Source/Books普通待办未通过不称完成。

| exact-v1 | 原有约束 → 增量 → 重新考虑的选择 | 拟评分/唯一owner |
| --- | --- | --- |
| 23355ReVal | 昂贵fresh rollout一次即弃 → Bellman step internalconsistency+terminaloutcome/replay → 从policy-only更新转受验证Q学习替代分支 | 2+2+3=7，TRAIN-PPO Ch32 |
| 23198Sparse | unstructured稀疏通常不兑现dense pipeline效率 → sparse packing与CUDA配合L1形成高稀疏 → 格式/kernel是否能实际消费稀疏而非只零化参数 | 2+2+3=7，INFER-TENSORRT-LLM Ch49；MLP形成仅交接不重复写 |
| 23497WildWorld | pixel-level actions掩盖潜state → 帧同步action/state/skeleton/camera/depth与两独立评价 → statealignment不等framequality/actionfollowing | 2+2+3=7，MULTIMODAL-WORLD-MODELS Ch25 |
| 23491Foveated | uniformtoken成本忽略已知gaze → 从highres构造mixed-resolution训练/采样 → spatial预算能否按观察者条件动态而非全图压缩 | 2+2+3=7，MULTIMODAL-GENERATIVE-PARADIGMS Ch24 |
| 23481VTAM | contactstate视觉不可辨 → videotransformer迁入tactile与attentionbalance → crossmodal占优和forceaction条件一起验收 | 2+2+3=7，MULTIMODAL-EMBODIED-VLA Ch26 |
| 23462RealMaster | 显式engine控制与视频写实分离 → 几何条件anchor propagation产pair后ICLoRA蒸馏，无anchor部署 → target合成流程与部署条件不能等同 | 2+1+3=6，Ch24 |
| 23413I3DM | cameraFoV检索对occlusion不够 → FF-NVS特征评分/implicitwarp/可靠区域注入 → historicalview匹配与targetview对齐应分开 | 2+2+3=7，Ch25 |
| 23376ABot | likelihood视觉真不等physical → decoupledDPO discriminator与actioncontextblock/独立物理vs动作评价 → quality与physics不能被一个总分替代 | 2+2+3=7，Ch25；DPO目标仅必要交接 |
| 23326ViBe | highresimage直调video发生modalitygap → 两stageRelayLoRA分开模态/分辨率，部署只保高res适配 → 训练适配和交付组合不能同一选择 | 2+1+3=6，Ch24 |
| 23246GORenderer | appearance拟合与viewcontrol互约束 → 3Dproxy条件视频diffusion分担几何/材质 → 潜在新控制接口还是常见模块组合待定点S3判断 | 不预评分；贡献决定接口未明，普通待办 |
| 23202Gaze | attention与任务细粒度不对齐 → aggregatedgazepatch分布KL监督不新增部署通道 → 训练prior与实测实时输入/解释可信分开 | 2+1+3=6，Ch26；noeyetracking/热图来源需必要核验 |
| 23132InterDyad | 两人reactive视频不能只lip-sync → motionprior/MetaQuery桥conversation intent timing+RoDG → reactive条件和render/identity/lip指标须拆开 | 2+1+2=5，Ch24；贡献是否仅模块组合待首校 |

不照录所有摘要指标或『essential』『无需任意视频数据』『保证物理』；小数据/benchmark本身不决定准入，贡献只按具体机制或边界。ReVal owner/InterDyad准入与GORenderer决定接口请独立校准，未授完成。
