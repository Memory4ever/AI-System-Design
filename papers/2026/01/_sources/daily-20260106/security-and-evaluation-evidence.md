# Jan06 安全/评价必要证据（三）

下面均实际打开精确v1 HTML，题摘已独立初筛；不以安全/benchmark标签自动准入或自动深入全部附件。拟评分与Books判断待root核验，不是最终Daily Gate。

## [Defensive M2S 2601.00454v1](https://arxiv.org/html/2601.00454v1)

实际§3.1–3.6/4/5/Limitations与C2。新增是turn-only三格式与guard共同训练/测试的有条件效率/召回取舍，拟2+2+2=6安全深入。f(C)明确只取user，丢assistant responses；模板来自旧M2S，不当本篇首次。理论O(n²)→O(n)比较同时取消回复生成与n个incremental-prefix训练样本，不是同任务同训练协议的纯算子改进；93×含data generation不是训练walltime。

三8B guard，779训练/385unsafe394safe，≥8轮；QLoRA NF4/bf16 r16/alpha32/drop.1，batch4accum4/3epochs，A10040GB。SafeDial2037三seed Table1 Nemotron full99→numberize87.8、Llama75.1→hyphen24.1，Qwen54.9→hyphen93.8；不是所有model格式占优。Longturn195的98% recall/FPR1.1来自Llama单seed，不证明SafeDial同FPR。p=.12非等效证明；B1 Qwenhyphen seeds1/2/3与主文42/123/456不同，数字不升级统计普适结论。未测试知晓压缩的adversary，loss of context可能丢原模型已经comply的信号；unsafe substring parser有接口依赖，未复现/未授生产。

实际Ch77 1146–1156承载safety summary不扩权限/当前evidence/压缩误报；Ch72 inspection-window/downstream身份及比例稀释之后，角色投影/format/guard联合版本与同模型模板回归的具体边界经root必要核授权窄写。Ch72实际1967/1969两段及2998注已通过root actual POST，锁释放，不采93×walltime或p=.12等效。

## [Right for Wrong Reasons 2601.00513v1](https://arxiv.org/html/2601.00513v1)

实际Methodology/Results/Discussion/Limitations以及A/B/C必要范围；拟2+2+2=6评价反证。RIS三值step标签/平均/阈值.8测显式trace质量，oracle RAG不等真实retrieval，human truth未校准，correlation不识别pseudo-reflection内部机制。10,734 traces、三7–8B模型三任务不能定义“所有小于10B不能自省”的capacity阈值。

中心identity冲突：主文三judge GPT4omini/Claude3.5/Gemini1.5、greedyT0、5-layer/391feature MLP；Appendix B/C称DeepSeekV3.1/Gemini2.5FlashLite、provider defaultT.7–1、4-layer不同网络。Self-critique主文两轮与appendix single-prompt表述也不同。κ=.657、F1=.86、100×及50–69%等不能据不一致协议当正面校准/安全发生率。精确v1可读，不是材料访问受阻；拟保中心争议、要求唯一run config/judge/prompt/sampling/modelsplit与对应结果/label校准后重开，不写Books纠错章节里没有的错误。

现Ch66 110标签粒度/rubric proxy、363–376真实process trace与outcome分账、1166–1171 graph非思维读出已足以承载稳定谨慎原则；本篇不一致评价不能增加正面保证。root实际主文与A/B/C的judge、binary/ternary标签、sampling和网络配置独立核通过中心争议隔离；self-critique是单prompt追加，不采用两阶段同预算。重开只需唯一run/config、label定义/校准、对应结果，不写Books已有论证中没有的错误。

## [MAESTRO 2601.00481v1](https://arxiv.org/html/2601.00481v1)

实际§3.1.1/3.1.2/4.1/4.3/5.1与A2.2，精确原段缓存core-2601.00481v1-selected.json。拟2+2+2=6：框架统一telemetry schema不证明字段真的暴露；provider/transport/framework可各层丢token metadata，generation/embedding与stream/nonstream不同，missing不能当低usage。12实例≥20runs、10mincap，architecture suite8192token上限，Gemini2.5Flash模拟user、gpt4omini judge；hardware/precision=Not Disclosed（provider）。

edge-set Jaccard平均.86而ordered LCS.65只说明这些run结构与时序不同，两个emptygraph Jaccard0、emptysequence LCS1的约定需保，不能自动诊断异常；framework/架构/suite差异未作普遍因果控制。只有predefined instances、有限可调参数，profiling有overhead且没有生产SLO保证。root已定点核原source与Ch69字段availability gap并授权窄写，实际67/69两段与334注POST通过，锁释放，不把统一wrapper当production portability。

## [JourneyBench 2601.00596v1](https://arxiv.org/html/2601.00596v1)

实际§2/3/4/7/K的必要范围，原段缓存core-2601.00596v1-selected.json。拟2+2+2=6：workflow adherence与tool/参数/outcome分责，SOP graph固定branch responses、缺参数/函数失败三扰动；DPA每node prompt+tool exposure改变，而SPA全SOP，不能唯一归因model大小。三SOP由5expert unanimous10→4→3，703conversations/40turn cap/defaulttemperature，GPT4o模拟user；模型版本精确日期、hardware/precision、重复seed=Not Disclosed。

UJCS在工具序列任何missing/extra/misorder时先归0，再参数命中；仅目标path，不认证所有合法异步路径/真实工具effect。相同UA rubric/LLM judge realism非生产代表性证明；原文确有simulator凭空补input或提前终止，不能都归Agent失败。评价$388.88限制model范围，不外推小模型通用优势。

实际Ch81 880–938 passing trace/induced acceptance/authorized workflow三对象、deterministic invariants与probabilistic scenario分账；Ch66 363–376 simulator/oracle与合法路径反例可承载拟稳定命题。root已实际必要graph/metric/DPA/simulator与当前上述正文对读通过具体已有覆盖，无共享Books修改。数据身份为703 datapoints、41 tools；未称7033，也未把模拟交互等同真实工具副作用。
