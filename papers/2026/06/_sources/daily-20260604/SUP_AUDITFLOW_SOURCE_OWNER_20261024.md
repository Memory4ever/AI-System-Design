# AuditFlow — necessary Source → owner / one-paragraph PRE

作者supp_20260604_author。R1准入/日期已过；2+1+2=5，具体gate差额深入必要域，非借金融范围泛收。

exact v1原件SUP_ABS/SUP_CORE_2606.03031v1_20261024.html完整；作者已必要读§3.1–3.6/4/5/Limitations及G明确内部冲突。采用：search可adaptive，terminal checks由typed deterministic environment持有，required-tool gate只接受每角色必需checks已返非错误receipt才收报告；senior disagreement只导向补证据，不代算核验。非LLM输出confidence自证。

评价67 FinMR案例、3DQC规则（sign/calctree/dim），static taxonomy与filing fact graph分离但依赖正确parse/tag/year。各role同backbone；standard compatible models temperature0，reasoning-family按AppE reasoning_effort=low且不传temperature，不能称全部greedy相同；junior20steps/4096out，senior8192out/3rounds；offline gpt5mini judge minimal/low/256tokens，最多8cases并发。v1去checks由82.09跌17.91只是受测protocol局部反侧；gate去掉74.63/invalid升，fusion去掉77.61。**无checker-only baseline**，不可断言多agent/LLM是不可替代核验来源；checker返回规则不等全artifact独立oracle。整output jointACC经LLMjudge，verdict与reported/expected值要分账。未核代码/复现。

G内部不一致作者定点确认：主文GPT55=55/67/82.09而其他三强=54/67/80.60，但G文称四强samecorrectness vector/ACC；T10 Fino31.34与12/67算术不符。只不采用这些跨backbone统计优越/精确CI，不因不采数字无限查全附录，也不消除局部checker反侧。AppE局部本地硬件已披露原话“on 8 GPU nodes with two NVIDIA A100 80GB GPUs”，torch2.9.0+cu128；句法节点/卡数含糊，不补总卡数。完整precision与各run服务配置矩阵未披露，不再笼统hardware Not Disclosed。硬件未作本次性能命题采用；图构建、全部role调用/checker、parser、judge/人工校验和重复运行均费。

Books context三文已读，唯一owner PLATFORM-EVALUATION-SYSTEM Ch66。actual4967“Domain Workflow可以编译为Deterministic Verifier”完整段讲专家spec→程序生成task/verdict及specbug/independentsolver，没有runtime report admission必须等required checker非错误证据的合同。已读完整前侧Native-runtime两段+marker与后侧Miscoverage段，不改其他知识。拟仅在26321整段/marker后、Miscoverage真H3前加下一段。

## PRE完整两侧与正文

上锚完整段：

人工编写少量 ERP 题目容易审计，却难覆盖约束组合；纯自然语言生成又会引入不可判定答案。Benchmark owner 可以把领域专家 specification 编译为 constraint optimization program，由同一版本的 generator 与 executable verifier 产生任务和判定。收益是扩大覆盖并保留可复算性，代价是 specification bug 会系统性污染数据；必须以人工 anchor、独立 solver 和版本化约束做交叉检查。exact-v1 只支持单一 ERP domain 与生成任务，不证明真实业务流程或跨域泛化。<!-- source-family:SF-2026-ARXIV-2605-26321 -->

拟增单段：

当模型负责在结构化环境中搜索证据时，还须让报告接受条件独立于模型的停止意愿：预先声明必需的 typed checks，只有它们返回非错误的规则与数据回执后才接受报告；缺项就返回明确的待取证需求，而不是由更多讨论替代计算。[一个受限核验分支](https://arxiv.org/html/2606.03031v1)将自适应搜索、确定性核算与报告聚合分责，去掉 checker 的反侧说明其局部收益不能全归给多 Agent。已调用且无错误不等规则完备、输入标签正确或完整 artifact 被独立证明；无 checker-only 对照、有限规则覆盖与模型 judge 仍限制归因。图与规范版本、检查回执和最终输出应可回指，解析、全部搜索/核算、聚合与独立审校均计费；规范或证据不可靠时保留 Unknown、固定检查与人工复核，不由共识或终态分数批准业务正确性。<!-- source-family:SF-2026-ARXIV-2606-03031 -->

下锚完整组：

### Miscoverage 要拆成 Sampling Failure 与 Selection Failure

只给最终 coverage 数字，会把候选集中没有正确项和 selector 选错混成同一故障。Evaluation owner 应分别估计有限采样失败，并在 calibration/exchangeability 条件下对 conditional selection 使用 conformal gate，再组合总体 bound。收益是为增加采样或改进 selector 指明责任，代价是校准集、额外样本与假设检查；分布漂移或相关自适应采样会破坏保证，应退回经验 risk-coverage 曲线或 abstain。exact-v1 仅支持论文的有限采样实验、conditional exchangeability 与 population-bound 假设，不是开放世界 truth guarantee。<!-- source-family:SF-2026-ARXIV-2605-27091 -->

Review note拟：`SF-2026-ARXIV-2606-03031`：2+1+2=5；exact-v1 §3–5/Limitations/G，required checker非错误receipt→report admission，模型只引导search；67case/3规则/LLMjudge、无checker-only与parse依赖/全部费用保留。G同vector文字/T10计数与主文冲突，不采用跨backbone统计优势，未核实现或复现。待实际写后复核。
