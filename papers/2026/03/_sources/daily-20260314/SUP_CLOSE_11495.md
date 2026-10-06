# 11495 Tool-DC：最低评分与关闭判断提案

作者mar14_supplement，root已实际决定core窄P；不因准入自动给5–6或造Books缺口。精确[2603.11495v1](https://arxiv.org/html/2603.11495v1)，五作者/完整题摘/仅v1/Comments17pages8figures在`SUP_ABS_11495`，未识别具体纠错/修订/先稿信号。日级Mar13夹证原件见`SUP_DATE_SECOND.md`/`SUP_DATE_11495.raw`，v1Thu03:30:01UTC与owning/findable registered Mar13 01:56:53UTC；同日上下界规则复用，不以元数据单独作first-public。

实际必要core §3.1–3.3/Eq1–5/Alg1，另已读§4.1/Table1全部Qwen行、Table2训练直接baseline、§4.3/Table3、§4.4/Limitations及A.1–2/A.4必要条件。不会因本次已读更多提高分数：新增是**固定候选目录里S0/topK保留、anchor+disjoint tail的局部分组与最后重选配置**，不是schema validator、重试、parallel proposal或CoT训练这些成熟原理的新发明。

评分提案 **1+1+2=4，已关闭，仅报告**。Design Delta1：它让retriever遗漏的tail在本次分组中仍有被评估机会，改变局部candidate exposure实现；并未给新的可行性/正确选择条件或独立执行协议。System Reach1：固定目录的单步function selector，不外推一般workflow、授权或工具effect。Durability2：保留tail召回机会而不让schema授语义正确性是可复用的有限实现取舍；不借成熟retrieval/validator/teacher原则加分。该打分不是因费时、访问、已有书稿或工作量压池，仍通过窄贡献筛选。

机制边界：S0保topK，另外K组各1anchor+disjoint tail，本地call/null→名字/必需key/type检测→只取有效call的tool definitions供最后M重新选择，非执行commit或独立语义truth；若局部阶段都漏正确tool，global retry不能恢复它。TB改为逐tool singleton枚举，仅最终与GT一致样本模板化rationale；无证据该CoT等真实内部推理。46,897 xLAM派生样本、LoRA2epoch/A800×2/b16，inference vLLM/temp0/max512。评价仅BFCL2501/ACEBench Normal828，随机irrelevant工具扩到20和N10–50；AST exact match不等真实环境outcome，single-step限制明确。Table1 TF在部分子项仍低于TopK或其他策略（7B标准BFCL79.78<80.05；部分TB几乎只比vanilla小幅），不授普遍优胜。Table3 no-Retry退5.26%改变output聚合protocol，不能独立归因self-reflection；Fig7只给多call费用增加，未据此认证生产SLO/全平台低成本。精度/并发/SLO/重复CI未披露，无代码核验/复现。

最低0–4所需身份/日期/重复关系/关闭理由充分。无需Books判断或写入；只保留局部实现/评价上下文，未证它改变长期机制、边界或本书设计结论。为避免以覆盖决定评分，Ch78仅作路由核对：现178–221已有固定目录shortlist与bounded revisable frontier、parallel proposal及独立executor检查，599–636另有集合依赖/多query融合；本稿没有在这些通用约束上改变effect/authority语义。若后来出现独立分组控制、跨目录漏检保证或新执行界，才定点重开该命题。

待root实际评分/处置独核；无需重复全PDF或所有hyperparameter。通过后可正式列当窗候选4分已关闭/仅报告，不能把它当新Books或5分Evidence家族。
