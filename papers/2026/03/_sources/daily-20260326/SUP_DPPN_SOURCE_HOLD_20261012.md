# DPPN22858 exact-v1 — 具体中心争议

作者supp_mar26_fresh，2+1+3=6/date25已reader准入校准，不因疑难降分或贡献删除。实际必要HTML §3、§7–10、§12/Eq13/Table3/5/6；因abstract与正文seed/增益口径不一致，定点读取同exact-v1 PDF的§4.3–4.4、§9、§12/Table5–6 (p8/13/18–19)，不是无差别版本比对或附件遍历。原始：https://arxiv.org/html/2603.22858v1 ，https://arxiv.org/pdf/2603.22858v1。

## 已知而不能进一步采用

reset全部模型weights、只保存slot-transition pheromone再warm/cold训练，确实将坐标对应和forward/LR消费者分开；fixed Fourier用同seed/位置有稳定索引，含tokenid重新引入surface依赖。routingbias十seed没显著positive不证明零迁移或所有learned坐标必不稳定。有限synthetic motif/4目标、单H100/bfloat16、训练/对齐/统计与复训费用不能推出大模型长context普适机制。

中心链存在三处具体未闭合：

1. §12 Eq13为 `eta_base*(1+lambda*(tau_ab-mean))`，紧接例子却用tau/mean得到1.71/0.29；低prior也低于base，不是叙述『错误prior仍以base学习』，λ/非负guard的可执行含义没有被本句恢复。正文实验与统计确实能形成候选，不把不完整mapping当实现已验。
2. HTML/PDF Table6 extrinsicP的A2 .007、random .005，其difference为.002，但Trained−Random行A2印.013；C1 .016−.009=.007，difference行印.000。叙述samefamily .006–.013 / differentfamily indistinguishable无法从这些公开表中一致恢复，不自行改表后称结构收益已证实。
3. 官方exact-v1 abstract页面称17seeds/p<.05/+.003，actual HTML和PDF协议/Table5却7seeds、均non-significant；HTML abstract还写neverreduce，§12均值non-negative不等每seed不负。不是普通7vs10配置对照，而是支撑『graceful transfer』与完成数值身份冲突。

具体中心主张（坐标稳定＋graceful消费者足以结构迁移、trained-completion排除随机regularization）尚无一致证据。将它缩成『保存状态需identity』『已有bias不能授保证』只是成熟原则，不能假借本篇分数写新机制。因此暂缓Books，不提出新正文，不签显著positive、necessary/nojointlearn全称、zero-negative guarantee或安全/性能保证。

## Owner判断与定点恢复

Ch22现有state identity、persistent state/KV与模型memory论证保留，不足以承载本篇尚未可靠的结构prior新验证；不把主题相似写已有覆盖。主线潜力与6分仍保留，终态采用隔离而非排除。重开需要作者更正或可核exact-v1原始对照/同seed定义、Table6四目标的trained/random成对结果、Eq13实际mapping/λ范围与非负处理，以及abstract17seed与正文7seed关系；已有可读同PDF不重复请求。只重开本family和依赖结论，不扩全学科或未来修订队列。

请非报告作者复核这些原位置、算术和必要负侧；未获独核前普通工作仍可执行，不伪称外部终态已获验收。
