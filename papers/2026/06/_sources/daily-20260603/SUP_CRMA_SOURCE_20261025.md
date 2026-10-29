# 00382 CRMA：受限必要审阅 / 五分 / 仅报告提案

仅Jun03补Jun02。当前AGENTS/Research/Report/Sources适用分组/统一入口/ROADMAP及本日停点按恢复读取。R26/28完整题摘/准入/联合日期有效复用：v1 May29 21:50:23Z，精确DOI `10.48550/arxiv.2606.00382` 的arxiv.content/findable/registered Jun02 03:50:12Z与适用日程共同限定Jun02 BJT；非submitted直接归日。当前[官方abs](https://arxiv.org/abs/2606.00382)唯一v1，明确专利待披露/companion report in preparation，所见无撤回信号；HTML封面April只是作者文稿日期，没有实际更早公开渠道线索，不扩假想日期追索。

实际读[exact-v1](https://arxiv.org/html/2606.00382v1)§3–5完整公开构造与省略、§6.1.2–6.1.3/T4/6/7及§8.1限制；未核完整QA面板/附录pilot、全部图像素/匿名实现/复现。充分判断可公开支持的命题后停止，不追未披露专利或完整训练曲线。

公开部分把理想非负双随机M的谱范数≤1归于Birkhoff凸组合，线性M这一局部命题成立，但并不约束base/LoRA或整块Jacobian。有限Sinkhorn轮次/容差、stream结构、非线性、readout/gate、残差blend、nearidentity初值及CRMA训练配置**均明确省略**。因此不能从M推导完整residual adapter非扩张、任意训练步无遗忘或当前实现精确双随机；标准residual相加本身甚至不保同一谱界。§3.4说完整adapter经验验证，§5.2实际描述instrumented层的mixing transformation均值、每五步记录867点，不是完整Jacobian/所有layer所有step证书。§5.3“不可能朝覆盖旧任务漂移”的强解释不由该局部界成立，本次不采用。

§6.1.3自己承认大部分忘却改善来自每task独立LoRA，FROZEN已给主要隔离；相对NAIVE共享LoRA的大差额混合模块化和CRMA。T7三seed Mistral7B/5域各500train/100holdout，MODULAR相对FROZEN NLL平均改善约1.99%，但仍是整体bundle，组件细消融待未来；T6单次4域也有Medical/Finance的MODULAR holdout差于FROZEN，不授各任务均优。T7的FROZEN drift非零与“zero by construction”字面口径不一致，保原表，不自行修定义或签严格零遗忘。三seed的参数t检验和排列检验不同，作者已述小样本限制，不把不重叠区间当普遍显著性。

§6.1.2 Gemma9B五阶段后MMLU−6.46pp、修评分后GSM8K仍−10.2pp，作者未做净组件归因，不能把保旧域loss写成全部能力保留。所有保留数字依赖路由正确；31题centroid全对不证明重叠/OOD路由。QA由first-author单人非盲评分且题少，无published CL head-to-head。A10080GB/LoRA16alpha32/all-linear/3epochs/batch2、D1 LR1e-4/后3e-5只对应主Gemma配置，不移给全部T7；CRMA特有配置/完整precision和卡数、router/adapter驻留/交换开销、真实throughput/SLO未闭，未授production。多adapter与共享state、Sinkhorn/路由、全部训练/搜索/回归费用保留。

正式Design Delta2 + System Reach1 + Durability2 = 5：拟核增量是可继续更新的共享adapter基底与per-task参数隔离的取舍，不给一般双随机数学或大headline加分；不因专利/访问或仅报告降分。

实际读[Ch17多流几何完整组](../../../../../books/part-02-model/17-transformer-layer.md)与[Ch30](../../../../../books/part-04-training-system/30-lora.md)持续适配/冻结控制的完整段及“从持续改写共享权重到可检索的临时参数更新”完整组，Ch29/31交接职责有效复用。现有Ch17已经解释局部M界、差异可能抹除、完整Jacobian不同及有限Sinkhorn；Ch30已有冻结/模块分责、旧能力与task顺序/路由须另验。未披露的新共享基底组合无法独立说明其完整机制，也不能用有限bundle结果补造成可执行设计。

故拟**仅报告——关键机制未披露**，保可核公开数学范围及受限作者结果，不新增Book/PRE/本人注。不是将整个论文排除或访问故障/暂缓普通待办，也不采未证明的整pipeline/无遗忘结论。未来companion report实际公开且补齐blend/readout、训练与匹配组件消融时，定点重开该家族必要机制与Books判断，不要求重跑全日。当前首次必要/五分/仅报告仍待非writer核，不预采用或DAY。


## root实际采用（2026-10-25）

R161独立标准必要/正式五分与仅报告已实际采用入本日六节；中心桥未证、测量对象差额与FROZEN漂移冲突明确隔离，不能由Only支持正面机制/整pipeline/Coverage。无Book/PRE/注/POST/I，具体重开条件保留；未DAY。
