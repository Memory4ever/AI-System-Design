# AGMARL-DKS：exact-v1决定范围/贡献的必要core

mar14_supplement准备，03-14只补Mar13。SUP_FINAL_NARROW7.md保留latestv4题摘与actualv1身份差别；本判断只用SUP_CORE_STOP_12031.raw官方2603.12031v1 GET200373444B/2026-10-10T03:45:45.862671Z，首稿是单作者Hamed Hamzeh的AGMARL-DKS，不倒灌Agentic-Kube v4三objective-agent/QMIX/plurality/1000node/17ms。日级夹证见精确SUP_DATE_STOP_12031.raw.raw，仍待非准备者核，不用Submitted单独当公开。

实际完整题摘B1–10、§3.1–3.3必要B63–182/193–250（state/action/reward、GNN、hybrid lex、既有MADDPG更新/全Algorithm1）、§4–5 B252–303部署/工作负载/比较入口及§7 B327–329。未读剩余全部结果图、引用或代码，未复现。核心已足以决定实际增量，不以完整文件缓存存在要求所有表/附件。

拟贡献前EX，无评分/Books：实际新配置是一般Kubernetes CPU/内存pod placement中，用节点actor预测FT/UTIL/COST三分数、按stress切换既有lexicographic priority并逐层保留近最优候选，再由中心extender选择node。§3.2.3直接给high-stress [FT,Cost,Util]与normal [Util,Cost,FT]例子、乘性容差δlex及最低index tie-break。这是明确的局部机制，不因“Kubernetes”/MARL/模块数量本身排除；但本稿未把它连接到模型训练/推理工作负载的状态、GPU/通信/SLO或模型能力机制，也未给出改变当前学习/优化理论的重要有效性条件。CTDE、MADDPG、GNN、replay、target-soft-update均明示借用。仅将其类比当前调度/Agent policy约束，不能替代本稿对项目主线的实际贡献。

原文实际压力是4–8node GKE的nginx、stress-ng、busybox、普通batch job、liveness-fail/OOM与NoSchedule taint；不是foundation-model训练/服务协议。资源/容错/费用应用收益本身不足。reward只winning node的三metric prediction MSE+placement bonus，ground-truth也只是定义的node metrics；没有建立新校准定理。GNN用全连接cluster图、共享全局input，后面的actor局部执行不意味着全系统无中心依赖；lex中央选择仍存在。§5/6主要default Kubernetes对照，不认证lex相对matched MADDPG/weighted-priority受控归因；§7自称四state-of-art/A/B，所读实际设置不能拿这句补造四实测baseline。

此EX不是以负结果、CPU而非GPU、小cluster、费时或已有Book覆盖关闭，也不否定一般调度研究价值。决定core读足后，本稿没有被支持的新增学习机制/新有效条件或直接模型系统边界；按当前项目范围停在原始记录。如果非准备者在确切原件发现模型工作负载接口、独立新的learning/optimization命题或影响当前解释的受控反证，只重开该事实及准入，不扩全版本。待独立准入/core校准，不formal。
