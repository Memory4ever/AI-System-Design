# MemArchitect 18330：必要原证与具体 No Change 提案

作者 resume_mar18，仅03-21补BJT03-20，不自授独立Source/NC/DAY。题摘准入已由root在受影响65集合中通过；本packet供非准备者必要核，不写Books。

## 身份、日期与拟采用命题

[官方 exact-v1](https://arxiv.org/abs/2603.18330v1)、[原HTML](https://arxiv.org/html/2603.18330v1)。当前history只有v1，comment为ongoing research，不见正式先稿、撤回或纠错事件标记，不授全版本/作者历史审计。[官方DataCite](https://api.datacite.org/dois/10.48550/arXiv.2603.18330)实际created03-20T02:10:07.000Z、registered03-20T02:10:08.000Z、statefindable、published2026；v1Submitted03-18T22:37:05Z、Updated03-20T00:21:23Z、Available2026-03。与本日官方announcement流程/同批公开夹证支持BJT03-20有限arXiv归属，不以Submitted当公开时刻或证明其他入口从未先稿。

拟评分2+1+2=5：单memory组件中read ranking、输出使用反馈与background retention三个路径分开，用policy-state管理上下文候选而不改模型weights；少读/遗忘与事实保存发生明确取舍。不给借用FSRS/Kalman/通用治理原则、隐私宣传或跨两模型数量新分。原§3/T1反侧足以反驳“治理总更好”广告，却不为已知Ch77过剪边界再计DD3。

## 必要 Source 实际范围与限制

实际 exact-v1 §2.1–2.2、§3.1–3.2/Table1、§4、AppendixA.1–A.4/Eqs1–9与B.1–B.3；支持机制、主要评价配置与直接反侧足够停止，不核代码/实验复现、全venue/版本diff。

- Read：query分类→调整similarity / retrievability / utility权重→crossencoder筛相关→共检索co-occurrence扩张→token预算。Reflect：输出word-overlap heuristic估计是否使用某memory，更新Kalman U与FSRS S；Background：gzip压缩比例proxy触发，将低R物理删除、中R汇总。R是借用flashcard曲线的规则状态，不是实际用户未来recall概率；gzip比例不是语义熵/完整性证明。Eq7 fact的lambda0只免**读取排序**中的age penalty，不豁免A.1后台物理prune，不能凭“facts timeless”保证保留。
- Output使用不等事实正确或单条因果贡献：A.2把usage heuristic交给utility，不给independenttruth label；论文“hallucinations mathematically downweighted”与“True Utility”措辞未由该信号支持。Crossencoder标entailment未给独立calibration/可靠过滤证据，co-occurrence也不是逻辑依赖或truth；不采那些精确阈值保证。
- A.2 conflict resolver与A.4toxicity write-filter / right-to-forgotten cascade均标**Planned**，不能授已经实现隐私、冲突解决或防注入。无实施不可得本身不让整个接口EX；不把计划当当前证据。
- Table1不是同一固定model/evaluator下三backend全交叉。B.1作者声明Llama3.1-8BInstruct/BGE-M3/同MemOS脚本、同Llama judge；B.2是Qwen2.5-3BInstruct/nomic-embed-v1.5/同SimpleMem脚本、同Qwenjudge。LoCoMo10 1986QA。Qwen四项较SimpleMem高，Llama single74→53.2、temporal72→27.1反退，multi36→40.1、open45→56.3；不跨这两个model/evaluator把差额平均当统一架构因果。作者将temporal退步归过剪，但没有逐policy干预证明唯一归因，也未测真实长期漂移/线上安全。hardware/precision/inputoutput/batch/concurrency/SLO/独立repeat/CI及全费用均Not Disclosed，使用LLMjudge不是独立truth。
- 原Table1八行baseline均值由数字得62.0375、系统69.4875，仅表内无权平均；按category样本加权意义未闭合。§4“governance preserves semantic integrity”不能由聚合高分盖住直接退步。读classifier/decompose/crossencoder、usage检测、embedding、图维护、KV/context、合并与删除都付费；论文未给matchedtoken/fullbudget，不能授更高效率或deployment能力。

## Actual sole owner 与具体已有覆盖提案

`AGENT-MEMORY` / [Ch77](../../../../../books/part-07-agent/77-memory.md)。实际已读298–336、1289–1414、1520–1567与669–678；Ch76/78开篇分责复用本日已实际上下文。

1. 298–323明确fact-state与retrieval-policy-state分开；312–315rawstore持truth/ACL/freshness/retention/deletion，proxy只排序；317–323utility反馈不等单entry因果、rare evidence前过滤无法恢复、需recall/outcome/drift/fallback分账。这真正承载read/reflect接口，不是只映射memory标题。
2. 1545已经active→dormant→retired、原因/依赖/可逆窗与不可逆法定清理分开；1558已经选择性写入漏低频事实，需要可恢复archive/periodicaudit；1560已有write/retain/retrieve/revise/delete分责、feedback与治理commit分开，低规模/稳定规则优先deterministicpolicy。因此本文规则套件是现有控制接口的实例，不强加FSRS、Kalman名称或未经校准的参数。
3. 1311–1321已有acquisition/retention/forgetting/transfer与下游费用分验，1343冻harness并报告protected-slice退化，1349实际resolver误删/保留和损害证据；1547交叉固定construction/retrieval，不把aggregate高分作为治理充分性。本文两个model/evaluator下收益与过剪反侧支持此现有边界，不是已有原文称“总更好”待纠错。
4. 669–678已有consolidatedmemory派生索引、保raw/provenance/版本/回滚且不得改变Workflow权限；1389–1414已有authorization/gradedtrust/actiongate分开，保留planned隐私/冲突事实与usage≠truth限制。不能因为正文没有精确“R(t)”而强造diff。

作者建议标准Source完成后以**具体No Change**闭合有限可采用命题，不给未证实治理安全/总效率正面Evidence；Table1过剪与planned安全边界入日报，不伪称完全复现或POST。若非准备者认为某个新机制真实未承载，应指出具体原命题再最小PRE，不能把NC当缩池/删中心反证理由。本packet待root独核裁定，不先计safe。

## root 非准备者必要证据与具体 NC 裁定

2026-10-11，root 已实际打开精确 v1 §2.1–2.2、§3/Table1、§4、A.1–A.4/B.1–B.3，官方 v1 身份与有限 DOI 字段；实际读 Ch77 Fact State/Retrieval-policy State 的298–323、harness/protected-slice与resolver真实误删段、active/dormant/retired及共享 memory 控制段，邻章 Ch76/78开篇分责。有限 **PASS**，保持2+1+2=5；接口与过剪/反馈误当真值的设计边界确由现有正文承载，不写一组未经验证的FSRS/Kalman阈值以制造diff。

实际 Table1/B 配置支持两组不同 backbone/embedding/judge 下的受限比较，而非三 backend 全交叉或统一总体优势。Llama temporal72→27.1与single74→53.2反侧必须留在日报；使用反馈与共现只支持策略状态，不认证事实、单 entry 因果、完整性或隐私。后台按R物理清除并不因读取时fact λ=0被豁免；conflict/toxic/right-to-forgotten为Planned。保留未披露运行配置、重复/CI与全费用，不采用“mathematically downweight hallucination”“语义保真总更好”等宣传。该具体NC不是来源无法读取后的缩池、也不是实际写后POST；不替代最终六部分DAY。
