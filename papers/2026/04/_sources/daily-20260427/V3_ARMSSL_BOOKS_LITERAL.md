# 2604.22550v1 ArmSSL：Ch72 条件分支写前提案

这只是作者供 root 独立采用判断的材料，不是 Books 实写、写后复核或整日 Gate。[apr20 的必要源→owner 审阅](V3_APR20_ARMSSL_INDEPENDENT.md)支持恢复候选与窄缺口；是否采入仍须 root 判断。日期依据与受限原始字段见[本日筛选记录](V3_SCREENING_NOTES.md#同类泛化排除理由的第二个具名漏收260422550-armssl)。

**Owner 与位置：** `PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)“Extraction Budget 必须跨身份聚合”一节的 watermark/canary 回退之后，或其下一段 model-theft 审计前。现文把 watermark 留作辅助 sensor，但没有将被验证资产（encoder）、后续适配层（classifier）和验证者实际可见输出（embedding 或 confidence vector）绑定为同一模型归属检查身份。它与上方生成内容 provenance watermark 不同，不应插入该处混成一类。

**拟正文：**

> 对可被盗取并适配到下游任务的 foundation encoder，模型归属检查还取决于服务暴露的观察接口。直接提供 encoder embedding 的服务，与只返回下游分类置信向量的服务，不能沿用同一个探针与阈值；后者需要在只有 black-box confidence 输出时用匹配的 clean/trigger 探针对比，且把 encoder revision、下游适配和查询协议一起记入验收身份。这个统计信号只为调查提供证据，不能替代发行记录、授权链或法律权属判断。<!-- source-family:SF-2026-ARXIV-2604-22550 -->
>
> 水印若在表示空间形成可分离的 OOD 密簇，还会向攻击者暴露定位或移除的线索，因此“检测得出”与“难以被对手检测”须分别验收。分布纠缠、表示对齐和干净 encoder 参考约束可在两者之间做受限折中，但会增加训练、阴影样本和迁移验证成本。主对照多为冻结 encoder 后训练下游 head，不保证任意 full fine-tune；64 个负例中的零误报不是总体零，受控自适应移除仍能以效用损失换掉信号。接口不满足置信向量/匹配探针条件或攻击超出已测范围时，应保留 inconclusive，回退访问控制、跨身份查询预算和人工调查，而不是由 watermark 分数直接认定盗用。

**来源与反证：** [官方 exact-v1](https://arxiv.org/html/2604.22550v1) §III-A–C/§IV-A–C/§V-A–G/§VI；[独立有限审阅](V3_APR20_ARMSSL_INDEPENDENT.md)已指出 MLaaS 黑盒验证并非该文首创（SSL-WM 先例），本项可采的是**验收接口与 OOD 攻击面的条件性分账**，不是 ArmSSL 的普适鲁棒性或法律归属保证。正文中的“把 revision/适配/查询协议作为验收身份”是本书工程推断，不声称作者验证了该发布控制。
