# Latent-WAM24581 必要Source与已有覆盖

root 实际复核：复用已核完整题摘/决定接口及日门，本次实际核 exact-v1 §3.3–3.5/§4.1–4.3/T2–6 与 live Ch25 1006–1046 的完整 training-only future objective→删除预测接口→轻量forecast→pixels/closedloop取舍；训练future/ego监督不等运行期imaginedcontrol，compression/geometry/stride局部反退及训练费保留。具体已有覆盖成立，6标准处置通过，Books0无需POST；不授DAY。

root有限决定接口准入通过；日级26原字段NEXT_DATACITE。拟2+2+2=6标准，窄命题是training-only未来latent/ego约束与部署只encoder/decoder的替代路径，不用futureprediction名称倒推部署imaginedcontrol。

实际读[v1](https://arxiv.org/html/2603.24581v1)§3.1–3.5/Eq1–6、§4.1–4.3/T1–6。DINOv2patch压16queries/view/frame、WorldMirror几何feature对齐；frozengeometryteacher可预缓存但生成/存储费用不免费。historyscene+ego interleave，causalDLWM预测EMAencoder futuretarget，futurecommand/velocity/acceleration辅助监督；teacherforced上下文与部署当前history分开。trajectoryquery读当前worldrepresentation依command选轨迹。§3.5runtime只SCWE+trajectorydecoder不保DLWM、egoauxdecoders或geometryteacher；不能把geometry teacher纹理feature当metric真值或线上模拟器。

32A100/100epochs/globalbatch512/约2day、BF16，inference104M/train191M其中trainable104M；3views224×448/T4/hidden256。NAVSIMv1/v2分别非同构指标，不拼成safetytruth，HUGSIM436scenarios zero-shot无需再finetune但不是实路闭环安全。§4.3compression alone87.7比base87.9退，geometryconcat88.0低于无geometry88.3、distill89.3，Base-LoRA68.5明显退；这些局部配置不能证明LoRA永远不能几何distill。stride2密target89.1低stride4 89.3，增加监督密度不延长相同8frame horizon。difftraining/config/referencebaseline和模块增量不能授universaldurability/省全部费；没实测全部署latency，attentionmap只是可视化非内部因果证明。

## concrete NC

Books公共上下文/Ch24与26交接已核；MULTIMODAL-WORLD-MODELS Ch25实际1002–1036完整trade-offs明确training-onlyfutureobjective塑形worldtokens、移除预测分支只policyrepresentation、不提供runtimecounterfactual、train–servegap/额外训练coupling和WM仍适用分支。414–430包括DynFlowDrive部署去WM/全候选训练费用与未授safe。它们实际承载本次采用的训练/部署分责；Latent-WAM是本地驾驶表示配置的新验证，有限geometry/stride差异保报告，不需要新长期推理接口。具体已有覆盖而非因同主题跳过Source，Books0无需POST。

待root实际必要Source/owner独核，不授DAY，未核artifact/复现。
