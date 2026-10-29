# 00515：语义提案与接触端能量合同

## 首次必要证据与边界

仅06-03补Jun02自然日，当前AGENTS/研究和Report合同、Daily来源/Prompt已重读；ROADMAP/三Books约束及actual Ch26与Ch25/27交接已读。R62完整题摘和Jun02联合日证复用，不重抓日期或搬原候选。[精确v1](https://arxiv.org/html/2606.00515v1)本轮实际读§3–5、§7限制、Appendix A全部假设/定理/证明、B.1参数与B.3资源；未看图像像素、全B.2/B.4–6、代码/真实机器人或复现。[当前官方事件页](https://arxiv.org/abs/2606.00515)实际开，v1 May30、v2 Sep18，所见无撤回/勘误；仅用v1，不以当前作者表/后版变化补旧事实。

正式评分提案2+2+2=6，非原题摘8=3+2+3：实际增量是把经典admittance/tank接成VLA提案无关的提交接口，不是新创passivity基础理论或所有物理安全结论；跨语义/低层控制与有状态能量预算，稳定接口价值足够，不把借用原理计D3/Dur3。原拟8留作准入过程，不修改任何已有正式候选旧评分，也不因已有覆盖/工作量降低分数。安全合同受影响域仍深入以下必要证明与反证。

## 机制及保证到哪里为止

VLA只提出binding/stage/recovery/diagonal M-D-K schedule；finite/fresh/timing/binding/context gate和独立wrench governor选出候选，投影先clip合法box、提高阻尼或降低正质量跳变满足sampled margin，tank再限制正质量/刚度增量，只提交shield后的schedule。无效/陈旧时换有限recovery并暂停stage，不让模型confidence取得actuator权。

Appendix A证明对象是sample-and-hold对角接口的storage加tank：A1–6要求合法旧schedule、正mass/damping和可行margin、有限且被envelope涵盖的state、固定参数sampled residual、实际可用的非负damping credit及有限recovery/终止。两端box凸性/affine margin保插值；正参数跳变以envelope上界计费，tank扣款与先前damping credit抵消，得到带数值残差的storage不等式。它不消去未控制residual，不自动给峰值force、耦合contact、actuator饱和或任意plant recovery保证；zero sampled violation也不是开放环境全轨迹安全。这里仅核采用的有限证明，不把已定义residual当实机已标定。

直接反侧：T1 PaCo任务成功最高但safe .953低于rule 1.000；同为0 sampled margin violation的不同controller仍有不同任务/安全表现。T2 stale .986、random .792的safe也非恒1，说明proposal-independent端口证书不等整个任务安全。反事实semantic控制虽同shield且成功差明显，语义能力归因仍限相应绑定/任务人口。真实fixture仅每种10次，共30，另EV8/15不是同一统计；不以小样本或跨直接policy不同预算的表拼普遍胜负。B.1 shield250Hz/proposal50Hz/camera10Hz、timeout/freshness/tank参数是本实验，不当部署默认；B.3仅neural evaluation用2×4090/OpenVLA BF16，低层loop不用GPU，不由模型吞吐认证control deadline。训练/推断、state/wrench校准、projection/tank、logging与真实执行均付费，终止/接管仍独立。

## actual owner：具体已有覆盖提案

唯一 `MULTIMODAL-EMBODIED-VLA`，Ch26约1848的“Passivity Shield把语义Proposal与Contact Authority分开”三完整段及其直接前后均实际读：

1. 首段从低速自由空间直接指令的合理性推到陈旧输出/时变schedule注能，明确单独裁joint/force不足以解释能量约束。
2. 第二段完整承载semantic/stage/recovery与diagonal proposal→finite/fresh/context gate→box/margin→tank interpolation→唯一admittance提交链，以及无效/陈旧recovery、stage停止和独立governor，不是只有主题名。
3. 第三段已将证书限定sampled diagonal residual与connector任务，保投影保守性、校准/tank/切换成本，明确不授peak force/coupled contact/saturation/全部plant recovery，失配回verified controller/停止/接管。没有在正文采用无需残差的完整物理安全或表格普遍优胜。

前方常态限幅与显式干预分责，后方有状态安全提交/计划版本与deadline交接也保持。因此本次可支持的长期机制和关键边界已有实质正文，提议具体No Change；不据同family marker宣称旧事件已审重复，不增I、不新写正文/本人注或要求PRE/POST。必要证据/6分/具体NC仍待唯一非writer首次核，本日未DAY。下一01914未必要，Agent/Multi余15在本项通过后再行政确认。
