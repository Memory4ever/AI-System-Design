# τ0-WM：被评价的动作与重新提出的动作

仅06-03补Jun02自然日，R62完整v1题摘及联合日证有效复用。实际打开[exact-v1](https://arxiv.org/html/2606.01027v1)及[当前官方事件](https://arxiv.org/abs/2606.01027)，所见v2 Aug23不倒填，未见撤回提示。当前合同/ROADMAP/Books上下文有效；本次实际必要III–VII/Alg1–2/T1–2和直接A/B部署/缓存条件，不读代码/所有引用或图像像素，不复现实机。

## 必要机制与直接反侧

27.3K小时由17.8K实机、6.5K UMI、3K人类视频组成：实机动作与目标控制接口最匹配，UMI动作样信号只是弱对齐，人视频只训练video loss。Mask声明观察/目标/active loss，不把缺动作标签补成机器人动作。Wan5B视频骨干+0.5B action DiT，观测clean/未来加噪；VAM联合提出future/action，ACVS以候选动作条件预测future与reward，二者共享架构/数据接口不据名称补成一个权重对象或独立真值。

VI/Alg1先采N个action，按K个随机flow timestep重新加噪后的平均重去噪误差取负作为RCS。它测与所学条件分布的自一致，不是成功/安全校准概率，所有候选也可同样差。若最好分仍低于γ才让ACVS评价所有候选，以预测reward轨迹的最大进度取最高future；不是累计return或最坏碰撞证书。LAR再将该future转条件重新调用VAM产生新动作，**不是执行原被ACVS评价的动作**。项目推论：旧候选的评价不能静默升级为新生成动作的验收，仍需controller/真实反馈；原文未给完整新动作再模拟/独立安全门实现，不补造。

Reward来自subtask切分/成功进度与失败段负标签，不是物理观测真值；共享backbone/训练来源有相关模型误差，最大预测进度偏好也可能漏阶段中危险。VII四任务/三本体主要有限成功率，Faucet仍难；将后续额外压紧行为归因future只是作者假说，非固定policy因果实验。T1 Robot-only对完整mixture同时加UMI+Ego，未隔离二者或总数据预算，不授人视频单独因果贡献。T2两task各20次、禁retry、每decision默认4proposal；无TTC .43、RCS .50、加LAR .60的mean只本条件，不授显著普效。CFG/ACG反而低于直接执行是反侧，额外TTC也未给完整成本匹配。K、阈值校准/风险曲线、训练重复/置信区间与完整质量分母未披露，不按表值补造。

A global batch12288/384、AdamW5e-5、30长度chunk；单RTX5090标准约220ms/query，缓存文字约180ms，compile约140ms却可能变采样数值且主结果不用compile。没有明确把4proposal、K次复噪、条件触发的全ACVS+LAR、感知/传输/control等待全部绑定到这些延迟，不签完整deadline/平均或tail SLO。精度/完整并发未披露；不能把训练共享或复用clean context的KV推广成生成未来在任意去噪步不变。数据制备、双接口训练、全部候选/重评分、rollout、再生成及独立质量/控制回归都计费。

## 评分与actual owner

正式拟2+2+2=6，原AB暂拟7=2+3+2：本次采可生成/可评价的两消费接口及重新提案后的证据身份，不借训练→推理→控制的一般全生命周期常识给Reach3，不因工作量/Books处置降分。唯一owner从题摘Ch25修为`MULTIMODAL-EMBODIED-VLA` Ch26：此增量是模型生成动作的消费/控制接口，不重写Ch25泛世界模型或Ch27数据配比。

实际Ch26 World-action完整开头与三种interface、近期shared-mask/data监督组、Future-to-Action/控制时钟交接已读。原文已承载joint模型有相关错误、future非真观察、controller拥有执行、无动作video不计action loss，不把这些重复作为新gap。具体差额是廉价re-denoising选择→条件触发昂贵future评分→重新生成动作的不同身份及费用；当前未具体承载该两级消费者链。拟在现三种interface code block之后、完整“这些接口也可以共用一个backbone…”段之前补一段；若独核找到具体充分承载，可NC，不强改。

> 具备动作提案与未来预测接口后，还可把测试时预算分成两级：先对多个action候选重新加噪，按模型能否恢复它们的误差排序；只有自一致分不足时，才对候选模拟未来、读预测进度，再把选中future作为条件重新生成动作。[受限τ0-WM分支](https://arxiv.org/html/2606.01027v1#S6)中，自一致不等成功概率，最大预测进度也不是碰撞或整段回报保证；更关键的是，重新生成的动作不再是先前被模拟的那个候选，旧评价不能直接继承到新提案。两任务少量实机尝试支持局部收益，未校准的阈值、共享模型误差和未绑定完整TTC的局部延迟仍限制放行。采样、反复评分、全部rollout、再生成和控制验收都付费；新提案、证据或deadline不合格时，保留直接policy、短chunk真实重观测与独立controller，不让高分future代签动作安全。<!-- source-family:SF-2026-ARXIV-2606-01027 -->

当前首次必要/评分/owner与原单段PRE待独核，未改Books/注或预I/POST/DAY；必要支持与直接反侧足即停，不为全部未知扩附件。
