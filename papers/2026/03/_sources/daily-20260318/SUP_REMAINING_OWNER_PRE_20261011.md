# 本18具名末批：实际owner差额与逐字PRE（未授权写入）

作者resume_mar18。必要Source与反侧见SUP_EVIDENCE_TITLE_COMPLEMENT各唯一family；18项首arXiv日级夹证与准入独核有效复用。本文件只保存具名拟稿，不授Source/Books/写锁/POST/DAY。Books公共上下文已实际加载，现正文与邻接已定点读；不改LS/索引或其他family。

## 15271 Flash-Unified：唯一INFER-TENSORRT-LLM / Ch49

实际529–547讲calibration objective、batchgeometry/noise-clock与artifact；Ch24 821讲跨模型生成capacity阶段但不拥有同weights任务mask。拟在Ch49现537 noise/time calibration段后、539局部结构惩罚前加入仅一段；不重复生成solver/头cache/视觉tokenprune。root/reader若判现文已充分承载，可具体NoChange，不强造diff。

共享同一组理解/生成权重，也不要求两种任务交付同一个稀疏路径。一条受限分支按各自 activation 人口制作 FFN mask，仍保留完整权重：理解消费自己的静态路径，生成按已校准的时间阶段在完整与裁剪路径间切换。逐神经元干预的任务敏感度诊断，与实际 weight×activation 剪枝评分应分开；首张生成图和少量理解样本不证明神经元对所有任务永久专用。Mask、任务模式、校准人口、生成时钟及 full-path fallback 共同构成 artifact identity，不让共享 weights 隐去两套质量责任。[有限 unified-model 对照](https://arxiv.org/html/2603.15271v1)仍有理解/生成质量退步，部分组合还同时输掉质量与速度，不采“正交无干扰”或 training-free 等于零校准。双路径驻留、校准、切换与实际 backend 都付费，平均 latency 不授服务 SLO；模式或人口失配时回完整路径/保守裁剪，生成阶段接口继续由第24章验收。<!-- source-family:SF-2026-ARXIV-2603-15271 -->

## 14948 WorldDrive：唯一MULTIMODAL-WORLD-MODELS / Ch25

实际357–375是显式imaginedrollout；953–965是训练期future塑形/部署移除predictor；Ch26 443–469的teacher/directpolicy等不拥有该worldforecast-to-critic分工。拟在Ch25现965 training-only监督代价后、967 Pixels vs latent前加入两小段，不改原训练期塑形分支或动作提交owner。

未来监督还可以把昂贵的候选 rollout 蒸馏为部署期的轻量 forecast，而不只塑形 policy 后删除整个预测接口。训练时让冻结的、按候选 trajectory 条件化的 world generator 提供 future latent target，再由只读取当前 scene 和候选表示的 query decoder 学习对齐；部署不运行该生成器，直接预测候选未来 latent 供 critic 比较。Teacher 未来和部署预测是不同对象，query 输出仍是 learned belief，不是真实未来或候选动作可达性的证书。<!-- source-family:SF-2026-ARXIV-2603-14948 -->

这种分工把在线逐候选生成费用移到 teacher 生成、偏好标注和 forecast/critic 训练，却留下 teacher bias、候选支持域与 critic 校准风险。[受限驾驶对照](https://arxiv.org/html/2603.14948v1)只支持所测 NAVSIM/nuScenes 和设备上的局部取舍；oracle best-candidate 是 ceiling，部分安全代理或生成指标仍退步，跨 pipeline 平均延迟不证明预算匹配、物理安全或 tail deadline。真实 observation 仍拥有状态真值，controller 仍拥有动作提交权。预测或评分漂移、环境反应性超出训练支持时，保留显式短 horizon rollout、真实反馈刷新、direct policy 与独立安全 controller，不让更便宜的 latent forecast 静默替代它们。<!-- source-family:SF-2026-ARXIV-2603-14948 -->
