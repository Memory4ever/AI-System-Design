# 12/15 必要局部、反证与条件Books决定

作者Gibbs；以下实际打开exact v1必要位置及当前owner正文，不是全potential Evidence完成。所有潜在家族first-public仍未获授权，均不进入Books、不授实验复现；局部草案只供root在日期恢复与非作者证据核后协调，不冒称整合。Books未写，日期缺口不会被已有覆盖或低分隐藏。

## LLRC：条件整合差额

[2512.13733v1](https://arxiv.org/html/2512.13733v1)实际§4.1–4.4、§5.1–5.2、§6.2及§7.1：原权重冻结，Gumbel-Sigmoid mask学习任意singular values；目标联合compression、两处hidden-state蒸馏和TV。3000 WikiText-2文档、AdamW；后处理阈值0.5，微小压缩层还原dense。无post-compression权重微调不等没有训练。any-k/top-k及fine-tuned LLM-Pruner比较均有限模型任务，后者在Llama3-8B更好；不采全局最优或serving提速。

Owner `INFER-TENSORRT-LLM`，[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)实际1304–1338行：SVDQuant双路径、SoLA保留重要原通道/whitening和同预算rank，贪心代理非任务最优；随后prompt条件动态rank另有执行身份。现有段不承载**冻结原权重、跨层学习mask、蒸馏目标与artifact后处理分责**。相邻Ch48 25–65是draft/target分布验证，Ch50 25–65是request/cache/scheduler，不能把rank calibration误归在线调度。

条件局部插入草案：放Ch49静态rank预算段后、输入条件动态rank前，保留原分支：

> 静态rank也可以由校准学习提出，而不只按奇异值能量搜索：冻结原权重，用可学习mask在压缩预算和中间activation差异之间取舍。mask优化仍有训练及full-rank表示成本；最终二值选择、低收益层还原dense和因子合并才产生可执行artifact。校准代理不是任务最优，参数减少也不等serving变快；分布或kernel不支持时，统一rank、已核静态策略或原dense仍合理。

这是待采用机制草案，后半验收/fallback是作者工程推论；没有确定本窗日期、独立源核和完整质量/成本证据前不写书。

## Sandbox：具体已有覆盖，不等原型安全证明

[2512.12806v1](https://arxiv.org/html/2512.12806v1)实际§4.2–4.3、§6.2–6.4、§7.5：allowlist无快照、blacklist阻止、不确定变更用shutil复制快照；非零exit回滚、零exit提交。原型所谓COW是copy模拟，zero exit不授semantic postcondition。四类各20例全过只限80测试。pip baseline4.69s、原型6.51s，增加1.82s；原文14.5%与这两个分母不一致，**不采用14.5%**，250MB复制I/O应分账。Gemini CLI headless sign-in失效是auth setup，不作隔离反证。§7.5只本地文件，HTTP/email无法撤销；Saga/compensation为未来工作。

Owner `AGENT-TOOL-CALLING`，[Ch78](../../../../../books/part-07-agent/78-tool-calling.md)实际540–575：Preventive/Evidential Gate明确授权、effect及postcondition分责；staged view/flat store/override tree/journal段明确文件候选与commit，下一段明说已读秘密、网络/进程effect不可回滚、journal不证通用原子性。相邻[Ch81](../../../../../books/part-07-agent/81-workflow.md)290–335已解释COW/完整副本、mutation/compute成本和未捕获外部依赖barrier；Ch77 25–62明确memory不拥有环境事实。

**条件No Change/已有覆盖**仅针对本地rollback不等整个Agent安全完成与成本分账这条拟保留命题，具体正文确已承载；不是整篇所有实现已覆盖，不把原型100%变成长期安全证据。日期未授，当前最终Books为暂缓。

## DeliberationBench：选择器混杂保留

[2601.08835v1](https://arxiv.org/html/2601.08835v1)实际§3.1–3.3、§4.4、§5.4：270人工研究QA、五个较弱council模型，blind rank/rubric/defender三协议；baseline GPT-4o直接选五响应，v2B final也GPT-4o。pairwise评价GPT-4o与baseline selector重合，另Claude协议总体agreement68.4%，不是独立oracle自动消除混杂。三seed/两个温度、paired t-test不能把selector能力差异授为所有deliberation无效；任务只QA，不是代码/数学或强council普遍结论。

Owner `AGENT-MULTI-AGENT`，[Ch82](../../../../../books/part-07-agent/82-multi-agent.md)实际90–160：shared终态失独立oracle选择机会；配置/judge/候选池/预算共同冻结；Peer/Debate相关共识、oracle覆盖与可靠selector分别验收。相邻Ch81外部state/预算段已读，Ch83 25–60只protocol/host职责，不授协商策略。

**条件No Change/已有覆盖**仅针对“候选覆盖、聚合/选择器与最终评价不能合并归因”已被这些正文承载；本协议是局部反证，仍保留潜在贡献，不因为Books已覆盖排除。未日期授权，Books暂缓，不新增统一反协商结论。

## Memoria/Hindsight：排序不授事实

[2512.12686v1](https://arxiv.org/html/2512.12686v1)实际IV-E完整weight calculation、VI-A/B：age在全triplet归一到[0,1]再指数衰减，retrieved权重归一，引导LLM偏新；这不是自动fact revision。148条LongMemEval（70single、78update），GPT4.1-mini判分；同OpenAI embedding下single retrieval A-Mem 252s比Memoria260s更快，不能采memory全方面优越。全context平均115k tokens与399左右检索tokens不是相同信息预算；保留局部质量/成本取舍，不授幻觉消失。

[Hindsight12818v1](https://arxiv.org/abs/2512.12818v1)此轮只完整题摘，四类network与retain/recall/reflect尚不是已核实现或四网最优；不借Memoria局部代替它的Evidence。

Owner `AGENT-MEMORY`，[Ch77](../../../../../books/part-07-agent/77-memory.md)实际25–62区分derived memory/world reference与事实authority，170–235的score示意明确recency/relevance/confidence、紧接段明说recency高不等正确并要求time/source/supersession；return epoch、授权及整组覆盖另验。相邻Ch76 25–65：embedding/index不是source of truth与ingestion revision；Ch78 effect commit段实际已读。

**条件No Change/已有覆盖**针对recency优先仅为读取策略、不是durable事实更新的拟采用命题。不是声称Memoria所有图策略或Hindsight四网已覆盖；后者恢复日期后须核事实/信念写入和supersession机制，如出现未覆盖长期差额交root局部草案，当前不得整篇授已有覆盖。Books暂缓。

## 两项必要准入补读与一项关闭

[SignRAG12885v1](https://arxiv.org/html/2512.12885v1)实际III-A–D、IV-C：离线描述抽象变量、303项reference、VLM描述与位置、top5 code候选给LLM；scope/nonscope L2 KDE是局部threshold依据。100次latency平均3.99s、2.48–32.06s，作者明确不适合实时；保留representation/catalog选择与代价反证，不仅因为pipeline组合关闭，不授车载实时能力。

[SoT12777v1](https://arxiv.org/html/2512.12777v1)实际§3/3.1.1及完整§4–5：固定种子pure-function迭代，footnote明确KV是token可派生cache；Catalan中间值不唯一决定计算、加10编码反例使表面语义和计算用途分离。保留理论条件下计算状态不等完整解释的潜在增量，不冒称一般LLM已经采取该编码，不错误指责忽视KV。待Popper校准准入。

[Vision-enhanced LLM12595v1](https://arxiv.org/pdf/2512.12595v1)HTML失败后有限PDF替代成功；实际8页中§3.1–3.3、§5/§6 Tables1–2及ablation。共享token/bidirectional attention/rectified flow仍成熟描述，remeasurement未给具体objective/threshold新协议；FID、runtime及未明确image-quality ablation不能替代具体增量。贡献前关闭理由见ADMISSION，不将有利数字当Evidence，也不是因为正文取得费时而删。

[Annotation13714v1](https://arxiv.org/pdf/2512.13714v1)HTML失败后PDF成功；实际§3.1–3.5、§4.3–4.4与§5.1。多轮人审/weak supervision/ensemble/confidence与既有SFT/RL模块；SI/FC/AP/RDR的概念标签和数表没有新增可区分稳定性协议。具体贡献关闭而非评分关闭，不再为不影响处置的日期追查。

其余ADMISSION潜在家族只题摘完成；不从上述局部授全部Evidence。必要first-public恢复后按各自真实贡献评分/审阅，先保留全部潜在集合，未以工作量、缺全文或已有Books缩池。
