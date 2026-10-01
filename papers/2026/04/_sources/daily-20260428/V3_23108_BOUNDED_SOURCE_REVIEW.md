# 2604.23108v1 异宽 MoE 有界证据审阅（日期／Books 未过 Gate）

窗口仍为 `[2026-04-27 09:00, 2026-04-28 09:00) +08:00`。继[作者贡献提案](./V3_TWO_MOE_CONTRIBUTION_OWNER_TRIAGE.md)和[root 有限 source→owner 复核](./V3_ROOT_TWO_MOE_OWNER_INDEPENDENT.md)后，本页重开[官方 exact-v1](https://arxiv.org/html/2604.23108v1) §3.1–3.4、§4.1–4.2/Tables 1–6，并对读 [Ch21](../../../../../books/part-02-model/21-moe.md) 的参数/执行预算、动态 expert 集合和 router→placement 交接。当前[日期组合](./V3_TWO_MOE_DATE_PROPOSAL.md)仍待非作者确认，不计正式分母、评分或 Books。

真正的新选项是把 expert 按不同 FFN width 分组、先选 group 再选组内 expert，而每 GPU 放一套跨所有宽度组的同编号 experts。这样可让每个 GPU 的**静态参数组合**相近；动态 token 工作量平衡还依赖组内路由频率，作者另用 group-size penalty 与 intra-group balance loss 来调路由。Ch21 当前已将总/激活参数与真实 dispatch/placement 分账，也有每 token 动态计算、topology-aware replica 等机制；但未具体表达“异宽 expert 的结构选项必须与每设备跨宽度组合布局及组内负载一起规划”的联合设计。主 owner 是 MODEL-MOE/Ch21，Ch36 只交接训练 EP，不应把模型 router 直接当 runtime placement owner。

证据边界：Table 1 的 MoE-3B 3.3614B total/0.376B activated 对 MoHGE-3B 2.821B/0.295B；14B 行亦同时变化 total/activated 参数，不能把七任务分数归因于“同等预算下更好 router”。Table 2 有异任务时延反向与 Dense 更快情形，不支持普遍低延迟。Table 3 给的是八 GPU 的 token-route **比例**近均衡，尚未报告逐 GPU FLOPs、HBM、collective、利用率或生产尾时延；all-size set 只保证各设备静态 width 组合对称，实际工作量仍看请求负载。Tables 4–5 的词频／训练 perplexity 是 token 难度 proxy，不是独立标注的认知难度或证明 router 识别了语义任务难度。Table 6 的 GPU Utilization 列仅 `balanced/unbalanced` 类别，不可补造实测利用率百分比。

若有界日期复核通过，贡献分可暂拟 `2+2+2=6`；真实 Books gap 将按合同触发深入必要审阅。拟在 Ch21 现有“Total / Active Parameters 只是约束坐标”到 router/placement 分权链内，加入一处短条件分支：异宽 expert 的质量/参数预算、跨宽度设备对称布局和动态组内均衡分别拥有何种责任；用受测静态组合、token-route 比例和真实 FLOPs/时延缺口分别验收。保留同宽 full-width expert、固定 placement 与普通负载均衡作为较简单的条件旧方案。日期、root 写前裁决和共享 Ch21 锁前，不修改 Books，也不记 Integrate。
